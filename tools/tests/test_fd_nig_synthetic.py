"""Frozen EXP-0003 numerical gates. DO NOT RUN before formal Plan authorization."""
from __future__ import annotations

from pathlib import Path

import pytest
import torch

from tools.fd_nig_aggregation import (
    absolute_scales, aggregate, enforce_hermitian, hermitian_residual,
    inverse_real, pair_products, route_pairs, select_sparse_pairs,
)
from tools.fd_nig_reference import (
    exhaustive_aggregate, load_config, make_fixture, make_mask,
    pair_products as independently_expanded_products,
    route_pairs as independent_routing, zero_safe_error,
)


CONFIG = load_config(Path(__file__).resolve().parents[1] / "fd_nig_config.json")
SEED = CONFIG["seed"]
SIZE = CONFIG["grid"]["height"]
FFT_NORM = CONFIG["fft"]["normalization"]
DTYPES = (
    (torch.complex128, "float64"),
    (torch.complex64, "float32"),
)


def tolerance(precision: str) -> tuple[float, float]:
    values = CONFIG["tolerances"][precision]
    return values["atol"], values["rtol"]


def fixture_for(dtype: torch.dtype, size: int = SIZE):
    fixture = make_fixture(seed=SEED, height=size, width=size)
    return fixture, fixture.spectrum.to(dtype), fixture.coefficients.to(dtype)


def assert_zero_safe(actual, expected, contributions, pairs, precision,
                     record_property, label):
    side = actual.shape[-1]
    bins = independent_routing(pairs, side, side)
    scales = absolute_scales(contributions, bins, side * side).reshape(actual.shape)
    atol, rtol = tolerance(precision)
    excess = zero_safe_error(actual, expected, scales, atol=atol, rtol=rtol)
    record_property(label + "_max_abs", float((actual - expected).abs().max()))
    record_property(label + "_max_excess", float(excess.max()))
    record_property(label + "_empty_bins", int((scales == 0).sum()))
    nonzero = scales > 0
    cancel_ratio = torch.where(
        nonzero, expected.abs() / scales,
        torch.full_like(scales, float("inf")),
    )
    record_property(label + "_min_cancellation_ratio", float(cancel_ratio.min()))
    assert torch.isfinite(actual.real).all() and torch.isfinite(actual.imag).all()
    assert torch.isfinite(excess).all()
    assert torch.all(excess <= 0), label + " zero-safe error exceeded frozen gate"
    return scales


def test_frozen_configuration_and_cpu_fft_contract():
    assert CONFIG["numerical_memory_freeze_status"] == "approved"
    assert CONFIG["tolerances"]["status"] == "approved"
    assert CONFIG["status"] == "frozen"
    # Formal execution approval is checked only by the guarded runner, not pytest.
    assert CONFIG["grid"] == {"height": 16, "width": 16, "circular": True}
    assert CONFIG["seed"] == 20261011
    assert CONFIG["fft"] == {"order": "native-unshifted", "normalization": "backward"}
    assert CONFIG["pair_policy"] == {"reference": "all", "sparse_count": 256,
                                      "order": "lexicographic"}
    assert CONFIG["compute_budget"]["wall_seconds"] == 120
    assert CONFIG["compute_budget"]["wall_scope"] == "both-repetitions-total"
    assert CONFIG["compute_budget"]["memory_metric"] == "peak-process-tree-rss"
    assert CONFIG["compute_budget"]["watchdog_stop_mib"] == 1536
    assert CONFIG["compute_budget"]["watchdog_sample_ms"] == 100
    assert CONFIG["compute_budget"]["memory_gb"] == 2
    assert not torch.cuda.is_available() or CONFIG["compute_budget"]["device"] == "cpu"
    fixture = make_fixture(seed=SEED, height=SIZE, width=SIZE)
    assert torch.equal(fixture.spectrum, torch.fft.fft2(fixture.mask, norm=FFT_NORM))
    binary = make_mask(seed=SEED, height=SIZE, width=SIZE, binary=True)
    assert torch.all((binary == 0) | (binary == 1))
    assert torch.equal(binary, make_mask(seed=SEED, height=SIZE, width=SIZE, binary=True))
    assert not torch.equal(binary, fixture.mask)


