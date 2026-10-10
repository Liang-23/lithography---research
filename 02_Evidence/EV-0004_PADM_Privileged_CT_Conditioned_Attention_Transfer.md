---
schema_version: "1.0"
id: EV-0004
type: evidence-record
title: "Privileged CT-conditioned attention transfer to a CT-free Student"
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

# Privileged CT-conditioned attention transfer to a CT-free Student

## Claim

In PADM, the Teacher uses privileged CT-derived attenuation-map conditioning during training and supplies a normalized aggregated representation for attention transfer to the Student, while the Student uses NAC-only conditioning and does not require the CT-derived attenuation map at inference.

## Relationship

- Supports: Source-relative precedent for transferring training-only privileged CT conditioning into a Student whose deployed input boundary excludes the CT-derived attenuation map.
- Contradicts: An interpretation of the mathematically specified PADM transfer loss as corrected-output distillation from a Teacher-generated AC label.
- Does not establish: Generic success of privileged-physics transfer, Teacher-corrected output labels, removal of the Student's physics-aware architecture, representation-freedom benefit, lithography applicability, or superiority to other transfer mechanisms.

## Grounding

- `SRC-ID`: `SRC-0004`
- Exact source path: `D:\Litho\2-3nm litho\raw\SRC-0004_PADM.pdf`
- Human Audit basis: `D:\Litho\2-3nm litho\02_Evidence\SRC-0004_PADM.md`, targeted P1 and P3 verification.
- Exact locator: PDF p. 4, Figure 1 and Eqs. (3)-(4); p. 5, Eqs. (5)-(6), Algorithm 1, Eq. (9), and the piecewise definition of $C$; p. 6, Section 4.5 and Eqs. (16)-(18); p. 8, Conclusion.
- Evidence form: explicit author statement plus mechanism visible in equations/figure; bounded inference for Teacher absence from the completed Student execution path.
- Verbatim quote: None required.

## What the PDF explicitly establishes

- PADM-T is defined as $\hat I_{AC}^{T}\sim T_\theta(I_{NAC},A)$, and PADM-S as $\hat I_{AC}^{S}\sim S_\phi(I_{NAC})$.
- Reverse-process conditioning is $C^T=\operatorname{CrossAttn}(y,A)$ for the Teacher and $C^S=y$ for the Student.
- The Teacher remains frozen during Student training.
- The specified transfer representations are $Q_T=\operatorname{Agg}(C^T)$ and $Q_S=\operatorname{Agg}(C^S)$, and Eq. (17) matches their $L_2$-normalized forms.
- The Student objective is $\mathcal L_{Total}=\mathcal L_{ELBO}+\lambda\mathcal L_{AT}$.
- Paired AC image $x_0$ remains the diffusion target in Algorithm 1 and Eq. (9); no equation or algorithm supplies a Teacher-corrected AC output as the Student label.
- The Student is described as performing inference using only NAC slices, and the Conclusion says CT-based attenuation-map input is not required during inference.

## Applicability and limitations

- Conditions: The PADM Teacher-Student procedure reported for NAC-to-AC cardiac SPECT synthesis in the admitted arXiv `2511.06948v1` artifact.
- Valid scope: The CT-derived attenuation map is privileged Teacher-side conditioning; the mathematically specified Teacher-dependent Student loss is normalized attention/representation matching; the deployed Student input is NAC only.
- Excluded scope: Corrected-output distillation, a Teacher-output label corpus, a physics-free Student, universal transfer effectiveness, or any lithography-specific claim.
- Explicit non-support: The PDF does not specify Teacher-corrected output labels as Student supervision. Removing $A$ from Student inference does not remove the Student's own diffusion or physics-aware architecture.
- Assumptions: The reported frozen-Teacher training procedure is followed and no unreported Teacher call is inserted into deployment.
- Limitations: `Agg`, source layers, and tensor shapes are undefined; Eq. (16) sets $C^S=y$ while calling it a Student attention feature; Figure 1 labels U-Net feature distillation; and prose about replicating Teacher outputs is broader than the printed objective.
- Alternative interpretation: The prose could suggest output imitation, but Eqs. (16)-(18) instantiate attention matching rather than a Teacher-output label loss; this record follows the explicit objective.
- Confidence: Medium-high because the input boundary, frozen Teacher, and loss are explicit, while the exact transferred tensor is under-specified.
- Project relevance: Establishes a bounded training-only privileged-information precedent while preserving the distinction from external corrector output distillation.

## Conflicting evidence

- Contradicting `EV-ID`s: None.
- Conflict status: No external conflict identified; the internal prose/equation mismatch is retained as a limitation.

## Verification

- Provenance checked: Yes; admitted arXiv `2511.06948v1`, SHA-256 `EC7AAFC92B072C406DE957AB164531D81CFF435D3A34D2D2668EB8740012A3EF`.
- Locator checked: Yes; locators were checked against the original PDF during the completed targeted Human Audit recorded on 2026-09-01.
- Calculation reproduced: Not applicable.
- Reviewed by/date: Project lead / 2026-09-01, following AI Agent materialization and source check.
- Approval reference: User explicit approval of `EV-0004` through `EV-0006` current claim wording and applicability boundaries, 2026-09-01.
- Evidence state: `verified` within the recorded applicability boundary.
