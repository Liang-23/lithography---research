---
title: "Deep Epidemiological Modeling by Black-box Knowledge Distillation"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-30
updated_at: 2026-09-13
review_status: source-checked
human_audit_status: not-started
knowledge_status: source-reported-claims-unverified
canonical_refs:
  - "02_Evidence/SRC-0009_Deep_Epidemiological_Modeling_by_Black_Box_Knowledge_Distillation.md"
source_ids: [SRC-0009]
source_file: "raw/SRC-0009_Deep_Epidemiological_Modeling_Black_Box_KD.pdf"
exclude_from_synthesis: false
---

# Deep Epidemiological Modeling by Black-box Knowledge Distillation

## Human-readable summary

A costly mixture-SEIR simulation system is queried to create observation/projection sequences. Sequence mixup expands the pool, and a small MLP learns the teacher outputs through MSE. Deployment then uses the MLP without repeating the teacher search. [SRC-0009, pp. 3–6]

This is the clearest admitted example of black-box teacher output $\rightarrow$ student target $\rightarrow$ teacher-free inference, so it informs [[Projection-based Knowledge Distillation]] and [[Amortized Projection and Solver Distillation]]. It is nevertheless not corrected-prediction feedback: the student's raw output is never passed through the teacher and repaired.

## Boundaries

- Outputs are temporal scalar sequences, not spatial images or fields.
- The student has no explicit SEIR-feasibility check or safety gate.
- Exact vector dimensions, daily-versus-weekly evaluation details, and validity beyond four countries and three weeks are under-specified.
- No representation-freedom or lithography conclusion follows.

## 阅读记录 — 2026-09-13

对当前项目的学习而言，这篇保留为熟悉的 Teacher–Student 思路：Teacher 模拟系统生成输入与对应 target，Student 根据这些样本学习预测映射，训练后可以独立预测。Teacher 提供训练答案，没有修正 Student 的输出再教回网络。

用户认为这一核心机制较常见，目前已理解，暂不继续深入，转入 SRC-0011。这是当前阅读价值与进度的判断，不是否定论文全部贡献，也不表示完成 Human Audit 或验证了光刻适用性。

## Governance traceability

Canonical Source: `SRC-0009`, stored at `02_Evidence/SRC-0009_Deep_Epidemiological_Modeling_by_Black_Box_Knowledge_Distillation.md`. Claims remain unverified.
