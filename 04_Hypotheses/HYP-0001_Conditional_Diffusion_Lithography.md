---
schema_version: "1.0"
id: HYP-0001
type: hypothesis
title: "conditional diffusion＋U-Net 的光刻预测收益与成本"
lifecycle_status: draft
authority_class: working
authority_scope: candidate-hypothesis-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User explicitly requested the PADM-focused plan implementation, 2026-09-13"
created_at: 2026-09-13
updated_at: 2026-09-13
owner: project-lead
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
hypothesis_state: draft
source_ids: [SRC-0004, SRC-0010]
evidence_ids: [EV-0004, EV-0005, EV-0006]
exclude_from_synthesis: true
---

# conditional diffusion＋U-Net 的光刻预测收益与成本

## 1. Core relationship

- `00_Project_Core/Project_Overview.md` Sections 5–7：在高维映射学习中有效融入物理知识。
- `00_Project_Core/Research_Requirement.md` Sections 1–3、5–8：端到端输出、表示能力、光刻行为、效率与有限数据。
- 用户将 conditional diffusion＋U-Net 设为优先候选研究 framework；本记录不选择长期 architecture。
- 输出仍在 aerial image、resist image、wafer image 范围内，未确定首个阶段。输入保持 mask layout 与可用 optical/process conditions，排除 ILT。

## 2. Falsifiable claim

**候选主张：** 在同一已定义光刻任务、相同高保真训练样本和可比训练预算下，conditional diffusion＋U-Net 相比直接预测 U-Net，可以改善独立参考上的空间预测表现，同时满足预先定义的推理成本和重要光刻行为容差。

预期机制是把映射学习组织为条件引导的逐步重建。它是否比直接映射更容易保留边缘、频率与工况响应，必须由比较确认。逐步重建不保证每一步误差单调下降；外观更丰富也不代表预测更准确。

基础比较先不加入额外 physics module、外部 correction 或 Teacher transfer。明确且廉价的内部物理计算作为后续独立 ablation；不能将它与基础 diffusion 同时添加，再把全部收益归给 diffusion。

PADM 的 Brownian-bridge 路径依赖 paired NAC/AC 图像。光刻输入/输出的尺度、单位、状态路径与条件编码仍缺失；这里没有选择 Brownian bridge、noise schedule 或 sampling algorithm。diffusion step 不被解释为真实光刻阶段。

本假设不主张 diffusion 普遍优于直接预测、不主张无需 labels、不主张噪声扩增产生新物理样本，也不证明 representation freedom。

## 3. Variables and controls

| Role | Variable | Operational definition | Unit/shape | Measurement |
|---|---|---|---|---|
| Independent | 预测 framework | 直接 U-Net 与 conditional diffusion＋U-Net；基础比较不加额外物理/Teacher 机制 | architecture 尚未指定 | 配置与计算图记录 |
| Dependent | reference accuracy | 在独立 test 输入上比较完整输出与 reference；主指标待输出定义后从 Core 指标中冻结 | 图像单位/shape 待定义 | MSE/SSIM 候选，不先混成一个总分 |
| Dependent | 空间/工况行为 | edge、frequency、process response；只有所需条件与参考可用时测量 | 待物理任务定义 | 指标实现和容差须预先冻结 |
| Dependent | sampling repeatability | 同一输入不同预设随机种子的输出变化及误差分布 | 与目标输出一致 | 不以 test reference 挑选最佳样本 |
| Dependent | deployment cost | 完整输出所需时间、峰值内存、网络调用/采样次数 | 时间与内存单位在 Plan 中固定 | 同硬件、batch、precision 的测量 |
| Controlled | 数据与调参资源 | 相同独立高保真输入/标签、split、条件信息、训练和调参预算 | 样本计数按谱系定义 | 噪声版本不增加独立样本数 |
| Controlled | backbone 可比性 | 同类 U-Net 容量和条件信息，披露 time embedding 等必要差异 | 参数/算力待定义 | 不假称两个计算图完全相同 |

## 4. Evidence and alternatives

- `BG-0002` 汇总来源连接。EV-0004–EV-0006 仅验证 PADM 的有界 transfer、内部物理和部署机制；不支持本假设的光刻性能或速度结论。
- Source-reported：SRC-0004 PDF pp. 5–7 的 conditional diffusion、U-Net 与图像实验；SRC-0010 pp. 8–11 的内部物理变换和 field-to-field 预测。两者不是同一机制，后者也不是 diffusion 证据。
- 限制性材料：PADM 未提供 isolated physics-module/transfer ablation、representation-freedom 检验或实测推理加速；不能以其完整系统结果归因于 diffusion。
- 未验证假设：光刻输出结构适合逐步重建；收益足以抵消多步推理开销；有限独立样本能够支持训练。
- Alternative explanations：更多网络调用或训练预算、参数容量、conditioning、平滑效应、不同调参力度、以参考选择最佳 sample。
- Confounders：先添加物理模块或 privileged Teacher；同一 layout 的近重复 patch/noise 泄漏；只对 diffusion 做更充分调参。

## 5. Test and decision rule

**尚未分配 EXP-ID：** 无 DATA contract、首个输出定义、实现与阈值，因此仅记录最小测试设计，不执行。

1. 先冻结输出、reference、数据分组、主质量指标、空间/工况容差与成本上限。
2. 在相同独立样本与可比训练/调参预算下比较基础直接 U-Net 和基础 conditional diffusion；报告误差与完整推理成本。
3. 以固定 sampling policy 做重复性测量。步数/样本数如需扫描，只在 validation 选择，test 不择优。
4. 仅在具体关系有来源与规范后，为相同 framework 增加内部物理模块对照，单独检验该机制；不因此修改基础比较结论。

- **Primary metric：** 未选；需依据首个目标输出确定并在运行前冻结。
- **Success threshold：** 数值未设。支持需 reference 主指标达到预先规定的改善，关键光刻行为无超容差退化，且完整部署成本在上限内；不允许看结果后补阈值。
- **Rejection condition：** 在满足预定比较条件时没有达到主指标改善，或收益伴随超容差行为退化/超预算推理；仅更平滑或看起来更好不支持主张。
- **Inconclusive condition：** 预算/调参不匹配、输出参考不足、波动超过预定义不确定范围，或关键行为无法评估。
- **Stop condition：** 数据泄漏、无效 target、资源上限触发时停止该次测试并保留记录；此处不是部署 fallback。

## 6. Expected implications

- 若支持：diffusion 获得在该任务/预算下继续研究的依据，再用 HYP-0002/0003 分析知识回传与标签效率；不自动成为 selected Method。
- 若否定：降低 diffusion 优先级，直接预测仍可承载 HYP-0002/0003；不会因 PADM 阅读偏好而隐藏失败。
- 若 inconclusive：补齐比较条件，不能以喜欢逐步生成的概念替代证据。
- 缺失条件：输出单位/shape/坐标、reference 来源、data split、sampling/architecture、训练与部署预算、主指标/阈值。
- 持久 architecture 选择须单独记录 ADR 并由用户明确批准；本记录与本次创建授权不完成选择。

## 7. Review checklist

- [x] Core、来源与假设边界分开；变量、替代解释、支持/否定/不确定结果可区分。
- [x] 不把 diffusion timestep 当作物理阶段，不将内部模块收益归为基础 diffusion 收益。
- [x] 说明尚未可执行的原因，没有虚构 DATA/PC/METHOD/EXP 记录。
- [ ] 输出、指标、阈值和实验条件完成定义并审查；满足之前保持 draft。
