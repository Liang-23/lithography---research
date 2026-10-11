---
schema_version: "1.0"
id: METHOD-0002
type: method-design
title: "Frequency Difference Neural Interaction Graph (FD-NIG)"
lifecycle_status: draft
authority_class: working
authority_scope: candidate-method-only
created_by: human
content_origin: human
created_at: 2026-10-11
updated_at: 2026-10-11
owner: project-lead
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref: "User authorization in task request, 2026-10-11"
core_alignment: pass
method_state: candidate
source_ids: []
data_ids: [DATA-0001]
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
experiment_ids: []
decision_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: false
---

# Frequency Difference Neural Interaction Graph (FD-NIG)

## 1. Purpose and authority

FD-NIG is an independent draft candidate architecture for the project's forward computational lithography surrogate. It directly learns effective complex pairwise interactions between mask-frequency components and routes their frequency differences to an output spectrum. It remains a candidate only; this record does not select a project method, authorize an experiment, promote evidence, or freeze `DATA-0001`.

- Core requirements addressed: end-to-end forward prediction, high-dimensional representation learning, spatial-frequency behavior, and reduced inference cost relative to a high-fidelity simulator.
- Linked hypotheses and physics constraints: none currently registered. No separate `HYP-0004` is created because the present record specifies an architecture rather than a falsifiable comparative claim.
- Scope exclusions: inverse lithography, mask optimization or generation, and external inference-time filtering or optimization.
- Independent candidates: `METHOD-0001` remains unchanged. Low-rank coherent-mode learning is a separate baseline candidate; Graph Sampling, Graph Attention, and Graph Transformers are optional design mechanisms, not required combined components.

## 2. Mathematical formulation

Let the discrete mask spectrum be $M(k)$ on a finite frequency grid $mathcal{K}$. For each output difference frequency $q$ in $mathcal{Q}$, the primary architecture computes

$$
\widehat{I}(q)=\sum_{(k,l)\in\mathcal{P}_q} C_\theta(k,l,c)\,M(k)\,\operatorname{conj}(M(l)),
$$

where $\mathcal{P}_q=\{(k,l):k-l=q\}$, $C_\theta$ is a learned complex pairwise coefficient, and $c$ contains available optical and process conditions. Aggregation is complex summation over interactions routed to $q$. The predicted output spectrum is transformed to a spatial field by an explicitly recorded inverse discrete Fourier transform; a nonnegative image quantity must then be defined, for example $\widehat{I}_{\mathrm{img}}(x)=|\mathcal{F}^{-1}(\widehat{I})(x)|^2$ when the target represents intensity. This intensity interpretation is unresolved until the simulator/data contract is established.

The coefficient is produced by a shared neural message function from pair features such as frequency coordinates, condition features, and optional mask-independent positional encodings. Individual coefficients do not require ground-truth labels: supervision is applied to the final output image or its spectrum.

## 3. Interface contract

| Item | Definition | Shape | Unit / domain | Coordinate system | Status |
|---|---|---|---|---|---|
| Input mask | Spatial mask $m$ and its DFT $M(k)$ | $[N,1,H,W]$; $[N,|\mathcal{K}|]$ | normalized mask; discrete frequency bins | image pixels and integer FFT indices | DATA-0001 pairing exists; spectrum contract unresolved |
| Conditions | Optical/process vector $c$ | $[N,d_c]$ | simulator-defined | condition metadata coordinates | absent or incomplete in DATA-0001 |
| Pair features | $(k,l,k-l,c)$ and optional learned features | sparse pair list $[N,P,d_f]$ | discrete frequency indices plus condition units | FFT-index convention to be frozen | candidate design |
| Raw output | Complex spectrum $\widehat{I}(q)$ | $[N,|\mathcal{Q}|,2]$ or complex tensor | simulator output spectrum | output-frequency grid | candidate design |
| Final output | Spatial aerial/resist/wafer image | $[N,1,H_o,W_o]$ | target-specific intensity or normalized image | image pixels | target stage unresolved |

Discrete frequency indexing, FFT shift/order, grid padding, boundary convention, normalization, and Hermitian treatment must be frozen in an experiment plan before implementation.

## 4. Architecture and data flow

1. Convert the mask to a discrete spectrum $M(k)$ using a documented DFT convention.
2. Construct an explicitly sparse set of frequency pairs $\mathcal{P}\subseteq\mathcal{K}\times\mathcal{K}$; dense all-pairs evaluation is not assumed.
3. Apply a shared message function to pair and condition features to predict real and imaginary coefficient channels for $C_\theta(k,l,c)$.
4. Multiply each coefficient by $M(k)\operatorname{conj}(M(l))$ and scatter-add the complex interaction into bin $q=k-l$.
5. Convert the aggregated spectrum into the target output with the chosen inverse transform and output representation.

Sparse pair selection must be explicit: possible policies include a fixed low-frequency window, magnitude/top-$P$ mask-spectrum pairs, structured bands, or learned gates. Any data-dependent selection must define differentiability, tie handling, and train/inference consistency. Graph Sampling, Graph Attention, and Graph Transformer blocks may implement pair selection or message passing as ablations; none is mandatory to define FD-NIG.

