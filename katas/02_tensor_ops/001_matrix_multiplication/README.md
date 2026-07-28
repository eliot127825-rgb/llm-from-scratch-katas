# Kata 001: Matrix Multiplication from Scratch

## Why this is the first task

Matrix multiplication is the core operation behind:

- linear layers;
- attention scores, `Q @ K.T`;
- weighted value aggregation, `P @ V`;
- feed-forward networks;
- most large-model training workloads.

This kata also practices Python loops, indexing, shape reasoning, input validation, and complexity analysis.

## Goal

Implement two-dimensional matrix multiplication without using an existing matrix-multiplication operation.

Complete this function:

```python
def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    ...
```

Given:

```text
A has shape (M, K)
B has shape (K, N)
```

return:

```text
C has shape (M, N)
```

where:

```text
C[i][j] = sum(A[i][k] * B[k][j] for k in range(K))
```

## Example

```python
a = [
    [1, 2, 3],
    [4, 5, 6],
]

b = [
    [7, 8],
    [9, 10],
    [11, 12],
]

matrix_multiply(a, b)
```

Expected result:

```python
[
    [58, 64],
    [139, 154],
]
```

Shape reasoning:

```text
(2, 3) @ (3, 2) -> (2, 2)
```

## Rules

You may use:

- Python lists;
- `for` loops;
- `len`;
- arithmetic operations;
- helper functions that you write yourself.

Do not use:

- NumPy;
- PyTorch;
- `@`;
- `numpy.matmul`;
- `numpy.dot`;
- any library matrix-multiplication function.

## Required behaviour

Your implementation must:

1. compute valid matrix products correctly;
2. support integers and floating-point values;
3. reject empty matrices;
4. reject ragged matrices such as `[[1, 2], [3]]`;
5. reject incompatible shapes;
6. avoid modifying either input matrix.

Use `ValueError` for invalid matrices or incompatible shapes.

## Complexity target

For shapes `(M, K)` and `(K, N)`:

- time: `O(MKN)`;
- output space: `O(MN)`.

## How to work

1. Read the formula above.
2. Write the three required loops on paper.
3. Implement `matrix_multiply` in `implementation.py`.
4. Run the tests.
5. Fix one failing case at a time.
6. Record real mistakes in `mistakes.md`.

Run only this kata:

```powershell
python -m pytest katas/02_tensor_ops/001_matrix_multiplication -q
```

## Questions to answer after coding

1. Why must the two inner dimensions be equal?
2. Which loop corresponds to `M`, `K`, and `N`?
3. What shape does the result have?
4. Why is the time complexity `O(MKN)`?
5. How is this operation used inside self-attention?

## Optional extension

After passing all tests, implement a second version that transposes `b` first. Compare whether its indexing is easier to understand and explain why it may have better memory locality.
