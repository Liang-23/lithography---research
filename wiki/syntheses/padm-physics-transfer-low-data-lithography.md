---
title: "从 PADM 与物理知识回传到低数据光刻预测"
aliases:
  - "PADM 光刻研究候选方案"
type: synthesis
lifecycle_status: draft
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "用户要求执行 PADM 重点综合与三个 draft hypotheses 计划，2026-09-13"
created_at: 2026-09-13
updated_at: 2026-09-13
review_status: unreviewed
core_alignment: pass
knowledge_status: source-grounded-candidate-hypotheses-unverified
canonical_refs:
  - "00_Project_Core/Project_Overview.md"
  - "00_Project_Core/Research_Requirement.md"
  - "01_Background/BG-0002_PADM_Physics_Transfer_Low_Data_Lithography.md"
  - "04_Hypotheses/HYP-0001_Conditional_Diffusion_Lithography.md"
  - "04_Hypotheses/HYP-0002_Correction_Knowledge_Transfer.md"
  - "04_Hypotheses/HYP-0003_Physics_Guided_Label_Efficiency.md"
source_ids: [SRC-0001, SRC-0002, SRC-0003, SRC-0004, SRC-0005, SRC-0006, SRC-0007, SRC-0008, SRC-0009, SRC-0010, SRC-0011, SRC-0012, SRC-0013]
evidence_ids: [EV-0001, EV-0002, EV-0003, EV-0004, EV-0005, EV-0006]
hypothesis_ids: [HYP-0001, HYP-0002, HYP-0003]
exclude_from_synthesis: true
---


# 从 PADM 与物理知识回传到低数据光刻预测

**我们要研究的是：先让网络学习复杂的光刻映射，再利用输出端的物理 correction 指导它学习，使改善尽可能留在最终网络里。** conditional diffusion＋U-Net 是用户希望优先探索的预测方式；它要服务于这个问题。低数据则是这个方法必须面对的现实条件。

本文从项目问题解释候选流程，再调用论文中有用的部分。HYP-0001–HYP-0003 仍为 draft。下面的组合是待检验的项目设想，没有选定 architecture，也没有实验证明。

## 1. 我们的项目为什么需要这条路线

本项目做 [[Forward Computational Lithography Simulation]]：输入 mask layout、optical conditions 和可用 process parameters，预测 aerial image、resist image 或 wafer image。mask 在这里是输入；最终交付的是光刻物理输出，首个预测阶段尚未选定。

高保真模拟昂贵，我们希望网络学会这个复杂的高维映射，==*减少每次预测的成本*==。但训练样本有限，网络即使在已有图像上拟合得好，也可能在新的 layout 或工况下出现物理上不合理的行为。==*因此，项目需要利用物理知识补充数据。*==

接下来的问题才是研究重点：==**怎样利用这些知识，同时给网络留下学习复杂空间关系的能力？**== Core 已提出一条候选主线：

> 网络形成高维预测 → 物理关系修正输出 → 修正信息教回网络 → 检查独立预测是否改善。

[[overview|项目 Overview]] 定义了这条研究主线与最终独立部署的目标。它是一项研究假设，不是“输出端物理一定优于其他位置”的证明。

用户本次明确希望优先在 output 阶段使用物理信息，不先给输入附加 physics-derived features，也不先规定 hidden feature maps 应当服从哪些物理关系。optical/process conditions 仍然用于说明“这张 mask 在什么条件下被预测”，与额外设计的物理 features 不应混淆。

这样重新看三项候选，H2 是物理融合的中心问题，H1 探索用什么预测过程承载它，H3 检验这种学习能否减少昂贵标签。编号不是研究先后顺序。

## 2. 在输出端使用物理，不等于不通过 loss 学习

先区分三件事：物理在哪里参与计算、是否强制满足某个关系、梯度通过哪里更新网络。它们可以有不同组合。

| 做法                          | 物理具体做什么                    | 网络怎样获得学习信号                              |
| --------------------------- | -------------------------- | --------------------------------------- |
| physics loss                | 对输出违反物理关系的程度打分             | residual penalty 产生梯度                   |
| 内部物理计算                      | 用已知关系变换中间数据或构成预测结果         | 后续 loss 经实际计算路径更新可学习部分                  |
| output correction 后不再训练     | 直接修改已完成的预测                 | 原网络没有从该修正获得更新                           |
| corrected-target learning   | 把修正后的图像作为学习目标              | 网络拟合 target，梯度不经过 target 的 corrector 分支 |
| through-Projection training | 用 projected output 计算 loss | 梯度经过 Projection，再更新网络                   |

