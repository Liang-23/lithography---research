---
title: "Corrected-target and Teacher-student Transfer"
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
  - "02_Evidence/EV-0001_NewPINNs_State_Dependent_Black_Box_Solver_Feedback.md"
  - "02_Evidence/EV-0002_NewPINNs_Direct_Neural_Field_Prediction.md"
  - "02_Evidence/SRC-0004_PADM.md"
  - "02_Evidence/EV-0004_PADM_Privileged_CT_Conditioned_Attention_Transfer.md"
  - "02_Evidence/EV-0005_PADM_Internal_Physics_Aware_Attenuation_Factor_Computation.md"
  - "02_Evidence/EV-0006_PADM_Privileged_Input_Removal_Retains_Diffusion_Physics_Inference.md"
  - "02_Evidence/SRC-0007_Hard_Conservation_Correctors_Can_Hide_a_Degrading_Model.md"
  - "02_Evidence/SRC-0008_Solver_Integrated_Adversarial_Attacking_and_Training_of_Neural_Operators.md"
  - "02_Evidence/SRC-0009_Deep_Epidemiological_Modeling_by_Black_Box_Knowledge_Distillation.md"
  - "02_Evidence/SRC-0010_EngGeneNet_Transient_Heat_Conduction.md"
source_ids: [SRC-0003, SRC-0004, SRC-0007, SRC-0008, SRC-0009, SRC-0010]
evidence_ids: [EV-0001, EV-0002, EV-0004, EV-0005, EV-0006]
exclude_from_synthesis: true
---

# Corrected-target and Teacher-student Transfer

## Corpus-relative answer

The admitted corpus confirms that expensive teacher or solver knowledge can be transferred into a model that runs without that teacher. It does **not** yet contain the complete sequence in which an external physical operator corrects a raw surrogate prediction, the corrected result becomes a target, and the final student removes the operator.

| Pattern | Admitted example | What is transferred | External dependency at inference |
|---|---|---|---|
| Fixed black-box teacher targets | [[deep-epidemiological-modeling-by-black-box-knowledge-distillation|Deep Epidemiological Modeling]] | Complete teacher output sequences | Teacher removed |
| Privileged teacher features | [[padm-physics-aware-diffusion-model-for-attenuation-correction|PADM]] | Verified normalized attention/representation matching; paired AC ground truth remains the image target | Teacher/CT removed; reverse diffusion and Student physics-aware module remain |
| State-dependent solver response | [[newpinns|NewPINNs]] | Solver response to the current neural field enters the loss; backpropagation does not traverse $S$ | Solver absent from the reported direct prediction path; no speedup benchmark |
| Solver relabelling under perturbation | [[solver-integrated-adversarial-attacking-and-training-of-neural-operators|Solver-Integrated Adversarial Training]] | Solver output for adversarially perturbed inputs | Solver removed from direct prediction |
| Offline solver-generated spatial data | [[enggenenet-transient-heat-conduction|EngGeneNet]] | ADI temperature fields | ADI removed; embedded physics remains |
| Corrected-output supervision | [[hard-conservation-correctors-can-hide-a-degrading-model|Hard conservation correctors]] | Loss is evaluated after correction | Corrector remains and can erase a raw-model gradient direction |

## Most important boundary

“Teacher-free inference” is not equivalent to “corrected-target projection distillation.” Some papers transfer full solver outputs, others transfer features, and others use state-dependent targets. The raw-prediction-feedback loop remains the defining unresolved mechanism:

$$
\widehat y
\xrightarrow{\text{physical operator}}
y^{\mathrm{corr}}
\xrightarrow{\text{target or teacher signal}}
f_{\theta'}(x),
$$

with the operator absent from final inference.

The gradient-nullspace result from [[hard-conservation-correctors-can-hide-a-degrading-model|SRC-0007]] also means that corrected outputs cannot automatically be treated as safe supervision. Raw prediction quality and correction magnitude must remain observable. This is a requirement for [[Projection-based Knowledge Distillation]], not a selected Method.

For NewPINNs, `EV-0001` verifies the dynamic loss signal and its gradient boundary, while `EV-0002` verifies only the reported direct neural evaluation path. Neither Evidence record converts NewPINNs into external output projection or fixed corrected-target distillation.

For PADM, `EV-0004` verifies privileged CT-conditioned attention transfer rather than Teacher-corrected output labels, `EV-0005` verifies an internal attenuation-factor calculation rather than external solution-space projection, and `EV-0006` verifies that privileged deployment inputs disappear while iterative diffusion and the Student physics-aware path remain. PADM therefore narrows the teacher-transfer precedent without completing the external-correction-to-corrector-free-surrogate chain.
