---
schema_version: "1.0"
id: EXP-0003-FREEZE-REVIEW
type: experiment-local-review
title: "EXP-0003 numerical gates and memory policy: project-lead decision draft"
lifecycle_status: draft
authority_class: working
authority_scope: pre-experiment-proposal-only
created_by: ai
content_origin: ai-assisted
created_at: 2026-10-12
updated_at: 2026-10-12
owner: project-lead
review_status: unreviewed
experiment_ids: [EXP-0003]
method_ids: [METHOD-0002]
exclude_from_synthesis: true
---

# Numerical gates and memory policy: review for project-lead freeze

**Not approved or frozen. No permission to execute EXP-0003.**
This file is a review-ready proposal, not a formal Plan amendment or a Run.
The project lead explicitly approved only a **120-second total** wall-time
budget across up to two repetitions (2026-10-12). The following numerical
and memory choices still need explicit approval and implementation review.

## Existing calibration: evidence boundary

Pre_Experiment_Calibration.md preserves 4x4/8x8 CPU-only diagnostic values
from commit 8965161, not a formal 16x16 execution. The maximum 8x8
candidate/reference spectral differences were 2.27817331817e-13
(complex128) and 4.57763671875e-05 (complex64). The diagnostic
zero-safe excess was negative under the *proposed* bounds, and peak process
RSS was about 235 MiB. These observations do not calibrate every 16x16
condition, stress case, or gradient test.

## Recommended numerical contract (requires approval)

- Grid: circular 16x16, unshifted DFT frequency order, torch.fft.fft2/ifft2
  with norm="backward" (forward unnormalized, inverse divided by H*W).
  Use seed 20261011. Fixed c=[1], deterministic synthetic binary/nonbinary
  mask fixtures. No DATA-0001, training, or simulator calls.
- All-pairs reference: 65,536 lexicographically ordered pairs;
  q=(k-l) mod (16,16). Candidate sparse policy: first 256
  lexicographic base pairs and unique swapped partners, preserving the
  base prefix. Do not compare sparse and dense outputs if pairs differ.
- Precision: complex128 required primary 16x16 acceptance evaluation;
  complex64 required secondary diagnostic/acceptance evaluation on
  prescribed small or selected fixtures. Record both dtypes explicitly.
- Routing: exact integer agreement for every enumerated pair; correct
  counts including empty/multiple contributing bins.
- Pair product: compare C*M(k)*conj(M(l)) against independently expanded
  real/imag reference. Recommended scale-aware bound on each term:
  abs(candidate-reference) <= atol + rtol*abs(reference).
  complex128: atol=1e-12, rtol=1e-12.
  complex64: atol=1e-6, rtol=1e-5.
  This *replaces* the Plan's proposed absolute-only per-pair maximum
  threshold, which can reject correct high-amplitude float32 products.
  Always record absolute maximum error as a diagnostic.
- Aggregation (candidate vs independent loop, identical pair lists):
  define A_q=sum_{pairs routed to q}|reference pair contribution|.
  abs(candidate_q-reference_q) <= atol + rtol*A_q for **every** bin.
  complex128: atol=1e-12, rtol=1e-12.
  complex64: atol=1e-6, rtol=1e-5.
  For A_q=0 the limit reduces to atol. Report max absolute difference,
  maximum zero-safe excess, empty-bin and genuine cancellation-heavy-bin
  diagnostics separately. Do not replace A_q with |reference_q|.
- Hermitian fixture: check RAW (unprojected) spectrum, requiring
  max_q |Ihat(q)-conj(Ihat(-q))| <= 1e-10 in complex128,
  <= 1e-5 in complex64; self-conjugate DC/Nyquist imaginary magnitude
  <= 1e-10 (complex128), <= 1e-6 (complex64).
  Check projection separately; never let projection conceal an erroneous
  raw assembly.
