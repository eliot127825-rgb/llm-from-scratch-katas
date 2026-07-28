# Kata 004: Causal Attention Mask

## Goal

Create the boolean mask used by autoregressive self-attention.

```python
def causal_mask(sequence_length: int) -> np.ndarray:
    ...
```

Return shape `(T, T)`. A `True` entry means the query may attend to that
key position:

```text
mask[i, j] = (j <= i)
```

## Rules

Use NumPy. Do not call `np.tril` or copy a precomputed mask.

## Required behaviour

- Return an array with `dtype == np.bool_`.
- Include the diagonal.
- Reject booleans, non-integers, zero, and negative lengths with `ValueError`.
- Allocate an independent array on every call.

## Complexity target

- Time: `O(T^2)`
- Output space: `O(T^2)`

## Run

```powershell
python -m pytest katas/02_tensor_ops/004_causal_mask -q
```

## Explain after coding

1. Why is the diagonal allowed?
2. Which triangle prevents information leakage from future tokens?
3. How would this `(T, T)` mask broadcast over batch and head dimensions?
