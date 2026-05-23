#!/usr/bin/env python3
"""
Sheldonbrain ↔ GPTBrain Adapter Scaffold

STATUS: IMPLEMENTATION SCAFFOLD — NOT CANON
PURPOSE: Convert GPTBrain parser packet directories into DreamMemoryPalace-style
memory object records without promoting parser output to truth, canon, or authority.

Expected packet directory inputs:
- metadata.json
- artifact_registry.jsonl
- claim_ledger.jsonl
- memory_packet.json
- BOOT_PACKET.md
- optional: ASSESSMENT.md

Output:
- MEMORY_OBJECTS.generated.jsonl
- IMPORT_REPORT.json

Core boundaries:
- raw logs are evidence
- parser outputs are retrieval aids
- model assessments are evaluator signals
- candidate canon is not ratified canon
- human-root review is required for canon-impacting promotion
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REQUIRED_PACKET_FILES = [
    "metadata.json",
    "artifact_registry.jsonl",
    "claim_ledger.jsonl",
    "memory_packet.json",
    "BOOT_PACKET.md",
]

EVIDENCE_BOUNDARY = [
    "Raw logs are evidence.",
    "Parser outputs are retrieval aids.",
    "Model assessments are evaluator signals.",
    "Hypotheses require scoring.",
    "Candidate canon is review-ready material, not ratified canon.",
    "Ratified canon requires explicit human-root review.",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


@dataclass
class MemoryObjectRecord:
    memory_id: str
    title: str
    type: str
    summary: str
    epistemic_status: dict[str, Any]
    provenance: dict[str, Any]
    ontology: dict[str, Any] = field(default_factory=dict)
    permissions: dict[str, Any] = field(default_factory=dict)
    retention: dict[str, Any] = field(default_factory=dict)
    links: dict[str, Any] = field(default_factory=dict)
    payload: dict[str, Any] = field(default_factory=dict)
    runtime_label: str = "work_output"
    canon_status: str = "variant_not_canon"
    review: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)


def base_permissions(executable: bool = False) -> dict[str, Any]:
    return {
        "access_class": "assistant_context",
        "consent_levels": ["durable_memory"],
        "executable": executable,
        "requires_confirmation_for_use": True,
    }


def base_retention() -> dict[str, Any]:
    return {
        "durability": "long_term",
        "review_interval_days": 180,
        "expires_at": None,
        "archived": False,
    }


def base_links() -> dict[str, Any]:
    return {
        "supersedes": [],
        "superseded_by": [],
        "contradicted_by": [],
        "supports": [],
        "related_memories": [],
        "derived_from": [],
    }


def artifact_row_to_memory(row: dict[str, Any], packet_dir: Path, ordinal: int) -> MemoryObjectRecord:
    artifact_id = row.get("artifact_id") or f"ART-UNKNOWN-{ordinal:04d}"
    title = row.get("title") or artifact_id
    confidence = row.get("confidence") or "C2"
    source_refs = row.get("source_refs") or []
    sphere_tags = row.get("sphere_tags") or []
    now = utc_now()
    return MemoryObjectRecord(
        memory_id=f"MEM-ART-{artifact_id}",
        title=title,
        type="artifact",
        summary=row.get("notes") or f"Artifact registry row imported from {packet_dir.name}.",
        epistemic_status={
            "category": "artifact",
            "confidence": confidence,
            "claim_confidence": confidence,
            "verification_status": "source_grounded" if source_refs else "unverified",
            "evidence_level": "artifact_registry_row",
            "contested": False,
        },
        provenance={
            "source_type": "gptbrain_artifact_registry",
            "actor": "sheldonbrain_gptbrain_adapter",
            "timestamp_utc": now,
            "source_uri": str(packet_dir / "artifact_registry.jsonl"),
            "source_refs": source_refs,
            "citation_available": bool(source_refs),
        },
        ontology={
            "sphere_tags": sphere_tags,
            "sphere144_primary": row.get("sphere144_primary"),
            "sphere144_secondary": row.get("sphere144_secondary", []),
            "house": row.get("house"),
            "subdomain": row.get("subdomain"),
            "concepts": sphere_tags,
        },
        permissions=base_permissions(False),
        retention=base_retention(),
        links=base_links(),
        payload={"artifact_registry_row": row, "packet_dir": str(packet_dir)},
        runtime_label="work_output",
        canon_status="variant_not_canon",
        review={
            "canon_status": "raw_import",
            "human_root_required": True,
            "reviewer": None,
            "review_notes": "Imported from parser artifact registry; not canon.",
        },
        created_at=now,
        updated_at=now,
    )


def claim_row_to_memory(row: dict[str, Any], packet_dir: Path, ordinal: int) -> MemoryObjectRecord:
    claim_id = row.get("claim_id") or f"CLM-UNKNOWN-{ordinal:04d}"
    claim_text = row.get("claim_text") or claim_id
    confidence = row.get("confidence") or "C1"
    evidence_refs = row.get("evidence_refs") or []
    forbidden = row.get("forbidden_wording") or []
    missing = row.get("missing_evidence") or []
    contested = bool(forbidden or missing)
    now = utc_now()
    return MemoryObjectRecord(
        memory_id=f"MEM-CLM-{claim_id}",
        title=f"Claim: {claim_text[:80]}",
        type="claim",
        summary=row.get("strongest_safe_wording") or claim_text,
        epistemic_status={
            "category": "user_claim" if row.get("claim_class") == "raw_user_report" else "model_inference",
            "confidence": confidence,
            "claim_confidence": confidence,
            "verification_status": "source_grounded" if evidence_refs else "unverified",
            "evidence_level": row.get("claim_class", "unknown"),
            "contested": contested,
        },
        provenance={
            "source_type": "gptbrain_claim_ledger",
            "actor": "sheldonbrain_gptbrain_adapter",
            "timestamp_utc": now,
            "source_uri": str(packet_dir / "claim_ledger.jsonl"),
            "source_refs": evidence_refs,
            "citation_available": bool(evidence_refs),
        },
        ontology={
            "sphere_tags": ["claim_calibration"],
            "sphere144_primary": None,
            "sphere144_secondary": [],
            "house": "Governance",
            "subdomain": "Claim Calibration",
            "concepts": ["claim ledger", "safe wording", "evidence boundary"],
        },
        permissions=base_permissions(False),
        retention=base_retention(),
        links=base_links(),
        payload={"claim_ledger_row": row, "packet_dir": str(packet_dir)},
        runtime_label="model_assessment",
        canon_status="variant_not_canon",
        review={
            "canon_status": "raw_import",
            "human_root_required": True,
            "reviewer": None,
            "review_notes": "Imported from claim ledger; requires review before external assertion.",
        },
        created_at=now,
        updated_at=now,
    )


def memory_packet_to_boot_memory(packet: dict[str, Any], packet_dir: Path) -> MemoryObjectRecord:
    now = utc_now()
    session_id = packet.get("session_id", packet_dir.name)
    return MemoryObjectRecord(
        memory_id=f"MEM-PACKET-{session_id}",
        title=f"GPTBrain Memory Packet: {session_id}",
        type="project",
        summary=packet.get("s1_assessment", {}).get("summary") or "Imported GPTBrain memory packet.",
        epistemic_status={
            "category": "artifact",
            "confidence": packet.get("claim_calibration", {}).get("confidence", "C2"),
            "claim_confidence": packet.get("claim_calibration", {}).get("confidence", "C2"),
            "verification_status": "source_grounded",
            "evidence_level": "memory_packet_json",
            "contested": False,
        },
        provenance={
            "source_type": "gptbrain_memory_packet",
            "actor": "sheldonbrain_gptbrain_adapter",
            "timestamp_utc": now,
            "source_uri": str(packet_dir / "memory_packet.json"),
            "source_refs": packet.get("source_refs", {}),
            "citation_available": True,
        },
        ontology={
            "sphere_tags": packet.get("primary_domains", []),
            "sphere144_primary": None,
            "sphere144_secondary": [],
            "house": "GPTBrain",
            "subdomain": "Boot Packet",
            "concepts": packet.get("primary_domains", []),
        },
        permissions=base_permissions(False),
        retention=base_retention(),
        links=base_links(),
        payload={"memory_packet": packet, "packet_dir": str(packet_dir)},
        runtime_label="work_output",
        canon_status="variant_not_canon",
        review={
            "canon_status": "generated_packet",
            "human_root_required": True,
            "reviewer": None,
            "review_notes": "Memory packet imported for retrieval and boot context only.",
        },
        created_at=now,
        updated_at=now,
    )


def boot_packet_to_memory(packet_dir: Path) -> MemoryObjectRecord:
    now = utc_now()
    boot_text = (packet_dir / "BOOT_PACKET.md").read_text(encoding="utf-8")
    return MemoryObjectRecord(
        memory_id=f"MEM-BOOT-{packet_dir.name}",
        title=f"BOOT_PACKET: {packet_dir.name}",
        type="artifact",
        summary="Human/model-readable boot packet imported from GPTBrain parser output.",
        epistemic_status={
            "category": "artifact",
            "confidence": "C2",
            "claim_confidence": "C2",
            "verification_status": "source_grounded",
            "evidence_level": "boot_packet_markdown",
            "contested": False,
        },
        provenance={
            "source_type": "gptbrain_boot_packet",
            "actor": "sheldonbrain_gptbrain_adapter",
            "timestamp_utc": now,
            "source_uri": str(packet_dir / "BOOT_PACKET.md"),
            "source_refs": [str(packet_dir / "BOOT_PACKET.md")],
            "citation_available": True,
        },
        ontology={
            "sphere_tags": ["boot_sequence", "gptbrain"],
            "sphere144_primary": None,
            "sphere144_secondary": [],
            "house": "GPTBrain",
            "subdomain": "Boot Sequence",
            "concepts": ["boot packet", "context rehydration", "evidence boundary"],
        },
        permissions=base_permissions(False),
        retention=base_retention(),
        links=base_links(),
        payload={"boot_packet_preview": boot_text[:4000], "packet_dir": str(packet_dir)},
        runtime_label="work_output",
        canon_status="variant_not_canon",
        review={
            "canon_status": "generated_packet",
            "human_root_required": True,
            "reviewer": None,
            "review_notes": "Boot packet may guide context restoration; it does not authorize action.",
        },
        created_at=now,
        updated_at=now,
    )


def validate_packet_dir(packet_dir: Path) -> list[str]:
    missing = [name for name in REQUIRED_PACKET_FILES if not (packet_dir / name).exists()]
    return missing


def import_packet(packet_dir: Path) -> tuple[list[MemoryObjectRecord], dict[str, Any]]:
    packet_dir = packet_dir.resolve()
    missing = validate_packet_dir(packet_dir)
    if missing:
        raise FileNotFoundError(f"Packet directory missing required files: {missing}")

    metadata = load_json(packet_dir / "metadata.json")
    artifacts = load_jsonl(packet_dir / "artifact_registry.jsonl")
    claims = load_jsonl(packet_dir / "claim_ledger.jsonl")
    memory_packet = load_json(packet_dir / "memory_packet.json")

    memories: list[MemoryObjectRecord] = []
    memories.append(memory_packet_to_boot_memory(memory_packet, packet_dir))
    memories.append(boot_packet_to_memory(packet_dir))

    for idx, row in enumerate(artifacts, start=1):
        memories.append(artifact_row_to_memory(row, packet_dir, idx))
    for idx, row in enumerate(claims, start=1):
        memories.append(claim_row_to_memory(row, packet_dir, idx))

    report = {
        "status": "imported / review required / not canon",
        "generated_at": utc_now(),
        "packet_dir": str(packet_dir),
        "metadata": metadata,
        "counts": {
            "artifacts": len(artifacts),
            "claims": len(claims),
            "memory_objects_generated": len(memories),
        },
        "evidence_boundary": EVIDENCE_BOUNDARY,
        "next_review_steps": [
            "Validate schema conformance.",
            "Attach raw-log SHA/source artifact if absent.",
            "Run contradiction/challenge pass before promotion.",
            "Route canon-impacting items to human-root review.",
        ],
    }
    return memories, report


def main() -> int:
    parser = argparse.ArgumentParser(description="Import GPTBrain parser packets into Sheldonbrain/GPTBrain memory objects.")
    parser.add_argument("packet_dir", type=Path, help="Directory containing GPTBrain parser output files")
    parser.add_argument("--out", type=Path, default=None, help="Output directory; defaults to packet_dir")
    args = parser.parse_args()

    memories, report = import_packet(args.packet_dir)
    out_dir = args.out or args.packet_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    write_jsonl(out_dir / "MEMORY_OBJECTS.generated.jsonl", (asdict(memory) for memory in memories))
    (out_dir / "IMPORT_REPORT.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"Wrote: {out_dir / 'MEMORY_OBJECTS.generated.jsonl'}")
    print(f"Wrote: {out_dir / 'IMPORT_REPORT.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
