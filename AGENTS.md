# Windloop Agent Instructions

## About This Repo
This is the windloop framework itself — a spec-driven autonomous development toolkit for Windsurf. The `.windsurf/` directory is the distributable artifact that users copy into their projects.

## For Development on Windloop Itself
- The framework code lives in `.windsurf/` (workflows, skills, hooks, mailbox)
- `README.md` is the user-facing documentation

## Windloop (Spec-Driven Development)

This project uses windloop for spec-driven autonomous development.

- Specs live in `.windloop/<name>/` — read `.windloop/index.md` for the registry
- Run `/spec-help` for available commands
- Run `/spec-plan <name>` to create or refine a spec
- Run `/spec-loop <name>` for autonomous implementation
- Run `/spec-status` to check progress across all specs
- Commit format: `feat(<spec>/T[N]): [description]`
