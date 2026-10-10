---
title: "PADM: A Physics-aware Diffusion Model for Attenuation Correction"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-30
updated_at: 2026-09-13
review_status: reviewed
human_audit_status: completed
knowledge_status: pivotal-claims-verified-with-boundaries
canonical_refs:
  - "02_Evidence/SRC-0004_PADM.md"
  - "02_Evidence/EV-0004_PADM_Privileged_CT_Conditioned_Attention_Transfer.md"
  - "02_Evidence/EV-0005_PADM_Internal_Physics_Aware_Attenuation_Factor_Computation.md"
  - "02_Evidence/EV-0006_PADM_Privileged_Input_Removal_Retains_Diffusion_Physics_Inference.md"
source_ids: [SRC-0004]
evidence_ids: [EV-0004, EV-0005, EV-0006]
source_file: "raw/SRC-0004_PADM.pdf"
exclude_from_synthesis: false
---

# PADM: A Physics-aware Diffusion Model for Attenuation Correction

## Human-readable summary

PADM is a 2D image-domain SPECT attenuation-correction model. Its Teacher receives NAC plus a CT-derived attenuation map, while its Student receives NAC only. The Source reports a teacher-student diffusion architecture, an internal physics-aware attenuation-factor calculation, and iterative reverse-diffusion inference. [SRC-0004, pp. 4–7]

The implemented output is a $256\times256$ slice, not a jointly corrected 3D volume. Claims outside the three verified mechanisms below remain Source-reported unless separately verified.

## Verified project Evidence

### Privileged physics transfer

`EV-0004` verifies the bounded mechanism in which PADM-T uses privileged CT-derived attenuation-map conditioning during training and PADM-S matches a normalized aggregated Teacher representation. PADM-S uses NAC-only conditioning and no longer requires the CT-derived attenuation map at inference. Paired AC image $x_0$ remains the diffusion target; the equations do not specify Teacher-corrected AC outputs as Student labels. This is attention/representation transfer, not corrected-output distillation. [[Projection-based Knowledge Distillation|Teacher-to-student transfer]] is therefore precedented here in a narrower form than projected-target transfer. [EV-0004]

### Internal physics integration

`EV-0005` verifies that PADM predicts per-angle path-length fields and a $\mu$ attenuation field, constructs an input-dependent attenuation-correction factor, and uses that calculation inside iterative reverse-diffusion denoising. This is an internal model mechanism, not an external projection of a completed neural output onto a defined physical solution space. The Source does not establish exact constraint satisfaction, physical accuracy or identifiability of the predicted fields, or complete gradient propagation through every physics-module operation. [EV-0005]

### Inference boundary

`EV-0006` verifies that PADM-S removes PADM-T and CT-derived attenuation-map conditioning from the reported inference structure while retaining iterative reverse diffusion and, structurally, the Student's own physics-aware denoising path. The Student is therefore not physics-free or corrector-free, inference is not established as one-pass, and the paper reports no measured PADM inference-time acceleration. The Student physics path is supported by the shared architecture, Figure 1, Section 4.4, and the sampling procedure rather than by a separate Student-only inference algorithm. [EV-0006]

## Project positioning

`retain as pivotal with narrowed role`

PADM is strong Source-relative precedent for transferring privileged training-time physics conditioning into a Student whose deployment input no longer requires that privileged information. It does not provide precedent for external physical projection, corrected-target distillation, a completely corrector-free one-pass surrogate, or a lithography-specific mechanism.

## Important boundaries

- Learned path-length and $\mu$ fields are not independently validated as physically accurate or identifiable.
- No exact physical admissibility guarantee, deployment gate, fallback, 3D consistency test, or representation-freedom comparison is established.
- The 16-projection Teacher-Student metric gap is supporting context inside `EV-0006`, not a separate general performance claim.
- The admitted artifact is exact arXiv v1. A later WACV version exists and was not substituted.

## 用户研究偏好与阅读补充 — 2026-09-13

用户希望优先研究 conditional diffusion＋U-Net：把 U-Net 作为逐步重建网络，探索物理信息如何参与内部计算，并研究 Teacher 的额外信息怎样传给 Student。这个偏好使 PADM 成为本轮重点参考，不表示已选定光刻 architecture 或证明它优于直接预测。

原文训练使用 paired NAC/AC 构造不同 timestep 的 noisy states；noise variants 是已有样本的训练变化，不是额外正确标签。推理从条件输入 NAC 开始，逐步得到重建结果。diffusion step 不能自动对应光刻真实物理阶段。[SRC-0004, PDF pp. 5–6, Algorithms 1–2]

Teacher 提供的是 attention/representation signal，paired AC target 仍在。光刻中是否存在合理的 training-only 信息尚未确认，不能直接把它当作 corrected-output distillation。[EV-0004、EV-0006]

[[padm-physics-transfer-low-data-lithography|从 PADM 与物理知识回传到低数据光刻预测]] 将这一偏好连接到三个 draft 研究问题：逐步预测的收益/成本、correction 知识保留、减少高保真标签。它们均未验证，且与上面已完成的 Source-relative Human Audit 分开。

## Governance traceability

Canonical Source: `SRC-0004`, stored at `02_Evidence/SRC-0004_PADM.md`. Targeted P1-P4 Human Audit and project-lead review completed on 2026-09-01. `EV-0004`, `EV-0005`, and `EV-0006` are verified only within their recorded applicability boundaries; other PADM claims and reported results remain Source-reported unless separately verified. The 2026-09-13 user preference is separate from that audit; HYP-0001–HYP-0003 are draft project questions, not verified lithography claims or a Method selection.
