# Specs Index

This project supports multiple specs, each in its own subdirectory under `specs/`.

## Active Specs

| Spec | Directory | Status | Description |
|------|-----------|--------|-------------|
| taskrunner | `specs/taskrunner/` | active | Test project: Python CLI task runner |

## How Multi-Spec Works

Each spec lives in `specs/<name>/` and contains:
- `spec.md` — full project specification
- `tasks.md` — ordered task list with dependencies
- `progress.txt` — auto-updated progress log

### Invoking workflows on a specific spec

Pass the spec name when invoking workflows:

```
/spec-loop taskrunner
/implement-task taskrunner T3
/verify-all taskrunner
```

If only one spec exists, the spec name can be omitted.

### Adding a new spec

1. Create `specs/<name>/` directory
2. Run `/plan-spec <name>` to generate spec.md and tasks.md from requirements
3. Or copy from `specs/templates/` and fill in manually
4. Add an entry to this index

### Parallel spec execution

Independent specs can be implemented in parallel using worktree Cascades:
- Cascade #1 (worktree): `/spec-loop auth`
- Cascade #2 (worktree): `/spec-loop dashboard`
- Cascade #3 (worktree): `/spec-loop api`

Each runs its own loop on its own spec, fully isolated.
