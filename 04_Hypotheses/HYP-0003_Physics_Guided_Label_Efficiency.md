---
schema_version: "1.0"
id: HYP-0003
type: hypothesis
title: "模拟 targets 与物理训练信号能否减少高保真标签需求"
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
source_ids: [SRC-0003, SRC-0004, SRC-0005, SRC-0008, SRC-0009, SRC-0010, SRC-0011, SRC-0012, SRC-0013]
evidence_ids: [EV-0001, EV-0002, EV-0003]
exclude_from_synthesis: true
---

# 模拟 targets 与物理训练信号能否减少高保真标签需求

## 1. Core relationship

- `00_Project_Core/Research_Requirement.md` Sections 4–8：物理知识融合、效率、limited high-fidelity data、科学贡献和评价。
- `00_Project_Core/Project_Overview.md` Sections 5–7：有效物理学习与独立高维 forward surrogate。
- 用户选择“减少高保真标签需求”作为主目标，而非预设完全无标签。保留独立 reference evaluation，不引入新的 simulator 或 dataset 选择。

## 2. Falsifiable claim

**候选主张：** 对已定义的光刻任务和固定 backbone，在可靠性与适用条件明确时，模拟/解析/Teacher targets 与可计算的物理训练信号，能够降低达到预设 reference quality 和光刻行为标准所需的独立高保真训练标签数。

这是一项标签效率主张。减少标签但增加过多 solver/训练成本不能直接称为“降低总成本”；两种结论分别报告。是否达成整体效率目标需要另检查总成本。

### 三类资源的不同作用

| 资源 | 提供什么 | 对 labels 的含义 | 必要前提 |
|---|---|---|---|
| analytic / simulator / Teacher targets | 为训练输入产生答案或近似答案 | 高保真生成答案仍计入高保真预算；低成本近似答案单列 | 注册来源、适用工况、误差/偏差和计算成本 |
| residual / consistency / 已知 objective | 无需每个输入的 reference 输出也能计算的训练信号 | 可能替代部分监督，不能自动确定唯一正确图像 | 已知参数/条件、可计算关系、identifiability 与多解分析 |
| noise / mixup / 数据变换 | 重用已有成对样本或构造变体 | 不增加独立物理样本数量；有效性不是默认事实 | 变换语义成立，target 同步变换有效，按谱系分割 |

PADM 的 paired-data noising 只是第三类，不证明第一、第二类可省略。ΠNet/DC3 的已知 objective 与 constraints 足以定义其 optimization 问题，不意味着任意固定 loss 能定义正确光刻图像。MSE/SSIM 若需要 reference，就不能被称为无 reference 的物理训练信号。

## 3. Variables and controls

| Role | Variable | Operational definition | Unit/shape | Measurement |
|---|---|---|---|---|
| Independent | 高保真标签预算 | 按独立 layout/conditions 与谱系规则计数，预算档位待冻结 | 独立输入/标签数量 | simulator 生成的高保真标签同样计入 |
| Independent | 辅助资源 | 无辅助、有效模拟 targets、物理信号、二者组合；有效 augmentation 在匹配条件下比较 | 来源类别与数量 | 单因素先比较，再解释组合交互 |
| Dependent | 达标标签数 | 各路线达到同一预设质量与行为标准的最小已测试预算 | 标签数 | budget–performance 曲线，不从噪声版本计样本 |
| Dependent | 相同预算表现 | 固定高保真标签数下的 reference accuracy 与光刻行为 | 输出 shape/单位待定义 | held-out reference 与行为指标 |
| Dependent | 总成本 | target/Teacher/simulator 生成及查询、训练、推理的分项和总量 | 时间/内存/调用计数 | 同硬件条件与实现边界；不隐去离线成本 |
| Controlled | backbone 与输入信息 | 在同一已定义基础 framework 上比较辅助资源，不同时换 architecture | architecture 待定 | HYP-0001 是否成功不改变该控制原则 |
| Controlled | split / sampling / 调参 | 固定 test 与 validation，低预算训练子集按预设规则构建 | 分组与随机策略待定 | 相关 layouts、patches、工况/noise 变体避免泄漏 |
| Controlled | reference 边界 | 独立于训练 targets、target 筛选与 model selection | provenance 待定 | 若同 simulator，只声称 simulator-relative 泛化 |

## 4. Evidence and alternatives

