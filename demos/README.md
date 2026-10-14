# Mask → Fourier Spectrum: Company Demo (Online)

**Status:** deterministic, educational visualization prototype (not a registered `EXP` experiment, trained FD-GNN, optical calibration, or verified physics simulation). This folder is an **independent demo**; it does not change the canonical method `METHOD-0003`, Locked Core, Evidence or research decisions.

## Use it entirely online

### Option A: Google Colab (recommended)

1. Open the notebook directly: [Launch the notebook from this branch in Colab](https://colab.research.google.com/github/Liang-23/lithography---research/blob/demo/mask-to-spectrum-colab-20261014/demos/mask_to_fourier_colab.ipynb).
2. If Colab cannot load the private GitHub repository directly, open [the Notebook on GitHub](https://github.com/Liang-23/lithography---research/blob/demo/mask-to-spectrum-colab-20261014/demos/mask_to_fourier_colab.ipynb), download the `.ipynb` file and upload it to [Colab](https://colab.research.google.com/) via **File → Upload notebook**. GitHub-to-Colab may require authorization to access private repositories.
3. Choose `MASK_PATTERN="mixed"` or `lines` / `contacts`, then use **Runtime → Run all**.
4. Find PNG exports in `demo_outputs/` and the ZIP `mask_fft_company_demo.zip` in Colab's Files pane. To download the ZIP, uncomment the `files.download` line in the final cell or download it from Colab's Files pane.
5. Optionally set `USE_UPLOAD=True` to upload your own mask into that Colab runtime. **Do not upload confidential company mask data without authorization.**

### Option B: GitHub Codespaces / cloud terminal

In a GitHub Codespace on this branch, run:

```bash
python -m pip install numpy matplotlib pillow
python demos/mask_to_fourier.py
```

The script writes the same three PNG presentations and a ZIP into the working directory; no GPU is needed. The `.py` file was generated from the notebook code cells so a cloud terminal can run it without a notebook interface.

### Option C: GitHub Actions (manual, synthetic masks only)

After this branch is merged to `main`, open **Actions → Mask Fourier Demo Images → Run workflow**. It will generate images with the **synthetic default mask only** and save a downloadable Actions artifact `mask-fft-demo-images`. The workflow does not train a model, read private company files, or commit synthetic outputs back into the repository.

## What the three exported PNG images show

| Output | Intended company-slide use | Physics status |
| --- | --- | --- |
| `01_mask_to_fourier.png` | Six-panel Mask → exit field → Fourier magnitude/phase → illustrative pupil → image-side intensity | **Toy coherent imaging** under unit plane-wave illumination; NOT high-fidelity aerial-image truth |
| `02_frequency_pair.png` | Choose two actual FFT peaks, show Frequency Nodes, `A(k)conj(A(l))` and difference `q=k-l` | Exact Fourier-product arithmetic on demonstration mask; **no GNN message passing** |
| `03_three_mask_comparison.png` | Compare different Mask geometries with corresponding Fourier magnitude maps | Standard deterministic FFT of synthetic masks; **not a performance comparison** |

`provenance.txt` records data origin, simplifying assumptions, input size and FFT inverse round-trip error.

## Main mathematical chain

```text
Binary Mask M(x,y), 1=transmitting
        ×  uniform unit plane-wave field E_in(x,y)=1+0j
        ↓
Exit field E_mask(x,y) = M(x,y) E_in(x,y)
        ↓  numpy.fft.fft2 + fftshift
Complex mask spectrum A(kx,ky)
        ├── |A(k)|; log amplitude heatmap
        ├── angle A(k); phase heatmap
        └── [Re A(k), Im A(k), kx, ky] (future FD-GNN node feature)
        ↓  TOY comparison only: circular pupil H(k)
Image-side field = inverse FFT [H(k) A(k)]
        ↓
Toy coherent intensity = |Image-side field|²
```

The demo uses `np.fft.fftfreq` frequency coordinates in **cycles/pixel** because no physical pixel pitch is given. The toy circular pupil cutoff is **not** an optical NA or process condition. Actual partially coherent lithography needs additional source/pupil/system parameters and correct label provenance.

**Important distinction:** FFT amplitude/phase are **not** ground-truth aerial intensity. No real `litho` label is used or declared physically verified. A mask-independent TCC and mask-conditioned *effective* modes must not be conflated. The L0/G1/G2 mode generators remain research candidates; this demo implements only input preprocessing and physical-structure illustration.

## Limitations and review checklist

- Binary, scalar **transmission** Mask under uniform coherent illumination, not EUV multilayer reflection or mask 3D scattering.
- Images loaded from disk/upload are binarized. Oversized images are scaled with nearest-neighbor interpolation; neither operation is physically calibrated.
- `A=` complex **field** Fourier spectrum; `I=` intensity after pupil filtering. No second squaring after intensity is computed.
- Fourier phase is masked for coefficients whose magnitude is extremely small; do not interpret apparent phase color where amplitudes vanish.
- The Pair example uses discrete shifted-array row/column indices and reports raw differences for illustration; complete renderer needs an explicitly chosen wrapped-versus-padded output-frequency convention.
- FFT invertibility is checked for the input field. This proves only numerical consistency of the **FFT/inverse FFT** pair, not fidelity of optical simulation or learned predictions.
- Official numerical experiments still require a separate approved `EXP-####/Plan.md`. Demo generation is not an experiment and must not be promoted as performance Evidence.

## Related canonical record

- `05_Method_Design/METHOD-0003_Mask_Conditioned_Effective_Mode_FD_GNN.md`
- `08_Project_Status/FD_GNN_Global_Context_Candidates_2026-10-14.md`

No derived Wiki knowledge state is changed by this standalone demonstration utility.
