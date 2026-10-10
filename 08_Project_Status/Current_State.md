---
schema_version: "1.0"
id: PROJECT-STATE
type: project-status
lifecycle_status: active
authority_class: derived
authority_scope: current-status-summary-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User request on 2026-08-26"
review_status: pending-user-review
reviewed_by:
approved_by:
approval_ref:
created_at: 2026-08-26
updated_at: 2026-09-21
core_alignment: pass
source_ids: [SRC-0001, SRC-0002, SRC-0003, SRC-0004, SRC-0005, SRC-0006, SRC-0007, SRC-0008, SRC-0009, SRC-0010, SRC-0011, SRC-0012, SRC-0013]
data_ids: [DATA-0001]
hypothesis_ids: [HYP-0001, HYP-0002, HYP-0003]
method_ids: [METHOD-0001]
experiment_ids: [EXP-0001, EXP-0002]
decision_ids: [ADR-0001, ADR-0002, ADR-0003, ADR-0004]
exclude_from_synthesis: false
---

# Current State

## Current phase

`Candidate Architecture 3 kernel-prediction method and blocked feasibility-plan preparation; external MetalSet data registered but unfrozen; no Method selected or Experiment authorized`

On 2026-09-21 the latest architecture figure was translated into candidate records `METHOD-0001`, `DATA-0001`, and draft-blocked `EXP-0002`. The candidate keeps the reference branch and postpones the correction branch. Its first proposed implementation is `x_t, mask m, timestep t, optical condition alpha -> conditioned U-Net -> predicted kernel tensor B -> differentiable FFT renderer -> clean-image estimate`.

The external `D:\project\lithobench-main` audit found reusable direct-image data/training infrastructure and a tiny `Stage4SmokeUNet`, but no conditioned kernel-prediction U-Net or optical renderer. The external production U-Net module is empty. Existing kernel-like files have unknown semantics and are not integrated.

This is a preparation update only. `alpha` is absent from DATA-0001; the first plumbing test would use a documented constant and cannot test condition generalization. The exact `B` tensor contract, multi-kernel count/combination rule, FFT conventions, simulator contract, and Stage 2 physical constraint remain unresolved. No experiment has run and no scientific claim has been promoted.

On 2026-09-13, the user explicitly requested implementation of a bounded literature-to-hypothesis plan. BG-0002 and three draft Hypothesis records now capture the comparison questions for conditional diffusion, correction knowledge transfer, and high-fidelity label efficiency. The user's preference gives conditional diffusion with U-Net priority for investigation; it does not select an architecture or establish performance. The corresponding Chinese Wiki synthesis and PADM/ΠNet reading records expose the distinctions and missing conditions. All three Hypotheses remain draft and untested; no concrete lithography formula, dataset, simulator, Method, numerical threshold, or new Experiment was selected.

The registered corpus remains SRC-0001 through SRC-0013 (13 Sources). The user's reference to a fourteenth article is unresolved; no additional Source was inferred. Conversational mechanism reading does not change Human Audit or Evidence status.

Following the user's same-day reading feedback, the Chinese synthesis was reorganized around the existing Core flow from neural prediction to output correction, knowledge transfer, and independent deployment. BG-0002 and HYP-0002 record the user's output-stage preference, clarification that the proposed parameters are few physical parameters, and unresolved image-generation interfaces. This completes an explanatory/navigation revision only; all three Hypotheses remain draft, and no Method or physical relationship has been selected.

The project has an approved high-level research frame and requirements. On 2026-08-27, the user completed `NA-0005` and accepted the current governance structure and ownership boundaries. Governance remains canonical, the Wiki remains a downstream derived Markdown projection without scientific authority, and Obsidian Native Graph View visualizes actual `[[wikilinks]]`.

