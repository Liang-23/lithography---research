---
title: "PhysicsCorrect: A Training-Free Approach for Stable Neural PDE Simulations"
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
  - "02_Evidence/SRC-0011_PhysicsCorrect.md"
source_ids: [SRC-0011]
source_file: "raw/SRC-0011_PhysicsCorrect.pdf"
exclude_from_synthesis: false
---

# PhysicsCorrect

## Human-readable summary

PhysicsCorrect is a training-free external predictor-corrector. At every rollout step it linearizes a discretized PDE residual around the raw prediction, solves a least-squares correction, and feeds the corrected state forward. A constant Jacobian and pseudoinverse can be cached for suitable semi-implicit residuals. [SRC-0011, PDF pp. 3–4]

The method operates on $64\times64$ and $128\times128$ 2D fields and a 512-point 1D state. It is strong spatial evidence for [[Output-level Physical Correction]], but the external residual evaluation and pseudoinverse multiplication remain mandatory in inference.

## Safety and scaling boundary

- A one-step linearized residual correction is not proof of exact nonlinear projection.
- Discretization mismatch means zero residual can differ from the numerical reference.
- Time and memory scale quadratically with grid resolution; fully 3D use is an explicit challenge.
- No gate, correction cap, fallback, corrected-target transfer, or representation-freedom comparison is provided.
- The abstract's “under $5\%$” overhead conflicts with a reported $0.90/0.69\,\mathrm{s}$ comparison; the artifact does not reconcile it.

These limits make the source central to [[High-dimensional Safe Correction]].

## 阅读记录：缓存 residual 到 correction 的转换算子

对当前阅读而言，PhysicsCorrect 的“预测后再进行物理 correction”整体 framework 已较熟悉，新增的框架启发有限。值得保留的是它减少重复计算的具体思路。

在特定的离散方程和固定配置下，residual 到 correction 的线性转换算子可能保持不变。因此，可以提前计算并缓存这个算子；后续每次预测只需计算新的 residual，再通过缓存算子计算新的 correction，从而减少重复计算。[SRC-0011, PDF pp. 3–4, Eq. (6) and Jacobian Caching]

**缓存的是转换算子，不是 residual 或 correction。** 不同预测仍产生不同 residual 和 correction。能否缓存，需要从离散方程确认算子不依赖变化的状态，并检查相关参数、网格和时间步长等配置是否仍适用。这个条件不对所有 PDE 自动成立。

本节记录 2026-09-13 用户的阅读判断，由 Agent 整理。“新增启发有限”是对当前学习价值的判断，不是否定论文全部贡献。光刻适用性尚未验证，保存笔记不表示完成 Human Audit 或选定项目 Method。

## Governance traceability

Canonical Source: `SRC-0011`, stored at `02_Evidence/SRC-0011_PhysicsCorrect.md`. Only the published AAAI artifact was reviewed; extended arXiv content was not imported.
