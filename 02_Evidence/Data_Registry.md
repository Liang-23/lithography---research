---
schema_version: "1.0"
id: DATA-REGISTRY
type: data-register
lifecycle_status: active
authority_class: derived
authority_scope: data-index-only
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

# Data Registry

| DATA-ID | Name | Exact local path | Origin | Version | Manifest hash | Data state | Split state | Allowed experiments | Record |
|---|---|---|---|---|---|---|---|---|---|
| DATA-0001 | MetalSet matched pixelILT/litho pairs (external candidate) | `D:\project\lithobench-main\work\lithodata.tar\lithodata\MetalSet` | derived/simulator-backed candidate; provenance pending review | external audit snapshot 2026-09-21 | train/val/test hashes in record | registered, unfrozen | existing manifests, not frozen | EXP-0002 only after plan freeze | [DATA-0001 record](DATA-0001_MetalSet_PixelILT_Litho.md) |

| DATA-ID | Name | Exact local path | Origin | Version | Manifest hash | Data state | Split state | Allowed experiments | Record |
|---|---|---|---|---|---|---|---|---|---|

## Rules

- Allocate from `DATA-0001`; never reuse an ID.
- Record measurement/simulator/synthetic/derived/mixed origin explicitly.
- Derived data must link to every parent `DATA-ID` and exact transformation recipe.
- Formal experiments may use only reviewed and frozen data versions.
- A changed sample set, generation recipe, split, or label contract requires a new version or `DATA-ID`.
- Use `_templates/Data_Record_Template.md` for detailed records.
