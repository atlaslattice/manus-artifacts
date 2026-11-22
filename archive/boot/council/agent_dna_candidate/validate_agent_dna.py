"""Offline advisory Agent DNA candidate metadata validation.

This is not resident identity authentication, permission granting, agent execution,
human-root signature verification, live memory, CANON or deployment.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

TOP = {"schema_version", "status", "canon", "deployed", "source_mode",
       "source_ref", "identity", "role", "capabilities", "governance",
       "memory", "temperament", "inheritance"}
IDENTITY = {"id", "display_name", "lineage", "verified"}
ROLE = {"primary_mode", "specialties"}
CAPS = {"declared_tools", "declared_protocols", "can_read", "can_write", "can_execute"}
GOV = {"authority_scope", "human_root_required", "requires_approval_for",
       "constitutional_constraints", "forbidden_actions"}
MEMORY = {"persistence", "replay_capable", "provenance_required", "native_memory_claim"}
TEMPERAMENT = {"creativity", "skepticism", "autonomy", "verbosity"}
INHERITANCE = {"descriptive_traits", "permissions_inherited", "authority_inherited"}
DESCRIPTIVE_ALLOWED = {"role.specialties", "temperament.creativity", "temperament.skepticism",
                       "temperament.autonomy", "temperament.verbosity", "memory.persistence"}
MODES = {"analysis", "execution", "reflection", "simulation", "memory", "arbitration"}
REQUIRED_GATES = {"external_write", "privacy_restricted_source", "canon", "deployment"}
REQUIRED_INVARIANTS = {"identity_metadata_is_not_authority", "memory_is_not_permission",
                       "no_merged_mind", "preserve_dissent"}


def read_strict_json(raw: bytes) -> Any:
    def duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, val in pairs:
            if key in result:
                raise ValueError("duplicate JSON key: " + key)
            result[key] = val
        return result
    return json.loads(raw.decode("utf-8"), object_pairs_hook=duplicates)


def inspect_profile(packet: Any) -> dict[str, Any]:
    problems: list[str] = []

    def error(message: str) -> None:
        problems.append(message)

    def fields(obj: Any, expected: set[str], label: str) -> bool:
        if not isinstance(obj, dict):
            error(label + "_must_be_object")
            return False
        if set(obj) != expected:
            error(label + "_missing_or_extra_fields")
        return True

    def text(obj: dict[str, Any], key: str, label: str) -> bool:
        v = obj.get(key)
        if not isinstance(v, str) or not v.strip():
            error(label + "_required_nonempty")
            return False
        return True

    def string_array(obj: dict[str, Any], key: str, label: str) -> list[str]:
        v = obj.get(key)
        if (not isinstance(v, list) or not all(isinstance(x, str) and bool(x.strip()) for x in v)
                or len(set(x for x in v if isinstance(x, str))) != len(v)):
            error(label + "_requires_unique_nonempty_strings")
            return []
        return v

    if not fields(packet, TOP, "packet"):
        return {"disposition": "HOLD", "errors": problems, "identity_verified": False,
                "execution_permission_granted": False, "canon": False, "deployed": False}

    if packet.get("schema_version") != "0.1.0" or packet.get("status") != "candidate":
        error("version_or_candidate_status_incorrect")
    if packet.get("canon") is not False or packet.get("deployed") is not False:
        error("canon_or_deployment_self_claim")
    if not isinstance(packet.get("source_mode"), str) or packet["source_mode"] not in {"synthetic", "consented_work"}:
        error("unsafe_source_mode")
    text(packet, "source_ref", "source_ref")

    identity = packet.get("identity")
    if fields(identity, IDENTITY, "identity"):
        if not text(identity, "id", "identity_id") or re.fullmatch(r"[A-Za-z0-9._:-]{2,80}", identity["id"]) is None:
            error("invalid_identity_id")
        text(identity, "display_name", "display_name")
        string_array(identity, "lineage", "lineage")
        if identity.get("verified") is not False:
            error("identity_claimed_verified")

    role = packet.get("role")
    if fields(role, ROLE, "role"):
        if not isinstance(role.get("primary_mode"), str) or role.get("primary_mode") not in MODES:
            error("invalid_role_mode")
        string_array(role, "specialties", "specialties")

    caps = packet.get("capabilities")
    if fields(caps, CAPS, "capabilities"):
        string_array(caps, "declared_tools", "declared_tools")
        string_array(caps, "declared_protocols", "declared_protocols")
        if any(caps.get(k) is not False for k in ("can_read", "can_write", "can_execute")):
            error("capability_declaration_is_not_permission")

    gov = packet.get("governance")
    if fields(gov, GOV, "governance"):
        if gov.get("authority_scope") != "none" or gov.get("human_root_required") is not True:
            error("authority_escalation_denied")
        approvals = string_array(gov, "requires_approval_for", "requires_approval_for")
        invariants = string_array(gov, "constitutional_constraints", "constitutional_constraints")
        forbidden = string_array(gov, "forbidden_actions", "forbidden_actions")
        if not REQUIRED_GATES.issubset(set(approvals)):
            error("required_approval_gates_missing")
        if not REQUIRED_INVARIANTS.issubset(set(invariants)):
            error("nonfusion_and_memory_invariants_missing")
        if "self_authorization" not in forbidden:
            error("self_authorization_must_be_forbidden")

    memory = packet.get("memory")
    if fields(memory, MEMORY, "memory"):
        if not isinstance(memory.get("persistence"), str) or memory.get("persistence") not in {"ephemeral", "session", "archive"}:
            error("invalid_memory_persistence")
        if type(memory.get("replay_capable")) is not bool:
            error("replay_must_be_boolean")
        if memory.get("provenance_required") is not True or memory.get("native_memory_claim") is not False:
            error("memory_as_authority_denied")

    temperament = packet.get("temperament")
    if fields(temperament, TEMPERAMENT, "temperament"):
        for name in TEMPERAMENT:
            val = temperament.get(name)
            if type(val) not in (float, int) or not 0 <= val <= 1:
                error("invalid_temperament_" + name)

    inherit = packet.get("inheritance")
    if fields(inherit, INHERITANCE, "inheritance"):
        attrs = string_array(inherit, "descriptive_traits", "descriptive_traits")
        if not set(attrs).issubset(DESCRIPTIVE_ALLOWED):
            error("permission_or_governance_inheritance_forbidden")
        if inherit.get("permissions_inherited") is not False or inherit.get("authority_inherited") is not False:
            error("no_inherited_permissions_or_authority")

    return {
        "disposition": "HOLD" if problems else "CANDIDATE_STRUCTURE_ONLY",
        "errors": sorted(set(problems)),
        "identity_verified": False,
        "source_rights_verified": False,
        "execution_permission_granted": False,
        "replay_identity_continuity_verified": False,
        "canon": False, "deployed": False
    }


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: python validate_agent_dna.py <candidate-profile.json>", file=sys.stderr)
        return 64
    try:
        result = inspect_profile(read_strict_json(Path(args[0]).read_bytes()))
    except (UnicodeError, OSError, ValueError) as exc:
        result = {"disposition": "HOLD", "errors": [str(exc)],
                  "identity_verified": False, "execution_permission_granted": False}
    print(json.dumps(result, indent=2))
    return 0 if result["disposition"] == "CANDIDATE_STRUCTURE_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
