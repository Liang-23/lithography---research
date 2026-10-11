---
id: EXP-0003
title: "FD-NIG synthetic frequency-difference aggregation feasibility"
experiment_state: draft-blocked
approval_status: not_requested
method_ids: [METHOD-0002]
data_ids: []
source_ids: []
hypothesis_ids: []
pc_ids: []
owner: project-lead
created: 2026-10-11
last_updated: 2026-10-11
---

# Purpose and authority boundary

This is the smallest proposed synthetic feasibility experiment for the candidate
Frequency Difference Neural Interaction Graph (FD-NIG). It is a numerical and
automatic-differentiation check of the primary intensity-spectrum formulation in
`METHOD-0002`; it is not a lithography validation, a Method selection, or a real
`DATA-0001` experiment. This plan must remain blocked until the prerequisites and
thresholds below are explicitly approved. No run, result, checkpoint, or scientific
claim is authorized by this draft.

## Research question

On a deterministic small circular DFT grid, does an implementation of

$$
\widehat{I}(q)=\sum_{k-l=q} C_\theta(k,l,c)M(k)\operatorname{conj}(M(l))
$$

route, multiply, aggregate, and inverse-transform correctly, stably, and with
usable gradients? The aggregate is predicted intensity spectrum. The spatial
output is obtained by one inverse FFT; a second magnitude-square operation is
forbidden.

## Governance linkage and blockers

- Method: `METHOD-0002` (candidate only).
- Hypothesis linkage: **method-local feasibility check without a separate
  Hypothesis, explicitly approved by the project lead in the ChatGPT conversation
  on 2026-10-11**. This check tests numerical implementation behavior under
  `METHOD-0002`, not a falsifiable comparative lithography research claim.
  No `HYP-0004` is created, and `HYP-0001`–`HYP-0003` are not repurposed.
  This approval applies only to hypothesis linkage: it does **not** approve
  numerical thresholds, the experiment Plan, or any test execution.
- Physics Constraint: none. Hermitian symmetry is an algebraic test condition,
  not a registered physical constraint.
- Data: no `DATA-0001` or MetalSet files; all inputs are generated and frozen in
  the plan/configuration.
- Approval blockers: project-lead approval of proposed thresholds, compute
  budget, FFT/index convention, sparse-pair policy, and implementation scope,
  followed by formal approval of the experiment Plan. Hypothesis linkage is
  resolved separately above. No execution is permitted while `draft-blocked`.

## Frozen synthetic contract (proposal)

- Grid: circular $H=W=16$, with integer FFT bins in native unshifted order
  (`torch.fft.fftfreq`/`fft2` convention); a $32\times32$ repeat is optional
  only after the $16\times16$ gate passes.
- Mask: deterministic real-valued spatial pattern generated from seed `20261011`
  (two rectangles plus one sinusoidal component), with a documented binary and
  non-binary case. Compute $M=\operatorname{FFT2}(m)$ using an explicit
  normalization recorded in the run configuration.
- Conditions: fixed vector $c=[1]$; no condition-generalization claim.
- Pair order: lexicographic `(k_row, k_col, l_row, l_col)` over the selected
  pair list. The exhaustive reference uses all $|\mathcal K|^2=65,536$ pairs;
  the sparse path uses a deterministic first-$P$ subset with $P=256$ plus its
  swapped pairs where required for symmetry.
- Routing: $q=(k-l)\bmod(H,W)$, represented by a flattened output-bin index.
- Coefficients: deterministic complex tensor $C(k,l,c)$ from seeded real and
  imaginary values; a Hermitian test fixture additionally enforces
  $C(l,k,c)=\operatorname{conj}(C(k,l,c))$ and real self-conjugate bins.
- Output: complex $\widehat I(q)$, then one `ifft2`; the test checks the
  imaginary residual and does not apply $|\cdot|^2$.

## Reference implementation and planned modules

The implementation is planned, but must not be created or executed as part of
this draft-only task. The reference path should use a transparent Python/NumPy
or PyTorch loop over every pair and direct indexed accumulation into a complex
`[H,W]` array. The FD-NIG path should use the same tensors with vectorized
complex multiply and complex scatter-add. Both paths must share only input
fixtures and conventions, not aggregation code, so agreement is meaningful.

Planned files for a later approved implementation:

1. `tools/fd_nig_reference.py`: exhaustive pair enumeration, modular routing,
   loop reference, and fixture generation.
2. `tools/fd_nig_aggregation.py`: sparse/vectorized complex aggregation and
   optional Hermitian enforcement, with no inverse-FFT magnitude square.
3. `tools/tests/test_fd_nig_synthetic.py`: deterministic numerical and gradient
   tests listed below.
4. `tools/fd_nig_config.json`: frozen seed, grid, normalization, pair policy,
   tolerances, and budget; generated only after approval.

## Ordered tests and proposed gates

