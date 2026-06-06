"""Packet helpers for Receipt Habitat v0.1."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict

import yaml


REQUIRED_DEFAULTS = {
    "canon_status": "not_canon",
    "deployment_status": "not_deployable",
    "authority_scope": "none",
    "runtime_status": "local_dry_run_only",
}


def load_yaml(path: str | Path) -> Dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("packet must be a YAML object")
    return data


def stable_packet_hash(packet: Dict[str, Any]) -> str:
    encoded = json.dumps(packet, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def apply_required_defaults(packet: Dict[str, Any]) -> Dict[str, Any]:
    updated = dict(packet)
    for key, value in REQUIRED_DEFAULTS.items():
        updated.setdefault(key, value)
    return updated


def assert_required_defaults(packet: Dict[str, Any]) -> None:
    for key, value in REQUIRED_DEFAULTS.items():
        if packet.get(key) != value:
            raise ValueError(f"{key} must be {value!r} in Receipt Habitat v0.1")
