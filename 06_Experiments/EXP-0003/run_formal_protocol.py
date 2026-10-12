#!/usr/bin/env python3
"""Guarded, proposal-only EXP-0003 launcher. Do not run before full approvals.

Two complete pytest repetitions share ONE 120-second monotonic deadline.
Every attempt receives a separate, never-overwritten artifact directory.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import io
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "06_Experiments" / "EXP-0003"
PLAN = EXPERIMENT / "Plan.md"
CONFIG = ROOT / "tools" / "fd_nig_config.json"
TEST_PATH = "tools/tests/test_fd_nig_synthetic.py"
DEFAULT_PYTHON = Path("/workspace/fd-nig-venv/bin/python")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def plan_field(contents: str, name: str) -> str:
    match = re.search(r"^" + re.escape(name) + r":[ \t]*(.*)$", contents, re.M)
    return (match.group(1).strip("\"'") if match else "").strip()


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def require_approval(config: dict, plan_text: str) -> None:
    # Reading an unapproved Plan MUST make this launcher refuse to execute.
    if plan_field(plan_text, "id") != "EXP-0003":
        raise RuntimeError("wrong experiment plan")
    if plan_field(plan_text, "experiment_state") != "preregistered":
        raise RuntimeError("experiment is not preregistered")
    if plan_field(plan_text, "approval_status") != "approved":
        raise RuntimeError("experiment Plan is not approved")
    if config.get("status") != "frozen" or config.get("approval_status") != "approved":
        raise RuntimeError("configuration is not approved/frozen")
    if config.get("tolerances", {}).get("status") != "approved":
        raise RuntimeError("numerical tolerances have not been approved")
    if (plan_field(plan_text, "numerical_memory_freeze_status") != "approved"
            or config.get("numerical_memory_freeze_status") != "approved"
            or config.get("numerical_memory_freeze_ref") !=
               plan_field(plan_text, "numerical_memory_freeze_ref")):
        raise RuntimeError("numerical and memory freeze approval is missing or mismatched")
    for key in ("plan_approval_ref", "formal_execution_authorization_ref"):
        value = config.get(key)
        if not isinstance(value, str) or not value.strip():
            raise RuntimeError(f"missing explicit {key}")
        if value != plan_field(plan_text, "approval_ref" if key == "plan_approval_ref"
                               else "formal_execution_authorization_ref"):
            raise RuntimeError(f"mismatched approval reference: {key}")
    budget = config.get("compute_budget", {})
    if (budget.get("device") != "cpu"
            or budget.get("wall_seconds") != 120
            or budget.get("wall_scope") != "both-repetitions-total"
            or budget.get("max_repetitions") != 2
            or budget.get("memory_gb") != 2
            or budget.get("memory_metric") != "peak-process-tree-rss"
            or budget.get("watchdog_stop_mib") != 1536
            or budget.get("watchdog_sample_ms") != 100
            or budget.get("enforcement") != "userspace-proc-rss-watchdog"
            or budget.get("kernel_memory_limit_enforced") is not False):
        raise RuntimeError("unreviewed or inconsistent resource budget")
    if (config.get("experiment") != "EXP-0003"
            or config.get("method") != "METHOD-0002"
            or config.get("seed") != 20261011
            or config.get("grid") != {"height": 16, "width": 16, "circular": True}
            or config.get("fft") != {"order": "native-unshifted", "normalization": "backward"}
            or config.get("pair_policy") != {"reference": "all", "sparse_count": 256,
                                               "order": "lexicographic"}):
        raise RuntimeError("unreviewed changes to the synthetic contract")


def fixture_digest(config: dict) -> str:
    # Hash actual deterministic fixture tensors, with no NumPy dependency.
    # Include dtype, shape, field names, and serialized tensor bytes.
    sys.path.insert(0, str(ROOT))
    import torch
    from tools.fd_nig_reference import make_fixture

    fixture = make_fixture(
        seed=config["seed"], height=config["grid"]["height"],
        width=config["grid"]["width"],
    )
    serial = io.BytesIO()
    torch.save({key: getattr(fixture, key) for key in (
        "mask", "spectrum", "pairs", "coefficients",
        "hermitian_coefficients", "target",
    )}, serial)
    return hashlib.sha256(serial.getvalue()).hexdigest()


def proc_rss_bytes(pid: int) -> int:
    """Linux /proc VmRSS in bytes; missing/unreadable data fail closed."""
    text = Path(f"/proc/{pid}/status").read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("VmRSS:"):
            fields = line.split()
            if len(fields) != 3 or fields[2] != "kB":
                raise RuntimeError(f"unreadable RSS units for pid={pid}")
            return int(fields[1]) * 1024
    raise RuntimeError(f"VmRSS unavailable for pid={pid}")


def proc_children(pid: int) -> list[int]:
    contents = Path(f"/proc/{pid}/task/{pid}/children").read_text(encoding="utf-8")
    return [int(part) for part in contents.split()]


def process_tree_rss_bytes(child_pid: int) -> int:
    """Conservatively sum parent + live test descendants, counting shared RSS."""
    total = proc_rss_bytes(os.getpid())
    visited: set[int] = set()
    pending = [child_pid]
    while pending:
        pid = pending.pop()
        if pid in visited:
            continue
        visited.add(pid)
        try:
            # Enumerate children before obtaining VmRSS to reduce missed forks.
            pending.extend(proc_children(pid))
            total += proc_rss_bytes(pid)
        except FileNotFoundError:
            # A process exiting during measurement is harmless; the
            # /usr/bin/time -v peak remains a secondary post-run check.
            continue
    if child_pid not in visited or len(visited) <= 1:
        # Parent RSS has still been checked even if no descendants exist.
        return total
    return total


def group_kill(process: subprocess.Popen) -> None:
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait()


def time_max_rss_kib(stderr_path: Path) -> int | None:
    for line in stderr_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if "Maximum resident set size (kbytes)" in line:
            try:
                return int(line.rsplit(":", 1)[1].strip())
            except (ValueError, IndexError):
                return None
    return None


def cgroup_value(path: str) -> str | None:
    try:
        return Path(path).read_text().strip()
    except OSError:
        return None


def write_json_new(path: Path, value: object) -> None:
    with path.open("x", encoding="utf-8") as output:
        json.dump(value, output, indent=2, sort_keys=True)
        output.write("\n")


def execute_attempt(run_dir: Path, index: int, python: Path,
                    deadline: float, env: dict) -> dict:
    attempt_dir = run_dir / f"attempt-{index:02d}"
    attempt_dir.mkdir(mode=0o700, exist_ok=False)
    stdout_path = attempt_dir / "stdout.log"
    stderr_path = attempt_dir / "stderr-and-resource.log"
    junit_path = attempt_dir / "junit.xml"
    command = ["/usr/bin/time", "-v", str(python), "-m", "pytest",
               TEST_PATH, "-q", f"--junitxml={junit_path}"]
    started = time.monotonic()
    remaining = deadline - started
    record = {
        "attempt": index,
        "start_utc": utc_now(),
        "command": command,
        "remaining_budget_seconds_at_start": remaining,
        "environment": {k: env[k] for k in (
            "OMP_NUM_THREADS", "MKL_NUM_THREADS", "PYTHONHASHSEED",
            "CUDA_VISIBLE_DEVICES",
        )},
    }
    timed_out = remaining <= 0
    return_code = None

    with stdout_path.open("x") as out, stderr_path.open("x") as err:
        if remaining > 0:
            process = subprocess.Popen(
                command, cwd=ROOT, env=env, stdout=out, stderr=err,
                start_new_session=True, preexec_fn=limits,
            )
            try:
                return_code = process.wait(timeout=remaining)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(process.pid, signal.SIGKILL)
                return_code = process.wait()
        else:
            err.write("Total 120-second deadline exhausted before this attempt.\n")

    record["end_utc"] = utc_now()
    record["elapsed_seconds"] = time.monotonic() - started
    record["exit_code"] = return_code
    record["timed_out"] = timed_out
    record["sha256"] = {
        p.name: digest(p) for p in (stdout_path, stderr_path)
    }
    test_ids = []
    test_results = []
    xml_problem = None
    if junit_path.is_file():
        record["sha256"][junit_path.name] = digest(junit_path)
        try:
            xml = ET.parse(junit_path).getroot()
            cases = list(xml.iter("testcase"))
            for case in cases:
                test_id = f'{case.get("classname", "")}.{case.get("name", "")}'
                test_ids.append(test_id)
                failure = case.find("failure")
                error = case.find("error")
                skipped = case.find("skipped")
                status = ("failure" if failure is not None else
                          "error" if error is not None else
                          "skipped" if skipped is not None else "passed")
                test_results.append({"id": test_id, "status": status,
                                     "duration_seconds": case.get("time")})
            record["test_count"] = len(cases)
            record["failures"] = sum(case.find("failure") is not None for case in cases)
            record["errors"] = sum(case.find("error") is not None for case in cases)
            record["skipped"] = sum(case.find("skipped") is not None for case in cases)
        except ET.ParseError as exc:
            xml_problem = str(exc)
    else:
        xml_problem = "JUnit XML was not produced"
    record["junit_parse_error"] = xml_problem
    record["test_ids"] = test_ids
    record["test_results"] = test_results
    record["passed"] = (
        not timed_out and return_code == 0 and xml_problem is None
        and len(test_ids) >= 8 and record["failures"] == 0
        and record["errors"] == 0 and record["skipped"] == 0
    )
    write_json_new(attempt_dir / "status.json", record)
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true",
                        help="Must be accompanied by an approved Plan/config and authorization refs.")
    parser.add_argument("--run-id", required=True,
                        help="Approved immutable RUN-EXP-0003-NNN identifier; reserve it in Run_Log first.")
    parser.add_argument("--python", type=Path, default=DEFAULT_PYTHON)
    parser.add_argument("--output-root", type=Path,
                        default=ROOT.parent / "fd-nig-exp0003-results")
    args = parser.parse_args()

    if not args.execute:
        parser.error("execution is disabled by default; use --execute only after formal authorization")
    if not re.fullmatch(r"RUN-EXP-0003-[0-9]{3}", args.run_id):
        parser.error("--run-id must be a reserved RUN-EXP-0003-NNN identifier")
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    plan_text = PLAN.read_text(encoding="utf-8")
    require_approval(config, plan_text)
    if not args.python.is_file():
        raise RuntimeError(f"missing approved Python environment: {args.python}")
    if Path(sys.executable).resolve() != args.python.resolve():
        raise RuntimeError("invoke this runner with the same approved Python interpreter")
    if not Path("/usr/bin/time").is_file():
        raise RuntimeError("required /usr/bin/time is unavailable")
    if git("status", "--porcelain", "--untracked-files=no"):
        raise RuntimeError("tracked Git worktree has uncommitted changes")
    revision = git("rev-parse", "HEAD")
    branch = git("branch", "--show-current")
    if branch != "task/fd-nig-verification":
        raise RuntimeError(f"unexpected branch: {branch}")
    log_path = EXPERIMENT / "Run_Log.md"
    if not log_path.is_file():
        raise RuntimeError("no append-only Run_Log.md reservation exists")
    reserved = re.search(
        r"(?m)^##[ 	]+" + re.escape(args.run_id) + r"[ 	]+\(reserved\)[ 	]*$",
        log_path.read_text(encoding="utf-8"),
    )
    if not reserved:
        raise RuntimeError("Run ID has not been explicitly reserved in Run_Log.md")

    output_root = args.output_root.resolve()
    if output_root == ROOT or ROOT in output_root.parents:
        raise RuntimeError("run artifacts must be stored outside the Git worktree")

    run_id = args.run_id
    output_root.mkdir(parents=True, exist_ok=True)
    run_dir = output_root / run_id
    run_dir.mkdir(mode=0o700, exist_ok=False)

    provenance = {
        "experiment": "EXP-0003",
        "formal_run_id": run_id,
        "created_utc": utc_now(),
        "git_commit": revision,
        "branch": branch,
        "python": str(args.python),
        "python_executable": sys.executable,
        "python_version": sys.version,
        "torch_version": importlib.metadata.version("torch"),
        "pytest_version": importlib.metadata.version("pytest"),
        "cpu_quota_cgroup_v2": cgroup_value("/sys/fs/cgroup/cpu.max"),
        "memory_limit_cgroup_v2": cgroup_value("/sys/fs/cgroup/memory.max"),
        "input_sha256": {str(p.relative_to(ROOT)): digest(p) for p in (
            PLAN, CONFIG, EXPERIMENT / "Formal_Execution_Protocol.md",
            EXPERIMENT / "run_formal_protocol.py",
            ROOT / "tools" / "fd_nig_reference.py",
            ROOT / "tools" / "fd_nig_aggregation.py",
            ROOT / TEST_PATH,
        )},
        "budget_seconds_total": 120,
        "budget_scope": "both-complete-repetitions-total",
        "memory_budget_metric": "peak-process-tree-rss",
        "memory_limit_bytes": 2 * 1024 ** 3,
        "rss_early_stop_bytes": 1536 * 1024 ** 2,
        "rss_sample_period_seconds": 0.1,
        "memory_enforcement": "userspace-watchdog-non-kernel-hard",
        "cgroup_memory_events_at_start": cgroup_value("/sys/fs/cgroup/memory.events"),
        "plan_approval_ref": config["plan_approval_ref"],
        "formal_execution_authorization_ref": config["formal_execution_authorization_ref"],
    }
    write_json_new(run_dir / "provenance.json", provenance)
    env = os.environ.copy()
    env.update({
        "OMP_NUM_THREADS": "2",
        "MKL_NUM_THREADS": "2",
        "PYTHONHASHSEED": str(config["seed"]),
        "CUDA_VISIBLE_DEVICES": "",
    })
    # The deadline covers fixture serialization and the two repeated test suites.
    start = time.monotonic()
    deadline = start + 120
    records = []
    try:
        fixture_hash = fixture_digest(config)
        write_json_new(run_dir / "fixture.json", {
            "fixture_sha256_torch_serialization": fixture_hash,
            "seed": config["seed"],
            "grid": config["grid"],
        })
        for index in (1, 2):
            record = execute_attempt(run_dir, index, args.python, deadline, env)
            records.append(record)
            if not record["passed"]:
                break

    except Exception as exc:
        records.append({"failed_in_runner": repr(exc), "at_utc": utc_now()})
    same_test_ids = (
        len(records) == 2
        and records[0].get("test_ids") == records[1].get("test_ids")
    )
    summary = {
        "experiment": "EXP-0003",
        "same_test_ids_across_repetitions": same_test_ids,
        "run_id": run_id,
        "attempts": records,
        "total_elapsed_seconds": time.monotonic() - start,
        "passed": len(records) == 2 and same_test_ids and all(x.get("passed") for x in records),
        "completed_utc": utc_now(),
    }
    write_json_new(run_dir / "summary.json", summary)
    print(json.dumps({"run_dir": str(run_dir), "passed": summary["passed"],
                      "attempts": len(records), "elapsed": summary["total_elapsed_seconds"]}))
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
