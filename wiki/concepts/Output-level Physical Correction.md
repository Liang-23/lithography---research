---
schema_version: "1.0"
title: "Output-level Physical Correction"
aliases:
  - "Output-level Correction"
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

# Output-level Physical Correction

## Core idea

Output-level Physical Correction introduces physical knowledge after a neural prediction instead of continuously placing the correction inside the optimization objective. It is one candidate family for [[Physics Knowledge Integration]].

## Candidate mechanism

The correction could use [[Physics-defined Solution Space Projection]] or another physically meaningful operator. A corrected solution could then provide a target or learning signal for [[Projection-based Knowledge Distillation]] back into the [[High-dimensional AI Surrogate]].

## Inference boundary

The project requires the final surrogate to operate end to end without a required external post-processing module during inference. Any concrete correction design must therefore specify whether correction is training-only, distilled into the model, or otherwise compatible with that boundary.

## Source-bounded comparison

`SRC-0002` directly demonstrates post-training output correction through an external constrained optimizer. This means that generic “predict first, then project onto $g(x,p)=0$” is already occupied relative to that Source. The paper leaves hidden representations untouched structurally, but it does not study representation quality or prove that this freedom improves learning.

The demonstrated corrector remains required for every corrected prediction, which conflicts with this project's final inference boundary. The full human-readable comparison is [[output-projection-project-positioning|Output Projection and Project Positioning]]. These conclusions remain Source-relative and do not select or reject a project Method.

## Status and open questions

This is a Core-recorded candidate, not a selected Method or supported Physics Constraint. No exact operator, variables, units, tensor shapes, validity regime, or rejection experiment has been defined.
