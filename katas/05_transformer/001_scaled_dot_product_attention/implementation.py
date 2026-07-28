"""Batched single-head scaled dot-product attention."""

import numpy as np


def scaled_dot_product_attention(
    query: np.ndarray,
    key: np.ndarray,
    value: np.ndarray,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Return attention output and normalized attention weights."""

    raise NotImplementedError
