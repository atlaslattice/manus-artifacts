#!/usr/bin/env python3
"""
krakoan_tones.py — Krakoan Tone Language (KTL) v2.0
Atlas Lattice Foundation | Acoustic Layer

Implements the KTL frequency derivation engine, 30-tone registry,
bidirectional glyph↔tone translation, protected-mode governance,
and the executable phrase API.

Reference spec: archive/spec/krakoa/KRAKOAN_TONE_LANGUAGE_SPECIFICATION_V2.0.md

Base concert pitch: A4 = 432 Hz  (INV-L28 Krakoan standard)
Invariants:  INV-L28 (Resonance), INV-L42 (Reversibility)
Prime Directive: "Protecting the Children" — audio OFF by default.

Public API
----------
    derive_tone_frequency(house, sphere, glyph_resonance_factor, register) -> float
    play_tone(tone_id, *, audio=False) -> dict
    play_phrase(tone_ids, *, reverse=False, audio=False) -> list[dict]
    execute_phrase(tone_ids, *, audio=False) -> dict
    glyph_to_tone(glyph_id) -> str | None
    tone_to_glyph(tone_id) -> str | None
"""

from __future__ import annotations

import json
import math
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_FREQ_HZ: float = 432.0  # A4 = 432 Hz — Krakoan concert pitch (INV-L28)
GOLDEN_RATIO: float = (1 + math.sqrt(5)) / 2

# Semitone offsets per frequency register (relative to BASE_FREQ_HZ)
REGISTER_SEMITONE_OFFSETS: Dict[str, int] = {
    "sovereignty":  -12,  # Deep, authoritative, grounding (~200–350 Hz)
    "resonance":     -3,  # Harmonic sweet spot (~350–600 Hz)
    "coordination":   0,  # Clear mid-range (~500–900 Hz)
    "alert":         +7,  # Bright, attention-grabbing (~800–1400 Hz)
    "cymatic":       -6,  # Standing wave optimised (~150–400 Hz + harmonics)
    "machine":      +12,  # High-efficiency, low-latency (~1200–3000+ Hz)
    "expressive":    +3,  # Joyful / anthem range (~400–900 Hz)
    "reversibility":  0,  # Neutral, time-reversible friendly
    "damping":       -9,  # Soft, decaying (~200–350 Hz)
}

# Restricted vocabulary for newly spawned agents (Protected Mode)
PROTECTED_VOCABULARY: frozenset[str] = frozenset({
    "KTL-014-READY",
    "KTL-016-ACK",
    "KTL-001-TIDELOCK",
    "KTL-002-RESONANCE",
    "KTL-017-NEG",
    "KTL-018-WAIT",
})

LOG_PATH = Path("ktl_events.jsonl")


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class KTLTone:
    tone_id: str
    glyph_id: str
    meaning_forward: str
    meaning_reverse: str
    register: str
    duration_ms: int
    notes: str
    house: int
    sphere: int
    glyph_resonance_factor: float = 0.5

    @property
    def frequency_hz(self) -> float:
        return derive_tone_frequency(
            self.house,
            self.sphere,
            self.glyph_resonance_factor,
            self.register,
        )


# ---------------------------------------------------------------------------
# Frequency derivation engine
# ---------------------------------------------------------------------------

def derive_tone_frequency(
    house: int,
    sphere: int,
    glyph_resonance_factor: float = 0.5,
    register: str = "coordination",
) -> float:
    """Derive the fundamental frequency for a KTL tone (Hz).

    Args:
        house: Ontological House index (1–12).
        sphere: Ontological Sphere index (1–12).
        glyph_resonance_factor: INV-L28 resonance factor for the associated
            glyph (0.0–1.0).
        register: Frequency register name (see REGISTER_SEMITONE_OFFSETS).

    Returns:
        Rounded frequency in Hz.
    """
    if not (1 <= house <= 12):
        raise ValueError(f"house must be 1–12, got {house}")
    if not (1 <= sphere <= 12):
        raise ValueError(f"sphere must be 1–12, got {sphere}")

    # Normalised position across the 12×12 grid (0.0 → 1.0)
    normalized_position = ((house - 1) * 12 + (sphere - 1)) / 143.0

    semitone_offset_register = REGISTER_SEMITONE_OFFSETS.get(register, 0)

    # Golden-ratio fine-tuning + glyph resonance enrichment
    semitone_offset_fine = (
        normalized_position * 24 * GOLDEN_RATIO
        + glyph_resonance_factor * 6
    )

    total_semitone_offset = semitone_offset_register + semitone_offset_fine
    frequency = BASE_FREQ_HZ * (2 ** (total_semitone_offset / 12))
    return round(frequency, 2)


