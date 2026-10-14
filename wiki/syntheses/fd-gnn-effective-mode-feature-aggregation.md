---
title: "FD-GNN Effective Mode Feature Aggregation"
aliases: []
type: synthesis
lifecycle_status: draft
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-14
updated_at: 2026-10-14
review_status: unreviewed
core_alignment: pass
canonical_refs: ["08_Project_Status/FD_GNN_Effective_Mode_Progress_Review_2026-10-14.md", "08_Project_Status/FD_GNN_Global_Context_Candidates_2026-10-14.md", "05_Method_Design/METHOD-0003_Mask_Conditioned_Effective_Mode_FD_GNN.md"]
source_ids: [SRC-0016, SRC-0017, SRC-0018]
method_ids: [METHOD-0003]
evidence_ids: []
---

# FD-GNN: 从 Pair 信息到 Effective Modes 的候选学习结构

## Research status
**用户已审核研究进度回顾；架构仍是未验证的 Method candidate。** 这里解释当前设计，不代表已有优越性实验证据。

我们希望训练一次，在未见过的新 Mask 上直接前向生成 Mask-conditioned Effective Modes，并计算 Aerial Image。有效模式 $b_r(k)$ 只需是有用的 latent representation，不要求恢复真实光学 Coherent Modes。

## 已定的信息流与边界
- FFT 给出已知 $A(k)$，频率位置 $k$ 为 Frequency Node。
- Pair Product $p_{k,l}=A(k)A^*(l)$ 是 **确定性计算**，不是神经网络预测。
- Frequency Difference $q=k-l$ 决定 Pair 的**最终物理输出频率**。
- 用 $b_r(k)=G_\theta(A)_{r,k}$ 生成 $R$ 张有效模式图（中间表示）。
- 物理 Renderer：$\widehat I(q)=\sum_{k-l=q}A(k)A^*(l)\sum_r b_r(k)b_r^*(l)$；最终由 Aerial Image label 和普通反向传播训练。

## GNN 内部学习（区别于最终物理贡献）
已认可：Frequency Node 可以读取与自己相连的 Frequency Pairs，更新 Hidden Feature；此内部 Feature Routing 不得冒充 `q` 输出端的光强路由。

当前唯一明确列为待验证的 Aggregation Candidate A：

$$s_k=\sum_{l\in\mathcal N(k)}w_\theta(k-l)A(k)A^*(l).$$

其中 $w_\theta$ 是可学习的 Edge-conditioned Weight，$s_k$ 是内部 hidden feature 聚合值，**不是** $\widehat I(k)$。聚合是否过早丢失 Pair 信息、如何通过 $U_\theta$ 更新节点、如何接 Prediction Head，尚未确定。

## Related reading
- [[neural-message-passing-for-quantum-chemistry|Neural Message Passing for Quantum Chemistry]]：Message Passing Foundations，论文中的 graph framework 不等于光刻结果。
- [[how-powerful-are-graph-neural-networks|How Powerful are Graph Neural Networks?]]：Aggregation Expressivity，提醒测试压缩信息是否丢失。
- [[deep-sets|Deep Sets]]：Set Aggregation Theory，帮助分析邻居集合的顺序不变性。

三个来源均为官方在线版本的登记与摘要级 digest；尚未完成全文 Human Audit，也没有得到 Verified Evidence。

## 还需解决
定义 $U_\theta$、复数/向量聚合、Pair Sampling、FFT indexing、Hermitian/nonnegative intensity policy、独立泛化评估、显存和成本。与已注册的 Direct-pairwise FD-NIG 相比仍无正式实验。


## 2026-10-14 补充：两轮 Pair Messages、Global Context 与 Effective Mode Generator

**新进展是用户认可三个需要对照研究的 Generator 输入方案，并非验证出最佳模型。** 内部 GNN 仍只有三种节点：Frequency `F_k`、Pair `P_{k,l}`、Difference `D_q`。Frequency Node 的初始特征包含 `Re A(k)`、`Im A(k)` 和归一化的**绝对频率坐标** `(k_x,k_y)`，不加入实空间 `(x,y)` 位置。已知的 `A(k)A*(l)` 不由网络重新预测。

**消息与最终成像不可混为一谈。** 当前更丰富的候选 Message Passing 是 Pair Node 读取相连两端 Frequency Hidden Features、已知复数 Pair Product 和 `q=k-l` 后生成高维 Message；Frequency Node 对多个 Pair Messages 做 Attention + Max 的候选 Aggregation、Residual Update。暂用两轮得到 `h_k^(2)`，但这不是经验证的最优深度。Difference Node 继续在最终光强频谱端收集相同 `q` 的 Pair Contributions；是否也参加内部更新尚未决定。旧版差频加权求和 Candidate A 仍是独立待比较方案，没有被证实无效。

### 三种已认可的待比较方案

| 方案 | Generator 使用什么信息 | 为什么考虑 | 局限 |
| --- | --- | --- | --- |
| **L0 Local-only** | 只有本节点 `h_k^(2)` | 必须保留简洁基准，直接测两轮 GNN 是否足够 | 稀疏 Pair Graph 可能限制两轮可达范围 |
| **G1 Graph Global** | `h_k^(2)` + 从当前 Mask 所有**已建立 Frequency Nodes** 聚合的 `g_M^graph` | 低成本共享上下文，可先试 Mean + Max | 如果 Frequency Nodes 是采样子集，则这个全局向量并不覆盖完整频谱 |
| **G2 Full Spectrum Global** | `h_k^(2)` + 独立读取整个 `A(k_x,k_y)` 的 `g_M^spectrum` | 显式接触 Pair/Node Sampling 可能略过的频率信息 | 如何保留二维频谱、复数相位以及推理效率尚未设计清楚 |

三种方案**均不改变原来的 Graph Nodes 或 Edges**。G1/G2 是每张 Mask 独立计算的 Generator 旁路输入，不能跨 Mask batch 混合。Generator 对每个 `k` 输出 `R` 个复数 `b_r(k;M)`，最终仍使用原本的 `A(k)A*(l) Σ_r b_r(k;M)b_r*(l;M)` 沿 `P_{k,l} → D_{k-l}` 汇聚后 iFFT 得到 Aerial Image。

### 为什么这是待验证的问题？

两轮传播覆盖率取决于 Pair Graph 稀疏度；即便两轮能够接触大量 Frequency Nodes，固定宽度聚合也可能损失重要的分布信息。反过来，如果 Pair Graph 足够密，Global Encoder 未必值得额外的计算。G2 还需考虑 Fourier Phase 和空间平移带来的协变/等变条件。对于固定光学条件，真实 TCC 不应被误写为随 Mask 改变；Mask-conditioned Effective Modes 是灵活的 surrogate 中间表达。

**下一步：** 在不改 Graph 拓扑的前提下，研究轻量的 Full-Spectrum Global Encoder，比较如何保留绝对频率、复数实/虚部和二维频谱结构；正式实验必须单独预注册。候选状态及理由以 `METHOD-0003` 与 `FD_GNN_Global_Context_Candidates_2026-10-14.md` 为准。这里是人类阅读层，不是 Verified Evidence。
