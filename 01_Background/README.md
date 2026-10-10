---
schema_version: "1.0"
id: BACKGROUND-POLICY
type: layer-policy
lifecycle_status: active
authority_class: derived
authority_scope: background-policy-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User request on 2026-08-26"
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
exclude_from_synthesis: true
---

# Background Layer

`01_Background` 保存经过 source linking 的 domain context、terminology、existing approaches 和问题背景。它回答“已有语境是什么”，不回答“本项目已经决定做什么”。

## Authority

- Background 是 `working context`，没有 normative authority。
- Background 不能修改 Core、接受 Method、验证 Hypothesis 或替代 Evidence。
- Background 中的每个 factual claim 应引用 `EV-ID`；只有 source link 而没有 claim-level Evidence 时，必须标记 `unverified`。

## Admission rules

每个 `BG-####.md` 必须：

- 使用 `_templates/Background_Record_Template.md`；
- 关联一个或多个已登记 `SRC-ID`；
- 区分 quote、paraphrase、AI interpretation 和 inference；
- 记录 applicability、assumptions、limitations 与 conflicts；
- 标记 `created_by`、`content_origin` 和 `review_status`；
- 在 source checking 前保持 `lifecycle_status: draft`。

## Prohibited content

- 无来源的“已证明”结论
- Project decision
- Core revision
- Experiment conclusion without `EXP-ID`/`EV-ID`
- Unregistered external source or dataset
- AI suggestion presented as domain fact

Use [Background Index](Background_Index.md) as the single register for Background records.
