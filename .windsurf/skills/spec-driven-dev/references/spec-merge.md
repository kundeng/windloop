
## Review and Merge

Pass the spec name in your message (e.g. `/spec-merge taskrunner`).
If omitted, check `.windloop/index.md`. If only one active spec exists, use it.

Let SPEC be the resolved spec name.

1. Read `.windloop/SPEC/progress.txt` to see what tasks were completed.

2. Read `.windloop/SPEC/tasks.md` to check overall progress — count done vs remaining.

3. **File-tracking audit**: Read `.windloop/SPEC/tasks.md` and collect all files from every completed task's `Files` field. For each file, run `git ls-files <file>` to confirm it is tracked. Report any untracked/gitignored source files as a warning — these indicate commits that silently excluded source code.

// turbo
4. Run the full test suite (from `.windloop/SPEC/design.md`) to confirm everything still passes after merges.

// turbo
5. Run lint to confirm no issues.

6. If tests or lint fail, identify which task introduced the issue and describe the fix needed.

7. Summarize:
   - Tasks completed: [list]
   - Tasks remaining: [list]
   - Test status: PASS/FAIL
   - Lint status: PASS/FAIL
   - Recommended next steps
