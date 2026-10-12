# EXP-0003 Formal Execution Protocol (proposal)

This is a reproducibility protocol, not an approval or a run record. It does not change `experiment_state` or `approval_status`.

## Preconditions

- Project lead approval of the Plan's proposed numerical settings and formal execution.
- Clean checkout of `task/fd-nig-verification` at the recorded commit.
- CPU-only Python environment with the pinned PyTorch and pytest versions.
- No MetalSet, training, or external simulator inputs.

## Bounded command

From the repository root, use the isolated environment and capture all output:

```bash
set -o pipefail
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 PYTHONHASHSEED=20261011
mkdir -p artifacts/EXP-0003
/usr/bin/time -v timeout --signal=KILL 120s bash -c \
  'ulimit -v 2097152; /workspace/fd-nig-venv/bin/python -m pytest tools/tests/test_fd_nig_synthetic.py -q' \
  > artifacts/EXP-0003/stdout.log 2> artifacts/EXP-0003/stderr-and-resource.log
status=$?
printf '%s\n' "$status" > artifacts/EXP-0003/exit_status.txt
exit "$status"
```

Run the complete command at most twice, recording each attempt separately. A timeout, non-zero exit, memory failure, missing dependency, or incomplete artifact set is a failed attempt and must be retained.

## Required provenance and report fields

Record commit SHA, branch, UTC timestamp, Python executable/version, PyTorch/pytest versions, CPU quota, memory limit, thread environment, command, exit status, wall time, peak RSS, stdout/stderr hashes, fixture/config hashes, and per-test results. Do not rewrite a failed attempt or present calibration output as a formal result.

All tolerance values remain proposal settings until explicitly approved; this protocol does not freeze them.
