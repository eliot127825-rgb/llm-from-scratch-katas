import copy

import pytest

from implementation import min_max_scale


def test_scales_positive_values() -> None:
    assert min_max_scale([2, 4, 6]) == pytest.approx([0.0, 0.5, 1.0])


def test_scales_negative_and_unsorted_values() -> None:
    assert min_max_scale([5.0, -5.0, 0.0]) == pytest.approx(
        [1.0, 0.0, 0.5]
    )


def test_two_values() -> None:
    assert min_max_scale([10, 20]) == pytest.approx([0.0, 1.0])


def test_does_not_modify_input() -> None:
    values = [3.0, 1.0, 2.0]
    original = copy.deepcopy(values)

    min_max_scale(values)

    assert values == original


@pytest.mark.parametrize(
    "values",
    [
        [],
        (1.0, 2.0),
        [1.0, "2"],
        [True, 2.0],
        [1.0, float("inf")],
        [3.0, 3.0],
    ],
)
def test_rejects_invalid_input(values: object) -> None:
    with pytest.raises(ValueError):
        min_max_scale(values)  # type: ignore[arg-type]