def test_full_16x16_pair_routing_and_bin_counts():
    fixture = make_fixture(seed=SEED, height=SIZE, width=SIZE)
    actual = route_pairs(fixture.pairs, SIZE, SIZE)
    expected = independent_routing(fixture.pairs, SIZE, SIZE)
    assert len(fixture.pairs) == 65536
    assert torch.equal(actual, expected)
    assert torch.all((actual >= 0) & (actual < SIZE * SIZE))
    # Every q receives exactly |K|=256 pairs in the complete circular grid.
    assert torch.equal(torch.bincount(actual, minlength=SIZE * SIZE),
                       torch.full((SIZE * SIZE,), SIZE * SIZE, dtype=torch.long))


@pytest.mark.parametrize("dtype,precision", DTYPES)
def test_full_16x16_complex_pair_products(dtype, precision, record_property):
    fixture, spectrum, coefficients = fixture_for(dtype)
    actual = pair_products(coefficients, spectrum, fixture.pairs)
    reference = independently_expanded_products(coefficients, spectrum, fixture.pairs)
    atol, rtol = tolerance(precision)
    error = (actual - reference).abs()
    threshold = atol + rtol * reference.abs()
    record_property("max_pair_absolute_error", float(error.max()))
    record_property("max_pair_zero_safe_excess", float((error - threshold).max()))
    assert torch.isfinite(actual.real).all() and torch.isfinite(actual.imag).all()
    assert torch.all(error <= threshold)


@pytest.mark.parametrize("dtype,precision", DTYPES)
def test_full_16x16_dense_aggregation(dtype, precision, record_property):
    fixture, spectrum, coefficients = fixture_for(dtype)
    candidate = aggregate(coefficients, spectrum, fixture.pairs)
    independent = exhaustive_aggregate(coefficients, spectrum, fixture.pairs)
    products = independently_expanded_products(coefficients, spectrum, fixture.pairs)
    assert_zero_safe(candidate, independent, products, fixture.pairs,
                     precision, record_property, "dense_16")


