# Kata 001: Linear Layer Forward Pass

## Goal

Implement the forward pass of a linear layer:

```python
def linear_forward(
    x: np.ndarray,
    weight: np.ndarray,
    bias: np.ndarray | None = None,
) -> np.ndarray:
    ...
```

Shapes:

```text
x: (..., in_features)
weight: (out_features, in_features)
bias: (out_features,) or None
output: (..., out_features)
```

Formula:

```text
y = x W^T + b
```

## Rules

Use NumPy array operations. Do not use PyTorch, Keras, or a library linear
layer. Do not change any input array.

## Required behaviour

- Support both `(B, D)` and higher-rank inputs such as `(B, T, D)`.
- Validate all feature dimensions and the optional bias shape.
- Reject zero-sized dimensions and non-array inputs with `ValueError`.
- Preserve the natural NumPy result dtype.

## Run

```powershell
python -m pytest katas/04_nn_primitives/001_linear_forward -q
```

## Explain after coding

1. Why is the stored weight shape `(out_features, in_features)`?
2. Which dimensions of `x` are preserved?
3. How is the bias broadcast across batch and sequence dimensions?
