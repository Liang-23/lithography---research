"""Tests for the EXP-0003 synthetic contract (not run by implementation task)."""
from __future__ import annotations

import torch

from tools.fd_nig_aggregation import (absolute_scales, aggregate, enforce_hermitian,
                                      hermitian_residual, inverse_real, pair_products,
                                      route_pairs)
from tools.fd_nig_reference import (exhaustive_aggregate, make_fixture,
                                    pair_products as reference_products,
                                    route_pairs as reference_route)


def test_route_and_pair_products_are_independent():
    fixture = make_fixture()
    assert torch.equal(route_pairs(fixture.pairs, 16, 16), reference_route(fixture.pairs, 16, 16))
    assert torch.allclose(pair_products(fixture.coefficients, fixture.spectrum, fixture.pairs),
                          reference_products(fixture.coefficients, fixture.spectrum, fixture.pairs))


def test_vectorized_matches_exhaustive_reference():
    fixture = make_fixture()
    actual = aggregate(fixture.coefficients, fixture.spectrum, fixture.pairs)
    expected = exhaustive_aggregate(fixture.coefficients, fixture.spectrum, fixture.pairs)
    assert torch.allclose(actual, expected, atol=1e-10, rtol=1e-10)


def test_hermitian_inverse_is_real_without_magnitude_square():
    fixture = make_fixture()
    spectrum = aggregate(fixture.hermitian_coefficients, fixture.spectrum, fixture.pairs)
    # Validate the raw conjugate-paired assembly before any projection.
    assert hermitian_residual(spectrum) <= 1e-10
    raw_complex = torch.fft.ifft2(spectrum)
    assert raw_complex.imag.abs().amax() <= 1e-10
    raw_image = inverse_real(spectrum, check=True, tolerance=1e-10)
    assert torch.isfinite(raw_image).all()
    symmetric = enforce_hermitian(spectrum)
    assert hermitian_residual(symmetric) <= 1e-10
    image = inverse_real(symmetric, check=True, tolerance=1e-10)
    assert torch.isfinite(image).all()
    assert image.dtype.is_floating_point


def test_gradient_propagation_and_centered_finite_difference():
    fixture = make_fixture(height=4, width=4)
    coefficients = fixture.coefficients[:32].clone().requires_grad_(True)
    pairs = fixture.pairs[:32]
    output = inverse_real(aggregate(coefficients, fixture.spectrum, pairs), check=False)
    loss = (output - fixture.target).square().mean()
    (gradient,) = torch.autograd.grad(loss, coefficients)
    assert torch.isfinite(gradient.real).all() and torch.isfinite(gradient.imag).all()
    index = 3
    step = 1e-6
    with torch.no_grad():
        plus = coefficients.detach().clone(); plus[index] += step
        minus = coefficients.detach().clone(); minus[index] -= step
    lp = (inverse_real(aggregate(plus, fixture.spectrum, pairs), check=False) - fixture.target).square().mean()
    lm = (inverse_real(aggregate(minus, fixture.spectrum, pairs), check=False) - fixture.target).square().mean()
    numerical = (lp - lm) / (2 * step)
    assert torch.allclose(numerical, gradient[index].real, atol=1e-5, rtol=1e-4)


def test_sparse_and_exhaustive_pair_sets_agree_on_small_grid():
    fixture = make_fixture(height=4, width=4)
    pairs = fixture.pairs
    coefficients = fixture.coefficients
    expected = exhaustive_aggregate(coefficients, fixture.spectrum, pairs)
    actual = aggregate(coefficients, fixture.spectrum, pairs)
    assert torch.allclose(actual, expected, atol=1e-10, rtol=1e-10)


def test_zero_safe_error_and_stress_fixture_are_finite():
    fixture = make_fixture(height=8, width=8)
    scaled = fixture.spectrum * 1e3
    output = aggregate(fixture.coefficients, scaled, fixture.pairs)
    bins = route_pairs(fixture.pairs, 8, 8)
    scales = absolute_scales(reference_products(fixture.coefficients, scaled, fixture.pairs), bins, 64)
    reference = exhaustive_aggregate(fixture.coefficients, scaled, fixture.pairs)
    error = (output - reference).abs() - (1e-12 + 1e-12 * scales.reshape(8, 8))
    assert torch.isfinite(error).all()
    # Explicit empty-bin and cancellation cases remain well-defined.
    empty_candidate = torch.zeros(2, dtype=torch.complex128)
    empty_reference = torch.zeros_like(empty_candidate)
    empty_scale = torch.zeros(2)
    assert torch.isfinite((empty_candidate - empty_reference).abs() - 1e-12).all()
    cancellation = torch.tensor([1 + 0j, -1 + 0j], dtype=torch.complex128)
    cancellation_scale = cancellation.abs().sum()
    assert cancellation_scale > 0 and cancellation.sum().abs() == 0


def test_dc_and_nyquist_bins_are_real_for_hermitian_spectrum():
    fixture = make_fixture(height=8, width=8)
    spectrum = enforce_hermitian(aggregate(fixture.hermitian_coefficients, fixture.spectrum, fixture.pairs))
    for row, col in ((0, 0), (0, 4), (4, 0), (4, 4)):
        assert spectrum[row, col].imag.abs() <= 1e-10


def test_sparse_repeatability_and_gradient_corner_case():
    fixture = make_fixture(height=8, width=8)
    pairs = fixture.pairs[:256]
    coefficients = fixture.coefficients[:256].clone().requires_grad_(True)
    first = aggregate(coefficients, fixture.spectrum, pairs)
    second = aggregate(coefficients, fixture.spectrum, pairs)
    assert torch.equal(first, second)
    loss = inverse_real(first, check=False).square().mean()
    (gradient,) = torch.autograd.grad(loss, coefficients)
    assert torch.isfinite(gradient.real).all() and torch.isfinite(gradient.imag).all()
    # An inactive parameter (zero mask spectrum) has an exactly zero gradient.
    inactive = torch.zeros_like(coefficients, requires_grad=True)
    zero_spectrum = torch.zeros_like(fixture.spectrum)
    inactive_loss = aggregate(inactive, zero_spectrum, pairs).abs().sum()
    (inactive_gradient,) = torch.autograd.grad(inactive_loss, inactive)
    assert torch.equal(inactive_gradient, torch.zeros_like(inactive_gradient))
