---
id: METHOD-0001
title: "Architecture 3: kernel-predicting differentiable optical renderer"
method_type: candidate
lifecycle_status: draft
authority_class: working
method_state: candidate
content_origin: ai-assisted
owner: project-lead
core_alignment: pass
hypothesis_ids: [HYP-0001, HYP-0002]
data_ids: [DATA-0001]
experiment_ids: [EXP-0002]
decision_ids: []
review_status: unreviewed
created: 2026-09-21
last_updated: 2026-09-21
---

# Purpose and status

This record translates the latest architecture figure into an implementable candidate. It is not a selected method and does not authorize an experiment. The first implementation target is a one-step feasibility prototype that tests whether a U-Net can predict an optical kernel representation and whether a differentiable Fourier renderer can turn that representation into a clean-image estimate.

The current interpretation preserves the user's original direction: the U-Net predicts the kernel representation itself. It does not predict a fixed kernel-bank weight vector. A fixed bank and a separate mixture-weight head are therefore not part of the first prototype.

# Candidate interface

The U-Net receives four inputs:

| Input   | Meaning                                              | First-prototype status                                                                                           |
| ------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `x_t`   | noisy image state at timestep `t`, shape `[N,1,H,W]` | generated from the litho target for a one-step test                                                              |
| `m`     | spatial-domain mask, shape `[N,1,H,W]`               | available from the `pixelILT` image                                                                              |
| `t`     | diffusion timestep, shape `[N]`                      | required input, but only a small fixed set of timesteps is used first                                            |
| `alpha` | optical-condition vector, shape `[N,d_alpha]`        | ==no condition metadata exists in DATA-0001; use a documented constant only for the first single-condition run== |

The supervised target is `x_ref`, the matched litho image. In the current data adapter, `x_ref` is the `litho` image and `m` is the `pixelILT` image. The arrow `x_ref -> reconstruct -> x_t` in the figure should be implemented as a diffusion noising operation, not as a learned reconstruction block:

$$x_t = q_t(x_{ref},\epsilon,t).$$

`x_ref` is a training target and is not an input to the U-Net at inference time.

# What the U-Net outputs

The output is a predicted kernel tensor `B`, not an image and not a bank-weight vector. The general interface is:

$$B = U_\phi(x_t,m,t,\alpha),$$

$$B \in \mathbb{R}^{N\times J\times C_B\times H_f\times W_f}.$$

`J` is the number of predicted kernel components. `C_B=2` is the proposed representation for a complex frequency-domain kernel (real and imaginary channels). If a later experiment chooses a real-valued transfer function, `C_B=1` may be used, but that is an experiment-level decision and must be recorded before execution. `H_f,W_f` are the FFT-grid dimensions.

For the smallest smoke test, set `J=1` and `C_B=2`. This gives one predicted complex kernel and removes the unresolved multi-kernel combination rule. It still tests the central claim that the U-Net predicts a kernel used by an explicit optical renderer. Increasing `J` is a later ablation, not a prerequisite for the first run.

# Differentiable optical renderer

For the first prototype, the renderer is explicit and differentiable:

1. Convert the mask to the frequency domain: `M_hat = FFT(m)`.
2. Convert the real/imaginary channels of `B` to a complex kernel `K_B`.
3. Multiply in the frequency domain: `E_hat = M_hat * K_B`.
4. Apply the inverse transform: `e = IFFT(E_hat)`.
5. Convert the complex field to the chosen image quantity, initially `abs(e)^2`, then normalize with a recorded rule to obtain `x_hat0`.

For `J=1`, there is no weighted superposition. The figure's “Weighted superposition” block should therefore be renamed “intensity and normalization” in the first-prototype diagram. For `J>1`, a separate combine rule must be specified before implementation, for example a fixed sum of component intensities or a predicted nonnegative weight vector. The current method intentionally leaves that choice open and does not silently invent weights.

The clean-image estimate is therefore:

$$\hat{x}_0 = R(m,B) = \operatorname{Normalize}\left(\left|\mathcal{F}^{-1}\{\mathcal{F}(m)\odot K_B\}\right|^2\right).$$

The FFT, frequency-domain multiplication, IFFT, intensity operation, and normalization belong to `R`, not to the U-Net.

# First-prototype training path

The first experiment should test only the reference branch:

```text
litho target x_ref ── q_t ──> x_t
                                  │
mask m ────────────────────────────┤
timestep t ────────────────────────┤──> conditioned U-Net ──> B
optical condition alpha ───────────┘                         │
                                                            v
                                      FFT(m) × K_B → IFFT → intensity → x_hat0
                                                            │
                                             compare with x_ref using L_ref
```

Use a full-image MSE for the first wiring test. A masked loss is allowed only after the project defines and records a valid loss-region field; DATA-0001 currently does not provide one in its loader contract. The correction branch, multi-step sampling, corrector, projection rule, and `L_corrected` are future work and must not be included in the first feasibility run.

# Reuse and rebuild boundary

The external `lithobench-main` repository supplies reusable dataset pairing, deterministic split handling, patch cropping, training loops, checkpointing, MSE/SSIM/gradient losses, and a tiny direct-image `Stage4SmokeUNet`. It does not supply the required conditioned kernel-prediction U-Net, timestep embedding, optical-condition encoder, complex-kernel output head, or Fourier optical renderer. The production U-Net module is empty. Therefore the first kernel prototype requires a new model and renderer implementation; reusing the direct-image checkpoint would be invalid because its input and output contracts differ.

# Required decisions before implementation

The following items are still open and must be frozen in the experiment plan: FFT grid and padding/cropping rule; `J` beyond the first `J=1` smoke test; complex versus real kernel representation; kernel normalization and clipping; intensity normalization; the meaning and source of `alpha`; and the multi-component combine rule. The Stage 2 corrector remains blocked until a registered physical-constraint record exists.

# Risks and interpretation limits

DATA-0001 has no recorded optical-condition variation, so a constant `alpha` can test plumbing but cannot demonstrate condition generalization. The external kernel-like files have no verified decoder or shape contract and are not used as ground truth in this candidate. A successful first run would establish software and gradient feasibility only; it would not establish a physical optical model or advanced-node accuracy.
