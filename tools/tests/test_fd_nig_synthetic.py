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
    symmetric = enforce_hermitian(spectrum)
    assert hermitian_residual(symmetric) == 0
    image = inverse_real(symmetric, check=True, tolerance=1e-10)
    assert torch.isfinite(image).all()
    assert image.dtype.is_floating_point


def test_gradient_propagation_and_centered_finite_difference():
    fixture = make_fixture(height=4, width=4)
    coefficients = fixture.coefficients[:32].clone().requires_grad_(True)
    pairs = fixture.pairs[:32]
    output = inverse_real(aggregate(coefficients, fixture.spectrum, pairs))
    loss = (output - fixture.target).square().mean()
    (gradient,) = torch.autograd.grad(loss, coefficients)
    assert torch.isfinite(gradient.real).all() and torch.isfinite(gradient.imag).all()
    index = 3
    step = 1e-6
    with torch.no_grad():
        plus = coefficients.detach().clone(); plus[index] += step
        minus = coefficients.detach().clone(); minus[index] -= step
    lp = (inverse_real(aggregate(plus, fixture.spectrum, pairs)) - fixture.target).square().mean()
    lm = (inverse_real(aggregate(minus, fixture.spectrum, pairs)) - fixture.target).square().mean()
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
    error = (output - output).abs() - (1e-12 + 1e-12 * scales)
    assert torch.isfinite(error).all()


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
