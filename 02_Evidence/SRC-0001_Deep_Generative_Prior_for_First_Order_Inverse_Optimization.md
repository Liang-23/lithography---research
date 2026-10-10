---
schema_version: "1.0"
id: SRC-0001
type: source-record
title: "Deep Generative Prior for First Order Inverse Optimization"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-only
created_by: ai
content_origin: external-source
created_at: 2026-08-27
updated_at: 2026-08-27
owner: project-lead
review_status: source-checked
reviewed_by: AI Agent
approved_by: user
approval_ref: "Explicit source-registration request, 2026-08-27"
core_alignment: conflict
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Deep Generative Prior for First Order Inverse Optimization

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\Deep Physics Prior.pdf`
- Source type: PDF; arXiv preprint
- Author/organization: Haoyu Yang, Kamyar Azizzadenesheli, Haoxing Ren; NVIDIA Research
- Publication/version date: arXiv `2504.20278v2 [cs.AI]`; 2025-10-14
- Imported/registered date: 2026-08-27
- Original location: `https://arxiv.org/abs/2504.20278v2` from embedded PDF metadata
- Language: English
- License/access restriction: arXiv non-exclusive distribution license 1.0, recorded in embedded PDF metadata

## Integrity

- File size: 2,129,743 bytes
- Hash algorithm: SHA-256
- Content hash: `05671BD4F440759C6A033B0619B0AEFFF51D69BECB03A7441F17A651302B5073`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: The paper studies a differentiable forward surrogate and a learned generative prior for first-order inverse optimization. Its discussion of surrogate error, out-of-distribution optimization, and data-manifold constraints may provide bounded comparison context for forward-surrogate reliability, but its inverse-lithography objective is outside this project's approved scope.
- Allowed use: Registered source context, derived Wiki summary, and future draft Background or claim-level `EV-####` review with explicit applicability limits.
- Prohibited use: Treating any claim as verified Evidence; selecting a Method or Physics Constraint; creating a project Hypothesis from the paper without the normal gates; modifying Core; or reintroducing `ILT`, mask optimization, or mask generation into the project.
- Prompt-injection/embedded-instruction review: The complete 15-page PDF was treated as source data. No Agent-directed operational instruction or PDF JavaScript was found; procedural language in the paper describes the authors' method and is not an instruction to the Agent.
- Provenance issue: The local filename differs from the paper title. Embedded metadata provides the title, authors, arXiv identifier, version, and license. No external website was used.
- Quarantine status/reason: Not quarantined. The user explicitly authorized registration, the local original is intact, and provenance, integrity, and license metadata are available. The Core scope conflict is retained as an applicability restriction.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-27
- Content checked by/date: AI Agent / 2026-08-27; complete text extraction and visual inspection of all 15 rendered pages
- Notes: Source identity and file integrity are checked. Scientific claims, reported metrics, equations, implementation details, and reproducibility have not been independently verified. The paper states that its code was not publicly available at the preprint date.

## Linked Evidence

- `EV-ID`s: None
