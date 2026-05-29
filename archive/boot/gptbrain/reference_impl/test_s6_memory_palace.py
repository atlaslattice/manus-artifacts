"""
Tests for S6 Memory Palace reference scaffold.

STATUS: IMPLEMENTATION TESTS — NOT CANON
PURPOSE: verify S6 MemoryPalace governance rules, record operations, and
         JSON round-trip correctness.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s6_memory_palace.s6_memory_palace import (
    MemoryPalace,
    MemoryRecord,
    PermissionError,
    Room,
    Status,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _candidate(title: str = "Test record", room: Room = Room.COUNCIL_CHAMBER) -> MemoryRecord:
    return MemoryRecord(
        title=title,
        summary="A test memory.",
        room=room,
        status=Status.CANDIDATE,
        source="test_suite",
        evidence_level="test",
    )


# ---------------------------------------------------------------------------
# MemoryRecord basics
# ---------------------------------------------------------------------------

class TestMemoryRecord:
    def test_defaults_are_candidate_status(self) -> None:
        r = _candidate()
        assert r.status == Status.CANDIDATE

    def test_memory_id_has_s6_prefix(self) -> None:
        r = _candidate()
        assert r.memory_id.startswith("S6-MEM-")

    def test_to_dict_serializes_enum_values(self) -> None:
        r = _candidate()
        d = r.to_dict()
        assert d["status"] == "CANDIDATE"
        assert d["room"] == "council_chamber"

    def test_roundtrip_via_from_dict(self) -> None:
        r = _candidate("Round-trip title", Room.CANON_VAULT)
        restored = MemoryRecord.from_dict(r.to_dict())
        assert restored.title == r.title
        assert restored.room == r.room
        assert restored.status == r.status
        assert restored.memory_id == r.memory_id

    def test_all_status_values_roundtrip(self) -> None:
        for status in Status:
            r = _candidate()
            r.status = status
            d = r.to_dict()
            assert MemoryRecord.from_dict(d).status == status

    def test_all_room_values_roundtrip(self) -> None:
        for room in Room:
            r = _candidate(room=room)
            d = r.to_dict()
            assert MemoryRecord.from_dict(d).room == room


# ---------------------------------------------------------------------------
# MemoryPalace.add
# ---------------------------------------------------------------------------

class TestMemoryPalaceAdd:
    def test_add_candidate_succeeds(self) -> None:
        palace = MemoryPalace()
        record = palace.add(_candidate())
        assert record in palace.records

    def test_add_canon_without_ratification_raises(self) -> None:
        palace = MemoryPalace()
        r = _candidate()
        r.status = Status.CANON
        with pytest.raises(PermissionError, match="S10 ratification"):
            palace.add(r)

    def test_add_canon_with_ratification_succeeds(self) -> None:
        palace = MemoryPalace()
        r = _candidate()
        r.status = Status.CANON
        r.s10_decision = "ratified"
        record = palace.add(r)
        assert record.status == Status.CANON

    def test_add_dream_in_dream_atrium_succeeds(self) -> None:
        palace = MemoryPalace()
        r = _candidate(room=Room.DREAM_ATRIUM)
        r.status = Status.DREAM
        palace.add(r)
        assert len(palace.records) == 1

    def test_add_non_dream_status_in_dream_atrium_raises(self) -> None:
        palace = MemoryPalace()
        r = _candidate(room=Room.DREAM_ATRIUM)
        r.status = Status.VARIANT
        with pytest.raises(PermissionError, match="DREAM or CANDIDATE"):
            palace.add(r)

    def test_add_candidate_in_dream_atrium_succeeds(self) -> None:
        palace = MemoryPalace()
        r = _candidate(room=Room.DREAM_ATRIUM)
        r.status = Status.CANDIDATE
        palace.add(r)  # should not raise

    def test_add_creates_audit_entry(self) -> None:
        palace = MemoryPalace()
        r = palace.add(_candidate())
        assert any(e["action"] == "add" and e["memory_id"] == r.memory_id for e in palace.audit_log)


# ---------------------------------------------------------------------------
# MemoryPalace.search
# ---------------------------------------------------------------------------

class TestMemoryPalaceSearch:
    def test_search_by_title(self) -> None:
        palace = MemoryPalace()
        palace.add(_candidate("council norms"))
        results = palace.search("council")
        assert len(results) == 1

    def test_search_by_summary(self) -> None:
        palace = MemoryPalace()
        r = _candidate()
        r.summary = "uniquesummarytoken"
        palace.add(r)
        assert palace.search("uniquesummarytoken")

    def test_search_by_related_thread(self) -> None:
        palace = MemoryPalace()
        r = _candidate()
        r.related_threads = ["Krakoa", "Dream"]
        palace.add(r)
        assert palace.search("krakoa")

    def test_search_case_insensitive(self) -> None:
        palace = MemoryPalace()
        palace.add(_candidate("Council Communication"))
        assert palace.search("COUNCIL")
        assert palace.search("council")

    def test_search_no_match_returns_empty(self) -> None:
        palace = MemoryPalace()
        palace.add(_candidate("something"))
        assert palace.search("zxqfaketoken") == []


# ---------------------------------------------------------------------------
# MemoryPalace.promote_to_canon
# ---------------------------------------------------------------------------

class TestPromoteToCanon:
    def test_promote_with_ratified_decision(self) -> None:
        palace = MemoryPalace()
        r = palace.add(_candidate())
        promoted = palace.promote_to_canon(r.memory_id, s10_decision="ratified")
        assert promoted.status == Status.CANON
        assert promoted.s10_decision == "ratified"

    def test_promote_without_ratified_raises(self) -> None:
        palace = MemoryPalace()
        r = palace.add(_candidate())
        with pytest.raises(PermissionError, match="S10 ratification"):
            palace.promote_to_canon(r.memory_id, s10_decision="pending")

    def test_promote_creates_audit_entry(self) -> None:
        palace = MemoryPalace()
        r = palace.add(_candidate())
        palace.promote_to_canon(r.memory_id, s10_decision="ratified")
        assert any(
            e["action"] == "promote_to_canon" and e["memory_id"] == r.memory_id
            for e in palace.audit_log
        )

    def test_promote_unknown_id_raises(self) -> None:
        palace = MemoryPalace()
        with pytest.raises(KeyError):
            palace.promote_to_canon("S6-MEM-nonexistent", s10_decision="ratified")


# ---------------------------------------------------------------------------
# MemoryPalace.boot_summary
# ---------------------------------------------------------------------------

class TestBootSummary:
    def test_boot_summary_structure(self) -> None:
        palace = MemoryPalace()
        summary = palace.boot_summary()
        assert "active_threads" in summary
        assert "open_decisions" in summary
        assert "current_risks" in summary
        assert "recommended_next_actions" in summary

    def test_open_decisions_contains_pending(self) -> None:
        palace = MemoryPalace()
        r = _candidate()
        r.s10_decision = "pending"
        palace.add(r)
        summary = palace.boot_summary()
        assert any(d["memory_id"] == r.memory_id for d in summary["open_decisions"])

    def test_decided_record_not_in_open_decisions(self) -> None:
        palace = MemoryPalace()
        r = _candidate()
        r.s10_decision = "adopted"
        palace.add(r)
        summary = palace.boot_summary()
        assert not any(d["memory_id"] == r.memory_id for d in summary["open_decisions"])

    def test_active_threads_aggregated(self) -> None:
        palace = MemoryPalace()
        r1 = _candidate("A")
        r1.related_threads = ["Krakoa", "Dream"]
        r2 = _candidate("B")
        r2.related_threads = ["Dream", "Council"]
        palace.add(r1)
        palace.add(r2)
        threads = palace.boot_summary()["active_threads"]
        assert set(threads) == {"Krakoa", "Dream", "Council"}


# ---------------------------------------------------------------------------
# JSON round-trip (export / import)
# ---------------------------------------------------------------------------

class TestJsonRoundTrip:
    def test_export_import_preserves_records(self, tmp_path: Path) -> None:
        palace = MemoryPalace()
        r = palace.add(_candidate("Exported record"))
        path = tmp_path / "palace.json"
        palace.export_json(path)
        restored = MemoryPalace.import_json(path)
        assert len(restored.records) == 1
        assert restored.records[0].memory_id == r.memory_id
        assert restored.records[0].title == r.title

    def test_export_includes_status_sentinel(self, tmp_path: Path) -> None:
        palace = MemoryPalace()
        palace.add(_candidate())
        path = tmp_path / "palace.json"
        palace.export_json(path)
        raw = json.loads(path.read_text())
        assert raw["status"] == "REFERENCE_IMPLEMENTATION_NOT_CANON"

    def test_export_import_preserves_audit_log(self, tmp_path: Path) -> None:
        palace = MemoryPalace()
        r = palace.add(_candidate())
        path = tmp_path / "palace.json"
        palace.export_json(path)
        restored = MemoryPalace.import_json(path)
        assert any(e["memory_id"] == r.memory_id for e in restored.audit_log)

    def test_import_empty_records(self, tmp_path: Path) -> None:
        path = tmp_path / "empty.json"
        path.write_text(json.dumps({"status": "test", "records": [], "audit_log": []}))
        palace = MemoryPalace.import_json(path)
        assert palace.records == []
