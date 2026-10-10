---
schema_version: "1.0"
id: ADR-0003
type: architecture-research-decision-record
title: Governance ownership and experiment decision boundary
lifecycle_status: active
authority_class: approved-decision
authority_scope: governance-responsibility-and-strategic-experiment-decision-boundary
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-27
updated_at: 2026-08-27
owner: project-lead
review_status: approved
reviewed_by: user
approved_by: user
approval_ref: "Explicit governance correction request, 2026-08-27"
core_alignment: pass
decision_state: accepted
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
method_ids: []
experiment_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: false
---

# ADR-0003 — Governance ownership and experiment decision boundary

## Status

- Decision state: accepted
- Decision owner: project lead
- Decision date: 2026-08-27
- Explicit approval reference: user governance correction request on 2026-08-27
- Effective date: 2026-08-27

## Decision question

How should duplicated governance rules be assigned canonical ownership, and where is the boundary between strategic ADR decisions and experiment-local choices?

## Context

`AGENTS.md` and `00_Project_Core/Core_Governance.md` repeated the Authority Model, Core Modification Gate, source/context isolation, and AI permissions. The duplication increased context cost and allowed the copies to diverge. Existing wording also implied that an ADR was required before a candidate Method could be implemented and tested, which incorrectly elevated routine experiment-local choices into strategic approvals.

This decision is administrative and persistent. It changes governance responsibility and one Locked Core governance file, but it does not change the research question, scientific hypothesis, scope, input/output boundary, functional requirements, candidate scientific directions, or evaluation requirements.

## Alternatives considered

### Option 1 — Keep duplicated rules

- Rejected because two detailed copies can drift and increase mandatory context overhead.

### Option 2 — Assign one canonical owner per concern and distinguish strategic from experiment-local decisions

- Accepted because it preserves the safety model while removing duplicate procedures.
- `AGENTS.md` owns project-wide Agent behavior, authority, source/context, and ADR scope.
- `Core_Governance.md` owns the detailed Core Modification Gate and Core-specific interpretation.
- `04_Hypotheses/` owns specific falsifiable `HYP-####` records.
- `06_Experiments/EXP-####/Plan.md` owns experiment-local frozen choices.

### Option 3 — Add another registry, approval layer, or governance abstraction

- Rejected as unnecessary and outside the approved correction boundary.

## Decision

1. Keep one detailed project-wide Authority Model in `AGENTS.md`.
2. Keep one detailed Core Modification Gate in `00_Project_Core/Core_Governance.md`.
3. Keep project-wide source/context isolation and AI behavior rules in `AGENTS.md`; Core retains only the rule that unauthorized material cannot be promoted into Locked Core.
4. Keep high-level research questions, strategic research hypotheses, directions, and candidate families in Core; place precise falsifiable `HYP-####` records only in `04_Hypotheses/`.
5. Require ADRs only for strategic, persistent, project-wide, or materially future-affecting decisions.
6. Freeze routine experiment-local choices in the preregistered `EXP-####/Plan.md` without requiring an ADR.
7. Permit a Method to progress experimentally through `concept → candidate → specified → implemented → tested` without an ADR. Only promotion to `selected` as a persistent project Method requires the strategic decision process and explicit user approval.
8. Keep `wiki/` downstream and derived-only, without scientific authority.

## Core-change gate

| Core section | Before | After |
|---|---|---|
| `What Core may contain` | “User-approved research hypotheses or candidate families” without a record-level boundary | High-level strategic hypotheses/directions/families are allowed; precise falsifiable `HYP-####` records with variables, measurable conditions, and Experiment linkage belong in `04_Hypotheses/` |
| `Normative and factual authority` | A second detailed authority table | A concise reference to the single detailed Authority Model in `AGENTS.md`, retaining the normative/factual distinction |
| `Core modification gate` | Nine-step procedure requiring an ADR for every Core change | Seven-step canonical procedure requiring an ADR when the change is strategic, persistent, or materially affects future research; explicit patch, approval, audit log, and consistency validation remain mandatory |
| `Source and context isolation` | Detailed operational source/context rules copied from `AGENTS.md` | “Unreviewed, unregistered, or unauthorized material must not be promoted into Locked Core.” |
| `AI permissions` | Detailed Agent permission list copied from `AGENTS.md` | Removed; Agent behavior remains canonical in `AGENTS.md` |

- User approval obtained: yes, through the explicit governance correction request dated 2026-08-27.
- Planned change record: `CORE-CHG-0004`.

## Consequences

- Mandatory context contains fewer duplicate rules and fewer divergence points.
- Core protection, source provenance, Agent restrictions, and Wiki authority boundaries remain intact.
- Experiment teams can specify, implement, and test candidate Methods under a preregistered Plan without implying project selection.
- Persistent promotion still requires an accepted ADR and explicit user approval.

## Core compatibility

- Core requirements affected: governance interpretation only.
- Locked Core file changed: `00_Project_Core/Core_Governance.md`.
- `Project_Overview.md` changed: no.
- `Research_Requirement.md` changed: no.
- Scientific meaning changed: no.
- Core alignment: pass.

## Rollback

If the ownership split creates a missing safety boundary, restore only the missing boundary in its canonical owner through a new explicitly approved governance correction. Do not restore duplicate detailed procedures by default.
