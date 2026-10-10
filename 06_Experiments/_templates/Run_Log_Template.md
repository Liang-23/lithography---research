---
schema_version: "1.0"
id: EXP-####-RUN-LOG
type: experiment-run-log
title:
lifecycle_status: template
authority_class: none
authority_scope: append-only-run-history
created_by:
content_origin: experiment
created_at:
updated_at:
owner:
review_status: unreviewed
core_alignment: unknown
experiment_id: EXP-####
experiment_state:
exclude_from_synthesis: true
---

# EXP-#### Run Log

Append entries chronologically. Never rewrite or delete an earlier run entry. Corrections must be new dated entries that identify the corrected record.

## RUN-EXP-####-001

- Start timestamp:
- End timestamp:
- Operator:
- Purpose:
- Plan version/frozen hash:
- Code revision:
- Configuration path/hash:
- Environment/lockfile hash:
- `DATA-ID` and manifest/hash:
- Hardware:
- Exact command/runner:
- Random seed(s):
- Status: running | completed | failed | stopped | invalidated
- Exit code/error:
- Deviations from Plan:
- Reason for each deviation:
- Output artifact paths/hashes:
- Raw metric output paths/hashes:
- Observed anomalies:
- Immediate containment action:
- Notes (observation only):

## Correction entries

Use this form without editing the original entry:

- Correction timestamp:
- Corrects run/field:
- Old recorded value:
- Correct value:
- Reason and evidence:
- Corrected by:

## Log checklist

- [ ] Failed and stopped runs are preserved.
- [ ] Every run has a permanent Run ID.
- [ ] Commands, revisions, configs, data, environment, and seeds are resolvable.
- [ ] Deviations and anomalies are explicit.
- [ ] Artifact hashes are recorded.
- [ ] Interpretations are deferred to `Result.md`.
