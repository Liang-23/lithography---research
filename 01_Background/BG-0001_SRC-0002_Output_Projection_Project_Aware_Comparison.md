---
schema_version: "1.0"
id: BG-0001
type: background-record
title: "SRC-0002 Pass 2: Project-aware comparison of output projection"
lifecycle_status: draft
authority_class: none
authority_scope: context-only
created_by: ai
content_origin: mixed
created_at: 2026-08-28
updated_at: 2026-08-29
owner: project-lead
review_status: pending-user-review
reviewed_by:
approved_by:
approval_ref: "User explicitly cleared the Human Audit gate and requested Pass 2 on 2026-08-28"
core_alignment: conflict
source_ids: [SRC-0002]
evidence_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: true
---

# SRC-0002 Pass 2: Project-aware comparison of output projection

## Purpose, authority, and scope

This record performs Pass 2 only: it interprets the human-audited reconstruction of *Physics-consistent machine learning with output projection onto physical manifolds* in relation to the current forward-lithography project.

- **Paper facts** below are source-reported facts from registered Source **SRC-0002**. They remain unverified because no claim-level **EV-####** record exists.
- **Project interpretations** are bounded comparisons against **Project Overview** and **Research Requirements**. They are not scientific Evidence or project decisions.
- **Human Audit basis:** the user explicitly stated on 2026-08-28 that the Human Audit was completed and the gate was cleared. No separate Human Audit artifact was found in the routed project files; the audited Pass 1 reconstruction and the explicit user clearance were therefore used as the operational basis.
- All mathematical expressions use Obsidian-compatible MathJax delimiters so that they render directly in Live Preview and Reading View.

This record does not establish field-wide novelty, define a lithography Physics Constraint, select a Method, create a Hypothesis or Experiment, or modify Locked Core.

## 1. Actual overlap with the current project

### Directly preceded by this Source

1. **Post-training output-level physical correction.** The paper explicitly corrects an already-produced ML output after the base model has been trained. [Source locator: SRC-0002, p. 2, “Framework and workflow”; p. 8, Conclusions]
2. **Projection onto a constraint-defined admissible set.** The paper formulates correction as the nearest output, under a weighted metric, satisfying selected physical equality constraints. [Source locator: SRC-0002, p. 2, Eq. (1)]
3. **Separation between neural prediction and physical correction.** The trained model first produces $f(x;\Theta)$; a separate optimizer then produces the corrected value $p^*$. [Source locator: SRC-0002, pp. 2–3, Eq. (1) and Fig. 1c]
4. **Physics after prediction rather than only through a training loss.** The demonstrated projection is invoked at prediction time, independently of whether the base model is a data-only NN or a loss-based PINN. [Source locator: SRC-0002, pp. 2–3, workflow and Fig. 1; p. 8, Conclusions]

These elements are **direct prior art relative to this Source**. Merely proposing “take a neural output and project it onto $g(x,p)=0$ after training” cannot by itself be treated as this project's scientific contribution.

### Partial overlap

1. **Physics-loss comparison.** The paper compares data-only NN, loss-based PINN, projected NN, and projected PINN in two case studies. This partially overlaps the project's concern that continuously adding physics penalties may conflict with data learning. [Source locator: SRC-0002, pp. 3–5, Figs. 1–3 and Table 1; pp. 5–10, Figs. 4 and 8]
2. **Limited-data and smaller-model motivation.** The reported plasma experiments show larger projection benefits for smaller networks and limited training sets. This is relevant to the project's limited high-fidelity data requirement, but it is evidence only for the paper's $17$-scalar plasma surrogate. [Source locator: SRC-0002, pp. 6–8, Figs. 5–7]
3. **Model-agnostic correction.** The correction accepts a point prediction and a constraint function without requiring a particular NN architecture. This supports separation of predictor and corrector, but does not establish compatibility with image-sized lithography tensors. [Source locator: SRC-0002, p. 2, “Framework and workflow”]

### Conceptually related but technically different

