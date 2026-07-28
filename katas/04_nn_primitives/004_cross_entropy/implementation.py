"""Multiclass cross-entropy loss computed directly from logits."""

import numpy as np


def cross_entropy(
    logits: np.ndarray,
    targets: np.ndarray,
    reduction: str = "mean",
    ignore_index: int | None = None,
) -> np.ndarray:
    """Return stable per-row or reduced cross-entropy loss."""

    raise NotImplementedError
