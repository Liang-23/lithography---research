---
title: "Solver-Integrated Adversarial Attacking and Training of Neural Operators"
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
  - "02_Evidence/SRC-0008_Solver_Integrated_Adversarial_Attacking_and_Training_of_Neural_Operators.md"
source_ids: [SRC-0008]
source_file: "raw/SRC-0008_Solver_Integrated_Adversarial_Neural_Operators.pdf"
exclude_from_synthesis: false
---

# Solver-Integrated Adversarial Attacking and Training of Neural Operators

## 阅读后保留的内容 — 2026-09-12

**用户要求保留的思路：物理信息可以用来决定接下来训练哪些样本，以及确定这些样本应该对应什么样的物理结果。** 对目前的学习而言，这补充了物理信息进入模型的一处位置：训练样本的选择与参考结果的构造，而不只是在预测后进行 [[Output-level Physical Correction]] 或 [[Physics-defined Solution Space Projection]]。

**论文的具体实现：** SRC-0008 的完整 solver 一致方案通过 adversarial attacking 寻找当前 neural operator 与 solver 分歧较大的输入。修改输入后，用 solver 重新计算对应结果，再用这些输入与参考结果训练同一个 neural operator。这里物理信息参与“选哪些题”和“这些题对应什么答案”。[SRC-0008，PDF p. 5 Eqs. (21)–(25)、pp. 6–7]

**必须保留的边界：** solver 是这篇论文采用的物理信息载体，不能由此推出“我们的项目必须用 solver 才能引入物理信息”。同样，论文也没有验证任何尚未指定的无 solver 替代方式。如何在光刻项目中选择物理上有意义的样本、确定参考结果、引入训练过程，目前都未确定；本笔记不选择实现方案。

**与此前理解的区别：** 新增的是“物理信息作用于样本选择和参考结果构造”这一思路，并不是训练从此不使用 loss；论文仍然用损失来寻找困难输入并更新网络。“新方式”指用户当前学习框架得到扩展，不是对整个领域作首创性判断。

本节为用户阅读结论及待解决的迁移问题，由 Agent 整理；论文陈述仍保留 source-reported / unverified 状态，不因保存笔记而完成 Human Audit。

## Human-readable summary

This work uses a numerical solver as an oracle during adversarial neural-operator training. Perturbed inputs are relabelled with the solver, and the same surrogate is fine-tuned on those field pairs. Final inference is structurally solver-free, but the solver is not correcting a raw neural output and there is no separate student. [SRC-0008, pp. 3–7]

Outputs include Burgers fields of length $1024$, Darcy grids, and $256\times256$ Navier–Stokes vorticity. This is relevant to [[Amortized Projection and Solver Distillation]], while remaining technically distinct from output projection.

## Important trade-off

The full solver-integrated training wins most constructed shifted datasets but loses the ordinary train/test comparisons reported for Burgers and Darcy. Solver differentiation can also be extremely expensive. [SRC-0008, pp. 16–17, 24–25]

The paper does not establish exact feasibility, output correction, a safety gate, representation-freedom benefit, or lithography validity.

## Governance traceability

Canonical Source: `SRC-0008`, stored at `02_Evidence/SRC-0008_Solver_Integrated_Adversarial_Attacking_and_Training_of_Neural_Operators.md`. Claims remain unverified.
