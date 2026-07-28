# Kata 006: RMS Normalization

## Goal

Implement RMSNorm over the final feature dimension:

```python
def rms_norm(
    x: np.ndarray,
    weight: np.ndarray,
    eps: float = 1e-6,
) -> np.ndarray:
    ...
```

Formula:

```text
rms = sqrt(mean(x^2) + eps)
output = (x / rms) * weight
```

Unlike LayerNorm, RMSNorm does not subtract the mean.

## Rules

Use basic NumPy reductions and elementwise operations. Do not use a library
normalization layer.

## Required behaviour

- Support input shape `(..., hidden_size)`.
- Require `weight` shape `(hidden_size,)`.
- Reject empty, non-floating, non-finite, or incompatible inputs.
- Require a finite positive `eps`.
- Do not modify inputs.

## Run

```powershell
python -m pytest katas/04_nn_primitives/006_rms_norm -q
```

## Explain after coding

1. How does RMSNorm differ mathematically from LayerNorm?
2. Why does `weight` broadcast across the leading dimensions?
3. What happens for an all-zero feature vector?
