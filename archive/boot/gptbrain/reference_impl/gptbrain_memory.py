#!/usr/bin/env python3
"""
GPTBrain S1 reference implementation scaffold.

STATUS: IMPLEMENTATION SCAFFOLD — NOT CANON
ISSUE: manus-artifacts#12

This module intentionally implements a tiny, auditable substrate:
- load JSONL ledgers
- filter claims
- trace claims to evidence refs
- challenge overclaims
- diff registry snapshots

It does not authorize action, ratify canon, or imply native model memory.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CLAIM_LEDGER = ROOT / "CLAIM_LEDGER.seed.jsonl"
ARTIFACT_REGISTRY = ROOT / "ARTIFACT_REGISTRY.seed.jsonl"


@dataclass(frozen=True)
class ChallengeReport:
    target_id: str
    status: str
    findings: list[str]
    required_next_steps: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_id": self.target_id,
            "status": self.status,
            "findings": self.findings,
            "required_next_steps": self.required_next_steps,
        }


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            rows.append(json.loads(stripped))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL in {path} line {line_no}: {exc}") from exc
    return rows


def dump(obj: Any) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True))


def find_one(rows: Iterable[dict[str, Any]], key: str, value: str) -> dict[str, Any] | None:
    for row in rows:
        if row.get(key) == value:
            return row
    return None


def list_claims(confidence: str | None = None, review_status: str | None = None) -> list[dict[str, Any]]:
    claims = load_jsonl(CLAIM_LEDGER)
    if confidence:
        claims = [c for c in claims if c.get("confidence") == confidence]
    if review_status:
        claims = [c for c in claims if c.get("review_status") == review_status]
    return claims


def trace_claim(claim_id: str) -> dict[str, Any]:
    claim = find_one(load_jsonl(CLAIM_LEDGER), "claim_id", claim_id)
    if not claim:
        return {"claim_id": claim_id, "found": False, "evidence_refs": []}
    return {
        "claim_id": claim_id,
        "found": True,
        "claim_text": claim.get("claim_text"),
        "claim_class": claim.get("claim_class"),
        "confidence": claim.get("confidence"),
        "evidence_refs": claim.get("evidence_refs", []),
        "missing_evidence": claim.get("missing_evidence", []),
        "strongest_safe_wording": claim.get("strongest_safe_wording"),
        "forbidden_wording": claim.get("forbidden_wording", []),
    }


def challenge_claim(claim_id: str) -> ChallengeReport:
    claim = find_one(load_jsonl(CLAIM_LEDGER), "claim_id", claim_id)
    if not claim:
        return ChallengeReport(
            target_id=claim_id,
            status="not_found",
            findings=["No claim record exists for this claim_id."],
            required_next_steps=["Create or locate a ClaimRecord before asserting the claim."],
        )

    findings: list[str] = []
    next_steps: list[str] = []

    confidence = claim.get("confidence")
    claim_class = claim.get("claim_class")
    review_status = claim.get("review_status")
    evidence_refs = claim.get("evidence_refs", [])
    missing_evidence = claim.get("missing_evidence", [])
    forbidden = claim.get("forbidden_wording", [])
    human_root_required = claim.get("human_root_required", True)

    if confidence in {"C0", "C0_UNSUPPORTED"}:
        findings.append("Claim is C0 and must not be asserted as fact.")
    if not evidence_refs:
        findings.append("Claim has no evidence_refs.")
        next_steps.append("Attach source artifact paths, issue refs, or citations.")
    if claim_class == "ratified_canon" and review_status != "ratified":
        findings.append("Claim class says ratified_canon but review_status is not ratified.")
    if claim_class == "ratified_canon" and human_root_required:
        findings.append("Ratified canon requires explicit human-root review completion.")
    if missing_evidence:
        findings.append("Claim has declared missing evidence.")
        next_steps.extend(str(item) for item in missing_evidence)
    if forbidden:
        findings.append("Claim includes forbidden wording boundaries that must be respected.")

    status = "pass_with_boundaries" if not findings else "needs_review"
    if not next_steps and findings:
        next_steps.append("Route to human-root review or claim calibration before promotion.")

    return ChallengeReport(
        target_id=claim_id,
        status=status,
        findings=findings or ["No blocking issue found in current seed record."],
        required_next_steps=next_steps,
    )


def index_by_id(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = row.get("artifact_id") or row.get("claim_id") or row.get("memory_id")
        if key:
            out[str(key)] = row
    return out


def diff_jsonl(old_path: Path, new_path: Path) -> dict[str, Any]:
    old = index_by_id(load_jsonl(old_path))
    new = index_by_id(load_jsonl(new_path))
    old_keys = set(old)
    new_keys = set(new)
    changed = sorted(k for k in old_keys & new_keys if old[k] != new[k])
    return {
        "old": str(old_path),
        "new": str(new_path),
        "added": sorted(new_keys - old_keys),
        "removed": sorted(old_keys - new_keys),
        "changed": changed,
        "unchanged_count": len((old_keys & new_keys) - set(changed)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="GPTBrain S1 scaffold CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    claims = sub.add_parser("claims")
    claims.add_argument("--confidence")
    claims.add_argument("--review-status")

    trace = sub.add_parser("trace")
    trace.add_argument("--claim-id", required=True)

    challenge = sub.add_parser("challenge")
    challenge.add_argument("--claim-id", required=True)

    diff = sub.add_parser("diff")
    diff.add_argument("--old", required=True)
    diff.add_argument("--new", required=True)

    args = parser.parse_args()

    if args.command == "claims":
        dump(list_claims(confidence=args.confidence, review_status=args.review_status))
    elif args.command == "trace":
        dump(trace_claim(args.claim_id))
    elif args.command == "challenge":
        dump(challenge_claim(args.claim_id).to_dict())
    elif args.command == "diff":
        dump(diff_jsonl(Path(args.old), Path(args.new)))
    else:
        parser.error(f"Unsupported command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
