---
schema_version: "1.0"
id: SRC-0002
type: source-record
title: "Physics-consistent machine learning with output projection onto physical manifolds"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-and-audited-reconstruction
created_by: ai
content_origin: mixed
created_at: 2026-08-27
updated_at: 2026-08-29
owner: project-lead
review_status: source-checked
reconstruction_review_status: human-audit-cleared
reviewed_by: AI Agent
approved_by: user
approval_ref: "Explicit source-admission and Pass 1 reconstruction request, 2026-08-27"
human_audit_ref: "User explicitly confirmed the Pass 1 Human Audit gate was cleared on 2026-08-28; no separate audit artifact was found"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Physics-consistent machine learning with output projection onto physical manifolds

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\Physics-consistent machine learning.pdf`
- Source type: PDF; peer-reviewed journal article
- Authors: Matilde Valente, Tiago C. Dias, Vasco Guerra, Rodrigo Ventura
- Organizations: Instituto de Plasmas e Fusão Nuclear, Instituto Superior Técnico, University of Lisbon; Department of Electrical Engineering, University of Michigan; Instituto de Sistemas e Robotica, Instituto Superior Técnico, University of Lisbon
- Journal: *Communications Physics* 8, Article 433 (2025)
- DOI: `10.1038/s42005-025-02329-1`
- Publication history: Received 2025-03-25; accepted 2025-09-25; published online 2025-11-17
- Imported/registered date: 2026-08-27
- Original location: `https://doi.org/10.1038/s42005-025-02329-1`, printed in the original PDF
- Language: English
- License/access restriction: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (`CC BY-NC-ND 4.0`), as printed on page 11

## Integrity

- File size: 2,639,760 bytes
- Hash algorithm: SHA-256
- Content hash: `99A2573C7D4FFE8F501BC871BEE256935F7CA70358F32508832BF7AD8ED9A869`
- PDF page count: 11
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Admitted for source-faithful reconstruction of the paper's physics-consistent machine-learning formulation and reported experiments. Project-specific applicability was intentionally not assessed in this Pass 1 task.
- Allowed use: Source-faithful Background/Wiki reconstruction and possible future claim-level review through the normal Evidence workflow.
- Prohibited use: Treating registration or reconstruction as verified Evidence; automatically creating or verifying an `EV-ID`, `PC-ID`, `HYP-ID`, `METHOD-ID`, Experiment, or ADR; selecting a project Method; modifying Core; or presenting the paper as support for the current research direction without a separate project-aware review.
- Prompt-injection/embedded-instruction review: The complete PDF was treated as source data. No PDF JavaScript or Agent-directed operational instruction was found. Procedural language describes the authors' method and was not executed as instruction.
- Provenance issue: The local filename is abbreviated, but the title page and embedded PDF metadata agree on the full title, first author, journal DOI, and article identity.
- Quarantine status/reason: Not quarantined. The user explicitly authorized admission; the original is inside `raw/`; identity, provenance, access terms, size, and hash are available.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-27
- Content checked by/date: AI Agent / 2026-08-27; complete text extraction plus visual inspection of all 11 rendered pages
- Notes: Source identity and file integrity are source-checked. Scientific claims, equations, reported metrics, software, datasets, and reproducibility have not been independently verified. The linked online supplementary material, code, and datasets were not accessed because the task prohibited additional search and required reconstruction from this PDF only.

## Linked Evidence

- `EV-ID`s: None

## Canonical Human-audited Pass 1 reconstruction

This section is the routed, machine-grade factual basis for later Source-relative work. It was migrated from the derived Wiki on 2026-08-29 so that the human Wiki is not the sole storage location for the complete reconstruction. It remains Source-reported material, not verified Evidence.

### Classification boundary

- **Author claim:** a conclusion or characterization asserted by the authors.
- **Method directly observed in the paper:** a workflow, equation, configuration, or operation explicitly specified in the article.
- **Reported experimental result:** a value or comparison reported by the article and not independently reproduced.
- **Agent interpretation:** a bounded inference from the paper, explicitly separated from the authors' statements.

