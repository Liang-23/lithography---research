---
schema_version: "1.0"
id: EV-0002
type: evidence-record
title: "Direct neural field prediction in the reported NewPINNs evaluation path"
lifecycle_status: active
authority_class: verified-record
authority_scope: atomic-claim-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-31
updated_at: 2026-09-01
owner: project-lead
review_status: approved
reviewed_by: project-lead
approved_by: project-lead
approval_ref: "User Human Audit decision approving P3 with its inference/runtime boundary, 2026-09-01"
core_alignment: pass
evidence_state: verified
source_ids: [SRC-0003]
data_ids: []
experiment_ids: []
supports_ids: []
contradicts_ids: []
exclude_from_synthesis: false
---

# Direct neural field prediction in the reported NewPINNs evaluation path

## Claim

In the reported NewPINNs forward evaluations, trained neural networks directly map physical parameters and, where applicable, time and geometry inputs to spatial solution fields; the conventional solver is not shown as part of that forward prediction path.

## Relationship

- Supports: Source-relative structural precedent for training-time solver coupling followed by direct neural field prediction.
- Contradicts: None established.
- Does not establish: Deployment acceleration, runtime speedup, production cost, inference-time safety, exact feasibility, or lithography applicability.

## Grounding

- `SRC-ID`: `SRC-0003`
- Exact path: `D:\Litho\2-3nm litho\raw\SRC-0003_NewPINNs.pdf`
- Exact locator: PDF p. 6, Eqs. (8)–(12) and text preceding Algorithm 1; p. 12, Section 3.2; pp. 17–18, Section 3.4; pp. 21–22, Section 3.5; pp. 23–24, Section 3.6 and Conclusion.
- Evidence form: method definition plus reasonable inference from the reported experimental evaluation path.
- Verbatim quote: None required.

## Applicability and limitations

- Conditions: Forward evaluation of trained NewPINNs models in the experiments reported in the admitted PDF.
- Valid scope: The network supplies predicted spatial fields; independently generated solver solutions are used as evaluation references.
- Excluded scope: An explicit deployment procedure, solver-removal experiment, latency comparison, or inference-safety guarantee.
- Assumptions: The described evaluation calculations use the stated direct network mappings without an unreported solver post-processing step.
- Limitations: The paper does not provide a dedicated inference algorithm that explicitly marks the solver as disabled.
- Alternative interpretation: The solver remains necessary for generating the reported reference solutions, but that evaluation role is separate from the network's forward prediction path.

## Conflicting evidence

- Contradicting `EV-ID`s: None.
- Conflict status: None identified in the admitted PDF.

## Verification

- Provenance checked: Yes; admitted arXiv `2601.17207v2`, SHA-256 `5CE2A9CA162CDA72019D2E3FB5021FAD170A18133179F07813F249E523299EDF`.
- Locator checked: Yes; original PDF text and relevant rendered pages visually inspected on 2026-08-31.
- Calculation reproduced: Not applicable.
- Reviewed by/date: Project lead / 2026-09-01, following AI Agent source check on 2026-08-31.
- Approval reference: User Human Audit decision approving P3 with its inference/runtime boundary, 2026-09-01.
- Evidence state: `verified` within the recorded applicability boundary.
