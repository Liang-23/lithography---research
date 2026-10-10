---
schema_version: "1.0"
title: "Amortized Projection and Solver Distillation"
aliases:
  - "Solver Distillation"
  - "Amortized Solver"
type: concept
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-30
updated_at: 2026-09-01
review_status: unreviewed
core_alignment: pass
knowledge_status: corpus-relative-mechanism-family
canonical_refs:
  - "02_Evidence/SRC-0003_NewPINNs.md"
  - "02_Evidence/EV-0001_NewPINNs_State_Dependent_Black_Box_Solver_Feedback.md"
  - "02_Evidence/EV-0002_NewPINNs_Direct_Neural_Field_Prediction.md"
  - "02_Evidence/EV-0003_NewPINNs_Solver_Inherited_Limitations.md"
  - "02_Evidence/SRC-0008_Solver_Integrated_Adversarial_Attacking_and_Training_of_Neural_Operators.md"
  - "02_Evidence/SRC-0009_Deep_Epidemiological_Modeling_by_Black_Box_Knowledge_Distillation.md"
  - "02_Evidence/SRC-0010_EngGeneNet_Transient_Heat_Conduction.md"
  - "02_Evidence/SRC-0012_Pinet.md"
source_ids: [SRC-0003, SRC-0008, SRC-0009, SRC-0010, SRC-0012]
evidence_ids: [EV-0001, EV-0002, EV-0003]
exclude_from_synthesis: false
---

# Amortized Projection and Solver Distillation

## Core idea

Amortization moves repeated numerical work into training so a learned model performs cheaper inference. The admitted corpus separates several mechanisms that should not be collapsed into one label:

1. a black-box teacher produces fixed targets and disappears at deployment, as in [[deep-epidemiological-modeling-by-black-box-knowledge-distillation|Deep Epidemiological Modeling]];
2. a solver produces state-dependent responses that enter the training loss while backpropagation does not traverse the solver mapping, as in [[newpinns|NewPINNs]];
3. perturbed field inputs are relabelled by a solver, as in [[solver-integrated-adversarial-attacking-and-training-of-neural-operators|Solver-Integrated Adversarial Training]];
4. an offline solver generates spatial training data, as in [[enggenenet-transient-heat-conduction|EngGeneNet]];
5. a learned backbone reduces optimizer work but a projection loop remains at inference, as in [[pinet|$\Pi$net]].

## Project boundary

Only the first four provide solver-free inference relative to their training oracle, and none demonstrates the exact project chain

$$
\text{raw lithography prediction}
\rightarrow
\text{physical correction}
\rightarrow
\text{corrected-target transfer}
\rightarrow
\text{standalone student}.
$$

The distinction between “solver calls reduced” and “solver/corrector removed” must remain explicit. This mechanism family connects to [[Projection-based Knowledge Distillation]] and [[High-dimensional Safe Correction]], but it is not a selected Method.

For NewPINNs specifically, verified `EV-0001`–`EV-0003` establish the bounded mechanism, the reported direct neural evaluation path, and the inherited solver limitations. They do not establish runtime acceleration, exact feasibility, inference-time safety, or lithography validity. The other corpus examples retain their independently recorded Evidence states.
