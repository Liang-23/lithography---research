---
title: "Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers"
aliases:
  - "ΠNet"
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
  - "02_Evidence/SRC-0012_Pinet.md"
source_ids: [SRC-0012]
source_file: "raw/SRC-0012_Pinet.pdf"
exclude_from_synthesis: false
---

# Pinet / $\Pi$net

## Human-readable summary

$\Pi$net appends a differentiable Euclidean projection layer to an arbitrary backbone for context-dependent convex constraints. Douglas–Rachford splitting runs in the forward pass, while implicit differentiation propagates gradients through the limiting fixed point. [SRC-0012, pp. 3–6]

This is direct prior art for [[Physics-defined Solution Space Projection]] in a differentiable output layer. It also demonstrates an important boundary for [[Amortized Projection and Solver Distillation]]: replacing a full optimizer with a learned backbone plus a cheaper projection loop is not the same as removing the projector.

## What remains at inference

- Every prediction still executes the explicit projection loop.
- Finite iterations give exact encoded equalities but only numerical convergence for other constraints.
- Outputs are optimization/trajectory vectors up to about $9{,}000$ variables; a $1024\times1024$ image is context input, not corrected output.
- No corrected targets, teacher, safety gate, broad OOD test, supervised prediction-damage analysis, or lithography relationship is provided.

## 阅读结论 — 2026-09-13

用户已理解最值得保留的机制：**将 Projection 放在 loss 之前，以 projected output 计算 loss，并让梯度经过 Projection 更新 neural network 参数。** 关键不仅是前向位置，还包括 gradient path；Projection 自身不是 optimizer。[SRC-0012, PDF pp. 5–6]

是否改善光刻 raw prediction、保留表示能力或满足推理成本，需要本项目自己的实验判断。用户已吸收这一核心机制，暂不要求进一步算法推导；这不等于完成全文 Human Audit，claims remain unverified。

该机制在 [[padm-physics-transfer-low-data-lithography|PADM、物理回传与低数据研究综合]] 中作为 HYP-0002 的比较路径，与 corrected-target learning 分开。没有因此选定 through-Projection 为项目 Method，原文推理保留 Projection 的边界不变。

## Governance traceability

Canonical Source: `SRC-0012`, stored at `02_Evidence/SRC-0012_Pinet.md`. Claims remain unverified; Human Audit has not started.
