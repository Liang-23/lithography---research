---
schema_version: "1.0"
id: EXP-0003-CAL-0001
type: pre-experiment-calibration-record
lifecycle_status: draft
authority_class: working
authority_scope: diagnostic-only
created_by: ai
content_origin: experiment
created_at: 2026-10-11
updated_at: 2026-10-11
owner: project-lead
review_status: unreviewed
core_alignment: pass
experiment_ids: [EXP-0003]
method_ids: [METHOD-0002]
exclude_from_synthesis: true
---

# PRE-EXPERIMENT CALIBRATION — FD-NIG

This diagnostic record preserves the authorized 4×4 and 8×8 calibration. It is not a formal EXP-0003 run, does not change `experiment_state` or `approval_status`, and is not verified Evidence.

The exact measured report and provenance are preserved below. The reproducibility script is [`pre_experiment_calibration.py`](pre_experiment_calibration.py). It was run at commit `8965161e3997fc0f62dca46edece65fffb9ac28f`.

- Python: `3.12.14` (`/workspace/fd-nig-venv/bin/python`)
- PyTorch: `2.5.1+cpu`
- Device: CPU, `OMP_NUM_THREADS=2`, `MKL_NUM_THREADS=2`
- Seed: `20261011`
- Grids: 4×4 and 8×8 only
- Dtypes: complex64 and complex128
- Command: `OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 timeout --signal=KILL 120s bash -c 'ulimit -v 2097152; /workspace/fd-nig-venv/bin/python /tmp/fd_nig_calibration.py'`
- Peak RSS: `240832 kB` (~235 MiB)
- Repetitions: one calibration pass plus one immediate candidate repeatability pass

## Exact results

| Grid | dtype | max abs candidate/reference | max abs vs high-precision reference | max zero-safe excess | cancellation-bin error / scale | empty bins | ref s | candidate s | repeatable |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 4x4 | complex64 | 7.62939453125e-06 | 1.5728399375802837e-05 | -4.992561881e-04 | 0.0 / 49.825618743896484 | 0 | 0.002192668 | 0.000356198 | yes |
| 4x4 | complex128 | 7.105427357601002e-15 | 7.105427357601002e-15 | -5.0823842767954397e-11 | 1.7763568394002505e-15 / 49.825619124793796 | 0 | 0.002153589 | 0.000079548 | yes |
| 8x8 | complex64 | 4.57763671875e-05 | 1.3037114695190207e-04 | -2.589389681816101e-03 | 3.84438408218557e-06 / 259.2234191894531 | 0 | 0.034983978 | 0.000437578 | yes |
| 8x8 | complex128 | 2.278173318171838e-13 | 2.278173318171838e-13 | -2.6021697565980664e-10 | 6.404745667978753e-15 / 259.2233804054746 | 0 | 0.035163282 | 0.000347735 | yes |

The zero-safe excess is `abs(candidate-reference) - (atol + rtol*scale)` using the diagnostic proposal values. Negative values are within those diagnostic bounds. Float32-versus-high-precision differences are rounding diagnostics, not implementation errors.

No failures or interruptions occurred. No result is promoted to Evidence or a formal run. Proposed tolerances remain proposals and are not frozen or approved.

## Subsequent static-review clarification (2026-10-12)

The preserved numerical measurements above were produced at the explicitly
recorded **original calibration commit** and have not been recomputed.
The original calibration's reported `cancellation-bin error / scale` chose a
bin with the smallest positive absolute-contribution scale; this is **not**
a validated measure of destructive cancellation. The later interim revision
selected by error-to-scale ratio, which also does **not** measure cancellation.
The now-revised, **unexecuted** reproducibility script separates
`cancellation_ratio = abs(reference_bin) / sum(abs(contributions))` from
`error_to_scale_ratio = abs(candidate-reference) / sum(abs(contributions))`.
No revised calibration outcomes are claimed, and historical values above
must not be silently relabeled or substituted.