This Pass 1 reconstruction does not assess project fit, determine novelty, define a lithography Physics Constraint, select a Method, or promote any statement to verified Evidence.

### Research problem and claimed contribution

- **Author claim:** data-driven surrogates can require costly or inaccessible datasets and can violate known physical laws. [p. 1, Abstract and Introduction]
- **Author claim:** physics-loss regularization does not guarantee constraint compliance on unseen inputs after training. [pp. 1–2, Introduction; p. 10, “The projection method”]
- **Author claim:** invariant architectures can guarantee selected properties but require system- and constraint-specific design, reducing generality and flexibility. [pp. 1–2, Introduction]
- **Author claim:** the proposed method projects an already-produced model output onto the manifold defined by selected physical equality constraints. [p. 1, Abstract; p. 2, Eq. (1); p. 3, Fig. 1c]
- **Author claim:** the correction is model-agnostic because it requires a point prediction and the constraint function, not a specific neural architecture. [p. 2, “Framework and workflow”]
- **Author claim:** constraints can be added or removed by changing the projection problem without retraining the base model. [p. 8, Conclusions]

### Complete demonstrated workflow

1. Generate supervised ground truth by numerically solving the coupled ODE model for each case study. [p. 2, workflow; p. 3 and p. 5, “Data generation”]
2. Train a data-only fully connected NN. Separately train a loss-based PINN with residual penalties. [p. 3, Fig. 1a–b; pp. 9–10, Eqs. (8)–(15)]
3. Evaluate the already-trained predictor $f(x;\Theta)$ for an input $x$. [p. 2, workflow step (i)]
4. Initialize the optimization variable $p$ with the raw prediction. [p. 2, workflow step (ii)]
5. Solve

$$
p^*(x)
=
\underset{p}{\operatorname{argmin}}\;
\left\|p-f(x;\Theta)\right\|_{W}^{2}
\quad\text{subject to}\quad
g(x,p)=0,
$$

where

$$
\left\|v\right\|_{W}^{2}=v^{\mathsf T}Wv,
\qquad W\succ 0.
$$

[p. 2, Eq. (1)]

6. Return the optimizer result as the corrected point prediction. The projection is repeated for every prediction, including every transition in the spring-mass rollout. [p. 2, workflow; p. 3, “Trajectory prediction”]
7. Apply the same corrector to both NN and loss-based PINN outputs, yielding NN, PINN, projected NN, and projected PINN variants. [pp. 2–4, Fig. 1 and Fig. 2; p. 6, Fig. 4]

All reported projections use $W=I$. The constrained problem uses CasADi Opti and IPOPT with solver tolerances $10^{-3}$ for spring-mass and $10^{-8}$ for plasma. [p. 10, “The projection method”]

**Agent interpretation:** the paper's physical-consistency guarantee is bounded to numerical satisfaction of the selected equality constraints and solver tolerance. It does not establish universal physical validity beyond those equations.

### Physical laws used

For the frictionless two-mass, two-spring system, the projection enforces total mechanical-energy conservation. The rollout residual is

$$
R_1=E(t)-E(0).
$$

[p. 2, Eqs. (2)–(3); p. 3, “Trajectory prediction”]

The spring loss-based PINN uses

$$
\mathcal{L}_{\mathrm{physics}}=\operatorname{MSE}(E_{\mathrm{out}},E_{\mathrm{in}}),
$$

and

$$
\mathcal{L}_{\mathrm{total}}
=
(1-\lambda_{\mathrm{physics}})\mathcal{L}_{\mathrm{data}}
+
\lambda_{\mathrm{physics}}\mathcal{L}_{\mathrm{physics}}.
$$

[p. 9, Eqs. (8)–(10)] The paper describes $E$ as kinetic plus elastic potential energy but does not print a standalone explicit expression for $E$.

