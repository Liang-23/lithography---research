---
title: "High-dimensional Safe Correction"
type: synthesis
lifecycle_status: draft
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-30
updated_at: 2026-09-01
review_status: pending-user-review
core_alignment: pass
knowledge_status: corpus-relative-synthesis
canonical_refs:
  - "02_Evidence/SRC-0003_NewPINNs.md"
  - "02_Evidence/EV-0003_NewPINNs_Solver_Inherited_Limitations.md"
  - "02_Evidence/SRC-0004_PADM.md"
  - "02_Evidence/SRC-0005_Hard_Constrained_Deep_Learning_for_Climate_Downscaling.md"
  - "02_Evidence/SRC-0006_Adaptive_Correction_for_Ensuring_Conservation_Laws_in_Neural_Operators.md"
  - "02_Evidence/SRC-0007_Hard_Conservation_Correctors_Can_Hide_a_Degrading_Model.md"
  - "02_Evidence/SRC-0008_Solver_Integrated_Adversarial_Attacking_and_Training_of_Neural_Operators.md"
  - "02_Evidence/SRC-0011_PhysicsCorrect.md"
source_ids: [SRC-0003, SRC-0004, SRC-0005, SRC-0006, SRC-0007, SRC-0008, SRC-0011]
evidence_ids: [EV-0003]
exclude_from_synthesis: true
---

# High-dimensional Safe Correction

## Spatial evidence now exists

The admitted corpus includes 2D/3D PDE fields, medical slices, climate images up to $(3,512,512)$, and global weather-emulator fields. Therefore high-dimensional application is no longer absent at the corpus level. It remains unverified for aerial, resist, and wafer images.

## Why correction is not automatically safe

Three failure patterns are directly reported:

1. **Constraint mismatch:** [[hard-constrained-deep-learning-for-climate-downscaling|Hard-Constrained Climate Downscaling]] forces zero violation while worsening NorESM reference error.
2. **Metric/allocation mismatch:** [[adaptive-correction-for-ensuring-conservation-laws-in-neural-operators|Adaptive Correction]] reports a minimum-$L_2$ projection that conserves the selected invariant but catastrophically worsens one PDE-field error.
3. **Gradient information loss:** [[hard-conservation-correctors-can-hide-a-degrading-model|Hard conservation correctors]] shows corrected-only supervision can hide raw-model drift along a corrector null direction.

[[physicscorrect|PhysicsCorrect]] adds discretization-target mismatch and quadratic grid-scaling concerns. [[solver-integrated-adversarial-attacking-and-training-of-neural-operators|Solver-Integrated Adversarial Training]] shows that robustness on constructed shifts can trade against clean performance.

Verified `EV-0003` adds a different boundary from [[newpinns|NewPINNs]]: even when the solver is used only during training, the method inherits solver stability requirements and computational cost and may require initialization, normalization, clipping, flooring, or warm start. Partial solver advancement does not itself establish exact feasibility or inference-time safety.

## Minimum future evidence package

A candidate must report, separately, raw accuracy, corrected accuracy, physical residual, correction magnitude, local/edge/frequency preservation, runtime/memory, and OOD/process-condition behavior. A safe design may require an accept/reject gate, trust region, correction cap, fallback, or raw-versus-corrected selector. None is currently selected.

This is guidance for [[High-dimensional AI Surrogate]] requirements, not a `PC-####`, Method, Hypothesis, or Experiment.
