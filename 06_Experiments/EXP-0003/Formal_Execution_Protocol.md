# EXP-0003 Formal Execution Protocol (proposal, not authorized)

This is an **unexecuted implementation protocol**, not a formal Run or an
approved/preregistered Plan. The numerical and monitored-RSS acceptance
settings have been explicitly **frozen by the project lead on 2026-10-12**,
but that scope-limited approval does **not** authorize a formal run,
promote Evidence, select METHOD-0002, or change experiment approval status.

## Scope of the project-lead's budget decision

On **2026-10-12**, the project lead explicitly approved **120 seconds TOTAL
wall time across up to two complete formal EXP-0003 test repetitions**, not
120 seconds per repetition. In a separate decision on **2026-10-12** the
project lead also approved and froze the exact numerical gates,
seed/FFT/pair policy and monitored-RSS memory policy documented in
`Numerical_and_Memory_Freeze_Review.md`. **The complete Plan, code
review and formal execution remain unapproved**.

The frozen resources are CPU-only, two threads maximum,
peak **process-tree RSS <= 2 GiB** including runner and test descendants,
and a userspace `/proc` watchdog sampling at <=100ms intervals. If monitored
RSS reaches **1536 MiB**, or RSS measurement fails during an active child,
kill the test process group, preserve failure artifacts and do not retry.
`RLIMIT_AS` is **not used**: a virtual-address limit is not peak RSS.
The watchdog does **not** provide a strict kernel-enforced RSS limit;
`/usr/bin/time -v` maximum RSS and cgroup memory events are also logged.
If measured RSS exceeds 2 GiB, the attempt fails independently of the
watchdog. The shared deadline begins before fixture hashing and includes
preparation between repetitions. Final artifact packaging is permitted
after that deadline solely to preserve outcomes, not additional tests.

## Prerequisites before ANY formal execution

1. The numerical gates, seed/FFT/pair policy and monitored-RSS memory rule
   are approved and frozen (2026-10-12). **Still required:** independent
   validation/review of code, the exact frozen commit/environment, artifact
   requirements, the complete Plan, and separate authorization to execute.
2. Explicitly record `experiment_state: preregistered` and
   `approval_status: approved` plus nonblank `approval_ref` and
   `formal_execution_authorization_ref` in `Plan.md`. Never infer those
   approvals from the 120-second budget decision.
3. The numerical/fixture/memory parts of `tools/fd_nig_config.json`
   already have `status: frozen` and `tolerances.status: approved`.
   The formal `approval_status` remains `not_requested`. Only after
   a separate full-Plan authorization may it become `approved` with
   matching nonblank approval and execution references.
4. Reserve a unique `RUN-EXP-0003-NNN` in append-only `Run_Log.md`
   with an exact heading such as `## RUN-EXP-0003-001 (reserved)` and
   independently review the exact committed branch, suite, and environment.
   The launcher refuses to start if the reservation is absent or mismatched.
5. Confirm the suite covers every Plan gate. The launcher's structural
   approval check does **not** replace scientific review.
6. Independently approve the exact **final** executable commit SHA and preserve
   a revision approval record **outside** the repository checkout. The
   `--approved-revision-record` argument is mandatory: the runner refuses to
   start if this record is absent, inside the checkout, malformed, or does not
   identify the checked-out full SHA, branch, Run ID, and matching Plan/execution
   authorization references. Merely providing a record is not permission to
   execute: an independent reviewer must establish the record's authenticity.

**At this PR revision the launcher rejects execution** because the
Plan and formal execution approval fields remain unapproved/blank.
The missing append-only reserved Run ID is an additional fail-closed gate.

## Proposed future launch (DO NOT RUN BEFORE FORMAL AUTHORIZATION)

From the repository root with the provisioned CPU-only environment:

~~~bash
/workspace/fd-nig-venv/bin/python \
  06_Experiments/EXP-0003/run_formal_protocol.py \
  --execute \
  --run-id RUN-EXP-0003-NNN \
  --approved-revision-record /external/approved-records/exp0003-revision.json
