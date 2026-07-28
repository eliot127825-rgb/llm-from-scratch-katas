# Kata 002: Embedding Lookup

## Goal

Implement token embedding lookup:

```python
def embedding_lookup(
    weight: np.ndarray,
    token_ids: np.ndarray,
) -> np.ndarray:
    ...
```

Shapes:

```text
weight: (vocab_size, embedding_dim)
token_ids: (...)
output: (..., embedding_dim)
```

Each integer token ID selects one row from the embedding table.

## Rules

Use NumPy indexing. Do not use PyTorch, Keras, `np.take`, or an embedding
layer implementation.

## Required behaviour

- Support scalar-free token ID arrays of any positive rank.
- Require an integer token-ID dtype.
- Reject negative and out-of-vocabulary IDs instead of accepting NumPy's
  negative indexing behaviour.
- Return a copy that does not alias the embedding table.
- Reject empty dimensions with `ValueError`.

## Run

```powershell
python -m pytest katas/04_nn_primitives/002_embedding_lookup -q
```

## Explain after coding

1. Why does the output append `embedding_dim` to the token-ID shape?
2. Why must negative IDs be checked explicitly in NumPy?
3. How does an embedding lookup differ from multiplying by a one-hot vector?
