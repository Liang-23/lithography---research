---
schema_version: "1.0"
id: HYP-0002
type: hypothesis
title: "correction 知识回传能否改善独立网络预测"
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
source_ids: [SRC-0002, SRC-0003, SRC-0004, SRC-0005, SRC-0006, SRC-0007, SRC-0011, SRC-0012, SRC-0013]
evidence_ids: [EV-0001, EV-0002, EV-0003, EV-0004, EV-0005, EV-0006]
exclude_from_synthesis: true
---

# correction 知识回传能否改善独立网络预测

## 1. Core relationship

- `00_Project_Core/Project_Overview.md` Sections 5–7：高维表示学习、output correction、knowledge transfer。
- `00_Project_Core/Research_Requirement.md` Sections 1–5、7–8：物理融合、表示能力、预测行为与最终无必需外部 post-processing 的部署。
- 核心目标是分清“corrector 改好了输出”和“训练改善了最终网络”。外部 Projection 保留的路径只作研究对照，不作为已批准最终部署架构。

## 2. Falsifiable claim

**主候选主张（target 路径）：** 对同一 backbone、相同高保真样本与可比预算，在适用且能改善部分训练/validation 预测的 correction 关系下，使用 `stop-gradient` corrected targets 回传知识，可使不含额外外部 corrector 的部署输出较无回传对照获得预先定义的预测/物理行为收益。

**条件性子问题（representation 路径）：** 若存在合法、可靠且有额外信息价值的 training-only input，Teacher representation transfer 是否也能实现上述部署收益？这是 PADM 提供的不同载体，必须单独评价，不能把二者合并为无法否定的“任一路径成功即可”。目前此子路径尚无光刻 privileged input 定义。

预期机制是网络通过目标差异或 representation 信号调整参数，而非依赖外部 corrector 永久接管误差。梯度经过 Projection 的训练作为关键比较，不预先认定更好或更差。

### 候选流程与 gradient boundary

本节为项目接口示意，不是任何论文的复现公式。设 $y_{\mathrm{raw}}=F_\theta(x)$，$y_{\mathrm{corr}}=C_x(y_{\mathrm{raw}})$。$C_x$ 尚未指定，也未保证为可微 Projection。

| 路径 | 训练中发生什么 | 梯度 | 评价与部署 |
|---|---|---|---|
| 无物理回传对照 | 使用相同可用参考/基础训练目标；匹配额外训练预算 | 更新 backbone | 评价原始完整输出 |
| 训练后 correction | 已训练 predictor 的输出经过 $C_x$，不以其回传更新网络 | 无 correction-derived 参数更新 | 同时报告 raw/corrected；外部 corrector 保留只作对照 |
| corrected targets | 计算 $z=\operatorname{stopgrad}(C_x(y_{\mathrm{raw}}))$，用 $z$ 指导网络；保留/组合基础目标的方案须在 Plan 固定 | 经过学习网络，不经过 target 的 corrector 分支 | 重点检验移除外部 corrector 后的完整输出 |
| through-Projection | $\mathcal L(C_x(F_\theta(x)),y_{\mathrm{ref}})$ 为有 reference 情况的示意；无 reference objective 另见 HYP-0003 | 经 $C_x$ 与 backbone；须有适用 derivative | raw 与 projected 分别报告；移除后退化不算成功知识保留 |
| 条件性 representation transfer | 冻结 Teacher，仅提供已定义 feature/attention target；Student 使用部署可获得输入 | 更新 Student，Teacher target 固定 | 移除 Teacher/privileged input；仍计内部迭代与物理计算 |

对于 diffusion，$F_\theta$ 表示完整基础输出过程，raw output 不是随意某个 noisy state；“移除外部 corrector”不等于移除 iterative sampling 或所有内部物理计算。对 noisy state、每步 clean estimate 或最终 sample 做 correction 是不同 Method 选择，本轮只把最终完整输出作为共同接口，不暗中固定中间步物理语义。

### 用户讨论澄清与待定接口 — 2026-09-13

以下记录用户对综合笔记的修正及 AI-assisted 概念解释；不改变 hypothesis_state，不选择 Method，也不新增科学 Evidence。

