---
schema_version: "1.0"
id: EVIDENCE-LEDGER
type: evidence-register
lifecycle_status: active
authority_class: derived
authority_scope: evidence-index-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User request on 2026-08-26"
created_at: 2026-08-26
updated_at: 2026-09-01
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
exclude_from_synthesis: true
---

# Evidence Ledger

| EV-ID | Atomic claim | Supports / contradicts | Source/Data/Experiment IDs | Exact locator | Evidence state | Applicability | Record |
|---|---|---|---|---|---|---|---|
| EV-0001 | NewPINNs uses the current neural field to obtain a dynamic black-box solver response that participates in the loss, while backpropagation does not differentiate through the solver mapping. | Supports training-time black-box physics feedback; does not establish projection, distillation, or feasibility | SRC-0003 | PDF p. 3, Figure 1; pp. 5–9, Eqs. (6)–(22), Algorithms 1–2, Section 2.3; p. 22 exception | verified; project-lead Human Audit 2026-09-01 | Reported NewPINNs training only; solver value affects the loss; $\partial S/\partial u$ is not evaluated; shallow-water warm-start exception retained | [Record](EV-0001_NewPINNs_State_Dependent_Black_Box_Solver_Feedback.md) |
| EV-0002 | Reported NewPINNs forward evaluation directly produces spatial fields with the trained network and does not show the conventional solver in the forward prediction path. | Supports direct neural prediction after solver-coupled training; does not establish deployment speedup or safety | SRC-0003 | PDF p. 6; pp. 12, 17–18, 21–24 | verified; project-lead Human Audit 2026-09-01 | Structural evaluation-path claim only; solver remains the reference generator | [Record](EV-0002_NewPINNs_Direct_Neural_Field_Prediction.md) |
| EV-0003 | NewPINNs inherits solver accuracy, stability requirements, invariant structure, and computational cost and reports problem-specific stabilization measures. | Supports solver-dependence/cost limitations; contradicts universal-safe-correction interpretations | SRC-0003 | PDF p. 8; pp. 10, 15, 22–25 | verified; project-lead Human Audit 2026-09-01 | Reported PDE/solver settings only; no exact-feasibility or deployment-safety proof | [Record](EV-0003_NewPINNs_Solver_Inherited_Limitations.md) |
| EV-0004 | PADM uses privileged CT-derived attenuation-map conditioning on the Teacher side and transfers a normalized aggregated representation to a NAC-only Student through attention matching. | Supports training-only privileged CT conditioning with CT-free Student deployment; contradicts corrected-output-distillation interpretations of the specified loss | SRC-0004 | PDF p. 4, Figure 1, Eqs. (3)–(4); p. 5, Eqs. (5)–(6), Algorithm 1, Eq. (9), piecewise $C$; p. 6, Eqs. (16)–(18); p. 8, Conclusion | verified; project-lead approval 2026-09-01 | Reported PADM only; paired AC remains the diffusion target; exact transferred tensor is under-specified; Student physics-aware architecture remains | [Record](EV-0004_PADM_Privileged_CT_Conditioned_Attention_Transfer.md) |
| EV-0005 | PADM predicts per-angle path-length fields and a $\mu$ attenuation field, constructs an input-dependent ACF, and uses it internally during reverse-diffusion denoising. | Supports internal physics-shaped prediction; contradicts external post-prediction projection interpretations | SRC-0004 | PDF p. 4, Figure 1(b); pp. 5–6, Algorithms 1–2, Eqs. (7)–(15), Section 4.4 | verified; project-lead approval 2026-09-01 | Internal mechanism only; no exact feasibility, physical-field validation, identifiability, or fully specified differentiation path | [Record](EV-0005_PADM_Internal_Physics_Aware_Attenuation_Factor_Computation.md) |
| EV-0006 | PADM-S removes PADM-T and CT-derived attenuation-map conditioning from inference while retaining iterative reverse diffusion and, structurally, its physics-aware denoising path. | Supports privileged-input removal; contradicts corrector-free, physics-free, or one-pass inference interpretations | SRC-0004 | PDF p. 4, Figure 1 and Eq. (4); p. 5, piecewise $C$; p. 6, Algorithm 2 and Eqs. (10)–(15); p. 7, Tables 3–4 context; p. 8, Conclusion | verified; project-lead approval 2026-09-01 | Student physics path is structurally reconstructed; no measured inference runtime, speedup, safety gate, fallback, or Student-only sampling algorithm | [Record](EV-0006_PADM_Privileged_Input_Removal_Retains_Diffusion_Physics_Inference.md) |

## Rules

- Allocate from `EV-0001`; never reuse an ID.
- One record supports or contradicts one atomic claim.
- Every claim needs an exact locator and bounded applicability.
- `quote`, `paraphrase`, `calculation`, `observation`, and `inference` must be distinguished.
- Conflicting Evidence remains visible.
- Wiki pages and AI summaries cannot be the sole support for `verified` Evidence.
- Use `_templates/Evidence_Record_Template.md` for detailed records.
