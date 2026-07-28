import numpy as np
import pytest

from implementation import scaled_dot_product_attention


def reference_attention(
    query: np.ndarray,
    key: np.ndarray,
    value: np.ndarray,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    scores = np.matmul(query, np.swapaxes(key, -1, -2))
    scores = scores / np.sqrt(query.shape[-1])
    if mask is not None:
        scores = np.where(mask, scores, -np.inf)
    maximum = np.max(scores, axis=-1, keepdims=True)
    numerator = np.exp(scores - maximum)
    if mask is not None:
        numerator = np.where(mask, numerator, 0.0)
    weights = numerator / np.sum(numerator, axis=-1, keepdims=True)
    return np.matmul(weights, value), weights


def test_unmasked_attention_matches_reference() -> None:
    query = np.array([[[1.0, 0.0], [0.0, 1.0]]])
    key = np.array([[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]])
    value = np.array([[[2.0, 0.0], [0.0, 4.0], [3.0, 5.0]]])

    output, weights = scaled_dot_product_attention(query, key, value)
    expected_output, expected_weights = reference_attention(query, key, value)

    np.testing.assert_allclose(output, expected_output)
    np.testing.assert_allclose(weights, expected_weights)
    np.testing.assert_allclose(weights.sum(axis=-1), 1.0)


def test_boolean_mask_blocks_positions() -> None:
    query = np.array([[[1.0, 0.0], [0.0, 1.0]]])
    key = np.array([[[1.0, 0.0], [0.0, 1.0]]])
    value = np.array([[[10.0], [20.0]]])
    mask = np.array([[True, False], [True, True]])

    output, weights = scaled_dot_product_attention(query, key, value, mask)
    expected_output, expected_weights = reference_attention(
        query,
        key,
        value,
        mask,
    )

    np.testing.assert_allclose(output, expected_output)
    np.testing.assert_allclose(weights, expected_weights)
    assert weights[0, 0, 1] == 0.0


def test_mask_broadcasts_over_batch_and_query_dimensions() -> None:
    query = np.ones((2, 3, 4))
    key = np.ones((2, 5, 4))
    value = np.arange(20, dtype=np.float64).reshape(2, 5, 2)
    mask = np.array([True, True, False, False, False])

    output, weights = scaled_dot_product_attention(query, key, value, mask)

    assert output.shape == (2, 3, 2)
    assert weights.shape == (2, 3, 5)
    np.testing.assert_array_equal(weights[..., 2:], 0.0)


def test_large_scores_stay_finite() -> None:
    query = np.array([[[1000.0, 1000.0]]])
    key = np.array([[[1000.0, 1000.0], [999.0, 999.0]]])
    value = np.array([[[1.0], [2.0]]])

    output, weights = scaled_dot_product_attention(query, key, value)

    assert np.all(np.isfinite(output))
    assert np.all(np.isfinite(weights))


@pytest.mark.parametrize(
    ("query", "key", "value", "mask"),
    [
        (np.ones((2, 3)), np.ones((2, 3, 4)), np.ones((2, 3, 4)), None),
        (
            np.ones((2, 3, 4)),
            np.ones((3, 3, 4)),
            np.ones((2, 3, 4)),
            None,
        ),
        (
            np.ones((2, 3, 4)),
            np.ones((2, 3, 5)),
            np.ones((2, 3, 4)),
            None,
        ),
        (
            np.ones((2, 3, 4)),
            np.ones((2, 5, 4)),
            np.ones((2, 3, 6)),
            None,
        ),
        (
            np.ones((2, 3, 4)),
            np.ones((2, 5, 4)),
            np.ones((2, 5, 6)),
            np.ones((3, 5)),
        ),
        (
            np.ones((1, 2, 3)),
            np.ones((1, 2, 3)),
            np.ones((1, 2, 4)),
            np.array([[False, False], [True, True]]),
        ),
    ],
)
def test_rejects_invalid_inputs(
    query: np.ndarray,
    key: np.ndarray,
    value: np.ndarray,
    mask: np.ndarray | None,
) -> None:
    with pytest.raises(ValueError):
        scaled_dot_product_attention(query, key, value, mask)
