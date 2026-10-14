---
schema_version: "1.0"
id: METHOD-0003
type: method-design
title: "Mask-conditioned Effective Mode Frequency-Difference GNN"
lifecycle_status: draft
authority_class: working
authority_scope: candidate-method-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-14
updated_at: 2026-10-14
owner: project-lead
review_status: pending-user-review
reviewed_by:
approved_by:
approval_ref: "2026-10-14 project-lead approved progress review, not final Method selection"
core_alignment: pass
method_state: concept
source_ids: [SRC-0016, SRC-0017, SRC-0018]
data_ids: [DATA-0001]
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
experiment_ids: []
decision_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: false
---

# Mask-conditioned Effective Mode FD-GNN

## 1. Status and purpose
Working conceptual design, **not an accepted or selected Method**. User-approved research objective is a reusable one-pass forward surrogate for unseen masks. Internal coefficients are not required to be identifiable physical coherent modes. Preserve separate direct-pairwise `METHOD-0002` and kernel-predictor `METHOD-0001` as independent candidates.

## 2. Interface and physics
- Input: spatial Mask M; Fourier spectrum $A(k)=\mathcal{F}[M](k)$ on discrete 2-D grid. For current candidate, imaging conditions assumed fixed across examples, pending data validation.
- Frequency Node: discrete k and $\operatorname{Re}A(k)$, $\operatorname{Im}A(k)$.
- Known Pair Product: $p_{k,l}=A(k)A^*(l)$.
- Routing: $q=k-l$ (exact modular vs padded FFT specification pending).
- Generator: $b_r(k)=G_\theta(A)_{r,k}$ with $R$ complex coefficients per frequency; $R$ unspecified.
- Physical contribution $c_{k,l}=A(k)A^*(l)\sum_{r=1}^{R}b_r(k)b_r^*(l)$.
- Output spectrum: $\widehat I(q)=\sum_{k-l=q}c_{k,l}$; spatial intensity $I=\mathcal F^{-1}[\widehat I]$ with consistent FFT normalization and real/intensity validity requirements.
- Ground truth: final Aerial Image only; no effective-mode label.

## 3. Inference and training
In a single forward evaluation: Mask FFT -> GNN internal feature learning -> mask-conditioned effective-mode prediction -> differentiable pairwise quadratic renderer -> predicted Aerial Image. Backpropagate image loss through all differentiable steps during training; no per-Mask inference-time optimization.

## 4. Internal GNN candidate
User has accepted **incident Frequency Pair -> Frequency Node** as an internal feature-update path. It does not redirect a Pair's final physical contribution to another aerial-output frequency.

For Frequency Node k, candidate edge-conditioned aggregation:
$$s_k=\sum_{l\in\mathcal N(k)}w_\theta(k-l)p_{k,l}.$$
This is **Candidate A for testing**, not a selected layer and not the physical output Complex Sum. Hidden update $h_k^{(1)}=U_\theta(h_k^{(0)},s_k)$ and prediction head remain to be specified. Pair orientation, conjugates, channel widths, complex weights and equivariance/consistency are open.

## 5. Risks and checks
- An unrestricted sparse pair set may discard image information; dense $O(|K|^2)$ edges are expensive.
- Early weighted sum can lose pair identity and phase; test explicit difference channels and alternative aggregators.
- Reusing abstract learned messages as if they were final intensity-spectrum contributions would conflate hidden features and physics.
- Fourier intensity consistency, conjugate symmetry, nonnegativity, real-output contract and simulator label validity require explicit numerical tests.
- Literature sources SRC-0016–SRC-0018 support general GNN concepts only; claims are not verified lithography Evidence.

## 6. Governance
No new experiment, test thresholds, data freeze, source claim verification, or Method selection approved. A registered Experiment plan and the required governance checks must precede formal evaluation.
