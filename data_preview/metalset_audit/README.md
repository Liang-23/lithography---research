# MetalSet audit package

**Inspection artifact, not verified Evidence.** This directory is a bounded, non-canonical review package prepared from the user-authorized local source tree. It does not modify `DATA-0001`, Locked Core, hypotheses, methods, experiment plans, or decisions.

## Source and selection

- Source root: `D:\project\lithobench-main\work\lithodata.tar\lithodata\MetalSet` (an extracted directory named `lithodata.tar`; it is not an archive file at this path).
- Categories inspected: `levelsetILT`, `pixelILT`, `litho`, `printed`, `resist`, `target`, plus non-image `gds` and `glp`.
- Pairing key: exact filename stem, case-sensitive, using direct `.png` files only.
- Counts: 16,472 `levelsetILT`, 16,472 `pixelILT`, 16,423 `litho`, 16,422 `printed`, 16,422 `resist`, 16,472 `target`; 16,423 `pixelILT`–`litho` matches; 16,422 matches across all six image categories.
- Deterministic sample rule: sort the six-way intersection by numeric `cellN` order and select indices 0, 20%, 40%, 60%, 80%, and the final index. Selected IDs: cell0, cell3292, cell6586, cell9905, cell13308, cell16753.

## Files

- `sample_manifest.csv`: one row per selected image/category, with original and preview paths, dimensions, dtype, min/max/mean/std, unique-value count, and exact preview transformation.
- `category_summary.csv`: category counts and range scope. `pixelILT` and `litho` full-range statements cross-check the existing authorized source audit; other category ranges are explicitly sample-only.
- `provenance_findings.md`: source-tree findings and unresolved physical meaning.
- `previews/`: 36 local PNG previews at 512×512. They are excluded from version control because the source dataset license/share permission is unresolved.

## Preview transformation

Each source image was opened as grayscale `L`, resized from 2048×2048 to 512×512 with nearest-neighbor interpolation, and saved as a lossless PNG. No contrast stretch, min-max normalization, percentile normalization, thresholding, channel conversion beyond `L`, or value remapping was applied. The preview is therefore a display artifact; the original statistics in `sample_manifest.csv` remain the authoritative observations for this inspection.

## Sharing status

The repository has no dataset license or sharing statement, and `work/README.md` only says to place data there. The source tree does not establish permission to redistribute image bytes. Therefore the preview images are retained locally and are not committed or pushed. Textual audit metadata contains paths and derived statistics only.
