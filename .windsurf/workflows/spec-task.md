---
description: Implement a single task from .windloop/<name>/tasks.md by ID. Use for parallel worktree execution or when you want to work on a specific task, pick a task, or implement one item. Keywords: task, implement, specific, single, parallel, worktree, pick, work on, spec, windloop.
---

## Implement a Single Task

Specify the spec name and task ID in your message (e.g. `/spec-task taskrunner T3`).
If only one spec exists in `.windloop/index.md`, the spec name can be omitted (e.g. `/spec-task T3`).

Let SPEC be the resolved spec name.

1. Read `.windloop/SPEC/spec.md` to understand the requirements and scope.

2. Read `.windloop/SPEC/design.md` to understand architecture, tech stack, testing strategy, and property tests.

3. Read `.windloop/SPEC/tasks.md` and locate the specified task by ID.

4. Verify that all dependencies for this task are satisfied (`[x]` or `[~]`). If not, report which dependencies are missing and STOP.

5. If `.windsurf/mailbox/board/claims.json` exists, check that this task is not already claimed by another session. If unclaimed, write your claim (use your trajectory ID or session name as the claimant).

6. Read any existing source files that this task depends on or modifies to understand the current state.

7. Implement the task (test-first):
   - **Write tests first**: if the task has a `Tests` field, implement those property tests before production code
   - Then write the production code to make the tests pass
   - For E2E test tasks (no production code): implement the test, run it, verify it passes
   - Create or modify only the files listed in the task's `Files` field
   - Add type hints where required
   - Follow existing code patterns and conventions

8. Run the task's verification command (from the `Verify` field).

9. If verification fails, analyze and fix. Retry up to 3 times.

// turbo
10. Run lint if configured: check `.windloop/SPEC/design.md` for the lint command.

11. Update `.windloop/SPEC/tasks.md`: mark the task status as `[x]` and check off acceptance criteria.

// turbo
12. Commit: `git add -A && git commit -m "feat(SPEC/[TASK_ID]): [description]"`

13. **Post-commit tracking guard**: For each file listed in the task's `Files` field, run `git ls-files <file>` to confirm it is tracked. If any file is missing from git (likely gitignored), run `git add -f <file>` for each untracked file, then `git commit --amend --no-edit` to include them. Report a warning: "File <file> was gitignored — force-added to commit."

14. Update `.windloop/SPEC/progress.txt`:
    - Append: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [description]`
    - Update the `# SUMMARY:` line to reflect current counts and next task.

15. If using the mailbox protocol, write a completion signal to `.windsurf/mailbox/outbox/<session>/done-[TASK_ID].json`.

16. Report completion and list any issues encountered.
