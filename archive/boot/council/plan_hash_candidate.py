"""Offline Council plan-hash binding and split-verifier packet checker.

No execution, policy grant, verified reviewer identity, signature, CANON or
deployment. This Python-local canonical JSON profile is NOT RFC 8785/JCS.
"""
from __future__ import annotations

from hashlib import sha256
import json
from typing import Any

MAX_PLAN_BYTES = 256 * 1024


class PlanHold(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for key, value in items:
        if key in data:
            raise PlanHold("DUPLICATE_JSON_KEY")
        data[key] = value
    return data


def _reject_number(_: str) -> None:
    raise PlanHold("NON_INTEGER_JSON_NUMBER")


def _plain(value: Any, depth: int = 0) -> bool:
    if depth > 32:
        return False
    if value is None or type(value) in (str, bool):
        return True
    if type(value) is int:
        return -(2 ** 53) < value < (2 ** 53)
    if type(value) is list:
        return len(value) <= 2000 and all(_plain(x, depth + 1) for x in value)
    if type(value) is dict:
        return (len(value) <= 2000 and
                all(type(k) is str and _plain(v, depth + 1) for k, v in value.items()))
    return False


def canonical_plan(raw: bytes) -> bytes:
    if type(raw) is not bytes or not raw or len(raw) > MAX_PLAN_BYTES:
        raise PlanHold("PLAN_MISSING_OR_TOO_LARGE")
    try:
        parsed = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_reject_number,
            parse_float=_reject_number,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise PlanHold("INVALID_PLAN_JSON") from exc
    if type(parsed) is not dict or not _plain(parsed):
        raise PlanHold("PLAN_NOT_STRICT_PLAIN_OBJECT")
    if parsed.get("status") != "candidate" or parsed.get("canon") is not False:
        raise PlanHold("NOT_A_CANDIDATE_PLAN")
    return json.dumps(
        parsed, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def digest_plan(raw: bytes) -> str:
    return sha256(canonical_plan(raw)).hexdigest()


def inspect_binding(plan_raw: bytes, execution: Any,
                    logic_verifier: Any, security_verifier: Any) -> dict[str, Any]:
    errors: list[str] = []
    try:
        fingerprint = digest_plan(plan_raw)
    except (PlanHold, TypeError, ValueError) as exc:
        fingerprint = None
        errors.append(str(exc))

    if type(execution) is not dict or set(execution) != {
        "plan_sha256", "dry_run_only", "effects_executed", "source_ref"
    }:
        errors.append("INVALID_EXECUTION_PACKET")
    else:
        if execution["plan_sha256"] != fingerprint or fingerprint is None:
            errors.append("EXECUTION_PLAN_HASH_MISMATCH")
        if execution["dry_run_only"] is not True or execution["effects_executed"] is not False:
            errors.append("EXECUTION_NOT_DRY_RUN")

    for lane, packet in (("logic_verifier", logic_verifier),
                         ("security_verifier", security_verifier)):
        if type(packet) is not dict or set(packet) != {
            "lane", "plan_sha256", "verdict", "evidence_ref"
        }:
            errors.append(lane.upper() + "_PACKET_INVALID")
            continue
        if packet["lane"] != lane:
            errors.append(lane.upper() + "_LANE_MISMATCH")
        if fingerprint is None or packet["plan_sha256"] != fingerprint:
            errors.append(lane.upper() + "_PLAN_HASH_MISMATCH")
        if packet["verdict"] != "PASS":
            errors.append(lane.upper() + "_NO_PASS")
        if type(packet["evidence_ref"]) is not str or not packet["evidence_ref"].strip():
            errors.append(lane.upper() + "_MISSING_EVIDENCE")

    return {
        "status": "HOLD" if errors else "STRUCTURAL_CANDIDATE_READY_NOT_AUTHORIZED",
        "plan_sha256_python_profile": fingerprint,
        "errors": sorted(set(errors)),
        "logic_verifier_identity_authenticated": False,
        "security_verifier_identity_authenticated": False,
        "host_execution_permitted": False,
        "approval_granted": False,
        "canon": False,
        "deployed": False,
    }