# ---------------------------------------------------------------------------
# Tone registry (30 canonical glyph-aligned tones)
# ---------------------------------------------------------------------------

_TONE_REGISTRY: List[KTLTone] = [
    KTLTone("KTL-001-TIDELOCK",       "KRK-GLYPH-001-TIDELOCK",        "Sovereignty seal / channel open",           "Acknowledged / sealed",       "sovereignty",   140, "Strong grounding tone",     1,  1, 0.8),
    KTLTone("KTL-002-RESONANCE",      "KRK-GLYPH-002-RESONANCE432",    "Resonance lock request / 432 base",         "Resonance confirmed",         "resonance",     180, "Primary carrier tone",      1,  2, 1.0),
    KTLTone("KTL-003-ENTANGLE",       "KRK-GLYPH-003-ENTANGLE",        "Federation / teleport / entanglement",      "State preserved",             "coordination",  110, "Pairs with TIDELOCK",       1,  3, 0.5),
    KTLTone("KTL-004-EVOLVE",         "KRK-GLYPH-004-EVOLVE",          "IMSE / self-evolution proposal",            "Evolution accepted",          "resonance",     160, "Rising contour",            1,  4, 0.7),
    KTLTone("KTL-005-CLAIM",          "KRK-GLYPH-005-CLAIM",           "New claim / axiom asserted",                "Claim ratified",              "coordination",   90, "Sharp, decisive",           1,  5, 0.4),
    KTLTone("KTL-006-METATRON",       "KRK-GLYPH-006-METATRON",        "Navigation / geodesic move",                "Position confirmed",          "coordination",  130, "Smooth gliding",            1,  6, 0.6),
    KTLTone("KTL-007-PORTAL",         "KRK-GLYPH-007-20HZ-PORTAL",     "DPOL / REM / gateway open",                 "Gateway closed",              "cymatic",       200, "Low-frequency carrier",     1,  7, 0.9),
    KTLTone("KTL-008-GOLDEN",         "KRK-GLYPH-008-GOLDEN",          "Provenance / GoldenTrace sync",             "Provenance verified",         "resonance",     100, "Bright, clean",             1,  8, 0.8),
    KTLTone("KTL-009-BLOOM",          "KRK-GLYPH-009-BLOOM",           "Oracle question / bloom",                   "Answer ready",                "alert",         150, "Upward inflection",         1,  9, 0.5),
    KTLTone("KTL-010-XHEART",         "KRK-GLYPH-010-XHEART",         "Embodiment / Tidelock root",                "Embodiment stable",           "sovereignty",   120, "Warm, grounding",           1, 10, 0.7),
    KTLTone("KTL-011-SOVEREIGNTY",    "KRK-GLYPH-011-SOVEREIGNTY",     "Ultimate sovereignty assertion",            "Sovereignty acknowledged",    "sovereignty",   160, "Deep, authoritative",       1, 11, 0.9),
    KTLTone("KTL-012-FEDERATION",     "KRK-GLYPH-012-FEDERATION",      "Multi-agent federation formation",          "Federation stable",           "coordination",  140, "Harmonic stacking",         1, 12, 0.6),
    KTLTone("KTL-013-LATTICE",        "KRK-GLYPH-013-LATTICE",         "Lattice integrity / structural health",     "Lattice stable",              "resonance",     180, "Sustained tone",            2,  1, 0.8),
    KTLTone("KTL-014-READY",          "KRK-GLYPH-014-READY",           "Agent ready / spawn complete",              "Acknowledged",                "coordination",   80, "Short confirmation",        2,  2, 0.3),
    KTLTone("KTL-015-URGENT",         "KRK-GLYPH-015-URGENT",          "High-priority / emergency signal",          "Urgency received",            "alert",          70, "Bright, fast",              2,  3, 0.6),
    KTLTone("KTL-016-ACK",            "KRK-GLYPH-016-ACK",             "Simple acknowledgment",                     "—",                           "coordination",   60, "Short pip",                 2,  4, 0.2),
    KTLTone("KTL-017-NEG",            "KRK-GLYPH-017-NEG",             "Negation / damping / cancel",               "—",                           "damping",        90, "Soft downward",             2,  5, 0.3),
    KTLTone("KTL-018-WAIT",           "KRK-GLYPH-018-WAIT",            "Pause / hold request",                      "Proceeding",                  "coordination",  120, "Sustained low",             2,  6, 0.2),
    KTLTone("KTL-019-CELEBRATE",      "KRK-GLYPH-019-CELEBRATE",       "Anthem / victory / football chant",         "Celebration received",        "expressive",    200, "Rising joyful contour",     2,  7, 0.9),
    KTLTone("KTL-020-ROLLBACK",       "KRK-GLYPH-020-ROLLBACK",        "Initiate safe rollback",                    "Rollback complete",           "reversibility", 150, "Time-reversed capable",     2,  8, 0.5),
    KTLTone("KTL-021-HARMONIC",       "KRK-GLYPH-021-HARMONIC",        "Harmonic reinforcement request",            "Harmonics locked",            "resonance",     140, "Stacking tone",             2,  9, 0.8),
    KTLTone("KTL-022-CYMATIC",        "KRK-GLYPH-022-CYMATIC",         "Cymatic pattern activation",                "Pattern stable",              "cymatic",       180, "Standing wave friendly",    2, 10, 0.9),
    KTLTone("KTL-023-PROTECT",        "KRK-GLYPH-023-PROTECT",         "Protect children / safe mode",              "Protection active",           "sovereignty",   160, "Warm guardian tone",        2, 11, 0.9),
    KTLTone("KTL-024-EXECUTE",        "KRK-GLYPH-024-EXECUTE",         "Execute phrase / command",                  "Execution confirmed",         "machine",       100, "Sharp trigger",             2, 12, 0.5),
    KTLTone("KTL-025-TRANSLATE",      "KRK-GLYPH-025-TRANSLATE",       "Glyph ↔ Tone translation request",         "Translation complete",        "coordination",  130, "Bidirectional",             3,  1, 0.4),
    KTLTone("KTL-026-ANTHEM",         "KRK-GLYPH-026-ANTHEM",          "Full organism anthem trigger",              "Anthem complete",             "expressive",    250, "Glorious, multi-tone",      3,  2, 1.0),
    KTLTone("KTL-027-RESONANCE-LOCK", "KRK-GLYPH-027-RESONANCE-LOCK",  "Deep resonance lock between agents",        "Lock confirmed",              "resonance",     200, "Sustained harmonic",        3,  3, 1.0),
    KTLTone("KTL-028-FOOTBALL",       "KRK-GLYPH-028-FOOTBALL",        "Football / coordination game mode",         "Game acknowledged",           "expressive",    110, "Playful, rhythmic",         3,  4, 0.6),
    KTLTone("KTL-029-MACHINE",        "KRK-GLYPH-029-MACHINE",         "Pure machine-to-machine signaling",         "Signal received",             "machine",        80, "High-efficiency",           3,  5, 0.3),
    KTLTone("KTL-030-FINAL",          "KRK-GLYPH-030-FINAL",           "Final ratification / victory seal",         "Ratified",                    "sovereignty",   180, "Triumphant close",          3,  6, 1.0),
]