所以，[[enggenenet-transient-heat-conduction|EngGeneNet]] 的内部变换与它的 physics loss 是两件事；[[padm-physics-aware-diffusion-model-for-attenuation-correction|PADM]] 的内部 attenuation 计算也不只是多加了一个 residual penalty。模型最后使用 loss 训练，不能抹掉前面计算方式的区别。[SRC-0010, PDF pp. 8–11；EV-0005]

通常说的 soft constraint，是通过惩罚鼓励满足关系；hard constraint 是通过结构或求解机制要求所指定的关系得到满足。**输出端 Projection 本身也可能是 hard constraint；用 loss 拟合它给出的 target，又不保证网络每次都精确满足该关系。** 因此不能把“输出端物理”直接称为 soft，也不能把“有 loss”直接称为传统 physics-loss 方法。

用户转述的导师经验是本轮偏好的背景，但项目没有对应实验记录，不能据此写成“soft 远强于 hard”的普遍事实。当前更准确的问题是：物理以什么方式介入，怎样影响训练，以及网络最后保留了什么能力。

“自由表征”也不是参数不受物理信息影响。我们希望物理改善学习，它必然会影响参数更新；希望避免的是不必要地缩小网络能表达的复杂映射范围。是否做到了，要结合 [[Neural Representation Learning]]、raw prediction 与空间行为检查。

## 3. 先用直接预测理解完整的学习过程

暂时假设我们已经有一个适用的 output corrector，不在这里编造光刻公式。最容易理解的一轮 corrected-target learning 是：

1. **先预测。** 同一 mask 和工况输入网络，由网络形成一张完整的物理预测图像。
2. **再修正。** corrector 读取预测与所需工况，根据已知物理关系调整图像，得到 corrected image。
3. **把修正结果教回去。** 在这次更新中，把 corrected image 视为固定 target，让网络对原输入的预测向它靠近。已有 reference 监督如何保留，需要随后定义。
4. **检查学到了什么。** 用未参与训练的新输入，只运行更新后的网络，检查预测是否改善。

这里的第三步就是 [[Projection-based Knowledge Distillation|知识回传的候选作用]]。如果只做到第二步，我们改善的是“网络加 corrector”的系统，网络参数没有因此变好。

为了看清梯度边界，可以用一组接口符号表示。它们不是光刻定律：

$$
y_{\mathrm{raw}}=F_\theta(x),\qquad
z=\operatorname{stopgrad}\!\left(C_x(y_{\mathrm{raw}})\right).
$$

$x$ 是输入及工况，$F_\theta$ 是预测网络，$C_x$ 是待定义的 correction，$z$ 是本次使用的 corrected target。用 $y_{\mathrm{raw}}$ 与 $z$ 的差异更新 $\theta$，但不通过 $z$ 的生成分支对 $C_x$ 求导。后续是否刷新 target、何时刷新、是否使用冻结的网络版本，都还没有选定。

==**这与“直接对物理 residual 求导”的区别在于：物理计算(corrector)先给出一个可供学习的目标，网络通过拟合该目标调整自己。它仍然会改变网络的学习方向，也仍可能继承 corrector 的偏差.**==

[[physics-consistent-machine-learning-with-output-projection-onto-physical-manifolds|SRC-0002]] 给我们输出后 Projection 的出发点，但没有完成上述知识回传；[[newpinns|NewPINNs]] 则说明物理计算的返回值可以参与训练，而不必对 solver 本身求导。二者都不能代替对本项目 corrected-target 效果的验证。[SRC-0002, PDF pp. 2–3、8–9；EV-0001–EV-0003]

“小的 correction”可以是希望研究的性质，==*但小改动不自动代表保留了重要边缘或频率信息。满足已知关系的 corrected image，也不自动成为真实答案。*==

## 4. PADM 怎样接到这条主线上

### 将直接预测换成逐步重建，物理回传的目的保持一致

