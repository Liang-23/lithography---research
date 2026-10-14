---
schema_version: "1.0"
id: NEXT-ACTION
type: action-register
lifecycle_status: active
authority_class: working
authority_scope: planning-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User request on 2026-08-26"
review_status: pending-user-review
reviewed_by:
approved_by:
approval_ref:
created_at: 2026-08-26
updated_at: 2026-10-14
core_alignment: pass
exclude_from_synthesis: true
---

# Next Action

This file contains bounded actions, not an open-ended idea list. An action may be `proposed`, `approved`, `in-progress`, `completed`, `blocked`, or `cancelled`.

## Current next step

NA-0011 is the proposed next design-review action for the FD-GNN Effective Mode Generator. NA-0010 remains blocked for the separate Architecture 3 candidate; existing actions retain their own statuses. No Method is selected, data frozen, or experiment authorized.

## NA-0001 — Review governance skeleton

- **Status:** cancelled
- **Owner:** project lead
- **Purpose:** Review the new `AGENTS.md`, `Core_Governance.md`, routing, status, registers, templates, Relationship Schema, and proposed `ADR-0001`.
- **Cancellation reason:** The user explicitly rejected the custom Relationship Schema/Graph architecture on 2026-08-26. `ADR-0001` was rejected before acceptance, so this mixed review action is no longer valid.
- **Replacement:** `NA-0005` covers review of the remaining governance and corrected Wiki synchronization system.
- **Core impact:** None unless the user requests a Core governance revision.

## NA-0002 — Admit the first Background sources

- **Status:** completed
- **Owner:** project lead and AI Agent under explicit paper-level approval
- **Purpose:** Select only project-relevant original sources, place them in `raw/` or explicitly register them, and assign `SRC-ID`s.
- **Completion condition:** Source provenance, version, path, hash, allowed use, and review status are recorded.
- **Completion confirmation:** The project lead approved eleven exact artifacts; lawful acquisition, integrity/version verification, and formal admission were completed as `SRC-0003` through `SRC-0013` by 2026-08-30. All eleven subsequently reached `tier2_review_status: agent-complete`; this does not constitute Human Audit or claim-level Evidence verification.
- **Core impact:** None. Source admission and Tier 2 ingestion do not select a Physics Constraint, Hypothesis, Method, Experiment, simulator, dataset, or scientific default.

## NA-0003 — Establish the first Physics Constraint candidate

- **Status:** blocked
- **Blocked by:** relevant verified Evidence and Data/Simulator definitions
- **Purpose:** Create one complete `PC-####` record for a computable terminal-output physical constraint.
- **Completion condition:** Equation/operator, variables, units, validity regime, projection definition, inference compatibility, failure modes, evidence, and rejection experiment are specified.

## NA-0004 — Preregister the first decisive experiment

- **Status:** blocked
- **Blocked by:** accepted Data/Simulator contract, ready-to-test Physics Constraint, Hypothesis, and Method Design
- **Purpose:** Compare a controlled data-only baseline with the selected physical-integration mechanism under frozen data, backbone, compute, metrics, and thresholds.
- **Completion condition:** `EXP-####/Plan.md` is complete and approved before any formal run.

## NA-0005 — Review corrected governance and Wiki synchronization

- **Status:** completed
- **Owner:** project lead
- **Purpose:** Review the governance skeleton that remains pending and the active Governance-to-Wiki synchronization rules. The Obsidian-native architecture itself was explicitly accepted in `ADR-0002`.
- **Completion condition:** User confirms the remaining governance text or requests bounded revisions.
- **Completion confirmation:** The user confirmed completion and accepted the current governance structure on 2026-08-27.
- **Outcome:** Governance ownership, task-specific routing, detailed Wiki workflow ownership, derived-only Wiki authority, the strategic-versus-experiment-local decision boundary, and candidate-Method experimental progression were reviewed and accepted. The source-admission, experiment-local planning, and strategic ADR approval-checkpoint simulations passed their governance boundaries.
- **Core impact:** None. This completion is administrative and does not change the research direction, scientific content, project Method, simulator, dataset, Experiment, Evidence, or persistent scientific default.

## NA-0006 — Retire the custom Graph projection

- **Status:** completed
- **Owner:** AI Agent under explicit user instruction
- **Purpose:** Reject `ADR-0001`, archive the empty relationship registry and standalone Graph module, activate Markdown Wiki synchronization, and validate an Obsidian-resolvable link path.
- **Completion condition:** Obsolete active paths are absent, archive history is recorded, health/lint read Markdown directly, all test links resolve, and no visual graph generation step remains.
- **Core impact:** None. Locked research files and scientific meaning remain unchanged.

## NA-0007 — Select pivotal Sources and prepare Human Audit

- **Status:** in-progress
- **Owner:** project lead / Human reviewer, with Agent preparation limited to the canonical Human Audit procedure
- **Approval reference:** User-directed Project Status reconciliation on 2026-08-31.
- **Purpose:** Select the pivotal subset from `SRC-0003` through `SRC-0013`, record the selection and audit order, and prepare the canonical Human Audit inputs without promoting Tier 2 content into verified Evidence.
- **Why this precedes Human Audit:** `Q-0001` records pivotal-paper selection as not started and defines it as the step immediately preceding the required Human Audit. Human Audit execution therefore remains gated until this selection is recorded.
- **Completion condition:** The pivotal Source set and audit order are recorded through the canonical campaign/Source route, after which Human Audit may begin under its required procedure.
- **Progress:** The project lead selected `SRC-0003`; targeted P1-P4 Human Audit completed on 2026-09-01, with corrected P1 wording and verified `EV-0001` through `EV-0003`. The project lead subsequently selected `SRC-0004`, completed its targeted P1-P4 Human Audit, and explicitly approved `EV-0004` through `EV-0006`; all three are verified and semantically projected into the existing PADM Wiki representation. The remaining pivotal subset and audit order are not yet fully recorded.
- **Excluded parallel work:** No claim-level Evidence creation, citation snowballing, new literature discovery, Physics Constraint selection, Hypothesis creation, Method selection, Experiment design, field-wide novelty assessment, or Core modification.
- **Core impact:** None. `SRC-0003` and `SRC-0004` targeted P1-P4 Human Audits and `EV-0001` through `EV-0006` verification are complete; Human Audit for the remaining Sources remains `not-started`. This action does not modify Core.

