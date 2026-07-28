import numpy as np
import pytest

from implementation import batched_matrix_multiply


def test_matches_numpy_matmul() -> None:
    a = np.arange(24, dtype=np.float64).reshape(2, 3, 4)
    b = np.arange(40, dtype=np.float64).reshape(2, 4, 5)

    actual = batched_matrix_multiply(a, b)

    np.testing.assert_allclose(actual, np.matmul(a, b))
    assert actual.shape == (2, 3, 5)


def test_batch_size_one() -> None:
    a = np.array([[[1, 2], [3, 4]]], dtype=np.float32)
    b = np.array([[[5], [6]]], dtype=np.float32)

    np.testing.assert_allclose(
        batched_matrix_multiply(a, b),
        np.array([[[17], [39]]], dtype=np.float32),
    )


def test_does_not_modify_inputs() -> None:
    a = np.ones((2, 2, 3))
    b = np.ones((2, 3, 2))
    a_before = a.copy()
    b_before = b.copy()

    batched_matrix_multiply(a, b)

    np.testing.assert_array_equal(a, a_before)
    np.testing.assert_array_equal(b, b_before)


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (np.ones((2, 3)), np.ones((2, 3, 4))),
        (np.ones((2, 3, 4)), np.ones((3, 4, 5))),
        (np.ones((2, 3, 4)), np.ones((2, 5, 6))),
        (np.ones((0, 3, 4)), np.ones((0, 4, 5))),
    ],
)
def test_rejects_invalid_shapes(a: np.ndarray, b: np.ndarray) -> None:
    with pytest.raises(ValueError):
        batched_matrix_multiply(a, b)