- `BG-0002` 保存跨来源连接。EV-0001–EV-0003 仅支持动态 solver feedback 的机制及 solver 依赖；不证明零数据或低成本，NewPINNs 的 shallow-water warm start 仍使用 labels。
- Source-reported：SRC-0009 PDF pp. 3–6 的 Teacher queries/mixup；SRC-0010 pp. 8–11 的 ADI 数据与 physics loss；SRC-0008 pp. 5–7 的输入选择/solver relabelling。这些区别决定计费与标签统计，不能合并成“免费数据”。
- SRC-0012 pp. 3–6、SRC-0013 pp. 3–5 支持有明确 objective/constraints 的 no-optimal-label optimization；光刻目标充分性未建立。
- SRC-0004 pp. 5–6 的 noising 仍需 paired targets；此事实不是 PADM 数据效率的独立证明。
- SRC-0005 的 NorESM mismatch、SRC-0011 的 residual/reference 差距提示：近似关系可产生系统性偏差；更多这类信号未必提高 reference quality。
- 未验证假设：候选近似模型足够可靠；物理条件能排除无意义/多解输出；辅助数据覆盖与目标工况相符。
- Alternative explanations：实际使用更多高保真调用、更多训练预算、test 泄漏、靠同一近似规则生成训练与评估答案、只改善熟悉工况。

## 5. Test and decision rule

**尚未分配 EXP-ID：** 无 DATA、simulator/physical relation contract、任务指标和预算档位，未运行数据生成或训练。

1. 先建立独立 reference test 和来源账目；定义什么算一个高保真标签，哪些变体属于同一数据谱系。
2. 在同一 backbone 下使用预定的多个训练标签预算。先比较有无模拟 targets、有无物理训练信号；组合效果单独报告，不只展示组合胜过最弱 baseline。
3. 用相同预算的误差比较与达到同等标准所需标签数两种视角评价；数量、误差、调用和总计算同时展示。
4. 只在关系确认有效后使用 mixup/物理变换。若残差含未知参数或有多个满足条件的输出，则先标记不能替代哪些监督，保留 reference 锚定；不擅自改为无标签训练。
5. diffusion noising 和查询挑选规则在比较中匹配或单独 ablate；不能把它们的作用混入其他资源收益。

- **Primary metric / quality target：** 根据首个物理输出冻结；包括 reference 主指标与必要光刻行为容差。标签预算、成本上限与数值阈值尚未定义。
- **Success condition：** 在固定 independent test 上，以更少高保真训练标签达到同一预设质量/行为标准；辅助资源来源有效且全部成本披露。若仅标签数下降而总成本上升，限定为标签效率支持，不宣称整体效率目标已实现。
- **Rejection condition：** 在合格比较中达标标签数未下降，或标签减少仅伴随不被允许的准确率/行为损失，或合成偏差无法满足预设标准。
- **Inconclusive condition：** 预算档位不覆盖达标点、reference 只检查同一生成规则、物理条件不足、数据泄漏或差异无法超出预设不确定范围。
- **Stop condition：** 数据来源/许可/参数不明、辅助 targets 超出有效范围、预定资源上限触发时暂停该测试；不在 test 上修正规则后继续宣称盲测。

## 6. Expected implications

若支持，确定的是某种物理资源在指定任务/预算下的标签效率，非自动获得普遍无标签能力。若否定，保留失败来源与偏差，调整资源而非无限增加不可靠数据。若 inconclusive，先明确 reference、关系充分性或预算范围。

本方向可用于直接预测或 conditional diffusion，不要求 HYP-0001 先获得正结果。与 HYP-0002 的组合只能在各机制单独有明确评价后分析。

后续所需：首个输出定义、高保真/近似 reference 来源、生成/查询账目、物理信号及可辨识性、数据谱系/split、预算曲线与质量/成本阈值。任何长期 dataset/simulator/Method 选择另走对应 ADR，本记录不完成选择。

## 7. Review checklist

- [x] 高保真 labels、近似 targets、physics signals 与 augmentation 分开计数和解释。
- [x] 固定 loss 不等于无标签，label-free optimization 不被改写成 label-free image prediction。
- [x] 支持/否定/不确定与标签效率/总成本结论分开。
- [x] 没有新建不存在的 DATA/PC/METHOD/EXP，未运行生成或训练。
- [ ] 任务、reference、预算和阈值审查完成前保持 draft。
