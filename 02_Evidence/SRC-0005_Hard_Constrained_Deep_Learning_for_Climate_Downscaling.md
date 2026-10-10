---
schema_version: "1.0"
id: SRC-0005
type: source-record
title: "Hard-Constrained Deep Learning for Climate Downscaling"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-and-source-check
created_by: ai
content_origin: external-source
created_at: 2026-08-30
updated_at: 2026-08-30
owner: project-lead
review_status: source-checked
tier2_review_status: agent-complete
human_audit_status: not-started
reviewed_by: AI Agent
approved_by: project-lead
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 1 item 8"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Hard-Constrained Deep Learning for Climate Downscaling

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0005_Hard_Constrained_Climate_Downscaling.pdf`
- Source type: PDF; peer-reviewed journal article
- Authors: Paula Harder, Alex Hernandez-Garcia, Venkatesh Ramesh, Qidong Yang, Prasanna Sattegeri, Daniela Szwarcman, Campbell D. Watson, David Rolnick
- Publication/version date: *Journal of Machine Learning Research* 24(365):1–40; published 2023-12
- Identifier: JMLR article `23-0158`; no journal DOI assigned
- Imported/registered date: 2026-08-30
- Original location: `https://www.jmlr.org/papers/v24/23-0158.html`
- Language: English
- License/access restriction: Creative Commons Attribution 4.0 International (`CC BY 4.0`); lawful JMLR full text
- Version relationship: The approved and admitted artifact is the JMLR 2023 published version. Related arXiv `2208.05424` was not substituted.

## Integrity

- File size: 7,397,445 bytes
- PDF page count: 40
- Hash algorithm: SHA-256
- Content hash: `235C7B7CB410C000B77F9A93698B8132D5E7CB33F5C3D3DD331A5BA6D72AE1F5`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate high-dimensional evidence on hard terminal consistency layers for climate and image-like spatial downscaling outputs, including predictive-quality and constraint metrics.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow.
- Prohibited use: Treating admission as verified Evidence; generalizing the paper's aggregation constraint to lithography; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. Its navigation-only PDF open action was not executable code; no JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: Embedded title metadata is blank, but the title page, authors, journal header, article number, and publication dates identify the approved JMLR version.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of method equations, principal tables/figures, damaging-constraint evidence, and limitations
- Notes: The JMLR title page spells the fifth author's surname `Sattegeri`; a related record may use a different spelling. This metadata discrepancy does not change the admitted artifact.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF and printed JMLR page numbers coincide.

### Output constraint and dimensionality

- The paper appends deterministic terminal layers to climate/weather super-resolution networks. For each low-resolution value $x$ and its corresponding $n=N^2$ high-resolution patch values $y_i$, the core relationship is

$$
\frac{1}{n}\sum_{i=1}^{n}y_i=x,
$$

with optional $y_i\ge0$. [PDF p. 5, Eqs. (1)–(2), Section 3.1]
- Given raw prediction $\widetilde y$, AddCL adds the same residual offset, ScAddCL allocates a scaled additive residual, MultCL rescales the patch, and SmCL uses a softmax allocation that also guarantees positivity. These are closed-form correction rules, not a minimum-distance orthogonal projection. [PDF pp. 5–7, Eqs. (3)–(7), Figure 1]
- Demonstrated outputs are genuine images/fields: ERA5 outputs include $(1,128,128)$ and $(3,128,128)$ tensors; WRF outputs $(1,135,135)$; NorESM outputs $(1,64,64)$; natural-image outputs reach $(3,512,512)$. [PDF p. 10, Table 1]

### Training, gradients, and inference

- The terminal layer is included in end-to-end training and remains in inference. Gradients pass through the differentiable correction formulas. Models include SR-CNN, conditional SR-GAN, SR-ConvGRU, and FlowConvGRU. [PDF pp. 5–7, Figures 1–2; PDF pp. 13–15, Sections 5.1–5.3]
- Physics is applied to the terminal output rather than hidden representations, but the source explicitly describes hard constraints as restricting the hypothesis space. It does not isolate hidden-representation freedom as an experimental variable.
- There is no corrected-target dataset, teacher-student transfer, distillation, or eventual removal of the correction layer.
- No trust region, accept/reject gate, fallback, correction-magnitude bound, or prediction-quality detector is provided. Layer choice is the main safeguard: MultCL can be unstable near zero; SmCL is unsuitable when valid values are signed. [PDF pp. 6–7, Section 3.2]

### Major reported results and failure evidence

- On the reported TCW $4\times$ case, the unconstrained CNN has RMSE $0.657$, while SmCL reports $0.582$ with mass violation printed as $0.000$ and zero negative pixels. [PDF p. 25, Table 5]
- In the time-split TCW test, the unconstrained CNN reports RMSE $0.661$ versus SmCL $0.579$, with mass violation $0.059$ versus $0.000$. [PDF p. 27, Table 9]
- Soft-loss tuning shows a bounded accuracy/constraint trade-off: increasing $\alpha$ from $0.0001$ to $0.9999$ reduces reported mass violation only from $0.021$ to $0.017$ while RMSE worsens from $0.241$ to $0.706$; at $\alpha=1$, RMSE is $2.618$. [PDF p. 23, Table 3]
- The NorESM case directly demonstrates constraint mismatch damage. The true LR/HR relation is already violated by RMSE $2.48$. The unconstrained CNN reports RMSE $2.348$ and violation $1.034$; hard layers force printed violation $0.000$ but worsen RMSE to $2.884$–$2.888$. [PDF pp. 27–28, Appendix F; PDF p. 32, Table 14]
- Clipping after a conservation layer can destroy consistency. [PDF p. 23, Appendix B, Table 4]

### Limitations and safe boundary

- The authors state that an incorrect or strongly violated LR/HR relationship can weaken performance and propagate low-resolution input bias. [PDF p. 22, Section 7]
- The correction family requires relationships expressible in the separable form of Eq. (8) and does not directly cover spatial subsampling. Online deployment in a climate model remains future work. [PDF pp. 7–8, Eq. (8); PDF pp. 20–22, Sections 6.7–7]
- Main ERA5 pairs are created by average pooling, so the constraint is exact by construction there; independent WRF/NorESM pairs provide the mismatch tests.
- Table 1 lists a WRF test size of $4{,}000$, whereas Table 2 says metrics over $10{,}000$ test samples; the artifact does not resolve this discrepancy.
- **Bounded relevance:** direct high-dimensional spatial-output precedent for differentiable terminal correction, and direct evidence that satisfying a mismatched imposed relation can worsen reference accuracy. It does not establish corrected-target transfer, projector removal, representation-freedom benefit, or universal failure of physics loss.

