---
schema_version: "1.0"
title: "High-dimensional Safe Correction"
aliases:
  - "Safe Spatial Correction"
type: concept
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-30
updated_at: 2026-09-01
review_status: unreviewed
core_alignment: pass
knowledge_status: corpus-relative-requirement-family
canonical_refs:
  - "02_Evidence/SRC-0003_NewPINNs.md"
  - "02_Evidence/EV-0003_NewPINNs_Solver_Inherited_Limitations.md"
  - "02_Evidence/SRC-0005_Hard_Constrained_Deep_Learning_for_Climate_Downscaling.md"
  - "02_Evidence/SRC-0006_Adaptive_Correction_for_Ensuring_Conservation_Laws_in_Neural_Operators.md"
  - "02_Evidence/SRC-0007_Hard_Conservation_Correctors_Can_Hide_a_Degrading_Model.md"
  - "02_Evidence/SRC-0011_PhysicsCorrect.md"
source_ids: [SRC-0003, SRC-0005, SRC-0006, SRC-0007, SRC-0011]
evidence_ids: [EV-0003]
exclude_from_synthesis: false
---

# High-dimensional Safe Correction

## Why “safe” is a separate requirement

Physical satisfaction and predictive quality are different axes. The admitted Sources provide three distinct warnings:

- a mismatched downscaling relation can force zero violation while worsening reference RMSE ([[hard-constrained-deep-learning-for-climate-downscaling|Hard-Constrained Climate Downscaling]]);
- a minimum-$L_2$ projection can catastrophically worsen a PDE-field prediction while satisfying the selected invariant ([[adaptive-correction-for-ensuring-conservation-laws-in-neural-operators|Adaptive Correction]]);
- corrected-output supervision can erase a raw-model gradient direction and hide drift ([[hard-conservation-correctors-can-hide-a-degrading-model|Hard conservation correctors]]).

[[physicscorrect|PhysicsCorrect]] adds two further boundaries: zero discretization residual can differ from the numerical reference, and correction cost can scale poorly with grid size.

[[newpinns|NewPINNs]] adds a verified training-time boundary: solver feedback can be removed from the reported forward evaluation path while solver stability requirements and computational cost remain during training. Reported stabilization measures do not amount to a deployment safety gate or exact-feasibility guarantee. [EV-0003]

## Candidate safety requirements

A future correction framework would need to measure both raw and corrected prediction quality, constraint residual, correction magnitude, local/spatial structure, runtime, and OOD behavior. It may need a gate, trust region, correction bound, fallback, or accept/reject rule. None of those mechanisms is currently selected.

The admitted papers demonstrate spatial correction on moderate-to-large fields, but none supplies a verified lithography relationship or proves safe operation for aerial, resist, or wafer images. This concept remains a corpus-relative requirement, not a Physics Constraint or Method.
