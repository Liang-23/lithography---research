---
title: "Amortized Projection and Solver Distillation"
type: synthesis
lifecycle_status: draft
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-30
updated_at: 2026-09-01
review_status: pending-user-review
core_alignment: pass
knowledge_status: corpus-relative-synthesis
canonical_refs:
  - "02_Evidence/SRC-0003_NewPINNs.md"
  - "02_Evidence/EV-0001_NewPINNs_State_Dependent_Black_Box_Solver_Feedback.md"
  - "02_Evidence/EV-0002_NewPINNs_Direct_Neural_Field_Prediction.md"
  - "02_Evidence/EV-0003_NewPINNs_Solver_Inherited_Limitations.md"
  - "02_Evidence/SRC-0008_Solver_Integrated_Adversarial_Attacking_and_Training_of_Neural_Operators.md"
  - "02_Evidence/SRC-0009_Deep_Epidemiological_Modeling_by_Black_Box_Knowledge_Distillation.md"
  - "02_Evidence/SRC-0010_EngGeneNet_Transient_Heat_Conduction.md"
  - "02_Evidence/SRC-0011_PhysicsCorrect.md"
  - "02_Evidence/SRC-0012_Pinet.md"
  - "02_Evidence/SRC-0013_DC3.md"
source_ids: [SRC-0003, SRC-0008, SRC-0009, SRC-0010, SRC-0011, SRC-0012, SRC-0013]
evidence_ids: [EV-0001, EV-0002, EV-0003]
exclude_from_synthesis: true
---

# Amortized Projection and Solver Distillation

## What the corpus establishes

Solver work can be moved into training in several ways. [[newpinns|NewPINNs]], [[solver-integrated-adversarial-attacking-and-training-of-neural-operators|Solver-Integrated Adversarial Training]], [[deep-epidemiological-modeling-by-black-box-knowledge-distillation|Deep Epidemiological Modeling]], and [[enggenenet-transient-heat-conduction|EngGeneNet]] all produce a final neural path that omits their training oracle.

For NewPINNs, verified Evidence narrows that statement: solver output participates in the training loss, backpropagation does not traverse $S$, and the solver is absent from the reported forward evaluation path. The paper does not provide an inference-runtime benchmark or formal solver-removal ablation. [EV-0001, EV-0002]

However, “faster than a full solver” does not necessarily mean “solver/corrector removed”:

- [[pinet|$\Pi$net]] replaces a full optimizer with a backbone plus an explicit Douglas–Rachford projection loop at every inference;
- [[dc3|DC3]] always runs equality completion and iterative inequality correction;
- [[physicscorrect|PhysicsCorrect]] caches a Jacobian/pseudoinverse but still evaluates a PDE residual and applies correction at every rollout step.

## Three deployment states

| Deployment state | Meaning | Corpus examples |
|---|---|---|
| Oracle removed | Direct neural prediction requires no training solver/teacher | NewPINNs, Solver-Integrated Adversarial Training, Deep Epidemiological Modeling, EngGeneNet |
| Full solver replaced, correction retained | Structured numerical work remains in each inference | $\Pi$net, DC3, PhysicsCorrect |
| External projection plus second student | Corrected raw outputs train a final corrector-free surrogate | Not established in this corpus |

## Research implication

The literature-review target must distinguish cost amortization, algorithm unrolling, correction-layer acceleration, and complete dependency removal. The project needs the third state while also satisfying [[High-dimensional Safe Correction]]. This synthesis does not select an architecture or establish lithography validity.

`EV-0003` further prevents a cost-free interpretation: NewPINNs inherits solver stability requirements and computational cost during training and may require problem-specific stabilization.