The approved three-topic literature campaign admitted eleven additional papers as `SRC-0003` through `SRC-0013`. Their canonical Source records contain Agent-complete Tier 2 full-text ingestion with exact locators and limitations. `SRC-0003` and `SRC-0004` have completed targeted project-lead Human Audits for pivotal claims P1-P4. The project lead explicitly approved `EV-0004` through `EV-0006` on 2026-09-01, and all three are verified within their recorded boundaries. `SRC-0005` through `SRC-0013` remain `human_audit_status: not-started` unless separately updated through their own audit workflow.

Human-readable Wiki source digests for all eleven Sources, three topic syntheses, and the cross-paper architecture/occupancy map have been projected and registered in `wiki/index.md` and `wiki/log.md`. The verified, bounded meaning of `EV-0001` through `EV-0003` is projected into the existing NewPINNs notes, and `EV-0004` through `EV-0006` are projected into the existing PADM source note, transfer concept/synthesis, and architecture/occupancy map without creating duplicate Wiki nodes. These Wiki artifacts remain derived navigation and synthesis; their authority comes only from the cited verified Evidence, not from Wiki placement or Graph prominence.

`EV-0001` verifies the bounded training-time mechanism: solver output participates in forward/loss computation, while backpropagation does not differentiate through the solver mapping. `EV-0002` verifies direct neural field prediction in the reported evaluation path without proving runtime speedup. `EV-0003` verifies solver-inherited limitations and reported stabilization measures without establishing exact feasibility or inference-time safety. These Evidence records do not establish lithography validity, select a Method, or change persistent scientific defaults.

`EV-0004` verifies privileged CT-conditioned attention/representation transfer to a NAC-only Student without corrected-output labels. `EV-0005` verifies internal attenuation-factor computation during diffusion without establishing exact constraint satisfaction or physical validity of learned fields. `EV-0006` verifies Teacher/CT removal from inference while iterative diffusion and the Student physics-aware path remain, without one-pass or measured-speedup proof. These Evidence records are Source-relative to PADM and do not establish lithography validity or select a project Method.

No specific physical constraint, data/simulator contract, implementable Method, or formal preregistered Experiment has been selected. `EXP-0001` is a draft/blocked planning record only and is not approved for execution.

## Administrative and Wiki status

