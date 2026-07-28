import numpy as np
import pytest

from implementation import knn_predict


def test_one_nearest_neighbor() -> None:
    train_x = np.array([[0.0], [2.0], [10.0]])
    train_y = np.array([0, 0, 1])
    query_x = np.array([[1.5], [9.0]])

    np.testing.assert_array_equal(
        knn_predict(train_x, train_y, query_x, k=1),
        np.array([0, 1]),
    )


def test_majority_vote() -> None:
    train_x = np.array([[0.0], [1.0], [2.0], [10.0]])
    train_y = np.array([2, 2, 1, 1])
    query_x = np.array([[1.5]])

    np.testing.assert_array_equal(
        knn_predict(train_x, train_y, query_x, k=3),
        np.array([2]),
    )


def test_vote_tie_uses_smaller_label() -> None:
    train_x = np.array([[0.0], [2.0]])
    train_y = np.array([5, 3])
    query_x = np.array([[1.0]])

    np.testing.assert_array_equal(
        knn_predict(train_x, train_y, query_x, k=2),
        np.array([3]),
    )


def test_multiple_features_and_queries() -> None:
    train_x = np.array([[0.0, 0.0], [1.0, 1.0], [5.0, 5.0]])
    train_y = np.array([0, 0, 1])
    query_x = np.array([[0.5, 0.5], [4.5, 5.0]])

    result = knn_predict(train_x, train_y, query_x, k=1)

    np.testing.assert_array_equal(result, np.array([0, 1]))
    assert result.shape == (2,)


@pytest.mark.parametrize(
    ("train_x", "train_y", "query_x", "k"),
    [
        ([[]], np.array([0]), np.ones((1, 1)), 1),
        (np.ones((2, 1)), [0, 1], np.ones((1, 1)), 1),
        (np.ones((2, 1)), np.array([0]), np.ones((1, 1)), 1),
        (np.ones((2, 1)), np.array([0.0, 1.0]), np.ones((1, 1)), 1),
        (np.ones((2, 2)), np.array([0, 1]), np.ones((1, 1)), 1),
        (np.ones((2, 1)), np.array([0, 1]), np.ones((0, 1)), 1),
        (np.ones((2, 1)), np.array([0, 1]), np.ones((1, 1)), 0),
        (np.ones((2, 1)), np.array([0, 1]), np.ones((1, 1)), 3),
        (np.ones((2, 1)), np.array([0, 1]), np.ones((1, 1)), True),
        (
            np.array([[1.0], [np.inf]]),
            np.array([0, 1]),
            np.ones((1, 1)),
            1,
        ),
    ],
)
def test_rejects_invalid_input(
    train_x: object,
    train_y: object,
    query_x: object,
    k: object,
) -> None:
    with pytest.raises(ValueError):
        knn_predict(  # type: ignore[arg-type]
            train_x,
            train_y,
            query_x,
            k,
        )
