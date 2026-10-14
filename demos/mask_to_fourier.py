#!/usr/bin/env python3
# Company-facing educational visualization. Generated from mask_to_fourier_colab.ipynb.
# Non-experimental: synthetic or explicitly selected input Mask; no model training.
# Run: python demos/mask_to_fourier.py
# Requires: numpy, matplotlib, Pillow
import matplotlib
matplotlib.use("Agg")

# --- Notebook code cell 1 ---
import io
from pathlib import Path
import zipfile

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Choose among "mixed", "lines", "contacts".
MASK_PATTERN = "mixed"
USE_UPLOAD = False       # True only when you choose to upload a mask image
LOCAL_MASK_PATH = ""     # Optional on a notebook runtime with an existing file
TRANSPARENT_IS_WHITE = True
RESIZE_LONGEST_SIDE_TO = 256
TOY_PUPIL_CUTOFF = 0.10  # cycles/pixel: illustrative, NOT calibrated

OUTPUT_DIR = Path("demo_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)
print("Output folder:", OUTPUT_DIR.resolve())

# --- Notebook code cell 2 ---
def synthetic_mask(n=256, pattern="mixed"):
    y, x = np.indices((n, n))
    if pattern == "lines":
        return ((x // 16) % 2 == 0).astype(np.float32)
    if pattern == "contacts":
        return (((x % 32 - 16)**2 + (y % 32 - 16)**2) <= 7**2).astype(np.float32)
    if pattern == "mixed":
        out = np.zeros((n, n), np.float32)
        x_left = x[30:n-30, 25:n//2]
        out[30:n-30, 25:n//2] = ((x_left // 16) % 2 == 0)
        discs = ((x % 42 - 21)**2 + (y % 42 - 21)**2 <= 9**2)
        out[24:n-24, n//2+12:n-24] = discs[24:n-24, n//2+12:n-24]
        return out
    raise ValueError("MASK_PATTERN must be one of: mixed, lines, contacts")


def load_mask_image(file_bytes, invert=False):
    image = Image.open(io.BytesIO(file_bytes)).convert("L")
    if max(image.size) > RESIZE_LONGEST_SIDE_TO:
        image.thumbnail(
            (RESIZE_LONGEST_SIDE_TO, RESIZE_LONGEST_SIDE_TO),
            Image.Resampling.NEAREST
        )
        print("Note: Large input resized for display; frequency sampling changed.")
    arr = np.asarray(image, dtype=np.float32) / 255.0
    arr = (arr >= 0.5).astype(np.float32)
    return (1.0-arr) if invert else arr


if USE_UPLOAD:
    from google.colab import files
    uploaded = files.upload()  # Upload to ephemeral Colab runtime only
    if not uploaded:
        raise ValueError("No mask uploaded.")
    filename, file_bytes = next(iter(uploaded.items()))
    mask = load_mask_image(file_bytes, invert=not TRANSPARENT_IS_WHITE)
    print("Uploaded:", filename, "shape:", mask.shape)
elif LOCAL_MASK_PATH:
    mask = load_mask_image(Path(LOCAL_MASK_PATH).read_bytes(),
                           invert=not TRANSPARENT_IS_WHITE)
else:
    mask = synthetic_mask(256, MASK_PATTERN)
    print("Synthetic example:", MASK_PATTERN)

assert mask.ndim == 2 and mask.size > 0
print("Mask shape (H,W):", mask.shape,
      "| transmission fraction:", float(mask.mean()))

# --- Notebook code cell 3 ---
E_in = np.ones(mask.shape, dtype=np.complex128)  # uniform, coherent, phase = 0
E_mask = mask.astype(np.complex128) * E_in

A = np.fft.fftshift(np.fft.fft2(E_mask))
magnitude = np.abs(A)
phase = np.angle(A)
phase_visible = np.ma.masked_where(
    magnitude < 1e-4 * magnitude.max(), phase
)

height, width = mask.shape
fy = np.fft.fftshift(np.fft.fftfreq(height))
fx = np.fft.fftshift(np.fft.fftfreq(width))
KX, KY = np.meshgrid(fx, fy, indexing="xy")

pupil = ((KX**2 + KY**2) <= TOY_PUPIL_CUTOFF**2).astype(np.float64)
E_image = np.fft.ifft2(np.fft.ifftshift(A * pupil))
toy_aerial_intensity = np.abs(E_image)**2

reconstructed = np.fft.ifft2(np.fft.ifftshift(A))
relative_fft_error = (
    np.linalg.norm(reconstructed - E_mask) / max(np.linalg.norm(E_mask), 1e-30)
)
print(f"FFT → inverse FFT field relative error: {relative_fft_error:.3e}")
print("Spectrum:", A.shape, A.dtype,
      "| toy intensity range:", float(toy_aerial_intensity.min()),
      float(toy_aerial_intensity.max()))
assert relative_fft_error < 1e-12, "Unexpected FFT round-trip discrepancy"

# --- Notebook code cell 4 ---
fig, axes = plt.subplots(2, 3, figsize=(15, 9), constrained_layout=True)
panels = [
    (mask, "1  Binary mask M(x,y)", "gray", None),
    (np.abs(E_mask), "2  Exit-field amplitude |E|", "gray", None),
    (np.log1p(magnitude), "3  FFT log(1+|A|)", "inferno", None),
    (phase_visible, "4  FFT phase (significant modes)", "twilight", (-np.pi, np.pi)),
    (pupil, "5  Illustrative pupil H(k)", "gray", None),
    (toy_aerial_intensity, "6  Toy coherent image |E_img|²", "viridis", None)
]
for ax, (data, title, cmap, limits) in zip(axes.flat, panels):
    settings = {"cmap": cmap, "interpolation": "nearest"}
    if limits is not None:
        settings.update(vmin=limits[0], vmax=limits[1])
    ax.imshow(data, **settings)
    ax.set_title(title, fontsize=12)
    ax.axis("off")
fig.suptitle(
    "Mask → Complex Field → Fourier Spectrum → Illustrative Coherent Imaging",
    fontsize=16
)
poster1 = OUTPUT_DIR / "01_mask_to_fourier.png"
fig.savefig(poster1, dpi=140, bbox_inches="tight")
plt.show()
plt.close(fig)
print("Saved:", poster1)

# --- Notebook code cell 5 ---
strongest = np.argsort(magnitude.ravel())[::-1]
picked = []
center = (height//2, width//2)
for flat in strongest:
    rc = tuple(map(int, np.unravel_index(flat, magnitude.shape)))
    if rc == center or magnitude[rc] <= 1e-8*magnitude.max():
        continue
    if all((rc[0]-a)**2 + (rc[1]-b)**2 > 8**2 for a, b in picked):
        picked.append(rc)
    if len(picked) == 2:
        break

if len(picked) != 2:
    raise ValueError("Need two separated non-DC frequencies; try mixed or contacts mask.")

k, l = picked
q_row_col = (k[0]-l[0], k[1]-l[1])
pair_product = A[k] * np.conj(A[l])
feature_k = [A[k].real, A[k].imag, fx[k[1]], fy[k[0]]]
feature_l = [A[l].real, A[l].imag, fx[l[1]], fy[l[0]]]
print("Frequency node h^0(k) = [Re A, Im A, kx, ky]:", feature_k)
print("Frequency node h^0(l) = [Re A, Im A, kx, ky]:", feature_l)
print("Pair product A(k) conj(A(l)):", pair_product)
print("Difference q = (delta row, delta col):", q_row_col)

fig, axes = plt.subplots(1, 2, figsize=(13, 5), constrained_layout=True)
axes[0].imshow(np.log1p(magnitude), cmap="inferno")
axes[0].scatter([k[1], l[1]], [k[0], l[0]], s=115,
                facecolors="none", edgecolors=["cyan", "lime"], linewidths=2.4)
axes[0].annotate("k", (k[1]+5,k[0]+4), color="cyan", fontsize=17)
axes[0].annotate("l", (l[1]+5,l[0]+4), color="lime", fontsize=17)
axes[0].set_title("Two Frequency Nodes in FFT");axes[0].axis("off")
axes[1].axis("off")
axes[1].text(.03,.84,"F_k + F_l → Pair P_(k,l)",fontsize=16,transform=axes[1].transAxes)
axes[1].text(.03,.66,f"k (row,col) = {k}; l = {l}",fontsize=12,transform=axes[1].transAxes)
axes[1].text(.03,.48,f"Difference node: q = {q_row_col}",fontsize=13,transform=axes[1].transAxes)
axes[1].text(.03,.30,"Known p(k,l) = A(k) conj(A(l))",fontsize=13,transform=axes[1].transAxes)
axes[1].text(.03,.13,f"Re(p) = {pair_product.real:.2e}; Im(p) = {pair_product.imag:.2e}",
             fontsize=11,transform=axes[1].transAxes)
poster2 = OUTPUT_DIR / "02_frequency_pair.png"
fig.savefig(poster2, dpi=140, bbox_inches="tight")
plt.show()
plt.close(fig)
print("Saved:", poster2)

# --- Notebook code cell 6 ---
patterns = ["lines", "contacts", "mixed"]
fig, axes = plt.subplots(3, 2, figsize=(9.5, 12), constrained_layout=True)
for i, name in enumerate(patterns):
    m = synthetic_mask(256, name)
    spec = np.fft.fftshift(np.fft.fft2(m.astype(np.complex128)))
    axes[i,0].imshow(m, cmap="gray", interpolation="nearest")
    axes[i,0].set_title(name.title()+" | Binary mask")
    axes[i,1].imshow(np.log1p(np.abs(spec)), cmap="inferno", interpolation="nearest")
    axes[i,1].set_title(name.title()+" | Fourier log magnitude")
    axes[i,0].axis("off")
    axes[i,1].axis("off")
fig.suptitle("Different Mask Geometries, Different Spectral Signatures", fontsize=16)
poster3 = OUTPUT_DIR / "03_three_mask_comparison.png"
fig.savefig(poster3, dpi=140, bbox_inches="tight")
plt.show()
plt.close(fig)
print("Saved:", poster3)

# --- Notebook code cell 7 ---
readme = (
    "Mask-to-Fourier visualization; synthetic/optional user mask.\n"
    "Assumptions: unit coherent plane wave, binary amplitude transmission, "
    "uncalibrated circular pupil.\n"
    f"Input shape={mask.shape}; FFT relative roundtrip error={relative_fft_error:.3e}.\n"
    "Panel 6 is toy coherent intensity, not a measured or validated Aerial Image.\n"
    "FD-GNN model not run; no scientific experiment or score.\n"
)
(OUTPUT_DIR / "provenance.txt").write_text(readme, encoding="utf-8")
zip_path = Path("mask_fft_company_demo.zip")
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for file in sorted(OUTPUT_DIR.iterdir()):
        if file.is_file():
            z.write(file, arcname=file.name)
print("Prepared:", zip_path, "| files:", [p.name for p in sorted(OUTPUT_DIR.iterdir())])
# Optional download when in Colab, with an explicit uncommented user gesture:
# from google.colab import files
# files.download(str(zip_path))
