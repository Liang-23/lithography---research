---
schema_version: "1.0"
id: SRC-0003
type: source-record
title: "NewPINNs: Physics-Informing Neural Networks Using Conventional Solvers for Partial Differential Equations"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-and-source-check
created_by: ai
content_origin: external-source
created_at: 2026-08-30
updated_at: 2026-09-01
owner: project-lead
review_status: source-checked
tier2_review_status: agent-complete
human_audit_status: completed
human_audit_reviewed_by: project-lead
human_audit_approval_ref: "User Human Audit decision on P1-P4, 2026-09-01"
reviewed_by: AI Agent
approved_by: project-lead
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 1 item 3"
core_alignment: unknown
parent_source_ids: []
evidence_ids: [EV-0001, EV-0002, EV-0003]
exclude_from_synthesis: false
---

# NewPINNs: Physics-Informing Neural Networks Using Conventional Solvers for Partial Differential Equations

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0003_NewPINNs.pdf`
- Source type: PDF; arXiv preprint
- Authors: Satish Chandran, Maedeh Makki, Maziar Raissi, Adrien Grenier, Behzad Mohebbi
- Publication/version date: arXiv `2601.17207v2 [cs.LG]`; 2026-06-19
- DOI: `10.48550/arXiv.2601.17207`
- Imported/registered date: 2026-08-30
- Original location: `https://arxiv.org/pdf/2601.17207v2`
- Language: English
- License/access restriction: Creative Commons Attribution 4.0 International (`CC BY 4.0`); lawful arXiv full text
- Version relationship: The approved and admitted artifact is arXiv v2. ArXiv v1 has a different author order; no published superseding version was verified at admission.

## Integrity

- File size: 2,489,810 bytes
- PDF page count: 31
- Hash algorithm: SHA-256
- Content hash: `5CE2A9CA162CDA72019D2E3FB5021FAD170A18133179F07813F249E523299EDF`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate mechanism evidence for integrating a conventional PDE solver into neural-network training through solver-consistency on spatial solution states.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow.
- Prohibited use: Treating admission as verified Evidence; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: None affecting admission. Exact arXiv v2 identity is printed in the PDF.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of the title, pivotal workflows, equations, experiment setups, results, and limitations
- Notes: Integrity and version identity are source-checked. Pivotal claims P1-P4 completed targeted Human Audit on 2026-09-01 and are represented by verified `EV-0001` through `EV-0003`; all other claims and reported results remain source-reported unless separately verified.

## Linked Evidence

- `EV-ID`s: `EV-0001`, `EV-0002`, `EV-0003`; Human-reviewed and verified on 2026-09-01 within their recorded boundaries.

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF and printed page numbers coincide.

### Solver-consistency mechanism

- NewPINNs replaces explicit PINN residual engineering with black-box numerical-solver consistency during training. A neural field at the current state is advanced by conventional solver $S$, and the solver-evolved state enters the loss. The solver therefore participates in forward/loss computation, but backpropagation does not differentiate through $S$. [PDF p. 3, Figure 1]
- For transient systems, $S$ advances $f_{\mathrm{NN}}(t_n,\alpha)$ and the loss compares $f_{\mathrm{NN}}(t_{n+1},\alpha)$ to that partial evolution, with an initial-condition term. [PDF pp. 5–6, Eqs. (6)–(12), Algorithm 1]
- For steady systems, the network is trained toward a fixed point after $N_s\ll N_{\mathrm{inf}}$ solver or optimizer iterations. The solver response is a partial advancement, not necessarily a converged feasible solution. [PDF pp. 6–8, Eqs. (13)–(22), Algorithm 2]
- The source explicitly distinguishes this state-dependent response from fixed solver-label supervision and teacher-student distillation. [PDF pp. 8–9, Section 2.3]

### Corrected target, gradients, and deployment

- A solver-evolved target exists in a narrow dynamic sense because it is recomputed from the current network output. There is no fixed projected-target corpus. Shallow-water training is an exception that uses solver-trajectory warm-start labels for ten epochs. [PDF p. 22, Section 3.5]
- The solver response remains numerically present in $L=\lVert u_{\mathrm{NN}}-u_{\mathrm{solver}}\rVert^2$ and therefore influences parameter gradients through the loss discrepancy. The stopped path is differentiation through the solver mapping itself, i.e. the method does not use $\partial S/\partial u$. The PDF does not show a specific software-level `detach()` operation. [PDF p. 3, Figure 1; PDF pp. 6–7, Algorithms 1–2]
- The trained network directly returns spatial fields at evaluation, so the conventional solver is structurally absent from forward inference. The artifact does not report a deployment-runtime benchmark or a formal solver-removal ablation.
- No deployment gate, trust region, correction bound, or fallback solver is provided. Solver-admissible initialization, clipping, depth flooring, and warm start are training stabilizers rather than output-safety gates. [PDF p. 15, Section 3.3; PDF p. 22, Section 3.5]

