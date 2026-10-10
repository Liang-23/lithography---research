---
schema_version: "1.0"
id: PC-####
type: physics-constraint
title:
lifecycle_status: template
authority_class: none
authority_scope: candidate-constraint-only
created_by:
content_origin:
created_at:
updated_at:
owner:
review_status: unreviewed
reviewed_by:
approved_by:
approval_ref:
core_alignment: unknown
constraint_state: draft
source_ids: []
evidence_ids: []
hypothesis_ids: []
method_ids: []
experiment_ids: []
decision_ids: []
supersedes:
superseded_by:
exclude_from_synthesis: true
---

# [Physics Constraint title]

## 1. Core relationship

- Core requirement addressed:
- Why this is relevant to terminal-output correction:
- Core conflict check:
- Explicitly out-of-scope risk:

## 2. Formal definition

### Equation or operator

\[
\text{[exact equation/operator]}
\]

### Variables and representation

| Symbol | Meaning | Shape | Unit | Coordinate system | Source |
|---|---|---|---|---|---|

### Relationship type

- Type: hard equality | inequality/feasible set | manifold | soft behavior | empirical heuristic
- Residual or violation measure:
- Tolerance and its source:

## 3. Physical interpretation

- Physical meaning:
- Assumptions:
- Validity regime:
- Invalid/excluded regime:
- Boundary/initial conditions:

## 4. Computability

- Required model inputs:
- Required model outputs:
- Required external parameters:
- Required simulator/data calls:
- Available at training time:
- Available at inference time:
- Missing information:

## 5. Correction / projection definition

### Raw prediction

\[
z=f_\theta(x)
\]

### Candidate correction

\[
y^+=P(x,z)
\]

- Objective minimized by (P):
- Distance/weighting definition:
- Solution uniqueness:
- Numerical solver/algorithm:
- Convergence condition:
- Behavior when no feasible solution exists:

## 6. Differentiability and knowledge transfer

- Differentiable:
- Discontinuous/non-differentiable regions:
- Direct backpropagation allowed:
- `stop-gradient`/teacher target design:
- Event-trigger candidate, if any:
- Risk of damaging learned information:

## 7. Computational cost

- Training-time cost:
- Inference-time cost:
- Memory cost:
- High-fidelity calls required:
- Compatibility with end-to-end inference requirement:

## 8. Evidence

- Supporting `EV-ID`s:
- Contradicting `EV-ID`s:
- Evidence boundary:
- Unverified assumptions:

## 9. Failure modes

- Physically valid but numerically wrong output:
- Projection changes along valid-solution directions:
- Incorrect units/coordinates:
- Out-of-regime behavior:
- Solver failure:
- Added cost eliminates surrogate speedup:
- Other:

## 10. Validation and rejection

- Linked `HYP-ID`:
- Required baseline:
- Proposed `EXP-ID`:
- Primary metric:
- Physical-consistency metric:
- Pass threshold:
- Rejection condition:
- Stop condition:
- Evidence required for `supported`:

## 11. Review checklist

- [ ] Equation/operator is exact and source-grounded.
- [ ] Variables, shapes, units, and coordinates are complete.
- [ ] Validity regime and failure conditions are explicit.
- [ ] Correction is computable with available information.
- [ ] Training and inference behavior are separated.
- [ ] End-to-end inference compatibility is checked.
- [ ] Supporting and conflicting Evidence are linked.
- [ ] A falsifiable rejection experiment is defined.
- [ ] Template metadata is replaced only when creating a real `PC-ID` record.

