---
schema_version: "1.0"
id: DECISIONS-README
type: layer-readme
lifecycle_status: active
authority_class: working
authority_scope: decision-management-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
core_alignment: pass
exclude_from_synthesis: true
---

# Decisions

This layer records material project choices through Architecture/Research Decision Records (`ADR-####`). It prevents a paper, result, meeting comment, or AI recommendation from silently becoming project policy.

The Agent may draft a proposed ADR. Only the authorized project owner may accept, reject, reverse, or approve a Core-changing ADR.

## Files

- `Decision_Log.md` — chronological decision index
- `_templates/ADR_Template.md` — decision proposal and record

An accepted ADR remains subordinate to Locked Core. A change to Locked Core also requires the separate Core modification gate and `Core_Change_Log.md` entry.
