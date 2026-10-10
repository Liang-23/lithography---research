---
title: "NewPINNs: Physics-Informing Neural Networks Using Conventional Solvers for Partial Differential Equations"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-30
updated_at: 2026-09-01
review_status: reviewed
human_audit_status: completed
knowledge_status: pivotal-claims-verified-with-boundaries
canonical_refs:
  - "02_Evidence/SRC-0003_NewPINNs.md"
  - "02_Evidence/EV-0001_NewPINNs_State_Dependent_Black_Box_Solver_Feedback.md"
  - "02_Evidence/EV-0002_NewPINNs_Direct_Neural_Field_Prediction.md"
  - "02_Evidence/EV-0003_NewPINNs_Solver_Inherited_Limitations.md"
source_ids: [SRC-0003]
evidence_ids: [EV-0001, EV-0002, EV-0003]
source_file: "raw/SRC-0003_NewPINNs.pdf"
exclude_from_synthesis: false
---

# NewPINNs

## Human-readable summary

NewPINNs uses a conventional numerical solver during training. The network predicts a field, the solver advances that prediction a small number of steps, and the returned state participates in the solver-consistency loss:

$$
L=\left\lVert u_{\mathrm{NN}}-u_{\mathrm{solver}}\right\rVert^2.
$$

The solver output therefore affects optimization through the loss discrepancy, but backpropagation does not differentiate through the solver mapping $S$ itself: the method does not calculate $\partial S/\partial u$. The PDF presents this as a black-box/non-differentiable solver boundary and does not show a specific PyTorch `detach()` call. [EV-0001; SRC-0003, pp. 3–9]

The main target is state-dependent and recomputed from the current network field. The paper explicitly distinguishes it from fixed teacher labels and teacher-student distillation, while the shallow-water experiment retains a clear exception: a ten-epoch fixed solver-trajectory warm start. [EV-0001; SRC-0003, p. 22]

In the reported evaluation path, the trained network directly predicts spatial fields without showing the conventional solver in that forward prediction path. Demonstrations include 2D fields and a $32\times16\times96\times3$ 3D elasticity output. This is verified structural evidence for [[Amortized Projection and Solver Distillation|solver-informed training followed by direct inference]], but it is not a runtime/speedup result and is not post-prediction projection. [EV-0002]


![[Screenshot 2026-09-01 100405.png]]


## What matters here

- Solver output participates in forward/loss computation; the stopped path is backpropagation through $S$, not the solver value's influence on the loss.
- A shallow-water warm start uses solver trajectories, so the whole paper should not be called label-free.
- Partial solver evolution does not prove exact feasibility or full convergence.
- The method inherits solver accuracy, stability requirements, invariant structure, and computational cost and reports problem-specific stabilization. [EV-0003]
- No deployment gate, fallback, inference-speed proof, representation-freedom comparison, or lithography mechanism is established.

## Governance traceability

Canonical Source: `SRC-0003`, stored at `02_Evidence/SRC-0003_NewPINNs.md`. Targeted P1-P4 Human Audit completed on 2026-09-01. `EV-0001`, `EV-0002`, and `EV-0003` are verified only within their stated boundaries; other paper claims and reported metrics remain source-reported unless separately verified. No Method, Physics Constraint, Hypothesis, or Experiment was created.
