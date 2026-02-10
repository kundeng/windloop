# File-Based Mailbox Protocol

## Overview

Windsurf Cascade sessions cannot communicate directly. This mailbox protocol uses the
shared filesystem as a message bus, enabling one Cascade session to signal, coordinate
with, or pass information to another.

**Why this works**: Cascade has real-time awareness of file changes in the workspace.
When one session writes a file, another session can be instructed (via workflows/rules)
to watch for and react to those files.

## Protocol

### Directory Structure

```
.windsurf/mailbox/
├── README.md          # This file
├── inbox/             # Messages TO a session (named by recipient)
│   ├── lead/          # Messages for the lead/orchestrator session
│   └── worker-1/      # Messages for worker session 1
├── outbox/            # Completed signals FROM a session
│   ├── worker-1/      # Completion signals from worker 1
│   └── worker-2/
└── board/             # Shared state visible to all sessions
    ├── status.json    # Overall coordination status
    └── claims.json    # Task claim registry (prevents double-work)
```

### Message Format

Messages are JSON files named `{timestamp}-{action}.json`:

```json
{
  "from": "lead",
  "to": "worker-1",
  "action": "implement",
  "spec": "taskrunner",
  "task_id": "T3",
  "timestamp": "2026-02-09T22:30:00Z",
  "payload": {
    "notes": "T1 and T2 are done. You can start T3."
  }
}
```

### Actions

| Action | Direction | Purpose |
|--------|-----------|---------|
| `implement` | lead → worker | Assign a task to a worker session |
| `done` | worker → lead | Signal task completion |
| `blocked` | worker → lead | Signal task is blocked |
| `status` | any → board | Update shared status |
| `claim` | worker → board | Claim a task (prevents double-work) |
| `abort` | lead → worker | Tell worker to stop current task |
| `info` | any → any | Pass arbitrary information |

### Coordination Patterns

#### Pattern 1: Lead-Worker (Orchestrated)

1. **Lead session** reads specs, plans work, writes assignment messages to `inbox/worker-N/`
2. **Worker sessions** (in worktrees) check their inbox, implement assigned tasks
3. Workers write completion signals to `outbox/worker-N/`
4. Lead watches outbox directories, assigns next tasks

#### Pattern 2: Claim Board (Self-Organizing)

1. All sessions read `board/status.json` for available tasks
2. Before starting, a session writes a claim to `board/claims.json`
3. Session checks if its claim was first (file-level atomicity)
4. Implements task, updates board on completion

#### Pattern 3: Pipeline (Sequential Handoff)

1. Session A completes Phase 1, writes to `inbox/session-b/`
2. Session B picks up, completes Phase 2, writes to `inbox/session-c/`
3. Each session handles one phase of a multi-phase pipeline

## Limitations

- **No true locking**: Filesystem writes aren't atomic across sessions. Use claim-then-verify.
- **Polling required**: Sessions must be instructed to check mailbox files. No push notifications.
- **Manual setup**: Each parallel session must be launched manually and told its role.
- **Cascade awareness**: Cascade sees file changes in real-time but won't automatically act on them
  unless instructed via workflows/rules to check the mailbox.
