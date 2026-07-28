# Kata 004: Cross-Entropy Loss

## Goal

Implement multiclass cross entropy from logits:

```python
def cross_entropy(
    logits: np.ndarray,
    targets: np.ndarray,
    reduction: str = "mean",
    ignore_index: int | None = None,
) -> np.ndarray:
    ...
```

Shapes:

```text
logits: (batch_size, num_classes)
targets: (batch_size,)
```

For each non-ignored sample:

```text
loss_i = logsumexp(logits_i) - logits_i[target_i]
```

## Rules

Use NumPy reductions and indexing. Do not call a cross-entropy, softmax, or
LogSumExp library implementation. Compute the loss directly from logits.

## Required behaviour

- Support `reduction` values `"none"`, `"sum"`, and `"mean"`.
- Under `"none"`, give ignored rows loss zero.
- Under `"mean"`, divide by the number of non-ignored rows.
- Reject invalid shapes, dtypes, targets, reductions, and non-finite logits.
- Reject `"mean"` when every row is ignored.

## Run

```powershell
python -m pytest katas/04_nn_primitives/004_cross_entropy -q
```

## Explain after coding

1. Why should softmax not be materialized before taking a logarithm?
2. Which dimension represents classes?
3. Why must ignored rows be excluded from the mean denominator?
