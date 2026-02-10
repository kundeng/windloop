---
description: Run all verification checks (tests + lint) and report results. Use after implementing tasks to confirm everything passes.
---

## Verify All

Pass the spec name in your message (e.g. `/verify-all taskrunner`).
If omitted, check `specs/index.md`. If only one active spec exists, use it.

Let SPEC be the resolved spec name.

1. Read `specs/SPEC/spec.md` to find the test and lint commands.

// turbo
2. Run the full test suite (e.g. `python -m pytest tests/ -v`).

3. If any tests fail, list the failures with file and line numbers.

// turbo
4. Run the lint check (e.g. `ruff check src/ tests/`).

5. If any lint errors, list them.

6. Summarize: total tests passed/failed, lint issues found, and overall status (PASS or FAIL).
