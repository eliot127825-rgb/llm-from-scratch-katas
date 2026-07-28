import numpy as np
import pytest

from implementation import embedding_lookup


def test_vector_ids() -> None:
    weight = np.arange(20, dtype=np.float32).reshape(5, 4)
    token_ids = np.array([3, 0, 3, 2])

    np.testing.assert_array_equal(
        embedding_lookup(weight, token_ids),
        weight[token_ids],
    )


def test_batched_sequence_ids() -> None:
    weight = np.arange(18).reshape(6, 3)
    token_ids = np.array([[0, 2, 5], [1, 1, 4]])

    result = embedding_lookup(weight, token_ids)

    np.testing.assert_array_equal(result, weight[token_ids])
    assert result.shape == (2, 3, 3)


def test_result_does_not_alias_weight() -> None:
    weight = np.arange(12).reshape(4, 3)
    result = embedding_lookup(weight, np.array([1, 2]))
    result[0, 0] = -999

    assert weight[1, 0] != -999


@pytest.mark.parametrize(
    ("weight", "token_ids"),
    [
        ([1, 2], np.array([0])),
        (np.ones((3, 2)), [0, 1]),
        (np.ones((3, 2)), np.array([0.0, 1.0])),
        (np.ones((3, 2)), np.array([-1, 0])),
        (np.ones((3, 2)), np.array([0, 3])),
        (np.ones((0, 2)), np.array([0])),
        (np.ones((3, 2)), np.array([], dtype=np.int64)),
    ],
)
def test_rejects_invalid_inputs(weight: object, token_ids: object) -> None:
    with pytest.raises(ValueError):
        embedding_lookup(weight, token_ids)  # type: ignore[arg-type]
