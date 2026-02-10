from __future__ import annotations

import json
from pathlib import Path

DEFAULT_PATH = Path("data.json")


def load_store(path: Path = DEFAULT_PATH) -> dict[str, str]:
    """Load JSON store from disk. Returns {} if file missing."""
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)


def save_store(path: Path = DEFAULT_PATH, store: dict[str, str] | None = None) -> None:
    """Write store dict to JSON file."""
    if store is None:
        store = {}
    with open(path, "w") as f:
        json.dump(store, f, indent=2)
        f.write("\n")