借鉴 PADM，可以让 U-Net 在 mask 和工况的条件引导下，多次参与重建，最终形成完整预测。这样，上一节的 $F_\theta$ 表示整个 conditional diffusion predictor，不再只表示一次 U-Net 调用。

一轮候选训练可以理解为：

> 当前 diffusion predictor(entire procedure) 生成完整图像 → output correction 得到 corrected target → 用该 target 构造带噪训练状态 → U-Net 学习在原 mask/工况条件下重建这个 target。

展开其中最容易误解的一步：我们先有 corrected image，再按所研究的 diffusion 训练规则对它构造 noisy states。U-Net 接收训练状态、timestep 与原输入条件，学习恢复目标信息；*具体预测 clean image、noise 或其他等价量，留到 architecture 定义时选择*。原始 reference targets 可以继续提供监督，组合方式尚待比较。

这样，**在这个候选训练流程中，物理 correction 先修改网络生成的完整输出图像，修正后的图像再作为 training target，用于更新 U-Net。diffusion 则规定如何从这个 target 构造带噪训练状态，以及如何在预测时逐步重建图像。。** 不需要先把一张人为设计的 physics feature map 拼进 mask，也不需要假定 hidden features 都有物理含义。

这是 HYP-0002 的 corrected-target 候选与 HYP-0001 的 diffusion 候选之间的具体连接。它不是 PADM 原文已经实现的流程，也尚未证明 corrected target 足够准确、能改善泛化或减少标签。

目标部署路径是：

> mask 与工况 → 学习后的 conditional diffusion predictor → 完整物理预测图像。

这条知识回传候选希望移除外部 corrector；网络内部的 diffusion 迭代仍存在，成本必须计算。只有在这条独立部署路径上仍有收益，才支持“物理修正的帮助被网络学进去”。

### 逐步物理 correction 是另一个需要区分的接口

如果想更接近 PADM 的“每一步都有物理计算”，可以进一步讨论在每一步网络预测的 **clean image estimate** 上进行 correction，再研究如何用于后续重建。

这里有两个限制。首先，clean estimate 必须明确对应所要约束的物理输出；noisy state 含有算法人为加入的噪声，不能未经定义直接当作真实物理图像使用方程。其次，修正后的 estimate 怎样进入下一步、训练与 inference 是否都保留 correction，是额外的设计问题。

因此，“每一步修正当前估计”和“修正完整输出，再教网络重建”不是同一流程。当前最小比较仍使用完整输出这个共同接口。每步方案保留为待讨论接口，不在缺少定义时宣布已经成立，更不能仅把外部 corrector 改名为网络 layer 就认为解决了独立部署问题。

### PADM 原文给出的依据与没有给出的部分

PADM 在 SPECT 中用 paired NAC input 与 AC target 构造带噪训练状态，采用 Brownian-bridge 路径，推理从条件输入 NAC 开始逐步重建。它支持我们认真考察这种 image-to-image 过程，但 mask 与光刻输出的语义、单位和尺度不同，不能直接照搬其桥接方式。[SRC-0004, PDF pp. 5–6, Algorithms 1–2]

原文还有两项独立机制：预测的物理相关 fields 参与内部 attenuation-factor 计算；CT-conditioned Teacher 提供 attention/representation transfer。后者不是外部 Projection 生成 corrected-output labels。部署移除 Teacher/CT，保留 Student 的 iterative diffusion 与内部物理计算。[EV-0004–EV-0006]

因此，我们吸收的是逐步重建和训练知识传递的机制参考，再围绕本项目的 output correction 重新提出组合问题。diffusion step 不代表真实光刻阶段，noise variants 也不等于新的独立正确样本。光刻中尚没有已定义的 Teacher-only 信息，不能为了模仿 PADM 而虚构 CT 的对应物。

## 5. 如果 U-Net 输出 parameters，再生成 image，会发生什么

用户已明确说明：这里希望 U-Net 输出的是**少数几个物理参数，用它们生成整张 image**。这与直接预测完整图像有实质区别；它是当前讨论的设想，还没有成为选定 architecture。

| 输出形式 | 图像由谁决定 | 对“自由学习”的关键问题 |
|---|---|---|
| 完整 image | 网络直接预测各位置的物理输出，再考虑 correction | correction 是否修改了本来有用的空间信息 |
| 整张 parameter map 或多张 fields | 网络预测逐位置变量，后续关系把它们组成 image | 这些 fields 与生成关系是否足以表达所需图像 |
| 少数 physical parameters | 少数参数与固定生成算子决定整张 image | 是否把复杂输出压缩到了过小的可表达范围 |

