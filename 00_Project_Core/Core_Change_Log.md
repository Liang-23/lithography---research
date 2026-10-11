---
id: CORE-CHANGE-LOG
type: core-change-log
status: active
authority: audit-record
created_by: ai
creation_authorization: "User request on 2026-08-26"
review_status: pending-user-review
created: 2026-08-26
updated: 2026-08-26
append_only: true
---

# Core Change Log

This file is append-only. It records every creation, modification, rename, move, or deletion affecting Locked Core or its governance.

## Rules

- Never erase or rewrite an existing entry.
- A correction to an entry must be appended as a new correction entry.
- Scientific Core changes require an accepted `ADR-ID` and explicit user approval.
- Administrative initialization may cite the direct user request that authorized it.
- `created_by` records authorship; `approved_by` records approval. Do not conflate them.

## [CORE-CHG-0001] Governance layer initialization

- **Date:** 2026-08-26
- **Status:** applied
- **Change type:** governance initialization
- **Created by:** AI Agent
- **Creation authorization:** User request on 2026-08-26 to establish a project-specific `AGENTS.md`, Core governance, change log, routing, status, and skeleton/templates
- **Content review status:** pending user review
- **ADR:** Not required; no scientific scope or requirement was changed
- **Affected files:**
  - Added `00_Project_Core/Core_Governance.md`
  - Added `00_Project_Core/Core_Change_Log.md`
  - Preserved `00_Project_Core/Project_Overview.md` unchanged
  - Preserved `00_Project_Core/Research_Requirement.md` unchanged
- **Scientific meaning changed:** No
- **Validation:** Locked research files remain present and were not edited

---

## Entry template

```markdown
## [CORE-CHG-####] Short title

- **Date:** YYYY-MM-DD
- **Status:** proposed | approved | applied | rejected | corrected
- **Change type:** scientific | scope | requirement | governance | clerical | rename | move | delete
- **Created by:** human | AI Agent
- **Requested by:**
- **Approved by:**
- **Approval reference:**
- **ADR:** [[ADR-####]]
- **Affected files:**
- **Old wording/state:**
- **New wording/state:**
- **Rationale:**
- **Evidence:**
- **Compatibility checks:**
- **Validation result:**
- **Correction of:**
```

---

## [CORE-CHG-0002] Graph projection governance integration

- **Date:** 2026-08-26
- **Status:** applied
- **Change type:** governance
- **Created by:** AI Agent
- **Creation authorization:** User request on 2026-08-26 to design and implement a canonical-record-driven human Graph View
- **Content review status:** unreviewed
- **ADR:** `ADR-0001` proposed; no scientific Core decision was accepted
- **Affected files:**
  - Updated root `AGENTS.md` with Relationship and Graph projection rules
  - Updated `08_Project_Status/Context_Router.md`, `Current_State.md`, `Next_Action.md`, and `README.md`
  - Added `08_Project_Status/Relationship_Registry.yaml`
  - Added proposed `07_Decisions/ADR-0001_Graph_Relationship_Storage.md`
  - Added the derived `09_Knowledge_Graph/` module, validators, tests, and generated projections
- **Scientific meaning changed:** No
- **Locked research files changed:** No
- **Validation:** Graph acceptance fixture, invalid-edge checks, authority checks, and deterministic rebuild tests passed

---

## [CORE-CHG-0003] Correct Graph architecture to Obsidian-native Wiki synchronization

- **Date:** 2026-08-26
- **Status:** applied
- **Change type:** governance correction
- **Created by:** AI Agent
- **Creation authorization:** Explicit user request on 2026-08-26 correcting the previous custom Knowledge Graph interpretation and requiring Obsidian Native Graph View
- **Content review status:** The Obsidian-native architecture is explicitly approved; the broader governance skeleton remains pending user review
- **ADR:** `ADR-0001` rejected before acceptance; `ADR-0002` accepted by explicit user instruction
- **Correction of:** `CORE-CHG-0002` implementation architecture only; the historical entry remains unchanged
- **Old state:** Active custom relationship registry plus Python-generated JSON/Markdown/Mermaid Graph projection
- **New state:** Governance-controlled canonical research state with downstream derived Wiki synchronization; Markdown `[[wikilinks]]` are visualized directly by Obsidian Native Graph View
- **Affected files and movements:**
  - Updated `AGENTS.md` and root `README.md`
  - Added `08_Project_Status/Wiki_Workflow.md`
  - Updated `08_Project_Status/Context_Router.md`, `Current_State.md`, `Next_Action.md`, and `README.md`
  - Rejected and retained `07_Decisions/ADR-0001_Graph_Relationship_Storage.md`; added accepted `ADR-0002_Obsidian_Native_Wiki_Graph.md`; updated `Decision_Log.md`
  - Archived `09_Knowledge_Graph/` and the empty `08_Project_Status/Relationship_Registry.yaml` under `ARC-0001`
  - Added Markdown-native `tools/health.py`, `tools/lint.py`, their shared validator, and tests
  - Initialized `wiki/overview.md` and seven Core-derived concept notes; updated `wiki/index.md` and append-only `wiki/log.md`
  - Scoped Obsidian's native Graph search to the Wiki while preserving its other settings
