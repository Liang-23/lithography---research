---
id: EV-0007
type: evidence-record
title: "Official LithoBench simulator distinguishes aerial and printed outputs"
authority_scope: atomic-claim-only
owner: project-lead
reviewed_by:
approved_by:
approval_ref:
lifecycle_status: draft
authority_class: working
content_origin: mixed
review_status: unreviewed
evidence_state: unverified
created_at: 2026-10-11
updated_at: 2026-10-11
source_ids: [SRC-0014, SRC-0015]
data_ids: [DATA-0001]
exclude_from_synthesis: true
---

# EV-0007: bounded atomic claim

## Claim

In the inspected official LithoBench simulator implementation, `LithoSim.sim` returns distinct pre-threshold aerial-intensity tensors and post-sigmoid printed tensors for the nominal and modeled process-corner settings.

## Grounding and applicability

- Primary registered Source: `SRC-0014`, official code at Git commit `9c74e82218e377eaf6d02d113fc1ce6e36c92aa6`.
- Exact locators: `pylitho/exact.py`, `_LithoSim.forward`, `LithoSim.sim` (aerial and printed output calculations); `lithobench/dataset.py`, `filesLithoSim` and `DataLitho.__getitem__` (related loader-channel mapping).
- Supporting background source: `SRC-0015`, official NeurIPS 2023 LithoBench paper, benchmark description.
- Evidence form: source-code observation and bounded interpretation, not independent validation of the user's local MetalSet image generation.
- Supports: The official simulator implementation distinguishes optical aerial fields from sigmoid-transformed printed responses.
- Does **not** establish: The user's local `MetalSet/litho/*.png` files were generated using this exact simulator or revision, nor their absolute physical units, scaling, correspondence to process corners, or suitability as verified aerial-intensity targets.

## Review and verification boundary

The project lead states that the official sources' identities and trustworthiness have been inspected. This is a source-level review acknowledgement, not blanket approval of the local dataset's physical interpretation. The atomic claim remains `evidence_state: unverified` until its exact locators and wording are approved through the established claim-level Evidence workflow. No local-data provenance or scientific validation status is promoted by this administrative registration.

## Supporting inspection report

The following sections preserve the existing broader provenance review and unresolved questions. They are context supporting the single atomic claim above, not separately verified `EV` claims.

# Scope and source boundary

This is a source-traceable inspection report, not verified Evidence and not a change to DATA-0001. The official repository was inspected read-only at commit `9c74e82218e377eaf6d02d113fc1ce6e36c92aa6` (2023-06-07). The local audit package is `data_preview/metalset_audit/`; its findings remain inspection artifacts.

## What the paper and repository establish

The LithoBench paper, *LithoBench: Benchmarking AI Computational Lithography for Semiconductor Manufacturing* (NeurIPS 2023), describes a lithography-simulation task in its dataset/benchmark sections: an optimized mask is mapped to an aerial image and a resist/printed image. The repository README makes the interface explicit: the lithography loader returns “optimized masks, aerial images, and resist images” (README, “Train and Test a New Model”), and a lithography model returns aerial and resist tensors (same section). The paper is the source for the benchmark framing; the executable mapping below is stronger evidence for this checkout’s implementation.

## Exact data-flow mapping

`lithobench/dataset.py` function `filesLithoSim(folder, binarized=True)` enumerates `folder/pixelILT/*.png`, `folder/litho/*.png`, and, when `binarized=True`, `folder/printed/*.png` (otherwise `folder/resist/*.png`). It intersects filename stems and sorts each list by stem. Thus a valid sample is `(pixelILT stem, litho stem, printed stem)` by exact basename; `resist` is selected only when `binarized=False`. `DataLitho.__getitem__` loads and returns `(mask, litho, resist)` in that order. `lithosim()` calls `filesLithoSim` with its default, so the normal loader target is `printed`, despite the variable being named `resist`.

`DataLitho._loadImage` reads PNG bytes with OpenCV, takes channel zero, converts to float32, divides by `255.0`, and resizes with `torch.nn.functional.interpolate`. Therefore the loader exposes encoded PNG sample values in `[0,1]`; it does not recover a separately calibrated optical unit.