All thresholds are proposals requiring approval. Tests compare the independent
reference implementation with the candidate aggregation wherever applicable.

**Floating-point accumulation review:** An exhaustive 16x16 frequency-pair
reference sums 65,536 complex contributions, and different summation orders
may lead to materially different float32 rounding. Before approving the
candidate tolerances, document the reduction order, compare float64
reference/vectorized outputs, and characterize float32-vs-float64 errors
(including cancellation-heavy and empty bins) using separately authorized
calibration fixtures. The values listed below are starting proposals, not
empirically justified gates. Any revision of numerical thresholds must be
reviewed and frozen BEFORE executing the formal experiment; do not silently
relax thresholds after a failed run.

1. **Frequency-difference routing:** every enumerated pair lands in exactly one
   bin and the candidate route equals `(k-l) mod (H,W)` for 100% of pairs.
2. **Complex pairwise multiplication:** compare
   $C\,M(k)\operatorname{conj}(M(l))$ against an independently expanded real/imag
   calculation; maximum absolute error $\le 1\times10^{-6}$ (float32) or
   $\le 1\times10^{-12}$ (float64).
3. **Complex scatter-add:** compare candidate and independent loop
   reference for all output bins, including zero, one, and many contributing
   pairs. A pure relative error is undefined when the reference bin is
   zero. Instead, define per-bin absolute difference
   `error[q] = abs(candidate[q] - reference[q])` and evaluate against
   `atol + rtol * scale[q]`. For a cancellation-resistant diagnostic,
   `scale[q]` is the independently accumulated sum of the absolute
   magnitudes of all pair contributions to bin q. Empty bins use the
   absolute tolerance. Suggested initial float32 values are
   `atol=1e-6` and `rtol=1e-5`; float64 values may start at
   `atol=1e-12` and `rtol=1e-12`. These values are NOT approved:
   determine whether they fit the actual numerical magnitudes and
   addition order before freezing the experiment plan. Record maximum
   absolute error and cancellation-heavy bin errors separately.
4. **Conjugate symmetry:** for the Hermitian fixture,
   $\max_q|\widehat I(q)-\operatorname{conj}(\widehat I(-q))|\le1\times10^{-5}$
   (float32); DC and self-conjugate Nyquist bins have imaginary magnitude
   $\le1\times10^{-6}$.
5. **Real inverse FFT:** `ifft2(\widehat I)` has maximum imaginary residual
   $\le1\times10^{-5}$ (float32), and the real output is identical between
   reference and candidate within the aggregation tolerance. No magnitude square
   is performed.
6. **Gradient propagation:** with a scalar loss equal to the mean squared error
   of the real inverse-FFT output against a fixed real target, gradients
   must be finite for all active independent parameter components, with
   nonzero gradients verified on chosen nondegenerate active components.
   Zero gradients on masked, unused, or symmetry-constrained terms are
   permitted and must be documented. Centered finite-difference spot
   checks compare effective independent parameters using both absolute
   and relative error tolerances; numerical values remain proposals
   subject to approval, and near-zero reference gradients require the
   absolute tolerance rather than division by zero.
7. **Finite/stability gate:** all intermediate and final real/imaginary values,
   losses, and gradients are finite for the normal fixture and a stress fixture
   scaled by $10^3$; no NaN/Inf and no runtime overflow.
8. **Sparse versus exhaustive:** on tiny $4\times4$ and $8\times8$ grids where
   sparse selection equals the exhaustive pair set, outputs and gradients meet
   the scatter-add tolerance. The $16\times16$ sparse policy is then checked
   for deterministic repeatability; it is not judged against exhaustive output
   when the pair sets differ.

The gate is pass only if every required test passes in two consecutive runs with
the same seed and the recorded environment. Any failed test blocks all later
training or MetalSet work and is recorded as a failed run if execution is later
authorized.

## Compute budget and artifacts (proposal)

Budget: CPU-only, one process, at most 2 minutes wall time, 2 GB peak memory,
and at most 2 repetitions of the test suite. No GPU, network data, training,
or external simulator is required. Expected artifacts are a JSON test report,
environment/version capture, fixture hash, and (if approved) a small gradient
summary. No artifact may be described as scientific validation.

## Unresolved prerequisites

1. **Resolved, 2026-10-11:** Project lead explicitly approved treating
   `EXP-0003` as a `METHOD-0002` method-local numerical feasibility check,
   without creating `HYP-0004`. This does not approve test execution.
2. **Still blocked:** User approval of all proposed numerical tolerances, seed,
   grid/normalization, sparse-pair policy, and compute budget.
3. **Still blocked:** Final implementation review confirming reference/candidate
   independence, adequate test coverage, and protected-file boundaries.
4. **Still blocked:** Formal approval of this Plan (`approval_status`) before
   any test execution.

Until all four prerequisites are resolved, `EXP-0003` remains `draft-blocked`.
