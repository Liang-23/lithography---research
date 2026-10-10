---
schema_version: "1.0"
id: SRC-0006
type: source-record
title: "Adaptive Correction for Ensuring Conservation Laws in Neural Operators"
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
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 1 item 9"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Adaptive Correction for Ensuring Conservation Laws in Neural Operators

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0006_Adaptive_Correction_Neural_Operators.pdf`
- Source type: PDF; arXiv preprint
- Authors: Chaoyu Liu, Yangming Li, Zhongying Deng, Chris Budd, Carola-Bibiane Schönlieb
- Publication/version date: arXiv `2505.24579v2 [cs.LG]`; 2026-03-07
- DOI: `10.48550/arXiv.2505.24579`
- Imported/registered date: 2026-08-30
- Original location: `https://arxiv.org/pdf/2505.24579v2`
- Language: English
- License/access restriction: arXiv non-exclusive distribution license; lawful arXiv full text
- Version relationship: The approved and admitted artifact is arXiv v2. No published superseding version was verified at admission.

## Integrity

- File size: 5,362,527 bytes
- PDF page count: 21
- Hash algorithm: SHA-256
- Content hash: `77801C5E9B3B31BC361C0B8016BD0B9C02C555F5EE0CDCDF7F974AD19D61D8F9`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate evidence on learnable terminal correction operators for conserving linear and quadratic quantities in high-dimensional neural-operator fields.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow.
- Prohibited use: Treating admission as verified Evidence; inferring a lithography constraint from adjacent PDE invariants; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: None affecting admission; exact arXiv v2 identity is printed in the PDF.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of method equations, theorem, benchmark setup, Tables 2–6, figures, appendices, and limitations
- Notes: Integrity and version identity are source-checked. Scientific claims and reported results remain source-reported and are not independently verified Evidence.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF and manuscript page numbers coincide.

### Corrector and output dimensionality

- The proposed plug-and-play terminal corrector enforces one global linear or quadratic conservation law while a learnable vector allocates correction over the neural-operator field. [PDF pp. 1–5, Abstract and Sections 1–3]
- For $\sum_iU_i=m_0$, the corrected field is

$$
L(m_0,U)=U+\bigl(m_0-M(U)\bigr)A,
\qquad
\sum_iA_i=1.
$$

[PDF pp. 3–4, Eqs. (3)–(8)]
- For $\sum_iU_i^2=c_0$, the paper parameterizes $U_{\mathrm{new}}=\lambda_1U+\lambda_2A$ and gives closed-form coefficients. Unlike the optimization-projection baseline, the proposed operator has no minimum-distance objective; it learns the spatial allocation $A$. [PDF pp. 2–4, Eq. (2) and Eqs. (9)–(18)]
- Benchmarks include UNet, GTNO, and FNO on 2D transport, conservative Allen–Cahn, shallow water, compressible Navier–Stokes, and 1D Schrödinger systems. Confirmed 2D grids include $128\times128$; Schrödinger fields have shape $(2,128)$. [PDF pp. 5–7, Sections 4.1–4.2; PDF pp. 13–14, Appendices A.3–A.5]

### Training, gradients, and inference

- $A$ is produced by a lightweight convolution or MLP and trained jointly with the raw neural operator through ordinary reconstruction targets. The terminal corrector remains at every inference. [PDF pp. 4–5; PDF p. 14, Appendix A.4]
- There is no external teacher, corrected-target dataset, distillation stage, or student-only deployment.
- Theorem 3.1 compares ideal best reconstruction losses and states a function-class inclusion under its assumptions. It is not empirical proof that unconstrained hidden-representation freedom improves learning. [PDF p. 5, Eqs. (19)–(20)]
- No gate, trust region, fallback, correction bound, or damaging-correction detector is provided. The method is restricted to one linear or quadratic global invariant at a time. [PDF p. 8, Section 5]

### Major reported results and failure evidence

- Table 2 reports lower prediction error for every proposed corrected counterpart across the tested architecture/system combinations; examples include FNO conservative Allen–Cahn $2.01\times10^{-2}$ to $1.65\times10^{-2}$ and GTNO shallow water $1.55\times10^{-2}$ to $0.78\times10^{-2}$. [PDF p. 7, Table 2]
- The proposed method and optimization-projection baseline report conservation error `0.00 ± 0.0` across the test cases. This is recorded as printed numerical precision, not independent proof beyond the source. [PDF p. 7, Table 4]
- The loss-weight sweep is highly task-sensitive and transfers poorly: for example, a norm case rises to $90.1\%$ conservation error at $\lambda=10^{-3}$. [PDF pp. 7–8, Table 5]
- The optimization projection gives a direct damaging-correction example: conservative Allen–Cahn error changes from raw FNO $2.01\times10^{-2}$ to projected $99.7\times10^{-2}$ while printed conservation error is zero. The proposed adaptive corrector reports $1.65\times10^{-2}$. [PDF p. 7, Tables 3–4; PDF p. 8, “Adaptive Correction vs. Projection method”]
- Projection also modestly worsens several other reported cases while conserving the selected invariant. This supports only a Source-bounded conclusion that exact invariant satisfaction does not guarantee better reference accuracy.

### Limitations and safe boundary

- The source covers one linear or quadratic conservation law at a time; simultaneous and higher-order laws are future work. It reports no runtime comparison against the optimization projection. [PDF p. 8, Section 5; PDF p. 3, Related Work]
- The manuscript contains a broken internal theorem reference on p. 5. Eq. (18) inserts an unspecified $\epsilon$ in a formula derived for exact equality, while the artifact asserts machine-precision conservation without explaining analytically why nonzero $\epsilon$ preserves it. These are unresolved formulation/reporting details.
- The arXiv banner gives 2026-03-07 while the footer says 2026-03-10; both are retained. Compressible Navier–Stokes grid size is not explicitly confirmed in the appendix resolution sentence.
- **Bounded relevance:** direct high-dimensional field evidence for a learned terminal corrector and direct evidence that a minimum-$L_2$ projection can harm accuracy. It does not establish corrected-target transfer, inference-time removal, universal physics-loss failure, or representation-freedom benefit.

