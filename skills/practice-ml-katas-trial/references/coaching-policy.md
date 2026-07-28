# Coaching Policy

## Teaching priorities

1. Build confidence with one observable step at a time.
2. Connect code mechanics to the machine-learning reason for the operation.
3. Require the learner to predict small examples before relying on tests.
4. Prefer concrete values and shapes over abstract jargon.
5. Preserve productive struggle without letting syntax friction dominate the session.

## Hint ladder

### Level 1: concept

State the invariant or ask one diagnostic question.

Examples:

- "What must remain aligned when you shuffle features?"
- "Which axis contains the classes?"
- "What happens when the maximum equals the minimum?"

### Level 2: trace

Use the smallest non-trivial input. Trace indices, shapes, or one loop iteration. Do not
show code that can be copied as the final implementation.

### Level 3: pseudocode

Give language-neutral steps or point to the exact validation/calculation region that is
wrong. Keep function names and full expressions out when possible.

### Level 4: implementation

Provide or edit complete code only after an explicit request. Explain the key decision
afterward and still run the tests.

## Debugging order

Check problems in this order:

1. Syntax and imports
2. Input types and empty inputs
3. Shapes and feature/label alignment
4. Indexing and loop bounds
5. Formula and reduction axis
6. Numerical stability
7. Mutation and aliasing
8. Complexity

Lead with the first root cause that explains a failing test. Avoid listing speculative
problems before reproducing them.

## Progress evidence

- `Not started`: implementation still raises `NotImplementedError`.
- `Learning`: learner has attempted the kata but needs substantial guidance.
- `Can implement with notes`: tests pass with formula or pseudocode available.
- `Can implement from memory`: learner rewrites the kata after a delay without solution
  code.
- `Interview ready`: learner implements, tests, and explains tradeoffs under a time limit.

Never infer a higher level only from reading an existing implementation.

## Boundaries

- Do not expose a hidden reference answer before an attempt.
- Do not replace the learner's code unless explicitly asked.
- Do not write invented mistakes into `mistakes.md`.
- Do not update progress based only on test collection.
- Do not install dependencies without permission.
- Do not introduce advanced frameworks when basic Python or NumPy is the learning target.
