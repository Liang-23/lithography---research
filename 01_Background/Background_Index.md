---
schema_version: "1.0"
id: BACKGROUND-INDEX
type: background-register
lifecycle_status: active
authority_class: derived
authority_scope: background-index-only
created_by: ai
content_origin: ai-assisted
creation_authorization: "User request on 2026-08-26"
created_at: 2026-08-26
updated_at: 2026-09-13
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: pass
exclude_from_synthesis: true
---

# Background Index

This is the canonical register of `BG-####` records. An entry in this table means the record exists; it does not mean its claims are verified.

## Records

| BG-ID | Title | Lifecycle | Review status | Source IDs | Evidence IDs | Core alignment | Path |
|---|---|---|---|---|---|---|---|
| BG-0001 | SRC-0002 Pass 2: Project-aware comparison of output projection | draft | pending-user-review | SRC-0002 | None | conflict | [Background record](BG-0001_SRC-0002_Output_Projection_Project_Aware_Comparison.md) |
| BG-0002 | 以 PADM 为重点的物理融合、知识回传与低数据光刻研究背景 | draft | unreviewed | SRC-0001–SRC-0013 | EV-0001–EV-0006 (bounded mechanisms only) | pass | [Background record](BG-0002_PADM_Physics_Transfer_Low_Data_Lithography.md) |

## ID rule

- Allocate IDs sequentially from `BG-0001`.
- Never reuse an ID.
- Preserve rejected, superseded, and archived IDs.
- Do not create an entry until its file exists.

## Promotion rule

`draft → review → active → superseded | rejected | archived`

`active` means approved for contextual use; it does not mean every scientific claim is verified.
