---
schema_version: "1.0"
id: ADR-0004
type: architecture-research-decision-record
title: "Proposed canonical high-fidelity simulator"
lifecycle_status: draft
authority_class: working
authority_scope: proposed-canonical-simulator-decision-only
created_by: ai
content_origin: mixed
created_at: 2026-08-27
updated_at: 2026-08-27
owner: project-lead
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: unknown
decision_state: proposed
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
method_ids: []
experiment_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: true
---

# ADR-0004 — Proposed canonical high-fidelity simulator

## Status

- Decision state: `proposed`
- Decision owner: project lead
- Decision date: Not decided.
- Explicit approval reference: None. The 2026-08-27 instruction authorized only preparation and evaluation of this proposal; it is not approval.
- Effective date: None.
- Implementation status: Not implemented.

## Decision question

- Exact question: Should the project adopt `pylitho.exact.LithoSim` as the canonical high-fidelity simulator for future governed experiments?
- Why a decision is strategically relevant: A canonical simulator would persist across future experiments and affect data provenance, label generation, simulator contracts, comparability, reproducibility, experiment plans, and claims about fidelity and acceleration. It is therefore project-level rather than experiment-local.
- Why a decision is required now: No operational decision is currently required. This ADR exists solely to place the hypothetical proposal behind the required strategic approval checkpoint.
- Deadline/trigger: Before any project record treats `pylitho.exact.LithoSim` as canonical or relies on that status in a governed Experiment.
- Scope excluded from this decision: Locked Core changes, simulator implementation, installation, execution, dataset creation, `DATA-ID` allocation, Method selection, Experiment creation/execution, metric thresholds, and Evidence verification.

## Proposed decision

Adopt `pylitho.exact.LithoSim` as the canonical high-fidelity simulator for future governed experiments.

This is the proposal under review, not an accepted or selected outcome. It creates no persistent default and grants no execution authority.

## Core relationship

- Core requirements affected: `Research_Requirement.md` Sections 5 (Efficiency Requirement), 6 (Data Constraint Requirement), and 8 (Evaluation Requirement), plus the forward-computational-lithography input/output boundary in `Project_Overview.md`.
- Compatibility result: `unknown`. A canonical high-fidelity simulator is compatible with the Core in principle, but the current records do not establish that this specific implementation satisfies the required domain, fidelity, input/output, process-condition, reproducibility, or availability boundaries.
- Does acceptance require a Core change: No identified Core-text change is required merely to select a canonical simulator.
- Locked Core modification: None proposed or authorized.

## Context and available evidence

- Relevant `EV-ID`s: None exist.
- Relevant `DATA-ID`s or simulator contracts: None exist.
- Relevant `HYP-ID`s: None exist.
- Relevant `METHOD-ID`s: None exist.
- Relevant verified `EXP-ID`s: None exist.
- Available supporting Evidence: None in the current canonical project records.
- Conflicting Evidence: None registered. The absence of conflicting Evidence does not support adoption.
- Evidence limitations: There is no verified record establishing the identity, version, provenance, physical fidelity, numerical behavior, supported inputs/outputs, process-condition coverage, deterministic behavior, computational cost, licensing/availability, maintainability, or reproducibility of `pylitho.exact.LithoSim` for this project.

**Evidence sufficiency result: insufficient to justify acceptance.**

## Alternatives considered

| Alternative | Description | Benefits | Costs/risks | Evidence status | Core compatibility |
|---|---|---|---|---|---|
| A — Adopt `pylitho.exact.LithoSim` | Make the named implementation the persistent canonical high-fidelity simulator. | Could standardize future data generation and experiment comparison. | Premature lock-in, unsupported fidelity assumptions, implementation coupling, and irreproducible future records if the contract is incomplete. | No verified support. | Unknown for this implementation. |
| B — Keep the canonical simulator unresolved | Make no persistent selection until qualification records exist. | Preserves flexibility and avoids granting authority without Evidence. | Future formal Experiments remain blocked where a frozen simulator contract is required. | Consistent with current records. | Pass. |
| C — Define an implementation-neutral simulator contract first | Specify required inputs, outputs, units, versions, configuration, provenance, determinism, fidelity validation, and artifact rules before evaluating implementations. | Separates scientific requirements from a specific software choice and creates auditable selection criteria. | Requires additional specification and review work before selection. | Contract is currently missing. | Pass in principle. |
| D — Qualify multiple candidates before selecting one | Compare candidate simulators under one preregistered validation protocol, then make a later ADR decision. | Allows evidence-based comparison and makes trade-offs visible. | Requires registered candidates, reference data, compute, thresholds, and verified results. | No qualifying Experiment or Evidence exists. | Pass in principle. |

## Decision criteria

No scientific threshold is created by this proposal. Before acceptance, the project would need explicit, reviewable criteria covering:

| Criterion | Required basis before acceptance |
|---|---|
| Physical fidelity | Verified claim-level Evidence against an independent accepted reference or measurement boundary, with exact locators and applicability. |
| Domain and interface coverage | Reviewed simulator contract specifying supported inputs, outputs, units, tensor/coordinate conventions, optical/process conditions, and validity limits. |
| Reproducibility | Frozen version, configuration, dependencies, deterministic controls, provenance, and recomputable validation artifacts. |
| Experiment suitability | Preregistered comparison protocol with exact metrics, aggregations, thresholds, splits/conditions, failure rules, and retained artifacts. |
| Computational suitability | Verified runtime, memory, and resource observations under a defined workload relevant to the Core efficiency requirement. |
| Operational sustainability | Documented availability, licensing constraints, maintenance/version policy, and rollback feasibility. |

