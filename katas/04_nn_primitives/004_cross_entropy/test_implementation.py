import numpy as np
import pytest

from implementation import cross_entropy


def reference_losses(logits: np.ndarray, targets: np.ndarray) -> np.ndarray:
    maximum = np.max(logits, axis=1, keepdims=True)
    log_partition = maximum[:, 0] + np.log(
        np.sum(np.exp(logits - maximum), axis=1)
    )
    return log_partition - logits[np.arange(logits.shape[0]), targets]


def test_none_reduction_matches_reference() -> None:
    logits = np.array([[2.0, 0.0, -1.0], [0.5, 1.5, -2.0]])
    targets = np.array([0, 2])

    np.testing.assert_allclose(
        cross_entropy(logits, targets, reduction="none"),
        reference_losses(logits, targets),
    )


def test_sum_and_mean_reductions() -> None:
    logits = np.array([[1.0, 2.0], [3.0, -1.0], [0.0, 0.0]])
    targets = np.array([1, 0, 1])
    expected = reference_losses(logits, targets)

    np.testing.assert_allclose(
        cross_entropy(logits, targets, reduction="sum"),
        expected.sum(),
    )
    np.testing.assert_allclose(
        cross_entropy(logits, targets, reduction="mean"),
        expected.mean(),
    )


def test_ignore_index() -> None:
    logits = np.array([[1.0, 2.0], [3.0, -1.0], [0.0, 0.0]])
    targets = np.array([1, -100, 0])
    expected_valid = reference_losses(logits[[0, 2]], np.array([1, 0]))

    losses = cross_entropy(
        logits,
        targets,
        reduction="none",
        ignore_index=-100,
    )

    np.testing.assert_allclose(losses, [expected_valid[0], 0.0, expected_valid[1]])
    np.testing.assert_allclose(
        cross_entropy(logits, targets, ignore_index=-100),
        expected_valid.mean(),
    )


def test_large_logits_are_finite() -> None:
    result = cross_entropy(
        np.array([[1000.0, 1001.0]]),
        np.array([1]),
    )

    assert np.isfinite(result)


@pytest.mark.parametrize(
    ("logits", "targets", "reduction", "ignore_index"),
    [
        ([1.0, 2.0], np.array([0]), "mean", None),
        (np.ones((2, 3)), [0, 1], "mean", None),
        (np.ones((2, 3)), np.array([0.0, 1.0]), "mean", None),
        (np.ones((2, 3)), np.array([0]), "mean", None),
        (np.ones((2, 3)), np.array([0, 3]), "mean", None),
        (np.ones((2, 3)), np.array([0, 1]), "median", None),
        (np.array([[1.0, np.inf]]), np.array([0]), "mean", None),
        (np.ones((2, 3)), np.array([-1, -1]), "mean", -1),
    ],
)
def test_rejects_invalid_inputs(
    logits: object,
    targets: object,
    reduction: str,
    ignore_index: int | None,
) -> None:
    with pytest.raises(ValueError):
        cross_entropy(
            logits,  # type: ignore[arg-type]
            targets,  # type: ignore[arg-type]
            reduction=reduction,
            ignore_index=ignore_index,
        )
