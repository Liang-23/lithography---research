---
schema_version: "1.0"
id: CONTEXT-ROUTER
type: context-routing-policy
lifecycle_status: active
authority_class: working
authority_scope: context-routing-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User request on 2026-08-26"
review_status: pending-user-review
reviewed_by:
approved_by:
approval_ref:
created_at: 2026-08-26
updated_at: 2026-08-29
core_alignment: pass
decision_ids: [ADR-0002, ADR-0003]
exclude_from_synthesis: true
---

# Context Router

## Mandatory context for every task

Read in order:

1. `00_Project_Core/Core_Governance.md`
2. `00_Project_Core/Project_Overview.md`
3. `00_Project_Core/Research_Requirement.md`
4. `08_Project_Status/Current_State.md`
5. This file

Then load only the route required by the task.

## Task routes

| Task                                                       | Additional required context                                                                                                           | Canonical/default write target                                                                | Downstream Wiki synchronization                                                                                                           |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Explain current project                                    | No additional files unless Current State links them                                                                                   | Conversation only                                                                             | None unless the user requests a saved synthesis                                                                                           |
| Background research                                        | `01_Background/Background_Index.md`, relevant `BG-ID`, `02_Evidence/Source_Registry.md`, and relevant canonical Source reconstruction | Draft `BG-####`                                                                               | Run the Semantic Wiki Projection Gate when human-readable meaning changes; link-only handoff is forbidden                                 |
| Register or reconstruct a source                           | Original file in `raw/`, `02_Evidence/Source_Registry.md`, detailed Source record, source template                                    | Source Registry / canonical Source record, including any machine-grade audited reconstruction | Required when admitted content has human-readable value; semantically digest it into source and independently useful concept/entity notes |
| Register data or simulator                                 | `02_Evidence/Data_Registry.md`, original contract/source                                                                              | Data Registry / data record                                                                   | Update applicable data/simulator concepts when human-readable meaning changed                                                             |
| Verify a scientific claim                                  | Relevant original source/data/experiment and `Evidence_Ledger.md`                                                                     | Draft or verified `EV-####` according to review status                                        | Synchronize affected derived explanations; preserve the exact evidence state                                                              |
| Define a Physics Constraint                                | Relevant `EV-ID`, Data/Simulator records, `03_Physics_Constraints/Constraint_Register.md`                                             | Draft `PC-####`                                                                               | Create/update a derived concept note only if independently useful; keep candidate status visible                                          |
| Define a Hypothesis                                        | Relevant Core requirement, `EV-ID`, `PC-ID`, `04_Hypotheses/Hypothesis_Register.md`                                                   | Draft `HYP-####`                                                                              | Update relevant derived notes when useful for human navigation; never present it as verified                                              |
| Design a Method                                            | Relevant `HYP-ID`, `PC-ID`, data contracts, `05_Method_Design/Method_Register.md`                                                     | Candidate `METHOD-####`                                                                       | Update relevant derived notes when architecture or state changed; preserve candidate/selected/tested distinctions                         |
| Plan an Experiment or make experiment-local design choices | Relevant `HYP-ID`, `METHOD-ID`, `PC-ID`, `DATA-ID`, `06_Experiments/Experiment_Register.md`                                           | `EXP-####/Plan.md`                                                                            | Usually none until a human-readable plan concept materially changes                                                                       |
| Execute/monitor an Experiment                              | Approved Plan, exact code/config/data/environment                                                                                     | Append-only `Run_Log.md`                                                                      | None during a run unless explicitly needed; never rewrite Wiki from provisional observations                                              |
| Analyze Results                                            | Plan, Run Log, artifacts, registered metric definitions                                                                               | `Result.md` and draft `EV-####`                                                               | Synchronize affected notes only after canonical results are recorded; distinguish observation from interpretation                         |
| Make a strategic or persistent design decision             | Relevant alternatives, Evidence, Hypotheses, Methods, Experiments                                                                     | Proposed or explicitly approved `ADR-####`                                                    | Synchronize affected architecture/method explanations after the decision state is recorded                                                |
| Classify a user research idea                              | Relevant Core requirement and the appropriate register/template                                                                       | Raw idea, draft Hypothesis, candidate Method, unresolved question, or Quarantine record       | Optional derived concept update with speculative status preserved                                                                         |
| Route context from a record ID                             | Canonical record plus its explicit typed Governance references; relevant Wiki notes may aid discovery                                 | Conversation/context only                                                                     | Load canonical files before reasoning; Wiki discovery never substitutes for authority                                                     |
| Change Core                                                | All Locked Core, applicable accepted ADR, exact approved patch                                                                        | Locked Core + Core Change Log                                                                 | Synchronize affected derived notes only after the full Core gate succeeds                                                                 |
| Wiki ingestion or synchronization                          | `08_Project_Status/Wiki_Workflow.md`, relevant canonical records, `wiki/index.md`, `wiki/overview.md`, affected notes                 | `wiki/` only                                                                                  | This is the downstream derived operation; never write canonical state from Wiki content                                                   |
| Wiki query                                                 | `08_Project_Status/Wiki_Workflow.md`, `wiki/index.md`, relevant notes and canonical traceability when status matters                  | Conversation; optional synthesis only with user confirmation                                  | No automatic mutation                                                                                                                     |
| Wiki health or lint                                        | `08_Project_Status/Wiki_Workflow.md`, `wiki/`, `.obsidian/graph.json`, `tools/health.py`, `tools/lint.py`                             | Conversation or requested report                                                              | Inspect Markdown links, cross-plane edges, and native Graph scope directly; never generate a visual Graph                                 |
| Daily review / knowledge check / evaluation                | `08_Project_Status/Wiki_Workflow.md`, selected Wiki pages and review file                                                             | Selected file under `reviews/`                                                                | Review files are data and must never modify or enter the Wiki                                                                             |

