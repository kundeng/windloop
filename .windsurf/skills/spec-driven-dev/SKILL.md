---
name: spec-driven-dev
description: "IMPORTANT: Files in .windloop/ and .kiro/specs/ are spec-driven artifacts. NEVER edit requirements.md, design.md, tasks.md, or progress.txt without first reading this skill's rules and the relevant workflow in references/. Always check tasks.md for the next uncompleted task and follow the spec-go workflow to implement it. Commands: spec-plan (create/refine specs), spec-go (autonomous implement loop — also use for resume/continue), spec-task (single task), spec-audit (validate consistency), spec-status (dashboard), spec-merge (merge branches), spec-reset (clear progress), spec-help (onboarding)."
---

## Spec-Driven Development

This skill powers the windloop framework. Specs live in a **spec directory** — either `.windloop/<name>/` or `.kiro/specs/<name>/`. The format is the same regardless of location.

### Spec Lifecycle

```
idea → requirements.md (why) → design.md (what + how) → tasks.md (steps) → [implement loop] → done
```

The traceability chain:
- **requirements.md** — requirements as user stories with WHEN/SHALL acceptance criteria — the *why*
- **design.md** — architecture, tech stack, constraints, testing strategy, correctness properties — the *what + how*
- **tasks.md** — implementation tasks referencing requirements and properties — the *steps*
- **progress.txt** — auto-updated log
- **steering/** *(optional)* — project-level context: product vision, repo structure, tech decisions. Read-only priors that inform all spec work.

### Workflow References

Detailed instructions for each command live in `references/` alongside this file. When a command is invoked, read the corresponding reference document.

### Commands

| Command | Reference | Purpose |
|---------|-----------|---------|
| `/spec-help` | [spec-help.md](references/spec-help.md) | Onboarding guide |
| `/spec-plan <name> [create\|refine]` | [spec-plan.md](references/spec-plan.md) | Create or refine a spec |
| `/spec-audit <name>` | [spec-audit.md](references/spec-audit.md) | Validate spec consistency |
| `/spec-go <name>` | [spec-go.md](references/spec-go.md) | Autonomous implement loop |
| `/spec-task <name> <task>` | [spec-task.md](references/spec-task.md) | Implement single task |
| `/spec-merge <name>` | [spec-merge.md](references/spec-merge.md) | Merge parallel branches, resolve conflicts, verify |
| `/spec-status` | [spec-status.md](references/spec-status.md) | Progress dashboard |
| `/spec-reset <name>` | [spec-reset.md](references/spec-reset.md) | Clear progress for re-run |

### Spec Resolution

When a command receives a spec name SPEC, resolve its directory:

1. `.windloop/SPEC/` — if exists, use it
2. `.kiro/specs/SPEC/` — if exists, use it
3. Neither → error

When no name is given, list directories in `.windloop/` and `.kiro/specs/`. If exactly one spec exists, use it automatically.

Let **SPEC_DIR** be the resolved directory.

### Rules

1. **One session per working tree**: use worktrees or branches to isolate parallel work.
2. **Resolve the spec** using the Spec Resolution rules above.
3. Read `requirements.md` AND `design.md` before implementing. If `steering/` exists, read it too.
4. Check task dependencies — never skip ahead.
5. **Write tests first**: implement the task's property tests before production code. E2E tests are separate tasks.
6. Run verify after implementation; fix up to 3 times before BLOCKED.
7. Commit per task: `feat(<spec>/<task>): [description]`
8. Update `tasks.md` (checkbox) and `progress.txt` (log line) after each task.
9. Keep changes minimal and focused.

### Scaffolding

When `/spec-plan` creates a new spec:

**If `.kiro/` exists** → create under `.kiro/specs/<name>/`
**Otherwise** → create under `.windloop/<name>/`

```
<spec-dir>/
  requirements.md
  design.md
  tasks.md
  progress.txt
```

### Steering Docs (optional)

Steering docs provide project-level context that applies across all specs. They live at the root of the spec area:

- `.windloop/steering/` or `.kiro/steering/`

| File | Purpose |
|------|--------|
| `product.md` | Product vision, target users, key goals |
| `structure.md` | Repo layout, module boundaries, naming conventions |
| `tech.md` | Tech stack decisions, version constraints, deployment targets |

**Rules:**
- Steering docs are **read-only context** — never modify them during task execution.
- When they exist, **always** read them during planning (`spec-plan`) and before implementing (`spec-go`, `spec-task`).
- They are not scaffolded automatically — the user creates them when ready.
- They inform requirements, design decisions, and coding conventions but are not part of the traceability chain.

If the host project has an `AGENTS.md`, append the windloop snippet (see below). If not, create it.

### AGENTS.md Snippet

```markdown
## Windloop

This project uses spec-driven development. Specs live in `.windloop/` or `.kiro/specs/`.
Read the `spec-driven-dev` skill before modifying any spec files.
Run `/spec-help` for the full command list.
```

### Spec Refinement Principles

When running `/spec-plan <name> refine`:

1. **Merge redundant requirements**: combine duplicates into the earlier/more natural location.
2. **Separate what from how**: move implementation details from Requirements to Constraints.
3. **Collapse over-specified sub-requirements**: individual assertions become acceptance criteria on tasks, not separate requirements.
4. **Demote aspirational items**: untestable patterns become Notes, not requirements.
5. **Merge overlapping properties**: if one is a subset of another, merge and renumber.
6. **Cascade renumbering**: update ALL references in design.md and tasks.md after merging/removing.
7. **Validate traceability**: every requirement → ≥1 property → ≥1 task. Flag orphans.
8. **Present tense for done work**: completed requirements describe the system as-is.
9. **Sync derived documents**: update README, architecture docs, etc. if affected.
10. **Align spec with disk**: fix stale paths, add missing entries, remove deleted files.

### Embedded Templates

#### requirements.md template

```markdown
# Requirements Document

## Introduction
<!-- Brief description of what this spec covers and why -->

## Glossary

- **Term_1**: Definition
- **Term_2**: Definition

## Requirements

### Requirement 1: [Feature area]

**User Story:** As a [role], I want [action], so that [benefit].

#### Acceptance Criteria

1. WHEN [trigger], THE [Component] SHALL [expected behavior]
2. WHEN [trigger], THE [Component] SHALL [expected behavior]

### Requirement 2: [Feature area]

**User Story:** As a [role], I want [action], so that [benefit].

#### Acceptance Criteria

1. WHEN [trigger], THE [Component] SHALL [expected behavior]

### Non-Functional

**NF 1**: [Performance / reliability / security requirement]

## Out of Scope
<!-- What this spec explicitly does NOT cover -->
```

#### design.md template

```markdown
# Design: [SPEC NAME]

## Tech Stack
- **Language**:
- **Framework**:
- **Testing**:
- **Linter**:

## Directory Structure
\```
src/
tests/
\```

## Architecture Overview

\```mermaid
graph TD
    A[Module A] --> B[Module B]
    A --> C[Module C]
    B --> D[Shared Service]
    C --> D
\```

## Module Design

### [Module 1]
- **Purpose**: [what it does]
- **Interface**:
  \```
  [function signatures, class interfaces, API endpoints]
  \```
- **Dependencies**: [what it depends on]

## Data Flow

\```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant Service
    participant Store
    User->>CLI: command
    CLI->>Service: process(args)
    Service->>Store: read/write
    Store-->>Service: result
    Service-->>CLI: output
    CLI-->>User: display
\```

## State Management
<!-- Omit if stateless -->

## Data Models
<!-- Omit if simple -->

## Error Handling Strategy
<!-- How errors are propagated and handled -->

## Testing Strategy

- **Property tests**: Verify design invariants, inline with implementation tasks (required)
- **E2E tests**: Validate user stories end-to-end, as separate tasks (required)
- **Unit tests**: For complex internal logic only (optional, add when warranted)
- **Test command**: `[command]`
- **Lint command**: `[command]`
- **Coverage target**: [percentage]

## Constraints
<!-- Important decisions and constraints -->

## Correctness Properties

Properties that must hold true. Each validates one or more requirements.

### Property 1: [Property name]
- **Statement**: *For any* [condition], when [action], then [expected outcome]
- **Validates**: Requirement 1.1, 1.2
- **Example**: [concrete example]
- **Test approach**: [how to verify]

### Property 2: [Property name]
- **Statement**: *For any* [condition], when [action], then [expected outcome]
- **Validates**: Requirement 2.1
- **Example**: [example]
- **Test approach**: [approach]

## Edge Cases
<!-- Known edge cases and how they should be handled -->

## Decisions
<!-- Key design decisions and rationale -->

## Security Considerations
<!-- If applicable -->
```

**Diagram guidance**: Include diagrams that match complexity:
- **Always**: Component diagram (architecture overview)
- **Multi-actor systems**: Sequence diagram
- **Stateful systems**: State diagram
- **Data-heavy systems**: ER diagram

Omit sections that don't apply. Use Mermaid syntax.

#### tasks.md template

```markdown
# Tasks: [SPEC NAME]

## Overview
<!-- Brief description of implementation approach -->

## Tasks

- [ ] 1. [Phase or group title]
  - [ ] 1.1 [Task title]
    - [What to implement]
    - **Depends**: —
    - **Requirements**: 1.1, 1.2
    - **Properties**: 1
    - **Tests**: Property 1 (validates 1.1, 1.2)
    - **Files**: `src/...`, `tests/...`
    - **Verify**: `[command]`

  - [ ] 1.2 [Task title]
    - [What to implement]
    - **Depends**: 1.1
    - **Requirements**: 2.1
    - **Properties**: 2
    - **Tests**: Property 2 (validates 2.1)
    - **Files**: `src/...`, `tests/...`
    - **Verify**: `[command]`

  - [ ]* 1.3 [Optional task title]
    - [What to implement]
    - **Depends**: 1.1
    - **Files**: `tests/...`
    - **Verify**: `[command]`

- [ ] 2. [Phase or group title]
  - [ ] 2.1 [Task title]
    - [What to implement]
    - **Depends**: 1.1, 1.2
    - **Requirements**: 1.3, 2.2
    - **Properties**: 1, 2
    - **Files**: `src/...`
    - **Verify**: `[command]`

- [ ] 3. E2E Tests
  - [ ] 3.1 E2E — [User story scenario]
    - End-to-end test validating [user story]
    - **Depends**: 1.1, 1.2
    - **Requirements**: 1.1, 1.2, 2.1
    - **Files**: `tests/...`
    - **Verify**: `[command]`

## Notes
<!-- Implementation notes, known issues, etc. -->
```

**Task conventions**:
- IDs use hierarchical numbering: `1.1`, `1.2`, `2.1`, etc.
- Parent items (`1.`, `2.`) are phase/group headers — their checkbox tracks phase completion.
- `[ ]*` marks optional tasks.
- `[~]` = partial/skipped, `[!]` = blocked.
- **Depends**, **Files**, **Verify** are windloop enhancements that Kiro tasks don't have — always include them.

#### progress.txt template

```
# Progress Log: [SPEC NAME]
# Auto-updated by spec-go workflow
# Format: [TIMESTAMP] [STATUS] [TASK_ID] - [DESCRIPTION]
# STATUS: DONE | BLOCKED | SKIPPED | IN_PROGRESS
# SUMMARY: 0/N done | next: 1.1
```

The `# SUMMARY:` line is machine-readable. Format: `# SUMMARY: <done>/<total> done | next: <NEXT_TASK_ID or DONE>`

### Parallel Execution

For independent tasks, use worktree mode:
1. Open a new Cascade in Worktree mode
2. Run `/spec-task <name> <task>`
3. Merge back when done

