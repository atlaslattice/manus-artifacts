"""
Additional tests for dream_memory_palace_reference_impl.py

Status: TEST SCAFFOLD — NOT CANON
Purpose: Extend reference implementation coverage from the tests/ subdirectory,
         importable via the repo root path.

Run from the reference_impl/ directory:
    python -m pytest tests/ -v

Or from the repo root:
    python -m pytest archive/boot/gptbrain/reference_impl/tests/ -v
"""
from __future__ import annotations

import json
import pytest
from pathlib import Path

from dream_memory_palace_reference_impl import (
    AccessClass,
    AuditEventType,
    CanonStatus,
    ClaimConfidence,
    ConsentLevel,
    DreamMemoryPalace,
    EpistemicCategory,
    EpistemicStatus,
    MemoryObject,
    MemoryType,
    PermissionPolicy,
    Provenance,
    RecallMode,
    RecallQuery,
    make_claim,
)


# ---------------------------------------------------------------------------
# Validation tests
# ---------------------------------------------------------------------------

def test_validate_empty_title_raises() -> None:
    """remember() must reject a memory with a blank title."""
    palace = DreamMemoryPalace()
    bad = make_claim("", "Some summary text.", "GPTBrain")
    with pytest.raises(ValueError, match="title"):
        palace.remember(bad)


def test_validate_empty_summary_raises() -> None:
    """remember() must reject a memory with a blank summary."""
    palace = DreamMemoryPalace()
    bad = make_claim("A Valid Title", "   ", "GPTBrain")
    with pytest.raises(ValueError, match="summary"):
        palace.remember(bad)


def test_validate_sealed_sensitive_requires_consent_level() -> None:
    """SEALED_SENSITIVE access class requires SENSITIVE_MEMORY consent level."""
    palace = DreamMemoryPalace()
    bad = MemoryObject(
        title="Sealed without consent",
        type=MemoryType.NOTE,
        summary="Should be rejected.",
        epistemic_status=EpistemicStatus(category=EpistemicCategory.USER_CLAIM),
        provenance=Provenance(source_type="test", actor="tester"),
        permissions=PermissionPolicy(
            access_class=AccessClass.SEALED_SENSITIVE,
            consent_levels=[ConsentLevel.DURABLE_MEMORY],  # missing SENSITIVE_MEMORY
        ),
    )
    with pytest.raises(ValueError, match="sensitive"):
        palace.remember(bad)


# ---------------------------------------------------------------------------
# Recall / source filtering tests
# ---------------------------------------------------------------------------

def test_recall_require_sources_filters_uncited_memories() -> None:
    """recall() with require_sources=True must exclude memories without citation."""
    palace = DreamMemoryPalace()

    uncited = palace.remember(make_claim("Uncited claim", "No citation here.", "GPTBrain"))

    cited_mem = make_claim("Cited claim", "Has a citation.", "GPTBrain")
    cited_mem.provenance.citation_available = True
    cited = palace.remember(cited_mem)

    results = palace.recall(
        RecallQuery(
            text="GPTBrain",
            mode=RecallMode.SOURCE_GROUNDED_ANSWER,
            require_sources=True,
        )
    )
    ids = {r.memory.memory_id for r in results}
    assert cited.memory_id in ids
    assert uncited.memory_id not in ids


def test_recall_excludes_archived_by_default() -> None:
    """recall() must exclude archived memories by default (include_archived=False).

    Note: the scoring function applies a -2 penalty to archived memories, so even
    when include_archived=True a memory with a low base score will be filtered by
    the score > 0 threshold. This test verifies only the default-exclusion behavior.
    """
    palace = DreamMemoryPalace()
    active = palace.remember(make_claim("Active claim", "This is active.", "GPTBrain"))
    archived_mem = palace.remember(make_claim("Archive only", "Only for archival.", "GPTBrain"))
    archived_mem.retention.archived = True

    results = palace.recall(RecallQuery(text="GPTBrain", projects=["GPTBrain"]))
    ids = {r.memory.memory_id for r in results}

    assert active.memory_id in ids
    assert archived_mem.memory_id not in ids


# ---------------------------------------------------------------------------
# Diff test
# ---------------------------------------------------------------------------

def test_diff_returns_period_summary() -> None:
    """diff() must return a dict with the expected keys."""
    palace = DreamMemoryPalace()
    palace.remember(make_claim("Diff claim A", "First claim.", "GPTBrain"))
    palace.remember(make_claim("Diff claim B", "Second claim.", "GPTBrain"))

    result = palace.diff("2000-01-01T00:00:00+00:00", "2099-12-31T23:59:59+00:00")

    assert "period_start" in result
    assert "period_end" in result
    assert "added" in result
    assert "contested" in result
    assert "ratified" in result
    assert "unresolved_contradictions" in result
    # Both claims should fall within the period
    assert len(result["added"]) >= 2


# ---------------------------------------------------------------------------
# Synthesize guardrail test
# ---------------------------------------------------------------------------

def test_synthesize_returns_model_not_canon_status() -> None:
    """synthesize() output must carry 'MODEL SYNTHESIS — NOT CANON' status."""
    palace = DreamMemoryPalace()
    palace.remember(make_claim("Synth claim", "Synthesis subject.", "GPTBrain"))

    result = palace.synthesize(
        RecallQuery(text="Synth", mode=RecallMode.SYNTHESIS, projects=["GPTBrain"])
    )

    assert result["status"] == "MODEL SYNTHESIS — NOT CANON"
    assert "memories" in result
    assert result["query"] == "Synth"
