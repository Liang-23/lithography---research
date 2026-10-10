---
title: "Physics-consistent machine learning with output projection onto physical manifolds"
aliases:
  - "Physics-consistent machine learning"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-27
updated_at: 2026-08-29
review_status: source-checked
reconstruction_review_status: human-audit-cleared
core_alignment: conflict
canonical_refs:
  - "02_Evidence/SRC-0002_Physics_Consistent_Machine_Learning_with_Output_Projection_onto_Physical_Manifolds.md"
  - "01_Background/BG-0001_SRC-0002_Output_Projection_Project_Aware_Comparison.md"
source_ids:
  - SRC-0002
source_file: "raw/Physics-consistent machine learning.pdf"
exclude_from_synthesis: false
---

# Physics-consistent machine learning with output projection onto physical manifolds

## Human-readable summary

The paper corrects the output of an already-trained surrogate by solving a constrained optimization problem after prediction. The corrected point is chosen to remain close to the raw neural output while satisfying selected physical equality constraints. It demonstrates the approach on a $4$-scalar spring-mass state and a $17$-scalar reactive-plasma output—not on images or spatial fields.

All claims here remain Source-reported and unverified: no claim-level `EV-####` exists. The full machine-grade Pass 1 reconstruction, exact audit detail, and page locators are stored in the canonical `SRC-0002` Source record rather than only in this Wiki note.

## Method at a glance

For an input $x$ and trained predictor $f(x;\Theta)$, the paper solves

$$
p^*(x)
=
\underset{p}{\operatorname{argmin}}\;
\left\|p-f(x;\Theta)\right\|_{W}^{2}
\quad\text{subject to}\quad
g(x,p)=0.
$$

The optimization variable starts at the raw prediction, and the optimizer returns the final corrected output. All reported experiments use $W=I$ and CasADi/IPOPT. The operation is external to neural training and is repeated for every corrected prediction. [SRC-0002, p. 2, Eq. (1) and workflow; p. 10, “The projection method”]

This is a concrete Source precedent for [[Output-level Physical Correction]] and [[Physics-defined Solution Space Projection]]. It does not transfer the corrected output back into the network.

## What the paper demonstrates

- The same external corrector is applied to a data-only NN and a loss-based PINN. [pp. 2–4, Fig. 1 and Fig. 2; p. 6, Fig. 4]
- The spring-mass constraint is total mechanical-energy conservation. The plasma constraints represent pressure, discharge current, and quasi-neutrality. [p. 3; p. 5, Eqs. (5)–(7)]
- Across $100$ spring trajectories, mean four-variable RMSE improves for $96\%$ of NN trajectories, but all four variables improve together for only $60\%$. This is evidence against assuming universal component-wise improvement. [p. 5, Table 1]
- Plasma residual-law errors fall by more than $9$ orders of magnitude after projection; benefits are larger for smaller models and become marginal near the high-complexity plateau. [pp. 5–7, Figs. 4–5]
- For $500$ plasma observations, the reported projection step takes $1.75\,\mathrm{s}$ and adds $4.33\%$ to total measured computation time in that implementation. [p. 8, “Computation time”]
- The tested loss-based PINN formulation does not outperform the data-only baseline in these two systems, while projection improves the reported selected metrics. This comparison is bounded to the tested systems, losses, tuning, and architectures. [pp. 3–6; pp. 9–10, Fig. 8]

## What the paper does not establish

- It does not study hidden-representation quality or prove that unconstrained representation learning is beneficial.
- It does not show that post-training correction is generally superior to every way of integrating physics during training.
- It does not use projected values as targets, perform teacher-student transfer, or implement [[Projection-based Knowledge Distillation]].
- It does not remove the external constrained optimizer at inference.
- It does not analyze backpropagation through the projection or establish differentiability of the projection map.
- It does not demonstrate aerial, resist, or wafer images, spatial fields, or other very large output tensors.
- It does not establish projection uniqueness or a safeguard that rejects damaging corrections.

## Human Audit and project interpretation

The user explicitly cleared the Pass 1 Human Audit gate on 2026-08-28. No separate Human Audit artifact was found, so that procedural ambiguity remains recorded in the canonical Source and Background records.

The project-aware implications are digested in [[output-projection-project-positioning|Output Projection and Project Positioning]]. The central distinction is that the paper keeps a required external optimizer at inference, while the project requires a final [[High-dimensional AI Surrogate]] without required external post-processing and is interested in transferring corrected knowledge into the surrogate.

## Governance traceability

- Canonical Source: `SRC-0002`, stored at `02_Evidence/SRC-0002_Physics_Consistent_Machine_Learning_with_Output_Projection_onto_Physical_Manifolds.md`
- Registered original: `raw/Physics-consistent machine learning.pdf`
- Project comparison: `BG-0001`, stored at `01_Background/BG-0001_SRC-0002_Output_Projection_Project_Aware_Comparison.md`
- Evidence status: claims unverified; no `EV-####`
- Graph boundary: the paths above are non-clickable traceability, not Wiki Graph edges