Hermitian symmetry is not automatic for a learned complex coefficient. If a real spatial output is required, the implementation must either enforce the appropriate conjugate symmetry in the assembled spectrum, use a real-valued output construction, or document why the target is complex. A real nonnegative intensity cannot be obtained by unconstrained spectrum summation alone; an intensity/magnitude-squared, bounded output map, or simulator-defined observation operator is required.

## 5. Training behavior

- Supervision: compare the final predicted image or spectrum with the registered high-fidelity target; no coefficient-level labels are required.
- Objective: a task loss is required, with optional spectrum, edge, spatial-frequency, process-condition, or other terms defined only in a future experiment plan. No loss or weighting is selected here.
- Gradient path: gradients flow through coefficient prediction, complex multiplication, scatter aggregation, and the chosen differentiable transform/output map. Hard top-$P$ selection, quantization, clipping, or non-differentiable simulator calls require an explicit surrogate or stop-gradient rule.
- Data: `DATA-0001` is referenced but remains unfrozen; optical/process-condition coverage, target semantics, and independent train/validation/test splits are unresolved.
- Training-only correction or teacher targets: none specified. A future corrected-target or distillation procedure would require separate registration and plan controls.

## 6. Inference behavior and boundaries

Inference receives a mask and whatever optical/process conditions are available, evaluates the fixed sparse pair policy and shared message function, aggregates interactions once, and emits the selected forward output. FD-NIG is a forward surrogate: it does not optimize a mask, solve an inverse problem, or invoke an external ILT/optimization loop. Any simulator call, iterative correction, or post-processing required to produce the output would violate the intended end-to-end boundary unless the Core and a future approved plan explicitly redefine it.

Required fallback behavior is unresolved. Candidate safeguards include rejecting unsupported condition ranges, returning a documented validity flag, or falling back to a separately registered baseline; none is selected. Latency and memory depend primarily on the number of retained pairs $P$, output bins $|\mathcal{Q}|$, message width, and FFT size.

## 7. Numerical constraints and complexity

For $P$ retained pairs, message width $d$, and $Q=|\mathcal{Q}|$ output bins, coefficient prediction is approximately $O(P\,d)$ per message layer and interaction aggregation is $O(P)$. A two-dimensional FFT over an $H\times W$ grid adds $O(HW\log(HW))$ time and $O(HW)$ memory. Dense pair evaluation costs $P=|\mathcal{K}|^2$ and is generally prohibitive; the sparse policy and its worst-case bound must be recorded. Scatter accumulation must be deterministic or its nondeterminism measured.

Complex arithmetic must specify real/imaginary storage, precision, overflow/underflow handling, coefficient clipping or normalization, and accumulation precision. The implementation must define behavior for NaN/Inf, empty pair bins, duplicate pairs, out-of-range $q$, and zero or near-zero mask spectra. Nonnegative output, bounded dynamic range, and Hermitian constraints are numerical/model constraints rather than assumed consequences of the equation.

## 8. Evaluation design and baselines

Required comparisons are not yet experiments: direct image prediction, `METHOD-0001`, and a separately specified low-rank coherent-mode candidate are potential baselines. Ablations should isolate sparse-pair policy, learned coefficient versus fixed coefficient structure, condition inputs, symmetry enforcement, and output representation. Evaluation should include image/spectrum accuracy, spatial-frequency and edge behavior, process-condition response where data exist, OOD conditions, runtime, memory, and failure/validity rates. No threshold, experiment ID, or superiority claim is established by this draft.

## 9. Assumptions, failure modes, and rollback

Unresolved physical assumptions include whether the pairwise quadratic form is an adequate representation of the optical/process mapping, what output stage the spectrum denotes, whether conditions $c$ are available and sufficient, and whether target normalization preserves physical meaning. Unresolved data assumptions include `DATA-0001` provenance, target encoding, sampling, condition variation, and independent label accounting.

Failure modes include spectral aliasing and grid mismatch; incorrect FFT indexing or normalization; violation of Hermitian symmetry; negative or unbounded predicted intensity; sparse-pair bias; quadratic scaling when sparsity collapses; unstable complex coefficients; sensitivity to unseen conditions; information loss from clipping or projection; and data leakage through pair selection or normalization. A candidate rejection condition is failure to meet the predeclared accuracy/behavior/cost criteria in a future approved experiment or inability to define a valid forward output contract. Rollback is to a registered baseline candidate such as `METHOD-0001` or direct image prediction, without changing this record's candidate status.

## 10. Review checklist

- [ ] Output stage, simulator contract, units, shapes, and coordinates are frozen.
- [ ] Sparse pair selection and worst-case complexity are frozen.
- [ ] Hermitian, real-output, nonnegative-intensity, and numerical policies are specified.
- [ ] Training and inference boundaries remain separate and forward-only.
- [ ] Baselines, ablations, metrics, thresholds, and compute budget are preregistered before any experiment.
- [ ] `DATA-0001` is reviewed/frozen through its own route before use.
- [ ] No method selection or superiority claim is made without an accepted ADR and approved evidence.
