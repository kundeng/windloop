---
name: spec-driven-dev
description: Guides spec-driven autonomous development. Workflows: spec-plan (plan/design/create a feature), spec-loop (autonomous implement/build/code loop), spec-task (implement a single task), spec-audit (validate consistency/traceability/drift), spec-status (check progress/dashboard), spec-merge (merge parallel work), spec-reset (start over), spec-help (onboarding).
---

## Spec-Driven Development

This skill powers the windloop framework. Specs live in `.windloop/<name>/` and are registered in `.windloop/index.md`.

### Spec Lifecycle

```
idea → spec.md (why) → design.md (what + how) → tasks.md (steps) → [implement loop] → done
```

The traceability chain ensures nothing is lost:
- **spec.md** — requirements as user stories (R1.1, R1.2, NF1) — the *why*
- **design.md** — architecture, tech stack, constraints, testing strategy, properties (P1, P2 validate R-numbers) — the *what + how*
- **tasks.md** — tasks reference both requirements and properties they fulfill — the *steps*
- **progress.txt** — auto-updated log

### Workflow References

Detailed instructions for each command live in `references/` alongside this file. When a command is invoked, read the corresponding reference document.

### Commands

| Command | Reference | Purpose |
|---------|-----------|---------|
| `/spec-help` | [spec-help.md](references/spec-help.md) | Onboarding guide |
| `/spec-plan <name> [create\|refine\|update]` | [spec-plan.md](references/spec-plan.md) | Create, refine, or update a spec |
| `/spec-audit <name>` | [spec-audit.md](references/spec-audit.md) | Validate spec consistency |
| `/spec-loop <name>` | [spec-loop.md](references/spec-loop.md) | Autonomous implement loop |
| `/spec-task <name> T[N]` | [spec-task.md](references/spec-task.md) | Implement single task |
| `/spec-merge <name>` | [spec-merge.md](references/spec-merge.md) | Review and merge parallel work |
| `/spec-status` | [spec-status.md](references/spec-status.md) | Progress dashboard |
| `/spec-reset <name>` | [spec-reset.md](references/spec-reset.md) | Clear progress for re-run |

### Rules

1. **One session per working tree**: never run multiple Cascade sessions on the same branch/worktree. Use worktrees or branches to isolate parallel work — sessions that share a working tree will conflict.
2. Read `.windloop/index.md` first to find specs
3. Read spec.md AND design.md before implementing
4. Check task dependencies — never skip ahead
5. **Write tests first**: implement the task's property tests before production code. E2E tests are separate tasks.
6. Run verify after implementation; fix up to 3 times before BLOCKED
7. Commit per task: `feat(<spec>/T[N]): [description]`
8. Update `tasks.md` (checkbox) and `progress.txt` (log line) after each task
9. Keep changes minimal and focused

### Scaffolding

When `/spec-plan` runs and `.windloop/` doesn't exist, auto-create:
```
.windloop/
  index.md
  dependencies.md
  <name>/
    spec.md
    design.md
    tasks.md
    progress.txt
```

If the host project already has an `AGENTS.md`, append the windloop snippet (see below). If not, create it.

### AGENTS.md Snippet

When creating or updating AGENTS.md for a host project, append this block:

```markdown
## Windloop

This project uses the `spec-driven-dev` skill for autonomous development. Run `/spec-help` to get started.
```

### Spec Refinement Principles

When running `/spec-plan <name> refine`, follow these principles to simplify while keeping completeness:

1. **Merge redundant requirements**: If two requirements describe the same behavior in different sections, merge them into the earlier/more natural location and delete the duplicate.
2. **Separate what from how**: Move implementation details (specific file contents, build instructions, config snippets) from Requirements to Constraints. Requirements describe *what the user can do*; constraints describe *how it must be built*.
3. **Collapse over-specified sub-requirements**: If multiple sub-requirements describe individual assertions inside a single feature, collapse them into one requirement. The individual checks become acceptance criteria on the implementing task, not separate requirements.
4. **Demote aspirational items**: If a requirement describes a *supported pattern* rather than a *tested feature*, demote it to a Note under the parent requirement section. Requirements must be testable.
5. **Merge overlapping properties**: If one property is a strict subset of another, merge the smaller into the larger and renumber.
6. **Cascade renumbering**: After merging or removing requirements/properties, update ALL references in:
   - `design.md` — property `Validates:` lines
   - `tasks.md` — task `Requirements:`, `Properties:`, and `Tests:` lines
   - Verify no orphan references remain
7. **Validate traceability**: After refactoring, check:
   - Every R maps to ≥1 P in design.md
   - Every P maps to ≥1 T in tasks.md
   - No T references a nonexistent R or P
   - Flag orphans in the change summary
8. **Present tense for done work**: Rewrite completed requirements in present tense ("X does Y") not future tense ("X should do Y", "currently missing"). The spec describes the system as it is, plus pending goals.
9. **Sync derived documents**: If spec changes affect project documentation files (e.g., README, architecture docs, agent docs), update them. The spec is the source of truth.
10. **Align spec with disk**: Verify the directory structure in the spec matches the actual repo layout. Fix stale paths, add missing entries, remove entries for deleted files.

### Embedded Templates

#### spec.md template

