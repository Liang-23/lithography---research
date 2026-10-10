---
schema_version: "1.0"
id: ADR-0002
type: architecture-research-decision-record
title: Obsidian-native Graph View from the derived Markdown Wiki
lifecycle_status: active
authority_class: approved-decision
authority_scope: knowledge-organization-and-navigation-architecture-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
owner: project-lead
review_status: approved
reviewed_by: user
approved_by: user
approval_ref: "Explicit architecture correction request, 2026-08-26"
core_alignment: pass
decision_state: accepted
source_ids: []
data_ids: []
evidence_ids: []
physics_constraint_ids: []
hypothesis_ids: []
method_ids: []
experiment_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: false
---

# ADR-0002 — Obsidian-native Graph View from the derived Markdown Wiki

## Status

- Decision state: accepted
- Decision owner: project lead
- Decision date: 2026-08-26
- Explicit approval reference: user architecture correction request on 2026-08-26
- Effective date: 2026-08-26

## Context

The project needs two different forms of access to one research state:

- bounded canonical context for AI work;
- a human-readable knowledge network for navigation in Obsidian.

`ADR-0001` proposed a separate relationship registry and generated JSON/Markdown/Mermaid projection. The user explicitly rejected that interpretation before the ADR was accepted. “Graph View” means Obsidian's Native Graph View, which already derives connections from Markdown links.

## Decision

Use this architecture:

```text
Governance System
    -> Wiki ingestion / synchronization
    -> Markdown notes + [[wikilinks]]
    -> Obsidian Native Graph View
```

Separately:

```text
Governance System
    -> Context Router
    -> bounded canonical context for AI Agents
```

Governance records remain canonical for provenance, admissibility, authority, and scientific state. `wiki/` is a derived human-readable projection. Governance IDs and canonical paths provide traceability; `[[wikilinks]]` provide semantic navigation. Neither link presence nor graph connectivity changes scientific authority.

## Options considered

### Option 1 — Custom relationship registry and generated Graph projection

- Rejected because it creates a parallel relationship layer and requires custom rendering artifacts.
- It does not match the requested Obsidian-native experience.
- Its provisional registries contained no accepted relationships.

### Option 2 — Derived Markdown Wiki with Obsidian Native Graph View

- Accepted because Markdown notes remain the readable knowledge substrate.
- Actual `[[wikilinks]]` serve both navigation and native visualization.
- No graph database, web renderer, generated `graph.json`, or `build graph` command is required.

### Option 3 — No linked Wiki visualization

- Rejected because it would not provide the requested human cognitive map.

## Consequences

- Every meaningful human-facing node is a Markdown Wiki note.
- Wiki links must resolve, remain contextual, and avoid synonym duplication or indiscriminate linking.
- Admissible canonical changes trigger applicable downstream Wiki synchronization.
- Deterministic scripts may validate Markdown integrity but must not generate a replacement Graph View.
- Scientific relationship semantics remain in canonical records and explanatory prose; a Wiki link alone is not a scientific assertion.
- Obsidian controls visual layout and display preferences, so presentation is not versioned as a generated research artifact.

## Core compatibility

- Core requirements affected: none; this is administrative knowledge-organization architecture.
- Locked Core changes required: none.
- Scientific meaning changed: no.
- Scope exclusions remain unchanged.

## Rollback

The Wiki is plain Markdown and remains readable without Obsidian. Replacing Obsidian or changing navigation architecture would require a new explicit decision. The rejected custom module remains archived and must not be restored automatically.
