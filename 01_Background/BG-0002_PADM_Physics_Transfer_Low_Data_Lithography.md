---
schema_version: "1.0"
id: BG-0002
type: background-record
title: "以 PADM 为重点的物理融合、知识回传与低数据光刻研究背景"
lifecycle_status: draft
authority_class: working
authority_scope: context-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User explicitly requested implementation of the PADM-focused synthesis and three draft hypotheses, 2026-09-13"
created_at: 2026-09-13
updated_at: 2026-09-13
owner: project-lead
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
source_ids: [SRC-0001, SRC-0002, SRC-0003, SRC-0004, SRC-0005, SRC-0006, SRC-0007, SRC-0008, SRC-0009, SRC-0010, SRC-0011, SRC-0012, SRC-0013]
evidence_ids: [EV-0001, EV-0002, EV-0003, EV-0004, EV-0005, EV-0006]
hypothesis_ids: [HYP-0001, HYP-0002, HYP-0003]
exclude_from_synthesis: true
---

# 以 PADM 为重点的物理融合、知识回传与低数据光刻研究背景

## Purpose and scope

本记录把已登记文献连接到三个研究问题：如何形成图像、物理信息如何进入学习、如何减少昂贵标签需求。它保存来源定位和跨领域适用条件，为 HYP-0001、HYP-0002、HYP-0003 提供背景；假设的具体主张与判断规则由对应 Hypothesis records 管理。

用户已明确偏好优先研究 conditional diffusion＋U-Net，以 correction → 知识回传为主线，以减少高保真标签需求为数据目标。“优先”指本轮研究讨论顺序，不表示长期 architecture 或 Method 已被选择。用户授权创建记录，不等于批准全部科学结论。

2026-09-13 用户阅读综合笔记后进一步澄清：正文应先解释本项目为何需要“自由形成预测 → 输出端 correction → 教回网络”，再说明 PADM 怎样服务于这条主线，不能由文献机制列表代替项目问题。本轮优先解释 output 阶段的物理作用，不以 physics-derived input features 或 hidden feature 约束作为组合前提。用户随后确认其 parameters 设想为“少数几个物理参数，用它们生成整张 image”；生成模块是否仍读取 mask、输出表达范围，以及完整输出/每步 clean estimate 的接口区别，记录于 HYP-0002，均未成为选定设计。关于导师实验与 soft/hard 优劣的转述不是已登记实验 Evidence。

范围为当前注册的 SRC-0001 至 SRC-0013，共 13 篇。用户提到的第 14 篇尚未与登记记录对应，不创建来源或补入外部知识。只使用项目内已批准版本；不读取 Quarantine、Archive 或相邻项目，不以新版论文补全当前版本。

## Core relevance

- `00_Project_Core/Project_Overview.md` Sections 5–7：物理知识融合与高维表示能力，以及 output correction → knowledge transfer 的候选研究主线。
- `00_Project_Core/Research_Requirement.md` Sections 1–7：forward 输入/输出、端到端部署、表示能力、光刻行为、效率与有限高保真数据。
- 输入仍为 mask layout、optical conditions 与可用 process parameters；候选输出仍在 aerial image、resist image、wafer image 范围内，未选首个输出阶段。
- 内部 iterative diffusion 可以是完整预测模型的一部分，但仍需满足计算效率要求。外部输出 Projection 的保留方案只作比较；不得用“layer”的命名规避最终无必需外部 filtering/post-processing 的要求。
- “自由表征”是待检验目标。没有额外 physics loss、没有改变参数量或没有直接限制 hidden features，都不能单独证明表示能力得到保护。
- SRC-0001 的 inverse-optimization / mask-generation 部分不进入候选设计。不存在 Core 修改、Method 选择、正式实验或领域创新认定。

## Source-grounded statements

以下全部为 paraphrase，没有新增原文引语。EV 的 verified 状态仅覆盖表中列出的有界机制，不覆盖光刻迁移或整篇论文。完整来源身份、版本、逐项审查保留在各 canonical Source record。

