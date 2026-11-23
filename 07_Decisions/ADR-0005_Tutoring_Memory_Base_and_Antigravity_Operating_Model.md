---
schema_version: "1.0"
id: ADR-0005
type: architecture-research-decision-record
title: "Pure Google Drive daily study log and event-driven Antigravity operating model"
lifecycle_status: draft
authority_class: working
authority_scope: proposed-decision-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-11-23
updated_at: 2026-11-23
owner: project-lead
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
decision_state: proposed
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
method_ids: [METHOD-0003]
experiment_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: true
---

# ADR-0005 — Pure Google Drive daily study log and event-driven Antigravity operating model

## Status

- Decision state: `proposed`
- Decision owner: project lead
- Decision date: Not decided.
- Explicit approval reference: None — revised to Option 2 (Pure Drive daily study log) per user preference on 2026-11-23; awaiting explicit approval to mark `accepted` per `AGENTS.md` §12.
- Effective date: None.

## Decision question

- Exact question: Should personal FD-GNN tutoring and daily learning logs live purely in **Google Drive** (consumed directly by Gemini / NotebookLM with end-of-day updates), while **GitHub `main`** remains the sole canonical store for governed research records and code, and **Antigravity** acts on-demand (refreshing the read-only Drive research snapshot when repo docs change and handling repo code/governance updates when study insights mature)?
- Why a decision is required now:
  1. During the Phase 2 mini-trial (`2026-11-23`), Gemini's direct private GitHub Import failed (`Something went wrong (13)`), whereas `@gdrive` staging (`FD-GNN-Tutor-Staging-RO`) passed $5/5$ `WORKFLOW.md` Fresh-chat acceptance checks ($60\,\mathrm{s}$, $2$ clicks, $0$ errors).
  2. Syncing tutoring checkpoints back to GitHub after every micro-step or every day creates unnecessary learning friction. Separating **non-canonical personal study in Google Drive** from **canonical research/code on GitHub** removes daily sync overhead while preserving full governance integrity.
- Deadline/trigger: Before standardizing the daily Gemini / NotebookLM study workflow and retiring `codex memory 11-22-2026/` as an active per-step sync target.
- Scope excluded from this decision: Locked Core (`00_Project_Core/`), canonical governance (`01_Background/`–`08_Project_Status/`), derived `wiki/`, `METHOD-0003` selection or design-choice freezing, `EV-####` scientific evidence promotion, `raw/` PDFs or large binary/dataset storage (`6B`), and formal `EXP-####` execution.

## Core relationship

- Core requirements affected: None of the scientific requirements in `00_Project_Core/Project_Overview.md` or `00_Project_Core/Research_Requirement.md` are altered. Because personal study notes in Google Drive are explicitly **non-canonical** and cannot modify Locked Core, `METHOD-0003`, or `EV-####` without going through Antigravity and the GitHub governance gates, `AGENTS.md` §3, §4, §12, §15, and §16 remain fully satisfied.
- Compatibility result: `pass`
- Does acceptance require a Core change: No.
- If yes, exact Locked Core file/statement: Not applicable.

## Context and evidence

- Relevant `EV-ID`s: None (workflow infrastructure decision; personal study notes are never promoted to scientific `EV-####`).
- Relevant `PC-ID`s: None.
- Relevant `HYP-ID`s: None.
- Relevant `METHOD-ID`s: `METHOD-0003` (remains `draft` / `concept` candidate; staged read-only to Drive for study reference only).
- Relevant `EXP-ID`s: None.
- Observed empirical workflow measurements (`2026-11-23` Phase 2 mini-trial, separated from interpretation):
  - **GitHub Import (Arm A):** Gemini's Import code dialog parsed `liang-23/lithography---research` (`main`, `a0e2987`) and failed with `Something went wrong (13)` ($166$ tracked files, $6.7\,\mathrm{MB}$).
  - **Google Drive Read-Only Staging (Arm C):** Initial $6$-file plain-Markdown (`text/markdown`) export to `FD-GNN-Tutor-Staging-RO` took $9.77\,\mathrm{s}$; incremental $3$-file in-place update (`e46434e`) took $4.90\,\mathrm{s}$ (both $\le 15\,\mathrm{s}$). Fresh Gemini chat via `@gdrive` took $60\,\mathrm{s}$ / $2$ clicks / $0$ errors and passed $5/5$ `WORKFLOW.md` Fresh-chat checks (`Continuity`, `Teaching style`, `Correct grouping`, `Research fidelity`, `Repeatability`).
  - **User Ergonomics Feedback (`2026-11-23`):** Per-step GitHub checkpoint round-trips interrupt learning flow; the project lead prefers studying continuously in Gemini / NotebookLM and saving daily progress directly in Google Drive, invoking Antigravity only when updating canonical repo files or refreshing the Drive research snapshot.
