# Kata 005: Stable LogSumExp

## Goal

Implement a numerically stable reduction:

```python
def stable_logsumexp(
    x: np.ndarray,
    axis: int = -1,
    keepdims: bool = False,
) -> np.ndarray:
    ...
```

The mathematical operation is:

```text
logsumexp(x) = log(sum(exp(x)))
```

Use the shift identity:

```text
m + log(sum(exp(x - m)))
```

where `m` is the maximum along the reduction axis.

## Rules

Use NumPy reductions and elementwise operations. Do not use
`np.logaddexp.reduce`, SciPy, or another `logsumexp` implementation.

## Required behaviour

- Support positive and negative axis indices.
- Match NumPy reduction shape semantics for `keepdims`.
- Reject non-arrays, rank-zero inputs, invalid axes, and empty reduction axes
  with `ValueError`.
- Remain finite for large finite values such as `1000`.

## Run

```powershell
python -m pytest katas/02_tensor_ops/005_stable_logsumexp -q
```

## Explain after coding

1. Why does subtracting the maximum not change the final result?
2. Which intermediate value would overflow in the naive implementation?
3. How is this operation related to softmax and cross entropy?