1. **Representation-learning freedom.** The paper's projection does not act on hidden representations because it is applied after training, but the paper does not measure representation quality or experimentally compare “free” versus constrained internal representation learning. [Source locator: SRC-0002, pp. 2–3, workflow and Fig. 1; pp. 8–9, Conclusions]
2. **High-dimensional output.** The plasma example is described by the authors as complex and high-dimensional, but the actual output is a $17$-scalar vector. The project requires aerial, resist, or wafer images. [Source locator: SRC-0002, pp. 4–6, Case study 2 and Fig. 4]
3. **Terminal correction as a teacher.** The project proposes transferring corrected knowledge back into the surrogate. The paper leaves projection external and does not use corrected values as training targets. [Source locator: SRC-0002, p. 3, Fig. 1; pp. 8–9, Conclusions]
4. **End-to-end deployment.** The project requires direct inference without a required external post-processing module. The paper's demonstrated final prediction depends on an external constrained optimizer for every point prediction. [Source locator: SRC-0002, p. 2, workflow; p. 8, Conclusions]

### Not addressed by this Source

- Lithography-specific physical relationships for aerial, resist, or wafer outputs. [Source locator: SRC-0002, pp. 2–8, demonstrated case studies]
- Projection or correction in image/tensor output spaces. [Source locator: SRC-0002, p. 3 and pp. 5–6, demonstrated output structures]
- Corrected-target training, pseudo-labeling, teacher-student distillation, or projection-based knowledge transfer. [Source locator: SRC-0002, p. 3, Fig. 1; pp. 8–9, Conclusions]
- Removal of the projection operator at deployment. [Source locator: SRC-0002, p. 2, workflow; p. 8, Conclusions]
- Differentiation through the projection and gradient interaction with $\Theta$. [Source locator: SRC-0002, pp. 9–10, Conclusions and “The projection method”]
- Non-differentiable or discontinuous terminal physical rules. [Source locator: SRC-0002, pp. 2 and 10, equality-constrained formulation]
- A safeguard that detects when projection would damage an already-good prediction. [Source locator: SRC-0002, p. 6, robustness discussion; no safeguard is specified]

## 2. Paper-to-project comparison

### 2.1 Output-level physical correction

**Paper fact.** Given a trained predictor $f(x;\Theta)$, the paper corrects its output by solving

$$
p^*(x)
=
\underset{p}{\operatorname{argmin}}\;
\left\|p-f(x;\Theta)\right\|_{W}^{2}
\quad
\text{subject to}
\quad
g(x,p)=0,
$$

with

$$
\left\|v\right\|_{W}^{2}=v^{\mathsf T}Wv,
\qquad W \succ 0.
$$

[Source locator: SRC-0002, p. 2, Eq. (1)]

**Project interpretation.** The general location of correction—after the neural prediction—is already occupied. A lithography contribution must therefore be more specific than output projection itself.

**Relationship.** **direct prior art**

**Boundary.** This Source does not show that an analogous, computable lithography constraint $g(x,p)$ exists, or that the same optimization is tractable for image-valued $p$.

### 2.2 Physically admissible solution set

**Paper fact.** The paper defines physical admissibility through the selected equality constraints $g(x,p)=0$. A compact mathematical restatement of the paper's feasible set is

$$
\mathcal{M}_x
=
\left\{
p \,\middle|\, g(x,p)=0
\right\}.
$$

This set notation is an Agent restatement of Eq. (1), not a separate equation printed by the authors. [Source locator: SRC-0002, p. 2, Eq. (1); p. 10, “The projection method”]

**Project interpretation.** The paper provides a reusable optimization pattern, but not the missing lithography feasible set.

**Relationship.** **partial overlap**

**Boundary.** Satisfaction of the selected equations establishes consistency with those equations only. It does not establish full physical correctness, simulator equivalence, or accuracy relative to the reference solution.

### 2.3 Separation of predictor and corrector

