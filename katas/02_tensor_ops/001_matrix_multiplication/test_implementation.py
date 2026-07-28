import copy

import pytest

from implementation import matrix_multiply


def test_example() -> None:
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]

    assert matrix_multiply(a, b) == [[58, 64], [139, 154]]


def test_one_by_one() -> None:
    assert matrix_multiply([[3]], [[4]]) == [[12]]


def test_rectangular_result() -> None:
    a = [[1, 2], [3, 4], [5, 6]]
    b = [[1, 2, 3, 4], [5, 6, 7, 8]]

    assert matrix_multiply(a, b) == [
        [11, 14, 17, 20],
        [23, 30, 37, 44],
        [35, 46, 57, 68],
    ]


def test_negative_and_float_values() -> None:
    result = matrix_multiply([[1.5, -2.0]], [[2.0], [0.5]])

    assert result[0][0] == pytest.approx(2.0)


def test_does_not_modify_inputs() -> None:
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    original_a = copy.deepcopy(a)
    original_b = copy.deepcopy(b)

    matrix_multiply(a, b)

    assert a == original_a
    assert b == original_b


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ([], [[1]]),
        ([[1]], []),
        ([[]], [[1]]),
        ([[1]], [[]]),
    ],
)
def test_rejects_empty_matrices(
    a: list[list[float]],
    b: list[list[float]],
) -> None:
    with pytest.raises(ValueError):
        matrix_multiply(a, b)


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ([[1, 2], [3]], [[1], [2]]),
        ([[1, 2]], [[1, 2], [3]]),
    ],
)
def test_rejects_ragged_matrices(
    a: list[list[float]],
    b: list[list[float]],
) -> None:
    with pytest.raises(ValueError):
        matrix_multiply(a, b)


def test_rejects_incompatible_shapes() -> None:
    with pytest.raises(ValueError):
        matrix_multiply([[1, 2, 3]], [[1, 2], [3, 4]])
