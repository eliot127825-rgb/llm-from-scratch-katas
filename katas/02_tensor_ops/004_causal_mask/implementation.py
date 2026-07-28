"""Build a boolean causal self-attention mask."""

import numpy as np


def causal_mask(sequence_length: int) -> np.ndarray:
    """Return a (T, T) boolean mask whose True entries are attendable."""

    raise NotImplementedError
