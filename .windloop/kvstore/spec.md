# Specification: kvstore

## Overview
A tiny Python CLI key-value store. Three commands (`get`, `set`, `delete`) persist data to a local JSON file. Zero external dependencies beyond the standard library.

## Goals
- [ ] Provide a simple CLI for key-value CRUD operations
- [ ] Persist data reliably to `data.json`
- [ ] 100% test coverage
- [ ] Clean, lint-free code

## Architecture

### Tech Stack
- **Language**: Python 3.11+
- **Framework**: None (stdlib only — `argparse`, `json`, `pathlib`)
- **Testing**: pytest + pytest-cov
- **Linter**: ruff

### Directory Structure
```
kv.py              # CLI entry point + all logic
data.json          # persisted key-value data (created at runtime)
tests/
  test_kv.py       # all tests
pyproject.toml     # project config (ruff + pytest settings)
```

## Requirements

### R1: Store a key-value pair
- **R1.1**: As a user, I should be able to run `python kv.py set <key> <value>` to store a key-value pair in `data.json`.
- **R1.2**: As a user, I should be able to overwrite an existing key by running `set` again with a new value.

### R2: Retrieve a value by key
- **R2.1**: As a user, I should be able to run `python kv.py get <key>` to print the value to stdout and exit 0.
- **R2.2**: As a user, I should see an error on stderr and exit code 1 when I `get` a key that does not exist.

### R3: Delete a key
- **R3.1**: As a user, I should be able to run `python kv.py delete <key>` to remove a key from `data.json`.
- **R3.2**: As a user, I should see no error when I `delete` a key that does not exist (silent no-op, exit 0).

### R4: Persistence
- **R4.1**: As a user, I should have my data persisted to `data.json` in the working directory so it survives across invocations.
- **R4.2**: As a user, I should be able to run commands without a pre-existing `data.json` — it is created on first write and treated as empty on read.

### R5: Quality
- **R5.1**: The project must have zero external runtime dependencies (stdlib only).
- **R5.2**: The project must have 100% line coverage via pytest-cov.
- **R5.3**: The project must have zero ruff lint violations.

## Data Models
- **Store**: A flat `dict[str, str]` serialized as JSON in `data.json`
- Keys and values are always strings

## Testing Strategy
- **Test command**: `pytest --cov=kv --cov-report=term-missing --cov-fail-under=100`
- **Lint command**: `ruff check .`
- **Coverage target**: 100%

## Constraints
- Single-file implementation (`kv.py`) — keep it simple
- `data.json` is created on first write if it doesn't exist
- Reading a missing `data.json` is treated as an empty store
- All keys and values are strings (no type coercion)

## Out of Scope
- Nested values or complex data types
- Concurrent access / file locking
- Remote storage or networking
- Shell completion
