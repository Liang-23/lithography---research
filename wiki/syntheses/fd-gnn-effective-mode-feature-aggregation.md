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
canonical_refs: ["08_Project_Status/FD_GNN_Effective_Mode_Progress_Review_2026-10-14.md", "05_Method_Design/METHOD-0003_Mask_Conditioned_Effective_Mode_FD_GNN.md"]
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
