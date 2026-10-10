---
schema_version: "1.0"
id: EV-0003
type: evidence-record
title: "Solver-inherited limitations and stabilization in NewPINNs"
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
approval_ref: "User Human Audit decision approving P4 with feasibility/safety boundaries, 2026-09-01"
core_alignment: pass
evidence_state: verified
source_ids: [SRC-0003]
data_ids: []
experiment_ids: []
supports_ids: []
contradicts_ids: []
exclude_from_synthesis: false
---

# Solver-inherited limitations and stabilization in NewPINNs

## Claim

The paper explicitly states that NewPINNs inherits the numerical solver's accuracy, stability requirements, invariant structure, and computational cost, and it reports solver-compatible initialization, normalization, clipping, depth flooring, or warm start for difficult systems.

## Relationship

- Supports: Bounded Evidence that black-box solver feedback is not cost-free or universally stable during training.
- Contradicts: Any unqualified interpretation that a solver-coupled consistency target automatically supplies safe or exact correction.
- Does not establish: A deployment-time safety gate, fallback solver, trust region, accept/reject mechanism, or exact converged feasibility of the final neural output.

## Grounding

- `SRC-ID`: `SRC-0003`
- Exact path: `D:\Litho\2-3nm litho\raw\SRC-0003_NewPINNs.pdf`
- Exact locator: PDF p. 8, Eqs. (21)–(22) and stability/scaling discussion; p. 10, Section 3.1; p. 15, Section 3.3; p. 22, Section 3.5; p. 23, Section 3.6; pp. 24–25, Conclusion.
- Evidence form: explicit author statement plus reported experimental procedures.
- Verbatim quote: None required.

## Applicability and limitations

- Conditions: The reported PDE solver-coupled training settings and their selected numerical solvers/optimizers.
- Valid scope: Training inherits solver/optimizer properties and can require problem-specific stabilization.
- Excluded scope: Universal behavior across solvers, deployment safety, exact PDE feasibility, or lithography validity.
- Assumptions: Reported stabilization steps are materially related to maintaining admissible solver calls or stable optimization as described by the authors.
- Limitations: The paper does not isolate each stabilization component in controlled ablations.
- Alternative interpretation: Boundary conditions or positivity may be enforced within an individual solver call, but this is narrower than proving that the network output is an exact converged solution.

## Conflicting evidence

- Contradicting `EV-ID`s: None.
- Conflict status: No direct conflict; author rhetoric about “physically admissible” outputs is bounded by the partial-step formulation and absence of a final-feasibility theorem.

## Verification

- Provenance checked: Yes; admitted arXiv `2601.17207v2`, SHA-256 `5CE2A9CA162CDA72019D2E3FB5021FAD170A18133179F07813F249E523299EDF`.
- Locator checked: Yes; original PDF text and relevant rendered pages visually inspected on 2026-08-31.
- Calculation reproduced: Not applicable.
- Reviewed by/date: Project lead / 2026-09-01, following AI Agent source check on 2026-08-31.
- Approval reference: User Human Audit decision approving P4 with feasibility/safety boundaries, 2026-09-01.
- Evidence state: `verified` within the recorded applicability boundary.