### Output dimensionality and reported results

- Demonstrated outputs include a $32\times32$ 2D Fokker–Planck density; $32\times32\times3$ lid-driven-cavity velocity/pressure; $256\times64\times3$ transient cylinder flow; $64\times64\times3$ shallow water; and $32\times16\times96\times3$ 3D elasticity displacement. [PDF pp. 10, 12, 17–18, 20–23, Sections 3.1–3.6]
- Fokker–Planck error is reported below $5\times10^{-3}$ for most $\alpha$. [PDF pp. 10–11, Figures 2–3]
- Cylinder-flow RMSE at $Re=75$ is reported as $6.7\times10^{-3}$ velocity and $4.9\times10^{-3}$ pressure; across 11 Reynolds numbers, $9.9\times10^{-3}$ and $6.8\times10^{-3}$. [PDF pp. 18–19, Figures 10–12]
- Shallow-water mean full-state RMS is reported as $3.5\times10^{-3}$ across validation. The 3D elasticity mean displacement-magnitude RMS is $3.51\times10^{-2}$. [PDF p. 22, Figure 14; PDF pp. 23–25, Figures 15–16]
- Lid-cavity prose/caption says errors remain below $10^{-2}$, but the plotted velocity point near $Re=2000$ appears around $1.5\times10^{-2}$; the artifact contains this unresolved visual-text discrepancy. [PDF p. 14, Figure 7]

### Limitations and safe boundary

- The method inherits solver accuracy, stability requirements, invariant structure, and training cost. Nonlinear, nearly incompressible, or discontinuous systems may require solver-admissible initialization, normalization, or warm start. [PDF p. 25, Conclusion]
- Optimization-based training can destabilize when updates are not contractive or output scale mismatches equilibrium scale. [PDF p. 8, Section 2.2.1]
- The paper does not establish exact physical feasibility, convergence from partial steps, a controlled comparison with data-only networks or standard PINNs, representation-freedom benefit, broad OOD behavior, or inference-time safety.
- **Bounded relevance:** strong high-dimensional precedent for black-box solver feedback during training followed by direct neural inference. It is not external post-prediction projection and is not corrected-output distillation in the paper's own classification.

## Targeted Human Audit preparation — pivotal claims P1–P4

- Audit date: 2026-08-31
- Audit operator: AI Agent; original admitted PDF checked textually and visually
- Selection basis: the project lead's targeted-audit instruction identifies `SRC-0003` as a selected pivotal Source
- Audit state: Human-reviewed and completed; P1 wording corrected and P2-P4 approved by the project lead on 2026-09-01
- Scientific authority: `D:\Litho\2-3nm litho\raw\SRC-0003_NewPINNs.pdf`, arXiv `2601.17207v2`, SHA-256 `5CE2A9CA162CDA72019D2E3FB5021FAD170A18133179F07813F249E523299EDF`
- Scope: only P1–P4 below; no full-paper Human Audit and no independent replication of reported experiments

### A. Audit verdict table

| Claim | Verdict | Best locator | Confidence | Important boundary |
|---|---|---|---|---|
| P1 | `verified-with-boundary` | PDF p. 3, Figure 1; pp. 5–8, Eqs. (6)–(22), Algorithms 1–2 | High | Solver output participates in forward/loss computation and affects parameter gradients through the discrepancy, but backpropagation does not traverse $S$; no explicit `detach()` code is shown. |
| P2 | `verified-with-boundary` | PDF pp. 6–7, Algorithms 1–2; pp. 8–9, Section 2.3; p. 22, Section 3.5 | High | The main solver-consistency signal is dynamic, but shallow-water training first uses ten epochs of fixed precomputed solver trajectories. |
| P3 | `verified-with-boundary` | PDF p. 6, Eqs. (8)–(12); p. 17, Section 3.4; pp. 21–23, Sections 3.5–3.6; p. 24, Conclusion | Medium-high | Solver absence is supported structurally by the reported evaluation path; no deployment-runtime benchmark or formal solver-removal ablation is reported. |
| P4 | `verified-with-boundary` | PDF p. 8, Eqs. (21)–(22) and Section 2.2.1; pp. 10, 15, 22–23; pp. 24–25, Conclusion | High for inherited limitations and stabilizers; medium-high for audited non-support | Partial solver advancement can define a consistency residual without proving convergence or exact physical feasibility; boundary enforcement by the solver is narrower than full-solution feasibility. |

