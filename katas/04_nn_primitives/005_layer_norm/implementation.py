"""Layer normalization over the final feature dimension."""

import numpy as np


def layer_norm(
    x: np.ndarray,
    gamma: np.ndarray,
    beta: np.ndarray,
    eps: float = 1e-5,
) -> np.ndarray:
    """Normalize the last axis and apply an affine transformation."""

    raise NotImplementedError
