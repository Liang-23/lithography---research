# Provenance findings (inspection artifact; not verified Evidence)

## Available documentation and code-derived facts

- The registered `DATA-0001` record and the prior dataset map document the external root and the filename-stem pairing used for the software-only `pixelILT -> litho` baseline.
- The paired loader reads PNGs as single-channel grayscale and scales values by `/255` for model tensors.
- The loader and split manifests establish a machine-learning input/label role, not a physical output-stage identity.
- The prior cloud migration report states that the external dataset, raw papers, and Windows-only source paths were intentionally not migrated.

## What was not established

The reviewed cloud records do not contain a complete MetalSet generator or simulator contract that identifies:

- whether `litho` is aerial intensity, resist, wafer/printed output, or another derived image;
- the governing optical equations or numerical solver;
- illumination, wavelength, NA, pupil, focus, dose, resist, process, or calibration parameters;
- image units, physical pixel pitch, scaling, clipping, or normalization provenance;
- whether `pixelILT` and `levelsetILT` are binary masks, level-set fields, or post-processed mask encodings beyond their file appearance;
- the exact data-generation script and version used for each category.

## Confidence boundary

The evidence supports a software-level paired-image feasibility review. It does not support the claim that `litho` is aerial-image ground truth. A physical interpretation remains unresolved until the original MetalSet documentation and generator/simulator code are reviewed locally and linked to the exact dataset version.

## Sharing/licensing check

The target repository is private, but no `LICENSE` file was found and no dataset license/confidentiality statement was found in the reviewed repository records. Image previews are therefore withheld from this branch.