### B. Claim-by-claim verification

#### P1

**Candidate claim**

NewPINNs uses a conventional solver inside training: the current neural state is advanced by the solver and the solver response enters the loss, while gradients are not backpropagated through the solver itself.

**What the PDF actually establishes**

For transient problems, the network supplies $\hat{u}(x,t_n;\theta)$ together with boundary conditions $B[u]$, physical parameters $\alpha$, and the solver-step specification $N_s$. Solver $S$ returns $u_{\mathrm{solver}}(x,t_{n+1})$, and training compares it with $f_{\mathrm{NN}}(t_{n+1},\alpha;\theta)$ using a discrete $L_2$ loss. For steady problems, $f_{\mathrm{NN}}(\alpha;\theta)$ is used as the solver/optimizer initial state; $S$ returns the state after $N_s$ iterations, and the loss compares the original network field with that returned state. Thus $u_{\mathrm{solver}}$ participates numerically in the loss and affects the resulting parameter gradient. Figure 1 and the inverse formulation establish the narrower boundary that the external solver is treated as non-differentiable: backpropagation does not compute $\partial S/\partial u$.

**Best supporting locator(s)**

- PDF p. 3, Figure 1 and caption.
- PDF p. 5, Eqs. (6)–(10).
- PDF p. 6, Eqs. (11)–(15) and Algorithm 1.
- PDF p. 7, Algorithm 2 and Eqs. (16)–(19).
- PDF p. 8, Eqs. (20)–(23), Section 2.2.2.

**Mechanism / textual basis**

The figure caption is an explicit author statement about the gradient boundary. Eqs. (7)–(10) and Algorithm 1 show current-state input, solver advancement, returned state, and loss use for transient systems. Eq. (15) and Algorithm 2 show the analogous steady fixed-point residual. The loss has the form $L=\lVert u_{\mathrm{NN}}-u_{\mathrm{solver}}\rVert^2$: the solver value influences optimization, while the stopped path is differentiation through $S$. A specific PyTorch `detach()` implementation is neither shown nor required by the paper-level claim.

**Boundary / non-support**

The PDF does not establish that gradients are backpropagated through $S$, does not specify a software-level `detach()` operation, and does not make NewPINNs an external post-prediction projection method. The solver response still affects gradients through its numerical value in the loss. For steady problems, $N_s\ll N_\infty$ means the returned state can be a partial advancement rather than a converged solution.

**Recommended final Evidence wording**

In the reported NewPINNs training loop, the solver participates in forward/loss computation by advancing the current neural field and supplying the dynamic response in $L=\lVert u_{\mathrm{NN}}-u_{\mathrm{solver}}\rVert^2$, but gradients are not backpropagated through the solver mapping itself; the PDF shows no specific `detach()` implementation.

#### P2

**Candidate claim**

The main NewPINNs solver response is recomputed from the current network prediction during training rather than supplied as a fixed solver-label corpus, and the authors distinguish this from conventional supervision and teacher–student distillation.

**What the PDF actually establishes**

Algorithms 1–2 place network prediction and the subsequent solver call inside the epoch/parameter loops. Section 2.3 explicitly calls the solver response dynamic and state-dependent because it depends on the network's current prediction, and contrasts this mechanism with fixed precomputed solver trajectories and fixed teacher outputs. The target therefore changes when the current network field changes.

**Best supporting locator(s)**

- PDF pp. 6–7, Algorithms 1–2.
- PDF pp. 8–9, Section 2.3.
- PDF p. 22, Section 3.5.

**Mechanism / textual basis**

The repeated algorithmic sequence is $\hat{u}\leftarrow f_{\mathrm{NN}}$, $u_{\mathrm{solver}}\leftarrow S[\hat{u},\ldots]$, followed by a discrepancy loss. Section 2.3 explicitly says no static target is used in the principal solver-consistency mechanism and that the solver is not a fixed teacher.

