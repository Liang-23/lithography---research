---
id: CORE-GOVERNANCE
type: core-governance
status: active
authority: normative
created_by: ai
creation_authorization: "User request on 2026-08-26"
review_status: pending-user-review
approved_by:
approval_ref:
created: 2026-08-26
updated: 2026-08-27
---

# Core Governance

## Purpose

`00_Project_Core` 是本项目的 research constitution。它用于锁定项目身份、研究问题、scope、functional requirements、scientific contribution requirements 和 evaluation boundary，防止 AI suggestion、单篇 paper、临时实现或单次 experiment 让项目方向漂移。

本文件管理 Core 的权威性与修改流程；它不新增具体 scientific claim，也不选择具体 architecture、physical constraint 或 experiment。

## Locked Core files

- `Project_Overview.md`
- `Research_Requirement.md`
- `Core_Governance.md`

`Core_Change_Log.md` 是 append-only audit record，不是研究定义正文。

## What Core may contain

- Project identity and domain
- Core research question
- Scope boundary and explicit exclusions
- Input/output boundary
- Functional and inference requirements
- Representation-learning requirements
- Data constraints
- Scientific-contribution requirements
- Evaluation dimensions
- User-approved high-level research questions, strategic research hypotheses, strategic research directions, or candidate research families, clearly labelled as such

Core strategic framing defines which families of mechanisms or scientific questions the project may investigate. A specific experimentally falsifiable claim with independent/dependent variables, measurable success/rejection conditions, and Experiment linkage is a `HYP-####` record and belongs in `04_Hypotheses/`, not in Core.

## What Core must not contain

- Unreviewed AI brainstorm
- Unregistered external sources or data
- Source summaries presented as decisions
- Unsupported literature claims presented as facts
- Experiment-specific `HYP-####` records, thresholds, hyperparameters, ablations, or local implementation choices
- One-off experiment results
- Unaccepted architecture, loss, dataset, simulator, or physical formula
- Content imported from adjacent projects

## Important interpretation rule

Core scope and requirements have normative authority. `Research Hypothesis`, `Proposed Research Direction`, `may involve`, and `possible approaches` remain strategic hypotheses or candidate-family framing until supported by Evidence and Experiments; a project goal is not proof that it has been achieved.

## Normative and factual authority

The detailed project-wide Authority Model is defined only in `AGENTS.md`. Locked Core has normative authority over project scope and requirements, but placement in Core does not establish factual scientific truth; factual scientific claims still require verified Evidence and/or verified Experiments.

## Core modification gate

A Core change is allowed only when the user explicitly requests or approves it.

Required sequence:

A Locked Core modification is normally a strategic or persistent decision and therefore requires an ADR. Only the objective clerical exception in the Emergency correction rule below may omit one.

1. Identify the exact Core statement to change and why revision is needed.
2. When the change is strategic, persistent, or materially affects future research, record the decision, relevant alternatives, and available Evidence/Experiments in an `ADR-####` with a Core compatibility check.
3. Show the exact proposed patch or before/after wording.
4. Obtain explicit user approval; when an ADR is required, record it as `accepted` only with that approval reference.
5. Apply only the approved change.
6. Append a `CORE-CHG-####` entry to `Core_Change_Log.md`.
7. Re-read all Locked Core files and validate research question, scope, input/output, inference, data, and evaluation consistency.

No Background note, paper, meeting note, Wiki page, experiment, or AI suggestion may bypass this gate.

## Emergency correction rule

Objective clerical errors such as a broken link, malformed heading, or obvious filename typo may be corrected only when the intended text is unambiguous. Record the correction in `Core_Change_Log.md` as `clerical`; do not use this exception to alter scientific meaning.

## Source and context isolation

Unreviewed, unregistered, or unauthorized material must not be promoted into Locked Core.

## Review status of this governance file

This file was created by an AI Agent under the user's explicit instruction to establish project governance. `review_status: pending-user-review` means the user authorized creation of the governance layer but has not yet been represented as having approved every sentence verbatim.
