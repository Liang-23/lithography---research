---
schema_version: "1.0"
id: PHYSICS-CONSTRAINT-POLICY
type: layer-policy
lifecycle_status: active
authority_class: derived
authority_scope: physics-constraint-policy-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User request on 2026-08-26"
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
exclude_from_synthesis: true
---

# Physics Constraints Layer

`03_Physics_Constraints` converts a potentially relevant physical formula or behavior into a traceable, computable, falsifiable candidate for terminal-output correction.

No equation may enter Method Design or Experiment merely because it is physically plausible. It must first receive a `PC-####` record and pass Core, Evidence, computability, and inference-compatibility screening.

## Authority

- `draft`, `screened`, and `ready-to-test` are candidate states.
- `supported` means supported only within recorded experimental conditions.
- A supported constraint still does not automatically become the selected project Method.
- Selection requires an accepted ADR.

## Required distinction

Every record must say whether the relationship is:

- a hard equality;
- an inequality or feasible set;
- a solution manifold;
- a soft behavior or regularity;
- an empirical heuristic.

Use [Constraint Register](Constraint_Register.md) and `_templates/Physics_Constraint_Template.md`.
