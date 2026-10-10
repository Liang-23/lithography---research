---
schema_version: "1.0"
id: PROJECT-STATUS-README
type: layer-readme
lifecycle_status: active
authority_class: working
authority_scope: project-status-navigation-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
core_alignment: pass
exclude_from_synthesis: true
---

# Project Status

This layer is the compact operational entry point after reading Locked Core.

- `Current_State.md` — the single current-status summary; verified/administrative state only
- `Context_Router.md` — minimum-context routing rules for each task
- `Next_Action.md` — bounded proposed or approved actions, not an idea backlog
- `Wiki_Workflow.md` — downstream derived Wiki ingestion, synchronization, linking, integrity, and learning workflow

Status files summarize canonical records but do not replace them. If a status summary conflicts with a canonical register, Evidence record, accepted ADR, or Locked Core, report and repair the summary rather than silently changing the canonical record.

`Context_Router.md` routes applicable canonical changes into downstream `wiki/` synchronization. Wiki notes and `[[wikilinks]]` remain derived; they cannot modify or override canonical scientific content or state.
