---
schema_version: "1.0"
id: SRC-0008
type: source-record
title: "Solver-Integrated Adversarial Attacking and Training of Neural Operators"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-and-source-check
created_by: ai
content_origin: external-source
created_at: 2026-08-30
updated_at: 2026-09-12
owner: project-lead
review_status: source-checked
tier2_review_status: agent-complete
human_audit_status: not-started
reviewed_by: AI Agent
approved_by: project-lead
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 2 item 6"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Solver-Integrated Adversarial Attacking and Training of Neural Operators

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0008_Solver_Integrated_Adversarial_Neural_Operators.pdf`
- Source type: PDF; arXiv preprint
- Author: Yifei Sun
- Publication/version date: arXiv `2510.18989v3 [cs.LG]`; 2026-07-07
- DOI: `10.48550/arXiv.2510.18989`
- Imported/registered date: 2026-08-30
- Original location: `https://arxiv.org/pdf/2510.18989v3`
- Language: English
- License/access restriction: Creative Commons Attribution 4.0 International (`CC BY 4.0`); lawful arXiv full text
- Version relationship: The approved and admitted artifact is arXiv v3. Earlier versions used the title “Towards Universal Solvers: Using PGD Attack to Improve the Generalization and Robustness of Neural Operators”; they belong to the same arXiv record. No published superseding version was verified.

## Integrity

- File size: 44,302,261 bytes
- PDF page count: 68
- Hash algorithm: SHA-256
- Content hash: `F256BE971FB78E3CFE0C1EB6FCB29EE7A0ABCD516CC714B5C5FC7CB4B790A793`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate adjacent evidence on solver-integrated model-solver error, adversarial evaluation, and solver-informed training for spatial neural operators.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow.
- Prohibited use: Treating admission as verified Evidence; misclassifying robustness training as corrected-target distillation without full-text support; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: Non-blocking title-history discrepancy recorded as a same-arXiv-record alias.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of title, method, attacks, results, cost tables, appendices, and limitations
- Notes: Integrity and exact arXiv v3 identity are source-checked. Scientific claims and reported results remain source-reported and are not independently verified Evidence.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF and manuscript page numbers coincide.

### Solver-integrated training mechanism

- Neural operator $F_\theta$ is the surrogate and numerical solver $G$ is the oracle; the paper defines error operator $E_\theta=F_\theta-G$. [PDF p. 3, Eqs. (1)–(3)]
- Three attacks distinguish changing model output, comparing attacked model output with the clean solver target, and comparing $F_\theta(x+\delta)$ with $G(x+\delta)$. Full $L_3$ differentiates the solver with respect to input perturbation $\delta$; $L_3^{\mathrm{sg}}$ blocks that solver gradient. [PDF p. 5, Eqs. (19)–(26)]
- During adversarial training, $F_\theta$ is frozen while an inner attack constructs $x_{\mathrm{adv}}$; $G(x_{\mathrm{adv}})$ is recomputed; $F_\theta$ is then updated on these adversarial solver-labelled pairs. [PDF pp. 6–7]
- This is solver-generated relabelling, not post-prediction correction. The same surrogate is fine-tuned; there is no distinct student architecture, and $G$ does not correct a raw $F_\theta$ output.
- Final surrogate inference is structurally solver-free and one-pass, while $G$ remains mandatory for adversarial training. Solver gradients occur only in the input-attack loop. No deployment gate, fallback, or trust region exists; norm-bounded projected attacks control inputs rather than repair outputs.

### Output dimensionality

- Burgers maps a 1D scalar field of length $1024$ to a final scalar field. Darcy maps a binary coefficient field on a grid with $n=85$ to a steady scalar field. Recurrent Navier–Stokes maps vorticity frames on a $256\times256$ grid. [PDF pp. 12–14, Appendix A, Eqs. (30)–(50)]
- These are high-dimensional field outputs, but the mechanism concerns solver-informed adversarial supervision rather than an output projector.

### Major reported results and trade-offs

- Table 4 reports the full $L_3$ attack as strongest among listed attacks in the shown settings; examples include Burgers $0.7262\pm0.624$ versus $L_1$ $0.0988$, and Navier–Stokes $276.760\pm44.681$ versus $118.588$ and $69.505$. [PDF p. 10, Table 4]
- Table 5 reports lower attack-loss increase and Jacobian-error metrics for $L_3$ training in selected Burgers and Darcy settings, but the Darcy baseline has the smallest $\sigma_1(J_E)$; the metrics do not uniformly agree. [PDF p. 10, Table 5]
- $L_3$ wins $48/50$ shifted Burgers datasets and $47/50$ shifted Darcy datasets, but $0/1$ on ordinary training and $0/1$ on ordinary test for both systems. This is direct Source evidence of a shifted-distribution-versus-clean trade-off. [PDF pp. 24–25, Tables 13–14]
- Navier–Stokes receives only six $L_3$ rounds and some selected generalization cases worsen. [PDF p. 68, Figure 49]

### Cost, limitations, and safe boundary

- Full $L_3$ Burgers solver-path time is $0.4463\,\mathrm{s}$ versus detached $0.1624\,\mathrm{s}$ and approximate target $0.0047\,\mathrm{s}$. One Navier–Stokes backend full path uses $5.6932\,\mathrm{s}$ and $34.30\,\mathrm{GiB}$. [PDF p. 16, Tables 6–8]
- Estimated Navier–Stokes training is $65.17$ minutes per epoch and $23$–$26$ days for 500 epochs. The authors identify solver time, gradient memory, and long reverse-mode tapes as limitations. [PDF pp. 9 and 17, Table 11]
- The paper does not establish post-output projection, exact feasibility/conservation, separate-student distillation, output-safety gating, broad systematic Navier–Stokes benefit, representation-freedom effect, or deployment speed.
- **Bounded relevance:** direct high-dimensional precedent for solver-relabelled training followed by solver-free inference, and evidence that robustness training can trade off clean accuracy. It is not the external correction $\rightarrow$ corrected-target transfer chain.

## User reading takeaway — 2026-09-12

This section records the user's requested learning memory, paraphrased by the Agent. It separates the user's methodological takeaway from the paper's implementation and does not complete Human Audit, verify claims, or select a project Method.

- **Retained methodological takeaway:** physical information can help decide which samples to train on next and determine the corresponding physical reference outcomes. Relative to the user's previously emphasized physics penalties and output correction/projection, this adds an intervention at sample selection and target construction.
- **Source-specific implementation:** in the full solver-consistent adversarial scheme, the current neural operator is fixed while input perturbations are sought that enlarge model–solver discrepancy. The numerical solver evaluates the modified input, and the same neural operator is trained on these input/reference-output pairs. This is the concrete implementation reported in SRC-0008, not proof that a solver is the only possible carrier of physical information. [PDF p. 5, Eqs. (21)–(25); PDF pp. 6–7]
- **Do not infer necessity or validation:** the paper does not establish that this project's physics integration must use a solver. It also does not validate an unspecified solver-free substitute. How to identify physically meaningful inputs, obtain their reference outcomes, and integrate this idea into lithography remains unresolved.
- **Interpretation boundary:** “new way” means an additional mechanism in the user's current understanding, not a field-wide novelty claim. This mechanism still uses losses to search for challenging inputs and train the predictor; the distinction is where physical information acts, not the absence of a loss.
- **Classification:** user learning takeaway with an unresolved project-transfer question. No solver, architecture, data-generation procedure, Hypothesis, Method, or Experiment is selected or authorized by saving this note.

