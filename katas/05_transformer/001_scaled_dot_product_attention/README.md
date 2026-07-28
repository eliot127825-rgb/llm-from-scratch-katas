# Kata 001: Scaled Dot-Product Attention

## Goal

Implement a single-head, batched attention operation:

```python
def scaled_dot_product_attention(
    query: np.ndarray,
    key: np.ndarray,
    value: np.ndarray,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    ...
```

Shapes:

```text
query:   (B, T_query, D_key)
key:     (B, T_key, D_key)
value:   (B, T_key, D_value)
mask:    broadcastable to (B, T_query, T_key), True means allowed
output:  (B, T_query, D_value)
weights: (B, T_query, T_key)
```

Formula:

```text
scores = query @ key^T / sqrt(D_key)
weights = softmax(mask(scores))
output = weights @ value
```

## Rules

Use NumPy operations and your own stable softmax logic. Do not call an
attention or softmax library implementation.

## Required behaviour

- Validate ranks, batch sizes, feature sizes, sequence lengths, and dtypes.
- Accept only boolean masks that broadcast to the score shape.
- Treat `True` as attendable and `False` as blocked.
- Reject a query row with no attendable keys.
- Produce zero probability at every masked position.
- Keep weights finite and normalized along the key axis.
- Do not modify any input.

## Complexity target

For `T_query = T_key = T` and `D_key = D_value = D`:

- Time: `O(BT^2D)`
- Attention-matrix space: `O(BT^2)`

## Run

```powershell
python -m pytest katas/05_transformer/001_scaled_dot_product_attention -q
```

## Explain after coding

1. Why divide scores by `sqrt(D_key)`?
2. Why does softmax operate over the key axis?
3. Why must masking happen before softmax?
4. Which tensor becomes the quadratic memory bottleneck?
