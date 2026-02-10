---
description: Run all verification checks (tests + lint) and report results. Use when you want to run tests, check lint, verify the build, or confirm everything passes. Keywords: test, lint, verify, check, run tests, validate, coverage, spec, windloop.
---

## Verify All

Pass the spec name in your message (e.g. `/spec-verify taskrunner`).
If omitted, check `.windloop/index.md`. If only one active spec exists, use it.

Let SPEC be the resolved spec name.

1. Read `.windloop/SPEC/spec.md` to find the test and lint commands.

// turbo
2. Run the full test suite (e.g. `python -m pytest tests/ -v`).

3. If any tests fail, list the failures with file and line numbers.

// turbo
4. Run the lint check (e.g. `ruff check src/ tests/`).

5. If any lint errors, list them.

6. Summarize: total tests passed/failed, lint issues found, and overall status (PASS or FAIL).
