---
schema_version: "1.0"
id: EVIDENCE-POLICY
type: layer-policy
lifecycle_status: active
authority_class: derived
authority_scope: evidence-layer-policy-only
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

# Evidence Layer

`02_Evidence` controls source provenance, data/simulator provenance, and claim-level evidence.

## Three separate records

- `SRC-####`: proves that a source artifact exists and records its provenance.
- `DATA-####`: records a dataset, simulator-produced release, or derived data lineage.
- `EV-####`: supports or contradicts one atomic scientific claim with an exact locator.

A registered source does not verify every statement inside it. A polished summary is not Evidence.

## Human-controlled promotions

- AI may draft a Source, Data, or Evidence record.
- AI may calculate hashes and verify local paths.
- AI may perform a documented source check.
- AI may not fill `approved_by` on the user's behalf.
- `evidence_state: verified` requires the required review and approval.
- Unknown provenance goes to `90_Quarantine`.

## Canonical registers

- [Source Registry](Source_Registry.md)
- [Data Registry](Data_Registry.md)
- [Evidence Ledger](Evidence_Ledger.md)
