---
name: spec-driven-dev
description: Guides spec-driven autonomous development. Use when implementing features from a spec, breaking down requirements into tasks, or running the autonomous development loop.
---

## Spec-Driven Development

This project uses a spec-driven development workflow where:

1. **Specs** define the project requirements, architecture, and testing strategy (`specs/spec.md`)
2. **Tasks** break the spec into ordered, dependency-aware work items (`specs/tasks.md`)
3. **Progress** is tracked automatically (`specs/progress.txt`)

## Key Workflows

| Command | Purpose |
|---------|---------|
| `/plan-spec` | Generate spec + tasks from a project idea |
| `/spec-loop` | Autonomous loop: pick task → implement → test → commit → repeat |
| `/implement-task` | Implement a single task by ID (for parallel worktree use) |
| `/verify-all` | Run all tests + lint and report status |
| `/review-merge` | Review progress and validate after merges |

## Task Format

Each task in `specs/tasks.md` has:
- **ID**: T1, T2, etc.
- **Priority**: P0 (critical), P1 (important), P2 (nice-to-have)
- **Dependencies**: Which tasks must be done first
- **Acceptance criteria**: Checkable items that define "done"
- **Files**: Which files to create/modify
- **Verify**: Command to validate the task
- **Status**: `[ ]` pending, `[x]` done, `[!]` blocked

## Rules for Implementation

1. Always read the spec before starting any task
2. Check dependencies before implementing — never skip ahead
3. Run the task's verify command after implementation
4. Fix failures up to 3 times before marking BLOCKED
5. Commit after each successful task with a descriptive message
6. Update both `tasks.md` (status) and `progress.txt` (log entry)
7. Follow the tech stack and conventions defined in the spec
8. Keep changes minimal and focused on the current task

## Parallel Execution

For independent tasks (no shared dependencies), use worktree mode:
1. Open a new Cascade in Worktree mode
2. Run `/implement-task T[N]` for the specific task
3. After completion, merge the worktree back

Tasks are independent if they don't share the same `Files` and their dependency chains don't overlap.
