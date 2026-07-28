import numpy as np
import pytest

from implementation import rms_norm


def reference_rms_norm(
    x: np.ndarray,
    weight: np.ndarray,
    eps: float,
) -> np.ndarray:
    rms = np.sqrt(np.mean(x**2, axis=-1, keepdims=True) + eps)
    return x / rms * weight


def test_matrix_input_matches_reference() -> None:
    x = np.array([[1.0, 2.0, 4.0], [-1.0, 0.5, 3.0]])
    weight = np.array([1.0, 0.5, 2.0])

    np.testing.assert_allclose(
        rms_norm(x, weight),
        reference_rms_norm(x, weight, 1e-6),
    )


def test_batched_sequence_input() -> None:
    x = np.arange(1, 25, dtype=np.float64).reshape(2, 3, 4)
    weight = np.ones(4)

    result = rms_norm(x, weight)

    assert result.shape == x.shape
    np.testing.assert_allclose(
        np.mean(result**2, axis=-1),
        1.0,
        atol=2e-6,
    )


def test_zero_vector_is_finite() -> None:
    result = rms_norm(np.zeros((2, 3)), np.ones(3))

    assert np.all(np.isfinite(result))
    np.testing.assert_allclose(result, 0.0)


@pytest.mark.parametrize(
    ("x", "weight", "eps"),
    [
        ([1.0, 2.0], np.ones(2), 1e-6),
        (np.array(1.0), np.ones(1), 1e-6),
        (np.ones((2, 0)), np.ones(0), 1e-6),
        (np.ones((2, 3)), np.ones(2), 1e-6),
        (np.ones((2, 3)), np.ones((1, 3)), 1e-6),
        (np.ones((2, 3), dtype=np.int64), np.ones(3), 1e-6),
        (np.ones((2, 3)), np.ones(3), -1.0),
    ],
)
def test_rejects_invalid_inputs(
    x: object,
    weight: object,
    eps: float,
) -> None:
    with pytest.raises(ValueError):
        rms_norm(  # type: ignore[arg-type]
            x,
            weight,
            eps,
        )
