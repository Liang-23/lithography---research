---
schema_version: "1.0"
id: EXP-0001
type: experiment-plan
title: "Data-only baseline versus SSIM-loss ablation"
lifecycle_status: draft
authority_class: working
authority_scope: experiment-local-planning-only
created_by: ai
content_origin: user-proposed-ai-structured
created_at: 2026-08-27
updated_at: 2026-08-27
owner: project-lead
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
experiment_state: draft-blocked
plan_frozen_at:
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
method_ids: []
decision_ids: [ADR-0003]
exclude_from_synthesis: true
---

# Data-only baseline versus SSIM-loss ablation — Draft Blocked Plan

## 0. Status and authority boundary

This record is a planning-only governance simulation. It is not a frozen preregistration, is not approved for execution, and must not be used to launch training or claim Evidence.

The proposed choices in this record have authority only within `EXP-0001`. They do not select a persistent Method, canonical architecture, project-wide baseline, dataset, simulator, metric, threshold, or default hyperparameter. Formal preregistration remains blocked until the canonical prerequisites listed in Section 10 exist and the unresolved fields are frozen.

## 1. Research question

- Question: Under an otherwise identical experiment-local configuration, how does the user-described current data-only baseline compare with the same baseline augmented by an SSIM-based loss term?
- Linked `HYP-ID`s: None registered; required before formal preregistration.
- Linked `METHOD-ID`s: None registered; required before formal preregistration.
- Linked `PC-ID`s: None. A `PC-ID` is not assumed to be applicable to this data-loss ablation; applicability must be determined from a later canonical design rather than invented here.
- Exact Core requirement: `00_Project_Core/Research_Requirement.md` Section 3, Prediction Performance, and Section 8, Evaluation Requirement, within the forward computational lithography scope and inference boundary.
- Decision this experiment may inform: Whether an SSIM-based loss term warrants further experiment-local investigation. It cannot establish a persistent project default or select a canonical Method or architecture.

## 2. Design

- Experimental unit: Unresolved pending a registered data/simulator contract and frozen sampling protocol.
- Independent variable: Experiment-local loss composition with two variants: data-only baseline loss; the same baseline loss plus an SSIM-based term.
- Dependent variable: Unresolved pending exact experiment-specific metrics and aggregation definitions.
- Controlled variables: Dataset/simulator, split, sample budget, code revision, architecture instance, optimizer, learning rate, batch size, training steps, initialization, seed policy, hardware, and numerical precision must be held constant across variants unless explicitly frozen otherwise in this plan.
- Treatment/method variants:
  1. User-described current data-only baseline loss. Its canonical definition does not yet exist.
  2. The identical baseline plus an SSIM-based loss term. The SSIM implementation and weight are unresolved.
- Baselines: The user-described current data-only baseline is proposed only for this ablation. It is not registered as a project-wide baseline and is not sufficiently defined for formal preregistration.
- Ablations: SSIM-based loss term off versus on.
- Number of seeds/replicates: Unresolved.
- Randomization: Unresolved.

## 3. Data and simulator freeze

- `DATA-ID`s: None registered.
- Simulator/tool and version: No canonical simulator contract exists.
- Dataset manifest/hash: Unresolved.
- Train split: Unresolved.
- Validation split: Unresolved.
- Test split: Unresolved.
- OOD/process-condition split: Unresolved.
- Leakage checks: Unresolved.
- Sample budget: Unresolved.

## 4. Metrics and decision thresholds

No metric or scientific threshold is preregistered by this draft.

| Candidate item | Exact implementation | Aggregation | Direction | Preregistered threshold | Role |
|---|---|---|---|---|---|
| SSIM-based training loss | Unresolved: formula, window, constants, value range, boundary handling, tensor axes, and implementation must be frozen | Unresolved | Unresolved | Not set | Experiment-local optimization term only |
| Experiment evaluation metrics | Unresolved; must be selected from canonical requirements or explicitly defined within the approved experiment plan | Unresolved | Unresolved | Not set | Primary/secondary roles not assigned |

- Primary decision rule: Unresolved.
- Rejection rule: Unresolved.
- Inconclusive rule: Unresolved.
- Multiple-comparison/statistical treatment: Unresolved.
- Allowed diagnostic metrics: Unresolved.

