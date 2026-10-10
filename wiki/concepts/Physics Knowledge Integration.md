---
schema_version: "1.0"
title: "Physics Knowledge Integration"
aliases:
  - "Physics-guided Surrogate Learning"
type: concept
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
core_alignment: pass
knowledge_status: core-research-question
canonical_refs:
  - "00_Project_Core/Project_Overview.md"
  - "00_Project_Core/Research_Requirement.md"
exclude_from_synthesis: false
---

# Physics Knowledge Integration

## Core idea

Physics Knowledge Integration is the project's central research question: how can physical knowledge improve a [[High-dimensional AI Surrogate]] without unnecessarily limiting [[Neural Representation Learning]]?

## Design tension

The Core frames a possible conflict between continuously enforcing physical constraints during optimization and retaining flexible high-dimensional representation learning. That framing is a project hypothesis, not verified Evidence.

## Candidate direction

The current candidate family places physical knowledge after neural prediction through [[Output-level Physical Correction]], potentially using [[Physics-defined Solution Space Projection]]. Corrected solutions may then be transferred back through [[Projection-based Knowledge Distillation]].

The project has not yet defined the exact physical relationship, correction operator, validity regime, data/simulator contract, or experimental threshold needed to test this family.

## Governance traceability

This note summarizes the Core research question and candidate direction. Link density in Obsidian cannot make the candidate scientifically supported.