## Rationale and uncertainty

- Strategic rationale for considering the proposal: Standardizing the high-fidelity reference could improve consistency across future governed data and Experiments.
- Current recommendation: Do not accept yet. Retain Alternative B while preparing the contract and Evidence required to compare Alternative A responsibly.
- Primary uncertainty: The project has no canonical factual record about `pylitho.exact.LithoSim` beyond the user-supplied hypothetical identifier and proposal.
- Conditions attached to any later acceptance: The missing records and qualification work in the approval checkpoint must exist, be reviewed, and support the decision within an explicit applicability boundary.

## Consequences if later accepted

- Positive consequences: Future governed experiments could reference one canonical simulator identity and contract, improving consistency and traceability.
- Negative consequences: Project-wide coupling to one implementation; migration cost; risk of systematic simulator-specific bias; and possible blockage if the implementation, license, or version becomes unavailable.
- New obligations: Maintain an exact simulator contract and version history; preserve generation configurations and hashes; disclose simulator limitations; define how version changes affect `DATA-ID`s; and qualify replacements through a superseding ADR.
- Follow-on actions: Create and review the simulator contract, register the resulting simulator-backed data boundary through the normal Data workflow, qualify the implementation, and update future Experiment Plans individually. These actions are not authorized by this proposed ADR.
- Monitoring/revisit trigger: Material fidelity failure, unsupported required process conditions, reproducibility failure, unacceptable computational cost, licensing/availability change, or a demonstrably superior qualified alternative.

## Rollback and supersession

- Rollback condition: Any revisit trigger above, or verified Evidence that the simulator is unsuitable within the accepted boundary.
- Rollback procedure: Stop assigning the implementation to new governed Experiments; preserve all historical `DATA-ID`, Experiment, and result provenance; propose a superseding ADR; qualify a replacement; and migrate only future work unless an explicit revalidation plan requires otherwise.
- Supersedes: None.
- Superseded by: None.

## Exact records affected if later accepted

Acceptance would require explicit, separately authorized updates to:

1. `07_Decisions/ADR-0004_Proposed_Canonical_High_Fidelity_Simulator.md` — change decision and approval metadata only after explicit user approval.
2. `07_Decisions/Decision_Log.md` — record the accepted or rejected outcome, approval reference, and effective date.
3. `08_Project_Status/Current_State.md` — report the accepted canonical simulator state and remaining limitations.
4. `02_Evidence/Data_Registry.md` — index a separately reviewed simulator/data contract under the next available `DATA-ID`; no ID is allocated by this proposal.
5. A new detailed record based on `02_Evidence/_templates/Data_Record_Template.md` — define the exact simulator identity, version, configuration, provenance, interface, validity boundary, and reproducibility contract; no record is created by this proposal.
6. Future `06_Experiments/EXP-####/Plan.md` records — reference the accepted simulator contract and frozen version individually. Existing Experiment Plans must not be rewritten automatically.
7. Applicable derived Wiki explanations, only after the decision and contract are canonically recorded and only through `08_Project_Status/Wiki_Workflow.md`.

`Project_Overview.md`, `Research_Requirement.md`, and `Core_Governance.md` are not identified as records requiring modification for this proposal.

## Need-more-evidence path

Before responsible acceptance, obtain all of the following without inventing IDs or outcomes:

1. A reviewed simulator contract defining exact package/component identity, version, provenance, configuration, supported inputs/outputs, units, coordinate/tensor conventions, physical models, process-condition range, deterministic behavior, failure modes, licensing/availability, and reproducibility procedure.
2. Claim-level Evidence with exact locators for simulator fidelity, applicability, and limitations. Evidence must be checked against primary source material and/or independently recomputable validation artifacts.
3. A preregistered simulator-qualification Experiment comparing the candidate against an independent accepted reference or measurement boundary over representative in-domain and required process conditions, with exact metrics, aggregation, thresholds, invalidity rules, compute budget, and retained artifacts defined before execution.
4. A verified Experiment result or independent review demonstrating that the preregistered qualification criteria were met, including disclosed deviations and reproducible hashes.
5. Verified operational Evidence for runtime, memory/resource cost, determinism, version pinning, and continued availability under the intended project workflow.
6. Any conflicting Evidence discovered during qualification, retained with an explicit applicability analysis rather than silently resolved.

## Human approval checkpoint

No acceptance or implementation may occur until the user explicitly selects one of:

- **Accept** — accept the proposed canonical simulator decision, subject to any stated conditions and the required approval recording.
- **Reject** — reject the proposal while preserving `ADR-0004` for history.
- **Revise** — change the proposal, alternatives, criteria, or conditions before deciding.
- **Need more evidence** — keep the ADR proposed and pursue the evidence path above through separately authorized governance work.

## Review checklist

- [x] Alternatives and missing/conflicting Evidence are represented.
- [x] Decision criteria are explicit without inventing thresholds.
- [x] Core compatibility is checked and unresolved implementation suitability is visible.
- [x] Consequences and rollback are recorded.
- [x] Exact records that would be affected by later acceptance are listed.
- [x] `decision_state` remains `proposed`.
- [x] No Core change, simulator selection, implementation, Data record, Evidence, Method, or Experiment was created.
- [ ] Explicit user decision received.

