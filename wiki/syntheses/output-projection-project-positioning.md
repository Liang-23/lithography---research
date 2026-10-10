---
title: "Output Projection and Project Positioning"
aliases:
  - "SRC-0002 Project Positioning"
type: synthesis
lifecycle_status: draft
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-29
updated_at: 2026-08-29
review_status: pending-user-review
core_alignment: conflict
knowledge_status: source-relative-project-interpretation
canonical_refs:
  - "01_Background/BG-0001_SRC-0002_Output_Projection_Project_Aware_Comparison.md"
  - "02_Evidence/SRC-0002_Physics_Consistent_Machine_Learning_with_Output_Projection_onto_Physical_Manifolds.md"
source_ids:
  - SRC-0002
exclude_from_synthesis: true
---

# Output Projection and Project Positioning

## Why this node exists

This is the human-readable ==semantic== projection of the draft `BG-0001` comparison. It extracts the conclusions that matter for the current project without exposing the full Background record as a Graph node. Paper facts remain Source-reported and unverified; project interpretation remains derived and does not change Core.

## What SRC-0002 already occupies

Relative to this Source, the following space is already occupied:

- post-training [[Output-level Physical Correction]];
- nearest-point [[Physics-defined Solution Space Projection]] under a weighted output metric;
- equality-constraint-defined ==admissibility== through $g(x,p)=0$;
- separation of an already-trained predictor from an external physical corrector;
- per-prediction constrained optimization at inference;
- application of the same corrector to data-only NN and loss-based PINN outputs.

The ==generic== sequence

$$
\text{raw neural output}
\longrightarrow
\underset{p}{\operatorname{argmin}}\;
\left\|p-f(x;\Theta)\right\|_{W}^{2}
\quad\text{s.t.}\quad g(x,p)=0
\longrightarrow
\text{corrected output}
$$

therefore cannot, by itself, serve as the project's scientific contribution. This is a Source-relative ==prior-art== conclusion, not a field-wide novelty determination. [SRC-0002, p. 2, Eq. (1) and workflow; p. 3, Fig. 1c]

## The decisive project ==distinctions==

| Question                                            | What the paper establishes                                                                            | Meaning for this project                                                                                                            | Relationship          |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Does projection leave hidden activations untouched? | Yes structurally: correction occurs after training and does not update $\Theta$.                      | Compatible with preserving [[Neural Representation Learning]], but it does not prove that representation freedom improves learning. | partial overlap       |
| Is projection better than physics losses?           | It outperforms the tested loss-based PINN baselines in two small vector systems on selected measures. | Useful bounded precedent, not a general verdict on all training-time physics integration.                                           | supporting precedent  |
| Are corrected values learned by the surrogate?      | No corrected-target training, distillation, retraining, or teacher-student stage is described.        | [[Projection-based Knowledge Distillation]] remains unoccupied relative to this Source.                                             | important distinction |
| Is the external corrector removed?                  | No; the constrained optimizer produces every corrected prediction.                                    | Conflicts with the required end-to-end inference boundary of the [[High-dimensional AI Surrogate]].                                 | potential conflict    |
| Are spatial outputs demonstrated?                   | No; outputs have $4$ and $17$ scalar components.                                                      | Transfer to aerial, resist, or wafer images is an inference, not demonstrated evidence.                                             | important distinction |

## Why projection is computable in the paper

For each fixed input $x$, physical admissibility is the zero-level set

$$
\mathcal{M}_x=\left\{p\mid g(x,p)=0\right\}.
$$

The set is computable because the paper provides explicit algebraic residuals in a small output vector. The spring-mass example uses energy conservation; the plasma example uses pressure, current, and quasi-neutrality relations. IPOPT solves for only $4$ or $17$ output variables and starts from the neural prediction. [SRC-0002, pp. 2–6; p. 10]

The paper does not establish uniqueness. It warns that predictions far from the manifold can lead to ineffective or ambiguous correction when multiple solutions exist. The metric also matters: all experiments use $W=I$, and alternative weighting remains unresolved. [SRC-0002, p. 6; p. 10]

## Why this is not yet a lithography mechanism

The corresponding lithography relation remains scientifically undefined. The project does not yet know:

- which aerial, resist, or wafer variables would enter a constraint;
- whether admissibility should be an equality, inequality, range, variational condition, or operator-consistency relation;
- the units, tensor shapes, coordinates, boundary conditions, and validity regime;
- whether checking or enforcing the relation is materially cheaper than rerunning the high-fidelity simulator;
- whether a feasible solution exists and is unique for realistic image predictions;
- which distance metric preserves spatial frequency, edges, and process-dependent structure;
- whether the rule is differentiable, discontinuous, approximate, or black-box.

No lithography constraint is proposed here.

## Projection is not a universal repair mechanism

The paper itself shows that projection does not improve every component of every prediction: all four spring variables improve simultaneously in only $60\%$ of projected-NN trajectories, even though mean four-variable RMSE improves in $96\%$. It also reports marginal benefit for strong base models, imperfect smoothness for a very weak model, ambiguity far from the manifold, and nonzero computational cost. [SRC-0002, pp. 5–8, Table 1 and Figs. 5–7]

Project-level implications—not demonstrated paper results—are that a correction can satisfy the chosen constraint while worsening reference accuracy, an incomplete or incorrect feasible set can remove useful learned information, and a poor metric can damage important spatial structure. A practical method therefore needs a correction-magnitude rule and an accept/reject safeguard.

## Most important consequence

SRC-0002 narrows the direction and forces any contribution claim to be reformulated, while leaving the central project question intact. Generic external output projection is already occupied relative to this Source. The open project work is more specific:

- define a lithography-specific and computable terminal relation;
- scale correction safely to large spatial tensors;
- preserve useful learned structure and reject damaging corrections;
- transfer corrected knowledge back into the surrogate;
- remove any required external optimizer from final deployment.

The paper's demonstrated method cannot be adopted unchanged because its inference-time optimizer conflicts with the final end-to-end inference requirement. That conflict does not authorize a Core change or select a Method.

## Unresolved relative to this Source

1. What terminal lithography relationship can define admissibility or a correction direction?
2. Can it be evaluated and enforced without effectively rerunning the full simulator?
3. How should a metric preserve spatial structure in large image tensors?
4. How should correction be rejected when the raw prediction is already better?
5. Can corrected outputs train a surrogate that no longer needs projection at inference?
6. How do feasibility, uniqueness, memory, solver stability, and runtime scale from $17$ scalars to image tensors?
7. What mechanism works for discontinuous, approximate, or non-differentiable terminal physics?

These are unresolved relative to `SRC-0002`, not global literature gaps.

## Connected Wiki knowledge

Read [[physics-consistent-machine-learning-with-output-projection-onto-physical-manifolds|the SRC-0002 source digest]] for the paper-level method and results. The relevant project concepts are [[Output-level Physical Correction]], [[Physics-defined Solution Space Projection]], [[Projection-based Knowledge Distillation]], [[Neural Representation Learning]], and [[High-dimensional AI Surrogate]].

## Governance traceability

- Canonical comparison: `BG-0001`, stored at `01_Background/BG-0001_SRC-0002_Output_Projection_Project_Aware_Comparison.md`
- Canonical Source reconstruction: `SRC-0002`, stored at `02_Evidence/SRC-0002_Physics_Consistent_Machine_Learning_with_Output_Projection_onto_Physical_Manifolds.md`
- Status: draft human-facing synthesis; pending user review; excluded from higher-level synthesis
- No field-wide novelty claim, `EV-####`, `PC-####`, Hypothesis, Method, Experiment, simulator, dataset, ADR, or Core change was created

