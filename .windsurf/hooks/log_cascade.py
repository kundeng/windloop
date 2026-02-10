#!/usr/bin/env python3
"""Post-cascade-response hook: logs responses for audit/debugging.

Appends a summary to .windsurf/cascade_log.jsonl so you can review
what Cascade did across sessions.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def main():
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, Exception):
        sys.exit(0)

    if data.get("agent_action_name") != "post_cascade_response":
        sys.exit(0)

    tool_info = data.get("tool_info", {})
    response = tool_info.get("response", "")
    trajectory_id = data.get("trajectory_id", "unknown")

    # Truncate very long responses for the log
    max_len = 2000
    summary = response[:max_len] + ("..." if len(response) > max_len else "")

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "trajectory_id": trajectory_id,
        "response_length": len(response),
        "summary": summary,
    }

    log_path = Path(".windsurf/cascade_log.jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with open(log_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")


if __name__ == "__main__":
    main()
