import copy

import pytest

from implementation import count_labels


def test_counts_labels_in_first_seen_order() -> None:
    result = count_labels([2, 1, 2, 0, 1, 2])

    assert result == {2: 3, 1: 2, 0: 1}
    assert list(result) == [2, 1, 0]


def test_empty_input() -> None:
    assert count_labels([]) == {}


def test_negative_labels() -> None:
    assert count_labels([-1, 0, -1]) == {-1: 2, 0: 1}


def test_does_not_modify_input() -> None:
    labels = [1, 2, 1]
    original = copy.deepcopy(labels)

    count_labels(labels)

    assert labels == original


@pytest.mark.parametrize("labels", [(1, 2), "12", [1, 2.0], [True, 1]])
def test_rejects_invalid_input(labels: object) -> None:
    with pytest.raises(ValueError):
        count_labels(labels)  # type: ignore[arg-type]
