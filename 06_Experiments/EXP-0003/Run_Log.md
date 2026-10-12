---
schema_version: "1.0"
id: EXP-0003-RUN-LOG
type: experiment-run-log
title: "EXP-0003 append-only formal run record"
lifecycle_status: draft
authority_class: working
authority_scope: experiment-local-run-record-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-12
updated_at: 2026-10-12
owner: project-lead
review_status: unreviewed
exclude_from_synthesis: true
---

# EXP-0003 Run Log

**Status: template only. No Run ID is reserved; no formal execution has occurred or is authorized by this file.**

This append-only log belongs to `EXP-0003`, the candidate `METHOD-0002`
synthetic frequency-difference aggregation feasibility check. It is a record
of reservations and outcomes, **not** a substitute for the approved Plan,
independent execution authorization, or verified scientific Evidence.

## Approval boundary

- Numerical acceptance settings and the monitored-RSS memory policy were
  approved and frozen on 2026-10-12, as recorded in
  `Numerical_and_Memory_Freeze_Review.md`.
- The complete `Plan.md` remains `experiment_state: draft-blocked` and
  `approval_status: not_requested` until separately approved.
- `formal_execution_authorization_ref` remains ungranted. Creating this log
  does not preregister the Plan, approve any run, select the Method, or permit
  use of the runner's `--execute` flag.

## Append-only rules

1. Reserve a unique `RUN-EXP-0003-NNN` only after the project's required
   review and approvals; record its exact heading as
   `## RUN-EXP-0003-NNN (reserved)` with `NNN` replaced by three digits.
   **There is deliberately no such heading in this template.**
2. Each real reservation and its subsequent outcome must remain visible.
   Do not delete, recycle, renumber, overwrite, or silently amend a Run ID,
   including for failed, timed-out, interrupted, or incomplete attempts.
   Record corrections as dated append-only addenda.
3. Before any authorized launch, independently check the approved commit SHA,
   branch/environment, complete Plan, execution authorization, frozen config,
   suite coverage, and the unique reservation. The runner's structural
   preflight does not replace this independent review.
4. Store per-attempt immutable artifacts separately, outside the Git worktree.
   Link their locations and SHA-256 digests; preserve incomplete attempts.
5. Never treat a logged result as verified Evidence without the project's
   separate evidence-review process. Do not silently adjust frozen thresholds,
   the shared 120-second total limit, or the monitored-RSS policy after failure.

## Information required for each future run

When a run is explicitly authorized, append a new record with the following
fields. **These are field definitions, not a run entry or reservation.**

| Field | Required contents |
| --- | --- |
| Run identity | Unique `RUN-EXP-0003-NNN` and UTC reservation timestamp |
| Governance | Plan approval reference, formal execution authorization reference, approver and scope |
| Frozen revision | Independently approved exact Git commit SHA and branch; static-review reference |
| Execution | Exact command, interpreter, CPU-only environment, Python/Torch/pytest versions and environment provenance |
| Input provenance | SHA-256 hashes for Plan, frozen config, runner, implementations, tests, and serialized fixture |
| Frozen protocol | Seed, 16×16 grid, FFT convention, sparse-pair policy, dtype gates, two-repeat total 120 s deadline |
| Resource policy | Maximum two CPU threads; process-tree RSS <= 2 GiB acceptance, 1536 MiB watchdog early stop, <= 100 ms monitoring; userspace guard is not a kernel hard cap |
| Attempt outcomes | Start/end UTC, exit status, elapsed time, timeout, memory failure, sampling errors, per-test JUnit results and numerical diagnostics for each attempt |
| Artifact links | Immutable per-attempt stdout/stderr, JUnit, status, resource logs, provenance, fixture and summary paths, with SHA-256 |
| Final assessment | PASS / FAIL / INCOMPLETE, two-repetition agreement, observed peak RSS, deviations, unresolved concerns, reviewer and review date |
| Follow-up | Dated append-only corrections, review decisions and Evidence promotion reference if separately authorized |

## Run entries

_None. No Run ID has been reserved, and no tests, calibration, benchmarks,
or formal experiments were executed while creating this template._
