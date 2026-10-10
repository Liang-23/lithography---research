---
schema_version: "1.0"
title: "Forward Computational Lithography Simulation"
aliases:
  - "Forward Lithography Simulation"
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
knowledge_status: core-defined-research-task
canonical_refs:
  - "00_Project_Core/Project_Overview.md"
  - "00_Project_Core/Research_Requirement.md"
exclude_from_synthesis: false
---

# Forward Computational Lithography Simulation

## Core idea

Forward computational lithography predicts physical lithography outputs from a specified mask and process setting. In this project, the input boundary includes mask layout, optical conditions, and process parameters when available; the output boundary includes aerial image, resist image, and wafer image.

## Role in this project

The project uses a [[High-dimensional AI Surrogate]] to approximate this forward mapping with lower inference time and computational cost than high-fidelity physical simulation. The task is explicitly distinct from `ILT`, mask optimization, and mask generation.

The prediction must be evaluated not only through pixel similarity, but also through spatial frequency behavior, edge response, process variation response, and the relationship between input geometry and output behavior.

## Connections

The central methodological question is how [[Physics Knowledge Integration]] can improve this forward prediction task without unnecessarily restricting [[Neural Representation Learning]].

## Governance traceability

This note derives from the project definition and requirements in `00_Project_Core`. It is a human-readable scope note, not a claim-level Evidence record.
