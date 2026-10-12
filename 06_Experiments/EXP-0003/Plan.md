---
id: EXP-0003
title: "FD-NIG synthetic frequency-difference aggregation feasibility"
experiment_state: draft-blocked
approval_status: not_requested
numerical_memory_freeze_status: approved
numerical_memory_freeze_ref: "Project lead explicit approval in ChatGPT conversation, 2026-10-12; numerical criteria and monitored-RSS policy only"
approval_ref:
formal_execution_authorization_ref:
method_ids: [METHOD-0002]
data_ids: []
source_ids: []
hypothesis_ids: []
pc_ids: []
owner: project-lead
created: 2026-10-11
last_updated: 2026-10-12
---

# Purpose and authority boundary

This is the smallest proposed synthetic feasibility experiment for the candidate
Frequency Difference Neural Interaction Graph (FD-NIG). It is a numerical and
automatic-differentiation check of the primary intensity-spectrum formulation in
`METHOD-0002`; it is not a lithography validation, a Method selection, or a real
`DATA-0001` experiment. Numerical acceptance gates, seed/FFT/pair selection, and the
monitored-RSS policy are **frozen by a scope-limited project-lead decision
on 2026-10-12**. However, the complete Plan remains `draft-blocked` and is
not preregistered or approved for execution: static implementation review,
required artifacts, and separate formal execution approval are pending.
No run, result, checkpoint, or scientific claim is authorized by this draft.

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
- The project lead separately approved (2026-10-12) the **exact numerical
  acceptance settings and monitored-RSS memory policy** in
  `Numerical_and_Memory_Freeze_Review.md`, in addition to the earlier
  method-local interpretation and 120-second combined budget. These
  experiment-local settings are now frozen but **do not constitute approval
  of the full Plan or of execution**. Implementation review, artifact/run
  provenance gate and independent authorization remain blocked.

## Frozen synthetic contract (scope-limited settings approval, 2026-10-12)

- Grid: circular $H=W=16$, integer FFT bins in native unshifted order,
  `torch.fft.fft2/ifft2(norm="backward")` (forward unnormalized, inverse
  divided by $HW$). No 32x32 repeat is in this approved test.
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

## Reference implementation and static code

The candidate and independent reference implementation files already exist
in the draft PR. Their numerical behavior is **not validated by a formal run**.
The reference uses an explicit loop and direct accumulation; the candidate
uses independent vectorized complex multiplication and scatter-add. Both
must share only fixtures and conventions, not reduction code.

Static files in the current draft PR:

1. `tools/fd_nig_reference.py`: exhaustive pair enumeration, modular routing,
   loop reference, and fixture generation.
2. `tools/fd_nig_aggregation.py`: sparse/vectorized complex aggregation and
   optional Hermitian enforcement, with no inverse-FFT magnitude square.
3. `tools/tests/test_fd_nig_synthetic.py`: deterministic numerical and gradient
   tests listed below.
4. `tools/fd_nig_config.json`: frozen seed, grid, normalization, pair policy,
   tolerances, and budget; generated only after approval.

## Frozen numerical acceptance gates (scope-limited approval, 2026-10-12)

The project lead explicitly approved the exact criteria documented in
`Numerical_and_Memory_Freeze_Review.md`. They are now frozen as
experiment-local numerical gates, **not proof of their attainability** at
16x16. No tolerance may be relaxed after a failure without a new review,
a separately recorded deviation, and reapproval BEFORE any new formal run.

The independent loop reference sums 65,536 complex contributions at 16x16;
the previous 4x4/8x8 calibration did **not** establish 16x16 performance.
The precision-specific scale-aware errors, Hermitian raw-output limits,
autograd/finite-difference checks, and stress checks below are mandatory.

1. **Frequency-difference routing:** every enumerated pair lands in exactly one
   bin and the candidate route equals `(k-l) mod (H,W)` for 100% of pairs.
2. **Complex pairwise multiplication:** compare
   $C\,M(k)\operatorname{conj}(M(l))$ against an independently expanded
   real/imag calculation using the per-term **scale-aware** bound
   $|p_\mathrm{candidate}-p_\mathrm{reference}|
   \le a_\mathrm{tol}+r_\mathrm{tol}|p_\mathrm{reference}|$.
   Record maximum absolute differences separately.
3. **Complex scatter-add:** compare candidate and independent loop
   reference for all output bins, including zero, one, and many contributing
   pairs. A pure relative error is undefined when the reference bin is
   zero. Instead, define per-bin absolute difference
   `error[q] = abs(candidate[q] - reference[q])` and evaluate against
   `atol + rtol * scale[q]`. For a cancellation-resistant diagnostic,
   `scale[q]` is the independently accumulated sum of the absolute
   magnitudes of all pair contributions to bin q. Empty bins use the
   absolute tolerance. Suggested initial float32 values are
   `atol=1e-6` and `rtol=1e-5`; float64
   `atol=1e-12` and `rtol=1e-12`, **approved and frozen** for
   both per-term and zero-safe aggregation comparisons. Record maximum
   absolute error and cancellation-heavy-bin errors separately; the
   cancellation ratio is $|I_\mathrm{reference}(q)|/A_q$ for $A_q>0$.
