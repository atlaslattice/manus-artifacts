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

import argparse
import json
import os
import random
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


def run_adversarial_smoke() -> bool:
    """Targeted mutation sweep over critical bytes from a known-good packet."""
    base = bytes.fromhex("0400000b00000000" + "00" * 24)
    failed_tests = 0

    mutations = [
        ("mut_v", 0, 0x05),
        ("mut_x", 1, 0x0C),
        ("mut_y", 2, 0x0C),
        ("mut_z_reserved", 3, 0x0A),
        ("mut_z_old_v2_0", 3, 0x0F),
    ]

    print("\n[+] Sector C: Running targeted adversarial mutation smoke...")
    for name, index, value in mutations:
        mutated = bytearray(base)
        mutated[index] = value
        try:
            parse_pkt_sundya0(bytes(mutated))
            print(f"  SECURITY HOLE: {name} unexpectedly accepted")
            failed_tests += 1
        except Layer1PacketError:
            print(f"  PASS: {name} rejected as expected")

    return failed_tests == 0


def run_fuzz_trials(trials: int = 2000, seed: int = 1728) -> bool:
    """
    Lightweight fuzzing for random byte streams.

    This fuzz pass does not assert that every 32-byte random packet must fail,
    because a random packet can theoretically match the shape gate. It asserts
    the stricter safety property that no non-32-byte random packet may be accepted.
    """
    rng = random.Random(seed)
    allowed_lengths = [0, 1, 2, 3, 4, 8, 16, 31, 32, 33, 64]
    failed_tests = 0
    accepted = 0

    print(f"\n[+] Sector D: Running fuzz trials... trials={trials} seed={seed}")
    for _ in range(trials):
        n = rng.choice(allowed_lengths)
        buf = os.urandom(n)
        try:
            parse_pkt_sundya0(buf)
            accepted += 1
            if n != PKT_SUNDYA_SIZE:
                failed_tests += 1
        except Layer1PacketError:
            pass

    print(f"  FUZZ SUMMARY: accepted={accepted} non_32_byte_accept_failures={failed_tests}")
    return failed_tests == 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PKT-SUNDYA-0 v2.1 Layer-1 harness")
    parser.add_argument(
        "fixtures",
        nargs="?",
        default="tests/pkt_sundya_0_fixtures.json",
        help="Path to JSON fixture suite",
    )
    parser.add_argument("--smoke", action="store_true", help="Run targeted mutation smoke tests")
    parser.add_argument("--fuzz", action="store_true", help="Run lightweight random fuzz trials")
    parser.add_argument("--fuzz-trials", type=int, default=2000, help="Number of fuzz trials")
    parser.add_argument("--fuzz-seed", type=int, default=1728, help="Fuzz length-selection seed")
    return parser


if __name__ == "__main__":
    args = build_arg_parser().parse_args()

    success = run_layer1_harness(args.fixtures)
    if args.smoke:
        success = run_adversarial_smoke() and success
    if args.fuzz:
        success = run_fuzz_trials(args.fuzz_trials, args.fuzz_seed) and success

    sys.exit(0 if success else 1)