**Boundary / non-support**

The shallow-water experiment is an explicit exception: it begins with ten epochs of direct regression onto precomputed solver trajectories for $16$ parameter values, then switches to solver-consistency training over $256$ parameter values. The paper's distinction from distillation is an author-defined conceptual distinction, not a controlled empirical comparison against teacher–student distillation.

**Recommended final Evidence wording**

NewPINNs' principal consistency target is recomputed from the network's current prediction during training rather than drawn from a fixed label corpus; the shallow-water experiment nevertheless uses a bounded ten-epoch solver-trajectory warm start before the dynamic solver-consistency phase.

#### P3

**Candidate claim**

The conventional solver participates during training, while the trained neural network directly produces spatial fields in the reported forward evaluation path without a solver call in that prediction path.

**What the PDF actually establishes**

The methodology defines transient predictions as $f_{\mathrm{NN}}(t,\alpha;\theta)$ and steady predictions as $f_{\mathrm{NN}}(\alpha;\theta)$, each returning the spatial solution field. Experimental sections describe feeding physical parameters, geometry/masks, and—where transient—time into trained U-Nets, then comparing their predicted fields against independently generated solver references. The reported evaluation path therefore uses the trained network as the forward predictor; the solver appears as a reference generator, not as a required post-processing component of the reported prediction.

**Best supporting locator(s)**

- PDF p. 6, Eqs. (8)–(12) and the paragraph preceding Algorithm 1.
- PDF p. 12, Section 3.2, direct Reynolds-number-to-field U-Net mapping.
- PDF pp. 17–18, Section 3.4, Reynolds number, geometry, and time to velocity/pressure fields.
- PDF pp. 21–22, Section 3.5, time and dam-height inputs to depth/momentum fields and evaluation against independent solver references.
- PDF pp. 23–24, Section 3.6 and Conclusion, direct Poisson-ratio/geometry-to-displacement mapping and an amortized parameter-to-solution map.

**Mechanism / textual basis**

This is supported by the defined network mappings and by the separate roles assigned to prediction and reference fields in the evaluation sections. The paper does not present a separate inference algorithm that explicitly says “solver disabled,” so solver absence is a structural reading of the reported forward evaluation path rather than a dedicated ablation result.

**Boundary / non-support**

The PDF does not report deployment latency, speedup, production cost, or a solver-removal ablation. Reference solutions are still generated by numerical solvers for accuracy evaluation. The evidence supports direct neural inference structurally, not a proved deployment-acceleration claim or inference-time safety claim.

**Recommended final Evidence wording**

In the reported forward evaluations, trained NewPINNs models directly map physical parameters and, where applicable, time and geometry inputs to spatial solution fields; the conventional solver is not shown in the forward prediction path, but the paper provides neither a runtime benchmark nor a formal solver-removal ablation.

#### P4

**Candidate claim**

NewPINNs training inherits material solver properties and costs and may require stabilization; the paper does not establish deployment-time safety or exact feasibility from a partial solver advancement.

**What the PDF actually establishes**

The conclusion explicitly states that NewPINNs inherits the solver's accuracy, stability requirements, invariant structure, and computational cost. Section 2.2.1 states that optimization-based training inherits optimizer convergence/stability and can become degenerate when the update is non-contractive or the output scale is mismatched. The experiments document Kaiming/admissible initialization, normalized inputs, gradient clipping, clamping the advection state to $[-3,3]$, a positive depth floor before shallow-water solver calls, and a ten-epoch solver-trajectory warm start.

**Best supporting locator(s)**

- PDF p. 8, Eqs. (21)–(22) and the following stability/scaling discussion.
- PDF p. 10, Section 3.1, solver-compatible initialization and normalized inputs.
- PDF p. 15, Section 3.3, gradient clipping and state clamping to $[-3,3]$.
- PDF p. 22, Section 3.5, warm start, positive depth floor, and gradient clipping.
- PDF p. 23, Section 3.6, five training-time solver iterations versus a tight-tolerance reference solve.
- PDF pp. 24–25, Conclusion.

**Mechanism / textual basis**

The inherited-limitations statement is explicit. The stabilization measures are reported experimental procedures. Eqs. (15) and (21) use $N_s\ll N_\infty$ or a small number of optimizer steps; the 3D elasticity experiment uses five preconditioned conjugate-gradient steps for consistency but a solver run to tolerance $10^{-8}$ for evaluation references. These establish a distinction between a consistency response and a converged reference solution.

