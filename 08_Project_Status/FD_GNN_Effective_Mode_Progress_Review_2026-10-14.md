---
schema_version: "1.0"
id: FD-GNN-PROGRESS-2026-10-14
type: project-progress-review
title: "FD-GNN Effective Mode Architecture Progress Review"
lifecycle_status: active
authority_class: working
authority_scope: user-reviewed-design-summary-not-selected-method
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-14
updated_at: 2026-10-14
owner: project-lead
review_status: reviewed
reviewed_by: project-lead
approved_by: project-lead
approval_ref: "Explicit 'research progress review 通过', 2026-10-14"
core_alignment: pass
source_ids: []
method_ids: [METHOD-0002, METHOD-0003]
experiment_ids: []
exclude_from_synthesis: false
---

# FD-GNN Research Progress Review

**Review accepted by project lead on 2026-10-14.**
**Phase:** Internal GNN Feature Learning / Aggregation Design.
**Scientific status:** conceptual only. No new experiment executed or performance claim verified.

## Objective
Train a one-pass, generalizable forward lithography surrogate: new Mask -> FFT -> mask-conditioned Effective Mode Generator -> differentiable physical renderer -> Aerial Image. Optimize final image accuracy, generalization and runtime; intermediate Effective Modes need not match identifiable physical coherent modes.

## Confirmed mathematics and architecture concepts
1. Mask Fourier coefficients: $A(k)=\mathcal F[M](k)$; Frequency Node carries position and real/imaginary components.
2. Known Pair Product: $p_{k,l}=A(k)A^*(l)$. Do not insert an unnecessary black-box to calculate this initial product.
3. Frequency Difference Routing: $q=k-l$ (discrete 2-D modulo / padding convention unresolved), which fixes the **final pair-to-output-frequency contribution**.
4. Mask-conditioned Generator: $b_r(k)=G_\theta(A)_{r,k}$. Shared trainable network weights $\theta$ generate different effective modes for different Masks; modes are latent intermediate values, not supervised labels.
5. Final rendering:
   $$\widehat I_\theta(q)=\sum_{k-l=q}A(k)A^*(l)\sum_{r=1}^R b_r(k)b_r^*(l).$$
   With a valid aerial-intensity spectrum contract, reconstruct spatial intensity by inverse FFT without squaring the intensity a second time.
6. Training: final Aerial Image target and ordinary backpropagation through differentiable renderer. No per-mask test-time optimization.
7. Internal GNN Feature Learning: approved candidate path **Pair -> incident Frequency Node**, to update hidden representation prior to the Mode Prediction Head. This **does not alter** the final physical routing $k-l=q$.

## Current design problem
Aggregate the known Pair Products connected to a Frequency Node without prematurely losing information about their frequency differences.

**Candidate A (accepted for validation, NOT selected or verified):**
$$s_k=\sum_{l\in\mathcal N(k)} w_\theta(k-l)A(k)A^*(l).$$
Here $w_\theta(q)$ is a learnable edge/difference-conditioned weight; precise representation, width, complex-number policy and normalization remain open. Distinguish source-graph theory from project-specific hypotheses.

## Still unresolved
- Additional Aggregation ablations, concrete hidden-node update $U_\theta$, Generator depth/readout and complex outputs.
- Pair sampling/density and measured memory/time; full spectrum availability versus sparse-pair design.
- FFT index convention, conjugate symmetry, physical units, nonnegative intensity and ground-truth semantics.
- Baseline fairness versus direct-pairwise `METHOD-0002`, other baselines and independent train/test masks.
- Source full-text audits and new experiment preregistration.

## Authority and separation
This reviewed progress snapshot captures user-confirmed discussion principles only. `METHOD-0003` remains a separate candidate draft, `METHOD-0002` remains the direct-pairwise baseline, and `METHOD-0001` remains unchanged. No Locked Core edits, Method selection, accepted ADR, Evidence promotion, DATA freeze, experiment approval, or run is implied.
