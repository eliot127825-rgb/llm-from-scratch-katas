import copy

import pytest

from implementation import train_test_split


FEATURES = [[0.0], [1.0], [2.0], [3.0], [4.0]]
LABELS = [10, 11, 12, 13, 14]


def test_split_sizes_and_alignment() -> None:
    train_x, test_x, train_y, test_y = train_test_split(
        FEATURES,
        LABELS,
        test_ratio=0.4,
        seed=7,
    )

    assert len(train_x) == len(train_y) == 3
    assert len(test_x) == len(test_y) == 2
    for row, label in zip(train_x + test_x, train_y + test_y):
        assert int(row[0]) + 10 == label


def test_same_seed_is_reproducible() -> None:
    first = train_test_split(FEATURES, LABELS, 0.4, 42)
    second = train_test_split(FEATURES, LABELS, 0.4, 42)

    assert first == second


def test_different_seed_changes_order() -> None:
    first = train_test_split(FEATURES, LABELS, 0.4, 1)
    second = train_test_split(FEATURES, LABELS, 0.4, 2)

    assert first != second


def test_does_not_modify_or_alias_inputs() -> None:
    features = copy.deepcopy(FEATURES)
    labels = LABELS.copy()
    original_features = copy.deepcopy(features)

    train_x, test_x, _, _ = train_test_split(features, labels, 0.4, 3)
    (train_x + test_x)[0][0] = -999

    assert features == original_features
    assert labels == LABELS


@pytest.mark.parametrize(
    ("features", "labels", "ratio", "seed"),
    [
        ([], [], 0.2, 1),
        ([[1.0]], [0], 0.2, 1),
        ([[1.0], [2.0]], [0], 0.5, 1),
        ([[1.0], [2.0, 3.0]], [0, 1], 0.5, 1),
        ([[1.0], [2.0]], [0, True], 0.5, 1),
        ([[1.0], [2.0]], [0, 1], 0.0, 1),
        ([[1.0], [2.0]], [0, 1], 0.1, 1),
        ([[1.0], [2.0]], [0, 1], 0.5, True),
    ],
)
def test_rejects_invalid_input(
    features: object,
    labels: object,
    ratio: object,
    seed: object,
) -> None:
    with pytest.raises(ValueError):
        train_test_split(  # type: ignore[arg-type]
            features,
            labels,
            ratio,
            seed,
        )