The local audit reports 16,423 exact `pixelILT`/`litho` pairs, 49 `pixelILT`-only files, and a 16,422 intersection across `levelsetILT`, `pixelILT`, `litho`, `printed`, `resist`, and `target`. These counts agree with the audit package, but the official loader itself does not establish that the local directory came from the official downloadable archive or from the same generation revision.

## Simulator equations and channel meaning

In `pylitho/exact.py`, `_LithoSim.forward` computes a coherent field by FFT convolution (`_computeImageMask` → `_kernelMult`), then returns

`aerial = sum_k scale_k * abs(ifft2(kernel_k * fft2(dose * mask)))^2`.

`LithoSim.sim` returns `aerialNom`, `aerialMax`, `aerialMin` followed by

`printed = sigmoid(PrintSteepness * (aerial - TargetDensity))`.

`LithoSim.forward` returns only the three printed tensors. The official implementation therefore distinguishes an optical aerial-intensity tensor from a sigmoid resist/printed tensor. The code does not write PNGs and contains no statement that the distributed `litho` PNGs are those aerial tensors. The names alone cannot close that gap. The loader’s `/255` is an image encoding conversion, not proof that stored `litho` values are physically normalized intensity.

## Comparison and confidence

High confidence: filename-stem intersection behavior; loader tuple order; `printed` versus `resist` selection; `/255` conversion; simulator’s squared-magnitude aerial equation and sigmoid printed equation. Moderate confidence: the paper’s benchmark-level description of mask → aerial → resist. Low confidence/unestablished: local `litho` PNGs are aerial intensity, local `printed`/`resist` files are generated by this exact simulator/configuration, and the local archive is the same dataset version.

The local audit’s 0..149 `litho` byte range and ~150 observed values are compatible with an encoded continuous field, but are equally compatible with an arbitrary or postprocessed grayscale target. They do not identify the physical quantity, dose, kernel set, threshold, or units.

## Additional evidence required before freezing the contract

1. Obtain and hash the exact official `lithodata.tar.gz` (or an official release manifest), record archive hash, extraction hash, and commit/download date; compare exact stem lists and per-file PNG hashes with the local directory.
2. Locate the dataset-generation scripts/configuration or an official statement that names `litho` as aerial intensity and `printed`/`resist` as the corresponding resist outputs. If unavailable, contact the authors or treat the interpretation as unresolved.
3. Recover the generation parameters: kernel files and hashes, `KernelNum`, dose values, target density, print steepness, focus/defocus/cunjuncture mode, pixel pitch, crop/resampling rule, and PNG write/dtype rule.
4. Verify whether bytes were linearly quantized from aerial values, clipped, thresholded, gamma transformed, or otherwise postprocessed; compare decoded arrays against a regenerated simulator output for several exact stems.
5. Freeze coordinate conventions: array origin, x/y axis order, row/column meaning, FFT normalization and kernel centering, mask polarity, pixel pitch, and resizing interpolation.
6. Resolve the 49 unmatched files and six-category one-file discrepancy with a reproducible inclusion policy and regenerated split manifests; record dataset version and split leakage controls.

## FD-NIG suitability (provisional)

`litho` is provisionally usable as an aerial-spectrum supervision target only as an explicitly *unverified grayscale proxy*. The official simulator makes aerial intensity a continuous pre-threshold quantity, so the channel’s continuity is directionally compatible. It is not yet justified to call it calibrated aerial intensity, compare spectra in physical units, or impose simulator-derived numerical constraints. Before freezing FD-NIG supervision, verify the provenance, scale, units, and coordinate/FFT contracts above and test a byte-level regeneration on representative stems.

## Missing contracts

Numerical: value range and normalization before/after PNG encoding, quantization precision, clipping, interpolation, NaN/finite policy, and tolerances. Physical: wavelength/NA/source, dose and defocus meanings, kernel normalization, resist model and threshold, pixel pitch, and whether `litho` is nominal/max/min or another condition. Coordinate: tensor shape/channel order, origin and handedness, x/y versus row/column, FFT shift/normalization, kernel alignment, crop boundaries, and resize convention.

No files, DATA-0001 record, experiments, architectures, or source claims were modified or promoted by this inspection.
