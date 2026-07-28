import numpy as np
import pytest

from implementation import layer_norm


def reference_layer_norm(
    x: np.ndarray,
    gamma: np.ndarray,
    beta: np.ndarray,
    eps: float,
) -> np.ndarray:
    mean = np.mean(x, axis=-1, keepdims=True)
    variance = np.mean((x - mean) ** 2, axis=-1, keepdims=True)
    return (x - mean) / np.sqrt(variance + eps) * gamma + beta


def test_matrix_input_matches_reference() -> None:
    x = np.array([[1.0, 2.0, 4.0], [-1.0, 0.5, 3.0]])
    gamma = np.array([1.0, 0.5, 2.0])
    beta = np.array([0.0, 1.0, -1.0])

    np.testing.assert_allclose(
        layer_norm(x, gamma, beta),
        reference_layer_norm(x, gamma, beta, 1e-5),
    )


def test_batched_sequence_input() -> None:
    x = np.arange(24, dtype=np.float64).reshape(2, 3, 4)
    gamma = np.ones(4)
    beta = np.zeros(4)

    result = layer_norm(x, gamma, beta)

    assert result.shape == x.shape
    np.testing.assert_allclose(np.mean(result, axis=-1), 0.0, atol=1e-7)
    np.testing.assert_allclose(np.var(result, axis=-1), 1.0, atol=2e-5)


def test_constant_vector_is_finite() -> None:
    result = layer_norm(
        np.ones((2, 3)),
        np.ones(3),
        np.zeros(3),
    )

    assert np.all(np.isfinite(result))
    np.testing.assert_allclose(result, 0.0)


@pytest.mark.parametrize(
    ("x", "gamma", "beta", "eps"),
    [
        ([1.0, 2.0], np.ones(2), np.zeros(2), 1e-5),
        (np.array(1.0), np.ones(1), np.zeros(1), 1e-5),
        (np.ones((2, 0)), np.ones(0), np.zeros(0), 1e-5),
        (np.ones((2, 3)), np.ones(2), np.zeros(3), 1e-5),
        (np.ones((2, 3)), np.ones(3), np.zeros((1, 3)), 1e-5),
        (np.ones((2, 3), dtype=np.int64), np.ones(3), np.zeros(3), 1e-5),
        (np.ones((2, 3)), np.ones(3), np.zeros(3), 0.0),
    ],
)
def test_rejects_invalid_inputs(
    x: object,
    gamma: object,
    beta: object,
    eps: float,
) -> None:
    with pytest.raises(ValueError):
        layer_norm(  # type: ignore[arg-type]
            x,
            gamma,
            beta,
            eps,
        )
