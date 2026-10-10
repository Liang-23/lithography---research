---
schema_version: "1.0"
id: SRC-0007
type: source-record
title: "Hard conservation correctors can hide a degrading model when training autoregressive emulators"
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
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 1 item 10"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Hard conservation correctors can hide a degrading model when training autoregressive emulators

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0007_Hard_Conservation_Correctors.pdf`
- Source type: PDF; arXiv preprint
- Authors: William E. Chapman, John S. Schreck, Yingkai Sha
- Publication/version date: arXiv `2607.18416v1 [physics.ao-ph]`; 2026-07-20
- DOI: `10.48550/arXiv.2607.18416`
- Imported/registered date: 2026-08-30
- Original location: `https://arxiv.org/pdf/2607.18416v1`
- Language: English
- License/access restriction: Creative Commons Attribution 4.0 International (`CC BY 4.0`); lawful arXiv full text
- Version relationship: The approved and admitted artifact is arXiv v1; no other version was verified at admission.

## Integrity

- File size: 892,956 bytes
- PDF page count: 12
- Hash algorithm: SHA-256
- Content hash: `0A1E76388DC0D3C70EB9F42B72DA0FBA1C8F358A04CA184DFD8DFAC2FA51E38A`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate failure-mode evidence on corrected-output supervision, raw-model drift, correction magnitude, and safeguards in a high-dimensional autoregressive weather emulator.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow.
- Prohibited use: Treating admission as verified Evidence; universalizing a single conservation-corrector failure mechanism; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: None affecting admission; exact arXiv v1 identity is printed in the PDF.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of equations, Figures 1–3, results, discussion, limitations, and numerical-precision appendix
- Notes: Integrity and version identity are source-checked. Scientific claims and reported results remain source-reported and are not independently verified Evidence.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF and manuscript page numbers coincide.

### Raw model, corrector, and gradient mechanism

- CAMulator v2 predicts six-hour global atmospheric states on a nominal $1.0^\circ$ grid with 32 hybrid-sigma levels; decoder blocks are fine-tuned while the backbone is frozen. The exact horizontal tensor dimensions are not printed. [PDF p. 2, Section 2.1]
- For raw precipitation field $P$ and budget-required global precipitation $Q$, the hard corrector is

$$
C(P)=Q\frac{P}{\mathbf{1}^{\mathsf T}P}.
$$

It preserves normalized spatial pattern while replacing global amplitude. [PDF p. 6, Eq. (1), Section 3.2; PDF pp. 9–10, Eqs. (4)–(6)]
- The production failure configuration evaluates supervised loss only after correction and has no raw-imbalance penalty. The remedy supervises the pre-correction output and adds $0.1(r-1)^2$, while retaining hard correction for the delivered field. [PDF pp. 3–4, Figure 1; PDF pp. 9–10, Eqs. (6)–(7)]
- Scale invariance gives $C(\alpha P)=C(P)$ and $J_C(P)P=0$, so corrected-output loss supplies no restoring gradient in the uniform raw-amplitude direction. The paper generalizes this risk to directions $v$ with $J_C(\hat x)v=0$. [PDF p. 6, Eq. (1); PDF p. 8, Eq. (2)]
- The corrector remains in the delivered inference path and corrected states feed back autoregressively. No second student or distillation stage removes it.

### Reported failure and safeguard evidence

