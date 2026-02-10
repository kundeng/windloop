---
description: Show onboarding help, available commands, and how to get started with windloop. Use when you need help, want to see commands, or are new to the project. Keywords: help, commands, getting started, onboarding, how to, what can, windloop.
---

## Windloop Help

Print the following guide:

---

### Windloop — Spec-Driven Autonomous Development

**Lifecycle**: idea → `spec.md` → `design.md` (with property tests) → `tasks.md` → autonomous implementation loop

**Available commands** (all accept an optional `<spec>` name):

| Command | Purpose |
|---------|---------|
| `/spec-help` | Show this help guide |
| `/spec-plan <name> [create\|refine\|update]` | Create, refine, or update a spec (auto-detected if omitted) |
| `/spec-loop <name>` | Autonomous loop: pick task → implement → test → commit → repeat |
| `/spec-task <name> T[N]` | Implement a single task by ID (for parallel worktree use) |
| `/spec-verify <name>` | Run all tests + lint and report status |
| `/spec-merge <name>` | Review completed work and merge worktree changes |
| `/spec-status` | Dashboard: show progress across all specs and sessions |
| `/spec-reset <name>` | Reset a spec: clear progress, uncheck tasks, clear claims |

> If only one spec exists, the `<name>` can be omitted.

### Quick Start

1. **New spec?** → `/spec-plan myfeature` — describe your idea, get spec + design + tasks
2. **Ready to build?** → `/spec-loop myfeature` — autonomous implementation loop
3. **Parallel work?** → Open **worktree** Cascades, each runs `/spec-task myfeature T[N]`
4. **Check progress?** → `/spec-status`

> **Important**: Never run multiple Cascade sessions on the same branch. Use Windsurf's **Worktree Mode** (toggle in Cascade input) to give each session its own isolated copy. Sessions sharing a working tree will overwrite each other's changes.

### Installation

Copy the `.windsurf/` directory into any project. Everything else is auto-created:
- `.windloop/` is scaffolded automatically by `/spec-plan`
- `AGENTS.md` is created/appended automatically by `/spec-plan`

### Key Files (auto-created)

| File | Purpose |
|------|---------|
| `.windloop/index.md` | Registry of all specs |
| `.windloop/<name>/spec.md` | Spec requirements and constraints |
| `.windloop/<name>/design.md` | Architecture, interfaces, property tests |
| `.windloop/<name>/tasks.md` | Ordered task list with dependencies |
| `.windloop/<name>/progress.txt` | Auto-updated progress log |
| `.windloop/dependencies.md` | Cross-spec dependency graph |

### Settings for Maximum Autonomy

- **Auto-Execution** → Turbo (Windsurf Settings)
- **Auto-Continue** → Enabled (Windsurf Settings)
- **Worktree Mode** → On (Cascade input toggle)

---

After printing, ask: "What would you like to do? You can `/spec-plan` a new spec, `/spec-loop` an existing one, or `/spec-status` to see progress."