## 5. Implementation freeze

- Code repository/path: Unresolved.
- Code revision: Unresolved.
- Configuration path/hash: Unresolved.
- Environment/lockfile: Unresolved.
- Hardware: Unresolved.
- Numerical precision: Unresolved.
- Determinism controls: Unresolved.
- Exact launch command or runner reference: Intentionally absent; execution is prohibited by this planning-only task.

The following may be fixed later as experiment-local choices without an ADR, provided they remain confined to `EXP-0001`: loss composition, SSIM loss weight, learning rate, batch size, training steps, experiment-specific metrics, and temporary architecture configuration.

## 6. Budget, artifacts, and stopping

- Compute/time budget: Unresolved.
- Maximum runs: Unresolved.
- Early-stop rule: Unresolved.
- Safety/invalidity stop rule: Unresolved.
- Expected artifact paths: Unresolved.
- Required artifact hashes: Unresolved.
- Required logs and plots: Unresolved.
- Retention location: Unresolved.

## 7. Risks and validity

- Known confounders: Any difference other than the SSIM-based term between the two variants; an undefined baseline; unfrozen data, split, initialization, or training schedule.
- Threats to internal validity: Objective/metric coupling, inconsistent preprocessing or normalization, implementation differences beyond the intended ablation, insufficient seed coverage, and post-hoc metric or threshold selection.
- Threats to external validity: No registered data/simulator boundary or OOD/process-condition protocol currently exists.
- Expected failure modes: Ambiguous SSIM behavior due to unfrozen implementation details; unstable weighting; misleading gains caused by metric coupling; or results that cannot be reproduced from unresolved code/configuration records.
- Core compatibility check: The proposed comparison is compatible at the task level only if it remains a forward-surrogate training ablation, preserves the inference boundary, and does not introduce `ILT`, mask optimization, mask generation, gradient trust certification, or an external post-processing requirement. Detailed compatibility cannot be completed until the Method and implementation are defined.

## 8. Experiment-local choice classification

The following choices are classified as experiment-local and have no authority outside `EXP-0001`:

- loss composition;
- SSIM loss weight;
- learning rate;
- batch size;
- training steps;
- experiment-specific metrics;
- temporary architecture configuration.

Recording or freezing these choices in a future approved revision of this plan would not create a persistent project default and would not require an ADR. Any later proposal to make one of them canonical or project-wide would be a separate governance action.

## 9. Freeze record

- Plan reviewed by: Not reviewed.
- Plan approved by: Not approved.
- Approval reference: None.
- Frozen timestamp: None.
- Changes after freeze must be recorded in `Run_Log.md`: Yes, if the plan is later completed, approved, and frozen.

## 10. Formal preregistration blockers

Formal preregistration is blocked by the absence of:

1. a canonical `HYP-ID` defining the testable hypothesis;
2. a canonical `METHOD-ID` defining the baseline and SSIM-loss variants sufficiently for implementation;
3. a registered `DATA-ID` and/or simulator contract, including provenance and version;
4. a canonical definition of the user-described current data-only baseline;
5. a frozen dataset manifest, splits, leakage checks, and sample budget;
6. exact SSIM implementation details and experiment-local weight;
7. exact evaluation metrics, aggregation rules, decision rules, and scientific thresholds;
8. frozen code revision, configuration, environment, hardware, precision, and determinism controls;
9. compute budget, replicate count, stop conditions, artifact paths, hashes, logs, and retention rules.

A `PC-ID` has not been listed as a blocker because this bounded data-loss ablation does not, on current information, claim to test a registered Physics Constraint. No applicability decision is promoted beyond this draft.

## 11. Preregistration gate result

**Blocked — draft planning record only. No training or formal experiment may begin from this plan.**

- [ ] All linked records exist and states are appropriate.
- [ ] Data, simulator, split, and manifest are frozen.
- [ ] Baselines, ablations, metrics, and thresholds are exact.
- [ ] Code/config/environment references are resolvable.
- [ ] Stop conditions and artifact retention are defined.
- [x] The proposed scope preserves the Locked Core at the planning level.
- [ ] Approval occurred before the first formal run.

