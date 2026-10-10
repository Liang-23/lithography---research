---
schema_version: "1.0"
id: SRC-0010
type: source-record
title: "Transient heat conduction modelling for real-time operation and control of steel-making reheating furnaces - a physics-informed knowledge distillation-assisted EngGeneNet approach"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-and-source-check
created_by: ai
content_origin: external-source
created_at: 2026-08-30
updated_at: 2026-09-13
owner: project-lead
review_status: source-checked
tier2_review_status: agent-complete
human_audit_status: not-started
reviewed_by: AI Agent
approved_by: project-lead
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 2 item 8"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Transient heat conduction modelling for real-time operation and control of steel-making reheating furnaces - a physics-informed knowledge distillation-assisted EngGeneNet approach

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0010_EngGeneNet_Transient_Heat_Conduction.pdf`
- Source type: PDF; author accepted manuscript
- Authors: Xiaofei Han, Kang Li, Chuan Wang, Jiayang Zhang, Yukun Hu
- Publication/version date: Accepted manuscript for *Control Engineering Practice* 164, Article 106472 (2025)
- DOI: `10.1016/j.conengprac.2025.106472`
- Imported/registered date: 2026-08-30
- Original location: `https://eprints.whiterose.ac.uk/id/eprint/236819/`
- Language: English
- License/access restriction: Creative Commons Attribution 4.0 International (`CC BY 4.0`) through White Rose Research Online
- Version relationship: The approved and admitted artifact is the author accepted manuscript. The published version of record exists under the DOI and was not silently substituted.

## Integrity

- File size: 2,595,472 bytes
- PDF page count: 17
- Hash algorithm: SHA-256
- Content hash: `F0DC435CE17F2E2D6D2A4AB782CD8269AF8C3E7D81E9CF844F8FED47A2ACA455`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate physics-informed teacher-student evidence for distilling a high-fidelity transient heat-conduction model into a real-time predictive network.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow, bounded to the accepted manuscript.
- Prohibited use: Treating admission as verified Evidence; substituting the version of record without approval; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: Non-blocking artifact relationship: accepted manuscript rather than the paywalled version of record. The repository cover states the DOI, version, and license.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of the repository cover and pivotal method, result, and limitation pages
- Notes: The title uses minor hyphenation differences across records; the DOI, authors, accepted-version statement, and repository record identify the same approved artifact.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. `PDF p. 1` is the White Rose cover; an article-page locator is one less than its local PDF page.

### Problem, physics, and output

- The task predicts the next two-dimensional cross-sectional temperature field of a steel bloom for real-time reheating-furnace operation. Input is $T^t(x,y)$ and output is $\widetilde{T}^{t+1}(x,y)$. [PDF p. 2, Abstract; PDF pp. 4–5, Sections 1–3; PDF p. 9, Figure 2]
- The source formulates a two-dimensional transient Fourier heat equation with temperature-dependent $k(T)$ and $C_p(T)$ plus radiative and convective boundary conditions. Crank–Nicolson finite differences define an interior residual used as a physics-informed loss. [PDF pp. 5–7, Eqs. (1)–(3) and (9)–(21), Sections 3.1–3.2]
- A boundary residual $Y_B$ is added through a binary mask. Although the paper calls this a “hard-constrained boundary condition,” the displayed implementation is a loss term rather than an architectural projection proving exact satisfaction. [PDF p. 8, Eqs. (22)–(24), Section 3.3]
- The `Eng-Gene` module transforms intermediate features using $w/Fo=w\rho C_p(T)d^2/[k(T)\Delta t]$ and is embedded at multiple U-Net levels. [PDF pp. 8–9, Eqs. (25)–(26), Section 3.4, Figure 7]
- Nominal discretization gives $m=n=16$, but boundary formulas index $0$ through $m$ and $n$; the literal stored shape may therefore be $17\times17$. The paper does not print an unambiguous tensor shape. [PDF p. 5, Section 3.1; PDF p. 10, Table 2]

### Teacher, training, and inference

