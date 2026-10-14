---
schema_version: "1.0"
id: BG-0003
type: background
title: "Message Passing Foundations: Neural Message Passing for Quantum Chemistry"
lifecycle_status: draft
authority_class: working
authority_scope: source-relative-background-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-14
updated_at: 2026-10-14
owner: project-lead
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
source_ids: [SRC-0016]
evidence_ids: []
exclude_from_synthesis: false
---

# Message Passing Foundations

**Paper:** Neural Message Passing for Quantum Chemistry (ICML 2017 / PMLR 70:1263–1272)  
**Registered source:** `SRC-0016`  
**Original:** https://proceedings.mlr.press/v70/gilmer17a.html  
**PDF:** https://proceedings.mlr.press/v70/gilmer17a/gilmer17a.pdf

## Source-reported mechanism (metadata/abstract-level reading only)
The paper introduces a common Message Passing Neural Network framework for graph-structured molecular property prediction.

## 对当前 FD-GNN 的潜在用途（研究者解释，不是验证结果）
提供 message / aggregation / node-update 的概念基础；应用于频率差图属于我们的架构类比，而非论文自身的光刻结论。

## Boundaries
Molecular-graph results do not establish computational lithography performance.
尚未完成论文全文 reconstruction / Human Audit；不能将其作为已验证 Evidence，也不能直接认定我们的 Aggregation 候选有效。

## Next reading
对照原文核实理论假设、公式适用边界、实验对象及是否要求额外 edge attributes，然后再写 Project-aware Comparison。
