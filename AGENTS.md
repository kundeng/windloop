# Windloop Agent Instructions

## Project Overview
This is a spec-driven autonomous development framework for Windsurf. It uses workflows, skills, and hooks to enable near-intervention-free cascaded agent loops.

## Development Workflow
1. Specs live in `specs/` — always read `specs/spec.md` and `specs/tasks.md` before implementing anything
2. Use `/spec-loop` for autonomous task-by-task implementation
3. Use `/implement-task` with a task ID for single-task execution (ideal for parallel worktrees)
4. Use `/verify-all` to run the full test + lint suite
5. Use `/plan-spec` to bootstrap a new project from requirements

## Conventions
- Always check task dependencies before starting implementation
- Run the task's verification command after every implementation
- Commit after each completed task with message format: `feat(T[N]): [description]`
- Update both `specs/tasks.md` (status checkbox) and `specs/progress.txt` (log line) after each task
- Keep changes minimal and focused — one task per commit
- Follow the tech stack and patterns defined in `specs/spec.md`

## File Structure
```
specs/                    # Project specifications and progress
  spec.md                 # Full project specification
  tasks.md                # Ordered task list with dependencies
  progress.txt            # Auto-updated progress log
  templates/              # Reusable templates for new projects
.windsurf/
  workflows/              # Cascade workflow definitions
  skills/                 # Cascade skill bundles
  hooks.json              # Lifecycle hook configuration
  hooks/                  # Hook scripts
hooks/                    # Worktree setup scripts
```

## Testing
- Run tests: check `specs/spec.md` for the exact command (typically `python -m pytest tests/ -v`)
- Run lint: check `specs/spec.md` for the lint command (typically `ruff check src/ tests/`)
- Never skip verification after implementation
