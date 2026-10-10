---
title: "Adaptive Correction for Ensuring Conservation Laws in Neural Operators"
type: source
lifecycle_status: active
authority_class: derived
authority_scope: human-readable-wiki-only
created_by: ai
content_origin: mixed
created_at: 2026-08-30
updated_at: 2026-08-30
review_status: source-checked
human_audit_status: not-started
knowledge_status: source-reported-claims-unverified
canonical_refs:
  - "02_Evidence/SRC-0006_Adaptive_Correction_for_Ensuring_Conservation_Laws_in_Neural_Operators.md"
source_ids: [SRC-0006]
source_file: "raw/SRC-0006_Adaptive_Correction_Neural_Operators.pdf"
exclude_from_synthesis: false
---

# Adaptive Correction for Ensuring Conservation Laws in Neural Operators

## Human-readable summary

The paper adds a lightweight learnable terminal operator that allocates the correction needed to satisfy one global linear or quadratic invariant over a spatial field. The raw neural operator and corrector train jointly, and the corrector remains in inference. Demonstrated fields include $128\times128$ 2D PDE outputs. [SRC-0006, pp. 3–7]

The comparison is especially valuable for [[High-dimensional Safe Correction]]: on conservative Allen–Cahn, the raw FNO error is $2.01\times10^{-2}$, while an exact minimum-$L_2$ projection reports $99.7\times10^{-2}$ despite zero printed conservation error. The adaptive corrector reports $1.65\times10^{-2}$. [SRC-0006, pp. 7–8]

## Boundaries

- The theorem is a function-class inclusion statement, not proof that representation freedom improves empirical learning.
- Only one linear or quadratic global invariant is handled at a time.
- No corrected targets, distillation, corrector removal, safety gate, OOD test, or lithography relationship is established.

## Governance traceability

Canonical Source: `SRC-0006`, stored at `02_Evidence/SRC-0006_Adaptive_Correction_for_Ensuring_Conservation_Laws_in_Neural_Operators.md`. Claims remain unverified.