- ADI is the offline numerical data generator. The paper reports $12{,}000$ OC1 fields, $6{,}000$ each for OC2 and OC4, and $5{,}000$ for OC3, split $8{:}1{:}1$. [PDF pp. 9–11, Section 4.2, Eqs. (27)–(28), Section 4.3]
- No gradient is propagated through ADI. Physics residuals and `Eng-Gene` are inside the neural training graph. Transfer freezes the contraction path and fine-tunes the expansion path while updating material parameters. [PDF p. 9, Sections 3.4–3.5; PDF pp. 11–12, Tables 4–5]
- ADI is absent at deployment, so inference is solver-free relative to that numerical teacher. The embedded `Eng-Gene` transformation remains part of the student.
- The source calls the method knowledge distillation, but it does not define a neural teacher, logits/features transfer, a distinct imitation loss, or a raw-prediction $\rightarrow$ ADI-correction $\rightarrow$ corrected-target loop. The displayed objective is a physics-residual objective. This is solver-generated training-data transfer, not demonstrated corrected-output distillation.
- No inference-time projector, accept/reject gate, fallback solver, correction-magnitude monitor, or damaging-correction analysis is reported.

### Major reported results

- PI-EngGeneUNet reports test MAE/RMSE/MAE-MaxE of $0.029/0.048/0.313$, versus PI-UNet $0.515/0.538/0.822$. [PDF p. 11, Table 4 and Figure 9]
- Replacing `Eng-Gene` with a same-complexity $1\times1$ convolution reports $0.106/0.148/0.690$; the 50-epoch `Eng-Gene` result is $0.029/0.048/0.313$. [PDF p. 12, Table 5]
- Under OC2–OC4 transfer, Table 8 reports MAE and RMSE reductions over PI-UNet ranging from $92\%$ to $97\%$ and $90\%$ to $99\%$, respectively, within the proposed physics-informed setup. [PDF p. 15, Table 8 and Figure 13]
- Per-frame timing is reported as $0.1608\,\mathrm{s}$ for ADI and $0.0059\,\mathrm{s}$ for PI-EngGeneUNet. [PDF pp. 15–16, Section 5.5, Figure 15]

### Limitations and safe boundary

- The physical model assumes negligible longitudinal $z$-direction temperature gradient and reduces the problem to two dimensions. Validation uses a pilot-scale walking-beam furnace, two bloom batches, and four constructed operating conditions. [PDF p. 5, Section 2; PDF pp. 10–11, Section 4]
- The paper does not provide exact residual evidence for the claimed hard boundary satisfaction, a controlled hidden-representation-freedom comparison, uncertainty or broad OOD guarantees, multi-solution analysis, or very-large image-tensor evidence.
- **Bounded relevance:** supporting precedent for solver-generated spatial training data followed by solver-free inference. It is only partial overlap with the desired external correction $\rightarrow$ corrected-target transfer $\rightarrow$ standalone student chain.

## 用户阅读启发 — 2026-09-13

- **记录性质：** 用户要求保存的阅读启发，由 Agent 整理；`content_origin: ai-assisted`，本节 `lifecycle_status: draft`、`authority_class: working`。归类为有来源依据的学习记录及尚未解决的项目迁移问题，不是已定义的 Hypothesis 或已选择的 Method。保存授权来自本次用户请求，不代表完成 Human Audit 或验证科学结论。
- **论文依据：** EngGeneNet 在热传导领域将已知材料性质相关的变换做成 Eng-Gene，嵌入网络内部计算，并在推理时继续保留。ADI 用于提前生成温度分布数据，部署网络不再运行 ADI；移除这一数值数据生成器不等于移除网络内的物理计算。[SRC-0010, PDF pp. 8–9, Section 3.4, Eqs. (25)–(26), Figure 7; PDF pp. 9–11, Section 4.2]
- **保留的启发：** 端到端 AI surrogate 可以包含明确的物理计算。对光刻输入到物理输出的映射，如果其中一部分物理依赖关系已经明确、能够可靠计算，而且计算成本较低，可以考虑将其加入网络内部，让神经网络在利用这些已知关系的基础上继续学习复杂的高维映射。这是用户从热传导实例获得的条件性启发，不是论文已证明的光刻结论；这里的“映射”不特指可行集合上的 projection。
- **适用条件与未决问题：** 光刻中具体采用什么关系、适用条件是否满足、额外计算是否足够便宜、是否改善预测和保留表示灵活性，均尚未确认。EngGeneNet 的热传导公式不能直接作为本项目的光刻关系。
- **不支持继续采用的情形：** 若候选关系在目标工况下不成立、额外计算不符合效率要求，或实验显示其损害预测与表示能力，则不能据此主张采用。这里仅记录判断边界，不新增实验方案或数值阈值。
- **项目边界：** 与 Core 的端到端 forward surrogate、物理知识融合、表示能力和效率要求相关；不改变 Core、研究主线、Evidence 状态或任何方法选择。