For the low-temperature reactive oxygen plasma, the projection uses

$$
R_1=P-\sum_i[X_i]k_{\mathrm B}T_g,
$$

$$
R_2=I-e\,n_e v_d\,\pi R^2,
$$

$$
R_3=n_e-\sum_i[X_i^+]+\sum_j[X_j^-].
$$

[p. 5, Eqs. (5)–(7)] The PINN constructs MSE penalties for pressure, current, and quasi-neutrality and combines them with $\lambda_P$, $\lambda_I$, and $\lambda_{n_e}$. [p. 10, Eqs. (11)–(15)]

### Training, inference, gradients, and feedback

| Question | Source-faithful reconstruction | Locator |
|---|---|---|
| Where is projection applied? | **Method directly observed:** after base-model training, to each point prediction. | p. 2, workflow; p. 8, Conclusions |
| Does projection participate in base-model training? | No. Physics enters training only in the separate loss-based PINN baseline. | p. 3, Fig. 1; pp. 9–10, Eqs. (8)–(15) |
| What produces the final corrected output? | A constrained optimizer initialized from the raw neural output. | p. 2, Eq. (1) and workflow |
| Are gradients propagated through projection into $\Theta$? | Not analyzed. **Agent interpretation:** the demonstrated already-trained model is not updated from projection, so no projection-derived gradient is passed back. | pp. 2–3, workflow and Fig. 1; p. 8, Conclusions |
| Are corrected outputs reused as targets? | No corrected-target reuse is described. | p. 3, Fig. 1; pp. 8–9, Conclusions |
| Is distillation or retraining performed? | No student, distillation objective, or retraining stage is described. | p. 3, Fig. 1; pp. 8–9, Conclusions |
| Is joint training discussed? | Only as future work. | p. 9, Conclusions |

### Demonstrated inputs, outputs, and dimensionality

| Case | Input | Output | Output size | Locator |
|---|---|---|---:|---|
| Spring-mass | Current state $(x_1,v_1,x_2,v_2)$ | Next state $(x_1,v_1,x_2,v_2)$ | $4$ scalars | p. 3, “Data generation”; p. 9, “Spring-mass system” |
| Reactive plasma | Pressure $P$, current $I$, radius $R$ | $11$ species densities plus $T_g$, $T_{nw}$, $E/N$, $v_d$, $T_e$, $n_e$ | $17$ scalars | pp. 5–6, system/data sections and Fig. 4 |

**Agent interpretation:** the paper demonstrates small vector-valued outputs, not images, spatial fields, or large tensors.

### Experimental configuration

- Both cases use fully connected feed-forward PyTorch models and an $80\%/10\%/10\%$ train/validation/test split. [p. 9]
- Features use min-max normalization to $[-1,1]$; selected skewed plasma outputs also use logarithmic transforms. [pp. 3, 5, and 9]
- Spring-mass ground truth uses RK4; the default set contains $N=100{,}000$ one-step transitions with $\Delta t=50\,\mathrm{ms}$ and initial states satisfying $E<5\,\mathrm{J}$. [pp. 2–3]
- The illustrated spring trajectory has $165$ recursive steps over $8.25\,\mathrm{s}$; robustness uses $100$ initial conditions and $10\,\mathrm{s}$ trajectories. [p. 3]
- The spring network uses hidden widths $[22,98,9]$, Leaky ReLU, Adam at $10^{-4}$, and $60$ epochs. The PINN uses $\lambda_{\mathrm{physics}}=0.005$. [pp. 9–10]
- Plasma ground truth uses LoKI-B+C with $12$ species and more than $85$ processes; the default $N=1000$ inputs span $P\in[0.1,10],\mathrm{Torr}$, $I\in[5,50],\mathrm{mA}$, and $R\in[4,20],\mathrm{mm}$. [pp. 4–5]
- The default plasma network has hidden widths $[50,50]$; the reported steady-state results use an ensemble of $30$ seeded models. The PINN uses $\lambda_{\mathrm{physics}}=0.015$ with equal weight for the three laws. [pp. 9–10]

