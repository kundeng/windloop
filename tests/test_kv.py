from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from kv import cmd_delete, cmd_get, cmd_set, load_store, main, save_store


@pytest.fixture()
def store_path(tmp_path: Path) -> Path:
    return tmp_path / "data.json"


# ---------------------------------------------------------------------------
# P4: Empty store on missing file
# ---------------------------------------------------------------------------


class TestLoadStore:
    def test_missing_file_returns_empty(self, store_path: Path) -> None:
        assert load_store(store_path) == {}

    def test_existing_file_returns_dict(self, store_path: Path) -> None:
        store_path.write_text('{"a": "1"}')
        assert load_store(store_path) == {"a": "1"}


class TestSaveStore:
    def test_writes_valid_json(self, store_path: Path) -> None:
        save_store(store_path, {"x": "y"})
        assert json.loads(store_path.read_text()) == {"x": "y"}

    def test_none_store_writes_empty(self, store_path: Path) -> None:
        save_store(store_path, None)
        assert json.loads(store_path.read_text()) == {}


# ---------------------------------------------------------------------------
# P1: Round-trip persistence
# ---------------------------------------------------------------------------


class TestRoundTrip:
    def test_save_then_load(self, store_path: Path) -> None:
        data = {"foo": "bar", "baz": "qux"}
        save_store(store_path, data)
        assert load_store(store_path) == data


# ---------------------------------------------------------------------------
# P5: Overwrite semantics
# ---------------------------------------------------------------------------


class TestOverwrite:
    def test_set_overwrites_existing_key(self, store_path: Path) -> None:
        assert main(["--path", str(store_path), "set", "k", "v1"]) == 0
        assert main(["--path", str(store_path), "set", "k", "v2"]) == 0
        assert load_store(store_path)["k"] == "v2"


# ---------------------------------------------------------------------------
# CLI command tests via main()
# ---------------------------------------------------------------------------


class TestCmdSet:
    def test_set_creates_entry(self, store_path: Path) -> None:
        assert main(["--path", str(store_path), "set", "foo", "bar"]) == 0
        assert load_store(store_path) == {"foo": "bar"}


class TestCmdGet:
    def test_get_existing_key(
        self, store_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        save_store(store_path, {"foo": "bar"})
        assert main(["--path", str(store_path), "get", "foo"]) == 0
        assert capsys.readouterr().out.strip() == "bar"

    def test_get_missing_key(
        self, store_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["--path", str(store_path), "get", "missing"]) == 1
        assert "Key not found: missing" in capsys.readouterr().err


# ---------------------------------------------------------------------------
# P2: Delete removes key
# ---------------------------------------------------------------------------


class TestCmdDelete:
    def test_delete_existing_key(self, store_path: Path) -> None:
        save_store(store_path, {"foo": "bar"})
        assert main(["--path", str(store_path), "delete", "foo"]) == 0
        assert "foo" not in load_store(store_path)

    def test_get_after_delete_returns_1(self, store_path: Path) -> None:
        main(["--path", str(store_path), "set", "foo", "bar"])
        main(["--path", str(store_path), "delete", "foo"])
        assert main(["--path", str(store_path), "get", "foo"]) == 1


# ---------------------------------------------------------------------------
# P3: Idempotent delete
# ---------------------------------------------------------------------------


class TestIdempotentDelete:
    def test_delete_nonexistent_key_exits_0(self, store_path: Path) -> None:
        assert main(["--path", str(store_path), "delete", "nope"]) == 0

    def test_delete_nonexistent_key_no_change(self, store_path: Path) -> None:
        save_store(store_path, {"a": "1"})
        main(["--path", str(store_path), "delete", "nope"])
        assert load_store(store_path) == {"a": "1"}


# ---------------------------------------------------------------------------
# main() edge cases
# ---------------------------------------------------------------------------


class TestMain:
    def test_no_args_returns_2(self, capsys: pytest.CaptureFixture[str]) -> None:
        assert main([]) == 2

    def test_empty_string_key_and_value(self, store_path: Path) -> None:
        assert main(["--path", str(store_path), "set", "", ""]) == 0
        assert load_store(store_path) == {"": ""}

    def test_main_block(self, store_path: Path) -> None:
        kv_path = Path(__file__).resolve().parent.parent / "kv.py"
        result = subprocess.run(
            [sys.executable, str(kv_path), "--path", str(store_path), "set", "x", "y"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert load_store(store_path) == {"x": "y"}