- `NA-0005` governance and Wiki synchronization review: completed with explicit user confirmation on 2026-08-27.
- Project-specific root `AGENTS.md`: active and accepted as the project-wide Agent/governance owner.
- `Core_Governance.md`: confirmed as the canonical owner of the detailed Core Modification Gate; no Locked Core content was changed by this administrative update.
- `Context_Router.md`: accepted as the canonical owner of task-specific context routing.
- `Wiki_Workflow.md`: accepted as the canonical owner of detailed Wiki operations.
- Current State and Next Action remain the canonical administrative status records.
- Background, Source, Data, Evidence, Physics Constraint, Hypothesis, Method, Experiment, Decision, Quarantine, and Archive control layers: present.
- Useful legacy Wiki behavior—semantic ingestion, source/concept/entity notes, language preservation, query, review, overview synthesis, and integrity checks—has been reintegrated under current Governance.
- `wiki/` is the semantically derived human-readable layer; Governance IDs and canonical paths provide non-clickable traceability, while Wiki-internal `[[wikilinks]]` provide semantic navigation. Link-only projection and cross-plane Graph edges are now explicitly forbidden.
- Obsidian Native Graph View reads Markdown links directly. No custom rendering command is required.
- Rejected custom Graph proposal `ADR-0001`: retained as rejected for decision history.
- Accepted administrative architecture `ADR-0002`: Obsidian-native Wiki Graph.
- Accepted governance responsibility correction `ADR-0003`: one canonical owner per governance concern, ADRs limited to strategic/persistent decisions, and experiment-local Method testing governed by preregistered Experiment Plans.
- Governance workflow simulations completed: bounded source admission, blocked experiment-local planning, and a strategic ADR approval checkpoint. Each simulation preserved its authority boundary; no scientific claim or project default was promoted.
- Former `09_Knowledge_Graph/` module and empty `Relationship_Registry.yaml`: archived under `ARC-0001`; no accepted relationship data existed.
- `.obsidian/graph.json`: preserved as Obsidian's native display-settings file, with its search scoped to `path:wiki -file:index -file:log`; deterministic health now fails if this scope drifts or a Graph-producing link crosses the canonical/Wiki boundary.
- Initial Core-to-Wiki projection: `wiki/overview.md` plus seven concept notes linked from `wiki/index.md`.
- Three-topic literature campaign: eleven approved papers were lawfully acquired, registered, and admitted as `SRC-0003` through `SRC-0013`; all eleven canonical records are `tier2_review_status: agent-complete`. `SRC-0003` and `SRC-0004` targeted P1-P4 Human Audits are completed, and `EV-0001` through `EV-0006` are verified within their recorded Source-relative boundaries; the other nine Sources remain not started unless separately audited.
- External source Wiki notes: derived human digests exist for `SRC-0001` through `SRC-0013`. The `SRC-0003` through `SRC-0013` digests, three topic syntheses, and cross-paper architecture/occupancy map are indexed and logged. NewPINNs displays the verified boundaries from `EV-0001` through `EV-0003`, and PADM displays the verified boundaries from `EV-0004` through `EV-0006`; other claims retain their recorded Source-reported or unverified status. The complete Human-audited Pass 1 reconstruction for `SRC-0002` is stored in its canonical Source record, while the draft `BG-0001` comparison is semantically projected into a separate human-facing Wiki synthesis.
- Wiki bookkeeping: the earlier source reconciliation passed at its recorded date. The 2026-09-13 structural baseline has 15 pre-existing unresolved links to `High-dimensional AI Surrogate`; no cross-plane edges or Graph-scope errors were reported. These links were not repaired by creating speculative content.
- PADM-focused synthesis: BG-0002 and HYP-0001–HYP-0003 are draft records created under the explicit 2026-09-13 plan request; their human-readable explanation is projected into a Chinese Wiki synthesis. Source-language digests and existing Evidence states are preserved.

## Locked research frame

According to `00_Project_Core`:

- Task: forward computational lithography simulation.
- System: end-to-end high-dimensional AI surrogate.
- Core question: integrate physical knowledge while preserving neural representation capability.
- Data condition: limited high-fidelity advanced-node lithography data.
- Inference boundary: no required external filtering or post-processing module.
- Explicitly out of scope: `ILT`, mask optimization, mask generation, gradient trust certification.

The migration did not modify `Project_Overview.md`, `Research_Requirement.md`, or `Core_Governance.md`.

## Candidate families recorded in Core

These are candidate research directions, not selected or validated Methods:

- Output-level physical correction.
- Physics-defined solution space projection.
- Projection-based knowledge distillation.
- Event-triggered correction for non-differentiable or discontinuous physical relationships.

The derived Wiki preserves this candidate status.

## Unresolved scientific definitions

- Exact physical relationship $R(x,y)$.
- Valid solution set and correction/projection operator.
- Variables, units, tensor shapes, coordinate system, and output stage to constrain.
- Training-time versus inference-time correction behavior.
- Dataset and high-fidelity simulator provenance.
- Sample budget defining `limited data`.
- Split and OOD/process-condition protocol.
- Baselines, ablations, metrics, and success thresholds.
- Architecture and implementation.

## Registers, decisions, and experiments

