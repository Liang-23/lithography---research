---
schema_version: "1.0"
id: METHOD-DESIGN-README
type: layer-readme
lifecycle_status: active
authority_class: working
authority_scope: method-management-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
core_alignment: pass
exclude_from_synthesis: true
---

# Method Design

This layer turns registered requirements, Physics Constraints, and Hypotheses into implementable candidate methods.

A Method Design is not selected merely because it is detailed or AI-generated. Selection for implementation requires an accepted `ADR-ID` when alternatives or material trade-offs exist.

## Required boundary

Every real `METHOD-####` must define:

- the Core requirement and `HYP-ID` / `PC-ID` it addresses;
- inputs, outputs, tensor shapes, units, and data/simulator contracts;
- training-time and inference-time data flow separately;
- loss/correction/projection behavior and gradient path;
- compute and memory cost;
- baselines, ablations, failure criteria, and rollback path.

## Files

- `Method_Register.md` — canonical method index
- `_templates/Method_Design_Template.md` — candidate method specification