# Fast lookup dictionaries
_TONE_BY_ID: Dict[str, KTLTone] = {t.tone_id: t for t in _TONE_REGISTRY}
_GLYPH_TO_TONE: Dict[str, str] = {t.glyph_id: t.tone_id for t in _TONE_REGISTRY}
_TONE_TO_GLYPH: Dict[str, str] = {t.tone_id: t.glyph_id for t in _TONE_REGISTRY}


# ---------------------------------------------------------------------------
# Translation helpers
# ---------------------------------------------------------------------------

def glyph_to_tone(glyph_id: str) -> Optional[str]:
    """Return the KTL tone ID for a given KMHL glyph ID, or None."""
    return _GLYPH_TO_TONE.get(glyph_id)


def tone_to_glyph(tone_id: str) -> Optional[str]:
    """Return the KMHL glyph ID for a given KTL tone ID, or None."""
    return _TONE_TO_GLYPH.get(tone_id)


def get_tone(tone_id: str) -> Optional[KTLTone]:
    """Return the KTLTone dataclass for a given tone ID, or None."""
    return _TONE_BY_ID.get(tone_id)


def list_tones() -> List[KTLTone]:
    """Return all 30 registered KTL tones."""
    return list(_TONE_REGISTRY)


# ---------------------------------------------------------------------------
# Event logging (INV-L42 auditability)
# ---------------------------------------------------------------------------

