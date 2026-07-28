import numpy as np
import pytest

from implementation import causal_mask


def test_length_four() -> None:
    expected = np.array(
        [
            [True, False, False, False],
            [True, True, False, False],
            [True, True, True, False],
            [True, True, True, True],
        ]
    )

    np.testing.assert_array_equal(causal_mask(4), expected)


def test_length_one() -> None:
    result = causal_mask(1)

    np.testing.assert_array_equal(result, np.array([[True]]))
    assert result.dtype == np.bool_


def test_calls_return_independent_arrays() -> None:
    first = causal_mask(2)
    second = causal_mask(2)
    first[0, 0] = False

    assert second[0, 0]


@pytest.mark.parametrize("length", [0, -1, 1.5, "3", True])
def test_rejects_invalid_lengths(length: object) -> None:
    with pytest.raises(ValueError):
        causal_mask(length)  # type: ignore[arg-type]