**Paper fact.** The prediction vector initializes $p$; IPOPT then solves the constrained problem and returns the corrected point prediction. The base model is already trained and is not modified by the demonstrated projection. [Source locator: SRC-0002, p. 2, workflow steps (i)–(iii); p. 10, “The projection method”]

**Project interpretation.** This cleanly precedes the project's predictor/corrector separation. It also exposes a deployment mismatch: the paper's corrector remains external.

**Relationship.** **direct prior art** for separation; **potential conflict** with the project's inference boundary.

**Boundary.** The paper does not show a single-pass neural surrogate that internalizes the correction.

### 2.4 Physics during training versus after prediction

**Paper fact.** Projection is absent from base-model training. Physics enters training only in the separate loss-based PINN baseline:

$$
\mathcal{L}_{\mathrm{total}}
=
\left(1-\lambda_{\mathrm{physics}}\right)\mathcal{L}_{\mathrm{data}}
+
\lambda_{\mathrm{physics}}\mathcal{L}_{\mathrm{physics}}.
$$

The projected variants instead apply the constraint after training, at prediction time. [Source locator: SRC-0002, p. 3, Fig. 1; p. 9, Eqs. (8)–(10); p. 8, Conclusions]

**Project interpretation.** The paper is a supporting precedent for separating data fitting from terminal physical correction.

**Relationship.** **supporting precedent**

**Boundary.** It does not prove that post-training correction is generally superior to every differentiable physics loss, physics-informed architecture, operator-learning method, or training schedule.

### 2.5 Effect on representation learning

**Paper fact.** The projection is applied after the base model is trained, so the demonstrated operation does not constrain hidden activations or update $\Theta$. The paper criticizes system-specific invariant architectures as lacking flexibility and reports weak results for its loss-based PINN baselines. [Source locator: SRC-0002, pp. 1–2, Introduction; pp. 2–3, workflow; pp. 8–10, Conclusions and Fig. 8]

**Project interpretation.** The method structurally leaves internal representations untouched, which is compatible with the project's desire not to unnecessarily constrain representation learning.

**Relationship.** **partial overlap**

**Boundary.** The authors do not explicitly define “representation-learning freedom,” do not inspect learned representations, and do not experimentally show that freedom itself causes better learning.

### 2.6 Differentiability and gradient interaction

**Paper fact.** The demonstrated projection is an external CasADi/IPOPT optimization performed after training. The paper does not analyze differentiability of the projection map or backpropagation through it. [Source locator: SRC-0002, p. 9, Conclusions; p. 10, Eq. (16) and “The projection method”]

**Project interpretation.** In the demonstrated workflow, no correction-derived gradient is transferred to $\Theta$. Any project mechanism that learns from corrected outputs needs an additional transfer path.

**Relationship.** **important distinction**

**Boundary.** It cannot be concluded that the map is non-differentiable, differentiable, or suitable for implicit differentiation; the paper simply does not establish this.

### 2.7 External projection at inference

**Paper fact.** The constrained optimization is solved for each point prediction; sequential spring-mass rollout repeats it at each state transition. [Source locator: SRC-0002, p. 2, workflow; p. 3, “Trajectory prediction”; p. 8, Conclusions]

**Project interpretation.** Adopted unchanged, this violates the Research Requirement that the final surrogate directly map inputs to outputs without a required external filtering or post-processing module.

**Relationship.** **potential conflict**

**Boundary.** This is a method-to-requirement conflict, not evidence that Locked Core should be changed. The governance boundary is to report it and not select the paper's method as the project Method.

### 2.8 Transfer of corrected knowledge back into the surrogate

**Paper fact.** No corrected output is reused as a training target; no pseudo-labeling, retraining, teacher-student distillation, or projection-removal stage is described. Unified integration of projection with training is only proposed as future work. [Source locator: SRC-0002, p. 3, Fig. 1; pp. 8–9, Conclusions]

**Project interpretation.** The project's “correction $\rightarrow$ knowledge transfer $\rightarrow$ end-to-end surrogate” stage is not occupied by this Source.

