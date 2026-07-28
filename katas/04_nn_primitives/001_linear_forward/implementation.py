"""Forward pass for a fully connected linear layer."""

import numpy as np


def linear_forward(
    x: np.ndarray,
    weight: np.ndarray,
    bias: np.ndarray | None = None,
) -> np.ndarray:
    """Return ``x W^T + b`` with features stored on the last axis."""

    raise NotImplementedError
