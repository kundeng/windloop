from __future__ import annotations

import argparse
import json
import sys
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


def cmd_set(args: argparse.Namespace) -> int:
    """Set key=value, return 0."""
    store = load_store(args.path)
    store[args.key] = args.value
    save_store(args.path, store)
    return 0


def cmd_get(args: argparse.Namespace) -> int:
    """Print value for key, return 0. Return 1 if key not found."""
    store = load_store(args.path)
    if args.key not in store:
        print(f"Key not found: {args.key}", file=sys.stderr)
        return 1
    print(store[args.key])
    return 0


def cmd_delete(args: argparse.Namespace) -> int:
    """Delete key if present, return 0."""
    store = load_store(args.path)
    store.pop(args.key, None)
    save_store(args.path, store)
    return 0


def main(argv: list[str] | None = None) -> int:
    """Parse args and dispatch to command handler."""
    parser = argparse.ArgumentParser(description="Tiny key-value store")
    parser.add_argument(
        "--path", type=Path, default=DEFAULT_PATH, help="Path to data file"
    )
    sub = parser.add_subparsers(dest="command")

    p_set = sub.add_parser("set", help="Store a key-value pair")
    p_set.add_argument("key")
    p_set.add_argument("value")

    p_get = sub.add_parser("get", help="Retrieve a value by key")
    p_get.add_argument("key")

    p_del = sub.add_parser("delete", help="Delete a key")
    p_del.add_argument("key")

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_usage(sys.stderr)
        return 2

    handlers = {"set": cmd_set, "get": cmd_get, "delete": cmd_delete}
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
