# Kata 003: Batched Matrix Multiplication

## Goal

Implement matrix multiplication for a batch of matrix pairs.

```python
def batched_matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    ...
```

Shapes:

```text
a: (B, M, K)
b: (B, K, N)
out: (B, M, N)
```

Formula:

```text
out[batch, i, j] =
    sum(a[batch, i, k] * b[batch, k, j] for k in range(K))
```

## Rules

Use NumPy arrays, indexing, loops, allocation, and elementwise arithmetic.
Do not use `@`, `np.matmul`, `np.dot`, or `np.einsum`.
Do not broadcast the batch dimension: both inputs must have the same `B`.

## Required behaviour

- Validate rank, batch size, and inner dimensions.
- Reject zero-sized dimensions with `ValueError`.
- Preserve a NumPy-compatible result dtype.
- Do not modify either input.

## Complexity target

- Time: `O(BMKN)`
- Output space: `O(BMN)`

## Run

```powershell
python -m pytest katas/02_tensor_ops/003_batched_matrix_multiplication -q
```

## Explain after coding

1. Which dimensions are multiplied and which are preserved?
2. How does this operation appear in multi-head attention?
3. What would change if batch broadcasting were allowed?