~~~

Replace the placeholder with the actual reserved Run ID and the path
to an independently approved revision record. No such record is approved
or provisioned at this stage. The launcher resolves the repository root
from its own location; by default it stores Run artifacts **outside the
Git repository**, in a sibling directory.

### Independent revision approval record (schema only, NOT an approval)

After **all** static fixes, Plan approval, Run ID reservation, and
independent final-revision review, an authorized reviewer must supply
a JSON file outside the Git checkout, using an absolute path. The
following is a *field illustration only*; it is not a usable approval:

~~~json
{
  "schema_version": "1.0",
  "experiment": "EXP-0003",
  "run_id": "RUN-EXP-0003-NNN",
  "approved_branch": "task/fd-nig-verification",
  "approved_commit_sha": "<full 40-character independently approved Git SHA>",
  "plan_approval_ref": "<existing separately approved Plan reference>",
  "formal_execution_authorization_ref": "<existing separate execution authorization>",
  "revision_approval_ref": "<independent reviewer decision reference>"
}
~~~

The runner checks the externally supplied record against HEAD, the actual
branch, the reserved Run ID, and the already approved Plan/config references
*before* creating any run artifacts or launching Python tests. It records
the record's resolved location, SHA-256 file digest, revision approval reference,
and approved commit SHA in `provenance.json`. The runner never supplies a
default SHA or silently adopts current HEAD as the approved revision.

**Ordering is important:** any tracked Run Log reservation or other
preparation that creates a commit must be completed *before* the final
executable revision is independently reviewed and approved. Then create the
external approval record. Do not edit the checkout after pinning without
re-review and a new decision. Never embed the HEAD SHA in a file within
that very commit (self-referential commit cycle).

**Trust boundary:** comparing the JSON values and hash proves agreement
with the supplied record, **not** that the record was genuinely issued by
the project lead. The approver must independently control and verify its
provenance; the runner does not cryptographically authenticate signatures
or prevent a party with write access to the external record from forging it.
Neither this record nor the commit pin supersedes formal Plan approval
and distinct execution authorization.

The script refuses to execute without Plan/config approvals and matching
approval/execution authorization references. It also validates the budget,
seed, grid, FFT/pair-policy declarations, branch, interpreter and clean
tracked worktree. Running without `--execute` is refused.

## Shared-time execution and stopping conditions

- The launcher sets **one 120-second monotonic deadline** for both complete
  test repetitions, including fixture serialization and between-run overhead.
  It never resets the deadline.
- CPU-only child processes use `OMP_NUM_THREADS=2` and
  `MKL_NUM_THREADS=2`. A 100ms process-tree RSS watchdog enforces a
  **1536 MiB conservative early-stop**, with 2 GiB peak RSS acceptance
  and **no RLIMIT_AS**. This policy is not a kernel hard-cap.
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

Each attempt stores its independent exit status, elapsed time, timeout
flag, **RSS-watchdog peak, early-stop status, sampling errors**, GNU time
peak RSS, cgroup memory event snapshots, test identifiers, per-test
JUnit outcomes **including numerical record_property measurements**,
stdout/stderr hash and resource log.
Never overwrite a prior attempt, hide failures, alter thresholds post hoc,
or promote these results to verified Evidence.

After an authorized run, `Run_Log.md` is append-only and must link its
reserved Run ID to the command, code/config/fixture hashes, artifacts, UTC
timestamps, environment, results, deviations and any incomplete attempts.

## Remaining limitations

- These files were changed **statically only**. The runner and revised
  test suite have not been executed or validated in the Cloud runtime.
- The numerical tolerance/FFT/sparse and RSS settings are now frozen under
  the separate project-lead approval. Their implementation in pytest and
  the watchdog still requires independent static/runtime review;
  **formal Plan approval and execution remain independently blocked**.
- No Wiki projection is needed: these are administrative execution
  controls, not new human-readable scientific findings.