- **研究主次：** 用户要求从 Core 的“高维预测 → output correction → 知识回传 → 独立部署”出发组织研究。HYP-0002 解释物理融合的中心问题；HYP-0001 是承载该学习过程的优先 framework 候选；HYP-0003 是有限高保真数据下的检验条件。编号不表示应先完成 HYP-0001 才能讨论回传。
- **物理作用位置：** 用户最后明确希望网络自行学习输入到输出的复杂映射，优先在 output 阶段使用物理知识；本轮候选解释不以添加 physics-derived input features 或约束 hidden feature maps 为前提。mask layout、optical conditions 与可用 process parameters 仍是定义 forward 任务的输入，不把取消人为派生 features 解释成删除任务条件。
- **导师经验的状态：** 用户转述导师曾观察到 input features 影响学习自由度，并提及 soft/hard 的优劣。当前没有对应实验记录、条件或数据；仅作为用户偏好的缘由，不认定为本项目已验证结果或普遍结论。物理位置、是否精确满足关系、梯度经过哪里，是三个不同问题。
- **diffusion 与 target 回传的组合解释：** 可把一轮学习理解为：已有完整 predictor 生成图像，output corrector 产生 corrected target，固定该 target 分支，再以同一 mask/工况和该 target 构造 diffusion 训练状态，更新 U-Net。具体 noising/conditioning 需按所选 diffusion 定义，不直接套用 PADM 的 NAC/AC Brownian bridge；reference 监督的保留、target 质量与刷新方式仍待规定。corrected target 不是已知真实答案。此解释展开了已有 corrected-target 候选，未新增一套已选训练算法。
- **每步 correction 的区别：** 如果进一步讨论逐步物理修正，首先区分每步预测的 clean image estimate 与 noisy state；只有前者已明确对应待约束的物理输出时，才有资格讨论该物理关系。把 corrected clean estimate 如何送回 diffusion update、训练与部署是否保留它，均是未决接口，不把每步 Projection 当作既定方案。当前共同对照仍使用最终完整输出。
- **输出形式的随后澄清：** 用户明确回答 parameters 指“少数几个物理参数，用它们生成整张 image”，并非逐位置 parameter maps。记录为当前讨论的用户设想，尚非选定 Method。若 image 仅由少数 parameters 与固定生成算子构成，可表达的图像族将依赖该参数化是否充分；如果生成算子还读取原始 mask/工况，不能仅按参数数量断言丢失空间信息，但需检查主要 forward 计算是否仍由该物理生成模块承担及其成本。参数语义、生成模块的输入和适用范围未确定，不以 PADM 的高维物理 fields 为少量参数生成全图提供充分性证明。
- **为检验表示能力保留的接口比较：** “少数参数决定完整 image”与“网络预测完整 image，少数参数仅参与 output correction”可作为待定义的两种接口比较，后者只展开已有 SRC-0006 的 correction 分配与 PADM auxiliary clean-image 分支所提示的角色区别，不指定光刻参数或方程。待检验问题是哪些空间信息由神经网络负责、哪些由物理算子负责；两者都不自动证明 representation freedom。此项是 unresolved design question，不替代已定义的 HYP-0002 主 target 假设。

概念讨论可以先在“有一个适用的 output corrector”这个明确假设下继续，不必等待全部光刻知识补齐。具体 PC/DATA/阈值是后续实现与实验的必要条件，不是本轮解释停止的理由。

## 3. Variables and controls

| Role | Variable | Operational definition | Unit/shape | Measurement |
|---|---|---|---|---|
| Independent | 回传路径 | 无回传、post-hoc、corrected target、through-Projection；representation 单列条件分支 | 流程类别 | 前向/梯度图与 target 来源 |
| Dependent | 独立网络预测 | 无外部 corrector 的完整部署输出与 reference 比较 | 输出 shape/单位待定 | Core 中适用的 accuracy 与行为指标 |
| Dependent | correction 依赖 | raw/corrected/deployed 的表现差异及 correction 幅度 | 与输出一致 | 分开评价，不能只展示 corrected 结果 |
| Dependent | physical consistency | 候选关系在 reference、raw、corrected、deployed 上的 residual | PC 定义后确定 | 不替代 reference accuracy |
| Dependent | 成本 | correction 查询、target/Teacher 生成、额外训练和完整部署成本 | 时间/内存/调用计数 | 固定硬件等比较条件 |
| Controlled | 学习与数据条件 | 同一 backbone、初始训练/checkpoint 规则、信息、split、调参和预算 | 待定义 | matching 条件逐项披露 |
| Controlled | correction 与 targets | 相同关系、算子精度和输出 metric；target 刷新策略固定 | 尚无 PC | 避免把更强 solver、更多 labels 当作 gradient 路径收益 |

