"""Independent exhaustive reference for the FD-NIG synthetic contract.

The reference intentionally uses a Python loop so it does not share the
candidate aggregation reduction with :mod:`fd_nig_aggregation`.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple
import json
from pathlib import Path

import torch


Pair = Tuple[int, int, int, int]


def load_config(path: str | Path) -> dict:
    """Read declared experiment-local settings without authorizing execution."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


@dataclass(frozen=True)
class Fixture:
    mask: torch.Tensor
    spectrum: torch.Tensor
    pairs: torch.Tensor
    coefficients: torch.Tensor
    hermitian_coefficients: torch.Tensor
    target: torch.Tensor


def enumerate_pairs(height: int, width: int) -> torch.Tensor:
    """Return lexicographically ordered ``(kr, kc, lr, lc)`` pairs."""
    return torch.tensor(
        [(kr, kc, lr, lc) for kr in range(height) for kc in range(width)
         for lr in range(height) for lc in range(width)],
        dtype=torch.long,
    )


def route_pairs(pairs: torch.Tensor, height: int, width: int) -> torch.Tensor:
    """Route pairs to flattened modular difference bins."""
    q_row = (pairs[:, 0] - pairs[:, 2]) % height
    q_col = (pairs[:, 1] - pairs[:, 3]) % width
    return q_row * width + q_col


def pair_products(coefficients: torch.Tensor, spectrum: torch.Tensor,
                  pairs: torch.Tensor) -> torch.Tensor:
    """Compute complex pair contributions in an explicit scalar formula."""
    values = []
    for index, (kr, kc, lr, lc) in enumerate(pairs.tolist()):
        c, a, b = coefficients[index], spectrum[kr, kc], spectrum[lr, lc]
        # Deliberately expand the complex product; this is independent of the
        # candidate's vectorized conjugate/multiply expression.
        cr, ci, ar, ai, br, bi = c.real, c.imag, a.real, a.imag, b.real, b.imag
        br, bi = br, -bi
        real = (cr * ar - ci * ai) * br - (cr * ai + ci * ar) * bi
        imag = (cr * ar - ci * ai) * bi + (cr * ai + ci * ar) * br
        values.append(torch.complex(real, imag))
    return torch.stack(values) if values else spectrum.new_empty((0,))


def exhaustive_aggregate(coefficients: torch.Tensor, spectrum: torch.Tensor,
                         pairs: torch.Tensor) -> torch.Tensor:
    """Reference loop aggregation into a flattened ``H*W`` spectrum."""
    height, width = spectrum.shape[-2:]
    output = spectrum.new_zeros((height * width,))
    for index, (kr, kc, lr, lc) in enumerate(pairs.tolist()):
        q = ((kr - lr) % height) * width + ((kc - lc) % width)
        output[q] = output[q] + coefficients[index] * spectrum[kr, kc] * spectrum[lr, lc].conj()
    return output.reshape(height, width)


def make_mask(seed: int = 20261011, height: int = 16, width: int = 16,
              binary: bool = False) -> torch.Tensor:
    """Create the deterministic synthetic mask specified by EXP-0003."""
    generator = torch.Generator().manual_seed(seed)
    mask = torch.zeros((height, width), dtype=torch.float64)
    mask[2:7, 1:6] = 1
    mask[9:14, 10:15] = 0.65
    y = torch.arange(height, dtype=torch.float64).view(-1, 1)
    x = torch.arange(width, dtype=torch.float64).view(1, -1)
    mask = mask + 0.15 * torch.sin(2 * torch.pi * (x + 2 * y) / width)
    if not binary:
        mask = mask + 0.02 * torch.rand((height, width), generator=generator, dtype=torch.float64)
    return (mask > 0.5).to(torch.float64) if binary else mask


def make_coefficients(pairs: torch.Tensor, seed: int = 20261011,
                      dtype: torch.dtype = torch.complex128) -> torch.Tensor:
    generator = torch.Generator().manual_seed(seed + 1)
    real = torch.randn((len(pairs),), generator=generator, dtype=torch.float64)
    imag = torch.randn((len(pairs),), generator=generator, dtype=torch.float64)
    return torch.complex(real, imag).to(dtype)


def make_hermitian_coefficients(pairs: torch.Tensor, height: int, width: int,
                                seed: int = 20261011) -> torch.Tensor:
    """Build coefficients satisfying ``C(l,k)=conj(C(k,l))``."""
    generator = torch.Generator().manual_seed(seed + 2)
    values = torch.zeros(len(pairs), dtype=torch.complex128)
    index = {tuple(pair): i for i, pair in enumerate(pairs.tolist())}
    for pair, i in index.items():
        swapped = (pair[2], pair[3], pair[0], pair[1])
        if i > index[swapped]:
            continue
        if pair == swapped:
            values[i] = torch.randn((), generator=generator, dtype=torch.float64)
        else:
            z = torch.complex(torch.randn((), generator=generator, dtype=torch.float64),
                              torch.randn((), generator=generator, dtype=torch.float64))
            values[i] = z
            values[index[swapped]] = z.conj()
    return values


def make_fixture(seed: int = 20261011, height: int = 16, width: int = 16) -> Fixture:
    mask = make_mask(seed, height, width)
    spectrum = torch.fft.fft2(mask, norm="backward")
    pairs = enumerate_pairs(height, width)
    return Fixture(mask, spectrum, pairs, make_coefficients(pairs, seed),
                   make_hermitian_coefficients(pairs, height, width, seed),
                   mask.clone())


def zero_safe_error(candidate: torch.Tensor, reference: torch.Tensor,
                    scale: torch.Tensor, atol: float, rtol: float) -> torch.Tensor:
    """Per-bin error bound that remains defined for zero reference bins."""
    return (candidate - reference).abs() - (atol + rtol * scale)
