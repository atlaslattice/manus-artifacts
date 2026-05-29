"""Deterministic REM-style 100-year simulation for the Aetherforge KG stack.

REM here means a bounded dream/rehearsal mode. It is not prediction,
canon, deployment, or authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any, Iterable

SURFACES = [
    "GitHub",
    "Notion",
    "Drive",
    "Calendar",
    "Sheets",
    "LocalFiles",
    "HumanRoot",
    "Aetherforge",
    "Sheldonbrain",
    "Lucerna",
    "ChildrenSwarm",
    "PublicKG",
]

PHASES = [
    ("Y001-Y010", "Stabilize receipts and boundary hydration"),
    ("Y011-Y020", "Convert missing receipts into graph-addressable nodes"),
    ("Y021-Y030", "Crosswalk raw archives into source-indexed lattices"),
    ("Y031-Y040", "Harden tests, CI, reproducibility, and rollback lanes"),
    ("Y041-Y050", "Extract reusable public knowledge graph schemas"),
    ("Y051-Y060", "Scale local simulation corpora without canon drift"),
    ("Y061-Y070", "Build contradiction and supersession ledgers"),
    ("Y071-Y080", "Federate lawful/open public mirrors with provenance gates"),
    ("Y081-Y090", "Compress mature patterns into teaching and onboarding loops"),
    ("Y091-Y100", "Preserve continuity while preventing authority leakage"),
]

RISKS = ["receipt_gap", "hash_gap", "export_staleness", "authority_leakage", "canon_drift", "context_loss"]
ACTIONS = ["preserve", "mirror", "validate", "crosswalk", "quarantine", "summarize", "test", "review"]


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def simulate(seed: int = 144, duration_years: int = 100) -> dict[str, Any]:
    if duration_years != 100:
        raise ValueError("REM v0.1 is intentionally fixed to 100 yearly states.")

    head = sha256_text(f"REM-100|seed:{seed}")
    yearly_states: list[dict[str, Any]] = []

    for year in range(1, duration_years + 1):
        decade_index = (year - 1) // 10
        phase = PHASES[decade_index][1]
        event = {
            "year": year,
            "phase": phase,
            "primary_surface": SURFACES[(year - 1) % len(SURFACES)],
            "dominant_risk": RISKS[((year * 7) + seed) % len(RISKS)],
            "recommended_action": ACTIONS[(year + seed) % len(ACTIONS)],
            "continuity_index": round(min(100, 35 + year * 0.55 + decade_index * 2), 2),
            "drift_pressure": round(max(0, 40 - year * 0.25 + (year % 7)), 2),
            "test_coverage_signal": round(min(100, 12 + year * 0.75), 2),
        }
        previous_head = head
        head = sha256_text(previous_head + canonical_json(event))
        event["previous_head"] = previous_head
        event["receipt_head"] = head
        yearly_states.append(event)

    return {
        "schema_version": "rem_100_year_simulation.v0_1",
        "artifact_id": "REM_100_YEAR_SIMULATION__AETHERFORGE_SHELDONBRAIN_KG__NON_CANON__2026-05-28",
        "status": "candidate_dream_rehearsal_not_canon",
        "seed": seed,
        "boundary": {
            "canon": False,
            "deployment": False,
            "authority": "none",
            "prediction": False,
            "mode": "REM dream rehearsal / simulation / graph stress test",
        },
        "duration_years": duration_years,
        "phases": [{"range": item[0], "purpose": item[1]} for item in PHASES],
        "final_receipt_head": head,
        "yearly_states": yearly_states,
        "keeper_read": "Continuity survives by making every gap addressable.",
    }


def validate(result: dict[str, Any]) -> dict[str, Any]:
    states = result["yearly_states"]
    receipt_links_ok = all(current["previous_head"] == previous["receipt_head"] for previous, current in zip(states, states[1:]))
    report = {
        "duration_years": result.get("duration_years"),
        "yearly_state_count": len(states),
        "phase_count": len(result.get("phases", [])),
        "receipt_links_ok": receipt_links_ok,
        "canon_false": result["boundary"].get("canon") is False,
        "deployment_false": result["boundary"].get("deployment") is False,
        "authority_none": result["boundary"].get("authority") == "none",
        "prediction_false": result["boundary"].get("prediction") is False,
    }
    report["ok"] = (
        report["duration_years"] == 100
        and report["yearly_state_count"] == 100
        and report["phase_count"] == 10
        and report["receipt_links_ok"]
        and report["canon_false"]
        and report["deployment_false"]
        and report["authority_none"]
        and report["prediction_false"]
    )
    return report


def render_text(result: dict[str, Any]) -> str:
    report = validate(result)
    return "\n".join(
        [
            "REM 100-year simulation",
            f"seed: {result['seed']}",
            f"years: {result['duration_years']}",
            f"phases: {len(result['phases'])}",
            f"yearly_states: {len(result['yearly_states'])}",
            f"final_receipt_head: {result['final_receipt_head']}",
            f"validation_ok: {report['ok']}",
            f"keeper_read: {result['keeper_read']}",
        ]
    )


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run deterministic REM 100-year simulation.")
    parser.add_argument("--json", action="store_true", help="Emit full JSON result.")
    parser.add_argument("--seed", type=int, default=144)
    args = parser.parse_args(list(argv) if argv is not None else None)
    result = simulate(seed=args.seed)
    print(json.dumps(result, indent=2, sort_keys=True) if args.json else render_text(result))
    return 0 if validate(result)["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
