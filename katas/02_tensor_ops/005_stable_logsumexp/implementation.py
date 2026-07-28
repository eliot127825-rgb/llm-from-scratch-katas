"""Numerically stable LogSumExp."""

import numpy as np


def stable_logsumexp(
    x: np.ndarray,
    axis: int = -1,
    keepdims: bool = False,
) -> np.ndarray:
    """Reduce ``x`` with LogSumExp along one axis."""

    raise NotImplementedError