## NA-0008 — PADM-focused literature synthesis and three draft hypotheses

- **Status:** completed
- **Owner:** AI Agent under project-lead instruction
- **Authorization:** Explicit request to implement the PADM-focused plan, 2026-09-13.
- **Delivered:** BG-0002; HYP-0001 (conditional diffusion), HYP-0002 (correction knowledge transfer), HYP-0003 (label efficiency); Chinese semantic Wiki synthesis; PADM preference and ΠNet reading records; updated registers and navigation.
- **Comparison boundary:** Conditional diffusion with U-Net is the preferred investigation candidate; correction-to-learning remains the physics thread; high-fidelity label reduction is the data goal. Representation freedom remains to be tested. No architecture or physical formula was selected.
- **Completion condition:** Sources, transfer assumptions, variables, comparisons, rejection/inconclusive conditions, missing inputs, and separate training/inference costs are recorded; the Wiki carries meaningful explanations with draft status.
- **Unresolved:** No first output stage, DATA/PC contract, executable Method, metric thresholds, or new Experiment. Corpus count is 13 registered Sources; the fourteenth is unconfirmed. The 15 pre-existing broken links remain reported separately.

## NA-0009 — Discuss the minimum definitions for the draft comparisons

- **Status:** proposed
- **Owner:** project lead with Agent assistance
- **Purpose:** Use BG-0002 and HYP-0001–HYP-0003 to narrow the next information request, before choosing a final architecture or running an experiment.
- **Discussion order:** First clarify the role of the user's proposed few physical parameters: whether they determine the entire image or guide correction of a full neural image, and whether the image-generation module also reads the original mask/conditions. Explain correction of complete output versus a physically defined per-step clean estimate without selecting either interface. Then identify the target physical output/reference, candidate relations and inputs, available high-fidelity/approximate resources, and quality/label-budget/deployment-cost criteria. Missing formulas do not block the conceptual discussion; they do block claiming a specified or executable Method.
- **HYP-specific outputs:** HYP-0001 needs task/conditioning/sampling-cost definitions; HYP-0002 needs a valid correction and its derivative/target boundary, with privileged information only if available; HYP-0003 needs target provenance, independent-label accounting, and sufficient physics signals.
- **Completion condition:** A bounded definition-gap list with concrete source/data requirements is reviewed; absent information is not filled with assumptions disguised as facts.
- **Limits:** No external acquisition, simulator adoption, DATA/PC promotion, model training, or experiment execution is initiated under this proposed action. Formal records and approvals follow their normal routes once concrete definitions are available.

## NA-0010 — Prepare the Architecture 3 kernel-prediction feasibility prototype

- **Status:** blocked
- **Owner:** project lead with Agent assistance
- **Date:** 2026-09-21
- **Trigger:** The user supplied a revised architecture and explicitly authorized a read-only audit of `D:\project\lithobench-main`.
- **Purpose:** Prepare the candidate method, data record, and experiment plan for a U-Net that predicts a kernel tensor `B` and an explicit differentiable FFT renderer.
- **Required order:** Freeze the matched-data contract and manifests; implement and gradient-test the FFT renderer; build a new conditioned U-Net with a one-kernel complex output head; overfit one sample and a tiny subset; compare with the direct-image baseline; only then consider multiple kernels, diffusion sampling, and the correction branch.
- **Blockers:** DATA-0001 is unfrozen; `alpha` is absent from the data; the exact `B` and multi-kernel combination contracts are open; external kernel assets are undecoded; no physical-constraint record exists for Stage 2; and no implementation is present in the current project.
- **Completion condition:** EXP-0002 is fully specified and approved, with data/tensor/simulator contracts and implementation artifacts ready before any run.
- **Evidence/report:** `08_Project_Status/Experiment_Preparation_Report_2026-09-21.md`.


## NA-0011 — Design and compare FD-GNN internal aggregation

- **Status:** proposed; user approved recording research progress and Candidate A for validation, not any formal test execution.
- **Owner:** project lead with AI assistance.
- **Date:** 2026-10-14.
- **Purpose:** Specify $w_\theta(q)$, hidden update $U_\theta$, effective-mode readout, FFT/complex contracts, and a fair comparison of aggregation variants for the independent `METHOD-0003` concept.
- **Research framing:** $p_{k,l}=A(k)A^*(l)$ is known; final pair contribution routes only to $q=k-l$. Internal incident Pair-to-Frequency-Node hidden message passing is separate from that physical output route.
- **First candidate:** $s_k=\sum_{l\in\mathcal N(k)} w_\theta(k-l) A(k)A^*(l)$, untested and not selected.
- **Blockers to experiment:** data/output contract, indexing and sparse edge policy, numerical/Hermitian/nonnegative constraints, competing aggregators, compute budget and preregistered acceptance criteria.
- **Completion condition:** project lead reviews a precise, implementable architecture and any formal experiment must subsequently receive separate approval.
- **Scope:** no code execution, data freeze, Core edit, Method selection, ADR acceptance or verified Evidence promotion.