- Registered sources: `SRC-0001` — *Deep Generative Prior for First Order Inverse Optimization*; source-checked for identity/integrity, with claims unverified and use bounded by the forward-only Core scope.
- Registered sources: `SRC-0002` — *Physics-consistent machine learning with output projection onto physical manifolds*; source-checked for identity/integrity, with its Human-audited Pass 1 reconstruction stored canonically and all scientific claims still unverified.
- Registered sources: `SRC-0003` through `SRC-0013` — the eleven project-lead-approved papers in the three-topic literature campaign; all are formally admitted and source-checked, and their Tier 2 Agent reviews are complete. `SRC-0003` and `SRC-0004` have completed targeted P1-P4 Human Audits; `SRC-0005` through `SRC-0013` remain unaudited.
- Registered data/simulators: `DATA-0001` is registered but unfrozen; no simulator contract is accepted.
- Verified Evidence: `EV-0001` (dynamic black-box solver response participates in loss; no backpropagation through $S$), `EV-0002` (direct neural field prediction in the reported evaluation path, without runtime proof), `EV-0003` (solver-inherited limitations and stabilization, without exact-feasibility or inference-safety proof), `EV-0004` (privileged CT-conditioned attention transfer to a CT-free Student), `EV-0005` (internal physics-aware attenuation-factor computation during diffusion), and `EV-0006` (privileged-input removal while iterative diffusion and the Student physics-aware path remain).
- Physics Constraints: none registered.
- Hypotheses: HYP-0001, HYP-0002, and HYP-0003 are registered as draft only; each records variables, conceptual comparisons, rejection conditions, and missing prerequisites. None is ready-to-test or supported.
- Method Designs: `METHOD-0001` is registered as a draft candidate only; no Method is selected.
- Formal Experiments: `EXP-0001` and `EXP-0002` are draft/blocked planning records only and have no execution authority.
- Accepted ADRs: `ADR-0002` (administrative Wiki/Obsidian architecture) and `ADR-0003` (governance responsibility and strategic/experiment decision boundary).
- Rejected ADRs: `ADR-0001` (custom relationship registry and Graph projection).
- Proposed ADRs: `ADR-0004` remains proposed, unapproved, and without effect on the current simulator state.
- Active separate relationship registries: none.
- Wiki source pages: derived human digests exist for `SRC-0001` through `SRC-0013`; the three campaign-topic syntheses and cross-paper architecture/occupancy map also exist. NewPINNs-related notes now expose the bounded verified state of `EV-0001` through `EV-0003`; the Wiki itself remains non-authoritative.

## Current blockers

1. `SRC-0003` and `SRC-0004` targeted P1-P4 Human Audits and their `EV-0001` through `EV-0006` verification are complete, but the remaining pivotal-Source set and audit order have not been fully recorded; `SRC-0005` through `SRC-0013` remain unaudited.
2. Verified `EV-0001` through `EV-0003` are bounded to NewPINNs' reported PDE/solver settings and do not establish a lithography relationship, universal solver-feedback superiority, deployment acceleration, exact feasibility, or inference-time safety.
3. No `PC-####` specification exists for a computable output constraint.
4. `DATA-0001` is registered but no Data or Simulator Contract is frozen or accepted.
5. `EXP-0001` remains a separate draft/blocked SSIM-ablation record and `EXP-0002` is a new draft/blocked Architecture 3 preparation record. Neither is approved. No experiment can be executed until the relevant Hypothesis, Method, Data/simulator, applicable Physics Constraint, baseline, split, metric/threshold, implementation, budget, stopping, and artifact prerequisites are supplied.
6. For HYP-0001–HYP-0003, the first output stage, physical relationship, reference provenance, label-accounting rules, and acceptable accuracy/behavior/cost thresholds remain undefined. Draft creation resolves organization, not these scientific prerequisites.

## State update rule

Update this file only when one of the following occurs:

- a source/data record is formally admitted or its status changes materially;
- a Physics Constraint, Hypothesis, Method, or Experiment changes state;
- an ADR is accepted/rejected/superseded;
- a verified result changes what is currently known;
- an explicitly approved Core change is applied;
- a clearly bounded administrative phase is completed;
- downstream Wiki synchronization materially changes the documented human-navigation state.

Do not add speculative scientific ideas to Current State.
