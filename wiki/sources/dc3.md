---
title: "DC3: A learning method for optimization with hard constraints"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-30
updated_at: 2026-09-12
review_status: source-checked
human_audit_status: not-started
knowledge_status: source-reported-claims-unverified
canonical_refs:
  - "02_Evidence/SRC-0013_DC3.md"
source_ids: [SRC-0013]
source_file: "raw/SRC-0013_DC3.pdf"
exclude_from_synthesis: false
---

# DC3: A learning method for optimization with hard constraints

## 阅读后保留的内容 — 2026-09-12

**用户要求保留的第一条思路：网络可以只预测部分解变量，剩余变量利用已知方程计算。** 前提是选定这部分变量后，确实存在有效且可计算的补齐关系；并非任意变量都可以随意拆分，也不是由网络自行发现缺失的物理方程。[SRC-0013，PDF pp. 3–4，Section 3.1]

**第二条思路：不一定需要提前提供最优答案，但必须知道怎样评价一个答案，以及答案必须满足哪些约束。** DC3 已知任务目标和约束，用补齐、修正后的结果计算目标值及剩余约束违反，再更新网络。这里省去的是最优解标签，不是评价标准、约束定义或训练 loss。[SRC-0013，PDF p. 3 Eqs. (1)–(2)、p. 4 Algorithm 1]

这为 [[Physics Knowledge Integration]] 补充了“由网络和方程分担输出变量”的理解。用户已完成本轮方法概览，认为这两点有启发；记录学习收获不表示全文精读或 Human Audit 已完成。

**迁移边界：** 论文解决受约束优化，不直接证明光刻参考图像预测可以取消标签。光刻中哪些变量可由方程补齐、相应约束与评价目标是什么，目前尚未确定。DC3 在推理时仍保留补齐和修正，没有蒸馏移除这些计算；非线性有限步修正不保证所有样本完全可行。[SRC-0013，PDF pp. 4–6、9]

本节为用户阅读结论，由 Agent 整理；论文陈述仍保留 source-reported / unverified 状态，未选择项目 Method。

## Human-readable summary

DC3 separates a neural partial prediction from equality completion and iterative inequality correction. Completion and correction run during both training and inference; gradients pass through explicit or implicit completion and through the unrolled correction steps. [SRC-0013, pp. 3–6]

This is direct prior art for differentiable terminal completion/correction and connects [[Output-level Physical Correction]] with [[Physics-defined Solution Space Projection]]. It is not corrected-target transfer: DC3 trains from the optimization specification and keeps correction logic at deployment.

## Important boundaries

- Synthetic outputs have 100 variables; ACOPF uses a 57-node graph-state problem, not dense image fields.
- Nonlinear inequality correction has no general convergence guarantee.
- Rounded zero violations do not mean universal exact feasibility; the ACOPF prose reports three slightly violating cases.
- No correction-distance bound, damage detector, gate, fallback, representation-freedom comparison, or lithography evidence exists.

## Governance traceability

Canonical Source: `SRC-0013`, stored at `02_Evidence/SRC-0013_DC3.md`. Claims remain unverified; Human Audit has not started.