**Relationship.** **important distinction**

**Boundary.** This Source neither validates nor refutes projection-based knowledge transfer.

### 2.9 Applicability to high-dimensional spatial outputs

**Paper fact.** The spring-mass model predicts $4$ scalars per transition; the plasma model predicts $17$ scalars from $3$ scalar inputs. The paper does not demonstrate images or spatial fields. [Source locator: SRC-0002, p. 3, “Data generation”; pp. 5–6, “Data generation” and Fig. 4]

**Project interpretation.** Transfer to lithography tensors is a project-level inference, not demonstrated evidence. The constraint evaluation, metric, solver memory, and optimization geometry can change qualitatively in a very large output space.

**Relationship.** **important distinction**

**Boundary.** The authors' use of “high-dimensional” for the plasma case does not support a direct claim about aerial images, resist images, wafer images, or very large output tensors.

## 3. Audit of current project assumptions

### A. Output projection itself

**Answer: yes, in a bounded form.** This Source establishes an existing methodology in which an already-trained model's output is projected onto a manifold defined by selected physical equality constraints through constrained optimization. The prior-art portion is:

$$
\text{raw prediction}
\;\longrightarrow\;
\underset{p}{\operatorname{argmin}}\,
\left\|p-f(x;\Theta)\right\|_{W}^{2}
\;\text{s.t.}\;
g(x,p)=0
\;\longrightarrow\;
\text{corrected prediction}.
$$

[Source locator: SRC-0002, p. 2, Eq. (1) and workflow; p. 3, Fig. 1c]

Therefore, “post-training output projection onto a physical equality-constraint manifold” cannot by itself serve as the project's scientific contribution. This conclusion is **Source-relative** and is not a field-wide novelty determination.

### B. Free representation learning

The three claims must remain separate:

1. **The method does not apply physics to hidden representations:** yes, structurally true for the demonstrated post-training workflow. [Source locator: SRC-0002, pp. 2–3, workflow and Fig. 1c]
2. **The authors explicitly argue for representation-learning freedom:** no. They argue that specialized invariant architectures can lack flexibility and generality, but they do not formulate the project's representation-freedom thesis. [Source locator: SRC-0002, pp. 1–2, Introduction]
3. **Experiments show that representation freedom improves learning:** no. No hidden-representation analysis or controlled experiment isolates representation freedom as the causal variable.

The paper is therefore compatible with, but does not establish, the project's stronger representation-learning rationale.

### C. Physics-loss avoidance

The paper supplies a bounded comparison, not a general verdict.

- In the spring-mass experiment, a grid search over more than ten orders of magnitude in $\lambda_{\mathrm{physics}}$ found no consistent improvement over $\lambda_{\mathrm{physics}}=0$, and performance degraded near $\lambda_{\mathrm{physics}}\approx 1$. [Source locator: SRC-0002, pp. 9–10, Fig. 8 and Methods]
- In both case studies, the selected general-law loss-based PINN did not improve predictive accuracy or law compliance relative to the data-only NN, while post-training projection strongly reduced residual-law error and improved selected predictive metrics. [Source locator: SRC-0002, pp. 3–6, Figs. 2–4; pp. 8–10, Conclusions]
- The authors explicitly bound their conclusion to the systems and the particular loss-based PINN formulation studied. [Source locator: SRC-0002, pp. 8–10, Conclusions and Methods]

What this proves: for these two systems, constraints, architectures, loss definitions, and tuning procedures, the tested post-training projection outperformed the tested physics-loss baseline on the reported measures.

What it does not prove: output correction is generally preferable to all ways of embedding physics into training, or that avoiding physics losses necessarily preserves better representations.

### D. Corrected-target knowledge transfer

