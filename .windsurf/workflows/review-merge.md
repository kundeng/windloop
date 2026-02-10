---
description: Review completed work and merge worktree changes. Use after parallel worktree Cascades finish their tasks.
---

## Review and Merge

Pass the spec name in your message (e.g. `/review-merge taskrunner`).
If omitted, check `specs/index.md`. If only one active spec exists, use it.

Let SPEC be the resolved spec name.

1. Read `specs/SPEC/progress.txt` to see what tasks were completed.

2. Read `specs/SPEC/tasks.md` to check overall progress — count done vs remaining.

3. If `.windsurf/mailbox/outbox/` has completion signals, read them to see which parallel sessions finished.

// turbo
4. Run the full test suite (from `specs/SPEC/spec.md`) to confirm everything still passes after merges.

// turbo
5. Run lint to confirm no issues.

6. If tests or lint fail, identify which task introduced the issue and describe the fix needed.

7. Summarize:
   - Tasks completed: [list]
   - Tasks remaining: [list]
   - Test status: PASS/FAIL
   - Lint status: PASS/FAIL
   - Mailbox signals: [any pending messages]
   - Recommended next steps
