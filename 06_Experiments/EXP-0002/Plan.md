---
id: EXP-0002
title: "Architecture 3 kernel-prediction optical-renderer feasibility prototype"
experiment_state: draft-blocked
approval_status: not_requested
method_ids: [METHOD-0001]
data_ids: [DATA-0001]
source_ids: []
hypothesis_ids: [HYP-0001, HYP-0002]
pc_ids: []
owner: project-lead
created: 2026-09-21
last_updated: 2026-09-21
---

# Research question

Can a conditioned U-Net predict a kernel representation `B` from `(x_t, m, t, alpha)` such that an explicit differentiable Fourier renderer produces a useful clean-image estimate `x_hat0`? The first test evaluates software and optimization feasibility; it does not claim that the learned kernel is already a physically calibrated optical kernel.

# Scope of the first run

Run only the reference branch from the latest architecture. Use one predicted complex kernel (`J=1`, two real channels for real/imaginary parts) and the path `FFT(mask) -> multiply by kernel -> IFFT -> intensity -> normalization`. Do not run the correction branch, multi-step sampling, the Corrector, or any projection rule. Those components have no registered physical-constraint contract.

The optical condition `alpha` is required by the model interface but is not present in DATA-0001. Set it to one documented constant for this plumbing run and label the result “single implicit condition.” Do not interpret this as condition generalization.

# Variants and controls

1. **Direct-image baseline:** reuse the external direct-image training plumbing and a one-channel image-output U-Net. This checks that the selected data and split can train at all.
2. **Kernel prototype:** new conditioned U-Net outputting `B` and new differentiable renderer. Use the same matched pairs and preprocessing as the baseline.
3. **Renderer-only check:** fixed synthetic masks and hand-constructed kernels to verify FFT/IFFT shapes, complex arithmetic, normalization, and nonzero gradients before training.

The direct-image checkpoint from the external repository must not be loaded into the kernel prototype; its input and output contracts are different.

# Ordered execution gates

1. **Data gate:** re-audit matched filenames, regenerate or verify train/validation/test manifests, record filtering of 49 unmatched files, and run a pattern-family leakage check.
2. **Renderer gate:** test identity-like and low-pass kernels on synthetic tensors; check reconstruction shape, finite values, gradient flow, and deterministic output.
3. **Tiny overfit gate:** train on one sample, then 16 samples, until the model can lower training loss. Save kernel tensors and rendered images at each checkpoint.
4. **Small controlled run:** use a fixed small subset and compare the kernel prototype with the direct-image baseline under the same preprocessing.
5. **Full run:** execute only after the preceding gates pass and the experiment plan has been frozen and approved.
6. **Later diffusion run:** add multiple timesteps and sampling only after the one-step kernel path is stable. The correction branch remains a separate experiment once a physical-constraint record exists.

# Proposed measurements

Record MSE, MAE, SSIM, edge/contour error, FFT amplitude statistics, finite-value rate, training time, peak memory, and rendered examples. Record the exact model configuration, manifest hashes, code revision, random seeds, and kernel output tensors. No success threshold is preregistered yet; thresholds must be added before the plan is frozen.

# Implementation contract still required

Before coding, freeze: FFT grid size; padding/cropping and frequency ordering; `B` real/imaginary channel convention; kernel normalization and clipping; intensity normalization; image range; batch and patch size; timestep sampling rule; constant `alpha` encoding; optimizer and training budget; and the baseline comparison protocol. For `J>1`, also freeze the component-combination rule and whether any weights are fixed or predicted. The first `J=1` run intentionally avoids that unresolved decision.

# Blockers

This plan is blocked because DATA-0001 is not frozen, no simulator/optical-condition contract exists, the external kernel-like assets have unknown semantics and shapes, the project has no conditioned kernel U-Net or renderer implementation, and no physical-constraint record exists for Stage 2. No training execution is authorized by this draft.

# Expected artifacts

The eventual run should produce a data audit, frozen manifests, configuration file, code revision, renderer gradient report, checkpoints, kernel visualizations, rendered-image comparisons, metrics, and a run report linked to this experiment. Until then, this file is a preparation plan only.
