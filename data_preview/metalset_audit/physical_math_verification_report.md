# Physical and Mathematical Verification Report

**Status:** inspection artifact, not verified Evidence  
**Scope:** read-only review of MetalSet data contracts, METHOD-0001 / Architecture 3, and FD-NIG. No model or experiment was executed. No scientific record was changed.

## 1. MetalSet observed properties

The prior filename-stem audit reports these directory counts:

- `pixelILT`: 16,472 PNG files.
- `levelsetILT`: 16,472 PNG files.
- `litho`: 16,423 PNG files.
- `target`: 16,472 PNG files.
- `resist`: 16,422 PNG files.
- `printed`: 16,422 PNG files.

Sampled `pixelILT` and `litho` files were 2048×2048, single-channel PNGs in mode `L`. The prior audit reports `pixelILT` values as binary 0/255 and `litho` as continuous grayscale with approximately 150 observed values and a reported range 0..149. These statements are file-level observations.

Filename-stem intersection gives 16,423 matched `pixelILT/litho` pairs and 49 `pixelILT)-only stems. Existing split manifests contain 13,138 train, 1,642 validation, and 1,643 test rows. `levelsetILT` has the same file count as `pixelILT`, but a current local recheck is still required before claiming that every selected sample forms a triplet.

The appearance or grayscale range of `litho` does not identify it as aerial intensity. The available records do not establish physical units, pixel pitch, calibration, or simulator stage.

## 2. Physical target interpretation and confidence boundary

### Directly observed / software-derived

- PNG categories and filename stems.
- Image dimensions and channel mode for sampled `pixelILT/litho`.
- Binary-looking `pixelILT) values and continuous-looking `litho) values.
- Loader behavior: grayscale conversion and division by 255.
- Pairing and split counts.

### Documentation claims

The current baseline treats `pixelILT` as the model input and `litho` as the machine-learning label. The dataset map describes `target` as an ideal pattern, `resist` as a later simulation output, and `printed` as a final printed result. These descriptions are useful dataset-role documentation, but they are not a complete generator proof.

### Mathematical inferences

A continuous grayscale target can be used as a regression target. A binary input can be Fourier transformed. Neither fact proves that the target is optical intensity or that a single transfer kernel is physically valid.

### Unverified physical interpretations

The current cloud-accessible records do not prove that `litho` is aerial intensity, resist, wafer image, or any other particular stage. No generator equation, simulator version, optical/process parameter table, or exact source-to-file mapping was available. Physical classification remains unresolved.

## 3. Data support by contract level

| Contract level | Current support | Missing evidence |
|---|---|---|
| Software-only forward image prediction | Supported as a paired-image plumbing task | current local recheck, frozen manifest, leakage policy |
| Synthetic Fourier aggregation / renderer checks | Supported independently of MetalSet semantics | explicit FFT convention, padding/cropping, normalization |
| Aerial-intensity spectral supervision | Not supported as a physical claim | verified target stage, simulator output definition, units/calibration |
| Physically meaningful optical conditioning | Not supported | condition schema and coverage: wavelength, NA, pupil, focus, dose, process, etc. |
| Controlled comparison of both architectures | Conditionally supportable as software comparison | common target, same information at inference, same preprocessing/splits/budgets, output-validity contracts |

## 4. FD-NIG mathematical review

Let the discrete FFT grid be \\(\mathcal K = \mathbb Z_{N_x}\times\mathbb Z_{N_y}\\), with all index arithmetic modulo \\(N_x,N_y\\). For mask spectrum \\(\hat M(k)\\), the proposed aggregation is

\\[
\hat I(q)=\sum_{k-l=q} C_\theta(k,l,c)\,\hat M(k)\,\overline{\hat M(l)}.
\\]

### Requirements

1. **Indexing:** state whether \\(q=k-l\\) or \\(q=l-k\\); use modulo-grid arithmetic consistently; define fftshift ordering separately from algebraic indices.
2. **Complex coefficients:** \\(C_\theta\\) is an effective complex interaction coefficient. It is not automatically a physical pupil, transfer function, or coherent mode.
3. **Conjugate symmetry:** for a real spatial output, require \\(\hat I(-q)=\overline{\hat I(q)}\\). This can be enforced by paired parameter tying, explicit symmetrization, or a real-valued output parameterization.
4. **IFFT convention:** document forward/inverse normalization. With the common unnormalized forward FFT and \\(1/N\\) inverse FFT, coefficient magnitudes and loss scales differ from orthonormal FFTs.
5. **Nonnegativity:** real-valued IFFT output is not enough for intensity. Arbitrary complex \\(C_\theta\\) can yield negative spatial pixels. Use an explicit nonnegative map or an intensity construction if nonnegativity is part of the target contract.
6. **Pair coverage:** all retained \\(q\\) nodes need defined coverage. Sampling pairs requires known inclusion probabilities and unbiased or deliberately normalized aggregation; otherwise frequency-dependent bias is introduced.
7. **Gradient propagation:** the map is differentiable through FFT, conjugation, complex multiplication, coefficient generation, summation, and IFFT, provided no hard discrete sampling is made dependent on trainable values. Fixed or reparameterized sampling is required for stable gradients.
8. **Output target:** decide whether supervision is on \\(\hat I\\), spatial real output, nonnegative output, or multiple views. Spectral loss alone does not enforce an admissible spatial intensity unless the output constraints are included.

### Complexity

With \\(N_f\\) retained Fourier bins, dense ordered pairs cost \\(O(N_f^2)\\) pair evaluations and memory \\(O(N_f^2)\\) if materialized. With \\(P\\) sampled pairs, pair processing is \\(O(P)\\) plus aggregation and coefficient-network cost, with \\(O(P)\\) pair-index/message memory. This is an architectural choice, not a mathematical identity.

### Pair product and physical interpretation

The product \\(\hat M(k)\overline{\hat M(l)}\\) is quadratic and intensity-like in form, but arbitrary learned coefficients do not guarantee a physically valid intensity. Low-rank coherent-mode learning is not required by this direct-pairwise construction; it is a separate constrained baseline.

## 5. Architecture 3 / METHOD-0001 review

The proposed J=1 prototype can be written schematically as

\\[
B=G_\theta(m,\text{conditions},\ldots),\qquad
E=\mathcal F^{-1}\{\mathcal F(m)\odot B\},\qquad
I=|E|^2.
\\]

### Mathematical consistency conditions

- Define whether \\(B\\) is a full complex spectrum, a spatial kernel transformed internally, or a real/imaginary pair.
- Freeze FFT normalization, frequency ordering, padding, and whether multiplication is circular convolution in the spatial domain.
- \\(I=|E|^2\\) is real and nonnegative by construction, but this only makes the output intensity-like; it does not prove that \\(B\\) is an optical transfer function.
- State output normalization and crop coordinates. Cropping after rendering is different from cropping before FFT because of boundary/circular-convolution effects.
- FFT, complex multiplication, IFFT, magnitude-squared, and standard normalizations are differentiable. Hard thresholding or data-dependent discrete event selection is not smoothly differentiable.
- If \\(B\\) is generated from \\(x_t\\) and \\(x_t\\) is derived from the target \\(x_{ref}\\), target information enters inference. A deployed predictor cannot obtain target-derived \\(x_t\\) from only mask and conditions. Target-independent inference therefore requires either (a) a mask/condition-only generator, or (b) a clearly defined diffusion sampling process whose state is generated without the target.
- A constant condition can test wiring but cannot test optical/process-condition generalization.

## 6. Common dataset and inference requirements

Before a fair architecture comparison:

1. Freeze one target stage and document its provenance.
2. Use identical matched stems, split boundaries, normalization, padding, crop policy, and target resolution.
3. Give both models exactly the same information at inference; do not provide target-derived \\(x_t\\) to one model only.
4. Define condition variables, units, ranges, and in-distribution/OOD protocol. The current data record has no condition metadata.
5. Compare spatial error, spectral error, edge/gradient error, output validity, parameter count, peak memory, and inference time under a declared budget.
6. Keep `levelsetILT` either out of both models or include it symmetrically as an alternative input; do not silently mix mask types.
7. Preserve the 49 unmatched `pixelILT` files and document the filtering rule for any supervised subset.

## 7. Minimum synthetic validation plan

These are numerical correctness gates, not lithography experiments.

### Shared renderer checks

- Constant and delta masks with analytically predictable FFTs.
- Random complex kernel with a reference NumPy/PyTorch implementation.
- Forward finite-value checks and finite-difference gradient checks.
- Explicit test of normalization and crop coordinates.
- Translation test to expose circular-convolution or padding mistakes.

### Architecture 3 J=1

- Set fixed known \\(B\\) and compare FFT/IFFT output to a reference implementation.
- Verify \\(I=|E|^2\\) is real and nonnegative.
- Check gradient flow to real and imaginary parts of \\(B\\) and to the mask.
- Test target-independent inference by removing any target-derived \\(x_t\\).

### FD-NIG

- Enumerate a tiny grid (for example 4×4 or 8×8) and compare explicit pair loops with the routed implementation.
- Test modulo frequency-difference indexing and fftshift/unshift conventions.
- Verify conjugate-symmetry enforcement produces a real IFFT.
- Test empty and partially covered \\(q\\)-bins, pair-count normalization, and deterministic sampled-pair reproducibility.
- Check nonnegativity behavior separately; it is not implied by real-output symmetry.
- Check gradients through complex coefficients, conjugation, pair products, aggregation, and IFFT.

Passing these gates establishes software/numerical correctness only. It does not establish aerial-image accuracy, physical validity, or superiority of either architecture.

## 8. Decisions requiring user approval

- Whether the local dataset license/confidentiality permits uploading up to six derived PNG previews to the private repository.
- Whether `litho` should remain an unresolved generic image target or be admitted as a named physical stage after generator evidence is found.
- The common output contract and whether `levelsetILT` participates in the comparison.
- The FD-NIG real/nonnegative output mechanism and pair-sampling policy.
- The target-independent input contract for METHOD-0001 / Architecture 3.

No Method selection, Evidence promotion, ADR creation, or experiment authorization is implied by this report.

## 9. Recommended next research action

Perform a local, read-only provenance pass over the original MetalSet documentation and generation code, without executing unknown scripts. Record the exact source files, simulator configuration, target definitions, and scaling operations needed to classify `litho`. Only after that review should a user-approved local preview package be generated and, if licensing permits, uploaded.
