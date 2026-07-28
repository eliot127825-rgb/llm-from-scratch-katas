# Kata 001: Greedy Decoding

## Goal

Implement deterministic autoregressive decoding:

```python
def greedy_decode(
    initial_tokens: list[int],
    next_logits: Callable[[list[int]], np.ndarray],
    max_new_tokens: int,
    eos_token_id: int | None = None,
) -> list[int]:
    ...
```

At each step:

1. call `next_logits` with the tokens generated so far;
2. select the smallest-index token among the maximum logits;
3. append that token;
4. stop after emitting `eos_token_id` or reaching `max_new_tokens`.

## Rules

Use Python control flow and `np.argmax`. Do not use a generation library,
beam search, or sampling.

## Required behaviour

- Return the prompt followed by newly generated tokens.
- Do not modify `initial_tokens`.
- Pass a token list containing all previously generated tokens to the callback.
- Require the callback to return a finite, non-empty, one-dimensional NumPy
  floating-point array.
- Reject invalid token IDs, arguments, or callback results with `ValueError`.
- Include an emitted EOS token in the returned sequence.
- Do not call the callback when `max_new_tokens == 0`.

## Complexity target

Ignoring model execution, for vocabulary size `V` and `S` generated steps:

- Time: `O(SV)`
- Additional output space: `O(S)`

## Run

```powershell
python -m pytest katas/06_generation/001_greedy_decoding -q
```

## Explain after coding

1. Why is greedy decoding deterministic?
2. What is its failure mode compared with beam search or sampling?
3. Why must every step receive the complete generated prefix?
4. Where would a KV cache change the computational cost?
