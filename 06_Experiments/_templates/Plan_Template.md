---
schema_version: "1.0"
id: EXP-####
type: experiment-plan
title:
lifecycle_status: template
authority_class: none
authority_scope: preregistration-only
created_by:
content_origin:
created_at:
updated_at:
owner:
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: unknown
experiment_state:
plan_frozen_at:
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
method_ids: []
decision_ids: []
exclude_from_synthesis: true
---

# [Experiment title] — Preregistered Plan

## 1. Research question

- Question:
- Linked `HYP-ID`s:
- Linked `METHOD-ID`s:
- Linked `PC-ID`s:
- Exact Core requirement:
- Decision this experiment may inform:

## 2. Design

- Experimental unit:
- Independent variable:
- Dependent variable:
- Controlled variables:
- Treatment/method variants:
- Baselines:
- Ablations:
- Number of seeds/replicates:
- Randomization:

## 3. Data and simulator freeze

- `DATA-ID`s:
- Simulator/tool and version:
- Dataset manifest/hash:
- Train split:
- Validation split:
- Test split:
- OOD/process-condition split:
- Leakage checks:
- Sample budget:

## 4. Metrics and decision thresholds

| Metric | Exact implementation | Aggregation | Direction | Preregistered threshold | Role |
|---|---|---|---|---|---|

- Primary decision rule:
- Rejection rule:
- Inconclusive rule:
- Multiple-comparison/statistical treatment:
- Allowed diagnostic metrics:

## 5. Implementation freeze

- Code repository/path:
- Code revision:
- Configuration path/hash:
- Environment/lockfile:
- Hardware:
- Numerical precision:
- Determinism controls:
- Exact launch command or runner reference:

## 6. Budget, artifacts, and stopping

- Compute/time budget:
- Maximum runs:
- Early-stop rule:
- Safety/invalidity stop rule:
- Expected artifact paths:
- Required artifact hashes:
- Required logs and plots:
- Retention location:

## 7. Risks and validity

- Known confounders:
- Threats to internal validity:
- Threats to external validity:
- Expected failure modes:
- Core compatibility check:

## 8. Freeze record

- Plan reviewed by:
- Plan approved by:
- Approval reference:
- Frozen timestamp:
- Changes after freeze must be recorded in `Run_Log.md`: yes

## 9. Preregistration checklist

- [ ] All linked records exist and states are appropriate.
- [ ] Data, simulator, split, and manifest are frozen.
- [ ] Baselines, ablations, metrics, and thresholds are exact.
- [ ] Code/config/environment references are resolvable.
- [ ] Stop conditions and artifact retention are defined.
- [ ] Core scope and inference boundary are preserved.
- [ ] Approval occurred before the first formal run.
- [ ] Template metadata is replaced only when creating a real `EXP-ID` Plan.
