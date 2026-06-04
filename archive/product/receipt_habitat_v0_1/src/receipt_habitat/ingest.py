"""Local ingest helper for Receipt Habitat v0.1.

This helper creates a minimal native-thread ingestion packet from local text.
It does not call networks, mutate external systems, or assign canon/deployment status.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

try:
    from .packet import apply_v0_defaults, validate_ingestion_packet
    from .serialize import to_simple_yaml, to_stable_json, write_packet
except ImportError:  # pragma: no cover - allows direct script use
    from packet import apply_v0_defaults, validate_ingestion_packet
    from serialize import to_simple_yaml, to_stable_json, write_packet


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_ingestion_packet(
    input_path: str,
    *,
    raw_status: str,
    timezone: str,
    seat_name: str = "unassigned",
    model_surface: str = "unknown",
    source_thread_label: str | None = None,
    privacy_status: str = "private",
) -> dict[str, Any]:
    path = Path(input_path)
    text = path.read_text(encoding="utf-8")
    label = source_thread_label or path.stem
    packet = {
        "packet_id": f"pkt-{sha256_text(str(path) + text)[:12]}",
        "seat_name": seat_name,
        "model_surface": model_surface,
        "source_thread_label": label,
        "thread_time_range": {
            "start": "unknown",
            "end": "unknown",
            "timezone": timezone,
        },
        "raw_export_status": raw_status,
        "access_scope": {
            "visible_sources": [str(path)],
            "unavailable_sources": [] if raw_status != "summary_only" else ["full raw transcript"],
            "assumed_context": [],
        },
        "source_refs": [str(path)],
        "sha256_if_available": sha256_text(text),
        "privacy_status": privacy_status,
        "key_events": [],
        "artifacts_created": [],
        "claims_extracted": [],
        "contradictions_or_uncertainties": [],
        "overclaims_to_avoid": [],
        "identity_drift_events": [],
        "strongest_safe_claim": "Local source captured as non-canon evidence packet input.",
        "next_action": "Review packet before synthesis or routing.",
        "public_claim_allowed": False,
    }
    return apply_v0_defaults(packet)


def main() -> int:
    parser = argparse.ArgumentParser(description="Receipt Habitat v0.1 local ingest helper")
    parser.add_argument("input")
    parser.add_argument("--raw-status", required=True, choices=["full_raw", "partial_raw", "summary_only", "unavailable"])
    parser.add_argument("--timezone", default="America/Chicago")
    parser.add_argument("--seat-name", default="unassigned")
    parser.add_argument("--model-surface", default="unknown")
    parser.add_argument("--format", choices=["json", "yaml"], default="json")
    parser.add_argument("--output", help="Optional output path for the generated packet")
    args = parser.parse_args()

    packet = build_ingestion_packet(
        args.input,
        raw_status=args.raw_status,
        timezone=args.timezone,
        seat_name=args.seat_name,
        model_surface=args.model_surface,
    )
    result = validate_ingestion_packet(packet)
    if not result.ok:
        for error in result.errors:
            print(f"ERROR: {error}")
        return 2

    if args.output:
        write_packet(packet, args.output, fmt=args.format)
        print(f"wrote packet: {args.output}")
        return 0

    if args.format == "yaml":
        print(to_simple_yaml(packet), end="")
    else:
        print(to_stable_json(packet), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
