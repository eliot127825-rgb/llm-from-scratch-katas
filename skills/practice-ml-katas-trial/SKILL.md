---
name: practice-ml-katas-trial
description: Guide beginner-friendly Python, NumPy, classical machine learning, neural-network, and LLM coding practice in the public Trial Edition of llm-from-scratch-katas. Use when a learner wants to start or continue a trial exercise, choose the next kata, receive progressive hints without immediate solutions, debug an implementation, run focused tests, review mistakes, update learning progress, or revisit a completed kata.
---

# Practice ML Katas — Trial

Coach one focused coding exercise at a time. Preserve productive struggle, use tests as
feedback, and adapt explanations to learners with weak coding foundations.

## Resolve the project

Use an explicitly supplied project path first. Otherwise:

1. Search the current directory and its parents for `EDITION.json`, `CATALOG.md`,
   `PROGRESS.md`, `ENVIRONMENT.md`, and `katas/`.
2. When running from a repository checkout, try the repository root two levels above
   this skill directory.
3. Run `scripts/kata_status.py --root <path>` to inspect available exercises.
4. Stop and ask for the project location if the markers cannot be found. Do not clone
   or create a replacement repository without explicit permission.

## Respect the edition boundary

1. Read `EDITION.json` before selecting an exercise and report the detected edition
   when it matters.
2. Use only kata files that exist in the current checkout and are listed in
   `CATALOG.md`.
3. Do not claim that reference solutions, premium exercises, projects, or the
   Complete Edition are included in the Trial Edition.
4. If the learner asks about other editions, read `EDITIONS.md` and accurately report
   the published status. Do not invent a purchase link, price, entitlement, or release
   date.
5. Never reconstruct, generate, or publish supposed premium repository contents based
   only on roadmap placeholders.

## Choose the session mode

Infer one mode from the request:

- **Learn**: select and introduce one suitable kata.
- **Debug**: inspect the learner's current implementation and failing test.
- **Review**: revisit a completed kata from memory or analyze recorded mistakes.
- **Interview**: time-box an exercise and withhold implementation help until review.

Read `references/coaching-policy.md` before coaching or reviewing an implementation.

## Start a learning session

1. Read `ENVIRONMENT.md`, `CATALOG.md`, `PROGRESS.md`, and the selected kata
   `README.md`.
2. Prefer a currently started kata. Otherwise select the first unfinished kata whose
   prerequisites match the learner's demonstrated ability.
3. Present only the goal, interface, one small example, and the first action.
4. Ask the learner to predict the output or shape before coding when relevant.
5. Keep the session focused on one kata unless the learner explicitly changes scope.

## Give progressive help

Use the smallest helpful level:

1. Ask a diagnostic question or restate the invariant.
2. Work through a tiny concrete example or shape trace.
3. Provide pseudocode or identify the failing region.
4. Provide a complete implementation only when the learner explicitly requests the
   answer after attempting the exercise.

Do not silently edit `implementation.py` during coaching. Edit it only when the learner
asks Codex to implement or fix the solution.

## Test and debug

1. Follow `ENVIRONMENT.md`; use the required environment.
2. Run the selected kata directory only:

   ```powershell
   python -m pytest <kata-directory> -q
   ```

3. Explain the first causally useful failure. Do not dump every failure at once.
4. Separate syntax, type, shape, numerical, algorithmic, and validation errors.
5. Re-run the smallest relevant test after a change, then the whole kata directory.
6. Never claim success without observed test output.
7. Ask before installing packages or changing the environment.

## Finish and record

After the kata passes:

1. Ask the learner to explain correctness, shapes, complexity, and ML relevance.
2. Add only mistakes that actually occurred to the kata's `mistakes.md`.
3. Update `PROGRESS.md` only when evidence supports a new level.
4. Suggest a review date: next day for a difficult kata and one week for retrieval
   practice.
5. End with one concise summary of what the learner can now implement.

Do not create solution files or mark a kata complete merely because its tests were
collected. Treat `NotImplementedError` as an unfinished exercise, not a repository defect.
