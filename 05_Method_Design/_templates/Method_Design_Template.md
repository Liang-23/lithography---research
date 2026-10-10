---
schema_version: "1.0"
id: METHOD-####
type: method-design
title:
lifecycle_status: template
authority_class: none
authority_scope: candidate-method-only
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
method_state: concept
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
experiment_ids: []
decision_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: true
---

# [Method title]

## 1. Purpose and authority

- Core requirement addressed:
- Linked `HYP-ID`s:
- Linked `PC-ID`s:
- Selection `ADR-ID`, if any:
- Current Method state:
- Scope exclusions:

## 2. Interface contract

| Item | Definition | Shape | Unit | Coordinate system | Source/Data ID |
|---|---|---|---|---|---|
| Input | | | | | |
| Target | | | | | |
| Raw output | | | | | |
| Final output | | | | | |

## 3. Architecture and data flow

- Components:
- Forward path:
- Where physical knowledge enters:
- What remains freely learned:
- External dependencies:

## 4. Training behavior

- Objective/loss terms:
- Gradient path:
- `stop-gradient` or teacher-target behavior:
- Sampling/curriculum:
- High-fidelity calls:
- Training-only correction:

## 5. Inference behavior

- End-to-end inference path:
- Required parameters and availability:
- Correction/projection at inference:
- Failure/fallback behavior:
- Latency and memory estimate:

## 6. Data and implementation contracts

- `DATA-ID`s:
- Simulator/tool and version:
- Code location/revision:
- Configuration schema:
- Randomness and determinism:
- Numerical precision:

## 7. Evaluation design

- Baselines:
- Ablations:
- Primary metrics:
- Physical-consistency metrics:
- Compute comparison:
- OOD/process-condition evaluation:
- Proposed `EXP-ID`s:

## 8. Risks and rollback

- Scientific failure modes:
- Numerical failure modes:
- Data leakage risks:
- Information-damage risks:
- Cost risks:
- Rejection condition:
- Rollback/fallback method:

## 9. Review checklist

- [ ] Interfaces, shapes, units, and coordinates are complete.
- [ ] Training and inference paths are separated.
- [ ] All Physics Constraints and data contracts are registered.
- [ ] Baselines and ablations can isolate causal contribution.
- [ ] Compute, failure, and rollback conditions are explicit.
- [ ] The method is not described as selected without an accepted ADR.
- [ ] Template metadata is replaced only when creating a real `METHOD-ID` record.
