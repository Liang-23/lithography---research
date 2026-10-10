---
schema_version: "1.0"
id: EXPERIMENTS-README
type: layer-readme
lifecycle_status: active
authority_class: working
authority_scope: experiment-management-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
core_alignment: pass
exclude_from_synthesis: true
---

# Experiments

Formal experiments use one folder per permanent ID:

```text
06_Experiments/
  EXP-####/
    Plan.md
    Run_Log.md
    Result.md
    artifacts/
```

## Integrity rules

1. Complete and review `Plan.md` before the first formal run.
2. Freeze data split, metrics, thresholds, code/config references, budget, and stop conditions in the Plan.
3. After execution starts, record deviations; do not rewrite history.
4. `Run_Log.md` is append-only. Give every attempt a `RUN-EXP-####-###` ID, including failed or stopped runs.
5. Keep observations separate from interpretations in `Result.md`.
6. Store or link artifacts with hashes. Never claim reproducibility without resolvable artifacts.
7. A post-hoc metric must be labeled post-hoc and cannot be presented as preregistered.
8. A completed experiment is not automatically verified Evidence or a project Decision.

## Files

- `Experiment_Register.md` — experiment index and state
- `_templates/Plan_Template.md`
- `_templates/Run_Log_Template.md`
- `_templates/Result_Template.md`
