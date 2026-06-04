"""Serialization helpers for Receipt Habitat v0.1.

Local dry-run only. Serialization makes packets hashable and reviewable; it
does not make them canon, deployable, or authoritative.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class SerializationError(ValueError):
    pass


def to_stable_json(data: dict[str, Any]) -> str:
    """Return deterministic JSON for hashing and review."""
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def _yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "" or any(ch in text for ch in [":", "#", "\n", "{", "}", "[", "]", ","]):
        return json.dumps(text, ensure_ascii=False)
    return text


def _to_simple_yaml(value: Any, indent: int = 0) -> list[str]:
    pad = "  " * indent
    lines: list[str] = []
    if isinstance(value, dict):
        for key in sorted(value.keys()):
            item = value[key]
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}{key}:")
                lines.extend(_to_simple_yaml(item, indent + 1))
            else:
                lines.append(f"{pad}{key}: {_yaml_scalar(item)}")
    elif isinstance(value, list):
        if not value:
            lines.append(f"{pad}[]")
        for item in value:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.extend(_to_simple_yaml(item, indent + 1))
            else:
                lines.append(f"{pad}- {_yaml_scalar(item)}")
    else:
        lines.append(f"{pad}{_yaml_scalar(value)}")
    return lines


def to_simple_yaml(data: dict[str, Any]) -> str:
    """Return a dependency-free YAML-like representation.

    This is intentionally conservative. Stable JSON remains the canonical
    machine-readable output for v0.1 tests and hashing.
    """
    return "\n".join(_to_simple_yaml(data)) + "\n"


def write_packet(data: dict[str, Any], output_path: str, *, fmt: str | None = None) -> Path:
    """Write a packet to disk as json or yaml.

    The output file is only an evidence packet candidate.
    """
    path = Path(output_path)
    selected = (fmt or path.suffix.lstrip(".") or "json").lower()
    if selected in {"json", "jsn"}:
        payload = to_stable_json(data)
    elif selected in {"yaml", "yml"}:
        payload = to_simple_yaml(data)
    else:
        raise SerializationError(f"unsupported serialization format: {selected}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(payload, encoding="utf-8")
    return path
