# Numerical statistics (inspection artifact; not verified Evidence)

## Dataset-level observations from the prior read-only audit

| Category | File count | Observed file type | Observed dimensions/channels | Observed numerical facts |
|---|---:|---|---|---|
| `pixelILT` | 16,472 | PNG | sampled files: 2048×2048, mode `L` | binary-valued grayscale, reported as 0/255 |
| `levelsetILT` | 16,472 | PNG | sampled dimensions were not re-established in this cloud session | numerical range not established in the available cloud record |
| `litho` | 16,423 | PNG | sampled files: 2048×2048, mode `L` | continuous grayscale; approximately 150 observed values; reported range 0..149 |
| `target` | 16,472 | PNG | not rechecked here | semantics documented as ideal pattern in the prior map; not the current label |
| `resist` | 16,422 | PNG | not rechecked here | later simulation output in the prior map; not the current label |
| `printed` | 16,422 | PNG | not rechecked here | final printed result in the prior map; not the current label |

## Pairing observations

- The audited current training join is filename-stem intersection of `pixelILT` and `litho`.
- Matched pair count reported by the prior audit: 16,423.
- Unmatched `pixelILT` count: 49.
- Existing split manifests report 13,138 train, 1,642 validation, and 1,643 test rows, totaling 16,423.
- `levelsetILT` has the same directory count as `pixelILT`, but a triplet match still requires a local recheck for every selected stem.
- No duplicate stems were reported in the existing pairing audit.

## Interpretation limits

These are file-level observations and prior audit outputs. They do not establish units, calibration, simulator stage, optical intensity, resist state, or physical meaning of any grayscale level. Preview display normalization must not be used as a numerical claim.
