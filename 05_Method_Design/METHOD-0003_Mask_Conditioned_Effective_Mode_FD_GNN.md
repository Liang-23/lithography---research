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
- Frequency Node: initial feature $h_k^{(0)}=[\operatorname{Re}A(k),\operatorname{Im}A(k),\widetilde k_x,\widetilde k_y]$ with **absolute normalized frequency coordinates**. Do not add real-space pixel $(x,y)$ coordinates to this candidate.
- Known Pair Product: $p_{k,l}=A(k)A^*(l)$.
- Routing: $q=k-l$ (exact modular vs padded FFT specification pending).
- Generator: $b_r(k)=G_\theta(A)_{r,k}$ with $R$ complex coefficients per frequency; $R$ unspecified.
- Physical contribution $c_{k,l}=A(k)A^*(l)\sum_{r=1}^{R}b_r(k)b_r^*(l)$.
- Output spectrum: $\widehat I(q)=\sum_{k-l=q}c_{k,l}$; spatial intensity $I=\mathcal F^{-1}[\widehat I]$ with consistent FFT normalization and real/intensity validity requirements.
- Ground truth: final Aerial Image only; no effective-mode label.

## 3. Inference and training
In a single forward evaluation: Mask FFT -> GNN internal feature learning -> mask-conditioned effective-mode prediction -> differentiable pairwise quadratic renderer -> predicted Aerial Image. Backpropagate image loss through all differentiable steps during training; no per-Mask inference-time optimization.

## 4. Internal three-node graph and high-dimensional message candidate

**Graph types unchanged:** Frequency Nodes `F_k`, Pair Nodes `P_{k,l}` and Difference Nodes `D_q`. Only existing Frequency--Pair incidence and Pair--Difference `q=k-l` routing are used. Difference Nodes remain part of the output aggregation; whether they should additionally update hidden features is unresolved.

The earlier difference-conditioned scalar/complex aggregation
$$s_k=\sum_{l\in\mathcal N(k)}w_\theta(k-l)p_{k,l}$$
is retained as **Candidate A for comparative testing**, not promoted into the current default.

The project lead subsequently acknowledged a richer conceptual alternative:
1. Pair Node `P_{k,l}` constructs learnable high-dimensional states/messages from incident `h_k^{(t)},h_l^{(t)}`, known complex product `p_{k,l}=A(k)A^*(l)`, and the difference `q=k-l`; complex values are supplied to real neural modules as real/imaginary channels.
2. Pair-to-incident-Frequency messages are aggregated with **attention plus elementwise max** as an initial multistatistic candidate, then used in residual Frequency updates. The exact message functions, target-specific message orientation, channel widths and normalization remain open.
3. Two complete Frequency->Pair->Frequency rounds are the **working depth for comparison**, producing `h_k^(1)` and `h_k^(2)`, not a proven optimum. A two-round receptive field covers at most two hops in the analytically induced Frequency graph, with actual coverage controlled by sparse Pair connectivity.

The internal Pair hidden message is **not** the final rendered complex Pair contribution; these are separate operations.

## 5. Effective Mode Head and three global-context alternatives

Let `h_k = h_k^(2)`, and let `g_M` denote per-mask context. The Mode Head emits `2R` real channels, interpreted as `R` complex effective-mode coefficients `b_r(k;M)`; the same network weights are shared across frequency nodes, and the modes have no individually supervised physical-mode labels.

**The project lead accepted the motivations and preservation boundaries of three alternatives for study, not their superiority or permanent selection:**

| ID | Candidate head | Source of global information | Main risk |
| --- | --- | --- | --- |
| L0 (local only) | $\mathbf b(k;M)=G_\theta(h_k)$ | None | Restricted by two-round information coverage |
| G1 (graph-global) | $\mathbf b(k;M)=G_\theta(h_k,g_M^{\rm graph})$ | $g_M^{\rm graph}=E_g(\{h_j^{(2)}\}_{j\in\mathcal K_{\rm graph}})$; inexpensive mean+max readout is a starting candidate | Graph selection may omit Fourier coefficients; pooling loses structure |
| G2 (full-spectrum-global) | $\mathbf b(k;M)=G_\theta(h_k,g_M^{\rm spectrum})$ | $g_M^{\rm spectrum}=E_s(\{\operatorname{Re}A(j),\operatorname{Im}A(j),\widetilde j_x,\widetilde j_y\}_{j\in\mathcal K_{\rm full}})$ | Full-grid encoder must preserve relevant 2D frequency/phase relationships efficiently |

The global representation is recomputed **separately for each Mask**, never pooled across separate Mask samples. Both G1 and G2 use a **side-channel into the Generator**, not a fourth node type or new graph edges. Initial fusion can be concatenation; FiLM/attention fusion remains a later candidate. For G2, no particular `E_s` architecture has been selected yet: frequency-aware pooling, structured 2D spectral encoders and attention-based readout are unresolved alternatives.

In all cases the **same final renderer** is used:
$$C_{k,l}=A(k)A^*(l)\sum_{r=1}^R b_r(k;M)b_r^*(l;M), \quad \widehat I(q)=\sum_{P_{k,l}\to D_q} C_{k,l}.$$

If final Pair routing is sampled, `I_hat(q)` is a sparse approximation of the complete quadratic sum. Full-spectrum context does **not** restore the missing pairwise renderer terms by itself.

## 6. Risks, diagnostics and study requirements

- **Receptive-field diagnostic:** Compute induced Frequency two-round reachability `C2=(1/N) Σ_k |R2(k)|/N`, and distinguish node reachability from fidelity of compressed hidden representations.
- **Controlled comparison:** Keep FFT conventions, Pair selection, two MP rounds, `R`, loss and dataset split fixed for L0/G1/G2; also compare against a parameter-matched L0 and, later, deeper local MP.
- **Generalization:** Assess held-out Mask families versus IID masks, spectral errors by Difference Node, and inference latency/memory, not just training loss. Numerical acceptance thresholds and experiments are **not approved**.
- **Mask Spectrum:** Decide whether active Frequency nodes equal the full FFT grid; if not, `g_M^graph` is not equivalent to a full-spectrum encoder.
- **Optical behavior:** For fixed optics, the canonical physical TCC is mask-independent. Mask-dependent *effective* modes are a flexible predictive parametrization, not a claim of a changing physical TCC.
- **Complex contracts:** Inspect phase preservation, absolute frequency coordinates, Hermitian consistency, real reconstructed intensity, nonnegativity, FFT normalization, and shift equivariance of global summaries.
- **Modes:** Individually learned effective-mode channels are not uniquely identifiable; compare aerial outputs and effective kernel diagnostics rather than matching channels to physical optical modes.
- **Governance:** Literature and Deep Research discussion motivate candidates but are not verified Source-derived Evidence for this project.

## 7. Governance and next design boundary

The three generator inputs L0/G1/G2 are **acknowledged conceptual research candidates** (progress addendum `08_Project_Status/FD_GNN_Global_Context_Candidates_2026-10-14.md`). `METHOD-0003` remains `concept`/`draft`, not implemented, tested or selected. No `EXP` plan, thresholds, data freeze, Evidence promotion, ADR acceptance, or Core change is implied. `METHOD-0002` and `METHOD-0001` remain independent and unchanged. Next: study exact lightweight G2 `Global Spectrum Encoder` input/phase/2D-structure design.
