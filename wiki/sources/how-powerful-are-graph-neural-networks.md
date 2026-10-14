---
title: "How Powerful are Graph Neural Networks?"
aliases: []
type: source
lifecycle_status: draft
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-14
updated_at: 2026-10-14
review_status: unreviewed
core_alignment: pass
canonical_refs: ["02_Evidence/SRC-0017_How_Powerful_are_Graph_Neural_Networks.md", "01_Background/BG-0004_How_Powerful_are_Graph_Neural_Networks.md"]
source_ids: [SRC-0017]
evidence_ids: []
method_ids: [METHOD-0003]
---

# How Powerful are Graph Neural Networks?

**Official page:** https://openreview.net/forum?id=ryGs6iA5Km  
**Official PDF:** https://openreview.net/pdf?id=ryGs6iA5Km  
**Role:** Aggregation Expressivity  
**Archive status:** Source URL and canonical notes admitted; PDF bytes have NOT been deposited.

## Source-relative overview (abstract-level, NOT Human-audited)
The paper examines how neighborhood aggregation constrains what GNN architectures can distinguish.

## Relevance to current FD-GNN design (interpretation)
Aggregation 后是否丢失原本来自不同 Frequency Difference 的 Pair 信息，需要单独验证；不能把 SUM/MEAN 的选择视为纯实现细节。

## Limitations
Expressivity theory is not a lithography accuracy result. No project performance claim is verified. Complete source-reading, licensing and PDF-integrity checks remain open.

## Research context
For the distinct user-reviewed architecture, see [[fd-gnn-effective-mode-feature-aggregation|FD-GNN Effective Mode Feature Aggregation]].
