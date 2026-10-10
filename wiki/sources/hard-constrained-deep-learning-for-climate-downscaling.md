---
title: "Hard-Constrained Deep Learning for Climate Downscaling"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-30
updated_at: 2026-09-12
review_status: source-checked
human_audit_status: not-started
knowledge_status: source-reported-claims-unverified
canonical_refs:
  - "02_Evidence/SRC-0005_Hard_Constrained_Deep_Learning_for_Climate_Downscaling.md"
source_ids: [SRC-0005]
source_file: "raw/SRC-0005_Hard_Constrained_Climate_Downscaling.pdf"
exclude_from_synthesis: false
---

# Hard-Constrained Deep Learning for Climate Downscaling

## 本次阅读保留的一条认识（2026-09-12）

**约束满足得更严格，不保证预测更准确；尤其当施加的约束与真实数据不一致时，强制满足约束可能让预测偏离参考结果。**

这是用户在本次中文阅读讨论中选择保留的学习收获。当前暂停该文的进一步深入阅读，保留其作为背景参考；这不表示方法无效，也不表示已经完成整篇 Human Audit。

具体依据是论文的 NorESM 实验：

| 方法 | 相对精细参考图的 RMSE | Constr. viol. |
|---|---|---|
| CNN，无约束 | $2.348$ | $1.034$ |
| CNN，AddCL | $2.885$ | $0.000$ |

论文 Table 14 报告上述结果为三次运行的平均值。约束指标改善，但相对参考图的 RMSE 增大；$0.000$ 是表格的报告精度，不单凭这个显示值推断无限精度的数值零。[SRC-0005，PDF p. 32，Table 14]

Appendix F 同时指出，真实粗图与精细图降采样结果之间本来就有 RMSE 为 $2.48$ 的不一致。作者认为这可能解释强约束模型的精度下降；这里区分表格中的观测与作者对原因的解释，不把它写成已经隔离所有因素的因果证明。[SRC-0005，PDF pp. 27–28，Appendix F；p. 22，§7]

今后看物理修正方法时，要分别问：**它更符合所规定的关系了吗？它更接近参考结果了吗？该关系适用于当前数据吗？** 这是 [[High-dimensional Safe Correction]] 中已有区别的具体阅读实例，不意味着物理约束或 projection 普遍有害，也不建立任何光刻约束。

状态：本条已回查本地原文，仍属于论文报告支持的阅读收获；没有新增或提升为 verified Evidence。

## Human-readable summary

This paper appends differentiable terminal layers so the mean of each high-resolution patch equals its corresponding low-resolution value, optionally with nonnegativity. It evaluates real spatial outputs up to $(3,512,512)$ and keeps the correction layer during both training and inference. [SRC-0005, pp. 5–10]

Its most important lesson for [[High-dimensional Safe Correction]] is negative: when independent NorESM low- and high-resolution simulations strongly violate the assumed relation, hard layers force reported violation to zero but worsen RMSE from $2.348$ to roughly $2.884$–$2.888$. [SRC-0005, pp. 27–32]

## What the Source does and does not show

- It directly shows that a mismatched constraint can improve feasibility while harming reference accuracy.
- It compares several spatial architectures, but does not isolate hidden-representation freedom.
- It does not create corrected targets, remove the correction layer, or establish a lithography constraint.
- No gate, correction bound, runtime analysis, or edge/frequency preservation guarantee is provided.

## Governance traceability

Canonical Source: `SRC-0005`, stored at `02_Evidence/SRC-0005_Hard_Constrained_Deep_Learning_for_Climate_Downscaling.md`. Claims remain unverified.