| Mechanism | Present in the paper? | Source-bounded assessment |
|---|---:|---|
| 1. External projection only | Yes | The final corrected output comes from a separate optimizer at prediction time. [SRC-0002, p. 2, workflow; p. 8, Conclusions] |
| 2. Projection used during training | No | Unified integration with training is future work only. [SRC-0002, p. 9, Conclusions] |
| 3. Corrected outputs used as targets | No | No such target construction is described. [SRC-0002, p. 3, Fig. 1; pp. 8–9, Conclusions] |
| 4. Distillation or teacher-student transfer | No | No student model, distillation loss, or retraining stage is described. [SRC-0002, p. 3, Fig. 1; pp. 8–9, Conclusions] |
| 5. Eventual removal of external projection at inference | No | Every corrected prediction still depends on the external constrained optimization. [SRC-0002, p. 2, workflow; p. 8, Conclusions] |

The distinction is decisive: the paper occupies **external terminal projection**, while the project is interested in **transferring corrected knowledge into the surrogate so that final deployment need not retain the external corrector**.

### E. High-dimensional applicability

The demonstrated output structures are:

$$
y_{\mathrm{spring}}\in\mathbb{R}^{4},
\qquad
y_{\mathrm{plasma}}\in\mathbb{R}^{17}.
$$

[Source locator: SRC-0002, p. 3, spring-mass “Data generation”; pp. 5–6, plasma “Data generation” and Fig. 4]

The evidence directly supports small vector-valued surrogate outputs and a sequential four-state rollout. It does not directly support:

- high-dimensional images;
- spatial fields;
- lithography aerial, resist, or wafer images;
- very large output spaces.

Applying the method to lithography is therefore an explicit **project inference**, not demonstrated evidence from this Source.

## 4. Projection mechanism from the project's perspective

### 4.1 What defines the paper's admissible set

For a fixed input $x$, the paper's admissible set is the zero-level set of selected equality constraints:

$$
\mathcal{M}_x=\left\{p:g(x,p)=0\right\}.
$$

The spring-mass projection uses conservation of mechanical energy. In trajectory notation, the paper writes

$$
R_{1}=E(t)-E(0),
$$

and the training loss computes the output/input energy mismatch. [Source locator: SRC-0002, p. 3, “Trajectory prediction”; p. 9, Eq. (8)]

The plasma projection uses:

$$
R_{1}
=
P-\sum_i [X_i]\,k_{\mathrm B}T_g,
$$

$$
R_{2}
=
I-e\,n_e v_d\,\pi R^2,
$$

$$
R_{3}
=
n_e-\sum_i[X_i^+]+\sum_j[X_j^-].
$$

[Source locator: SRC-0002, p. 5, Eqs. (5)–(7)]

These residuals use known inputs such as $P$, $I$, and $R$, together with predicted outputs such as species densities, $T_g$, $n_e$, and $v_d$.

### 4.2 Why projection is computationally possible in the paper

- The residual functions are explicitly available as algebraic functions of the known input and a small output vector. [Source locator: SRC-0002, pp. 2 and 5, Eqs. (1) and (5)–(7)]
- The correction solves for only $4$ or $17$ output variables, rather than rerunning the full ODE ground-truth generator inside Eq. (1). [Source locator: SRC-0002, p. 3; pp. 5–6]
- The authors implement the nonlinear constrained problem with CasADi Opti and IPOPT, initialize at the raw prediction, use $W=I$, and set solver tolerances to $10^{-3}$ for spring-mass and $10^{-8}$ for plasma. [Source locator: SRC-0002, p. 10, “The projection method”]

### 4.3 Explicitness, uniqueness, and computational burden

- **Feasible set:** explicitly known only as the implicit set defined by the selected equations. It is not shown to equal the complete set of physically correct states.
- **Uniqueness:** not established. The authors explicitly warn that outputs far from the manifold can lead to ambiguity from multiple possible solutions. [Source locator: SRC-0002, p. 6, “Robustness of the projection method”]
- **Numerical optimization:** required for every corrected prediction in the demonstrated method.
- **Metric:** all reported experiments use $W=I$; alternative weighting matrices are left for future work. [Source locator: SRC-0002, p. 10, “The projection method”]
- **Measured burden:** for $500$ plasma observations, projection reportedly takes $1.75\,\mathrm{s}$, adding $4.33\%$ to the paper's measured total computation time. This number is system- and implementation-specific and cannot be extrapolated to image tensors. [Source locator: SRC-0002, p. 8, “Computation time”]

