---
title: "2-3nm litho Overview"
type: synthesis
tags: []
sources: []
authority_class: derived
authority_scope: human-readable-wiki-only
canonical_refs:
  - "00_Project_Core/Project_Overview.md"
  - "00_Project_Core/Research_Requirement.md"
last_updated: 2026-08-27
---
.
# 2-3nm litho Overview

## Research task and boundary

The project studies [[Forward Computational Lithography Simulation]] through an end-to-end [[High-dimensional AI Surrogate]]. The defined inputs are mask layout, optical conditions, and process parameters when available. The required outputs are aerial image, resist image, and wafer image.

The scope excludes `ILT`, mask optimization, mask generation, and gradient trust certification. The Wiki is a derived explanation of this Core-defined boundary; it is not scientific Evidence.

## Main research problem

The central question is how [[Physics Knowledge Integration]] can improve lithography prediction while preserving [[Neural Representation Learning]]. The evaluation boundary includes pixel-level performance, lithography behavior, data efficiency under limited high-fidelity data, and computational efficiency.

## Candidate integration flow

The Core records the following direction as a research hypothesis and candidate family, not as a selected or verified Method:

```text
high-dimensional neural representation learning
    -> neural prediction
    -> output-level physical correction
    -> transfer of corrected knowledge back into the surrogate
```

Within that family, [[Output-level Physical Correction]] may use [[Physics-defined Solution Space Projection]]. The corrected solution may then inform [[Projection-based Knowledge Distillation]]. These mechanisms remain unselected until the required Evidence, Physics Constraint, Method, Experiment, and ADR gates are satisfied.

## System flow

1. **Input:** mask layout, optical conditions, and available process parameters.
2. **Operation:** the [[High-dimensional AI Surrogate]] learns the high-dimensional forward transformation.
3. **Output:** aerial image, resist image, and wafer image predictions.
4. **Candidate training-time guidance:** physically meaningful correction and knowledge transfer may improve learned prediction behavior.
5. **Inference boundary:** the final surrogate must not require an external filtering or post-processing module.

## Unresolved questions

- The exact physical relationship, variables, units, tensor shapes, and validity regime are not yet defined.
- No `PC-####`, `HYP-####`, `METHOD-####`, registered Data/Simulator contract, or formal Experiment has been selected.
- The training-time versus inference-time role of any correction remains to be specified.
- Success thresholds and the exact limited-data/OOD protocol remain unresolved.

## Governance traceability

This Overview derives only from `00_Project_Core/Project_Overview.md` and `00_Project_Core/Research_Requirement.md`. `SRC-0001` has been admitted and has a separate derived source note, but it is not incorporated into this canonical synthesis because its primary inverse-lithography task is outside the project scope and its claims remain unverified. No claim here is promoted to verified Evidence by source admission or link connectivity.