- Over 18 epochs with corrected-output supervision and no imbalance penalty, required correction grows from $2.4\%$ to $24.1\%$ while delivered budget closure remains at machine precision; raw global precipitation error worsens from $-4.0\%$ to $-19.8\%$. [PDF pp. 4–5, Section 3.1, Figure 2]
- A second run peaks above $60\%$ correction while mass/energy corrections remain near $0.01\%$. [PDF p. 5, Figure 2d]
- A direct scale test over $\alpha\in\{0.5,0.75,1,1.25,1.5\}$ leaves the corrected field and corrected loss unchanged to machine precision while raw loss and the penalty respond. [PDF p. 6, Section 3.2]
- Switching to pre-correction supervision plus penalty lowers the correction from $24\%$ to below $1\%$ within one epoch. The authors state that reduced correction is necessary but not sufficient evidence of a better model and do not measure raw-field forecast skill. [PDF pp. 6–7, Section 3.3]
- In the short $2\times2$ ablation, runaway occurs only with corrected supervision and no penalty. Corrected supervision plus a penalty and both pre-correction-supervision variants remain near zero correction. [PDF p. 7, Section 3.4, Figure 3]
- Suggested safeguards are diagnostic/training measures: supervise raw output, penalize raw imbalance, and monitor raw residual, $|r-1|$, and both raw and corrected skill. There is no trust region, accept/reject gate, correction cap, or fallback. [PDF pp. 8–10]

### Limitations and safe boundary

- The paper explicitly does **not** show that the delivered corrected product degrades. It demonstrates hidden raw-model degradation in one degree of freedom under a specific gradient-nullspace configuration. [PDF p. 8, Discussion]
- Evidence is from one emulator and one water-budget corrector. The production remedy changes two factors together; the factorial ablation is short and within-run. Raw forecast skill and long free-running stability are not measured. [PDF pp. 7–9]
- Bfloat16 global reductions distort correction diagnostics; the reported error averages $0.22\%$ and reaches $0.52\%$ over 30 steps. [PDF p. 10, Appendix A.1]
- The manuscript states it is under review and is not established as peer reviewed. It does not study hidden-representation freedom, lithography, correction-to-student transfer, runtime, or spatial edge/frequency preservation.
- **Bounded relevance:** direct evidence that corrected-output supervision can create a gradient nullspace and hide raw-model drift, plus concrete monitoring/training safeguards. It is not evidence that every corrector harms delivered outputs.

## User reading takeaway and raw idea — 2026-09-12

This section records the user's requested learning memory, paraphrased by the Agent. It is not a paper claim, Human Audit completion, verified Evidence, or project Method selection.

- **Retained takeaway:** distinguish a module correcting the neural prediction from the neural network learning to avoid that error through training. A physically corrected delivered output does not establish the latter.
- **Reading preference:** the user finds the source relevant to spatial physical-field prediction, but its global correction mechanism adds limited new method insight for their current reading purpose. Deeper reading is deferred; retain the diagnostic distinction above. This is the user's reading assessment, not a field-wide novelty or validity judgment.
- **Analogy boundary:** the user relates state-to-state field prediction to mask-to-lithography-output prediction. This is an input/output analogy, not equivalence of physical dynamics, constraints, or discretizations. CAMulator predicts multivariable atmospheric states with vertical levels; the precipitation field studied here has a horizontal spatial grid. The source does not establish lithography diffraction equations or intermediate lithography states.
- **Correction clarification:** the precipitation corrector applies one global scalar multiplier to every location, preserving normalized spatial pattern. Grid-cell area weights in global integration are not learned pixel-specific correction weights. The budget-required total is calculated from predicted evaporation and storage tendency; it is not a universally fixed constant or an inference-time reference answer. [SRC-0007, PDF p. 6 Eq. (1), pp. 9–10 Eqs. (4)–(5)]
- **Classification: raw user idea / unresolved question; speculative, not selected.** The user suggests exploring distillation to transfer physics-informed capability and potentially remove a training dependency. This is related to the candidate transfer family already in Core, but no new architecture, Hypothesis, or Method is specified or approved. PADM's bounded precedent is privileged CT-conditioned attention/representation transfer and removal of Teacher/CT; the Student's iterative diffusion and internal physics-aware path remain (SRC-0004; EV-0004–EV-0006). Whether distillation can remove a corrector while retaining useful capability remains untested here. SRC-0007 itself performs no such distillation.