### 4.4 What is scientifically undefined for lithography

The analogous lithography object would require a computable relation of the form

$$
g_{\mathrm{litho}}(x,y)=0
\quad\text{or, more generally,}\quad
R_{\mathrm{litho}}(x,y)
$$

for an aerial image, resist image, or wafer-level output $y$. This record does **not** propose such a relation.

The following remain scientifically undefined:

1. Which terminal lithography variables participate in the relation.
2. Whether the relation is an equality, inequality, admissible range, variational condition, operator consistency condition, or another computable form.
3. The variables, units, tensor shapes, coordinates, boundary conditions, and validity regime.
4. Whether checking or enforcing it is materially cheaper than rerunning the high-fidelity simulator.
5. Whether the feasible set is nonempty for realistic predicted images.
6. Whether projection is unique, and how competing feasible images should be ranked.
7. Which distance metric preserves lithographically important spatial structure.
8. Whether the relation is differentiable, discontinuous, or usable only through a black-box correction.

## 5. Projection failure modes relevant to the project

### 5.1 Failure behavior demonstrated in the paper

1. **Not every output improves on every trajectory.** In the spring-mass test, mean four-variable RMSE improves for $96\%$ of NN trajectories and $97\%$ of PINN trajectories, but all four variables improve simultaneously for only $60\%$ and $61\%$, respectively. Thus, the paper itself does not support “projection improves every component of every prediction.” [Source locator: SRC-0002, pp. 4–5, Table 1]
2. **Benefit becomes marginal for a strong base model.** As plasma network complexity approaches the high-complexity plateau, the projected and unprojected predictions converge and the projection advantage becomes marginal. [Source locator: SRC-0002, pp. 6–7, Fig. 5 and discussion]
3. **Very weak base models produce imperfect corrected structure.** For the simplest plasma network, projection substantially reduces electron-density RMSE but the corrected curve visibly lacks smoothness. [Source locator: SRC-0002, p. 7, Fig. 5b.i and discussion]
4. **Projection has nonzero computational cost.** It is an additional optimization step and contributes measured runtime in the paper's own setting. [Source locator: SRC-0002, p. 8, “Computation time”]

The paper does not isolate a controlled case proving that an already-more-accurate raw prediction is moved away from the reference. It does, however, empirically show non-universal component-wise improvement.

### 5.2 Limitations explicitly stated by the authors

1. Projection may be ineffective or ambiguous when the base prediction is far from the constraint manifold and multiple solutions exist. [Source locator: SRC-0002, p. 6, “Robustness of the projection method”]
2. Sufficient training and model complexity can make correction unnecessary or marginal. [Source locator: SRC-0002, pp. 6–7, “Robustness” and Fig. 5]
3. The method is demonstrated only post-training; unified training is future work. [Source locator: SRC-0002, p. 9, Conclusions]
4. $W=I$ is the only tested distance weighting; metric design is unresolved. [Source locator: SRC-0002, p. 10, “The projection method”]
5. Difficult high-frequency features are left for future evaluation. [Source locator: SRC-0002, p. 9, Conclusions]

### 5.3 Reasonable project-level implications inferred from the method

These are inferences, not demonstrated paper results:

- A correction can satisfy $g(x,p)=0$ while worsening reference accuracy because feasibility and predictive truth are different objectives.
- The chosen $W$, normalization, and variable scaling determine what “nearest” means; a poor metric can preserve the wrong quantities or damage spatial structure.
- An incomplete physical constraint can remove useful information that is not represented by the constraint.
- An approximate or incorrectly specified feasible set can make the output consistent with the wrong model.
- Large image tensors may make per-sample constrained optimization too expensive or numerically fragile.
- An external corrector creates a deployment dependency and a second failure surface.
- A correction policy needs a guard or acceptance criterion if the raw surrogate can already be better than the corrected result.

