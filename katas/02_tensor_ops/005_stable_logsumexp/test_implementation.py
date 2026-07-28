import numpy as np
import pytest

from implementation import stable_logsumexp


def reference_logsumexp(
    x: np.ndarray,
    axis: int,
    keepdims: bool,
) -> np.ndarray:
    maximum = np.max(x, axis=axis, keepdims=True)
    result = maximum + np.log(
        np.sum(np.exp(x - maximum), axis=axis, keepdims=True)
    )
    if not keepdims:
        result = np.squeeze(result, axis=axis)
    return result


@pytest.mark.parametrize("axis", [0, 1, -1])
@pytest.mark.parametrize("keepdims", [False, True])
def test_matches_reference(axis: int, keepdims: bool) -> None:
    x = np.array([[1.0, -2.0, 3.0], [0.5, 4.0, -1.0]])

    np.testing.assert_allclose(
        stable_logsumexp(x, axis=axis, keepdims=keepdims),
        reference_logsumexp(x, axis=axis, keepdims=keepdims),
    )


def test_large_values_stay_finite() -> None:
    result = stable_logsumexp(np.array([1000.0, 1000.0]))

    assert np.isfinite(result)
    np.testing.assert_allclose(result, 1000.0 + np.log(2.0))


def test_large_negative_values_stay_finite() -> None:
    result = stable_logsumexp(np.array([-1000.0, -1001.0]))

    assert np.isfinite(result)


@pytest.mark.parametrize(
    ("x", "axis"),
    [
        ([1.0, 2.0], 0),
        (np.array(3.0), 0),
        (np.ones((2, 0)), 1),
        (np.ones((2, 3)), 2),
    ],
)
def test_rejects_invalid_input(x: object, axis: int) -> None:
    with pytest.raises(ValueError):
        stable_logsumexp(x, axis=axis)  # type: ignore[arg-type]
