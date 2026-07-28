import numpy as np
import pytest

from implementation import stable_softmax


def reference_softmax(x: np.ndarray, axis: int) -> np.ndarray:
    shifted = x - np.max(x, axis=axis, keepdims=True)
    numerator = np.exp(shifted)
    return numerator / np.sum(numerator, axis=axis, keepdims=True)


@pytest.mark.parametrize("axis", [0, 1, -1])
def test_matches_reference(axis: int) -> None:
    x = np.array([[1.0, -2.0, 3.0], [0.5, 4.0, -1.0]])

    result = stable_softmax(x, axis=axis)

    np.testing.assert_allclose(result, reference_softmax(x, axis))
    np.testing.assert_allclose(np.sum(result, axis=axis), 1.0)
    assert result.shape == x.shape


def test_large_logits_are_finite() -> None:
    result = stable_softmax(np.array([1000.0, 1001.0, 1002.0]))

    assert np.all(np.isfinite(result))
    np.testing.assert_allclose(result.sum(), 1.0)


def test_is_invariant_to_constant_shift() -> None:
    x = np.array([[1.0, 2.0, 3.0]])

    np.testing.assert_allclose(stable_softmax(x), stable_softmax(x + 1000.0))


@pytest.mark.parametrize(
    ("x", "axis"),
    [
        ([1.0, 2.0], 0),
        (np.array(1.0), 0),
        (np.array([], dtype=np.float64), 0),
        (np.array([1, 2]), 0),
        (np.array([1.0, np.inf]), 0),
        (np.ones((2, 3)), 2),
    ],
)
def test_rejects_invalid_input(x: object, axis: int) -> None:
    with pytest.raises(ValueError):
        stable_softmax(x, axis=axis)  # type: ignore[arg-type]
