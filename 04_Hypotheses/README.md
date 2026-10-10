---
schema_version: "1.0"
id: HYPOTHESES-README
type: layer-readme
lifecycle_status: active
authority_class: working
authority_scope: hypothesis-management-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-08-26
updated_at: 2026-08-26
review_status: unreviewed
core_alignment: pass
exclude_from_synthesis: true
---

# Hypotheses

This layer stores falsifiable research hypotheses. A Hypothesis is a claim to test, not a project decision or verified fact.

## Admission rule

A real `HYP-####` record must:

- link to at least one exact Core requirement;
- state an observable mechanism and an explicit rejection condition;
- identify independent, dependent, and controlled variables;
- link supporting and conflicting Evidence where available;
- name a proposed `EXP-ID` or explain why it is not yet testable;
- remain non-authoritative until supported by valid experiments.

## Files

- `Hypothesis_Register.md` — canonical list and state of Hypotheses
- `_templates/Hypothesis_Template.md` — copy when creating a real Hypothesis

Do not convert an AI idea directly into a Hypothesis when it is out of Core scope or lacks a testable path. Put it in `90_Quarantine/` first.
