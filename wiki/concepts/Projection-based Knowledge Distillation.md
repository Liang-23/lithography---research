---
schema_version: "1.0"
title: "Projection-based Knowledge Distillation"
aliases:
  - "Projection Knowledge Distillation"
type: concept
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-09-01
review_status: unreviewed
core_alignment: pass
knowledge_status: candidate-family-in-core
canonical_refs:
  - "00_Project_Core/Project_Overview.md"
  - "00_Project_Core/Research_Requirement.md"
  - "01_Background/BG-0001_SRC-0002_Output_Projection_Project_Aware_Comparison.md"
  - "02_Evidence/SRC-0003_NewPINNs.md"
  - "02_Evidence/SRC-0004_PADM.md"
  - "02_Evidence/EV-0004_PADM_Privileged_CT_Conditioned_Attention_Transfer.md"
  - "02_Evidence/EV-0005_PADM_Internal_Physics_Aware_Attenuation_Factor_Computation.md"
  - "02_Evidence/EV-0006_PADM_Privileged_Input_Removal_Retains_Diffusion_Physics_Inference.md"
  - "02_Evidence/SRC-0007_Hard_Conservation_Correctors_Can_Hide_a_Degrading_Model.md"
  - "02_Evidence/SRC-0008_Solver_Integrated_Adversarial_Attacking_and_Training_of_Neural_Operators.md"
  - "02_Evidence/SRC-0009_Deep_Epidemiological_Modeling_by_Black_Box_Knowledge_Distillation.md"
  - "02_Evidence/SRC-0010_EngGeneNet_Transient_Heat_Conduction.md"
source_ids:
  - SRC-0002
  - SRC-0003
  - SRC-0004
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0010
evidence_ids:
  - EV-0004
  - EV-0005
  - EV-0006
exclude_from_synthesis: false
---

# Projection-based Knowledge Distillation

## Core idea

Projection-based Knowledge Distillation is a candidate strategy for transferring corrected solutions back into a [[High-dimensional AI Surrogate]]. The candidate flow pairs [[Physics-defined Solution Space Projection]] with learning from the corrected output.

## Intended role

The Core hypothesis is that correction followed by knowledge transfer may introduce [[Physics Knowledge Integration]] while preserving more [[Neural Representation Learning]] flexibility than continuously enforcing a physical term during optimization.

## Boundary（limitation）

The final inference model must remain end to end. A concrete Method would therefore need to state whether projection occurs only during training, what target or loss transfers the correction, and how performance and physical behavior are evaluated.

## Important distinction from SRC-0002

The paper does **not** perform this transfer. Its projection is external and post-training; corrected outputs are not reused as targets, no teacher-student or distillation stage is described, and the optimizer remains required for corrected inference. Joint training is mentioned only as future work.

Accordingly, projection-to-surrogate transfer remains unresolved relative to that Source. This distinction, and the need to remove external correction from deployment, are summarized in [[output-projection-project-positioning|Output Projection and Project Positioning]].

## What the admitted corpus now distinguishes

- [[deep-epidemiological-modeling-by-black-box-knowledge-distillation|Deep Epidemiological Modeling]] directly uses teacher outputs as student targets and removes the teacher at inference, but the teacher does not correct the student's raw prediction.
- Verified `EV-0004`-`EV-0006` show that [[padm-physics-aware-diffusion-model-for-attenuation-correction|PADM]] removes privileged CT/Teacher conditioning through normalized attention/representation transfer on 2D images, while paired AC ground truth remains the diffusion target. Its internal attenuation-factor calculation and reverse diffusion remain at Student inference, so PADM is not corrected-output distillation or a corrector-free one-pass surrogate.
- [[newpinns|NewPINNs]] and [[solver-integrated-adversarial-attacking-and-training-of-neural-operators|Solver-Integrated Adversarial Training]] provide solver-informed field supervision followed by direct neural inference, but neither is external output correction distilled into a second student.
- [[enggenenet-transient-heat-conduction|EngGeneNet]] removes an ADI data generator at inference, while also embedding physics residuals and architecture-specific transformations.
- [[hard-conservation-correctors-can-hide-a-degrading-model|Hard conservation correctors]] shows that naïvely supervising only corrected outputs can hide raw-model degradation.

Together these papers narrow the design question: knowledge transfer and solver removal are individually precedented, while the exact full chain remains unestablished within this admitted corpus. This is corpus-relative positioning, not a field-wide novelty claim. See [[corrected-target-and-teacher-student-transfer|Corrected-target and Teacher-student Transfer]].

## Status

This is not a selected or tested Method. No teacher/student definition, distillation objective, correction operator, data contract, or Experiment has been accepted.
