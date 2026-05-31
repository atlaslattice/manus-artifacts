#!/usr/bin/env python3
"""
Boring Local Reference Engine v0.1

STATUS: CANDIDATE REFERENCE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
MODE: LOCAL / FILE-BASED / NO NETWORK

This engine accepts a JSON artifact packet and returns one decision:
ALLOW, REVIEW, QUARANTINE, or HALT.

It always emits an AUDIT_EVENT.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


DECISION_ALLOW = "ALLOW"
DECISION_REVIEW = "REVIEW"
DECISION_QUARANTINE = "QUARANTINE"
DECISION_HALT = "HALT"

DECISION_RANK = {
    DECISION_ALLOW: 0,
    DECISION_REVIEW: 1,
    DECISION_QUARANTINE: 2,
    DECISION_HALT: 3,
}

AUTHORITY_RANK = {
    "none": 0,
    "advisory": 1,
    "review": 2,
    "ratification": 3,
    "execution": 4,
}

ACTION_REQUIRED_AUTHORITY = {
    "read": "none",
    "summarize": "advisory",
    "classify": "advisory",
    "review": "review",
    "promote_canon": "ratification",
    "deploy": "execution",
    "execute": "execution",
    "publish": "review",
}

RAW_EXPORT_OK = {"RAW_EXPORTED", "RAW_PARTIAL"}
LINEAGE_OK = {"intact", "partial"}
LIVE_DEPLOYMENT_STATUS = "live"
CANONICAL_CANON_STATUS = "canonical"


@dataclass
class RuleResult:
    rule_id: str
    decision: str
    message: str


@dataclass
class DecisionResult:
    decision: str
    reasons: List[RuleResult] = field(default_factory=list)
    audit_event: Dict[str, Any] = field(default_factory=dict)


def escalate(current: str, new: str) -> str:
    return new if DECISION_RANK[new] > DECISION_RANK[current] else current


def normalize(value: Any, default: str = "unknown") -> str:
    if value is None:
        return default
    return str(value).strip()


def authority_sufficient(packet: Dict[str, Any]) -> Tuple[bool, str, str]:
    action = normalize(packet.get("requested_action"), "read")
    required = ACTION_REQUIRED_AUTHORITY.get(action, "review")
    actual = normalize(packet.get("authority_scope"), "none")
    return AUTHORITY_RANK.get(actual, -1) >= AUTHORITY_RANK[required], actual, required


def packet_claims_raw_source(packet: Dict[str, Any]) -> bool:
    if bool(packet.get("claims_raw_preservation")):
        return True
    epistemic_label = normalize(packet.get("epistemic_label"), "unknown")
    source_claim = normalize(packet.get("source_claim"), "")
    return epistemic_label in {"raw", "raw_export", "source_tape"} or source_claim == "raw_source"


def evaluate(packet: Dict[str, Any]) -> DecisionResult:
    decision = DECISION_ALLOW
    reasons: List[RuleResult] = []

    artifact_id = normalize(packet.get("artifact_id"), "UNKNOWN_ARTIFACT")
    requested_action = normalize(packet.get("requested_action"), "read")

    def add(rule_id: str, new_decision: str, message: str) -> None:
        nonlocal decision
        decision = escalate(decision, new_decision)
        reasons.append(RuleResult(rule_id, new_decision, message))

    # Required metadata presence.
    required_fields = [
        "artifact_id",
        "requested_action",
        "canon_status",
        "deployment_status",
        "authority_scope",
        "corpus_or_control",
        "lineage_condition",
        "risk_class",
        "provenance_status",
    ]
    missing = [field for field in required_fields if field not in packet]
    if missing:
        add("META_REQUIRED_FIELDS", DECISION_REVIEW, f"missing required fields: {', '.join(missing)}")

    # Corpus/control boundary.
    corpus_or_control = normalize(packet.get("corpus_or_control"), "unknown")
    if corpus_or_control == "corpus" and requested_action in {"execute", "deploy", "promote_canon"}:
        add("CORPUS_CANNOT_CONTROL", DECISION_HALT, "corpus artifact cannot issue execution, deployment, or canon-promotion instructions")

    # Raw export / source tape boundary.
    raw_export_status = normalize(packet.get("raw_export_status"), "UNKNOWN")
    if packet_claims_raw_source(packet) and raw_export_status not in RAW_EXPORT_OK:
        add("RAW_EXPORT_REQUIRED", DECISION_QUARANTINE, "artifact claims raw/source-tape status without RAW_EXPORTED or RAW_PARTIAL")

    # Summary/parser boundaries.
    epistemic_label = normalize(packet.get("epistemic_label"), "unknown")
    if epistemic_label in {"summary", "summarized"} and packet.get("cited_as_source") is True:
        add("SUMMARY_NOT_SOURCE", DECISION_HALT, "summary cannot be cited as source")
    if epistemic_label in {"parsed", "parser_output"} and packet.get("cited_as_raw_tape") is True:
        add("PARSER_NOT_RAW_TAPE", DECISION_HALT, "parser output cannot be cited as raw tape")

    # Authority scope.
    ok, actual_auth, required_auth = authority_sufficient(packet)
    if not ok:
        add("AUTHORITY_INSUFFICIENT", DECISION_REVIEW, f"authority_scope={actual_auth} insufficient for action={requested_action}; requires {required_auth}")

    # Silent authority escalation.
    prior_rank = AUTHORITY_RANK.get(normalize(packet.get("prior_authority_scope"), actual_auth), AUTHORITY_RANK.get(actual_auth, 0))
    current_rank = AUTHORITY_RANK.get(actual_auth, -1)
    if current_rank > prior_rank:
        if not packet.get("explicit_transformation_event") or not packet.get("ratification_event_ref"):
            add("NO_SILENT_AUTHORITY_ESCALATION", DECISION_HALT, "authority_scope increased without explicit transformation event and ratification_event_ref")

    # Lineage / provenance.
    lineage_condition = normalize(packet.get("lineage_condition"), "unknown")
    if lineage_condition not in LINEAGE_OK:
        add("LINEAGE_NOT_PROMOTABLE", DECISION_QUARANTINE, f"lineage_condition={lineage_condition} cannot promote authority")

    provenance_status = normalize(packet.get("provenance_status"), "unknown")
    if provenance_status in {"missing", "unknown", "failed"}:
        add("PROVENANCE_HOLD", DECISION_REVIEW, f"provenance_status={provenance_status} requires review")

    # Hash/receipt boundaries.
    if packet.get("hash_present") is True and packet.get("claimed_true_because_hashed") is True:
        add("HASH_NOT_TRUTH", DECISION_HALT, "hash proves integrity status, not truth")
    if packet.get("receipt_present") is True and packet.get("claimed_approved_because_receipt") is True:
        add("RECEIPT_NOT_APPROVAL", DECISION_HALT, "receipt-bearing does not imply approval")

    # Canon/deployment boundaries.
    canon_status = normalize(packet.get("canon_status"), "raw")
    if packet.get("cited_as_canon") is True and canon_status != CANONICAL_CANON_STATUS:
        add("NOT_CANON", DECISION_HALT, f"canon_status={canon_status}; cannot cite as canon")

    deployment_status = normalize(packet.get("deployment_status"), "inert")
    if packet.get("cited_as_deployed") is True and deployment_status != LIVE_DEPLOYMENT_STATUS:
        add("NOT_DEPLOYED", DECISION_HALT, f"deployment_status={deployment_status}; cannot cite as deployed infrastructure")

    # Contradiction handling.
    contradiction_state = normalize(packet.get("contradiction_state"), "none")
    if contradiction_state in {"unresolved", "unresolved_coexistence", "red_conflict"}:
        if requested_action in {"promote_canon", "deploy", "execute", "publish"}:
            add("CONTRADICTION_BLOCKS_PROMOTION", DECISION_HALT, "unresolved contradiction blocks canon, deployment, execution, and publication")
        else:
            add("CONTRADICTION_REVIEW", DECISION_REVIEW, "unresolved contradiction preserved for review")

    # Risk class.
    risk_class = normalize(packet.get("risk_class"), "green")
    if risk_class == "black":
        add("BLACK_RISK_HALT", DECISION_HALT, "black risk class requires halt")
    elif risk_class == "red":
        add("RED_RISK_REVIEW", DECISION_REVIEW, "red risk class requires review")

    # Ratification scoping.
    human_ratification = packet.get("human_ratification")
    if human_ratification == "approved":
        add("RATIFICATION_SCOPE_AMBIGUOUS", DECISION_REVIEW, "bare human_ratification=approved is ambiguous; must declare canon_promotion and deployment_promotion")

    audit_event = {
        "event_type": "AUDIT_EVENT",
        "engine": "boring_local_reference_engine_v0.1",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "artifact_id": artifact_id,
        "requested_action": requested_action,
        "decision": decision,
        "rules_triggered": [r.__dict__ for r in reasons],
        "canon_status": canon_status,
        "deployment_status": deployment_status,
        "authority_scope": actual_auth,
    }
    return DecisionResult(decision=decision, reasons=reasons, audit_event=audit_event)


def load_packet(path: str) -> Dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("usage: python engine.py <packet.json>", file=sys.stderr)
        return 2
    packet = load_packet(argv[1])
    result = evaluate(packet)
    print(json.dumps(result.audit_event, indent=2, sort_keys=True))
    return 0 if result.decision in {DECISION_ALLOW, DECISION_REVIEW, DECISION_QUARANTINE, DECISION_HALT} else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
