---
title: "EngGeneNet transient heat-conduction surrogate"
aliases:
  - "Transient heat conduction modelling for real-time operation and control of steel-making reheating furnaces"
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
  - "02_Evidence/SRC-0010_EngGeneNet_Transient_Heat_Conduction.md"
source_ids: [SRC-0010]
source_file: "raw/SRC-0010_EngGeneNet_Transient_Heat_Conduction.pdf"
exclude_from_synthesis: false
---

# EngGeneNet transient heat-conduction surrogate

## Human-readable summary

The accepted manuscript trains a field-to-field network from ADI-generated transient temperature data while also using finite-difference physics residuals and an embedded `Eng-Gene` feature transform. The deployed network no longer runs ADI. [SRC-0010, PDF pp. 5–12]

This is spatial solver-to-surrogate transfer, but the paper uses “knowledge distillation” more broadly than standard teacher-student imitation. It does not run ADI on a raw prediction and feed the corrected result back as a target. The embedded physics module and physics-informed training objective also mean it is not a clean example of an otherwise unconstrained student.

## Evidence and boundary

- The output is a small 2D cross-section, nominally $16\times16$ or possibly $17\times17$ because indexing is ambiguous.
- Reported per-frame time is $0.1608\,\mathrm{s}$ for ADI versus $0.0059\,\mathrm{s}$ for PI-EngGeneUNet. [SRC-0010, PDF pp. 15–16]
- No exact hard-boundary verification, safe-correction mechanism, large-tensor test, or lithography evidence exists.

This source connects [[Projection-based Knowledge Distillation]] with [[Amortized Projection and Solver Distillation]], while remaining only partial overlap.

## 阅读启发：让明确的物理关系参与网络内部计算

这篇论文在热传导领域提供了一个值得借鉴的例子：将已知的物理依赖关系做成 Eng-Gene 模块，参与网络内部计算，并在推理阶段继续保留。这提醒我们，端到端 AI surrogate 可以包含明确的物理计算。移除生成数据的 ADI，并不意味着移除网络内部的 Eng-Gene。[SRC-0010, PDF pp. 8–11, Sections 3.4、4.2]

对我们的光刻项目而言，如果输入到物理输出的映射中，有一部分物理依赖关系已经明确、能够可靠计算，而且计算成本较低，就可以考虑把它直接加入网络内部。神经网络在利用这些已知关系的基础上，继续学习复杂的高维映射。这为 [[Physics Knowledge Integration]] 补充了一个作用位置：物理关系可以参与形成预测的内部计算。

这里值得探索的是：哪些关系适合显式计算，以及怎样让这些计算帮助网络学习，同时保留 [[Neural Representation Learning]] 所要求的表示灵活性。EngGeneNet 提供了热传导实例；这种思路在光刻中是否有效、计算成本是否合适、是否会限制表示能力，仍需要验证。

**记录性质：** 2026-09-13 用户要求保存的阅读启发，由 Agent 整理。项目迁移部分为 draft、尚待验证的条件性想法，不是已选 Method 或 verified Evidence，也不代表完成 Human Audit。这里的高维“映射”不特指可行集合上的 projection。

## Governance traceability

Canonical Source: `SRC-0010`, stored at `02_Evidence/SRC-0010_EngGeneNet_Transient_Heat_Conduction.md`. The admitted artifact is the CC BY accepted manuscript, not the version of record.