| 来源与作用 | 原论文机制及定位 | 验证状态 | 光刻候选用途：项目 inference | 所需条件 / 尚未证明 |
|---|---|---|---|---|
| SRC-0001：适用边界 | 其 Source record 的 Project admission 将 forward surrogate 背景与 inverse optimization 区分 | Source-checked；科学 claims unverified | 仅保留 forward-surrogate 范围背景 | 不引入 ILT、mask optimization 或生成 mask 的目标 |
| SRC-0002：output Projection | 训练后将输出投向显式约束集合；推理运行优化器；PDF pp. 2–3, Eq. (1), Fig. 1c；pp. 6、10 的多解与求解边界 | Source-reported / unverified | 提供网络与外部 correction 分离的对照 | 需光刻 admissibility、距离度量和可计算 solver；最近可行值不是 reference answer 的同义词 |
| SRC-0003：动态 solver feedback | 当前 neural field 进入 solver，返回值影响 loss，梯度不穿过 solver；PDF p. 3 Fig. 1, pp. 5–9；p. 22 warm-start 例外 | EV-0001–EV-0003 verified within boundary | 研究无 solver derivative 的动态物理训练信号和部署依赖移除 | 不是 fixed corrected-target distillation；光刻反馈算子、稳定性和成本尚缺 |
| SRC-0004：逐步重建与内部物理 | image-space Brownian-bridge training 与采样；U-Net 的物理量相关输出参与内部重建；PDF pp. 4–6, Eqs. (7)–(15), Algorithms 1–2 | 内部机制由 EV-0005 有界验证；其他细节 Source-reported | conditional diffusion 的重点结构参考；比较已知物理关系如何参与重建 | paired AC target 仍需要；不能将 NAC/AC 路径、attenuation 公式直接移为 mask/光刻关系 |
| SRC-0004：representation transfer | CT-conditioned Teacher attention 与 Student 匹配；部署去除 Teacher/CT，保留 iterative diffusion 与内部 physics-aware path；PDF pp. 4–6, Eqs. (16)–(18) | EV-0004、EV-0006 verified within boundary | 研究训练期额外信息能否留在只需部署输入的 Student 中 | 没有 projected-output labels；无完整 feature aggregation 实现或光刻 privileged input 定义；无实测推理加速证明 |
| SRC-0005：关系失配 | terminal LR/HR 一致性；NorESM 中硬满足不匹配关系损害 reference accuracy；PDF pp. 5–7、27–28、32, Table 14 | Source-reported / unverified | 要先检查候选关系对 reference 是否适用 | 不能从气候聚合关系推导光刻约束；不能将物理一致性等同准确性 |
| SRC-0006：correction 分配 | 可学习向量分配全局 invariant correction；某些 minimum-distance Projection 降低预测准确性；PDF pp. 3–5、7–8, Tables 3–4 | Source-reported / unverified | 区分“满足多少约束”与“修改哪些输出位置” | 对应的是特定 linear/quadratic invariant；无光刻适用性、部署移除或普遍安全保证 |
| SRC-0007：raw-model 学习 | 特定 scale-invariant corrector 的 gradient nullspace 可掩盖 raw 幅度退化；PDF pp. 4–8, Eq. (1), Figs. 2–3 | Source-reported / unverified | 同时观察 raw、corrected 和 deployed prediction，避免把组合系统收益当作网络收益 | 不代表所有 correction 或最终 corrected product 都退化；不证明任何一种蒸馏一定避免该问题 |
| SRC-0008：查询与样本利用 | 固定当前网络、搜索扰动输入、solver 重新标注并训练同一网络；PDF pp. 5–7；pp. 24–25 的 clean/shifted trade-off | Source-reported / unverified | 在给定高保真预算下考虑哪些输入值得查询 | 不是 raw-output correction；额外 solver 调用和 clean accuracy 损失必须计入 |
| SRC-0009：Teacher targets | 查询序列、sequence mixup、MSE imitation；PDF pp. 3–4, Eqs. (3)–(5), Algorithm 1；pp. 5–6 | Source-reported / unverified | familiar Teacher–Student target 路径、Teacher-free 部署、昂贵样本利用 | temporal sequence 非空间图像；mixup 不能无依据地套用非线性光刻映射 |
| SRC-0010：内部计算与模拟数据 | ADI 离线生成温度场；Eng-Gene 与 physics loss 作用不同；PDF pp. 8–11, Eqs. (25)–(28), Sections 3.4、4.2–4.3 | Source-reported / unverified | 便宜且可靠的已知关系可考虑作为内部计算；模拟 targets 可补充训练资源 | 时间推进与 mask-to-output 只是结构类比；热传导公式不能直接迁移；无标签或自由表征收益未确立 |
| SRC-0011：residual correction 与缓存 | 线性化 residual 求 correction，合适离散形式下缓存 Jacobian pseudoinverse；PDF pp. 3–4, Eqs. (5)–(6)；pp. 5–7 的误差/成本边界 | Source-reported / unverified | 寻找可计算 correction，区分可预计算算子与每次变化的 residual | 算子须对变化状态和配置仍有效；外部 correction 推理保留；零 residual 不等于 reference 精确 |
| SRC-0012：through-Projection 学习 | 用 projected output 计算 objective，implicit gradients 更新网络；convex feasible set；PDF pp. 3–6, Algorithms 1–3 | Source-reported / unverified | 比较 gradients 经过 Projection 与 target-based transfer | 推理保留 Projection；有限迭代未必满足全部 constraints；已知 objective 的优化不同于 reference image 预测 |
| SRC-0013：completion 与无 optimal labels | partial prediction、equality completion、inequality correction；已知 objective 与 constraints 驱动训练；PDF pp. 3–5, Eqs. (1)–(4), Algorithm 1 | Source-reported / unverified | 检查能否从部分变量确定其余变量、或以物理信号减少监督 | 需可计算且有效的 completion；推理保留相关计算；没有证明无标签即可确定光刻输出 |

