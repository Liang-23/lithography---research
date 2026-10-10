---
schema_version: "1.0"
id: DECISION-LOG
type: decision-register
lifecycle_status: active
authority_class: working
authority_scope: decision-index-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-27
review_status: unreviewed
core_alignment: pass
exclude_from_synthesis: false
---

# Decision Log

| ADR-ID | Decision question | Decision state | Outcome | Decision owner | Approval reference | Effective date | Supersedes |
|---|---|---|---|---|---|---|---|

| ADR-0001 | Where should explicit Graph relationships live? | rejected | Custom relationship registry/projection rejected as a misunderstanding of Obsidian Native Graph View | project lead | Explicit architecture correction request, 2026-08-26 | 2026-08-26 | — |
| ADR-0002 | How should the human Graph View be produced? | accepted | Derived Markdown Wiki with contextual `[[wikilinks]]`; Obsidian renders its Native Graph View directly | project lead | Explicit architecture correction request, 2026-08-26 | 2026-08-26 | — |
| ADR-0003 | How should governance ownership and experiment-local decision authority be separated? | accepted | Deduplicate governance ownership; reserve ADRs for strategic/persistent decisions; allow preregistered candidate-Method implementation and testing without selection | project lead | Explicit governance correction request, 2026-08-27 | 2026-08-27 | — |
| ADR-0004 | Should `pylitho.exact.LithoSim` become the canonical high-fidelity simulator for future governed experiments? | proposed | Proposal recorded for human review; no simulator selected or implemented | project lead | None — awaiting explicit user decision | — | — |
