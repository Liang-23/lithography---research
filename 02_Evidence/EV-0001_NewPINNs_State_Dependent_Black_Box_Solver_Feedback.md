---
schema_version: "1.0"
id: EV-0001
type: evidence-record
title: "State-dependent black-box solver feedback in NewPINNs training"
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
approval_ref: "User Human Audit decision correcting P1 and approving P1-P4, 2026-09-01"
core_alignment: pass
evidence_state: verified
source_ids: [SRC-0003]
data_ids: []
experiment_ids: []
supports_ids: []
contradicts_ids: []
exclude_from_synthesis: false
---

# State-dependent black-box solver feedback in NewPINNs training

## Claim

In the reported NewPINNs training loop, a conventional black-box solver advances the current neural field and its returned state participates in the dynamic solver-consistency loss, but gradients are not backpropagated through the solver mapping itself.

## Relationship

- Supports: Source-relative precedent for training-time black-box physics feedback in which solver output affects the loss but backpropagation does not traverse the external solver.
- Contradicts: None established.
- Does not establish: External post-prediction projection, fixed corrected-output distillation, final physical feasibility, representation-freedom benefit, lithography applicability, or superiority to all PINNs/data-only networks.

## Grounding

- `SRC-ID`: `SRC-0003`
- Exact path: `D:\Litho\2-3nm litho\raw\SRC-0003_NewPINNs.pdf`
- Exact locator: PDF p. 3, Figure 1; pp. 5–8, Eqs. (6)–(22), Algorithms 1–2; pp. 8–9, Section 2.3; PDF p. 22, Section 3.5 exception.
- Evidence form: explicit author statement plus mechanism visible in algorithms/equations.
- Verbatim quote: “The solver is treated as a black-box operator and does not participate in gradient computation.”

## Applicability and limitations

- Conditions: The reported transient and steady NewPINNs procedures using a conventional solver/optimizer response during training.
- Valid scope: Current network field is reinserted into $S$; $S$ returns a state after temporal/iterative advancement; that state participates in $L=\lVert u_{\mathrm{NN}}-u_{\mathrm{solver}}\rVert^2$ and therefore affects optimization through the discrepancy.
- Excluded scope: Deployment behavior, external output correction, fixed teacher labels as the main mechanism, formal feasibility, or lithography validity.
- Assumptions: The authors' black-box/non-differentiable description means that $\partial S/\partial u$ is not evaluated during backpropagation.
- Limitations: Eqs. (10), (15), and (21) and Algorithms 1–2 do not display an explicit detach/stop-gradient operation or a PyTorch `detach()` call.
- Alternative interpretation: Taken without Figure 1 and the non-differentiable-solver prose, the symbolic dependence $S[f_{\mathrm{NN}}(\cdot;\theta)]$ could be read as differentiable; the paper's explicit text rules out that reading for the intended method.
- Exception: The shallow-water experiment uses ten warm-start epochs regressing onto precomputed solver trajectories for $16$ parameter values before dynamic solver-consistency training over $256$ values.

## Conflicting evidence

- Contradicting `EV-ID`s: None.
- Conflict status: No internal contradiction after retaining the shallow-water warm-start exception.

## Verification

- Provenance checked: Yes; admitted arXiv `2601.17207v2`, SHA-256 `5CE2A9CA162CDA72019D2E3FB5021FAD170A18133179F07813F249E523299EDF`.
- Locator checked: Yes; original PDF text and rendered pages visually inspected on 2026-08-31.
- Calculation reproduced: Not applicable.
- Reviewed by/date: Project lead / 2026-09-01, following AI Agent source check on 2026-08-31.
- Approval reference: User Human Audit decision correcting P1 and approving P1-P4, 2026-09-01.
- Evidence state: `verified` within the recorded applicability boundary.
