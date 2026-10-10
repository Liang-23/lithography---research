---
schema_version: "1.0"
id: ADR-0001
type: architecture-research-decision-record
title: Central canonical Relationship Registry for the Graph projection
lifecycle_status: rejected
authority_class: none
authority_scope: historical-rejected-proposal-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
owner: project-lead
review_status: rejected
reviewed_by: user
approved_by:
approval_ref: "Explicit architecture correction request, 2026-08-26"
core_alignment: pass
decision_state: rejected
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
method_ids: []
experiment_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: true
---

# ADR-0001 — Central canonical Relationship Registry

## Status

- Decision state: rejected
- Decision owner: project lead
- Decision date: 2026-08-26
- Rejection reference: explicit user architecture correction request on 2026-08-26
- Effective date: 2026-08-26

## Decision outcome

This proposal was rejected before acceptance. It misunderstood “Graph View” as a custom relationship registry and generated technical projection rather than Obsidian's Native Graph View.

The provisional registry contained no accepted relationships, so rollback loses no scientific relationship data. The active replacement is recorded in `ADR-0002`: Governance remains canonical, the Wiki is a derived Markdown projection, `[[wikilinks]]` provide human semantic navigation, and Obsidian visualizes those links natively.

## Decision question

Where should explicit cross-record relationships live so that the Context Router and human Graph View share one source without modifying scientific content or creating a second knowledge base?

## Core relationship

- Core requirements affected: none; this is administrative research infrastructure.
- Compatibility result: pass.
- Core change required: no.

## Options considered

1. Inline normalized relationships in every canonical record.
2. One central canonical Relationship Registry with normalized triples.
3. Infer relationships from typed ID lists or prose.

## Proposed decision

Provisionally implement option 2 in `08_Project_Status/Relationship_Registry.yaml`.

Rationale:

- it is the least invasive design;
- it creates one explicit edge format;
- it avoids rewriting current templates and scientific records;
- it is deterministic and easy to validate;
- it can later migrate without changing permanent node or relation IDs.

The implementation is reversible and may be tested before this ADR is accepted. AI must not change `decision_state` to `accepted` or populate approval metadata on the user's behalf.

## Consequences

- Graph edges have a single reviewable location.
- Scientific claims remain in their canonical records.
- Existing typed ID lists are not automatically treated as graph edges.
- The registry may become a merge bottleneck if relation volume or team size grows.

## Rollback

Remove the derived `09_Knowledge_Graph` module and non-Core routing references. Preserve any reviewed relationship entries for migration; do not modify Locked Core.

Rollback was completed on 2026-08-26. The obsolete module and empty registry were archived for audit history; no Locked Core file or scientific meaning changed.
