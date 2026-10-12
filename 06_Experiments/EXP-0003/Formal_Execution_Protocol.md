# EXP-0003 Formal Execution Protocol (proposal, not authorized)

This is an **unexecuted implementation protocol**, not a formal Run or an
approved/preregistered Plan. It does not authorize anything, promote Evidence,
select METHOD-0002, or change experiment status.

## Scope of the project-lead's budget decision

On **2026-10-12**, the project lead explicitly approved **120 seconds TOTAL
wall time across up to two complete formal EXP-0003 test repetitions**, not
120 seconds per repetition. This approval concerns the budget interpretation
only. Numerical thresholds, FFT/sparse settings, Plan freeze, code revision
and formal execution remain **unapproved**.

The remaining resource proposal is CPU-only, two threads maximum, and a
2 GiB RLIMIT_AS virtual-address-space cap applied to each test process.
RLIMIT_AS is not the same as peak RSS and may cause PyTorch imports to fail;
any such failure must be preserved, never worked around silently.
The shared deadline begins before fixture hashing and includes preparation
between repetitions. Final artifact packaging is permitted after that
deadline solely to preserve outcomes, not to execute additional tests.

## Prerequisites before ANY formal execution

1. Project-lead approval of the entire EXP-0003 Plan including numerical
   gates, seed, FFT convention, sparse policy, code/config/environment,
   artifact requirements and separate authorization to execute.
2. Explicitly record `experiment_state: preregistered` and
   `approval_status: approved` plus nonblank `approval_ref` and
   `formal_execution_authorization_ref` in `Plan.md`. Never infer those
   approvals from the 120-second budget decision.
3. The frozen `tools/fd_nig_config.json` must have `status: frozen`,
   `approval_status: approved`, `tolerances.status: approved` and matching
   nonblank approval and formal execution references.
4. Reserve a unique `RUN-EXP-0003-NNN` in append-only `Run_Log.md` and
   independently review the exact committed branch, suite, and environment.
5. Confirm the suite covers every Plan gate. The launcher's structural
   approval check does **not** replace scientific review.

**At the current PR revision the launcher rejects execution** because the
Plan and config remain unapproved.

## Proposed future launch (DO NOT RUN BEFORE FORMAL AUTHORIZATION)

From the repository root with the provisioned CPU-only environment:

~~~bash
/workspace/fd-nig-venv/bin/python \
  06_Experiments/EXP-0003/run_formal_protocol.py \
  --execute \
  --run-id RUN-EXP-0003-NNN
~~~

Replace the placeholder with the actual reserved Run ID. The launcher
resolves the repository root from its own location; by default it stores
Run artifacts **outside the Git repository**, in a sibling directory.

The script refuses to execute without Plan/config approvals and matching
approval/execution authorization references. It also validates the budget,
seed, grid, FFT/pair-policy declarations, branch, interpreter and clean
tracked worktree. Running without `--execute` is refused.

## Shared-time execution and stopping conditions

- The launcher sets **one 120-second monotonic deadline** for both complete
  test repetitions, including fixture serialization and between-run overhead.
  It never resets the deadline.
- Each subprocess has a **2 GiB RLIMIT_AS** memory cap and runs on CPU with
  `OMP_NUM_THREADS=2` and `MKL_NUM_THREADS=2`.
- The complete test module is attempted at most twice. A failed, timed-out
  or incomplete first attempt stops execution, without retrying.
- The second attempt uses the **remaining** total budget. Both attempts
  must have zero failures, errors and skips; each must produce JUnit XML.
- Both successful attempts must have the same test identifiers. A
  time/memory/protocol failure is **not** scientific proof of a wrong formula.
- The maximum total of 120 seconds refers to execution work, not any later
  archiving needed to preserve logs after a failure.

## Non-overwriting artifacts and provenance

The launcher exclusively creates the Run directory named by the reserved
`RUN-EXP-0003-NNN`; attempting to reuse that name fails. Within it:

- `attempt-01/stdout.log`, `stderr-and-resource.log`, `junit.xml` (if produced)
  and `status.json`;
- the corresponding files in `attempt-02/`, only if the first attempt passes;
- `provenance.json` recording the exact commit/branch, interpreter and
  versions, cgroup limits, input SHA-256 hashes, approvals and budget;
- `fixture.json` recording the deterministic synthetic fixture hash;
- `summary.json` recording outcomes, test-ID agreement and shared elapsed time.

Each attempt stores its independent exit status, elapsed time, timeout flag,
test identifiers and JUnit result, stdout/stderr hash and resource log.
Never overwrite a prior attempt, hide failures, alter thresholds post hoc,
or promote these results to verified Evidence.

After an authorized run, `Run_Log.md` is append-only and must link its
reserved Run ID to the command, code/config/fixture hashes, artifacts, UTC
timestamps, environment, results, deviations and any incomplete attempts.

## Remaining limitations

- These files were changed **statically only**. The runner and revised
  test suite have not been executed or validated in the Cloud runtime.
- Numerical tolerances and other Plan settings still require review and
  formal approval, independently of the approved 120-second budget.
- No Wiki projection is needed: these are administrative execution
  controls, not new human-readable scientific findings.
