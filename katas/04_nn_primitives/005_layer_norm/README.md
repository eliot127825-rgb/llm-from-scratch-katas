# Kata 005: Layer Normalization

## Goal

Implement LayerNorm over the final feature dimension:

```python
def layer_norm(
    x: np.ndarray,
    gamma: np.ndarray,
    beta: np.ndarray,
    eps: float = 1e-5,
) -> np.ndarray:
    ...
```

For each final-dimension feature vector:

```text
mean = average(x)
variance = average((x - mean)^2)
normalized = (x - mean) / sqrt(variance + eps)
output = normalized * gamma + beta
```

Use the population variance, not the sample variance.

## Rules

Use basic NumPy reductions and elementwise operations. Do not use a library
normalization layer.

## Required behaviour

- Support input shape `(..., hidden_size)`.
- Require `gamma` and `beta` to have shape `(hidden_size,)`.
- Reject empty, non-floating, non-finite, or incompatible inputs.
- Require a finite positive `eps`.
- Do not modify inputs.

## Run

```powershell
python -m pytest katas/04_nn_primitives/005_layer_norm -q
```

## Explain after coding

1. Which axes are normalized and which are preserved?
2. Why use `keepdims=True` for the mean and variance?
3. What numerical problem does `eps` prevent?