4. **Conjugate symmetry, before projection:** on RAW Hermitian
   fixtures, $\max_q|\widehat I(q)-\operatorname{conj}(\widehat I(-q))|$
   is $\le 1e-10$ (complex128) or $\le 1e-5$ (complex64).
   DC and self-conjugate Nyquist imaginary magnitude is $\le 1e-10$
   (complex128) or $\le 1e-6$ (complex64). Check projection separately;
   it must never disguise a raw spectrum violation.
5. **Real inverse FFT:** `ifft2(\widehat I,norm="backward")`
   has maximum imaginary residual $\le 1e-10$ (complex128) or
   $\le 1e-5$ (complex64). Compare the reference and candidate real
   inverse outputs against the frozen numerical bounds. **No magnitude
   square** is performed.
6. **Gradient propagation:** with a scalar loss equal to the mean squared error
   of the real inverse-FFT output against a fixed real target, gradients
   must be finite for all active independent parameter components, with
   nonzero gradients verified on chosen nondegenerate active components.
   Zero gradients on masked, unused, or symmetry-constrained terms are
   permitted and must be documented. Centered finite-difference spot
   checks compare both independent real and imaginary parameter
   perturbations, with centered step $h=1e-6$, `atol=1e-5`,
   `rtol=1e-4`. Require at least one nonzero nondegenerate active real
   and imaginary component. Candidate/reference 8x8 gradients use
   `atol=rtol=1e-10`. Near-zero reference gradients require the
   absolute tolerance rather than division by zero.
7. **Finite/stability gate:** all intermediate and final real/imaginary values,
   losses, and gradients are finite for the normal fixture and a stress fixture
   scaled by $10^3$; no NaN/Inf and no runtime overflow.
8. **Sparse versus exhaustive:** on tiny $4\times4$ and $8\times8$
   grids where retained pairs equal exhaustive pairs, candidate/reference
   outputs and gradients must meet the frozen gates. At 16x16, use the
   first 256 lexicographic pairs **plus unique swapped partners**, indexing
   coefficients by those same pair indices. Test deterministic repeatability
   and pair-swap closure; never compare sparse versus dense outputs when
   pair sets differ. Test both binary and nonbinary masks.
   Primary 16x16 dense/symmetry/inverse/gradient gates use complex128;
   16x16 pair-product, aggregation, symmetry and inverse numerical gates
   additionally use complex64. No extra 32x32 run is approved.

The gate is pass only if every required test passes in two consecutive runs with
the same seed and the recorded environment. Any failed test blocks all later
training or MetalSet work and is recorded as a failed run if execution is later
authorized.

## Compute budget and artifacts (proposal)

The project lead approved a **120-second TOTAL wall-time deadline** across
both complete repetitions (2026-10-12). That is the maximum execution
budget, not 120 seconds per repetition. If the first attempt fails or exhausts
the deadline, stop and preserve all artifacts.

The project lead additionally approved (2026-10-12) the following
**monitored-RSS memory policy**. The acceptance metric is peak RSS summed
conservatively across the runner and live test-process tree, `<= 2 GiB`.
Monitor `/proc` process-tree RSS at intervals no greater than 100 ms and
fail/kill the test process group if the measured sum reaches `1536 MiB`
(1.5 GiB) or RSS measurement fails. Record each attempt peak, the overall
observed peak and `/usr/bin/time -v` maximum RSS and cgroup memory
events. A measurement exceeding 2 GiB is a failure even if the watchdog
did not stop it. **Do not use RLIMIT_AS** as a substitute for RSS.
This userspace watchdog is a conservative operational guardrail and
**not an independently verified strict 2 GiB kernel-enforced cap**.
No silent change of limits after any failure.

Resource setup: CPU-only, at most two CPU threads, one test process at a
time, at most two repetitions, no GPU, network data, training or external
simulator. Expected artifacts are immutable per-attempt stdout/stderr,
JUnit per-test outcomes, exit status, stopwatch/resource logs, a JSON
summary, environment/version capture, fixture/config/code hashes and
gradient diagnostics. The accepted scientific interpretation is bounded
to numerical implementation consistency; it is not lithography validation.

## Unresolved prerequisites

1. **Resolved, 2026-10-11:** Project lead explicitly approved treating
   `EXP-0003` as a `METHOD-0002` method-local numerical feasibility check,
   without creating `HYP-0004`. This does not approve test execution.
2. **Resolved for numerical/resource settings only, 2026-10-12:**
   Project lead explicitly approved the shared 120-second TOTAL budget,
   the full numerical acceptance criteria, grid/seed/FFT/sparse policy,
   and the monitored process-tree RSS memory policy. These settings
   are frozen within EXP-0003 and may not be modified silently. This
   **does not approve** the full Plan, formal execution, or use of
   as-yet-unreviewed runner code.
3. **Still blocked:** Complete static runner/test coverage implementation,
   code review (including process-tree RSS monitoring and memory guard
   behavior), artifact/provenance acceptance, and frozen code/environment
   identifiers. The launcher remains unexecuted and unvalidated.
4. **Still blocked:** Formal approval of this Plan (`approval_status`) before
   any test execution.

Until all four prerequisites are resolved, `EXP-0003` remains `draft-blocked`.
