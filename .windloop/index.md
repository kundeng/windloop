# Specs Index

This project supports multiple specs, each in its own subdirectory under `.windloop/`.

## Active Specs

| Spec | Directory | Status | Description |
|------|-----------|--------|-------------|
| taskrunner | `.windloop/taskrunner/` | active | Test project: Python CLI task runner |

## How Multi-Spec Works

Each spec lives in `.windloop/<name>/` and contains:
- `spec.md` — full project specification
- `tasks.md` — ordered task list with dependencies
- `progress.txt` — auto-updated progress log

Cross-spec dependencies are declared in `.windloop/dependencies.md`.

### Invoking workflows on a specific spec

Pass the spec name when invoking workflows:

```
/spec-loop taskrunner
/spec-task taskrunner T3
/spec-verify taskrunner
```

If only one spec exists, the spec name can be omitted.

### Adding a new spec

1. Run `/spec-plan <name>` to generate spec.md and tasks.md from requirements
2. Or create `.windloop/<name>/` manually from `.windloop/templates/`
3. Add an entry to this index
4. If it depends on other specs, add to `.windloop/dependencies.md`

### Parallel spec execution

Independent specs can be implemented in parallel using worktree Cascades:
- Cascade #1 (worktree): `/spec-loop auth`
- Cascade #2 (worktree): `/spec-loop dashboard`
- Cascade #3 (worktree): `/spec-loop api`

Each runs its own loop on its own spec, fully isolated.
