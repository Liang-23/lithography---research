---
title: "Deep Sets"
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
canonical_refs: ["02_Evidence/SRC-0018_Deep_Sets.md", "01_Background/BG-0005_Deep_Sets.md"]
source_ids: [SRC-0018]
evidence_ids: []
method_ids: [METHOD-0003]
---

# Deep Sets

**Official page:** https://papers.neurips.cc/paper_files/paper/2017/hash/f22e4747da1aa27e363d86d40ff442fe-Abstract.html  
**Official PDF:** https://papers.neurips.cc/paper_files/paper/2017/file/f22e4747da1aa27e363d86d40ff442fe-Paper.pdf  
**Role:** Set Aggregation Theory  
**Archive status:** Source URL and canonical notes admitted; PDF bytes have NOT been deposited.

## Source-relative overview (abstract-level, NOT Human-audited)
The paper studies permutation-invariant operations on variable-size sets.

## Relevance to current FD-GNN design (interpretation)
与一个 Frequency Node 相连的 Pairs 构成一个邻居集合；候选聚合应当对任意输入顺序保持一致。

## Limitations
Permutation invariance alone does not ensure pair-level information is recoverable. No project performance claim is verified. Complete source-reading, licensing and PDF-integrity checks remain open.

## Research context
For the distinct user-reviewed architecture, see [[fd-gnn-effective-mode-feature-aggregation|FD-GNN Effective Mode Feature Aggregation]].
