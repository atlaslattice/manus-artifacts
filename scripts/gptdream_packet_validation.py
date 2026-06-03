#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Strict packet validation helpers for GPTDream++ tests and validators."""

from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import re
from typing import Any

from scripts.lattice_kg_lib import load_yaml_strict


def strict_validate_packet(packet: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = schema.get("required", [])
    properties = schema.get("properties", {})
    allow_extra = schema.get("allow_extra", False)
    for field in required:
        if field not in packet:
            errors.append(f"missing required field: {field}")
    if not allow_extra:
        unexpected = sorted(set(packet) - set(properties))
        if unexpected:
            errors.append(f"unexpected fields: {', '.join(unexpected)}")
    for field, rules in properties.items():
        if field not in packet:
            continue
        value = packet[field]
        if value is None and not rules.get("nullable", False):
            errors.append(f"null not allowed: {field}")
            continue
        expected_type = rules.get("type")
        if expected_type == "string" and not isinstance(value, str):
            errors.append(f"wrong type for {field}: expected string")
        if expected_type == "integer" and not isinstance(value, int):
            errors.append(f"wrong type for {field}: expected integer")
        if expected_type == "list" and not isinstance(value, list):
            errors.append(f"wrong type for {field}: expected list")
        if "enum" in rules and value not in rules["enum"]:
            errors.append(f"invalid enum for {field}: {value}")
        if isinstance(value, str) and rules.get("format") == "date-time":
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value):
                errors.append(f"invalid format for {field}")
        if isinstance(value, int) and "max" in rules and value > rules["max"]:
            errors.append(f"overflow for {field}")
        if rules.get("non_empty") and value in ("", [], {}):
            errors.append(f"empty payload for {field}")
        if rules.get("forbid_self_ref") and value == packet.get("id"):
            errors.append(f"circular ref for {field}")
    if packet.get("schema_version") and packet.get("schema_version") != schema.get("schema_version"):
        errors.append("version conflict")
    if packet.get("authority") not in {None, "none"} and packet.get("ratification_event_id") in {None, "", "PENDING"}:
        errors.append("auth escalation")
    return errors


def parse_packet_yaml(text: str) -> tuple[dict[str, Any] | None, str | None]:
    payload, error = load_yaml_strict(text)
    if error:
        return None, error
    if not isinstance(payload, dict):
        return None, "packet must be a mapping"
    return payload, None