## PADM：本轮重点理解的可迁移结构

### 输入、训练状态、网络计算和输出各是什么

PADM 的 paired NAC input 与 AC target 共同构造中间 noisy state。Algorithm 1 随机抽取 diffusion timestep 和 Gaussian noise，再训练重建网络；这不要求每个训练样本完整执行一条采样轨迹。Algorithm 2 在 inference 从条件输入 NAC 开始，重复使用网络逐步得到 AC 重建。噪声状态的增加不等于增加独立的正确物理标签。[SRC-0004, PDF pp. 5–6]

U-Net 是重建计算主体，物理相关 quantities 参与内部 attenuation-factor 构造。其结构启发是“部分明确物理关系进入每一步预测”，不是让网络自动发现并验证材料定律。预测的 path lengths 与 attenuation field 缺乏独立真实性验证，不能仅因变量命名为物理量就视为物理事实。[EV-0005]

Teacher 的额外 CT 信息通过 attention/representation transfer 进入 Student；paired AC target 并未消失。原文没有 external Projection → corrected label 的流程。光刻中是否存在相应 privileged input，及 Teacher 的优势来自信息还是模型/预算差异，均未确认。[EV-0004、EV-0006]

### 对光刻的结构 inference 及边界

可以研究由 mask 和条件信息指导的逐步 output reconstruction，也可以对照直接 image-to-image prediction。尚未定义输出的单位、尺度、物理阶段、noise schedule 或输入输出桥接方式；不能因为两者都呈现为图像，就直接用 PADM 的 Brownian bridge 将 mask 和目标物理场线性混合。

diffusion timestep 是算法变量，不自动表示传播距离、曝光时间、resist 演化或任何真实中间物理状态。最终预测可以包含网络内部迭代；是否保留便宜物理模块由后续 Method/实验评估，不预设应删除所有物理计算。收益应表现为 reference accuracy 与光刻行为，而非单纯视觉平滑或更丰富纹理。

## Terminology and research interfaces

以下符号为本项目比较候选流程使用，不替换来源中的同名字母：

| 项目符号 / 术语 | 工作含义 | 尚待定义 |
|---|---|---|
| $x$ | mask layout 与可用 optical/process conditions 的输入集合 | 通道、shape、单位、坐标及工况范围 |
| $y_{\mathrm{ref}}$ | 独立参考输出 | aerial/resist/wafer 中首个阶段及 reference provenance |
| $y_{\mathrm{raw}}=F_\theta(x)$ | 完整基础预测器输出，尚未经过额外外部 corrector；$F_\theta$ 可以包含多步 diffusion | architecture、sampling policy 和计算预算 |
| $C_x(y_{\mathrm{raw}})=y_{\mathrm{corr}}$ | 待定义 output correction；不预先假定是 Projection、精确或可微 | 关系、metric、可行性、成本及有效范围 |
| $R(x,y)$ | 待定义的物理 residual/consistency 检查 | 缺失答案时是否能计算、是否足以确定目标输出 |
| $y_{\mathrm{deploy}}$ | 最终完整部署模型输出；HYP-0002 的目标路径无额外外部 corrector | 保留的内部迭代/物理计算及所需条件 |
| representation freedom | 不无必要地限制学习复杂高维映射的能力 | 需结构/gradient 分析与行为对照，不等同单一分数 |

