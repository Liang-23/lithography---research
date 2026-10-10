---
title: "Three-topic Architecture and Occupancy Map"
type: synthesis
lifecycle_status: draft
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-30
updated_at: 2026-09-13
review_status: pending-user-review
core_alignment: pass
knowledge_status: corpus-relative-synthesis
canonical_refs:
  - "90_Quarantine/Q-0001_Three_Topic_Literature_Screening_Campaign.md"
  - "02_Evidence/Source_Registry.md"
  - "02_Evidence/EV-0001_NewPINNs_State_Dependent_Black_Box_Solver_Feedback.md"
  - "02_Evidence/EV-0002_NewPINNs_Direct_Neural_Field_Prediction.md"
  - "02_Evidence/EV-0003_NewPINNs_Solver_Inherited_Limitations.md"
  - "02_Evidence/EV-0004_PADM_Privileged_CT_Conditioned_Attention_Transfer.md"
  - "02_Evidence/EV-0005_PADM_Internal_Physics_Aware_Attenuation_Factor_Computation.md"
  - "02_Evidence/EV-0006_PADM_Privileged_Input_Removal_Retains_Diffusion_Physics_Inference.md"
source_ids: [SRC-0003, SRC-0004, SRC-0005, SRC-0006, SRC-0007, SRC-0008, SRC-0009, SRC-0010, SRC-0011, SRC-0012, SRC-0013]
evidence_ids: [EV-0001, EV-0002, EV-0003, EV-0004, EV-0005, EV-0006]
exclude_from_synthesis: true
---

# Three-topic Architecture and Occupancy Map

## How the admitted papers occupy the design space

| Source | Main mechanism | Spatial output | Correction influences training | External dependency at inference | Corrected target / transfer |
|---|---|---:|---:|---:|---|
| [[newpinns|NewPINNs]] | Dynamic black-box solver consistency: solver value enters loss, but backpropagation does not traverse $S$ | Yes, 2D/3D | Yes | No in reported forward evaluation path; no runtime proof | Dynamic solver response; authors say not distillation; shallow-water warm-start exception |
| [[padm-physics-aware-diffusion-model-for-attenuation-correction|PADM]] | Privileged CT-conditioned attention/representation transfer plus internal attenuation-factor denoising | Yes, 2D slice | Yes | Teacher/CT no; reverse diffusion and Student physics-aware module yes | Attention representation; paired AC target; not corrected-output distillation |
| [[hard-constrained-deep-learning-for-climate-downscaling|Hard-Constrained Downscaling]] | Closed-form terminal consistency layer | Yes | Yes, by gradient | Yes | No |
| [[adaptive-correction-for-ensuring-conservation-laws-in-neural-operators|Adaptive Correction]] | Learnable terminal conservation allocation | Yes | Yes, by gradient | Yes | No |
| [[hard-conservation-correctors-can-hide-a-degrading-model|Hard conservation correctors]] | Global rescaling corrector | Yes | Yes; can erase gradient direction | Yes | Corrected-output supervision, no distillation |
| [[solver-integrated-adversarial-attacking-and-training-of-neural-operators|Solver-Integrated Adversarial Training]] | Solver relabelling on perturbed fields | Yes | Yes | No | Solver labels for same surrogate |
| [[deep-epidemiological-modeling-by-black-box-knowledge-distillation|Deep Epidemiological Modeling]] | Black-box teacher targets | No, temporal sequence | Yes | No | Direct teacher-output targets |
| [[enggenenet-transient-heat-conduction|EngGeneNet]] | ADI data + physics loss + embedded transform | Yes, small 2D field | Yes | ADI no; embedded module yes | Solver-generated training data |
| [[physicscorrect|PhysicsCorrect]] | Cached linearized PDE-residual correction | Yes | No | Yes | No |
| [[pinet|$\Pi$net]] | Iterative orthogonal projection layer | Vector/trajectory | Yes, by implicit gradient | Yes | No |
| [[dc3|DC3]] | Equality completion + inequality correction | Vector/graph state | Yes, by gradient | Yes | No |

## Corpus-relative occupancy conclusion

The admitted corpus already occupies terminal hard correction, differentiable projection, solver-informed training, black-box teacher transfer, spatial-field correction, and several correction-failure modes. What it does **not** establish as one verified architecture is:

$$
\text{high-dimensional raw surrogate}
\rightarrow
\text{lithography-specific physical correction}
\rightarrow
\text{safe corrected knowledge transfer}
\rightarrow
\text{corrector-free end-to-end inference}.
$$

This remaining chain is corpus-relative and scientifically blocked by the missing lithography relationship. It is not a field-wide novelty claim. Read the three focused syntheses: [[corrected-target-and-teacher-student-transfer|Corrected-target Transfer]], [[amortized-projection-and-solver-distillation|Amortized Projection]], and [[high-dimensional-safe-correction|High-dimensional Safe Correction]].

The NewPINNs row is bounded by verified `EV-0001`-`EV-0003`. The PADM row is bounded by verified `EV-0004`-`EV-0006`: its physics calculation is internal to diffusion, learned path-length/$\mu$ fields are not independently validated, and no one-pass or measured-speedup claim is established. Other rows retain their separately recorded review/Evidence states; this map does not promote the entire corpus to verified Evidence.

## 从机制比较进入候选研究 — 2026-09-13

用户明确偏好优先讨论 conditional diffusion＋U-Net，同时研究 correction 知识回传与高保真标签效率。新的 [[padm-physics-transfer-low-data-lithography|中文项目研究综合]] 将本表的机制拆为三个可分别检验的问题：预测 framework 的收益/成本、无外部 corrector 时的知识保留、同等质量下的标签需求。

HYP-0001–HYP-0003 目前均为 draft。内部 iterative diffusion 不自动违反端到端要求，但其成本与物理语义需定义；外部 correction 的保留对照不等于最终部署方案。前述 corpus-relative 空缺仍不是领域创新结论，也不意味着任意组合这些模块就能实现光刻目标。
