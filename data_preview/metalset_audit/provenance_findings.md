# Provenance findings

**Inspection artifact, not verified Evidence.**

## Relevant files read

- `D:\project\lithobench-main\work\README.md`: placeholder saying the data should be placed under `work`; no dataset provenance or license.
- `D:\project\lithobench-main\reports\MetalSet_Dataset_Audit.md`: prior read-only audit of `pixelILT`/`litho` pairing and image properties.
- `D:\project\lithobench-main\scripts\audit_metalset_pairs.py`: pairs direct PNGs by filename stem and reports binary `pixelILT` / continuous `litho`; it does not document how the images were generated.
- `D:\project\lithobench-main\scripts\create_metalset_splits.py` and `lithobench\metalset_pairs.py`: deterministic split/pair handling and grayscale PNG loading; `load_grayscale_tensor` divides uint8 values by 255 for tensors.
- `D:\project\lithobench-main\config\lithosimple.txt`: contains generic kernel/printing parameters (`KernelNum`, `PrintThresh`, `Dose*`), but no traceable link to the MetalSet files or generation run.
- `D:\project\lithobench-main\AGENTS.md`: confirms the MetalSet source directories are read-only and states the supervised convention `pixelILT` input / `litho` target; this is repository workflow guidance, not scientific provenance.

## What is observed

All six image categories are direct PNG files with `cellN` stems. The exact-stem intersection is 16,423 for `levelsetILT`/`pixelILT`/`litho` and 16,422 across all six categories. The 49 `pixelILT`-only stems have no `litho` counterpart; no `litho`-only stems were found.

The existing source audit reports all `pixelILT` and `litho` images as 2048×2048 single-channel `uint8` PNGs, with `pixelILT` values exactly `(0, 255)` and `litho` global range `0..149` with 150 observed values and ~45.98% intermediate-valued pixels. The additional category observations in this package are sample-scoped unless stated otherwise.

## Physical meaning status

No relevant README, generation script, simulator configuration, mask/target definition, optical/process parameter record, aerial-image reference, or resist-simulation contract was found in the authorized `D:\project\lithobench-main` source tree that establishes what `litho` physically represents. The names `litho`, `printed`, `resist`, `target`, `levelsetILT`, and `pixelILT` are labels and file categories, not verified physical interpretations. Do not treat `levelsetILT` or `pixelILT` as aerial intensity. Do not treat `litho` as aerial-image ground truth.

## Licensing and confidentiality

No license or redistribution permission was found in the repository root, `work/README.md`, or the relevant source files. Sharing permission is therefore unresolved. Image previews are retained locally and excluded from the branch; only textual derived audit metadata is eligible for review/push.
