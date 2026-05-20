#!/usr/bin/env python3
"""
ATLAS PRIME Layer-1 Wire Harness Validator (v2.1 Spec)

Candidate local integration suite for PKT-SUNDYA-0.
Validates fixed-width length constraints and the in-ring Śūnya boundary:

    version     = 0x04
    coord_x     ∈ {0,...,11}
    coord_y     ∈ {0,...,11}
    state_class = 0x0B
    sequence_id = uint32 little-endian
    residue     = 24 bytes

Status: candidate reference harness, not production canon.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PKT_SUNDYA_VERSION = 0x04
PKT_SUNDYA_STATE_CLASS = 0x0B
PKT_SUNDYA_SIZE = 32
COORD_MIN = 0
COORD_MAX = 11


class Layer1PacketError(ValueError):
    """Raised when PKT-SUNDYA-0 fails Layer-1 shape validation."""


@dataclass(frozen=True)
class PktSundya0:
    version: int
    coord_x: int
    coord_y: int
    state_class: int
    sequence_id: int
    residue_hash: bytes

    @property
    def matrix_i(self) -> int:
        return self.coord_x + 1

    @property
    def matrix_j(self) -> int:
        return self.coord_y + 1


def parse_hex_stream(hex_stream: str) -> bytes:
    try:
        return bytes.fromhex(hex_stream)
    except ValueError as exc:
        raise Layer1PacketError("ERR_INVALID_HEX_STREAM") from exc


def parse_pkt_sundya0(raw_bytes: bytes) -> PktSundya0:
    """
    Parse and validate a PKT-SUNDYA-0 byte stream.

    This is layout-safe byte deserialization, not zero-copy parsing.
    Sequence monotonicity and residue hash cryptographic validation are external
    D0 / session-guard responsibilities.
    """
    if len(raw_bytes) != PKT_SUNDYA_SIZE:
        raise Layer1PacketError("ERR_INVALID_BYTE_LENGTH")

    version = raw_bytes[0]
    coord_x = raw_bytes[1]
    coord_y = raw_bytes[2]
    state_class = raw_bytes[3]
    sequence_id = int.from_bytes(raw_bytes[4:8], byteorder="little", signed=False)
    residue_hash = raw_bytes[8:32]

    if version != PKT_SUNDYA_VERSION:
        raise Layer1PacketError("ERR_L1_VERSION_MISMATCH")
    if not (COORD_MIN <= coord_x <= COORD_MAX):
        raise Layer1PacketError("ERR_L1_COORD_X_OUT_OF_BOUNDS")
    if not (COORD_MIN <= coord_y <= COORD_MAX):
        raise Layer1PacketError("ERR_L1_COORD_Y_OUT_OF_BOUNDS")
    if state_class != PKT_SUNDYA_STATE_CLASS:
        raise Layer1PacketError("ERR_L1_STATE_CLASS_MISMATCH")

    return PktSundya0(
        version=version,
        coord_x=coord_x,
        coord_y=coord_y,
        state_class=state_class,
        sequence_id=sequence_id,
        residue_hash=residue_hash,
    )


def load_suite(fixtures_path: Path) -> dict[str, Any]:
    if not fixtures_path.exists():
        raise FileNotFoundError(f"Fixture file missing at {fixtures_path}")

    with fixtures_path.open("r", encoding="utf-8") as fh:
        suite = json.load(fh)

    if not isinstance(suite, dict) or "fixtures" not in suite:
        raise ValueError("ERR_INVALID_FIXTURE_SCHEMA")

    return suite


def run_layer1_harness(fixtures_path: str | os.PathLike[str]) -> bool:
    path = Path(fixtures_path)

    print("======================================================================")
    print("[PKT-SUNDYA-0] Initializing Layer-1 Shape & Invariant Testing Harness")
    print("======================================================================")

    try:
        suite = load_suite(path)
    except Exception as exc:
        print(f"CRITICAL ERROR: {exc}")
        return False

    fixtures = suite.get("fixtures", {})
    failed_tests = 0

    print("\n[+] Sector A: Evaluating compliant inbound claims...")
    for case in fixtures.get("good_cases", []):
        desc = case.get("description", "<missing description>")
        hex_stream = case.get("hex_stream", "")
        expected = case.get("expected_parse", {})

        try:
            packet = parse_pkt_sundya0(parse_hex_stream(hex_stream))

            expected_sequence = expected.get("sequence_id")
            if expected_sequence is not None and packet.sequence_id != expected_sequence:
                raise AssertionError(
                    f"ERR_SEQUENCE_MISMATCH expected={expected_sequence} actual={packet.sequence_id}"
                )

            print(f"  PASS: {desc}")
            print(
                f"     | Wire: ({packet.coord_x}, {packet.coord_y}) "
                f"-> Matrix: (i={packet.matrix_i}, j={packet.matrix_j})"
            )
            print(
                f"     | Class: {packet.state_class:#04x} (Sundya) | Seq: {packet.sequence_id}"
            )

        except Exception as exc:
            print(f"  UNEXPECTED FAILURE: {desc} | Reason: {exc}")
            failed_tests += 1

    print("\n[+] Sector B: Evaluating adversarial injection protections...")
    for case in fixtures.get("bad_cases", []):
        desc = case.get("description", "<missing description>")
        hex_stream = case.get("hex_stream", "")
        expected_err = case.get("expected_error")

        try:
            parse_pkt_sundya0(parse_hex_stream(hex_stream))
            print(f"  SECURITY HOLE: Malformed packet bypassed filters! {desc}")
            failed_tests += 1
        except Layer1PacketError as exc:
            actual_err = str(exc)
            if actual_err == expected_err:
                print(f"  PASS: Circuit breaker tripped cleanly. Caught: {actual_err}")
                print(f"     | Context: {desc}")
            else:
                print(f"  MISMATCHED ERROR: Expected {expected_err}, but got {actual_err}")
                failed_tests += 1
        except Exception as exc:
            print(f"  UNEXPECTED ERROR TYPE: {desc} | Reason: {exc}")
            failed_tests += 1

    print("\n======================================================================")
    if failed_tests == 0:
        print("HARNESS RESULT: SUCCESS. All v2.1 Layer-1 shape invariants verified.")
        print("======================================================================")
        return True

    print(f"HARNESS RESULT: FAILED. {failed_tests} verification errors found.")
    print("======================================================================")
    return False


if __name__ == "__main__":
    fixtures_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("tests/pkt_sundya_0_fixtures.json")
    success = run_layer1_harness(fixtures_file)
    sys.exit(0 if success else 1)