### Major reported results

All values below are paper-reported experimental results, not independently verified Evidence.

- In one illustrated spring trajectory, projected-NN RMSE falls by $49.5\%$, $71.7\%$, $21.7\%$, and $42.6\%$ for $x_1$, $v_1$, $x_2$, and $v_2$. Energy-compliance RMSE changes from $(7.99\pm0.35)\times10^{-1}\,\mathrm{J}$ to $(1.96\pm0.11)\times10^{-5}\,\mathrm{J}$. [pp. 3–4, Fig. 2]
- Across $100$ spring trajectories, mean-of-four RMSE improves for $96\%$ of NN trajectories and $97\%$ of PINN trajectories, but all four variables improve simultaneously for only $60\%$ and $61\%$. [p. 5, Table 1]
- Plasma projection reduces reported residual-law RMSE for all three laws by more than $9$ orders of magnitude. [pp. 5–6, Fig. 4b]
- For the simplest $[8,8]$ plasma network, electron-density RMSE changes from $2.55\times10^{-2}$ to $0.53\times10^{-2}$; for $[26,26]$, it falls by about $57\%$. Projection benefit becomes marginal near the high-complexity plateau. [pp. 6–7, Fig. 5]
- Across plasma dataset sizes, the aggregate $17$-output RMSE advantage is reported at approximately $2.4\%$–$2.8\%$, with larger benefits for selected outputs at small sizes. [pp. 7–8, Fig. 6]
- For $500$ plasma observations, projection takes $1.75\,\mathrm{s}$ and adds $4.33\%$ to the reported total time; mean RMSE reduction is $32.08\%$, reaching $63.86\%$ for simpler architectures. [p. 8 and p. 9, Fig. 7a]
- The paper compares an NN trained with $200$ observations ($\mathrm{RMSE}=0.050$, $4913\,\mathrm{s}$) against a projected NN trained with $50$ observations ($\mathrm{RMSE}=0.048$, $1338\,\mathrm{s}$), reporting an approximately $3.7$-fold cost reduction. [pp. 8–9, Fig. 7b]
- A spring PINN weight search over more than $10$ orders of magnitude reports no consistent improvement over $\lambda_{\mathrm{physics}}=0$ and degradation near $\lambda_{\mathrm{physics}}\approx1$. [pp. 9–10, Fig. 8]

### Explicit limitations and unresolved details

- **Author claim:** projection requires the raw output to be reasonably close to the target; a poor model can be far from the manifold, making projection ineffective or ambiguous when multiple solutions exist. [p. 2; p. 6, “Robustness”]
- **Author claim:** with sufficient model complexity and training, raw predictions can approach the target and the projection advantage becomes marginal. [pp. 6–7, Fig. 5]
- Projection is demonstrated only post-training; joint integration with training is future work. [p. 9, Conclusions]
- All experiments use $W=I$; metric selection is unresolved. [p. 10]
- Difficult high-frequency features are left for future evaluation. [p. 9]
- The paper does not establish uniqueness of Eq. (1), differentiability of the projection map, implicit differentiation, corrected-target learning, knowledge distillation, image-output scalability, or generalization beyond the two ODE-based systems.
- Exact values for every plasma output and constraint combination are plotted but not fully tabulated.
- Supplementary information, datasets, and code were not inspected in the bounded Pass 1 task.

### Human Audit gate

The user explicitly stated on 2026-08-28 that Human Audit was completed and cleared Pass 2. No standalone audit file was found. The cleared audit scope covered Eq. (1), physical-constraint signs and variables, post-training/inference behavior, the absence of correction-to-network feedback, the strongest reported results, failure/ambiguity regimes, IPOPT tolerances, and $W=I$. Later work must preserve this procedural ambiguity rather than invent a missing audit artifact.
