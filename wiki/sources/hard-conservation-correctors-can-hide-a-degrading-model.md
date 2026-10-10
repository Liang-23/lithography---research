---
title: "Hard conservation correctors can hide a degrading model when training autoregressive emulators"
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
  - "02_Evidence/SRC-0007_Hard_Conservation_Correctors_Can_Hide_a_Degrading_Model.md"
source_ids: [SRC-0007]
source_file: "raw/SRC-0007_Hard_Conservation_Correctors.pdf"
exclude_from_synthesis: false
---

# Hard conservation correctors can hide a degrading model when training autoregressive emulators

## 阅读后保留的内容 — 2026-09-12

**用户要求保留的提醒：必须区分“修正模块把网络预测的错误修好了”和“网络通过训练学会了避免这些错误”。** 只检查修正后的结果，不能证明原网络已经获得同样的能力。论文给出的具体机制是：整体缩放原始降水图，会被全局守恒修正抵消，因此只监督修正后的图无法识别原始总量的变化。[SRC-0007，PDF p. 6 Eq. (1)、p. 8 Eq. (2)]

**当前阅读取舍（用户判断）：** 这篇与空间物理场预测有关，值得保留上述提醒；但全局修正方式对用户当前的方法学习新增有限，暂不深挖细节。这不等于认定论文无效或没有学术贡献。

**图像处理补准：** 对这里的降水图，论文把每个位置都乘以同一个全局倍数，并没有学习逐像素的修正权重。面积权重用于计算全局总量，与逐像素学习如何修正不同。修正保持空间比例，不能针对性修复区域分布错误；要求的总量由预测的蒸发与储水变化计算，并非对所有样本固定，也不是推理时提供的真实答案。[SRC-0007，PDF pp. 6、8–10]

用户把状态到状态的物理场预测与 mask 到光刻图像的预测作类比。这可以帮助理解 [[Forward Computational Lithography Simulation]] 的高维输入输出，但两者并非同一种物理映射：本文预测多变量、含垂直层的大气状态，分析的降水图是水平空间场。本文不提供光刻中间状态或衍射关系的证据。

**待探索想法，尚未验证：** 用户提出结合 distillation，使 Student 学到有用能力，并探索移除训练阶段依赖。该想法已在 canonical SRC-0007 的用户阅读记录中分类为 raw user idea / unresolved question，未选为项目 Method。[[padm-physics-aware-diffusion-model-for-attenuation-correction|PADM]] 已核对的先例是 Teacher 的 CT 条件注意力／表征传递，以及 Teacher、CT 的移除；Student 的迭代 diffusion 和内部物理计算仍保留。因此它尚不能证明“蒸馏后可移除任意修正模块”。SRC-0007 本身没有 distillation。[SRC-0004；EV-0004–EV-0006]

本节区分用户阅读判断、论文内容和待探索想法；保存学习结论不完成 Human Audit，也不提升科学证据状态。

## Human-readable summary

This paper studies a differentiable global water-budget corrector during weather-emulator fine-tuning. Because uniform precipitation rescaling is erased by the corrector, corrected-output supervision creates a gradient null direction: $C(\alpha P)=C(P)$. Raw precipitation can drift while the delivered field still closes the budget. [SRC-0007, pp. 3–8]

The failure occurs only in the tested combination of corrected supervision and no raw-imbalance penalty. Pre-correction supervision and/or an imbalance penalty stabilize the short ablation. The paper recommends monitoring raw residuals and correction magnitude, making it a central node for [[High-dimensional Safe Correction]].

## What must not be overstated

- The authors explicitly do not show that the delivered corrected product degrades.
- The corrector remains at inference; there is no transfer to a standalone student.
- Evidence comes from one emulator and one water-budget rescaling corrector.
- No automatic gate, correction cap, runtime study, or lithography result exists.

## Governance traceability

Canonical Source: `SRC-0007`, stored at `02_Evidence/SRC-0007_Hard_Conservation_Correctors_Can_Hide_a_Degrading_Model.md`. Claims remain unverified.
