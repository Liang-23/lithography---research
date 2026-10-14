---
schema_version: "1.0"
id: BG-0005
type: background
title: "Set Aggregation Theory: Deep Sets"
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
source_ids: [SRC-0018]
evidence_ids: []
exclude_from_synthesis: false
---

# Set Aggregation Theory

**Paper:** Deep Sets (NeurIPS 2017 / Advances in Neural Information Processing Systems 30)  
**Registered source:** `SRC-0018`  
**Original:** https://papers.neurips.cc/paper_files/paper/2017/hash/f22e4747da1aa27e363d86d40ff442fe-Abstract.html  
**PDF:** https://papers.neurips.cc/paper_files/paper/2017/file/f22e4747da1aa27e363d86d40ff442fe-Paper.pdf

## Source-reported mechanism (metadata/abstract-level reading only)
The paper characterizes permutation-invariant functions over sets and motivates learnable set-processing architectures.

## 对当前 FD-GNN 的潜在用途（研究者解释，不是验证结果）
Frequency Node 所关联的 Pair 集合没有自然顺序；可借鉴集合不变性组织邻居信息。

## Boundaries
A set-aggregation representation does not by itself preserve every individual pair or phase relationship.
尚未完成论文全文 reconstruction / Human Audit；不能将其作为已验证 Evidence，也不能直接认定我们的 Aggregation 候选有效。

## Next reading
对照原文核实理论假设、公式适用边界、实验对象及是否要求额外 edge attributes，然后再写 Project-aware Comparison。
