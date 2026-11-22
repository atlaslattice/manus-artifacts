"""Strict offline candidate index loader. No imports or execution of referenced paths."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

MAX_BYTES = 256 * 1024


class IndexHold(ValueError):
    pass


def strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name, val in pairs:
        if name in result:
            raise IndexHold("DUPLICATE_JSON_KEY")
        result[name] = val
    return result


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    raw = path.read_bytes()
    if not raw or len(raw) > MAX_BYTES:
        raise IndexHold("EMPTY_OR_OVERSIZE_INDEX")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise IndexHold("INVALID_UTF8") from exc
    records: list[dict[str, Any]] = []
    for line, src in enumerate(text.splitlines(), start=1):
        if not src.strip():
            continue
        try:
            row = json.loads(
                src, object_pairs_hook=strict_pairs,
                parse_constant=lambda _: (_ for _ in ()).throw(IndexHold("NONFINITE_JSON"))
            )
        except (ValueError, IndexHold) as exc:
            raise IndexHold(f"INVALID_JSONL_LINE_{line}: {exc}") from exc
        if type(row) is not dict:
            raise IndexHold(f"NON_OBJECT_LINE_{line}")
        records.append(row)
    if not records or len(records) > 256:
        raise IndexHold("INDEX_ROW_COUNT_INVALID")
    return records


def text(value: Any) -> bool:
    return type(value) is str and bool(value.strip())


def unique_words(values: Any) -> bool:
    return (type(values) is list and len(values) > 0
            and all(text(v) for v in values)
            and len(values) == len(set(values)))


def safe_pointer(value: Any) -> bool:
    """Only basic relative repo paths; no path lookup, source access or network."""
    if not text(value) or "://" in value:
        return False
    return (not value.startswith(("/", "~", "\\")) and
            "\\" not in value and ".." not in value.split("/") and
            all(bool(part) for part in value.split("/")))
