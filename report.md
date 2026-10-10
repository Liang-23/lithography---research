# 近两日研究进展

## 1. 最近完成的工作

近两日主要深入阅读并核对了 NewPINNs 和 PADM 两篇工作，重点分析 physics information 如何进入 neural network 的 training，以及最终 inference 是否仍依赖外部物理信息。同时建立了长期研究 context 管理框架，使后续 AI-assisted research 能读取已核验结论并追溯原始依据，减少 context drift 和错误累积。

## 2. NewPINNs 带来的启发

NewPINNs 研究的是利用 neural network 求解偏微分方程。其核心思路是：网络先预测当前物理场，传统数值求解器再基于该预测向前计算，并把结果作为训练反馈，帮助网络逐步逼近更合理的解。求解器参与训练指导，但训练完成后，论文报告的预测过程由网络直接输出空间场。

这说明物理知识不一定都要写成 neural network 内部的可微公式，也可以由外部 physics tool 在 training 阶段提供动态指导，而不进入最终预测路径。对 lithography surrogate 而言，这为“训练时借助高保真模拟器、推理时由 surrogate 独立预测”提供了参考。不过，训练指导的质量仍受数值求解器精度、稳定性和计算成本制约。

![[Pasted image 20260901173603.png]]

## 3. PADM 带来的启发

PADM 来自医学影像中的心肌灌注 SPECT 衰减校正：输入是未经衰减校正的图像，CT 可以额外提供 attenuation map，目标是重建质量更好的校正图像。PADM 将 diffusion model、衰减相关物理计算和 Teacher–Student 结构结合起来。Training 时，Teacher 同时接收医学图像和 CT-derived attenuation map；Student 只接收原始医学图像，并学习 Teacher 利用额外物理信息时形成的内部 representation / attention information，而不是简单模仿 Teacher 最终生成的一张校正图像。

其价值在于说明：额外 physics information 可以只在 Teacher 侧用于 training，Student 在 inference 时不再需要该额外输入。PADM 与 lithography 的物理系统、数据和任务均不同，因此不能直接验证 lithography 方法；但它为分离“训练期 privileged physics information”和“部署期输入要求”提供了具体设计先例。需要注意的是，PADM-S 在 inference 时仍保留 diffusion sampling 和内部 physics-aware processing。


![[Pasted image 20260901173453.png]]




## 4. 对当前 lithography 项目的新认识

当前项目要建立从 mask layout、光学条件和工艺参数到 aerial image、resist image 或 wafer image 的端到端高维 surrogate，同时避免物理约束不必要地限制 representation learning，也避免最终 inference 长期依赖外部校正模块。

两篇论文共同把问题进一步具体化：physics knowledge 不只有“直接加入 loss”一种入口。NewPINNs 展示了“外部数值求解器提供动态训练反馈”的路线；PADM 展示了“掌握额外物理信息的 Teacher 向较少输入的 Student 传递内部表示”的路线。由此，下一阶段应重点比较：物理信息在何处进入、以什么形式传递、训练后哪些依赖能够移除，以及哪些计算仍会留在 inference 中。这是基于现有文献形成的项目认识，尚不是已选定的方法。

## 5. 下一步

继续核验其余 pivotal Sources，并比较不同 physics-integration 机制与当前端到端、representation learning 和 inference requirements 的匹配程度。

---

## Internal Evidence Reference

- `EV-0001` — NewPINNs 中数值求解器提供动态训练反馈。
    
- `EV-0002` — NewPINNs 报告的直接 neural field 预测路径。
    
- `EV-0003` — NewPINNs 对求解器精度、稳定性和成本的继承。
    
- `EV-0004` — PADM 的 CT-conditioned Teacher 到 NAC-only Student 信息传递。
    
- `EV-0005` — PADM 在 diffusion 内部进行衰减相关物理计算。
    
- `EV-0006` — PADM 移除 Teacher/CT 输入，但保留 diffusion 与 physics-aware inference。