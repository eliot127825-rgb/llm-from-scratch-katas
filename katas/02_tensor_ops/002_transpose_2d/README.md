# Kata 002: Transpose a 2D Matrix

## Goal

Implement a two-dimensional matrix transpose using Python lists.

```python
def transpose_2d(matrix: list[list[float]]) -> list[list[float]]:
    ...
```

For an input with shape `(M, N)`, return a new matrix with shape `(N, M)`:

```text
output[j][i] = input[i][j]
```

## Rules

You may use Python lists, loops, `len`, and helper functions you write.
Do not use NumPy, PyTorch, `zip`, or a library transpose operation.

## Required behaviour

- Support square and rectangular matrices.
- Reject empty matrices, empty rows, and ragged rows with `ValueError`.
- Do not modify or reuse row objects from the input.

## Complexity target

- Time: `O(MN)`
- Output space: `O(MN)`

## Run

```powershell
python -m pytest katas/02_tensor_ops/002_transpose_2d -q
```

## Explain after coding

1. Why does `(M, N)` become `(N, M)`?
2. Which input coordinate supplies `output[j][i]`?
3. Why must a rectangular-matrix check happen before indexing?
