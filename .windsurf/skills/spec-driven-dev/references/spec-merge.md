
## Merge Parallel Work

Pass the spec name (e.g. `/spec-merge taskrunner`).
If omitted, use the **Spec Resolution** rules from SKILL.md.

Let SPEC be the resolved spec name and SPEC_DIR the resolved directory.

### 1. Discover branches to merge

// turbo
Run `git branch --list "task/*"` and `git worktree list` to find branches or worktrees created for parallel tasks.

List the candidates and ask the user which to merge (or merge all). If the user specified branches, use those.

### 2. Merge each branch

For each branch:

// turbo
a. `git merge <branch> --no-edit`

b. If there are **merge conflicts**:
   - Read conflicting files (`git diff --name-only --diff-filter=U`)
   - Resolve intelligently: keep both sides if they added different things, merge intent if same function, ask user if unclear
   - After resolving: `git add <resolved-files> && git commit --no-edit`

c. If clean: "Merged `<branch>` cleanly."

### 3. Clean up merged branches

// turbo
For each merged branch:
- `git branch -d <branch>`
- If worktree: `git worktree remove <path>` (ask user to confirm)

### 4. Verify after merge

a. Read `SPEC_DIR/tasks.md` — count done vs remaining.

b. Run `git status` to check for untracked or uncommitted files.

// turbo
c. Run the test suite (from `SPEC_DIR/design.md`).

// turbo
d. Run lint if configured.

e. If tests or lint fail, identify which merge introduced the issue.

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
