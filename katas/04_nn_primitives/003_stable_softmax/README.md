# Kata 003: Stable Softmax

## Goal

Implement numerically stable softmax:

```python
def stable_softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    ...
```

Formula:

```text
softmax(x_i) = exp(x_i - m) / sum_j exp(x_j - m)
m = max_j x_j
```

## Rules

Use NumPy reductions and elementwise operations. Do not use SciPy, PyTorch,
or another softmax implementation.

## Required behaviour

- Support positive and negative axis indices.
- Preserve the input shape.
- Produce probabilities that sum to one along `axis`.
- Reject non-array, rank-zero, empty, non-floating, non-finite, or invalid-axis
  input with `ValueError`.
- Do not modify the input.

## Run

```powershell
python -m pytest katas/04_nn_primitives/003_stable_softmax -q
```

## Explain after coding

1. Why is softmax unchanged after subtracting one value from every logit?
2. Why should the maximum retain its reduced dimension during subtraction?
3. What happens to probabilities when one logit is much larger than the rest?
