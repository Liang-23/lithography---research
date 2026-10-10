---
schema_version: "1.0"
id: PHYSICS-CONSTRAINT-REGISTER
type: physics-constraint-register
lifecycle_status: active
authority_class: derived
authority_scope: physics-constraint-index-only
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

# Physics Constraint Register

| PC-ID | Title | Relationship type | Constraint state | Evidence IDs | Hypothesis IDs | Experiment IDs | Core alignment | Record |
|---|---|---|---|---|---|---|---|---|

## ID and state rules

- Allocate from `PC-0001`; never reuse an ID.
- State flow: `draft → screened → ready-to-test → supported | rejected | inconclusive → superseded`.
- AI may draft and screen; human approval is required for project selection.
- `supported` requires valid experiment evidence, not theoretical plausibility alone.
- Rejected and inconclusive records remain traceable.
