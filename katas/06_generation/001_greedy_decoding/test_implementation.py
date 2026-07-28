import numpy as np
import pytest

from implementation import greedy_decode


def test_generates_up_to_budget() -> None:
    calls: list[list[int]] = []

    def next_logits(tokens: list[int]) -> np.ndarray:
        calls.append(tokens.copy())
        preferred = len(tokens) % 3
        logits = np.zeros(3, dtype=np.float64)
        logits[preferred] = 1.0
        return logits

    result = greedy_decode([2], next_logits, max_new_tokens=3)

    assert result == [2, 1, 2, 0]
    assert calls == [[2], [2, 1], [2, 1, 2]]


def test_stops_after_emitting_eos() -> None:
    call_count = 0

    def next_logits(tokens: list[int]) -> np.ndarray:
        nonlocal call_count
        call_count += 1
        if len(tokens) == 1:
            return np.array([0.0, 2.0, 1.0])
        return np.array([0.0, 1.0, 3.0])

    result = greedy_decode(
        [0],
        next_logits,
        max_new_tokens=10,
        eos_token_id=2,
    )

    assert result == [0, 1, 2]
    assert call_count == 2


def test_tie_breaks_to_smallest_token_id() -> None:
    def next_logits(tokens: list[int]) -> np.ndarray:
        return np.array([1.0, 3.0, 3.0, 0.0])

    assert greedy_decode([0], next_logits, 1) == [0, 1]


def test_zero_budget_does_not_call_model() -> None:
    initial = [1, 2]

    def next_logits(tokens: list[int]) -> np.ndarray:
        raise AssertionError("callback must not be called")

    result = greedy_decode(initial, next_logits, 0)

    assert result == initial
    assert result is not initial


def test_does_not_modify_prompt() -> None:
    initial = [4, 5]

    def next_logits(tokens: list[int]) -> np.ndarray:
        return np.array([2.0, 1.0])

    greedy_decode(initial, next_logits, 2)

    assert initial == [4, 5]


@pytest.mark.parametrize(
    ("initial", "budget", "eos"),
    [
        ([], 1, None),
        ([0, -1], 1, None),
        ([0, 1.5], 1, None),
        ([0], -1, None),
        ([0], 1.5, None),
        ([0], 1, -1),
    ],
)
def test_rejects_invalid_arguments(
    initial: list[object],
    budget: object,
    eos: object,
) -> None:
    with pytest.raises(ValueError):
        greedy_decode(  # type: ignore[arg-type]
            initial,
            lambda _: np.ones(2),
            budget,
            eos,
        )


@pytest.mark.parametrize(
    "bad_logits",
    [
        [1.0, 2.0],
        np.ones((1, 2)),
        np.array([], dtype=np.float64),
        np.array([1, 2]),
        np.array([1.0, np.nan]),
    ],
)
def test_rejects_invalid_callback_output(bad_logits: object) -> None:
    def next_logits(tokens: list[int]) -> object:
        return bad_logits

    with pytest.raises(ValueError):
        greedy_decode(  # type: ignore[arg-type]
            [0],
            next_logits,
            1,
        )
