"""Token embedding lookup using a NumPy table."""

import numpy as np


def embedding_lookup(
    weight: np.ndarray,
    token_ids: np.ndarray,
) -> np.ndarray:
    """Select embedding rows for every integer token ID."""

    raise NotImplementedError
