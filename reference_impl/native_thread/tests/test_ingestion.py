"""
Tests for Native Thread Ingestion
NOT CANON — NOT DEPLOYABLE — reference implementation only
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from ingestion import (
    NativeThreadPacket, validate_packet, check_false_completeness,
    compute_strongest_safe_claim, ValidationError, FalseCompletenessError,
)


def make_valid_packet(**kwargs) -> NativeThreadPacket:
    defaults = dict(
        packet_id="pkt-001",
        seat_name="LucernaBrain",
        model_surface="O_AI",
        source_thread_label="Test Thread 2026-05-26",
        thread_time_range={"start": "2026-05-26T10:00:00Z", "end": "2026-05-26T12:00:00Z", "timezone": "UTC"},
        raw_export_status="full_raw",
        access_scope={"visible_sources": ["test"], "unavailable_sources": [], "assumed_context": []},
        strongest_safe_claim="Thread processed. Full raw available.",
    )
    defaults.update(kwargs)
    return NativeThreadPacket(**defaults)


class TestValidation:
    def test_valid_full_raw_packet(self):
        packet = make_valid_packet()
        errors = validate_packet(packet)
        assert errors == []

    def test_missing_raw_export_status_fails(self):
        packet = make_valid_packet(raw_export_status="")
        errors = validate_packet(packet)
        assert any("NT-VAL-001" in e for e in errors)

    def test_missing_thread_time_range_fails(self):
        packet = make_valid_packet(thread_time_range={})
        errors = validate_packet(packet)
        assert any("NT-VAL-002" in e for e in errors)

    def test_missing_access_scope_fails(self):
        packet = make_valid_packet(access_scope={})
        errors = validate_packet(packet)
        # Missing unavailable_sources and assumed_context
        assert any("NT-VAL-006" in e for e in errors)
        assert any("NT-VAL-007" in e for e in errors)

    def test_summary_only_without_caveat_warns(self):
        packet = make_valid_packet(
            raw_export_status="summary_only",
            strongest_safe_claim="Thread produced synthesis."  # No caveat!
        )
        errors = validate_packet(packet)
        assert any("NT-VAL-004" in e for e in errors)

    def test_summary_only_with_caveat_passes(self):
        packet = make_valid_packet(
            raw_export_status="summary_only",
            strongest_safe_claim="Thread produced synthesis. [CAVEAT: summary only; raw unavailable]"
        )
        errors = validate_packet(packet)
        assert not any("NT-VAL-004" in e for e in errors)


class TestFalseCompleteness:
    def test_summary_only_high_confidence_claim_fails(self):
        packet = make_valid_packet(
            raw_export_status="summary_only",
            strongest_safe_claim="[CAVEAT] summary only",
            claims_extracted=[
                {"claim_text": "The system is working", "confidence": "high"}
            ]
        )
        with pytest.raises(FalseCompletenessError):
            check_false_completeness(packet)

    def test_full_raw_high_confidence_claim_passes(self):
        packet = make_valid_packet(
            raw_export_status="full_raw",
            claims_extracted=[
                {"claim_text": "The system is working", "confidence": "high"}
            ]
        )
        check_false_completeness(packet)  # Should not raise


class TestStrongestSafeClaim:
    def test_full_raw_claim(self):
        packet = make_valid_packet(raw_export_status="full_raw")
        claim = compute_strongest_safe_claim(packet)
        assert "CAVEAT" not in claim
        assert "Full raw export available" in claim

    def test_summary_only_claim_has_caveat(self):
        packet = make_valid_packet(
            raw_export_status="summary_only",
            access_scope={"visible_sources": [], "unavailable_sources": ["raw transcript"], "assumed_context": []}
        )
        claim = compute_strongest_safe_claim(packet)
        assert "CAVEAT" in claim
        assert "summary only" in claim.lower() or "summary_only" in claim.lower()

    def test_unavailable_claim_has_strong_caveat(self):
        packet = make_valid_packet(raw_export_status="unavailable")
        claim = compute_strongest_safe_claim(packet)
        assert "CAVEAT" in claim
        assert "unavailable" in claim.lower()
