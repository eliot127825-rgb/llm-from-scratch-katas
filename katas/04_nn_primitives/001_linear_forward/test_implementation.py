import numpy as np
import pytest

from implementation import linear_forward


def test_two_dimensional_input() -> None:
    x = np.array([[1.0, 2.0], [3.0, 4.0]])
    weight = np.array([[1.0, 0.0], [0.5, 2.0], [-1.0, 1.0]])
    bias = np.array([0.5, -1.0, 2.0])

    expected = np.matmul(x, weight.T) + bias

    np.testing.assert_allclose(linear_forward(x, weight, bias), expected)


def test_sequence_input_and_no_bias() -> None:
    x = np.arange(24, dtype=np.float64).reshape(2, 3, 4)
    weight = np.arange(20, dtype=np.float64).reshape(5, 4)

    result = linear_forward(x, weight)

    np.testing.assert_allclose(result, np.matmul(x, weight.T))
    assert result.shape == (2, 3, 5)


def test_does_not_modify_inputs() -> None:
    x = np.ones((2, 3))
    weight = np.ones((4, 3))
    bias = np.ones(4)
    before = (x.copy(), weight.copy(), bias.copy())

    linear_forward(x, weight, bias)

    for actual, expected in zip((x, weight, bias), before):
        np.testing.assert_array_equal(actual, expected)


@pytest.mark.parametrize(
    ("x", "weight", "bias"),
    [
        ([1.0, 2.0], np.ones((3, 2)), None),
        (np.ones((2, 3)), np.ones(3), None),
        (np.ones((2, 3)), np.ones((4, 2)), None),
        (np.ones((2, 3)), np.ones((4, 3)), np.ones(3)),
        (np.ones((0, 3)), np.ones((4, 3)), None),
    ],
)
def test_rejects_invalid_inputs(
    x: object,
    weight: object,
    bias: object,
) -> None:
    with pytest.raises(ValueError):
        linear_forward(x, weight, bias)  # type: ignore[arg-type]
