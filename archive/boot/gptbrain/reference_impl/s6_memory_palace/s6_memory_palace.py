"""S6 Memory Palace reference scaffold.

Status: reference implementation, not canon.
Core rule: memory can inform action; memory cannot authorize action by itself.
"""

from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any


class Status(StrEnum):
    CANON = "CANON"
    CANDIDATE = "CANDIDATE"
    VARIANT = "VARIANT"
    SUPERSEDED = "SUPERSEDED"
    LINEAGE = "LINEAGE"
    DISPUTED = "DISPUTED"
    DREAM = "DREAM"
    PLAY = "PLAY"
    QUARANTINED = "QUARANTINED"


class Room(StrEnum):
    CONTINUITY_HALL = "continuity_hall"
    CANON_VAULT = "canon_vault"
    FAILURE_LEDGER_CHAPEL = "failure_ledger_chapel"
    COUNCIL_CHAMBER = "council_chamber"
    SIMULATION_FORGE = "simulation_forge"
    DREAM_ATRIUM = "dream_atrium"
    HUMAN_THREAD_GARDEN = "human_thread_garden"


@dataclass
class MemoryRecord:
    title: str
    summary: str
    room: Room
    status: Status = Status.CANDIDATE
    source: str = "unspecified"
    evidence_level: str = "unreviewed"
    source_url: str | None = None
    why_it_matters: str | None = None
    related_threads: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    next_action: str | None = None
    s10_decision: str = "pending"
    memory_id: str = field(default_factory=lambda: f"S6-MEM-{uuid.uuid4().hex[:12]}")
    date_recorded: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["room"] = self.room.value
        data["status"] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MemoryRecord:
        data = dict(data)
        data["room"] = Room(data["room"])
        data["status"] = Status(data["status"])
        return cls(**data)


class PermissionError(Exception):
    pass


class MemoryPalace:
    def __init__(self) -> None:
        self.records: list[MemoryRecord] = []
        self.audit_log: list[dict[str, Any]] = []

    def add(self, record: MemoryRecord) -> MemoryRecord:
        if record.status == Status.CANON and record.s10_decision != "ratified":
            raise PermissionError("CANON requires S10 ratification.")
        if record.room == Room.DREAM_ATRIUM and record.status not in {Status.DREAM, Status.CANDIDATE}:
            raise PermissionError("Dream outputs must remain DREAM or CANDIDATE until reviewed.")
        self.records.append(record)
        self._audit("add", record.memory_id, record.status.value)
        return record

    def search(self, query: str) -> list[MemoryRecord]:
        q = query.lower()
        return [
            r
            for r in self.records
            if q in r.title.lower() or q in r.summary.lower() or any(q in t.lower() for t in r.related_threads)
        ]

    def promote_to_canon(self, memory_id: str, *, s10_decision: str) -> MemoryRecord:
        if s10_decision != "ratified":
            raise PermissionError("Only explicit S10 ratification promotes canon.")
        record = self.get(memory_id)
        record.status = Status.CANON
        record.s10_decision = s10_decision
        self._audit("promote_to_canon", memory_id, "ratified")
        return record

    def get(self, memory_id: str) -> MemoryRecord:
        for record in self.records:
            if record.memory_id == memory_id:
                return record
        raise KeyError(memory_id)

    def boot_summary(self) -> dict[str, Any]:
        return {
            "active_threads": sorted({t for r in self.records for t in r.related_threads}),
            "open_decisions": [r.to_dict() for r in self.records if r.s10_decision == "pending"],
            "current_risks": sorted({risk for r in self.records for risk in r.risks}),
            "recommended_next_actions": [r.next_action for r in self.records if r.next_action],
        }

    def export_json(self, path: str | Path) -> None:
        payload = {
            "status": "REFERENCE_IMPLEMENTATION_NOT_CANON",
            "records": [r.to_dict() for r in self.records],
            "audit_log": self.audit_log,
        }
        Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @classmethod
    def import_json(cls, path: str | Path) -> MemoryPalace:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        palace = cls()
        palace.records = [MemoryRecord.from_dict(item) for item in payload.get("records", [])]
        palace.audit_log = payload.get("audit_log", [])
        return palace

    def _audit(self, action: str, memory_id: str, detail: str) -> None:
        self.audit_log.append(
            {
                "timestamp": datetime.now(UTC).isoformat(),
                "action": action,
                "memory_id": memory_id,
                "detail": detail,
            }
        )


def demo() -> None:
    palace = MemoryPalace()
    palace.add(
        MemoryRecord(
            title="Council communication norm",
            summary="Council transmissions should be open questions, not model-to-model instructions.",
            room=Room.COUNCIL_CHAMBER,
            status=Status.CANDIDATE,
            source="S10 direct statement",
            evidence_level="direct_user_statement",
            why_it_matters="Prevents model hierarchy and preserves human adjudication.",
            related_threads=["Council", "A2A", "Governance"],
            risks=["false hierarchy", "command language drift"],
            next_action="Use question-first packets.",
            s10_decision="adopted",
        )
    )
    palace.add(
        MemoryRecord(
            title="Dream outputs cannot auto-execute",
            summary="Dream/REM outputs can propose, but cannot mutate canon or execute real-world actions.",
            room=Room.DREAM_ATRIUM,
            status=Status.DREAM,
            source="S6 Dream Memory Palace variant",
            evidence_level="design_choice",
            related_threads=["Dream", "Circadian Protocol"],
            risks=["dream-output overpromotion"],
        )
    )
    print(json.dumps(palace.boot_summary(), indent=2))


if __name__ == "__main__":
    demo()