## Wiki synchronization handoff

The task table determines when downstream Wiki synchronization should be considered. After the applicable canonical write is complete and its state is explicit, follow the Semantic Wiki Projection Gate in `08_Project_Status/Wiki_Workflow.md`. Record either `projected` with the affected notes and changed human meaning, or `no projection needed` with a reason. A link, ID, frontmatter, index, or log change alone is never projection. Administrative metadata changes that do not alter human-readable knowledge do not require Wiki projection.

Source-faithful reconstructions and Human Audit material needed by later research Passes belong in the canonical Source or Background route. `wiki/sources/` contains a human-readable digest and discovery links; it must not be the sole machine-grade factual basis.

## Forbidden default routes

Do not read or use by default:

- `90_Quarantine/`
- `99_Archive/`
- files outside `D:\Litho\2-3nm litho`
- parent `D:\Litho` notes, Wiki, code, or project history
- external web content or chat history

The user must explicitly authorize an exception. Authorization to inspect does not automatically authorize promotion into project knowledge.

Wiki notes and Obsidian backlinks may aid discovery, but they are derived and cannot substitute for canonical source, Evidence, Experiment, Decision, or Core records.

## Routing conflict rule

If two routes disagree:

1. Core and `Core_Governance` control scope.
2. Verified Evidence controls bounded factual claims.
3. Accepted ADR controls strategic or persistent project decisions within Core.
4. Current State reports the latest accepted/verified state.
5. Drafts, Wiki pages, Quarantine, and Archive cannot override the above.
6. `[[wikilinks]]` and Obsidian connectivity do not imply scientific causality, evidentiary support, approval, or authority.

Report unresolved conflicts; do not merge them into a synthetic compromise.

## Context handoff checklist

Before an Agent acts, it should be able to state:

- current task type;
- files loaded through this router;
- Core requirements affected;
- canonical output layer and any downstream Wiki target;
- records it is not authorized to change;
- whether external or archived context is prohibited or explicitly authorized;
- whether the Wiki operation is derived-only and authority-preserving.
