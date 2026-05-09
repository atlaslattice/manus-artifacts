#!/usr/bin/env python3
"""
GPTBrain S1 reference implementation scaffold.

STATUS: IMPLEMENTATION SCAFFOLD — NOT CANON
ISSUE: manus-artifacts#12

This module intentionally implements a tiny, auditable substrate:
- load JSONL ledgers
- filter claims and memories
- trace claims to evidence refs
- challenge overclaims
- diff registry snapshots
- synthesize current state from seed ledgers

It does not authorize action, ratify canon, or imply native model memory.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CLAIM_LEDGER = ROOT / "CLAIM_LEDGER.seed.jsonl"
ARTIFACT_REGISTRY = ROOT / "ARTIFACT_REGISTRY.seed.jsonl"
MEMORY_OBJECTS = ROOT / "MEMORY_OBJECTS.seed.jsonl"


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


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


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


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")


def dump(obj: Any) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True))


def find_one(rows: Iterable[dict[str, Any]], key: str, value: str) -> dict[str, Any] | None:
    for row in rows:
        if row.get(key) == value:
            return row
    return None


def text_matches(row: dict[str, Any], query: str) -> bool:
    haystack = json.dumps(row, sort_keys=True).lower()
    return query.lower() in haystack


def list_claims(confidence: str | None = None, review_status: str | None = None) -> list[dict[str, Any]]:
    claims = load_jsonl(CLAIM_LEDGER)
    if confidence:
        claims = [c for c in claims if c.get("confidence") == confidence]
    if review_status:
        claims = [c for c in claims if c.get("review_status") == review_status]
    return claims


def list_memories(query: str | None = None, memory_type: str | None = None) -> list[dict[str, Any]]:
    memories = load_jsonl(MEMORY_OBJECTS)
    if query:
        memories = [m for m in memories if text_matches(m, query)]
    if memory_type:
        memories = [m for m in memories if m.get("type") == memory_type]
    return memories


def remember(title: str, memory_type: str, summary: str, source: str, confidence: str = "C1") -> dict[str, Any]:
    rows = load_jsonl(MEMORY_OBJECTS)
    memory_id = f"S1-MEM-{datetime.now(timezone.utc).strftime('%Y-%m%d-%H%M%S')}-{len(rows)+1:04d}"
    now = utc_now()
    row = {
        "memory_id": memory_id,
        "title": title,
        "type": memory_type,
        "summary": summary,
        "epistemic_status": "user_claim" if source == "user_message" else "artifact",
        "confidence": confidence,
        "provenance": {
            "source_type": source,
            "source_refs": [],
            "sha256": None,
            "captured_at": now,
        },
        "ontology": {"sphere_tags": ["S144"], "primary_house": None, "secondary_houses": []},
        "permissions": {
            "access_class": "assistant_context",
            "consent_level": "implicit_context",
            "executable": False,
        },
        "retention": {"status": "active", "review_after": None},
        "links": {
            "related_memory_ids": [],
            "contradicts": [],
            "supports": [],
            "supersedes": [],
            "superseded_by": [],
        },
        "payload": {},
        "review": {
            "canon_status": "raw",
            "human_root_required": True,
            "reviewer": None,
            "review_notes": "Created by local reference implementation; not canon.",
        },
        "created_at": now,
        "updated_at": now,
    }
    append_jsonl(MEMORY_OBJECTS, row)
    return row


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


def trace_memory(memory_id: str) -> dict[str, Any]:
    memory = find_one(load_jsonl(MEMORY_OBJECTS), "memory_id", memory_id)
    if not memory:
        return {"memory_id": memory_id, "found": False}
    return {
        "memory_id": memory_id,
        "found": True,
        "title": memory.get("title"),
        "type": memory.get("type"),
        "confidence": memory.get("confidence"),
        "provenance": memory.get("provenance", {}),
        "permissions": memory.get("permissions", {}),
        "review": memory.get("review", {}),
        "links": memory.get("links", {}),
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


def synthesize(scope: str) -> dict[str, Any]:
    claims = load_jsonl(CLAIM_LEDGER)
    artifacts = load_jsonl(ARTIFACT_REGISTRY)
    memories = load_jsonl(MEMORY_OBJECTS)
    return {
        "scope": scope,
        "status": "implementation_scaffold_not_canon",
        "generated_at": utc_now(),
        "counts": {
            "claims": len(claims),
            "artifacts": len(artifacts),
            "memories": len(memories),
        },
        "guardrails": [
            "Memory can inform action; memory cannot authorize action by itself.",
            "Readable memory is not executable memory.",
            "Candidate canon is not ratified canon.",
            "Human-root review is required for ratified canon.",
        ],
        "next_actions": [
            "Patch canonical candidate to integrate Variant E directly.",
            "Add tests for claim challenge and memory trace behavior.",
            "Promote this scaffold only through issue-linked review.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="GPTBrain S1 scaffold CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    claims = sub.add_parser("claims")
    claims.add_argument("--confidence")
    claims.add_argument("--review-status")

    memories = sub.add_parser("memories")
    memories.add_argument("--query")
    memories.add_argument("--type")

    remember_cmd = sub.add_parser("remember")
    remember_cmd.add_argument("--title", required=True)
    remember_cmd.add_argument("--type", required=True)
    remember_cmd.add_argument("--summary", required=True)
    remember_cmd.add_argument("--source", default="manual_entry")
    remember_cmd.add_argument("--confidence", default="C1")

    trace = sub.add_parser("trace")
    trace.add_argument("--claim-id")
    trace.add_argument("--memory-id")

    challenge = sub.add_parser("challenge")
    challenge.add_argument("--claim-id", required=True)

    diff = sub.add_parser("diff")
    diff.add_argument("--old", required=True)
    diff.add_argument("--new", required=True)

    synth = sub.add_parser("synthesize")
    synth.add_argument("--scope", default="current_state")

    args = parser.parse_args()

    if args.command == "claims":
        dump(list_claims(confidence=args.confidence, review_status=args.review_status))
    elif args.command == "memories":
        dump(list_memories(query=args.query, memory_type=args.type))
    elif args.command == "remember":
        dump(remember(args.title, args.type, args.summary, args.source, args.confidence))
    elif args.command == "trace":
        if args.claim_id:
            dump(trace_claim(args.claim_id))
        elif args.memory_id:
            dump(trace_memory(args.memory_id))
        else:
            parser.error("trace requires --claim-id or --memory-id")
    elif args.command == "challenge":
        dump(challenge_claim(args.claim_id).to_dict())
    elif args.command == "diff":
        dump(diff_jsonl(Path(args.old), Path(args.new)))
    elif args.command == "synthesize":
        dump(synthesize(args.scope))
    else:
        parser.error(f"Unsupported command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
