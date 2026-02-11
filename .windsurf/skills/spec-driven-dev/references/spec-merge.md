
## Merge Parallel Work

Pass the spec name in your message (e.g. `/spec-merge taskrunner`).
If omitted, check `.windloop/index.md`. If only one active spec exists, use it.

Let SPEC be the resolved spec name.

### 1. Discover branches to merge

// turbo
Run `git branch --list "task/*"` and `git worktree list` to find branches or worktrees created for parallel tasks.

List the candidates and ask the user which to merge (or merge all if they say so). If the user specified branches in their prompt, use those.

### 2. Merge each branch

For each branch to merge:

// turbo
a. `git merge <branch> --no-edit`

b. If there are **merge conflicts**:
   - Read the conflicting files (`git diff --name-only --diff-filter=U`)
   - For each conflict, read the file and resolve it intelligently:
     - If both sides added different tasks/tests, keep both
     - If both sides modified the same function, merge the intent
     - If unclear, show the conflict to the user and ask
   - After resolving: `git add <resolved-files> && git commit --no-edit`

c. If the merge was clean, report: "Merged `<branch>` cleanly."

### 3. Clean up merged branches

// turbo
For each successfully merged branch:
- `git branch -d <branch>` (delete local branch)
- If it was a worktree: `git worktree remove <path>` (ask user to confirm)

### 4. Verify after merge

a. Read `.windloop/SPEC/tasks.md` — count done vs remaining.

b. **File-tracking audit**: Collect all files from completed tasks' `Files` fields. Run `git ls-files <file>` for each. Report any untracked files as warnings.

// turbo
c. Run the test suite (from `.windloop/SPEC/design.md`).

// turbo
d. Run lint if configured.

e. If tests or lint fail, identify which merge introduced the issue and describe the fix.

### 5. Summarize

```
Merged: <branch-1>, <branch-2>, ...
Conflicts: none (or list resolved conflicts)
Tasks completed: [list with IDs and titles]
Tasks remaining: [list]
Test status: PASS/FAIL
Lint status: PASS/FAIL
Recommended next steps: ...
```

// turbo
6. Commit any post-merge fixes: `git add -A && git commit -m "chore(SPEC): post-merge fixes"`