## 4. Evidence and alternatives

- `BG-0002` 保存来源全貌。EV-0001–EV-0003 验证 NewPINNs 的动态 solver feedback、梯度边界与依赖限制，不证明本项目 corrected-target transfer。
- EV-0004 验证 PADM attention/representation transfer；EV-0006 验证 Teacher/CT 移除而非所有物理计算移除；EV-0005 不验证其学习到的物理字段为真。
- SRC-0012 PDF pp. 3–6 与 Appendix C.4 支持 through-Projection 作为对照；SRC-0002 pp. 2–3 和 SRC-0011 pp. 3–4 支持 post-hoc correction 对照。均保留 Source-reported 状态。
- SRC-0005 pp. 27–28、32；SRC-0006 pp. 7–8；SRC-0011 pp. 5–7：错误/近似物理关系或目标失配可损害 reference fidelity。
- SRC-0007 pp. 4–8：特定 corrector 下 corrected loss 可掩盖 raw drift；不是所有梯度穿过 correction 都失败的证据。
- 未验证假设：候选 correction 提供有用而非自我强化的偏差；网络能学到其收益；teacher 的额外信息合法且在训练期可获取。
- Alternative explanations：更多训练轮次、更强 Teacher/solver、额外参考标签、数据泄漏、只做平滑；correction target 的局部改善不保证新输入上的提升。

## 5. Test and decision rule

**尚未分配 EXP-ID：** 缺 DATA、PC、backbone、target protocol、指标与阈值。以下只是最小比较设计。

1. 用训练/validation 检查候选关系在 reference 上的适用性及 correction 的收益/损害，再冻结所用 operator、输出 metric、精度和 target 生成规则。
2. 比较 post-hoc correction、corrected-target learning 与 through-Projection training，并加入无物理回传的预算匹配对照；保持任务、数据、backbone 与调参资源可比。不可微/不满足条件的 $C_x$ 不伪装成 through-Projection，记录该比较不适用。
3. 分别评估 raw、corrected、deployed；reference test 不参与 target 生成、correction 筛选、sampling 择优或模型选择。
4. target 路径须预先冻结刷新频率、冻结 snapshot/同网更新方式、基础监督保留方式；这些尚未指定，不据此开展训练。
5. representation 分支仅在额外信息定义后单独比较，并设置不含该 transfer 的 Student 对照；不能因为额外数据更多就将收益全部归于 transfer。

- **Primary metric / numerical thresholds：** 目标输出确定后冻结。支持必须在移除外部 corrector 后达到预定义 reference 改善与物理行为/成本要求。
- **Rejection condition：** 主 target 路径只降低 corrected residual、仅保留外部 corrector 时改善，或部署 raw prediction 未达标准/损害关键空间行为，则拒绝该主张在测试边界内成立。representation 分支按自身对照单独判定。
- **Inconclusive condition：** 没有有效 correction、不可区分 target bias 与学习能力、比较数据/预算不匹配或参考不足。
- **Stop condition：** target 明显不在关系有效范围、计算不稳定、数据污染或资源超限时暂停该次测试，保留失败记录；不设计新的部署 risk harness。

## 6. Expected implications

若支持，说明在特定关系/数据/预算下观察到知识保留，不自动证明精确 feasibility 或 representation freedom。若否定，不能仅凭 corrected output 优秀继续宣称网络学到物理；应回到关系、target 质量或学习路径分析。若 inconclusive，先补齐原因，不扩大来源结论。

“自由表征”至少分为结构是否受限、gradient 是否被改变、复杂空间行为是否被保留三个问题。同样参数量、相同网络名或 raw metric 单点改善，都不构成表示能力的完整证明。

后续缺口为物理关系/PC、可微性、correction metric、数据与 reference、必要的 privileged input、目标刷新与损失安排、架构和计算预算。任何持久 Method 选择须经过 ADR；不以本次 draft 创建代替选择。

## 7. Review checklist

- [x] 区分 corrected targets、representation transfer 与 through-Projection gradients。
- [x] 主 target 假设与条件性 representation 分支单独可否定，不以任一成功掩盖另一失败。
- [x] raw/deployed 定义涵盖完整 diffusion 过程；未把内部迭代误作外部 correction。
- [x] 没有虚构 PC、DATA、METHOD、EXP 或 Teacher-only 光刻信息。
- [ ] 关系、协议、阈值及实现经审查并完整冻结；满足前保持 draft。
