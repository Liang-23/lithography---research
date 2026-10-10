---
title: "Deep Generative Prior for First Order Inverse Optimization"
aliases:
  - "Deep Generative Prior"
  - "DGP"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-27
updated_at: 2026-08-27
review_status: source-checked
core_alignment: conflict
canonical_refs:
  - "02_Evidence/SRC-0001_Deep_Generative_Prior_for_First_Order_Inverse_Optimization.md"
source_ids:
  - SRC-0001
source_file: "raw/Deep Physics Prior.pdf"
exclude_from_synthesis: false
---

# Deep Generative Prior for First Order Inverse Optimization

## Summary

This English-language arXiv preprint presents Deep Generative Prior (DGP), a framework for first-order inverse optimization that combines a differentiable Fourier Neural Operator (FNO) forward surrogate with a conditional generative prior. It performs Langevin Dynamics (LD) over the prior's latent or design representation to search for multiple candidate inputs while discouraging adversarial or out-of-distribution designs. The paper reports case studies on 2D Darcy flow, 2D Navier-Stokes flow, and inverse lithography.

The paper's primary lithography task is inverse design and therefore falls outside this project's approved forward-only scope. This note is retained as bounded comparison context; none of the paper's claims or reported results is verified Evidence.

## Key Claims Reported by the Authors

- Directly optimizing an input through a learned forward surrogate can exploit surrogate error when the optimized input leaves the training distribution.
- DGP uses a conditional generative operator to represent a learned manifold of plausible designs and refines candidates through LD guided by the forward surrogate.
- The authors report that this approach can recover diverse solutions for ill-posed inverse problems and mitigate adversarial designs more efficiently than the compared MCMC baseline.
- For the inverse-lithography case study, the authors report an EPE violation of `0.007` and throughput of `0.4` patterns/sec for `LD (w/ Gϕ, ours)` in Table 3.

These are source-reported claims. They have not been independently reproduced, checked against code, or promoted to an `EV-####` record.

## Key Quote

> "It is important to note that practical inverse lithography depends on heuristics and approximations."

## Important Concepts and Project Boundary

- The paper trains an FNO forward surrogate, which is adjacent to the project's [[High-dimensional AI Surrogate]], but uses it to optimize inverse designs rather than to satisfy the project's end-to-end forward inference objective.
- Its lithography forward model is related to [[Forward Computational Lithography Simulation]], yet the reported task optimizes masks and is therefore outside the project's explicit exclusion boundary.
- DGP constrains optimization through a learned data manifold. That is not, by itself, verified [[Physics Knowledge Integration]] and should not be conflated with a [[Physics-defined Solution Space Projection]].
- No concept or entity page was created for DGP because the admitted material is currently useful only as a bounded source-level comparison and has not been selected as an in-scope project mechanism.

## Contradictions and Limitations

- The paper focuses on inverse design, including inverse lithography and mask optimization, while this project explicitly excludes `ILT`, mask optimization, and mask generation.
- The main lithography section defines the forward operator as `F : M → Z`, mapping a mask to a thresholded wafer pattern, while Appendix A.3 describes `Fθ` as mapping masks to aerial images. The intended output stage requires source-level clarification before any claim-level use.
- The EPE tolerance and exact metric implementation are not fully specified in the inspected text and would require verification before comparison with this project's future evaluation protocol.
- The paper states that experiment code was not publicly available at the preprint date. Reported results and reproducibility therefore remain unchecked in this project.

## Governance Traceability

- Canonical source record: `02_Evidence/SRC-0001_Deep_Generative_Prior_for_First_Order_Inverse_Optimization.md`
- Registered original: `raw/Deep Physics Prior.pdf`
- Source status: source-checked for identity, provenance, and file integrity
- Evidence status: no linked `EV-####`; all scientific claims remain unverified
- Project effect: no Core, Hypothesis, Method, Physics Constraint, Experiment, ADR, or evaluation-protocol change
