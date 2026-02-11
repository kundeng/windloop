
## Windloop Help

Print the following guide:


### Windloop — Spec-Driven Autonomous Development

**Lifecycle**: idea → `spec.md` (why) → `design.md` (what + how) → `tasks.md` (steps) → autonomous implementation loop

**Available commands** (all accept an optional `<spec>` name):

| Command | Purpose |
|---------|---------|
| `/spec-help` | Show this help guide |
| `/spec-plan <name> [create\|refine\|update]` | Create, refine, or update a spec (auto-detected if omitted) |
| `/spec-audit <name>` | Validate spec consistency: traceability, redundancy, drift |
| `/spec-loop <name>` | Autonomous loop: pick task → implement → test → commit → repeat |
| `/spec-task <name> T[N]` | Implement a single task by ID (for parallel worktree use) |
| `/spec-merge <name>` | Review completed work and merge worktree changes |
| `/spec-status` | Dashboard: show progress across all specs |
| `/spec-reset <name>` | Reset a spec: clear progress, uncheck tasks |

> If only one spec exists, the `<name>` can be omitted.

### Quick Start

1. **New spec?** → `/spec-plan myfeature` — describe your idea, get spec + design + tasks
2. **Ready to build?** → `/spec-loop myfeature` — autonomous implementation loop
3. **Parallel work?** → Open **worktree** Cascades, each runs `/spec-task myfeature T[N]`
4. **Check progress?** → `/spec-status`

> **Important**: Never run multiple Cascade sessions on the same branch. Sessions sharing a working tree will overwrite each other's changes.

### Parallel Sessions (Worktrees)

**Option A — Windsurf Worktree Mode** (if available):
Toggle **Worktree Mode** in the Cascade input bar. Windsurf creates an isolated worktree automatically.

**Option B — Manual worktrees** (always works):
```bash
# From your repo root, create a worktree per task
git worktree add ../myproject-T2 main
git worktree add ../myproject-T3 main

# Open each worktree in a separate Windsurf window
# In window 1: /spec-task myfeature T2
# In window 2: /spec-task myfeature T3

# When done, merge back
cd /path/to/main/repo
git merge ../myproject-T2
git merge ../myproject-T3
git worktree remove ../myproject-T2
git worktree remove ../myproject-T3
```

**Option C — Feature branches** (simplest):
```bash
git checkout -b task/T2 main
# Open in Windsurf, run /spec-task myfeature T2
# Repeat for T3 on another branch in another window
# Merge branches when done
```

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


After printing, ask: "What would you like to do? You can `/spec-plan` a new spec, `/spec-loop` an existing one, or `/spec-status` to see progress."