- Real inverse FFT: max imaginary residual <= 1e-10 (complex128)
  and <= 1e-5 (complex64). Compare candidate/reference real IFFT output
  against the declared numerical bounds. Do not apply a magnitude square.
- Gradients: all required active gradient components finite; at least
  one prescribed nondegenerate active real component and one active
  imaginary component independently show nonzero gradients. Unused/
  zero-spectrum coefficients may correctly produce zero gradients.
  Check both real and imaginary parameter perturbations using centered
  finite differences h=1e-6; use atol=1e-5, rtol=1e-4
  on finite-difference-vs-autograd values. Also compare 8x8 reference
  and candidate gradients with atol=rtol=1e-10.
- Stability: finite real/imag products, spectra, inverse outputs, loss
  and gradients on normal and x1000 stress fixtures. Check exact
  deterministic pair selection/swap closure and two consecutive complete
  runs, with no failures/errors/skips or missing evidence. No post hoc
  threshold changes or silent reruns.
- Two complete test repetitions must fit within one shared 120-second
  wall-time deadline, approved separately by the project lead.

## Recommended memory policy (requires approval)

**Decision metric:** peak process-tree resident-set size (RSS) including
runner and child test processes, <= **2 GiB total**. Record in MiB and
bytes, per-attempt peaks and overall peak, and Linux cgroup memory events.
The documented Cloud container has an 8 GiB cgroup memory limit.

**Enforcement:** remove the 2 GiB RLIMIT_AS cap, which constrains *virtual
address space* and is not a valid proxy for peak RSS. Use a watchdog to
sample /proc process-tree RSS at <= 100ms cadence, conservatively summing
the RSS of live experiment processes. Stop the entire child process group
and mark resource failure on approaching **1.5 GiB (1536 MiB)** or if
measurement fails. After each attempt, record /usr/bin/time -v max RSS;
if the measured maximum is > 2 GiB, mark budget failure even if the
watchdog did not prevent overshoot. The 1.5 GiB early-stop is a
conservative operational guardrail, not proof of a strict kernel-enforced
2 GiB maximum. No silent limit increase or replacement by RLIMIT_AS.
If a dedicated writable cgroup v2 with memory.max=2GiB is available and
independently reviewed, a strict kernel cap may be substituted before
approval; otherwise explicitly disclose the watchdog's non-hard nature.

No 2 GiB hard enforcement is currently verified; choosing this policy
requires static runner changes and independent review before execution.

## Remaining implementation/review blockers

1. The current pytest module does not yet apply the config tolerances
   consistently: multiple numeric tolerances remain hardcoded, and
   float32 is not exercised against every proposed precision-specific
   gate. Wire the approved acceptance contract and report per-gate
   numerical measurements, not only test booleans.
2. The finite-difference test checks the real parameter perturbation
   only. Add a chosen nondegenerate imaginary-parameter perturbation
   and explicit active/unused gradient controls.
3. The Hermitian DC/Nyquist check currently uses the **projected**
   spectrum; add the raw unprojected check at the specified precision.
   Add a clear binary-mask fixture where the Plan requires it.
4. Implement process-tree RSS monitoring, early stop, and peak reporting;
   remove RLIMIT_AS only if this new memory policy is approved. The
   existing guarded runner is **not yet runtime-validated**.
5. Preserve SHA-256 provenance, unique append-only Run IDs, immutable
   per-attempt logs and a shared 120-second deadline. Independently
   review the suite, protocol, runner and approved commit before any run.

## Authority boundary

A separate explicit project-lead sign-off on **the exact choices above**
is required before changing Plan/config acceptance fields to frozen.
Even after a freeze, the formal EXP-0003 Plan approval and the execution
authorization remain separate, ungranted gates. No HYP-0004, ADR,
METHOD-0002 selection, DATA-0001 freeze or evidence promotion is implied.

Wiki projection: no projection needed; this is experiment-local numerical
and operational design, not a new human-facing research explanation.