```markdown
# Specification: [SPEC NAME]

## Overview
<!-- Brief description of what this spec covers and why -->

## Goals
- [ ] Goal 1
- [ ] Goal 2

## Requirements

<!-- Requirements are numbered hierarchically (R1, R1.1, R1.2, R2, etc.)
     and framed as user stories where applicable.
     Requirements describe WHY — what the user needs and why. -->

### R1: [Feature area]

**R1.1**: As a [role], I should be able to [action] so that [benefit].

**R1.2**: As a [role], I should be able to [action] so that [benefit].

### R2: [Feature area]

**R2.1**: As a [role], I should be able to [action] so that [benefit].

### Non-Functional

**NF1**: [Performance / reliability / security requirement]

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

<!-- Include a Mermaid component diagram showing major modules and their relationships -->

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

<!-- Include a Mermaid sequence diagram for key interactions -->

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

<!-- Include a Mermaid state diagram if the system has stateful behavior -->
<!-- Omit this section if the system is stateless -->

\```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: request
    Processing --> Success: ok
    Processing --> Error: fail
    Success --> Idle
    Error --> Idle: retry
\```

## Data Models

<!-- Include a Mermaid ER diagram if there are data relationships -->
<!-- Omit this section for simple data models -->

\```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ITEM : contains
\```

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

## Property Tests

Properties that must hold true. Each property validates one or more requirements from spec.md.

### P1: [Property name]
- **Statement**: *For any* [condition], when [action], then [expected outcome]
- **Validates**: R1.1, R1.2
- **Example**: [concrete example]
- **Test approach**: [how to verify]

### P2: [Property name]
- **Statement**: *For any* [condition], when [action], then [expected outcome]
- **Validates**: R2.1
- **Example**: [example]
- **Test approach**: [approach]

## Edge Cases
<!-- Known edge cases and how they should be handled -->

## Decisions
<!-- Key design decisions and rationale -->

## Security Considerations
<!-- If applicable -->
```

**Diagram guidance**: Include diagrams that match the spec's complexity:
- **Always**: Component diagram (architecture overview)
- **Multi-actor systems**: Sequence diagram (swimming lanes)
- **Stateful systems**: State diagram
- **Data-heavy systems**: ER diagram
- **Complex logic**: Flowchart

Omit diagram sections that don't apply. Use Mermaid syntax (renders in GitHub, VS Code, most markdown viewers).

#### tasks.md template

```markdown
# Tasks: [SPEC NAME]

<!--
STATUS: [ ] pending | [x] done | [~] partial/skipped | [!] blocked
OPTIONAL: add * after bracket to mark optional, e.g. [ ]* or [x]*
PRIORITY: P0 critical | P1 important | P2 nice-to-have
DEPENDS: task IDs that must complete first
REQUIREMENTS: requirement IDs from spec.md this task fulfills
PROPERTIES: property IDs from design.md this task should satisfy
-->

## Phase 1: Foundation

### T1: [Task title] `P0`
- **Description**: [What to implement]
- **Requirements**: R1.1, R1.2
- **Properties**: P1
- **Tests**:
  - [ ] Property test — P1: [Property name] (validates R1.1, R1.2)
- **Acceptance criteria**:
  - [ ] Criterion 1
  - [ ]* Criterion 2 (optional)
- **Files**: `src/...`, `tests/...`
- **Verify**: `[command]`
- **Status**: [ ]

### T2: [Task title] `P0`
- **Description**: [What to implement]
- **Depends**: T1
- **Requirements**: R2.1
- **Properties**: P2
- **Tests**:
  - [ ] Property test — P2: [Property name] (validates R2.1)
- **Acceptance criteria**:
  - [ ] Criterion 1
- **Files**: `src/...`, `tests/...`
- **Verify**: `[command]`
- **Status**: [ ]

## Phase 2: Core

### T3: [Task title] `P1`
- **Depends**: T1, T2
- **Requirements**: R1.3, R2.2
- **Properties**: P1, P2
- ...

## Phase 3: E2E Tests

### T4: E2E — [User story scenario] `P0`
- **Description**: End-to-end test validating [user story]
- **Depends**: T1, T2
- **Requirements**: R1.1, R1.2, R2.1
- **Acceptance criteria**:
  - [ ] [Full scenario passes]
- **Files**: `tests/...`
- **Verify**: `[command]`
- **Status**: [ ]

### T5: E2E — [Another scenario] `P1`
- **Description**: End-to-end test validating [user story]
- **Depends**: T3
- **Requirements**: R1.3
- **Acceptance criteria**:
  - [ ] [Full scenario passes]
- **Files**: `tests/...`
- **Verify**: `[command]`
- **Status**: [ ]

## Phase 4: Polish

### T6: [Task title] `P2`
- **Depends**: T4
- **Requirements**: NF1
- ...
```

#### progress.txt template

```
# Progress Log: [SPEC NAME]
# Auto-updated by spec-loop workflow
# Format: [TIMESTAMP] [STATUS] [TASK_ID] - [DESCRIPTION]
# STATUS: DONE | BLOCKED | SKIPPED | IN_PROGRESS
# SUMMARY: 0/N done | next: T1
```

The `# SUMMARY:` line is a machine-readable one-liner that agents update after each task. Format: `# SUMMARY: <done>/<total> done | next: <NEXT_TASK_ID or DONE>`

#### index.md template

```markdown
# Windloop Specs

| Spec | Status | Description |
|------|--------|-------------|
| [name] | active | [description] |
```

#### dependencies.md template

```markdown
# Spec Dependencies

Format: `<spec> -> <prerequisite>` (dependent -> prerequisite)

<!-- Example:
api -> auth
dashboard -> api
-->
```

### Parallel Execution

For independent tasks, use worktree mode:
1. Open a new Cascade in Worktree mode
2. Run `/spec-task <name> T[N]`
3. Merge back when done