- **Scientific meaning changed:** No
- **Locked research files changed:** No
- **Locked-file validation:**
  - `Project_Overview.md` SHA256 `68D06957E6649B7D996319758782D9F6040A34E393F16BAC97FA42D8BB9E78FB`
  - `Research_Requirement.md` SHA256 `24AFCD11360B02A90F3582BD664AC204B7FF725079BB775B261F0F55611D3DBA`
  - `Core_Governance.md` SHA256 `2F8F5B5B872F0141B942ABFDE34689A96E47CBBE69A2D26B1B2E287F454B140D`
- **Wiki validation:** 10 Markdown notes, 44/44 resolvable wikilinks, 0 structural errors, 0 deterministic lint warnings; three validator tests passed
- **End-to-end validation:** Existing Core records trace into the Overview and a six-edge concept chain ending at `Neural Representation Learning`; every target note exists
- **Language preservation:** passed; the English Core material remained English and technical terms, identifiers, filenames, paths, and scope exclusions were preserved

---

## [CORE-CHG-0004] Deduplicate governance ownership and correct the experiment decision boundary

- **Date:** 2026-08-27
- **Status:** applied
- **Change type:** governance correction
- **Created by:** AI Agent
- **Requested by:** User
- **Approved by:** User
- **Approval reference:** Explicit governance correction request on 2026-08-27
- **ADR:** `ADR-0003`
- **Affected files:**
  - Updated `00_Project_Core/Core_Governance.md`
  - Updated root `AGENTS.md`
  - Updated `08_Project_Status/Context_Router.md` and `Current_State.md`
  - Added `07_Decisions/ADR-0003_Governance_Ownership_and_Experiment_Decision_Boundary.md`
  - Updated `07_Decisions/Decision_Log.md`
- **Old wording/state:** Detailed Authority Model, source/context rules, and AI permissions were duplicated in Core; the detailed Core gate was also duplicated in `AGENTS.md`; ADR scope and Method lifecycle wording elevated routine experiment choices into strategic approval.
- **New wording/state:** `AGENTS.md` is the sole detailed owner of project-wide authority, source/context, Agent behavior, and ADR scope; `Core_Governance.md` solely owns the detailed Core gate; specific falsifiable Hypotheses and experiment-local choices remain in their canonical experimental layers; candidate Methods may be implemented and tested without selection.
- **Rationale:** Reduce duplicate governance and mandatory context overhead while preserving the existing safety and authority model.
- **Evidence:** Administrative consistency review only; no scientific claim or external source was used.
- **Compatibility checks:** Research question, scope, input/output boundary, inference requirement, data constraints, candidate scientific directions, and evaluation requirements preserved.
- **Validation result:** Pending post-edit validation.
- **Scientific meaning changed:** No

### Post-edit validation

- **Validation date:** 2026-08-27
- **Result:** Passed
- **Canonical ownership:** One detailed Authority Model in `AGENTS.md`; one detailed Core Modification Gate in `Core_Governance.md`; operational source/context and AI behavior rules remain in `AGENTS.md`.
- **Decision boundary:** ADR wording is limited to strategic/persistent decisions; experiment-local choices and candidate Method/Physics Constraint tests are governed by preregistered `EXP-####/Plan.md` records.
- **Hypothesis boundary:** Core retains strategic high-level framing; specific falsifiable `HYP-####` records are assigned to `04_Hypotheses/`.
- **Locked scientific files:** `Project_Overview.md` SHA256 `68D06957E6649B7D996319758782D9F6040A34E393F16BAC97FA42D8BB9E78FB`; `Research_Requirement.md` SHA256 `24AFCD11360B02A90F3582BD664AC204B7FF725079BB775B261F0F55611D3DBA`; both match their pre-change hashes.
- **Scientific meaning:** Unchanged.
- **Language preservation:** Passed.
- **Remaining contradictions in the six approved areas:** None found in active governance files.

---

## [CORE-CHG-0005] Cloud-First Transition workspace boundary

- **Date:** 2026-10-11
- **Status:** applied
- **Change type:** governance — administrative workspace migration
- **Created by:** AI Agent
- **Requested by:** User
- **Approved by:** User
- **Approval reference:** Explicit approval in this conversation on 2026-10-11
- **ADR:** Not required; no scientific scope, requirement, method, experiment, or persistent research decision changed
- **Affected files:**
  - Updated `AGENTS.md`
  - Updated `08_Project_Status/Context_Router.md`
  - Appended this entry to `00_Project_Core/Core_Change_Log.md`
- **Old wording/state:** The active project boundary was expressed as the Windows path `D:\Litho\2-3nm litho`.
- **New wording/state:** The current Git working-tree root is the location-independent active project boundary, regardless of operating system or absolute filesystem path. `D:\Litho\2-3nm litho` remains a legacy backup and provenance reference only.
- **Rationale:** Support governed Codex Cloud and GitHub operation while preserving historical provenance and the existing authority model.
- **Evidence:** Administrative workspace review only; no scientific claim, external source, or research content was used.
- **Compatibility checks:** Locked Core documents, scientific scope, authority hierarchy, Evidence verification rules, Experiment authorization rules, Core protections, ADR requirements, and historical provenance paths were preserved.
- **Validation result:** `git diff --check` passed; all 7 repository Wiki-integrity unit tests passed; health and lint each reported the pre-existing 28 errors (13 absent `raw/` source files and 15 unresolved `High-dimensional AI Surrogate` Wiki links) with no newly introduced errors.
- **Scientific meaning changed:** No
