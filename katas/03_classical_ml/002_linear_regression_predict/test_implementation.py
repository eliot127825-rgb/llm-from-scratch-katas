import numpy as np
import pytest

from implementation import linear_regression_predict


def test_single_feature() -> None:
    features = np.array([[1.0], [2.0], [3.0]])
    weights = np.array([2.0])

    np.testing.assert_allclose(
        linear_regression_predict(features, weights, bias=1.0),
        np.array([3.0, 5.0, 7.0]),
    )


def test_multiple_features() -> None:
    features = np.array([[1.0, 2.0], [3.0, -1.0]])
    weights = np.array([0.5, 2.0])

    result = linear_regression_predict(features, weights, bias=-1.0)

    np.testing.assert_allclose(result, np.array([3.5, -1.5]))
    assert result.shape == (2,)


def test_does_not_modify_inputs() -> None:
    features = np.ones((2, 3))
    weights = np.arange(3, dtype=np.float64)
    features_before = features.copy()
    weights_before = weights.copy()

    linear_regression_predict(features, weights, 0.0)

    np.testing.assert_array_equal(features, features_before)
    np.testing.assert_array_equal(weights, weights_before)


@pytest.mark.parametrize(
    ("features", "weights", "bias"),
    [
        ([[1.0]], np.array([1.0]), 0.0),
        (np.ones((2, 2)), [1.0, 1.0], 0.0),
        (np.ones(2), np.ones(2), 0.0),
        (np.ones((2, 2)), np.ones((2, 1)), 0.0),
        (np.ones((2, 2)), np.ones(3), 0.0),
        (np.ones((0, 2)), np.ones(2), 0.0),
        (np.ones((2, 2)), np.ones(2), float("inf")),
        (np.ones((2, 2)), np.ones(2), True),
    ],
)
def test_rejects_invalid_input(
    features: object,
    weights: object,
    bias: object,
) -> None:
    with pytest.raises(ValueError):
        linear_regression_predict(  # type: ignore[arg-type]
            features,
            weights,
            bias,
        )
