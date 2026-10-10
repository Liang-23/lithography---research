---
schema_version: "1.0"
id: EV-0005
type: evidence-record
title: "Internal physics-aware attenuation-factor computation during diffusion"
lifecycle_status: active
authority_class: verified-record
authority_scope: atomic-claim-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-09-01
updated_at: 2026-09-01
owner: project-lead
review_status: approved
reviewed_by: project-lead
approved_by: project-lead
approval_ref: "User explicit approval of EV-0004 through EV-0006 current claim wording and applicability boundaries, 2026-09-01"
core_alignment: pass
evidence_state: verified
source_ids: [SRC-0004]
data_ids: []
experiment_ids: []
supports_ids: []
contradicts_ids: []
exclude_from_synthesis: false
---

# Internal physics-aware attenuation-factor computation during diffusion

## Claim

PADM's physics-aware denoising path predicts per-angle path-length fields and a $\mu$ attenuation field, constructs an input-dependent attenuation-correction factor from those predictions, and uses the resulting calculation internally during reverse-diffusion denoising.

## Relationship

- Supports: Source-relative precedent for an input-dependent physics-shaped calculation embedded inside a diffusion predictor.
- Contradicts: Describing the reported PADM mechanism as an external post-prediction projection of a completed neural output onto a defined physical solution space.
- Does not establish: Exact physical-constraint satisfaction, physical accuracy or identifiability of predicted path lengths or $\mu$, differentiation through every physics-module operation, a formal feasibility guarantee, representation-freedom benefit, or lithography applicability.

## Grounding

- `SRC-ID`: `SRC-0004`
- Exact source path: `D:\Litho\2-3nm litho\raw\SRC-0004_PADM.pdf`
- Human Audit basis: `D:\Litho\2-3nm litho\02_Evidence\SRC-0004_PADM.md`, targeted P2 verification.
- Exact locator: PDF p. 4, Figure 1(b) and caption; pp. 5-6, Algorithms 1-2, reverse-process definition, Section 4.4, and Eqs. (7)-(15).
- Evidence form: explicit at-each-step author description plus equation/figure mechanism; bounded inference for composition inside the generic reverse update.
- Verbatim quote: None required.

## What the PDF explicitly establishes

- At diffusion step $t$, the U-Net input is $z^{(t)}=\operatorname{concat}(x_t,C)$.
- Equation (12) predicts $\{s_{\phi_m,\theta}^{(t)}\}_{m=1}^{N}$, $\mu_\theta^{(t)}$, and auxiliary clean-image channel $\tilde x_0^{(t)}$.
- Equation (13) forms an input-dependent $\operatorname{ACF}_\theta^{(t)}$ from an inverse mean of $\exp[-\mu_\theta^{(t)}s_{\phi_m,\theta}^{(t)}]$ terms.
- Equation (10) defines the denoising output using $y\odot\operatorname{ACF}_\theta^{(t)}$.
- Equations (14)-(15) describe a physics-aware module $\mathcal P$ that produces $\bar x^{(t)}$ from predicted $s$ and $\mu$ and blends it with $\tilde x_0^{(t)}$ to produce the refined clean estimate.
- Section 4.4 places this computation at each diffusion step, and Algorithm 2 calls the denoising network in every reverse-sampling iteration.

## Applicability and limitations

- Conditions: The PADM physics-aware Brownian Bridge diffusion mechanism reported in the admitted arXiv `2511.06948v1` artifact.
- Valid scope: Predicted attenuation-related fields parameterize an ACF and refined denoising estimate within the iterative model path.
- Excluded scope: An external final-output projector, a projection onto a defined physical solution set, exact feasibility, direct physical-field supervision, or verified physical truth of the learned latent fields.
- Explicit non-support: No direct loss, range constraint, field ground truth comparison, identifiability analysis, or physical-accuracy metric is reported for $s_{\phi_m}$ or $\mu$. Differentiation through every operation of $\mathcal P$ is not explicitly documented.
- Assumptions: The redefined $X_\theta$ in Section 4.4 is the denoising function called by the generic loss and sampling equations.
- Limitations: $\mathcal P$ is not expanded algorithmically; $\mu_\theta$ is overloaded between the reverse Gaussian mean on p. 5 and the attenuation field on p. 6; and Eqs. (10), (14)-(15), and Algorithm 2 do not fully specify one implementation-level composition.
- Alternative interpretation: The physics-aware block could be implemented as a distinct software module, but the paper places it inside every denoising step rather than after a completed final prediction.
- Confidence: Medium-high for the internal ACF mechanism; lower for undocumented gradient and implementation details.
- Project relevance: Distinguishes internal physics integration from the project's separate candidate family of external physical correction followed by knowledge transfer.

## Conflicting evidence

- Contradicting `EV-ID`s: None.
- Conflict status: No direct conflict; notation and composition ambiguities are retained as limitations.

## Verification

- Provenance checked: Yes; admitted arXiv `2511.06948v1`, SHA-256 `EC7AAFC92B072C406DE957AB164531D81CFF435D3A34D2D2668EB8740012A3EF`.
- Locator checked: Yes; locators were checked against the original PDF during the completed targeted Human Audit recorded on 2026-09-01.
- Calculation reproduced: Not applicable.
- Reviewed by/date: Project lead / 2026-09-01, following AI Agent materialization and source check.
- Approval reference: User explicit approval of `EV-0004` through `EV-0006` current claim wording and applicability boundaries, 2026-09-01.
- Evidence state: `verified` within the recorded applicability boundary.
