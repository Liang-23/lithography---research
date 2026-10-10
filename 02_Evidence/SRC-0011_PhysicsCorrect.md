---
schema_version: "1.0"
id: SRC-0011
type: source-record
title: "PhysicsCorrect: A Training-Free Approach for Stable Neural PDE Simulations"
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
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 2 item 9"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# PhysicsCorrect: A Training-Free Approach for Stable Neural PDE Simulations

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0011_PhysicsCorrect.pdf`
- Source type: PDF; peer-reviewed conference paper
- Authors: Xinquan Huang, Paris Perdikaris
- Publication/version date: *Proceedings of the AAAI Conference on Artificial Intelligence* 40(26):22057–22065; 2026
- DOI: `10.1609/aaai.v40i26.39360`
- Imported/registered date: 2026-08-30
- Original location: `https://ojs.aaai.org/index.php/AAAI/article/view/39360/43321`
- Language: English
- License/access restriction: Official AAAI PDF is lawfully open to read; copyright remains with AAAI/authors and no permissive reuse license was identified in the artifact.
- Version relationship: The approved and admitted artifact is the AAAI 2026 published version. The longer arXiv `2507.02227v2` is an extended version and was not substituted.

## Integrity

- File size: 2,662,384 bytes
- PDF page count: 9
- Hash algorithm: SHA-256
- Content hash: `BB52DA6ED7BB28B6700DF1B5CF62CA5FD1A521087D0C6091ED900C6460AFBBA8`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate high-dimensional post-prediction correction evidence for stabilizing neural PDE rollouts through cached residual-Jacobian inverse updates.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow, bounded to the published AAAI artifact.
- Prohibited use: Treating admission as verified Evidence; silently importing claims unique to the extended arXiv version; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: Non-blocking version boundary: the approved published paper is shorter than the related extended arXiv version.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete published-paper review plus visual inspection of Eqs. (1)–(6), Figures 1–8, setups, cost statements, and limitations
- Notes: Integrity and published-version identity are source-checked. Scientific claims and reported results remain source-reported and are not independently verified Evidence.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF p. 1 is printed p. 22057; the related extended arXiv version was not used to fill omissions in this approved published artifact.

### Predictor-corrector mechanism and outputs

- At every autoregressive step, a pretrained predictor gives $\widehat u_{t+1}=\phi_\theta(u_t)$. The method seeks an additive $u^c_{t+1}$ that reduces the governing discretized PDE residual. [PDF pp. 1–3, Sections 1–3.1, Eqs. (1)–(4)]
- First-order linearization gives

$$
A u^c_{t+1}=b,
\qquad
A=\frac{\partial L_{\mathrm{PDE}}}{\partial\widehat u_{t+1}},
\qquad
b=-L_{\mathrm{PDE}}(u_t,\widehat u_{t+1}),
$$

followed by least squares and $\widetilde u_{t+1}=\widehat u_{t+1}+u^c_{t+1}$. [PDF p. 3 / printed p. 22059, Eqs. (5)–(6)]
- With a residual linear in the next state, the Jacobian and Moore–Penrose pseudoinverse can be cached offline; each correction becomes matrix multiplication. This is a single linearized residual correction, not a proof of exact or unique projection onto the full nonlinear PDE solution set. [PDF p. 4 / 22060]
- Demonstrated fields include $64\times64$ 2D Navier–Stokes vorticity, $128\times128$ 2D wave fields, and a 512-point 1D Kuramoto–Sivashinsky state, using FNO, U-Net, and Vision Transformer predictors. [PDF pp. 5–6 / 22061–22062, Sections 4.1–4.3]

### Training and inference boundary

- Correction is training-free: no corrected target, distillation, retraining, or gradient transfer updates the pretrained surrogate. [PDF pp. 1–3]
- PDE residual evaluation and cached pseudoinverse multiplication are required at every inference step, and the corrected state is recursively fed back. The external corrector is therefore not removed. [PDF p. 3 / 22059]
- No gate, trust region, correction-norm cap, raw-better-than-corrected selector, or fallback numerical solver is implemented. Small correction, adequate raw prediction, and a cacheable residual discretization are methodological assumptions.

### Major reported results and failure evidence

- For one-step Navier–Stokes FNO prediction, relative $L_2$ error is reported to decrease from $3.3\times10^{-5}$ to $5.5\times10^{-6}$. [PDF p. 5 / 22061, Figure 5]
- An idealized residual-alignment test reaches $6.1\times10^{-7}$, demonstrating that a zero-discretization-residual target differs from the numerical reference's residual. [PDF pp. 5–6 / 22061–22062, Figure 6 discussion]
- Figure 4 reports final-state improvements across all three PDEs and architectures; exact bar values are not tabulated in the approved artifact. [PDF p. 5 / 22061, Figure 4]
- The offline Navier–Stokes warm-up is $8.74\,\mathrm{s}$. A 200-step corrected rollout is reported as $0.90\,\mathrm{s}$ versus baseline $0.69\,\mathrm{s}$; pseudoinverse caching reduces the standard correction cost by about $163\times$. [PDF p. 4 / 22060, Figure 3]
- First-order wave residual prediction “consistently failed,” so the authors changed the network target to a second-order temporal quantity. This is a formulation failure, not a demonstration that the selected final corrector worsens prediction. [PDF p. 6 / 22062, Section 4.2]

### Limitations and safe boundary

- Time and memory scale quadratically with grid resolution and challenge fully 3D use. Discretization error creates a gap between the zero-residual target and the numerical reference. Linearization may break in extreme chaos. [PDF p. 7 / 22063, Figure 8 and Limitations]
- Constant-Jacobian caching depends on a suitable semi-implicit residual; a fully implicit nonlinear residual would require recomputing the Jacobian or pseudoinverse. [PDF pp. 4 and 6]
- The abstract says inference overhead is under $5\%$, while the main-text $0.90/0.69\,\mathrm{s}$ comparison is about $30\%$ higher total time. The approved artifact does not reconcile this cost discrepancy.
- The published paper points to appendix material not present in its nine pages. The unapproved extended arXiv version was not imported to resolve those references.
- **Bounded relevance:** strong moderate-resolution spatial-field evidence for an accelerated external residual corrector. It does not establish corrected-target transfer, student-only inference, exact nonlinear projection, a lithography residual, very-large/3D scaling, or universal safe correction.

## 用户阅读判断与保留思路 — 2026-09-13

本节为用户要求保存的学习记录，由 Agent 整理，`content_origin: ai-assisted`。用户认为，预测后再进行物理 correction 的整体 framework 已较熟悉，对当前学习带来的新增框架启发有限；这不是对论文整体创新性的文献结论。

保留的具体思路是：在特定的离散方程和固定配置下，residual 到 correction 的线性转换算子可能保持不变。若已确认其不依赖变化的状态，并且相关参数、网格和时间步长等配置保持适用，就可以提前计算并缓存 Jacobian 的 pseudoinverse。后续每次预测只需计算新的 residual，再用缓存算子计算新的 correction，从而减少重复计算。[SRC-0011, PDF p. 3, Eq. (6); PDF p. 4, Efficient Implementation via Jacobian Caching]

缓存的是转换算子，不是 residual 或 correction；两者仍随预测变化。这里指特定离散形式，而非假定存在“理想方程”即可缓存。能否复用必须由 residual 的表达式及其系数依赖判断；若算子随状态或配置变化，不能默认沿用原缓存。

本节不选择光刻 correction 方法，不认定低 residual 必然带来更高预测准确率，也不改变 Source claims 的未验证状态或 Human Audit 状态。
