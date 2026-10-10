---
schema_version: "1.0"
id: SRC-0012
type: source-record
title: "Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-and-source-check
created_by: ai
content_origin: external-source
created_at: 2026-08-30
updated_at: 2026-09-13
owner: project-lead
review_status: source-checked
tier2_review_status: agent-complete
human_audit_status: not-started
reviewed_by: AI Agent
approved_by: project-lead
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 2 item 10"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0012_Pinet.pdf`
- Source type: PDF; arXiv preprint and ICLR 2026 conference paper
- Authors: Panagiotis D. Grontas, Antonio Terpin, Efe C. Balta, Raffaello D’Andrea, John Lygeros
- Publication/version date: arXiv `2508.10480v2 [cs.LG]`; 2026-02-18; published at ICLR 2026
- DOI: `10.48550/arXiv.2508.10480`
- Imported/registered date: 2026-08-30
- Original location: `https://arxiv.org/pdf/2508.10480v2`
- Language: English
- License/access restriction: Creative Commons Attribution 4.0 International (`CC BY 4.0`); lawful arXiv full text
- Version relationship: The approved and admitted artifact is exact arXiv v2. The conference stylizes the title as `ΠNet`; this is recorded as the same work, not a separate Source.

## Integrity

- File size: 6,621,519 bytes
- PDF page count: 47
- Hash algorithm: SHA-256
- Content hash: `307E1FB800607A61EB1F2E77805C3325BEAF5FA83E6CF18F10AF6D90326310AE`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate differentiable hard-projection-layer evidence for parametric constrained-optimization proxies, including forward projection, implicit gradients, and inference-time dependency.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow.
- Prohibited use: Treating admission as verified Evidence; treating a persistent projection layer as student-only inference; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. Its navigation-only PDF open action was not executable code; no JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: Non-blocking title alias (`Pinet` versus `ΠNet`) recorded; exact arXiv v2 is unchanged.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of pivotal equations, algorithms, results, ablations, limitations, and gradient-validation pages
- Notes: Integrity and exact arXiv v2 identity are source-checked. Scientific claims and reported results remain source-reported and are not independently verified Evidence.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF and printed page numbers coincide.

### Optimization and projection mechanism

- The task learns a context-to-solution map for

$$
\min_y \varphi(y,x)
\quad\text{subject to}\quad
y\in C(x),
$$

where $C(x)$ is nonempty, closed, and convex. [PDF p. 1, Section 1]
- A backbone produces $y_{\mathrm{raw}}$, then the output layer computes the Euclidean projection

$$
y=\Pi_{C(x)}(y_{\mathrm{raw}})
=\underset{z\in C(x)}{\operatorname{argmin}}\;\lVert z-y_{\mathrm{raw}}\rVert^2.
$$

[PDF p. 3, Eq. (1), Section 2.1]
- The feasible set is represented through an augmented-space intersection $A\cap K$: $A$ is affine and $K$ is a Cartesian product with efficient component projections. Douglas–Rachford splitting performs the iterative projection. [PDF pp. 3–4, Eqs. (2)–(4), Algorithm 1]
- With finite iteration count, the output lies in $A$ and therefore satisfies encoded equalities, but it need not yet lie in $A\cap K$; other feasibility is numerical until convergence. The ideal Euclidean projection is unique for a nonempty closed convex set. [PDF p. 5, Section 2.1.2; PDF pp. 41–42, Appendices D.2–D.3]

### Training, gradients, and inference

- The projection operates during both training and inference. Training minimizes the optimization objective on the projected output and requires no solver labels. [PDF p. 6, Sections 2.2–2.3, Algorithms 2–3]
- Backpropagation uses the implicit function theorem at the limiting fixed point and solves a vector-Jacobian linear system with `bicgstab`; the finite forward state substitutes for the ideal fixed point. Projection is almost everywhere differentiable, with generalized-gradient ambiguity at nonsmooth points. [PDF p. 5, Eqs. (5)–(9); PDF pp. 46–47, Appendix F, Figure 22]
- No corrected target, pseudo-label, teacher, or distillation stage exists. The backbone learns through projection-derived gradients.
- Every deployment inference still executes a finite Douglas–Rachford projection loop with explicit context-dependent constraints. The paper therefore does not provide projector-free or student-only inference.
- There is no accept/reject gate or classical-solver fallback; increasing projection iterations is the mechanism for reducing violation.

### Output dimensionality and reported results

- Standard benchmarks use decision dimensions $d=100$ and $d=1000$. Motion-planning appendices include about $9{,}000$ variables/constraints and a $1024\times1024$ context image, but that image is an input map, not the corrected output. The corrected outputs are optimization and trajectory vectors, not dense spatial fields. [PDF p. 7, Section 3.1; PDF p. 10, Section 3.2; PDF p. 29, Appendix B.4]
- Reported median inference for the large nonconvex benchmark is $0.0063\,\mathrm{s}$ single and $0.2804\,\mathrm{s}$ batch for $\Pi$net, versus $10.159\,\mathrm{s}$ and $10{,}720\,\mathrm{s}$ for the traditional solver. [PDF p. 21, Tables 2–3]
- An ablation comparing end-to-end projection training with attaching projection only at inference reports average relative suboptimality $0.00216$ versus $0.02178$ at an approximately eight-second training budget; both use the projector at inference and therefore have the same constraint-violation behavior. [PDF pp. 37–39, Appendix C.4]
- Too few test-time projection iterations reduce runtime but can worsen relative suboptimality because the output remains far from the projection. [PDF p. 37, Figure 18]

### Limitations and safe boundary

- The explicit method boundary is convex feasible sets; extending to nonconvex constraints is future work. Motion-planning constraints are convex and decoupled between vehicles. [PDF p. 10, Sections 3.2 and 4]
- Performance requires a computable set decomposition with efficient projections and vector-Jacobian products, numerical equilibration, and iteration choices.
- The paper does not study corrected-target transfer, projector removal, dense output-image correction, broad OOD behavior, or whether correction moves a supervised prediction away from its reference.
- **Bounded relevance:** direct prior art for a context-dependent differentiable orthogonal output-projection layer. It demonstrates gradient interaction, not representation freedom as an independently controlled experimental variable.

## 用户阅读结论 — 2026-09-13

用户已理解本轮最值得保留的机制：将 Projection 放在 loss 之前，以 projected output 计算 loss，并让梯度经过 Projection 更新 neural network 参数。关键不仅是前向顺序，还包括该 gradient path；Projection 本身不是 optimizer。[PDF pp. 5–6, Eqs. (5)–(9), Algorithms 2–3]

用户认为这一核心观点已经吸收，是否改善光刻 raw prediction、是否保留表示能力以及推理成本是否合适，需要由本项目自己的实验确认。该阅读进度不等于全文 Human Audit；claims remain unverified。用户未据此选择 through-Projection 作为项目 Method。

本节由 Agent 整理，`content_origin: ai-assisted`。HYP-0002 将这一机制作为与 corrected-target transfer 比较的路径；不改变论文推理时仍保留 Projection 的边界。
