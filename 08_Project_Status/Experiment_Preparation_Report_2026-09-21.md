---
title: "Architecture 3 experiment preparation and lithobench reuse audit"
type: report
status: candidate-preparation
date: 2026-09-21
---

# Finding

The latest architecture is a valid candidate for a staged feasibility study, but it is not yet executable as a formal experiment. The central idea is now unambiguous: a conditioned U-Net predicts a kernel tensor `B`; an explicit differentiable renderer performs FFT, frequency-domain multiplication, IFFT, intensity conversion, and normalization. The first implementation should use one predicted complex kernel (`J=1`) so that no separate kernel-bank weighting rule is needed.

The figure still contains three underspecified operations: the exact shape and representation of `B`, the meaning of “weighted superposition” when more than one kernel is used, and the Stage 2 Corrector/projection rule. These are recorded as blockers rather than silently filled in.

# External repository audit

`D:\project\lithobench-main` contains useful infrastructure but not the proposed model. Reusable pieces include matched `pixelILT`/`litho` loading, deterministic split handling, patch cropping, training/validation loops, checkpointing, MSE/SSIM/gradient losses, and a tiny direct-image `Stage4SmokeUNet` that can serve as a baseline. `production_unet.py` is empty. The tiny U-Net has one image input and one image output; it has no timestep embedding, optical-condition input, kernel head, complex arithmetic, or Fourier renderer. Existing checkpoints therefore cannot be reused for the kernel model.

The repository also contains 24 `fh*.bin` files in each of `kernel/M1OPC` and `kernel/M1OPC_def`, plus several `.pt` kernel-like files. No decoder or integration code was found, and their shapes/semantics were not verified. They are registered as leads for a later simulator audit, not as ground truth kernels for EXP-0002.

# Data readiness

The external MetalSet audit reports 16,423 matched pairs, 49 `pixelILT`-only files, 2048×2048 grayscale images, binary `pixelILT`, and continuous `litho`. Existing split manifests are useful starting points but are not project-frozen. There is no optical-condition field, so the first run can only use a documented constant `alpha` and must be described as a single implicit condition. A fresh audit, unmatched-file policy, and pattern-family leakage check are required before freezing DATA-0001.

# Recommended work order

1. Freeze the data contract and manifests for DATA-0001.
2. Implement and unit-test the FFT renderer independently of the U-Net.
3. Build a new conditioned U-Net with a `J=1`, two-channel real/imaginary kernel head.
4. Overfit one sample and then a tiny subset; save predicted kernels and rendered images.
5. Compare with the direct-image baseline using the same data adapter.
6. Only after these gates pass, decide whether to add multiple kernels, a combine/weight rule, multiple diffusion timesteps, and finally the correction branch.

The detailed candidate method and blocked plan are recorded in `METHOD-0001` and `EXP-0002`. No code was added yet because the data and tensor contracts are not frozen; implementing before those gates would create an unreviewable experiment.

# Governance result

No file literally named `modern dominance governance.md` exists in the project. The canonical governance files used for this update were `AGENTS.md`, `00_Project_Core/Core_Governance.md`, and the routed status/registry instructions. No Core file was changed. These rules require candidate methods and registered data to remain explicitly unselected until contracts and plans are reviewed. No Wiki projection is needed yet: this report records a candidate design and preparation state, not a verified scientific result.
