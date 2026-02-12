
## Windloop Help

Print the following guide:


### Windloop — Spec-Driven Autonomous Development

**Lifecycle**: idea → `requirements.md` (why) → `design.md` (what + how) → `tasks.md` (steps) → autonomous implementation loop

Specs live in `.windloop/<name>/` or `.kiro/specs/<name>/` — same format, auto-detected.

**Available commands** (all accept an optional `<spec>` name):

| Command | Purpose |
|---------|---------|
| `/spec-help` | Show this help guide |
| `/spec-plan <name> [create\|refine]` | Create or refine a spec (auto-detected) |
| `/spec-audit <name>` | Validate spec consistency: traceability, redundancy, drift |
| `/spec-go <name>` | Autonomous loop: pick task → implement → test → commit → repeat. Also resumes work. |
| `/spec-task <name> <task>` | Implement a single task by ID (for parallel worktree use) |
| `/spec-merge <name>` | Merge parallel branches/worktrees, resolve conflicts, verify |
| `/spec-status` | Dashboard: show progress across all specs |
| `/spec-reset <name>` | Reset a spec: clear progress, uncheck tasks |

> If only one spec exists, `<name>` can be omitted.

### Quick Start

1. **New spec?** → `/spec-plan myfeature` — describe your idea, get requirements + design + tasks
2. **Ready to build?** → `/spec-go myfeature` — autonomous implementation loop
3. **Parallel work?** → Open **worktree** Cascades, each runs `/spec-task myfeature 1.3`
4. **Check progress?** → `/spec-status`

> **Important**: Never run multiple Cascade sessions on the same branch.

### Parallel Sessions (Worktrees)

**Option A — Windsurf Worktree Mode** (if available):
Toggle **Worktree Mode** in the Cascade input bar.

**Option B — Manual worktrees**:
```bash
git worktree add ../myproject-1.2 main
git worktree add ../myproject-1.3 main
# Open each in a separate Windsurf window
# /spec-task myfeature 1.2  and  /spec-task myfeature 1.3
# Merge back when done
```

**Option C — Feature branches** (simplest):
```bash
git checkout -b task/1.2 main
# /spec-task myfeature 1.2
# Merge when done
```

### Installation

Copy the `.windsurf/` directory into any project. Everything else is auto-created:
- If `.kiro/` exists, specs go under `.kiro/specs/`
- Otherwise, `.windloop/` is scaffolded by `/spec-plan`
- `AGENTS.md` is created/appended automatically

### Spec Files (auto-created)

| File | Purpose |
|------|---------|
| `requirements.md` | Requirements with user stories and WHEN/SHALL criteria |
| `design.md` | Architecture, interfaces, correctness properties |
| `tasks.md` | Task list with dependencies and requirement traceability |
| `progress.txt` | Auto-updated progress log |
| `steering/` *(optional)* | Project-level context: `product.md`, `structure.md`, `tech.md` |

### Settings for Maximum Autonomy

- **Auto-Execution** → Turbo (Windsurf Settings)
- **Auto-Continue** → Enabled (Windsurf Settings)
- **Worktree Mode** → On (Cascade input toggle)


After printing, ask: "What would you like to do? You can `/spec-plan` a new spec, `/spec-go` an existing one, or `/spec-status` to see progress."
