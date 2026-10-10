---
schema_version: "1.0"
title: "Physics-defined Solution Space Projection"
aliases:
  - "Physics-defined Projection"
type: concept
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-29
review_status: unreviewed
core_alignment: pass
knowledge_status: candidate-family-in-core
canonical_refs:
  - "00_Project_Core/Project_Overview.md"
  - "00_Project_Core/Research_Requirement.md"
  - "01_Background/BG-0001_SRC-0002_Output_Projection_Project_Aware_Comparison.md"
source_ids:
  - SRC-0002
exclude_from_synthesis: false
---

# Physics-defined Solution Space Projection

## Core idea

Physics-defined Solution Space Projection is a candidate mechanism that maps a surrogate output toward a physically meaningful valid solution space. In the proposed flow, it would implement part of [[Output-level Physical Correction]].

## Role in the candidate flow

The projected or corrected solution may be used by [[Projection-based Knowledge Distillation]] so that physical guidance can influence the learned [[High-dimensional AI Surrogate]] rather than remain a required external inference module.

## Required specification

Before this idea can become an implementable Physics Constraint, the project must define the exact relationship or operator, variables, units, tensor shapes, coordinate system, validity regime, differentiability behavior, computational cost, failure modes, and rejection experiment.

## Lesson from SRC-0002

The paper defines the feasible set implicitly as

$$
\mathcal{M}_x=\left\{p\mid g(x,p)=0\right\},
$$

and selects the nearest feasible point under $\lVert p-f(x;\Theta)\rVert_W^2$. Projection is computationally manageable there because $g$ is an explicit algebraic residual in only $4$ or $17$ output variables. The paper does not establish uniqueness, tests only $W=I$, and warns of ambiguity when a raw prediction lies far from the manifold.

For lithography, the corresponding feasible set, output metric, validity regime, and scalable solver remain undefined. [[output-projection-project-positioning|Output Projection and Project Positioning]] records why transfer to aerial, resist, or wafer images is an inference rather than demonstrated evidence.

## Status

This note records a candidate family from the Core. It does not assert that a suitable solution space exists, that a projection is unique, or that the mechanism improves performance.
