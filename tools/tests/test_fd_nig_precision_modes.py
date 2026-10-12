"""Exploratory A/C precision-mode regression tests, NOT formal EXP-0003 gates.

The frozen test_fd_nig_synthetic.py and its native complex64 acceptance checks
remain unchanged. No Plan/execution approval is inferred from these tests.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import torch

from tools.fd_nig_aggregation import (
    aggregate, hermitian_residual, pair_products, route_pairs, scatter_add_complex,
)
from tools.fd_nig_reference import exhaustive_aggregate, load_config, make_fixture


CONFIG = load_config(Path(__file__).resolve().parents[1] / "fd_nig_config.json")


def hermitian_fixture(size: int = 16):
    fixture = make_fixture(seed=CONFIG["seed"], height=size, width=size)
    spectrum = fixture.spectrum.to(torch.complex64)
    coefficients = fixture.hermitian_coefficients.to(torch.complex64)
    return fixture, spectrum, coefficients


def test_strategy_a_native_complex64_is_still_the_default(record_property):
    fixture, spectrum, coefficients = hermitian_fixture()
    native = aggregate(coefficients, spectrum, fixture.pairs)
    explicit_native = aggregate(coefficients, spectrum, fixture.pairs,
                                precision_mode="native")
    height, width = spectrum.shape
    original_terms = pair_products(coefficients, spectrum, fixture.pairs)
    original_bins = route_pairs(fixture.pairs, height, width)
    manually_native = scatter_add_complex(
        original_terms, original_bins, height * width,
    ).reshape(height, width)
    assert native.dtype == torch.complex64
    assert torch.equal(native, explicit_native)
    assert torch.equal(native, manually_native)
    record_property("strategy_a_raw_hermitian_residual",
                    float(hermitian_residual(native)))
    record_property("strategy_a_ifft_imaginary_residual",
                    float(torch.fft.ifft2(native, norm="backward").imag.abs().max()))
    # Strategy A remains subject to the frozen native complex64 checks elsewhere.


def test_strategy_c_promotes_products_and_accumulation(record_property):
    fixture, spectrum, coefficients = hermitian_fixture()
    mixed = aggregate(coefficients, spectrum, fixture.pairs,
                      precision_mode="mixed-complex128")
    again = aggregate(coefficients, spectrum, fixture.pairs,
                      precision_mode="mixed-complex128")
    assert mixed.dtype == torch.complex64
    assert torch.equal(mixed, again)

    # Independent loop oracle operates on the same quantized complex64 inputs
    # converted to complex128 BEFORE multiplication, then casts at the output.
    reference = exhaustive_aggregate(
        coefficients.to(torch.complex128), spectrum.to(torch.complex128), fixture.pairs,
    ).to(torch.complex64)
    atol = CONFIG["tolerances"]["float32"]["atol"]
    rtol = CONFIG["tolerances"]["float32"]["rtol"]
    assert torch.allclose(mixed, reference, atol=atol, rtol=rtol)

    residual = float(hermitian_residual(mixed))
    inverse_residual = float(torch.fft.ifft2(mixed, norm="backward").imag.abs().max())
    record_property("strategy_c_raw_hermitian_residual", residual)
    record_property("strategy_c_ifft_imaginary_residual", inverse_residual)
    assert residual <= CONFIG["tolerances"]["hermitian"]["float32"]
    assert inverse_residual <= CONFIG["tolerances"]["inverse_imag"]["float32"]
    for row, col in ((0, 0), (0, 8), (8, 0), (8, 8)):
        assert float(mixed[row, col].imag.abs()) <= (
            CONFIG["tolerances"]["self_conjugate_imag"]["float32"])


def test_optional_mode_rejects_unknown_mode_and_non_complex64():
    fixture, spectrum, coefficients = hermitian_fixture(size=4)
    with pytest.raises(ValueError, match="precision_mode"):
        aggregate(coefficients, spectrum, fixture.pairs, precision_mode="unknown")
    with pytest.raises(TypeError, match="requires complex64"):
        aggregate(coefficients.to(torch.complex128), spectrum.to(torch.complex128),
                  fixture.pairs, precision_mode="mixed-complex128")
    with pytest.raises(TypeError, match="requires complex64"):
        aggregate(coefficients.to(torch.complex128), spectrum, fixture.pairs,
                  precision_mode="mixed-complex128")


def test_strategy_c_keeps_real_and_imag_gradient_paths_finite():
    fixture, spectrum, coefficients = hermitian_fixture(size=4)
    params = coefficients.detach().clone().requires_grad_(True)
    output = aggregate(params, spectrum, fixture.pairs,
                       precision_mode="mixed-complex128")
    image = torch.fft.ifft2(output, norm="backward").real
    target = fixture.target.to(image.dtype)
    loss = (image - target).square().mean()
    (gradient,) = torch.autograd.grad(loss, params)
    assert gradient.dtype == torch.complex64
    assert torch.isfinite(gradient.real).all()
    assert torch.isfinite(gradient.imag).all()
    assert gradient.real.abs().max() > 0
    assert gradient.imag.abs().max() > 0