## Assumptions and applicability

1. framework、物理知识进入位置、监督资源是三个维度；先做可归因的局部比较，再讨论组合。
2. 独立样本应按物理输入及数据谱系定义；同一 layout 的 patches、工况变体和 noisy states 的分组规则须冻结，不能让高度相关内容泄漏至 test。
3. 高保真 simulator 生成的标签仍计入高保真预算；近似 simulator 或 analytic targets 也不是零成本或默认 ground truth。混合数据需分别记录来源、误差和调用。
4. 固定 objective 能用于无 reference 训练，需要其无需 target 即可计算，且条件/方程对目标输出有充分约束。一个 MSE/SSIM 名称或固定 loss 权重不提供这些条件。
5. independent reference 指与训练 targets、model selection 隔离的评估；若测试也来自同一 simulator，结论仅是该 simulator-relative accuracy，不能宣称物理真实性已被独立证实。
6. 为学习位置比较保持 backbone、数据、调参和计算预算可比；diffusion 步数与采样次数计入推理成本。不得以 test ground truth 选择最佳生成样本。

## Conflicting evidence and unresolved disagreements

- SRC-0005/0006/0011 显示 constraint satisfaction 与 reference fidelity 可能分离。这与纠正误差的期待构成检验问题，不是所有物理融合无效的结论。
- SRC-0012 展示 through-Projection training 的 Source-bounded 收益；SRC-0007 展示特定 corrector 下 raw-model drift。问题、operator 与评估不同，不将二者合并成“梯度经过 Projection 必然好/坏”。
- PADM 不证明 iterative diffusion 在光刻中优于直接 prediction，亦无其速度收益测量；成本主张不得从其他论文移植。
- 既有 BG-0001 与其 Wiki projection 使用了“必须设置 accept/reject safeguard”的较强项目 inference。本记录不将其提升为 Core 要求；该表述不授权 external risk harness，本轮仅设计 raw/corrected/reference 的研究比较。既有记录保留，未静默改写。
- 没有 verified lithography Evidence 支持 HYP-0001–HYP-0003；EV-0001–EV-0006 只是相邻任务内的机制先例。

## Known gaps and downstream routing

HYP-0001 管理 conditional diffusion 的收益/成本问题；HYP-0002 管理 correction/representation transfer 后的独立预测问题；HYP-0003 管理高保真标签效率问题。三者为 draft，未选方法且尚不具备执行条件。

后续最小缺口为：首个目标输出阶段及 reference 定义；物理关系与适用工况；数据与 simulator provenance；部署可获得参数；可接受的质量/成本阈值；数据分组和 held-out 协议。先按 hypothesis 定向寻找这些内容，再创建 PC、DATA、METHOD 和 preregistered EXP。本轮不分配不存在的这些记录 ID。

2026-09-13 定位复核：直接复核已批准 PADM PDF pp. 5–6、ΠNet p. 6、DC3 p. 3；其余表项使用当前 canonical full-text reconstruction 及本会话此前已检查的局部原文。不代表本轮重新通读全部论文或新增 Human Audit。

## Review checklist

- [x] 仅使用已登记来源，Source-reported 与 verified Evidence 分开。
- [x] 项目 inference、用户偏好与作者结论分开，没有新增原文引语。
- [x] 无 Core 修改、方法选择、物理方程编造或实验执行。
- [x] 相关假设保存为独立 draft records；缺失条件明确。
- [ ] 项目负责人审查本综合解释与三个 hypothesis 的科学措辞。

`exclude_from_synthesis: true` 保留待审查状态；本次显式授权的 Wiki projection 仅展示有状态标记的阅读解释，不将本记录升级为事实或更高层科学结论。
