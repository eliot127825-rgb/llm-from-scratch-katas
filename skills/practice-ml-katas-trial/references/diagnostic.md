# Learner Diagnostic

Use this diagnostic when no local learner profile exists, when the learner asks for a
level check, or after meaningful progress. Explain that it takes about five minutes
and adjusts support rather than judging intelligence.

## Administration

- Ask one question at a time in the learner's language.
- Do not require code execution or file edits.
- Accept plain-language answers.
- Do not reveal the rubric or correct answer until all five responses are collected.
- Score each dimension from 0 to 2.
- Store only dimension scores and short strengths/support notes. Do not store raw
  answers.

## Questions and scoring

### 1. Python basics

Ask for the printed result and a brief explanation:

```python
counts = {}
for label in [1, 2, 1]:
    counts[label] = counts.get(label, 0) + 1
print(counts)
```

- 2: gives `{1: 2, 2: 1}` and explains keys/counts or the update.
- 1: mostly correct output or reasoning with a small mistake.
- 0: cannot trace the loop yet.

### 2. Debugging

Ask what goes wrong and how to fix it:

```python
values = [10, 20, 30]
for i in range(len(values) + 1):
    print(values[i])
```

- 2: identifies the out-of-range final index and uses `range(len(values))`.
- 1: recognizes one extra iteration or an index problem without a precise fix.
- 0: cannot locate the problem yet.

### 3. Shape reasoning

Ask: matrix `A` has shape `(2, 3)` and `B` has shape `(3, 4)`. What is the shape of
`A @ B`, and why?

- 2: answers `(2, 4)` and explains matching inner dimensions.
- 1: answers `(2, 4)` without a reason or gives sound partial reasoning.
- 0: cannot determine the output shape yet.

### 4. Machine-learning concepts

Ask: why do we keep a test set separate from the training set?

- 2: explains evaluation on unseen data, generalization, or avoiding leakage.
- 1: says it checks model quality but cannot explain why separation matters.
- 0: does not yet distinguish training and testing.

### 5. Algorithm expression

Ask: without writing code, describe the steps for counting how many times each label
appears in a list.

- 2: describes an initially empty count mapping, one pass, and incrementing each label.
- 1: has the right overall idea but misses initialization or updating.
- 0: cannot yet break the task into steps.

## Levels

| Score | Level | Preferred difficulty | Teaching approach |
|---:|---|---|---|
| 0–2 | Starter | Beginner | Define every term, use concrete values, one action at a time, offer syntax scaffolds |
| 3–5 | Foundation | Beginner, Easy | Trace loops and values, briefly explain syntax, use frequent prediction checks |
| 6–8 | Guided | Easy, Medium | Ask for pseudocode first, focus on shapes and edge cases, give hints on request |
| 9–10 | Independent | Medium | Use concise problem statements, withhold hints initially, review complexity and tradeoffs |

Describe the result as a starting support mode. Allow the learner to choose an easier
or harder exercise regardless of the score.

## Save the result

After explaining the result, save it locally:

```powershell
python scripts/learner_profile.py save `
  --root <course-root> `
  --python-basics <0-2> `
  --debugging <0-2> `
  --shape-reasoning <0-2> `
  --ml-concepts <0-2> `
  --algorithm-expression <0-2> `
  --strength "<short evidence-based strength>" `
  --support "<short evidence-based support need>"
```

Tell the learner that the profile is stored in `.local/learner_profile.json`, ignored
by Git, and contains no raw answers.

## Reassessment

Offer reassessment after five completed katas, after repeated independent success, or
when the learner asks. Do not downgrade a learner because of one difficult exercise.
