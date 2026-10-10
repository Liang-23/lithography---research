# 2–3nm Lithography Research Workspace

This workspace combines controlled research Governance with a human-readable Obsidian Wiki. It contains one research state—not a Governance knowledge base plus a separate graph knowledge base.

## Final mental model

```text
Governance System
    -> decides what belongs to the project
    -> records provenance, authority, and scientific status
    -> maintains canonical research state
    -> Wiki Ingestion Agent
    -> derived Markdown notes + [[wikilinks]]
    -> Obsidian Native Graph View
```

For AI work:

```text
Governance System
    -> Context Router
    -> bounded canonical context
    -> AI Agent
```

- Governance determines what is admitted, where it came from, and its status.
- The Wiki Ingestion Agent organizes applicable admitted knowledge for human understanding.
- `[[wikilinks]]` connect related Wiki notes for navigation.
- Obsidian visualizes those Markdown links automatically.
- The Context Router selects authoritative context for AI tasks.

Wiki connectivity never proves a scientific claim and never changes Core, Evidence, an ADR, or any scientific status.

## Directory roles

```text
00_Project_Core/        locked scope, requirements, and Core governance
01_Background/          sourced context; no project decisions
02_Evidence/            source/data registries and claim-level Evidence
03_Physics_Constraints/ physical-constraint specifications
04_Hypotheses/          falsifiable Hypotheses
05_Method_Design/       candidate or selected Method designs
06_Experiments/         preregistered plans, run records, and results
07_Decisions/           ADRs and decision history
08_Project_Status/      current state, routing, actions, and Wiki workflow
90_Quarantine/          unreviewed or potentially contaminating material
99_Archive/             rejected, superseded, or historical material
raw/                    immutable admitted source files
wiki/                   derived human-readable Markdown knowledge
reviews/                learning assessments; never Wiki sources
tools/                  Markdown Wiki integrity checks
```

The active Wiki layout is:

```text
wiki/
├── index.md
├── log.md
├── overview.md
├── sources/
├── entities/
├── concepts/
└── syntheses/
```

## Adding knowledge

You can use either a short command or plain language:

```text
ingest raw/papers/example.md
Add this paper to my project.
Record this research idea.
query: how is physical knowledge integrated?
health
lint
daily review
knowledge check
```

Adding a paper runs this sequence:

```text
source authorization and admission
    -> immutable raw file and SRC-ID/provenance
    -> semantic Wiki ingestion
    -> source/concept/entity note updates
    -> contextual [[wikilinks]]
    -> index / overview / log maintenance
    -> integrity and language checks
```

An informal research idea is first classified as a raw idea, draft Hypothesis, candidate Method, unresolved question, or other working record. If it is useful for human organization, it may also update the Wiki with speculative status preserved. It is not promoted to verified knowledge.

When Evidence, a Hypothesis, a Method, an Experiment result, or an ADR changes canonically, the Agent synchronizes only the affected Wiki explanations when their human-readable meaning changed.

## Wiki note principles

- Preserve the source language and deliberate Chinese-English mixing.
- Preserve technical terms, variables, formulas, code, filenames, paths, and quotations exactly.
- Reuse an existing canonical concept note before creating a synonym duplicate.
- Create atomic notes only when they have independent retrieval or reasoning value.
- Prefer contextual links in explanatory prose over “everything links to everything.”
- Store relevant Governance IDs or canonical paths in frontmatter for traceability.
- Keep candidate, disputed, unverified, and accepted states explicit.

`wiki/overview.md` follows the research task and system flow—inputs, operations, outputs, reasons, downstream use, major distinctions, and unresolved questions. It is not a chronological list of source summaries.

## Obsidian Native Graph View

Open this folder as an Obsidian vault and use Obsidian's built-in Graph View. The graph changes when the Agent changes resolvable Markdown `[[wikilinks]]`.

> No Python command is required to generate the visual Graph View.

There is no active custom graph database, `graph.json` knowledge representation, `graph.html`, vis.js renderer, Mermaid projection, or `build graph` workflow. The file `.obsidian/graph.json` is preserved because it is Obsidian's own display-settings file, not a project knowledge graph.

The human-facing Global Graph is intentionally restricted by `.obsidian/graph.json` to `path:wiki -file:index -file:log`. Do not clear or weaken this filter. Canonical Governance files remain available to the Agent through the Context Router and to humans through the file tree, but they are not human-Wiki graph nodes. Local Graph remains clean because graph-producing links are forbidden across the canonical/Wiki boundary.

## Integrity checks

```text
python tools/health.py
python tools/lint.py
```

These tools inspect Markdown notes and links directly. They can report broken or ambiguous links, cross-plane Graph edges, an unscoped human Graph, orphan or under-linked notes, duplicate titles/aliases, index/log inconsistencies, missing traceability, and deterministic staleness signals. Semantic contradiction, missing-concept, fragmentation, and projection-quality review remains an Agent task.

Neither command generates a visual graph.

## Governing documents

- `AGENTS.md` — Agent behavior and authority boundaries.
- `00_Project_Core/Core_Governance.md` — Core modification and authority rules.
- `08_Project_Status/Context_Router.md` — minimum-context routes and downstream Wiki synchronization.
- `08_Project_Status/Wiki_Workflow.md` — ingestion, linking, language, health/lint, query, and learning workflows.
- `07_Decisions/ADR-0002_Obsidian_Native_Wiki_Graph.md` — accepted navigation architecture.

The archived legacy Wiki configuration and rejected custom Graph implementation are historical only. They cannot re-enter active context without explicit user authorization and the applicable Governance gates.
