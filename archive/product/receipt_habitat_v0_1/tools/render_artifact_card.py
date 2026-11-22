#!/usr/bin/env python3
"""Offline artifact-card renderer: candidate-only JSON or Markdown to stdout.

Does not access external services, grant canon, write to a graph, open a host,
or infer source rights. Caller supplies an explicit local JSON source packet.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "receipt_habitat"))
from artifact_card import build_artifact_card, artifact_card_to_markdown  # noqa: E402


def _unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate_json_key")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError("nonfinite_json_constant")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path, help="explicitly selected, local candidate JSON")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args(argv)
    try:
        raw = args.candidate.read_text(encoding="utf-8")
        if len(raw.encode("utf-8")) > 1024 * 1024:
            raise ValueError("candidate_too_large")
        payload = json.loads(raw, object_pairs_hook=_unique_keys, parse_constant=_reject_constant)
        result = build_artifact_card(payload)
    except (OSError, ValueError, UnicodeError, TypeError, RecursionError) as error:
        print("BLOCKED_CANDIDATE_PARSE: " + type(error).__name__, file=sys.stderr)
        return 2

    if not result.ok or result.card is None:
        print("BLOCKED_CANDIDATE_REVIEW: " + ",".join(result.errors), file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result.card, ensure_ascii=False, indent=2, allow_nan=False))
    else:
        sys.stdout.write(artifact_card_to_markdown(result.card))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
