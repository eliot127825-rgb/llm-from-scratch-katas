import numpy as np
import pytest

from implementation import mean_squared_error


def test_exact_predictions_have_zero_error() -> None:
    y = np.array([1.0, 2.0, 3.0])

    assert mean_squared_error(y, y.copy()) == pytest.approx(0.0)


def test_matches_manual_calculation() -> None:
    y_true = np.array([1.0, 2.0, 4.0])
    y_pred = np.array([2.0, 2.0, 1.0])

    assert mean_squared_error(y_true, y_pred) == pytest.approx(10.0 / 3.0)


def test_accepts_integer_arrays_and_returns_float() -> None:
    result = mean_squared_error(np.array([1, 3]), np.array([2, 1]))

    assert result == pytest.approx(2.5)
    assert isinstance(result, float)


@pytest.mark.parametrize(
    ("y_true", "y_pred"),
    [
        ([1.0], np.array([1.0])),
        (np.array([1.0]), [1.0]),
        (np.array([]), np.array([])),
        (np.ones((2, 1)), np.ones((2, 1))),
        (np.ones(2), np.ones(3)),
        (np.array([True, False]), np.array([True, False])),
        (np.array([1.0, np.nan]), np.array([1.0, 2.0])),
    ],
)
def test_rejects_invalid_input(y_true: object, y_pred: object) -> None:
    with pytest.raises(ValueError):
        mean_squared_error(  # type: ignore[arg-type]
            y_true,
            y_pred,
        )
