"""Deterministic autoregressive greedy decoding."""

from collections.abc import Callable

import numpy as np


def greedy_decode(
    initial_tokens: list[int],
    next_logits: Callable[[list[int]], np.ndarray],
    max_new_tokens: int,
    eos_token_id: int | None = None,
) -> list[int]:
    """Append maximum-logit tokens until the budget or EOS is reached."""

    raise NotImplementedError