@pytest.mark.parametrize("dtype,precision", DTYPES)
def test_raw_16x16_hermitian_dc_nyquist_and_inverse(dtype, precision, record_property):
    fixture, spectrum, _ = fixture_for(dtype)
    coefficients = fixture.hermitian_coefficients.to(dtype)
    candidate = aggregate(coefficients, spectrum, fixture.pairs)
    reference = exhaustive_aggregate(coefficients, spectrum, fixture.pairs)
    products = independently_expanded_products(coefficients, spectrum, fixture.pairs)
    scales = assert_zero_safe(candidate, reference, products, fixture.pairs,
                              precision, record_property, "hermitian_16")

    residual = float(hermitian_residual(candidate))
    record_property("raw_hermitian_residual", residual)
    assert residual <= CONFIG["tolerances"]["hermitian"][precision]
    for row, col in ((0, 0), (0, SIZE // 2), (SIZE // 2, 0),
                     (SIZE // 2, SIZE // 2)):
        assert float(candidate[row, col].imag.abs()) <= (
            CONFIG["tolerances"]["self_conjugate_imag"][precision])

    complex_spatial = torch.fft.ifft2(candidate, norm=FFT_NORM)
    residual_img = float(complex_spatial.imag.abs().max())
    record_property("raw_inverse_imaginary_residual", residual_img)
    assert residual_img <= CONFIG["tolerances"]["inverse_imag"][precision]
    reference_img = torch.fft.ifft2(reference, norm=FFT_NORM).real
    # Triangle-inequality bound derived from per-frequency zero-safe limits.
    atol, rtol = tolerance(precision)
    spatial_bound = (atol + rtol * scales).sum() / (SIZE * SIZE)
    assert torch.all((complex_spatial.real - reference_img).abs() <= spatial_bound)
    assert torch.allclose(
        enforce_hermitian(candidate),
        enforce_hermitian(enforce_hermitian(candidate)),
        atol=CONFIG["tolerances"]["hermitian"][precision], rtol=0,
    )
    checked = inverse_real(candidate, check=True,
                           tolerance=max(CONFIG["tolerances"]["hermitian"][precision],
                                         CONFIG["tolerances"]["inverse_imag"][precision]))
    assert torch.equal(checked, complex_spatial.real)


def test_complex_autograd_real_and_imaginary_centered_finite_differences(record_property):
    fixture, spectrum, _ = fixture_for(torch.complex128, size=4)
    pairs = fixture.pairs[:32]
    coefficients = fixture.coefficients[:32].clone().requires_grad_(True)

    def loss_fn(params):
        reconstructed = inverse_real(aggregate(params, spectrum, pairs),
                                     check=False)
        return (reconstructed - fixture.target).square().mean()

    (grad,) = torch.autograd.grad(loss_fn(coefficients), coefficients)
    assert torch.isfinite(grad.real).all() and torch.isfinite(grad.imag).all()
    step = CONFIG["tolerances"]["finite_difference"]["step"]
    atol = CONFIG["tolerances"]["finite_difference"]["atol"]
    rtol = CONFIG["tolerances"]["finite_difference"]["rtol"]
    for part, direction in (("real", 1.0), ("imag", 1.0j)):
        values = getattr(grad, part)
        index = int(values.abs().argmax())
        analytical = float(values[index])
        assert abs(analytical) > 0, part + " active gradient vanished"
        plus = coefficients.detach().clone()
        minus = coefficients.detach().clone()
        plus[index] += step * direction
        minus[index] -= step * direction
        numerical = float((loss_fn(plus) - loss_fn(minus)) / (2 * step))
        record_property("active_" + part + "_index", index)
        record_property("active_" + part + "_gradient", analytical)
        record_property("active_" + part + "_finite_difference", numerical)
        assert abs(numerical - analytical) <= atol + rtol * abs(analytical)

    inactive = coefficients.detach().clone().requires_grad_(True)
    zero_spectrum = torch.zeros_like(spectrum)
    zero_output = aggregate(inactive, zero_spectrum, pairs)
    (inactive_grad,) = torch.autograd.grad(zero_output.abs().sum(), inactive)
    assert torch.equal(inactive_grad, torch.zeros_like(inactive_grad))


def test_8x8_dense_output_and_gradient_agreement(record_property):
    fixture, spectrum, _ = fixture_for(torch.complex128, size=8)
    coefficients = fixture.coefficients.clone().requires_grad_(True)
    candidate = aggregate(coefficients, spectrum, fixture.pairs)
    reference = exhaustive_aggregate(coefficients, spectrum, fixture.pairs)
    products = independently_expanded_products(coefficients.detach(), spectrum, fixture.pairs)
    assert_zero_safe(candidate, reference, products, fixture.pairs,
                     "float64", record_property, "dense_8")
    (grad_candidate,) = torch.autograd.grad(candidate.abs().sum(), coefficients,
                                            retain_graph=True)
    (grad_reference,) = torch.autograd.grad(reference.abs().sum(), coefficients)
    thresh = CONFIG["tolerances"]["grad_eight_by_eight"]
    err = (grad_candidate - grad_reference).abs()
    record_property("gradient_max_abs", float(err.max()))
    assert torch.all(err <= thresh["atol"] + thresh["rtol"] * grad_reference.abs())
    assert grad_candidate.abs().max() > 0


def test_16x16_primary_dense_candidate_gradient_is_finite_and_active(record_property):
    fixture, spectrum, _ = fixture_for(torch.complex128)
    coefficients = fixture.coefficients.clone().requires_grad_(True)
    image = inverse_real(aggregate(coefficients, spectrum, fixture.pairs),
                         check=False)
    loss = (image - fixture.target).square().mean()
    (grad,) = torch.autograd.grad(loss, coefficients)
    assert torch.isfinite(image).all() and torch.isfinite(loss)
    assert torch.isfinite(grad.real).all() and torch.isfinite(grad.imag).all()
    record_property("dense16_gradient_max_abs", float(grad.abs().max()))
    assert grad.real.abs().max() > 0
    assert grad.imag.abs().max() > 0


def test_sparse_16x16_prefix_swap_closure_coefficient_alignment_and_repeatability():
    fixture, spectrum, _ = fixture_for(torch.complex128)
    selected = select_sparse_pairs(fixture.pairs, CONFIG["pair_policy"]["sparse_count"],
                                   include_swapped=True)
    again = select_sparse_pairs(fixture.pairs, CONFIG["pair_policy"]["sparse_count"],
                                include_swapped=True)
    assert torch.equal(selected, again)
    assert torch.equal(selected[:256], fixture.pairs[:256])
    lookup = {tuple(row): i for i, row in enumerate(fixture.pairs.tolist())}
    keys = [tuple(row) for row in selected.tolist()]
    assert len(set(keys)) == len(keys) == 511
    assert all((a[2], a[3], a[0], a[1]) in set(keys) for a in keys)
    indices = torch.tensor([lookup[key] for key in keys], dtype=torch.long)
    coefficients = fixture.hermitian_coefficients.index_select(0, indices)
    first = aggregate(coefficients, spectrum, selected)
    second = aggregate(coefficients, spectrum, selected)
    reference = exhaustive_aggregate(coefficients, spectrum, selected)
    assert torch.equal(first, second)
    atol, rtol = tolerance("float64")
    assert torch.all((first - reference).abs() <= atol +
                     rtol * reference.abs().sum())
    assert float(hermitian_residual(first)) <= CONFIG["tolerances"]["hermitian"]["float64"]


def test_stress_and_empty_or_cancelled_bins(record_property):
    fixture, spectrum, coefficients = fixture_for(torch.complex128, size=8)
    stress = spectrum * 1e3
    products = pair_products(coefficients, stress, fixture.pairs)
    candidate = aggregate(coefficients, stress, fixture.pairs)
    reference = exhaustive_aggregate(coefficients, stress, fixture.pairs)
    ref_products = independently_expanded_products(coefficients, stress, fixture.pairs)
    assert torch.isfinite(products.real).all() and torch.isfinite(products.imag).all()
    assert_zero_safe(candidate, reference, ref_products, fixture.pairs,
                     "float64", record_property, "stress_8")
    spatial = inverse_real(candidate, check=False)
    coeff = coefficients.clone().requires_grad_(True)
    image = inverse_real(aggregate(coeff, stress, fixture.pairs), check=False)
    loss = image.square().mean()
    (grad,) = torch.autograd.grad(loss, coeff)
    assert torch.isfinite(spatial).all() and torch.isfinite(loss)
    assert torch.isfinite(grad.real).all() and torch.isfinite(grad.imag).all()

    zero = torch.zeros(2, dtype=torch.complex128)
    scale = torch.zeros(2, dtype=torch.float64)
    atol, rtol = tolerance("float64")
    assert torch.all(zero_safe_error(zero, zero, scale, atol, rtol) <= 0)
    tampered = zero.clone()
    tampered[0] = 1e-4
    assert zero_safe_error(tampered, zero, scale, atol, rtol)[0] > 0

    # Exact two-term cancellation, nonzero sum of absolute contributions.
    terms = torch.tensor([1 + 0j, -1 + 0j], dtype=torch.complex128)
    assert float(terms.sum().abs()) == 0.0
    assert float(terms.abs().sum()) > 0
    assert torch.all(zero_safe_error(terms.sum().view(1), terms.sum().view(1),
                                      terms.abs().sum().view(1), atol, rtol) <= 0)