## 6. Paper-relative unresolved questions

**Unresolved relative to this Source**

1. What lithography-specific terminal relationship can define admissibility or a correction direction for aerial, resist, or wafer images?
2. Can that relation be evaluated and enforced without effectively rerunning the high-fidelity simulator?
3. How should a projection metric preserve spatial frequency, edge response, process-variation response, and input-geometry/output behavior?
4. How can the method detect or avoid a correction that worsens an already-accurate raw prediction?
5. Can corrected outputs be used as training targets or teacher outputs, and can the external projection then be removed at deployment?
6. How do feasibility, uniqueness, solver stability, memory, and runtime scale from $17$ scalars to large image tensors?
7. What mechanism is appropriate when the relevant physical rule is non-differentiable, discontinuous, approximate, or only locally valid?

These are not labelled global literature gaps because this Source has not been combined with broader verified literature Evidence.

## 7. Implications for future Physical Constraint Discovery

This section does not define or promote **PC-0001**.

| Candidate requirement | Lesson from SRC-0002 | Currently unresolved for lithography |
|---|---|---|
| Computability | The constraint must be evaluable inside a correction problem. | No terminal lithography relation has been defined. |
| Explicit variables and units | The paper's residuals name inputs/outputs and physical constants. | Output stage, variables, units, tensor shapes, coordinate system, and process conditions are unspecified. |
| Validity regime | A constraint is meaningful only in the regime where its law applies. | No aerial/resist/wafer validity domain or boundary-condition contract exists. |
| Admissibility or correction direction | Equality constraints define a zero-level set and the metric supplies a nearest-point direction. | It is unknown whether lithography has a useful explicit feasible set or only partial/approximate behavior rules. |
| Feasibility and uniqueness | Multiple feasible solutions can make projection ambiguous. | Existence, uniqueness, and tie-breaking for image outputs are undefined. |
| High-dimensional compatibility | SRC-0002 solves small vector problems. | Scalability to large spatial tensors is untested and scientifically unresolved. |
| Distance metric and scaling | $W$ determines the output-space metric; only $W=I$ is tested. | No metric is defined that preserves lithography-relevant spatial structure and respects heterogeneous units. |
| Correction magnitude and safety | Projection can be unnecessary, marginal, or fail to improve all outputs. | No trust region, trigger, rejection rule, or raw-versus-corrected selection criterion exists. |
| Constraint completeness | Compliance is guaranteed only for the selected equations. | It is unknown which constraints are sufficient and which important behaviors would remain unconstrained. |
| Computational cost | The paper requires per-prediction nonlinear optimization. | No cost bound shows that correction remains cheaper than simulation or compatible with deployment. |
| Training/inference compatibility | SRC-0002 keeps correction external at inference. | The project requires a path to transfer corrected knowledge and remove required external post-processing. |
| Differentiability | Not studied by the paper. | The need for gradients depends on whether correction is external, jointly trained, or distilled; no choice has been made. |
| Empirical rejection criteria | Paper results show that correction is not uniformly beneficial. | No lithography-specific benchmark, ablation, acceptance threshold, or failure test exists. |

## 8. Final Pass 2 synthesis

### A. What this paper already occupies

- Post-training output-level correction of ML predictions.
- Nearest-point projection under a weighted output metric.
- Equality-constraint-defined physical manifolds.
- Separation of a trained predictor from an external physical corrector.
- Application of the same corrector to data-only NN and loss-based PINN outputs.
- Bounded evidence that the tested projection can outperform the tested general-law physics-loss baseline in two small vector-output systems.
- Per-prediction constrained optimization with explicit runtime and robustness limitations.

### B. What remains open for our project

