"""RMS normalization over the final feature dimension."""

import numpy as np


def rms_norm(
    x: np.ndarray,
    weight: np.ndarray,
    eps: float = 1e-6,
) -> np.ndarray:
    """Scale final-axis vectors by their root mean square."""

    raise NotImplementedError
