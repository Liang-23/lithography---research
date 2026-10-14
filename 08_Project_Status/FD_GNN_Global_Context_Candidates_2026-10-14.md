---
schema_version: "1.0"
id: FD-GNN-GLOBAL-CONTEXT-2026-10-14
type: project-progress-review
title: "FD-GNN Global Context Generator Candidates"
lifecycle_status: active
authority_class: working
authority_scope: user-acknowledged-candidate-design-not-selected-method
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-14
updated_at: 2026-10-14
owner: project-lead
review_status: pending-user-review
reviewed_by:
approved_by:
approval_ref: "2026-10-14 conversation: project lead accepted L0/G1/G2 as candidate architectures and their motivations; not a final Method choice, ADR, or experiment authorization"
core_alignment: pass
source_ids: [SRC-0016, SRC-0017, SRC-0018]
method_ids: [METHOD-0003, METHOD-0002]
experiment_ids: []
exclude_from_synthesis: false
---

# FD-GNN Global Feature Candidate Review (2026-10-14)

**Research state:** Conceptual design, project-lead acknowledged three controlled comparison candidates. No performance validation, implementation, formal experiment or Method selection.

## Scope preserved

- Research target: **forward** Mask-to-Aerial-Image surrogate under a provisionally fixed optical setup, not ILT or mask optimization.
- Existing three node types remain **Frequency Nodes** `F_k`, **Pair Nodes** `P_{k,l}`, and **Difference Nodes** `D_q`.
- Frequency--Pair incidence and Pair--Difference output routing `q=k-l` remain; do not insert Frequency--Frequency edges, virtual nodes, or a fourth graph node.
- Frequency initialization includes `Re A(k)`, `Im A(k)`, and normalized **absolute** `k_x,k_y`. Real-space pixel coordinates are not added.
- `p_{k,l}=A(k)A*(l)` is deterministic; internal Pair hidden messages must not be confused with physically routed final Pair contributions.
- Candidate two-round internal scheme: high-dimensional Pair messages `z_{k,l}` conditional on incident Frequency states, complex Pair product and difference; Frequency aggregation through learnable attention plus elementwise max, with residual hidden updates `h_k^(1),h_k^(2)`. These are **unimplemented design candidates**; illustrative widths such as 32D are not fixed.
- Mode Head produces `R` learned complex values `b_r(k;M)` per frequency node. Neither individual modes nor an individual pair interaction need identifiable physical-mode labels.
- Final renderer retains `C_{k,l}=A(k)A*(l) Σ_r b_r(k;M)b_r*(l;M)`, `I_hat(q)=Σ_{k-l=q} C_{k,l}`, inverse FFT, and aerial-image-level training loss.

## Why consider an explicit global representation?

Two complete Frequency->Pair->Frequency rounds only exchange information within at most two hops of the **induced Frequency adjacency** (used for analysis, not added to the actual graph). The coverage depends on Pair selection/density, and even high reachability may compress information through fixed-width hidden features. If the Frequency graph is sampled, pooling its nodes does not automatically expose Fourier components absent from the sampled graph. These are structural concerns and **not** experimental proof that global context improves accuracy.

A common mask-specific context can condition all per-frequency Mode Head outputs. It is computed **per mask, never across the mini-batch**. How well it preserves 2D frequency structure, phase, and translational behavior remains unverified.

## Three acknowledged architecture candidates

| ID | Per-frequency generator input | Global source | Purpose and limitation |
| --- | --- | --- | --- |
| **L0** | `Gθ(h_k^(2))` | None | Essential local-only control; simplest but depends on two-round information coverage |
| **G1** | `Gθ(h_k^(2), g_M^graph)` | Per-mask pooling/encoding of **all available Frequency hidden states** `{h_j^(2)}` | Cheap shared graph context; potentially limited by sampled Frequency coverage and pooled-vector information loss |
| **G2** | `Gθ(h_k^(2), g_M^spectrum)` | Separate encoder reading the **complete input Mask Fourier spectrum** `{Re A(j), Im A(j), j_x, j_y}` | Can access frequencies omitted by Pair sampling; encoder design, compute and phase handling are unresolved |

G1 may initially test mean-plus-max pooling and an MLP. The fusion for G1/G2 can first use simple concatenation; FiLM is a follow-on **candidate**, not a frozen requirement. G2's encoder is deliberately **not yet selected**: frequency-aware pooling, attention and structured 2D spectral encoding remain design options. No new graph node/edge is required.

## Key distinctions and checks

1. Report two-round coverage `C2 = (1/N) Σ_k |R2(k)|/N`, where `R2(k)` contains up-to-two-hop Frequency neighbors in the induced analytic graph. Record active Frequency count, Pair count, and number of omitted spectrum locations; `C2` is not a measure of information preservation.
2. Compare L0/G1/G2 under the **same** input masks, sampled Pair routing, two-round MP, output contract, train/validation/test splits, `R`, and budget, including a parameter-matched local control.
3. Measure image MSE/NMSE/SSIM, difference-frequency error `E(q)`, IID versus held-out mask-family generalization, peak memory and latency. These are suggested evaluation dimensions, not a preregistered experiment.
4. If a global candidate is trained later, test dependence on `g_M` with a cross-mask global-feature shuffle and compare gains against `C2` and Frequency sampling coverage.
5. Check complex phase, absolute frequency coordinates, Hermitian FFT consistency, output realness/nonnegativity, FFT indexing, and spatial-shift equivariance. A naive real/imaginary pooled vector need not respect shift symmetry.
6. Fixed-optics physics would give mask-independent TCC for the idealized partially coherent model; mask-conditioned **effective** modes are a flexible surrogate parameterization, not a claim that the physical TCC changes between masks. A mask-independent-mode baseline is a useful additional hypothesis.

## Next design question

**Specify lightweight G2 Global Spectrum Encoder candidates** that retain information about `k_x,k_y`, complex phase and the 2D structure without silently changing the three-node graph; then define how to compare them with G1 graph pooling and L0. Do not freeze encoder, choose a persistent project Method or execute a formal experiment on this record alone.

**Governance:** Canonical Method `METHOD-0003` remains `concept / draft`. Independent direct-pairwise `METHOD-0002` and `METHOD-0001` are unchanged. No Locked Core, ADR, registered Evidence, data contract, simulator, or approved experiment changes.
