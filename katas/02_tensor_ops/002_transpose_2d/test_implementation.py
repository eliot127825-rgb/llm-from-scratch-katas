import copy

import pytest

from implementation import transpose_2d


def test_square_matrix() -> None:
    assert transpose_2d([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_rectangular_matrix() -> None:
    assert transpose_2d([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]


def test_single_row_and_single_column() -> None:
    assert transpose_2d([[1, 2, 3]]) == [[1], [2], [3]]
    assert transpose_2d([[1], [2], [3]]) == [[1, 2, 3]]


def test_does_not_modify_or_alias_input_rows() -> None:
    matrix = [[1, 2], [3, 4]]
    original = copy.deepcopy(matrix)

    result = transpose_2d(matrix)
    result[0][0] = 99

    assert matrix == original


@pytest.mark.parametrize("matrix", [[], [[]], [[1, 2], [3]]])
def test_rejects_invalid_matrices(matrix: list[list[float]]) -> None:
    with pytest.raises(ValueError):
        transpose_2d(matrix)