用户当前设想对应第三行。如果后续模块只读取这几个参数，整张图像就只能来自固定生成关系允许的图像族。即使这些图像看起来很复杂、Projection 的改动很小，网络也不能自行表达该生成关系之外的空间变化。因此，**把物理放在 output 端，并不自动保留自由表征；还要看 network output 留下了多少表达空间。** 少量参数是否已经足够覆盖目标任务，需要后续依据，不能仅凭参数少就断言一定失败。

还有一种重要情况：生成模块同时读取原 mask/工况与这些参数。此时不能说所有空间信息都被压进几个数，因为 mask 仍把高维几何信息传给生成模块；但必须辨明主要的 forward 计算由谁完成。如果复杂光刻映射仍主要由物理生成模块计算，网络的作用可能更接近预测参数，效率目标也要按整个系统检查。生成模块的输入目前尚未确定。

PADM 确实预测物理相关 fields 并参与图像计算，但没有验证这些 fields 都具有真实、可辨识的物理意义；它不能替我们证明这个接口在光刻中的充分性。[EV-0005]

围绕用户关心的自由学习，可以对照两种职责：**少数参数决定整张 image**，或**网络先预测完整 image，少数参数只参与 output correction**。后一种职责把复杂空间预测留给主网络，但也不能预先保证更优。SRC-0006 的可学习 correction 分配与 PADM 的 auxiliary clean-image 分支提供角色区分的参考；它们没有证明我们提出的少量参数接口。[SRC-0006, PDF pp. 3–5；EV-0005]

这项比较记录为 HYP-0002 的 unresolved design question。下一步需要解释 parameters 的物理含义、image 生成模块还读取什么，以及哪些空间关系由网络学习；本轮不编造具体光刻公式。

## 6. 三个 hypothesis 怎样一起回答项目问题

### H2：修正的帮助能否进入网络本身

同一 backbone 下，比较无回传、训练后 correction、corrected-target learning，以及条件允许时的 through-Projection training。后者让 loss 使用 projected output，并让梯度经过 Projection；[[pinet|ΠNet]] 是该路径的机制参考。[SRC-0012, PDF pp. 3–6]

两种更新并不等价：corrected targets 要求 raw prediction 接近被修正的目标；through-Projection 的 loss 对经 Projection 后的结果打分，raw prediction 怎样变化还需要单独观察。[[hard-conservation-correctors-can-hide-a-degrading-model|SRC-0007]] 给出特定 corrector 掩盖 raw-model 退化的例子，不能扩大为所有 Projection 都会失败。[SRC-0007, PDF pp. 4–8]

**支持观察：** 移除外部 corrector 后，新输入上的 reference accuracy 与目标物理行为仍改善。**否定观察：** 只有保留 corrector 才有效，或 raw/deployed prediction 的重要空间行为受损。PADM 的 representation transfer 单列比较，不以一个分支成功掩盖另一个失败。详细规则由 HYP-0002 管理。

### H1：diffusion 是否是值得使用的承载方式

用户仍优先关注 conditional diffusion＋U-Net。我们需要比较它与直接预测 U-Net，在相同高保真数据和可比预算下，是否改善 edge/frequency behavior、process response 与 reference accuracy。

先比较基础 predictor，再在各自固定 backbone 下比较 correction 回传，才能区分“逐步重建的帮助”和“物理回传的帮助”。

**支持观察：** 预测和光刻行为收益达到预定要求，完整采样成本可接受。**否定观察：** 只是视觉更精细、重复采样不稳定，或收益依赖不可接受的采样成本。H1 未获支持，仍可在直接预测网络上研究 H2。详细规则由 HYP-0001 管理。

### H3：这些物理资源能否减少高保真标签

物理可以通过不同资源帮助上面的学习过程：

