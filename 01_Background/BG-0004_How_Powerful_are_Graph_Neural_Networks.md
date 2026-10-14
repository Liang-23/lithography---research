---
schema_version: "1.0"
id: BG-0004
type: background
title: "Aggregation Expressivity: How Powerful are Graph Neural Networks?"
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
source_ids: [SRC-0017]
evidence_ids: []
exclude_from_synthesis: false
---

# Aggregation Expressivity

**Paper:** How Powerful are Graph Neural Networks? (ICLR 2019)  
**Registered source:** `SRC-0017`  
**Original:** https://openreview.net/forum?id=ryGs6iA5Km  
**PDF:** https://openreview.net/pdf?id=ryGs6iA5Km

## Source-reported mechanism (metadata/abstract-level reading only)
The paper analyzes the discriminative/representational power and limitations of neighborhood-aggregation graph neural networks.

## 对当前 FD-GNN 的潜在用途（研究者解释，不是验证结果）
提醒我们：过早把 Pair 信息压缩为单个数可能丢失可区分性；须做聚合消融试验。

## Boundaries
Graph discrimination theory is not a direct proof that any aggregation improves mask-to-aerial prediction.
尚未完成论文全文 reconstruction / Human Audit；不能将其作为已验证 Evidence，也不能直接认定我们的 Aggregation 候选有效。

## Next reading
对照原文核实理论假设、公式适用边界、实验对象及是否要求额外 edge attributes，然后再写 Project-aware Comparison。