- A computable lithography terminal constraint and validity regime.
- A safe, structure-preserving correction for aerial/resist/wafer image tensors.
- Scaling, feasibility, uniqueness, metric design, and correction acceptance.
- Transfer of corrected knowledge into the surrogate.
- Removal of required external correction during final inference.
- Behavior under discontinuous, approximate, or non-differentiable physics.

### C. Most important consequence for our research direction

This paper **narrows the direction and forces a reformulation of any contribution claim**, while leaving the central research question intact.

It strengthens the rationale for investigating terminal physical correction and shows that a tested post-training projection can outperform a tested general-law physics-loss baseline. At the same time, it makes clear that generic output projection is already occupied relative to this Source. The project's differentiating scientific work must therefore lie in the lithography-specific constraint, safe and scalable high-dimensional correction, corrected-knowledge transfer, and an end-to-end deployment path without the external optimizer.

The paper's demonstrated method cannot be adopted unchanged because its required inference-time IPOPT step conflicts with the project's final end-to-end inference requirement. This is reported as a Core-alignment conflict; no Core revision is authorized or performed.

### D. Next literature targets

1. **Terminal lithography admissibility:** computable physical relations on aerial, resist, or wafer images that can be evaluated without rerunning the full simulator.
2. **Scalable projection for spatial tensors:** constrained, proximal, or manifold correction methods for large image/field outputs, including metric choice, uniqueness, and spatial-structure preservation.
3. **Projection-to-surrogate transfer:** corrected-target learning, teacher-student distillation, or amortized projection that removes the external optimizer at inference.
4. **Safe selective correction:** event-triggered, trust-region, or accept/reject mechanisms that prevent approximate constraints from degrading accurate predictions.
5. **Differentiable and non-differentiable terminal physics:** training/inference strategies for implicit, discontinuous, or black-box correction operators.

## Completion report

1. **Source used:** **SRC-0002**, registered PDF at **raw/Physics-consistent machine learning.pdf**, SHA-256 matching the Source record.
2. **Pass 1 / Human Audit material used:** the complete audited Pass 1 reconstruction now stored in the canonical `SRC-0002` record at `02_Evidence/SRC-0002_Physics_Consistent_Machine_Learning_with_Output_Projection_onto_Physical_Manifolds.md`, plus the user's explicit 2026-08-28 statement that the Human Audit gate was cleared. Critical equations and claims were rechecked against PDF pages 2–10.
3. **Project files consulted through the normal route:** **Core_Governance.md**, **Project_Overview.md**, **Research_Requirement.md**, **Current_State.md**, **Context_Router.md**, **Background_Index.md**, the Background template/policy, **Source_Registry.md**, the **SRC-0002** source record, **Wiki_Workflow.md**, and the directly relevant derived concept notes.
4. **Main paper-to-project conclusion:** output-level post-training projection is already direct prior art relative to this Source; the project's open space is lithography-specific, high-dimensional, safe correction plus knowledge transfer into an end-to-end surrogate.
5. **Unresolved factual ambiguity:** the paper does not establish projection uniqueness, differentiability, corrected-target reuse, image-output scalability, or the exact scaling/domain in which $W=I$ defines distance. No standalone Human Audit artifact was found; the explicit user gate clearance was used procedurally.
6. **Next literature targets:** terminal lithography admissibility; scalable spatial-tensor projection; projection-to-surrogate transfer; safe selective correction; differentiable/non-differentiable terminal physics.
7. **Boundary confirmation:** no field-wide novelty claim, Physics Constraint selection, Method selection, Hypothesis creation, Experiment design, simulator selection, Evidence promotion, or Core modification was performed.

## Review checklist

- [x] Every source is registered.
- [x] Every paper-derived factual claim is marked unverified and has a Source locator.
- [x] AI/project interpretation is labelled and separated from paper fact.
- [x] No project decision or Core change is embedded here.
- [x] Mathematical expressions are written in LaTeX.
- [ ] Human review of this Pass 2 draft is pending.
- [ ] The record remains excluded from synthesis until review.
