---
schema_version: "1.0"
id: EV-0006
type: evidence-record
title: "Privileged-input removal without removing diffusion or physics-aware inference"
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

# Privileged-input removal without removing diffusion or physics-aware inference

## Claim

In the reported PADM inference structure, PADM-S removes PADM-T and CT-derived attenuation-map conditioning but retains iterative reverse diffusion and, structurally, the Student's own physics-aware denoising path.

## Relationship

- Supports: Source-relative precedent for removing privileged Teacher-side deployment inputs while retaining the learned Student model's internal predictive machinery.
- Contradicts: Interpreting PADM-S as a completely corrector-free, physics-free, or one-pass inference architecture.
- Does not establish: Measured inference-time acceleration, a runtime speedup factor, a separate Student-only sampling implementation, a deployment safety gate or fallback, exact feasibility, representation-freedom benefit, or lithography applicability.

## Grounding

- `SRC-ID`: `SRC-0004`
- Exact source path: `D:\Litho\2-3nm litho\raw\SRC-0004_PADM.pdf`
- Human Audit basis: `D:\Litho\2-3nm litho\02_Evidence\SRC-0004_PADM.md`, targeted P4 verification.
- Exact locator: PDF p. 4, Figure 1 and Eq. (4); p. 5, piecewise definition of $C$ and reverse-process description; p. 6, Algorithm 2, Sampling Process, Section 4.4, and Eqs. (10)-(15); p. 7, Tables 3-4 and Section 5.2 supporting context; p. 8, Conclusion.
- Evidence form: explicit input-boundary statement plus algorithm/figure structure and reasonable inference from the same-architecture and denoising definitions; direct table observation for supporting numerical context.
- Verbatim quote: None required.

## What the PDF explicitly establishes

- Equation (4) defines PADM-S inference from $I_{NAC}$, and the Conclusion states that CT-based attenuation-map input is not required during inference.
- Student conditioning is $C=y$, whereas Teacher conditioning is $C=\operatorname{CrossAttn}(y,A)$.
- Section 4.5 confines the frozen Teacher to Student training.
- Algorithm 2 initializes $x_T=y$ and iterates from $t=T$ to $1$, so the reported inference structure is reverse-diffusion sampling rather than one-pass prediction.
- Section 4.4 redefines the denoising network at each diffusion step through the physics-aware ACF path. Figure 1 shows reverse processes for PADM-T and PADM-S, and the Student is stated to use the same architecture as the Teacher.
- At 16 projections, Tables 3-4 report PADM-T/PADM-S as RMSE $0.0217/0.0218$, SSIM $0.9796/0.9795$, and PSNR $34.98/34.75$.

## Applicability and limitations

- Conditions: The reported PADM-S architecture and sampling procedure for the CardiAC experiments in the admitted arXiv `2511.06948v1` artifact.
- Valid scope: Teacher/CT conditioning is absent from the Student input path; iterative diffusion remains; the Student physics-aware path follows structurally from the common architecture and denoising definition.
- Excluded scope: A corrector-free or physics-free architecture, one-pass inference, measured deployment speed, runtime acceleration, or a separate verified Student implementation trace.
- Explicit non-support: The paper provides no inference latency, throughput, speedup factor, sampling-step count, deployment gate, fallback, or Student-only Algorithm 2 that expands $\mathcal P$.
- Assumptions: PADM-S uses the reported same architecture and the Section 4.4 denoising definition with Student condition $C=y$.
- Limitations: The Student physics-module inference path is reconstructed from Figure 1, the same-architecture statement, Section 4.4, and generic Algorithm 2 rather than stated in a separate Student-only inference algorithm. The reported numerical gap has no uncertainty or statistical-significance analysis and grows at higher projection counts.
- Alternative interpretation: DDIM is described as accelerating generation relative to standard Markovian diffusion, but that methodological statement is not a measured PADM inference-time comparison.
- Supporting numerical context: At 16 projections, the absolute PADM-S versus PADM-T differences are $0.0001$ RMSE, $0.0001$ SSIM, and $0.23\,\mathrm{dB}$ PSNR.
- Confidence: High for Teacher/CT removal and iterative sampling; medium-high for the structurally reconstructed Student physics-aware path.
- Project relevance: Prevents upgrading privileged-input removal into a claim that all physics/diffusion machinery disappears from deployment.

## Conflicting evidence

- Contradicting `EV-ID`s: None.
- Conflict status: No direct conflict; the absence of a separate Student sampling algorithm is retained as an inference boundary.

## Verification

- Provenance checked: Yes; admitted arXiv `2511.06948v1`, SHA-256 `EC7AAFC92B072C406DE957AB164531D81CFF435D3A34D2D2668EB8740012A3EF`.
- Locator checked: Yes; locators were checked against the original PDF during the completed targeted Human Audit recorded on 2026-09-01.
- Calculation reproduced: Yes; absolute differences from the 16-projection PADM-T/PADM-S values are $|0.0218-0.0217|=0.0001$, $|0.9795-0.9796|=0.0001$, and $|34.75-34.98|=0.23\,\mathrm{dB}$.
- Reviewed by/date: Project lead / 2026-09-01, following AI Agent materialization and source check.
- Approval reference: User explicit approval of `EV-0004` through `EV-0006` current claim wording and applicability boundaries, 2026-09-01.
- Evidence state: `verified` within the recorded applicability boundary.