**Boundary / non-support**

The audited method, algorithm, experiment, and conclusion sections do not provide an inference-time safety gate, accept/reject mechanism, trust region, fallback solver, or formal guarantee that a finite partial advancement is a converged physically feasible solution. The solver can enforce boundary conditions or admissible-variable requirements during its own call, but that is not a proof that the network's final output satisfies the full PDE/equilibrium system exactly.

**Recommended final Evidence wording**

NewPINNs explicitly inherits accuracy, stability requirements, invariant structure, and training cost from its numerical solver and uses problem-specific stabilization in difficult experiments; its partial solver-consistency steps do not establish an inference-time safety mechanism or exact converged feasibility of the final neural output.

### C. EV candidate recommendation

| Claim | Create EV | Disposition |
|---|---|---|
| P1 | yes | Drafted as `EV-0001`. |
| P2 | merge | Merged into `EV-0001` because dynamic state dependence is part of the same black-box solver-feedback mechanism; the warm-start exception is retained. |
| P3 | yes | Drafted as `EV-0002`. |
| P4 | yes | Drafted as `EV-0003`; negative safety/feasibility statements are recorded as boundaries rather than standalone absence Evidence. |

All three records were promoted to `verified` only after the project lead reviewed P1-P4 on 2026-09-01, corrected P1, and approved the remaining boundaries.

#### Proposed EV — `EV-0001`

- Proposed title: State-dependent black-box solver feedback in NewPINNs training
- Atomic claim: the current neural field is advanced by a black-box solver during training; the returned state participates in the dynamic consistency loss, but backpropagation does not differentiate through the solver mapping.
- Source ID: `SRC-0003`
- Exact locator: PDF p. 3, Figure 1; pp. 5–9, Eqs. (6)–(22), Algorithms 1–2, Section 2.3; p. 22 warm-start exception.
- Support type: explicit author statement plus algorithm/equation mechanism.
- Boundary / non-support: no explicit detach notation; not fixed corrected-output distillation; shallow-water uses a bounded fixed-label warm start.
- Confidence: High.
- Project importance: establishes a training-time black-box physics-feedback precedent without requiring differentiation through the solver.

#### Proposed EV — `EV-0002`

- Proposed title: Direct neural field prediction in the reported NewPINNs evaluation path
- Atomic claim: reported forward evaluation uses the trained neural network to directly produce spatial fields without showing the conventional solver in the forward prediction path.
- Source ID: `SRC-0003`
- Exact locator: PDF p. 6; pp. 12, 17–18, 21–24; Conclusion.
- Support type: method definition plus experimental evaluation structure.
- Boundary / non-support: no runtime benchmark, solver-removal ablation, deployment proof, or inference-safety result.
- Confidence: Medium-high.
- Project importance: supports the narrower architecture precedent of training-time solver coupling followed by direct neural prediction.

#### Proposed EV — `EV-0003`

- Proposed title: Solver-inherited limitations and stabilization in NewPINNs
- Atomic claim: NewPINNs inherits solver accuracy, stability requirements, invariant structure, and computational cost, and difficult experiments use solver-compatible initialization, normalization, clipping, flooring, or warm start.
- Source ID: `SRC-0003`
- Exact locator: PDF p. 8; pp. 10, 15, 22–25.
- Support type: explicit conclusion statement plus reported experimental procedures.
- Boundary / non-support: partial solver advancement does not prove exact feasibility; no deployment gate or fallback solver is reported.
- Confidence: High for the positive claim; medium-high for the audited absence boundary.
- Project importance: prevents treating solver feedback as a cost-free or universally safe correction mechanism.

### D. Human attention resolution

1. Resolved on 2026-09-01: P1 now states that solver output participates in forward/loss computation and affects parameter gradients through the discrepancy, while backpropagation does not traverse $S$. No claim is made that the authors used the PyTorch `detach()` function.
2. Resolved on 2026-09-01: P2 retains the shallow-water warm-start exception; P3 remains a structural forward-path claim rather than a speedup claim; P4 retains the exact-feasibility and inference-safety boundaries.

### E. Final pivotal judgment

`retain as pivotal with narrowed role`

`SRC-0003` is strong source-level precedent for dynamic, training-time black-box solver feedback followed by direct neural field prediction. Its role must remain narrower than external post-prediction projection, fixed corrected-target distillation, formal feasibility, deployment-time safety, or lithography-specific validation.