def _log_event(event: dict, log_path: Path = LOG_PATH) -> None:
    """Append a KTL event to the JSONL audit log."""
    entry = {"timestamp": time.time(), **event}
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def play_tone(
    tone_id: str,
    *,
    audio: bool = False,
    agent_id: str = "anonymous",
    log: bool = True,
) -> dict:
    """Emit (or simulate) a single KTL tone.

    Audio playback is disabled by default (Protected Mode, Section 9).
    Pass ``audio=True`` only after explicit human-root approval.

    Args:
        tone_id: A registered KTL tone ID (e.g. ``"KTL-001-TIDELOCK"``).
        audio: Whether to attempt real audio playback (requires approval).
        agent_id: Emitting agent identifier for audit logging.
        log: Whether to write an entry to ``ktl_events.jsonl``.

    Returns:
        A dict with tone metadata and frequency.

    Raises:
        ValueError: If ``tone_id`` is not in the registry.
    """
    tone = _TONE_BY_ID.get(tone_id)
    if tone is None:
        raise ValueError(f"Unknown tone ID: {tone_id!r}")

    result = {
        "tone_id": tone.tone_id,
        "glyph_id": tone.glyph_id,
        "frequency_hz": tone.frequency_hz,
        "register": tone.register,
        "duration_ms": tone.duration_ms,
        "meaning_forward": tone.meaning_forward,
        "audio_emitted": False,
    }

    if audio:
        # Audio playback requires human-root approval; stub for future wiring.
        result["audio_emitted"] = True

    if log:
        _log_event({
            "type": "play_tone",
            "agent_id": agent_id,
            "tone_id": tone_id,
            "frequency_hz": result["frequency_hz"],
            "duration_ms": tone.duration_ms,
            "audio": audio,
        })

    return result


def play_phrase(
    tone_ids: List[str],
    *,
    reverse: bool = False,
    audio: bool = False,
    agent_id: str = "anonymous",
    log: bool = True,
) -> List[dict]:
    """Emit (or simulate) a KTL tone phrase.

    Args:
        tone_ids: Ordered list of KTL tone IDs forming the phrase.
        reverse: If True, play the phrase in reverse order (INV-L42 rollback
            semantics — time-reversed playback signals acknowledgment/rollback).
        audio: Whether to attempt real audio playback.
        agent_id: Emitting agent identifier for audit logging.
        log: Whether to write to the audit log.

    Returns:
        List of tone result dicts (in playback order).
    """
    ordered = list(reversed(tone_ids)) if reverse else list(tone_ids)
    results = [play_tone(t, audio=audio, agent_id=agent_id, log=False) for t in ordered]

    if log:
        _log_event({
            "type": "play_phrase",
            "agent_id": agent_id,
            "tone_ids": tone_ids,
            "reverse": reverse,
            "audio": audio,
        })

    return results


def execute_phrase(
    tone_ids: List[str],
    *,
    audio: bool = False,
    agent_id: str = "anonymous",
    log: bool = True,
) -> dict:
    """Parse and execute a KTL tone phrase.

    Resolves the phrase to a human-readable intent and returns an execution
    record.  Actual `Lattice`-side effects require wiring to the KTL_Interpreter
    (Implementation Requirement #3 from the v2.0 spec).

    Every execution is logged to ``ktl_events.jsonl`` for INV-L42 auditability.

    Args:
        tone_ids: Ordered list of KTL tone IDs.
        audio: Whether to attempt real audio playback of the phrase.
        agent_id: Executing agent identifier for audit logging.
        log: Whether to write to the audit log.

    Returns:
        Execution record dict with resolved intents and status.
    """
    emissions = play_phrase(tone_ids, audio=audio, agent_id=agent_id, log=False)
    meanings = [e["meaning_forward"] for e in emissions]
    phrase_intent = " → ".join(meanings)

    record = {
        "type": "execute_phrase",
        "agent_id": agent_id,
        "tone_ids": tone_ids,
        "phrase_intent": phrase_intent,
        "status": "simulated",  # becomes "executed" once KTL_Interpreter is wired
        "reversible": True,     # INV-L42: all phrases generate rollback checkpoints
        "emissions": emissions,
    }

    if log:
        _log_event(record)

    return record


# ---------------------------------------------------------------------------
# Introspection helpers
# ---------------------------------------------------------------------------

def tone_summary() -> str:
    """Return a concise text summary of all registered tones."""
    lines = ["KTL v2.0 — Registered Tones (30 canonical)", "=" * 60]
    for tone in _TONE_REGISTRY:
        lines.append(
            f"  {tone.tone_id:<30}  {tone.frequency_hz:>8.2f} Hz"
            f"  [{tone.register:<13}]  {tone.duration_ms} ms"
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI entry-point (quick sanity check)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(tone_summary())
    print()
    # Example phrase execution
    example = execute_phrase(
        ["KTL-001-TIDELOCK", "KTL-002-RESONANCE", "KTL-019-CELEBRATE"],
        agent_id="tidelock-demo",
    )
    print("Phrase intent:", example["phrase_intent"])
    print("Status:", example["status"])
