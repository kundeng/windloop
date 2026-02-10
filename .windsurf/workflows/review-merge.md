---
description: Review completed work and merge worktree changes. Use after parallel worktree Cascades finish their tasks.
---

## Review and Merge

1. Read `specs/progress.txt` to see what tasks were completed.

2. Read `specs/tasks.md` to check overall progress — count done vs remaining.

// turbo
3. Run the full test suite to confirm everything still passes after merges.

// turbo
4. Run lint to confirm no issues.

5. If tests or lint fail, identify which task introduced the issue and describe the fix needed.

6. Summarize:
   - Tasks completed: [list]
   - Tasks remaining: [list]
   - Test status: PASS/FAIL
   - Lint status: PASS/FAIL
   - Recommended next steps