- Conflicting evidence / trade-offs: Keeping daily study logs exclusively in Google Drive means Antigravity and GitHub do not automatically see day-to-day tutoring progress unless the user explicitly shares a Drive note or requests a repo update.
- Evidence limitations: Workflow usability is specific to the current Gemini / NotebookLM and Google Drive tooling behavior as of `2026-11-23`.

## Alternatives

| Alternative | Description | Benefits | Costs/risks | Evidence | Core compatibility |
|---|---|---|---|---|---|
| **Option A — GitHub-Primary per-step/daily sync** | Tutoring checkpoints stay on GitHub `main`; Gemini reads via GitHub connector or paste | Single store; full Git history for study notes | Gemini private GitHub Import failed (`Something went wrong (13)`); high per-step copy-paste friction | Phase 2 Arm A observation (`a0e2987`) | `pass` |
| **Option C1 — Hybrid Daily Batch Sync (Drive $\leftrightarrow$ GitHub daily)** | Study in Drive/Gemini; Antigravity syncs daily Drive note back to GitHub `LESSONS.md` and refreshes Drive | GitHub tracks daily learning history; $5/5$ `WORKFLOW.md` verified | Still requires daily Antigravity sync round-trip even when no repo code/design changed | Phase 2 Arm C observations (`a0e2987` $\to$ `e46434e`) | `pass` |
| **Option C2 / Pure Drive Study Log *(Proposed)*** | Personal daily learning & progress live purely in **Google Drive** (Gemini / NotebookLM); **GitHub `main`** holds canonical research & code only; **Antigravity** runs on-demand to refresh read-only Drive research context (`FD-GNN-Tutor-Staging-RO`) or promote mature insights into governed repo code/docs | Zero per-step or daily GitHub sync friction; native Gemini/NotebookLM flow; $100\%$ GitHub governance integrity for actual research & code | Study progress is not versioned in Git; Drive read-only research snapshot refreshes only when requested | Phase 2 Arm C observations + user workflow selection (`2026-11-23`) | `pass` |

## Decision criteria

| Criterion | Priority | Measurement | Required threshold |
|---|---|---|---|
| Learning Flow & Ergonomics | Primary | Continuous Gemini / NotebookLM study without per-step GitHub round-trips | End-of-day Drive save only; $0$ mid-session sync steps |
| Governance & Core Protection | Mandatory | Separation between non-canonical Drive study notes and canonical GitHub records (`AGENTS.md` §4) | $0$ unreviewed Drive edits entering GitHub Core/Evidence/Method records |
| On-Demand Research Freshness | High | Antigravity one-way SHA-stamped export to `FD-GNN-Tutor-Staging-RO` | $\le 15\,\mathrm{s}$ export time, plain `text/markdown`, $0$ `health.py` error delta |

## Proposed decision

