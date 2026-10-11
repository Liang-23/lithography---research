"""Candidate vectorized FD-NIG complex aggregation operations."""
from __future__ import annotations

import torch


def route_pairs(pairs: torch.Tensor, height: int, width: int) -> torch.Tensor:
    q = torch.stack(((pairs[:, 0] - pairs[:, 2]) % height,
                     (pairs[:, 1] - pairs[:, 3]) % width), dim=1)
    return q[:, 0] * width + q[:, 1]


def pair_products(coefficients: torch.Tensor, spectrum: torch.Tensor,
                  pairs: torch.Tensor) -> torch.Tensor:
    left = spectrum[pairs[:, 0], pairs[:, 1]]
    right = spectrum[pairs[:, 2], pairs[:, 3]].conj()
    return coefficients * left * right


def scatter_add_complex(contributions: torch.Tensor, bins: torch.Tensor,
                        number_of_bins: int) -> torch.Tensor:
    """Deterministic indexed complex accumulation (duplicates are supported)."""
    output = contributions.new_zeros((number_of_bins,))
    return output.scatter_add(0, bins, contributions)


def aggregate(coefficients: torch.Tensor, spectrum: torch.Tensor,
              pairs: torch.Tensor) -> torch.Tensor:
    height, width = spectrum.shape[-2:]
    bins = route_pairs(pairs, height, width)
    values = pair_products(coefficients, spectrum, pairs)
    return scatter_add_complex(values, bins, height * width).reshape(height, width)


def enforce_hermitian(spectrum: torch.Tensor) -> torch.Tensor:
    """Project a 2-D spectrum onto Hermitian symmetry without squaring output."""
    rows = torch.arange(spectrum.shape[-2], device=spectrum.device)
    cols = torch.arange(spectrum.shape[-1], device=spectrum.device)
    flipped = spectrum.conj().index_select(-2, (-rows) % spectrum.shape[-2])
    flipped = flipped.index_select(-1, (-cols) % spectrum.shape[-1])
    return 0.5 * (spectrum + flipped)


def hermitian_residual(spectrum: torch.Tensor) -> torch.Tensor:
    """Return the maximum conjugate-symmetry residual over ``q`` and ``-q``."""
    rows = torch.arange(spectrum.shape[-2], device=spectrum.device)
    cols = torch.arange(spectrum.shape[-1], device=spectrum.device)
    negative = spectrum.conj().index_select(-2, (-rows) % spectrum.shape[-2])
    negative = negative.index_select(-1, (-cols) % spectrum.shape[-1])
    return (spectrum - negative).abs().amax()


def inverse_real(spectrum: torch.Tensor, enforce_symmetry: bool = False,
                 check: bool = True, tolerance: float | None = None) -> torch.Tensor:
    assembled = enforce_hermitian(spectrum) if enforce_symmetry else spectrum
    if check and tolerance is not None and hermitian_residual(assembled) > tolerance:
        raise ValueError("spectrum violates Hermitian symmetry")
    spatial = torch.fft.ifft2(assembled)
    residual = spatial.imag.abs().amax()
    if check and tolerance is not None and residual > tolerance:
        raise ValueError("inverse FFT has non-negligible imaginary residual")
    return spatial.real


def absolute_scales(contributions: torch.Tensor, bins: torch.Tensor,
                    number_of_bins: int) -> torch.Tensor:
    """Independent cancellation-resistant scale for zero-safe comparisons."""
    scale = contributions.abs().new_zeros((number_of_bins,))
    return scale.scatter_add(0, bins, contributions.abs())
