# Cloud Migration Report

Date: 2026-10-10
Source: `D:\Litho\2-3nm litho`
Target: `C:\Users\uaena\Documents\GitHub\lithography---research`
Remote: `https://github.com/Liang-23/lithography---research.git`
Branch: `main`

## 1. Migration completion status

**Local migration: complete and verified.**

The source and target directories were accessible. The target remote matched the requested private repository, and the target working tree was clean before migration. No source files were moved, deleted, or rewritten. No scientific content, Core record, hypothesis, method, experiment, decision, or review answer was modified.

The remote push is **blocked**: the connection to `github.com:443` timed out. All migration commits remain locally on `main`.

## 2. Successfully copied content

The following research layers were copied while preserving relative paths:

- `01_Background/`
- `02_Evidence/`
- `03_Physics_Constraints/`
- `04_Hypotheses/`
- `05_Method_Design/`
- `06_Experiments/`
- `07_Decisions/`
- `reviews/weekly/`
- `tools/` source and tests
- `wiki/`
- Small root Markdown notes and PNG figures

The already migrated `00_Project_Core/`, `08_Project_Status/`, `AGENTS.md`, and `README.md` were retained. Matching files were not recopied.

## 3. File counts and verification

- Eligible source files inspected: **116**
- New files copied: **106**
- Pre-existing target files with identical SHA-256 hashes: **10**
- Source files missing from target after migration: **0**
- Source/target SHA-256 mismatches: **0**
- Eligible files larger than 20 MB: **0**
- Text/configuration files with credential-pattern matches: **0**
- Scientific scripts executed: **none**

A repository `.gitignore` was added for local/editor state, temporary output, caches, raw sources, quarantine/archive content, environments/secrets, and large model/data artifacts.

## 4. Excluded content

The following were intentionally not migrated:

- `.git/`, `.obsidian/`, `.keep-the-rhythm/`
- `tmp/`, `output/`
- `90_Quarantine/`, `99_Archive/`
- `raw/` (source PDFs and other originals were not individually reviewed for cloud suitability)
- Python caches and compiled files such as `__pycache__/` and `*.pyc`
- Virtual environments, credentials, and large model/data artifact patterns

No excluded file was tracked by the migration commits.

## 5. Commits and push status

Local migration commits:

- `0384aac` — Migrate research background and evidence
- `0f0a038` — Migrate physics constraints hypotheses and methods
- `94ccd3c` — Migrate experiments decisions and project status
- `5fe40b0` — Migrate wiki tooling and research assets
- `319b362` — Migrate PAMD architecture figure

Push status: **not completed**. `git push origin main` failed because the environment could not connect to `github.com:443`. No force-push, history rewrite, branch deletion, or visibility change was attempted.

## 6. Security and governance concerns

- The canonical records contain Windows-only provenance paths such as `D:\Litho\2-3nm litho\raw\...` and the previously authorized external audit path `D:\project\lithobench-main\...`. These paths will not resolve in Linux-based Codex Cloud.
- The referenced raw PDFs and the external dataset were not uploaded. Cloud review can use the migrated canonical records and Wiki, but it cannot independently reopen those local originals.
- The target contains both the pre-existing root `Project_Overview.md` and canonical `00_Project_Core/Project_Overview.md`. They differ. Neither was overwritten or silently selected as authoritative; the Core governance hierarchy remains unchanged.
- The root `AGENTS.md` still defines the Windows project boundary. No rewrite was made to adapt authoritative governance text for Linux.
- Empty legacy Wiki placeholders were preserved as source files; they should be reviewed separately if they create health warnings.

## 7. Cloud environment readiness

**Ready for governed context and navigation, with source-reproducibility limitations.**

The target contains the project objectives, requirements, governance, context router, current state, evidence/source registers, hypotheses, candidate method, experiment plans, decision records, and Obsidian Wiki. Codex Cloud can therefore understand the approved research frame and current status from the migrated repository.

A fully reproducible source audit is not yet possible in Cloud because `raw/` and the external dataset remain local and the migrated records retain Windows-only paths. No Codex Cloud session was claimed or tested here.

## 8. Recommended synchronization workflow

1. Keep `C:\Users\uaena\Documents\GitHub\lithography---research` as the local mirror.
2. Before each sync, fetch the remote and inspect the working tree for unexpected changes.
3. Copy only approved, reviewable files from `D:\Litho\2-3nm litho`; never bulk-copy `raw/`, caches, outputs, quarantine, archive, or credentials.
4. Verify source/target SHA-256 hashes for copied files.
5. Review the diff for secrets, large artifacts, and Windows-only paths.
6. Commit by logical research layer and push without force.
7. Treat Core, Evidence state, Method selection, Experiment authorization, and ADR acceptance as governed project actions, not migration side effects.

## 9. Manual steps needed

After network access and GitHub authentication are available, run:

```text
cd C:\Users\uaena\Documents\GitHub\lithography---research
git fetch origin
git status
git push origin main
```

Then configure Codex Cloud to use the private repository `Liang-23/lithography---research` on `main`. If Cloud must verify original papers or data, individually review and deliberately admit suitable files through the project’s source/data governance workflow; do not upload the entire `raw/` tree.

The root/canonical `Project_Overview.md` duplication should be resolved only through the project’s established governance decision process.
