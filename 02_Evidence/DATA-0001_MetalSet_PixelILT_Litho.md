---
id: DATA-0001
title: "MetalSet matched pixelILT/litho pairs (external candidate)"
data_type: image-pair
data_state: registered
lifecycle_status: draft
split_state: existing-but-not-project-frozen
review_status: unreviewed
source_ids: []
method_ids: [METHOD-0001]
experiment_ids: [EXP-0002]
owner: project-lead
created: 2026-09-21
last_updated: 2026-09-21
---

# Provenance and location

The user explicitly authorized read-only inspection of the external repository `D:\project\lithobench-main`. The candidate dataset is located at:

`D:\project\lithobench-main\work\lithodata.tar\lithodata\MetalSet`

The project does not copy this external data into `raw/`; the path remains an external dependency until provenance and reproducibility are reviewed.

# Observed inventory

The external audit reports 16,472 `pixelILT` PNG files, 16,423 `litho` PNG files, and 16,423 matched pairs. There are 49 `pixelILT`-only files, no reported `litho`-only files, no duplicate names, and no corrupt PNGs in that audit. All reported images are 2048×2048 grayscale. `pixelILT` is binary-valued (`0/255`); `litho` is continuous grayscale with approximately 150 observed values and a reported range of `0..149`.

Existing split manifests point to the external data and report:

| Split | Rows | Manifest SHA256 |
|---|---:|---|
| train | 13,138 | `0F8C783B888DA9B345A5FDDA8FB8B3D3C0C4FB18BD84DDF0E88F1C134C` |
| val | 1,642 | `4ED7267BC03E0B8DC4E99B2C758E9FB0AD245C374240570F8324E6417F1F1D0E` |
| test | 1,643 | `283632EDE63C61365AE11FF9C9BB0DA9778467B73541F5866A8531CBAB5BF8B1` |

These manifests are useful starting points but are not yet project-frozen. A fresh audit and a pattern-family leakage check are required before a formal run.

# Contract relevant to METHOD-0001

The external loader returns matched `input` and `label` tensors with one grayscale channel scaled to `[0,1]`. It does not provide timestep `t`, noisy state `x_t`, mask metadata separate from the input image, or optical-condition metadata `alpha`. For the first plumbing experiment, `input` is treated as `m`, `label` as `x_ref`, `x_t` is generated on the fly, and `alpha` is a documented constant. This supports a single implicit optical condition only.

# Permitted and prohibited claims

Permitted initial use: a controlled forward-surrogate feasibility test on matched pairs after unmatched files are filtered. The result may be used to evaluate data loading, renderer gradients, optimization, and comparison with a direct-image baseline.

Not permitted from this record alone: claims of high-fidelity optical calibration, advanced-node physical validity, optical-condition generalization, or validated use of the external kernel-like assets. The audit did not establish a complete simulator contract, physical parameter provenance, or condition labels.

# Known gaps

The 49 unmatched files require an explicit filtering policy. The split manifests need to be regenerated or verified against the current directory. Optical-condition coverage is absent. Pattern-family separation and provenance of the `litho` labels remain to be confirmed. These gaps keep the data record registered but unfrozen.