- **提供训练答案：** 解析关系、近似 simulator 或 Teacher 生成 targets。[[deep-epidemiological-modeling-by-black-box-knowledge-distillation|SRC-0009]] 的 Teacher 数据与 EngGeneNet 的 ADI 数据提供先例；它们不是免费、无误差的真实答案。[SRC-0009, PDF pp. 3–6；SRC-0010, pp. 9–11]
- **提供无需逐样本 reference 的指导：** output residual、consistency 或已知 objective。[[dc3|DC3]] 和 ΠNet 提示已知条件可以参与无 optimal-label 的训练，但不证明任意光刻图像都能被这些条件唯一确定。[SRC-0013, PDF pp. 3–5；SRC-0012, pp. 3–6]
- **更充分利用已有样本：** diffusion noising 增加训练状态的变化；有效的查询选择决定哪些输入值得花钱标注。[[solver-integrated-adversarial-attacking-and-training-of-neural-operators|SRC-0008]] 提供查询路径参考，但新增调用与性能 trade-off 仍需计算。[SRC-0008, PDF pp. 5–7、24–25]

corrected-target learning 可能利用没有逐样本高保真答案的输入，前提是 correction 无需该答案也能计算，而且能提供有用信息；否则不能把它计作无标签收益。

**支持观察：** 用更少独立高保真标签达到同等预测标准。**否定观察：** 仅降低生成规则的 residual，独立 reference 上不改善，或标签优势来自未计入的高保真调用。noise versions 不算新独立样本；模拟、查询、训练和 inference 成本分开记录。详细规则由 HYP-0003 管理。

## 7. 我们真正要检验的贡献与下一步

候选贡献在于：**输出端物理 correction 能否成为有效的学习指导，使网络减少对昂贵标签与部署期外部 correction 的依赖，同时保留重要的高维空间预测能力？** diffusion 是否帮助实现它，是其中一个可单独检验的问题。把 U-Net、diffusion、physics 三个模块叠加起来，本身不构成已证实的贡献或领域创新。

其他来源帮助我们检查这条主线的前提。[[hard-constrained-deep-learning-for-climate-downscaling|SRC-0005]] 提醒约束可能与 reference 不匹配；[[adaptive-correction-for-ensuring-conservation-laws-in-neural-operators|SRC-0006]] 提醒满足同一关系也存在不同修改方式；[[physicscorrect|SRC-0011]] 提供 residual-based correction 与固定算子缓存的思路，并展示 residual 与 reference error 的区别。[SRC-0005, PDF pp. 27–28、32；SRC-0006, pp. 7–8；SRC-0011, pp. 3–7]

下一步先围绕用户已提出的少量 parameters 解释分工：它们决定整张 image，还是只指导完整预测图像的 correction；生成模块是否仍读取 mask。再区分物理作用于完整输出还是每步有明确物理含义的 clean estimate，随后定向寻找所需的光刻关系与数据。这里尚不需要全面补完光刻知识，也不因缺少全部公式而停止概念讨论。

进入实现前，才需要落实首个输出阶段、可计算关系、变量与单位、reference provenance、数据分组和质量/成本标准。保持 reference 评价独立于训练、target 生成筛选与模型选择；如果 reference 也来自同一 simulator，结论应限于该 simulator 的预测准确性。

完整来源比较保存在 [[three-topic-architecture-and-occupancy-map|architecture map]] 及 [[corrected-target-and-teacher-student-transfer|transfer 比较]]。[[deep-generative-prior-for-first-order-inverse-optimization|SRC-0001]] 保持 forward-only 的使用边界；本候选不转向 mask generation 或 ILT。

## 记录与来源状态

本页依据 Core 已有研究主线、BG-0002、HYP-0001–HYP-0003，以及 HYP-0002 保存的本次用户讨论澄清。canonical 路径只作为 frontmatter 中的非链接 traceability；本文不替代项目 Overview，也不改变 Locked Core。

PADM/NewPINNs 的 EV-0001–EV-0006 只验证原任务中的有界机制；其他相关论述维持 Source-reported 状态。组合方案、参数化影响与预期光刻收益是待检验的项目 inference，不是新增 verified Evidence。本次阅读反馈没有升级 Human Audit 或科学审核状态。

来源范围为已登记 SRC-0001–SRC-0013，第 14 篇待确认。保留中文解释与原 English technical terms；没有选定 Method、编造光刻公式、生成数据或启动实验。`exclude_from_synthesis: true` 保留待审查状态，允许阅读讨论，不允许把 draft 当作已验证结论上推。