- Selected alternative: **Pure Google Drive Daily Study Log + Event-Driven Antigravity Operating Model**:
  1. **Personal Learning Memory (Google Drive — Non-Canonical):** You study continuously in Gemini / NotebookLM and save your daily progress directly in Google Drive at the end of each session. No per-step or daily GitHub write-back is required.
  2. **Canonical Research & Code (GitHub `main`):** `00_Project_Core/`–`08_Project_Status/`, `wiki/`, `tools/`, and `06_Experiments/` remain strictly on GitHub under `AGENTS.md` governance.
  3. **Read-Only Research Snapshot (`FD-GNN-Tutor-Staging-RO` in Drive):** Holds SHA-stamped plain-Markdown (`text/markdown`) copies of live canonical context (such as `METHOD-0003` and `FD_GNN_Global_Context_Candidates_2026-10-14.md`) so Gemini / NotebookLM stay grounded in accurate project boundaries.
  4. **Antigravity's Role (Event-Driven):**
     - **On-Demand Context Refresher:** Re-exports `FD-GNN-Tutor-Staging-RO` whenever canonical GitHub records (e.g., `METHOD-0003`, `Current_State.md`) change.
     - **Repo Builder & Governance Gatekeeper:** When you decide to turn a learning takeaway into prototype code, a `METHOD-0003` revision, an `EXP-####/Plan.md`, or a `proposed` ADR, Antigravity implements, audits Core/MathJax/`tools/health.py` delta $= 0$, and commits to GitHub.
  5. **Codex:** Retired from tutoring orchestration (`7(i)`).
- Rationale: Eliminates per-step and daily sync friction while keeping `AGENTS.md` governance $100\%$ intact and leveraging the empirically verified $~5\,\mathrm{s}$ one-way `gdrive` export when canonical research docs update.
- Uncertainty: If personal Drive study notes grow large over months, periodic manual cleanup or an occasional Antigravity review may still be helpful to harvest concrete `METHOD-0003` questions.
- Conditions attached to acceptance:
  1. Personal Drive study notes remain strictly non-canonical; any change to `METHOD-0003`, code, or experiments enters GitHub through Antigravity's normal governance route.
  2. `FD-GNN-Tutor-Staging-RO` stays read-only (overwritten only by Antigravity from GitHub `main` with a commit SHA manifest); personal daily progress notes go in a separate Drive document/folder so Antigravity refreshes never overwrite your notes.

## Consequences

- Positive consequences: Frictionless daily learning in Gemini / NotebookLM; zero Git noise from routine tutoring Q&A; clean separation between personal learning and governed research records.
- Negative consequences: Daily study history is not stored in Git; `codex memory 11-22-2026/` becomes a historical snapshot (`e46434e`) rather than an actively synced log.
- New obligations: Keep your personal daily progress notes outside `FD-GNN-Tutor-Staging-RO` (e.g., in your own Drive study folder or NotebookLM notebook) so on-demand Antigravity refreshes of `FD-GNN-Tutor-Staging-RO` never touch your notes.
- Follow-on actions (post-approval only): Mark `ADR-0005` `accepted`, record bounded administrative completion in `08_Project_Status/Current_State.md`, optionally mark `codex memory 11-22-2026/` as superseded/archived or leave as historical reference, and record `no projection needed` at the Semantic Wiki Projection Gate.
- Monitoring/revisit trigger: Revisit if you later want automated daily GitHub checkpoint archival or if Gemini's private GitHub Import is fixed by Google.

## Rollback and supersession

- Rollback condition: Desire to track daily tutoring checkpoints in GitHub again or move away from Google Drive.
- Rollback procedure: Export personal Drive study notes to plain Markdown, audit against `METHOD-0003` boundaries and `tools/health.py`, commit to a chosen GitHub folder, and supersede `ADR-0005` via a follow-up ADR (`AGENTS.md` §12).
- Supersedes: None.
- Superseded by: None.

## Core-change gate, if applicable

Not applicable — no Locked Core file is modified.

## Review checklist

- [x] Alternatives and conflicting evidence are represented fairly.
- [x] The decision criteria are explicit.
- [x] Core compatibility is checked.
- [x] Consequences and rollback are recorded.
- [x] `decision_state: accepted` is never set by AI without explicit approval.
- [x] A Core change uses the separate Core modification gate.
- [x] Template metadata is replaced only when creating a real `ADR-ID` record.
