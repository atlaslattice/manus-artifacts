#!/usr/bin/env python3
"""Dongjiakou Node-001 pilot simulator.

Deterministic execution of Runs 0 / 0.2 / 1 / 2 / 3 / 4A / S02, reproduction of
every derived number against the committed evidence artifacts, and a full
validator gate sweep.

Usage:
    python3 simulator.py manifest     # regenerate sources/source_manifest.json
    python3 simulator.py reproduce    # reproduce every derived number
    python3 simulator.py validate     # run the gate suite
    python3 simulator.py unknowns     # emit the unresolved-UNKNOWN ledger
    python3 simulator.py run RUN_3    # print one run's result
    python3 simulator.py all          # manifest + reproduce + validate + unknowns

Nothing here writes to, or deploys anything at, physical plant infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PACKAGE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PACKAGE_DIR))

from models.common import UNKNOWN, is_unknown, rel_diff, resolve_path, to_jsonable  # noqa: E402
from models import RUN_REGISTRY, run0, run2_hydro, run3_compute  # noqa: E402
from sources import loader  # noqa: E402
from validators import build_bundle, validate  # noqa: E402

REPORTS_DIR = PACKAGE_DIR / "reports"
RUNS_DIR = PACKAGE_DIR / "runs"
REPRO_SPEC = RUNS_DIR / "reproduction_spec.json"

#: Runs that feed the validator bundle.
BUNDLE_ARTIFACT_KEYS = (
    "RUN_0", "RUN_0.2", "RUN_1", "RUN_2", "RUN_3", "RUN_4A", "S02",
    "INTEGRATED_NODE_PROFILE", "C01_MODEL_ROUTING_POLICY",
)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _model_for(name: str):
    """Resolve a 'module:function' or 'module.function' reference."""
    module_name, _, func_name = name.replace(":", ".").rpartition(".")
    module = {
        "run0": run0,
        "run1_solar": __import__("models.run1_solar", fromlist=["x"]),
        "run2_hydro": __import__("models.run2_hydro", fromlist=["x"]),
        "run3_compute": run3_compute,
        "run4a_biometabolic": __import__("models.run4a_biometabolic", fromlist=["x"]),
        "s02_bess": __import__("models.s02_bess", fromlist=["x"]),
    }[module_name]
    return getattr(module, func_name)


# ---------------------------------------------------------------------------
# reproduce
# ---------------------------------------------------------------------------
def reproduce() -> dict[str, Any]:
    """Execute every run and compare each derived number to the committed artifact."""
    spec = json.loads(REPRO_SPEC.read_text(encoding="utf-8"))
    runs_out: list[dict[str, Any]] = []
    total_checks = total_mismatch = total_annotated = 0

    for run_spec in spec["runs"]:
        run_id = run_spec["run_id"]
        model = _model_for(run_spec["model"])
        produced = model(**run_spec.get("model_kwargs", {}))
        committed = loader.load_artifact(run_spec["artifact_file"])
        annotations = {a["path"]: a for a in run_spec.get("annotations", [])}

        checks: list[dict[str, Any]] = []
        for comp in run_spec["comparisons"]:
            path, tol = comp["path"], comp["tol"]
            try:
                expected = resolve_path(committed, path)
            except KeyError as exc:
                checks.append({"path": path, "status": "MISSING_IN_ARTIFACT", "detail": str(exc)})
                continue
            try:
                actual = resolve_path(produced, path)
            except KeyError as exc:
                checks.append({"path": path, "status": "MISSING_IN_MODEL", "detail": str(exc)})
                continue

            if is_unknown(expected) or is_unknown(actual):
                ok = is_unknown(expected) and is_unknown(actual)
                diff = None
            elif isinstance(expected, str) or isinstance(actual, str):
                ok = expected == actual
                diff = None
            else:
                diff = rel_diff(float(expected), float(actual))
                ok = diff <= tol

            status = "MATCH" if ok else "MISMATCH"
            annotation = None
            if status == "MISMATCH" and path in annotations:
                status = "ANNOTATED_DIVERGENCE"
                annotation = annotations[path]
            checks.append({
                "path": path,
                "expected": to_jsonable(expected),
                "actual": to_jsonable(actual),
                "tol": tol,
                "rel_diff": diff,
                "status": status,
                "annotation": annotation,
            })

        matched = sum(1 for c in checks if c["status"] == "MATCH")
        annotated = sum(1 for c in checks if c["status"] == "ANNOTATED_DIVERGENCE")
        divergent = sum(
            1 for c in checks if c["status"] not in ("MATCH", "ANNOTATED_DIVERGENCE")
        )
        total_checks += len(checks)
        total_mismatch += divergent
        total_annotated += annotated
        if divergent:
            run_status = "DIVERGENT"
        elif annotated:
            run_status = "REPRODUCED_WITH_ANNOTATED_DIVERGENCE"
        else:
            run_status = "REPRODUCED"
        runs_out.append({
            "run_id": run_id,
            "title": run_spec["title"],
            "artifact_file": run_spec["artifact_file"],
            "model": run_spec["model"],
            "checks": checks,
            "matched": matched,
            "annotated": annotated,
            "divergent": divergent,
            "checked": len(checks),
            "status": run_status,
        })

    report = {
        "artifact_id": "DJK-NODE-001-REPRODUCTION-REPORT",
        "status": "ALL_RUNS_REPRODUCED" if total_mismatch == 0 else "DIVERGENCE_DETECTED",
        "generated_at": _now(),
        "reference_head": spec.get("reference_head"),
        "totals": {
            "runs": len(runs_out),
            "checks": total_checks,
            "matched": sum(r["matched"] for r in runs_out),
            "mismatched": total_mismatch,
            "annotated": total_annotated,
        },
        "runs": runs_out,
    }
    return report


def _reproduction_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Run 0-3 Reproduction Report",
        "",
        f"Generated: {report['generated_at']}  ",
        f"Reference head: `{report['reference_head']}`  ",
        f"Overall: **{report['status']}**",
        "",
        "| Run | Title | Checks | Matched | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for run in report["runs"]:
        lines.append(
            f"| {run['run_id']} | {run['title']} | {run['checked']} | "
            f"{run['matched']} | **{run['status']}** |"
        )
    totals = report["totals"]
    lines += [
        "",
        f"Totals: {totals['matched']}/{totals['checks']} derived values reproduced "
        f"across {totals['runs']} runs.",
        f"Annotated divergences preserved (not overwritten): {totals.get('annotated', 0)}.",
        f"Unexplained divergences: {totals['mismatched']}.",
        "",
    ]
    annotated_runs = [r for r in report["runs"] if r.get("annotated")]
    if annotated_runs:
        lines += ["## Annotated divergences", "",
                  "These are values where the committed artifact and the reproduced "
                  "value disagree beyond machine precision. Both are preserved; the "
                  "committed artifact is not overwritten.", ""]
        for run in annotated_runs:
            for c in run["checks"]:
                if c["status"] != "ANNOTATED_DIVERGENCE":
                    continue
                ann = c.get("annotation") or {}
                lines += [
                    f"### `{c['path']}` ({run['run_id']})",
                    "",
                    f"- Kind: **{ann.get('kind', 'UNCLASSIFIED')}**",
                    f"- Committed: `{c['expected']}`",
                    f"- Reproduced: `{c['actual']}`",
                    f"- Relative difference: `{c['rel_diff']:.3e}`",
                    f"- Detail: {ann.get('detail', '')}",
                    f"- Resolution: {ann.get('resolution', '')}",
                    "",
                ]
    for run in report["runs"]:
        lines += [f"## {run['run_id']} — {run['title']}", ""]
        lines += [f"Model: `{run['model']}`  ", f"Artifact: `{run['artifact_file']}`", ""]
        lines += ["| Path | Committed | Reproduced | Rel. diff | Tol | Status |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for c in run["checks"]:
            exp = c.get("expected", "")
            act = c.get("actual", "")
            diff = c.get("rel_diff")
            diff_s = "—" if diff is None else f"{diff:.2e}"
            lines.append(
                f"| `{c['path']}` | {exp} | {act} | {diff_s} | {c.get('tol', '')} | {c['status']} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------
def validate_all() -> tuple[dict[str, Any], Any]:
    """Build the validator bundle from disk and run every gate."""
    artifacts = loader.load_all()
    bundle_artifacts = {k: artifacts[k] for k in BUNDLE_ARTIFACT_KEYS if k in artifacts}

    profile = artifacts["INTEGRATED_NODE_PROFILE"]
    routing = artifacts["C01_MODEL_ROUTING_POLICY"]

    run3 = artifacts["RUN_3"]
    produced_runs = {rid: fn() for rid, fn in RUN_REGISTRY.items()}
    bundle = build_bundle(
        bundle_artifacts,
        node_profile=profile,
        routing_policy=routing,
        produced_runs=produced_runs,
        monte_carlo_requested=False,
        claimed_marine_discharge=False,
        compute_heat_credit_gwh=float(
            (run3.get("heat_credit") or {}).get("baseline_useful_heat_GWhth", 0) or 0
        ),
        compute_service_benefit=0.0,
        ecological_veto_passed=True,
        llm_actuator_authority=None,
        model_consensus_treated_as_evidence=False,
        hydro_recovered_head_m=UNKNOWN,
        hydro_pump_head_counted=False,
        s01_pv_credits=[],
        s01_pv_treated_as_incremental=False,
        net_positive_claim=False,
    )
    report = validate(bundle)
    return report.to_dict(), report


# ---------------------------------------------------------------------------
# unknown ledger
# ---------------------------------------------------------------------------
def unknown_ledger() -> dict[str, Any]:
    """Collect every UNKNOWN and every explicitly-zero credit into one ledger."""
    artifacts = loader.load_all()
    profile = artifacts["INTEGRATED_NODE_PROFILE"]

    unknown_params = dict(run3_compute.UNKNOWN_PARAMETERS)
    unchanged = list(run0.UNCHANGED_UNKNOWNS)

    components: list[dict[str, Any]] = []
    for comp in profile.get("components", []):
        components.append({
            "component_id": comp.get("component_id"),
            "type": comp.get("type"),
            "evidence_profile": comp.get("evidence_profile"),
            "credit": comp.get("credit", comp.get("energy_credit", comp.get("current_credit"))),
            "node001_access": comp.get("node001_access"),
            "contractual_basis": comp.get("contractual_basis"),
            "vetoes": comp.get("vetoes", []),
        })

    green = profile.get("green_direct_status", {})

    return {
        "artifact_id": "DJK-NODE-001-UNKNOWN-LEDGER",
        "generated_at": _now(),
        "principle": (
            "UNKNOWN remains UNKNOWN. Every entry below is either an unestablished "
            "quantity or an explicit zero-credit baseline. Nothing here may be "
            "backfilled from aggregate node performance."
        ),
        "counts": {
            "desalination_unknowns": len(unchanged),
            "compute_unknown_parameters": len(unknown_params),
            "components": len(components),
            "green_direct_unknowns": sum(
                1 for v in green.values() if is_unknown(v) or v is False
            ),
        },
        "desalination_unknowns": unchanged,
        "compute_unknown_parameters": unknown_params,
        "component_evidence": components,
        "green_direct_status": green,
        "explicit_zero_credit_baselines": [
            "RUN_0.retrofit_credit.* — no retrofit credit assigned",
            "RUN_2.baseline.hydro_credit_GWh_year = 0 — no receipt identifies unused head",
            "RUN_3.heat_credit.baseline_useful_heat_GWhth = 0 — no measured thermal sink",
            "RUN_4A.baseline_credit.* = 0 — no feedstock, chemistry or off-take receipt",
            "S02.baseline_credit = 0 — no hourly PV/load/curtailment trace",
            "INTEGRATED_NODE_PROFILE.green_direct_status.energy_credit = 0 — node allocation UNKNOWN",
        ],
        "data_required_to_close": {
            "desalination": [
                "plant-specific 2026 electricity tariff / settlement receipt",
                "whole-site SEC and delta_aux measurements",
                "current measured recovery fraction",
                "feed and reject stream map",
                "brine composition",
                "fouling rate and CIP history",
                "primary ecological monitoring data",
                "unused hydraulic head profile",
                "roof structural and interconnection limits",
            ],
            "compute": sorted(unknown_params),
            "biometabolic": [
                "Node-001 feedstock allocation or on-node generation receipt",
                "biogas quantity and CH4 composition",
                "actual conversion/use path",
                "digestate nutrient mass and product assay",
                "verified reclaimed-water reuse displacement",
            ],
            "grid": [
                "node allocation in MW / MWh under the direct-green pathway",
                "contract price and settlement rules",
                "eligible load set",
            ],
        },
    }


def _unknown_markdown(ledger: dict[str, Any]) -> str:
    lines = [
        "# Unresolved UNKNOWN Ledger",
        "",
        f"Generated: {ledger['generated_at']}",
        "",
        f"> {ledger['principle']}",
        "",
        "## Counts",
        "",
        "| Group | Count |",
        "| --- | --- |",
    ]
    for key, value in ledger["counts"].items():
        lines.append(f"| {key.replace('_', ' ')} | {value} |")

    lines += ["", "## Desalination unknowns", ""]
    lines += [f"- `{u}`" for u in ledger["desalination_unknowns"]]

    lines += ["", "## Compute unknown parameters", "", "| Parameter | State |", "| --- | --- |"]
    for key, value in ledger["compute_unknown_parameters"].items():
        lines.append(f"| `{key}` | {value} |")

    lines += ["", "## Component evidence profile", "",
              "| Component | Type | Evidence profile | Credit | Node access |",
              "| --- | --- | --- | --- | --- |"]
    for comp in ledger["component_evidence"]:
        lines.append(
            f"| {comp['component_id']} | {comp['type']} | {comp['evidence_profile']} | "
            f"{comp['credit']} | {comp['node001_access']} |"
        )

    lines += ["", "## Explicit zero-credit baselines", ""]
    lines += [f"- {z}" for z in ledger["explicit_zero_credit_baselines"]]

    lines += ["", "## Data required to close", ""]
    for group, items in ledger["data_required_to_close"].items():
        lines += [f"### {group}", ""]
        lines += [f"- {i}" for i in items]
        lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _resources_markdown(res: dict[str, Any]) -> str:
    """Render Run 6 as a human-readable report."""
    lines = [
        "# Run 6 — Resource Modules (one at a time)",
        "",
        f"**Artifact ID:** `{res['artifact_id']}`",
        f"**Status:** {res['status']}",
        f"**Study classification:** {res['study_classification']}",
        "",
        "> " + res["governing_rule"],
        "",
        "## Summary",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| Modules instantiated | {res['summary']['modules_instantiated']} |",
        f"| Modules eligible for value | **{res['summary']['modules_eligible_for_value']}** |",
        f"| Total value credit | **{res['summary']['total_value_credit']}** |",
        f"| Reason | {res['summary']['reason']} |",
        "",
        "## The eight required questions",
        "",
        "| Question | Requirement | Veto-bearing |",
        "| --- | --- | --- |",
    ]
    for key, question in res["required_questions"].items():
        veto = "**YES**" if key in res["veto_requirements"] else "no"
        lines.append(f"| `{key}` | {question} | {veto} |")

    lines += ["", "## Modules", ""]
    for name, module in res["modules"].items():
        lines += [
            f"### {name}",
            "",
            f"_{module['classification']}_",
            "",
            "| Quantity | Value |",
            "| --- | --- |",
        ]
        for k, v in module["transfer_function"].items():
            lines.append(f"| `{k}` | {v} |")
        reg = module["recovery"]
        lines += [
            "",
            f"- Receipted: **{reg['receipted_count']} / {reg['required_count']}**",
            f"- Eligible for value: **{reg['eligible_for_value']}**",
            f"- Value credit: **{reg['value_credit']}**",
            "",
            "**Finding.** " + module["finding"],
            "",
        ]
        if "architecture_consequence" in module:
            lines += ["**Architecture consequence.** " + module["architecture_consequence"], ""]
        lines += ["**Not claimed:**", ""]
        lines += [f"- {item}" for item in module["not_claimed"]]
        lines.append("")

    lines += [
        "## Sequencing",
        "",
        res["sequence_rule"],
        "",
        "## Unresolved",
        "",
    ]
    lines += [f"- {item}" for item in res["unresolved"]]
    lines.append("")
    return "\n".join(lines)


def _locality_markdown(res: dict[str, Any]) -> str:
    """Render the locality stream register v0.2 as a human-readable report."""
    c = res["counts"]
    lines = [
        "# Dongjiakou Locality Stream Register v0.2",
        "",
        f"**Artifact ID:** `{res['artifact_id']}`",
        f"**Status:** {res['status']}",
        f"**Boundary:** {res['boundary']}",
        "",
        "## v0.2 changes",
        "",
    ]
    lines += [f"- {x}" for x in res["v0_2_changes"]]

    lines += ["", "## Governing rules", ""]
    lines += [f"- {r}" for r in res["governing_rules"]]

    cl = res["clearance"]
    lines += [
        "",
        "## Clearance — two questions that must not be read as one",
        "",
        "| State | Question | Answer |",
        "| --- | --- | --- |",
        f"| `SIMULATOR_VALIDATION` | {cl['SIMULATOR_VALIDATION']['question']} | **{cl['SIMULATOR_VALIDATION']['answer']}** |",
        f"| `LOCALITY_CLEARANCE` | {cl['LOCALITY_CLEARANCE']['question']} | **{cl['LOCALITY_CLEARANCE']['answer']}** |",
        "",
        f"> {cl['warning']}",
        "",
        "## Subnodes",
        "",
        "| ID | Description |",
        "| --- | --- |",
    ]
    for sid, desc in res["subnodes"].items():
        lines.append(f"| `{sid}` | {desc} |")

    for title, key, note in (
        ("Physical StreamGraph — what actually flows today", "physical_streamgraph",
         "Flows that exist now. A stream may be counted once."),
        ("Opportunity Graph — what could flow", "opportunity_graph",
         "Nothing here carries realized credit. Ordered by strength of commitment."),
    ):
        lines += [
            "", f"## {title}", "", f"_{note}_", "",
            "| Stream | Source | Sink | Flow | Quantity | Evidence | Edge state | Credit owner | Allocation owner |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for s in res[key]:
            lines.append(
                f"| `{s['stream_id']}` | {s['source_subnode']} | {s['sink_subnode']} | "
                f"{s['material_or_energy']} | {s['quantity']} | {s['evidence_class']} | "
                f"**{s['edge_state']}** | {s['primary_credit_owner']} | "
                f"{s['candidate_allocation_owner']} |"
            )

    lines += [
        "",
        "## Edge-state distribution",
        "",
        "| Edge state | Count |",
        "| --- | --- |",
    ]
    for k, v in sorted(c["by_edge_state"].items()):
        lines.append(f"| {k} | {v} |")
    lines += [
        "",
        f"**{c['streams_total']} streams** = "
        f"{c['physical_streams']} physical + {c['opportunity_streams']} opportunity. "
        f"**{c['streams_realizing_credit']} realize credit** "
        f"(credit requires `MEASURED_PHYSICAL`).",
        "",
        "## Evidence-class distribution",
        "",
        "| Class | Count |",
        "| --- | --- |",
    ]
    for k, v in sorted(c["by_evidence_class"].items()):
        lines.append(f"| {k} | {v} |")

    lines += [
        "",
        "## Flywheel layers (derived from the register, not hand-written)",
        "",
        "| # | Layer | Subnodes | Streams | Physical | Realized credit | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for n, lay in res["flywheel_layers"].items():
        lines.append(
            f"| {n} | {lay['layer']} | {', '.join(lay['subnodes']) or '—'} | "
            f"{lay['streams']} | {lay['physical_streams']} | {lay['realized_credit']} | "
            f"**{lay['status']}** |"
        )

    np = res["node_pass"]
    lines += [
        "",
        "## Veto evaluation",
        "",
        f"> {np['rule']}",
        "",
        "| Veto | State | Why |",
        "| --- | --- | --- |",
    ]
    for vid, v in res["vetoes"].items():
        lines.append(f"| `{vid}` | **{v['state']}** | {v['why']} |")
    lines += [
        "",
        f"**Verdict: `{np['verdict']}`**",
        "",
        np["explanation"],
        "",
        "## Scale comparison",
        "",
        "| Quantity | Value |",
        "| --- | --- |",
    ]
    for k, v in res["scale"].items():
        if k in ("finding", "e02_note"):
            continue
        lines.append(f"| `{k}` | {v} |")
    lines += [
        "",
        res["scale"]["e02_note"],
        "",
        res["scale"]["finding"],
        "",
        "## Pareto rule",
        "",
        res["pareto_rule"],
        "",
        "## What this changes",
        "",
        res["what_this_changes"],
        "",
        "## Next receipts",
        "",
    ]
    lines += [f"- {item}" for item in res["next_receipts"]]
    lines.append("")
    return "\n".join(lines)


def _receipts_markdown() -> str:
    """Render the field-research receipt ledger."""
    from models import receipts as rc

    s = rc.round_summary()
    lines = [
        "# Field Research Receipt Ledger — Round 1",
        "",
        f"**Reviewer:** {s['reviewer']}",
        f"**Questions answered:** {s['questions_answered']}",
        "",
        "A **NULL** is a receipt, not a failure: it says the connection is not yet "
        "real. A **FOUND-CONTRADICTS** is the most valuable outcome, because it "
        "corrects an assumption before that assumption propagates to 120 localities.",
        "",
        "## Outcomes",
        "",
        "| Outcome | Count |",
        "| --- | --- |",
    ]
    for k, v in s["outcomes"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Contradictions found",
        "",
        "| ID | Assumption overturned |",
        "| --- | --- |",
    ]
    for r in rc.contradictions():
        lines.append(f"| {r['qid']} | {r['finding'].replace(chr(124), chr(92) + chr(124))} |")

    lines += [
        "",
        "## Receipts",
        "",
        "| ID | Outcome | Question | Evidence | Finding |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in rc.receipts():
        finding = r["finding"].replace("|", "\\|").replace("\n", " ")
        if len(finding) > 400:
            finding = finding[:397] + "..."
        lines.append(
            f"| {r['qid']} | **{r['outcome']}** | {r['question']} | "
            f"{r['evidence_class']} | {finding} |"
        )

    lines += [
        "",
        "## Effect on the register",
        "",
        "| ID | Effect |",
        "| --- | --- |",
    ]
    for r in rc.receipts():
        if r["effect_on_register"]:
            eff = r["effect_on_register"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {r['qid']} | {eff} |")

    lines += ["", "## Interpretation", "", s["interpretation"], "",
              "## Discipline", "", s["discipline_note"], ""]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("manifest", help="regenerate sources/source_manifest.json")
    sub.add_parser("reproduce", help="reproduce every derived number")
    sub.add_parser("validate", help="run the validator gate suite")
    sub.add_parser("unknowns", help="emit the unresolved-UNKNOWN ledger")
    sub.add_parser("resources", help="run the Run 6 resource and ecology modules")
    sub.add_parser("locality", help="emit the Dongjiakou locality stream register")
    sub.add_parser("receipts", help="emit the field-research receipt ledger")
    sub.add_parser("all", help="manifest + reproduce + validate + unknowns")
    packet_p = sub.add_parser("packet", help="offline OS integration review envelope")
    packet_p.add_argument("--revision")
    qol_p = sub.add_parser("qol", help="first-class human/ecological outcome vector")
    qol_p.add_argument("scenario", nargs="?", type=Path)
    sub.add_parser("current", help="reviewed current locality overlay as JSON")
    gap_p = sub.add_parser("gap", help="needs-matched resource-gap scenario as JSON")
    gap_p.add_argument("scenario", type=Path)
    run_p = sub.add_parser("run", help="print one run's result")
    run_p.add_argument("run_id", choices=sorted(RUN_REGISTRY))
    run_p.add_argument("--param", action="append", default=[], metavar="KEY=VALUE")

    args = parser.parse_args(argv)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.command == "packet":
        from models.integration import packet
        print(json.dumps(packet(args.revision),indent=2,allow_nan=False))
        return 0

    if args.command == "qol":
        from models.qol import evaluate
        case = json.loads(args.scenario.read_text()) if args.scenario else None
        print(json.dumps(evaluate(case), indent=2, allow_nan=False))
        return 0

    if args.command == "current":
        from models.current_state import run
        print(json.dumps(run(), indent=2))
        return 0

    if args.command == "gap":
        from resource_gap.simulate import read_case, simulate
        case, sha = read_case(args.scenario)
        print(json.dumps(simulate(case, sha), indent=2, allow_nan=False))
        return 0

    if args.command == "manifest":
        path = loader.write_manifest()
        print(f"wrote {path}")
        return 0

    if args.command == "run":
        kwargs: dict[str, Any] = {}
        for item in args.param:
            key, _, raw = item.partition("=")
            try:
                kwargs[key] = json.loads(raw)
            except json.JSONDecodeError:
                kwargs[key] = raw
        result = RUN_REGISTRY[args.run_id](**kwargs) if kwargs else RUN_REGISTRY[args.run_id]()
        print(json.dumps(to_jsonable(result), indent=2))
        return 0

    if args.command == "reproduce":
        report = reproduce()
        (REPORTS_DIR / "REPRODUCTION_REPORT.json").write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8")
        (REPORTS_DIR / "RUN_0-3_REPRODUCTION_REPORT.md").write_text(
            _reproduction_markdown(report), encoding="utf-8")
        print(f"{report['status']}: {report['totals']['matched']}/{report['totals']['checks']} "
              f"derived values reproduced across {report['totals']['runs']} runs")
        return 0 if report["totals"]["mismatched"] == 0 else 1

    if args.command == "validate":
        as_dict, report = validate_all()
        (REPORTS_DIR / "VALIDATION_REPORT.json").write_text(
            json.dumps(as_dict, indent=2) + "\n", encoding="utf-8")
        (REPORTS_DIR / "VALIDATION_REPORT.md").write_text(report.to_markdown(), encoding="utf-8")
        print(f"{as_dict['status']}: {report.counts}")
        return 0 if report.passed else 1

    if args.command == "unknowns":
        ledger = unknown_ledger()
        (REPORTS_DIR / "UNKNOWN_LEDGER.json").write_text(
            json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
        (REPORTS_DIR / "UNKNOWN_LEDGER.md").write_text(_unknown_markdown(ledger), encoding="utf-8")
        print(f"unknown ledger written: {ledger['counts']}")
        return 0

    if args.command == "resources":
        from models import run6_resources

        res = run6_resources.run()
        (REPORTS_DIR / "RUN_6_RESOURCE_MODULES.json").write_text(
            json.dumps(to_jsonable(res), indent=2) + "\n", encoding="utf-8")
        (REPORTS_DIR / "RUN_6_RESOURCE_MODULES.md").write_text(
            _resources_markdown(res), encoding="utf-8")
        print(f"resources: {res['summary']['modules_instantiated']} modules, "
              f"{res['summary']['modules_eligible_for_value']} eligible for value, "
              f"credit {res['summary']['total_value_credit']}")
        return 0

    if args.command == "locality":
        from models import locality

        res = locality.run()
        (REPORTS_DIR / "LOCALITY_STREAM_REGISTER.json").write_text(
            json.dumps(to_jsonable(res), indent=2) + "\n", encoding="utf-8")
        (REPORTS_DIR / "LOCALITY_STREAM_REGISTER.md").write_text(
            _locality_markdown(res), encoding="utf-8")
        print(f"locality: {res['counts']['streams_total']} streams "
              f"({res['counts']['physical_streams']} physical / "
              f"{res['counts']['opportunity_streams']} opportunity), "
              f"{res['counts']['streams_realizing_credit']} realizing credit, "
              f"clearance {res['clearance']['LOCALITY_CLEARANCE']['answer']}")
        return 0

    if args.command == "receipts":
        from models import receipts as _rc

        summary = _rc.round_summary()
        (REPORTS_DIR / "FIELD_RESEARCH_RECEIPTS.json").write_text(
            json.dumps(to_jsonable({"summary": summary,
                                    "receipts": _rc.receipts()}), indent=2) + "\n",
            encoding="utf-8")
        (REPORTS_DIR / "FIELD_RESEARCH_RECEIPTS.md").write_text(
            _receipts_markdown(), encoding="utf-8")
        counts = summary["outcomes"]
        print(f"receipts: {summary['questions_answered']} answered | "
              f"{counts['FOUND']} found, {counts['FOUND-CONTRADICTS']} contradicted, "
              f"{counts['NULL']} null, {counts['UNKNOWN-BUT-LEAD']} leads, "
              f"{counts['UNKNOWN']} unknown")
        return 0

    # all
    rc = 0
    print(f"wrote {loader.write_manifest()}")
    report = reproduce()
    (REPORTS_DIR / "REPRODUCTION_REPORT.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "RUN_0-3_REPRODUCTION_REPORT.md").write_text(
        _reproduction_markdown(report), encoding="utf-8")
    print(f"reproduce: {report['status']} "
          f"({report['totals']['matched']}/{report['totals']['checks']})")
    rc |= 0 if report["totals"]["mismatched"] == 0 else 1

    as_dict, vreport = validate_all()
    (REPORTS_DIR / "VALIDATION_REPORT.json").write_text(
        json.dumps(as_dict, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "VALIDATION_REPORT.md").write_text(vreport.to_markdown(), encoding="utf-8")
    print(f"validate: {as_dict['status']} {vreport.counts}")
    rc |= 0 if vreport.passed else 1

    ledger = unknown_ledger()
    (REPORTS_DIR / "UNKNOWN_LEDGER.json").write_text(
        json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "UNKNOWN_LEDGER.md").write_text(_unknown_markdown(ledger), encoding="utf-8")
    print(f"unknowns: {ledger['counts']}")

    from models import run6_resources

    res = run6_resources.run()
    (REPORTS_DIR / "RUN_6_RESOURCE_MODULES.json").write_text(
        json.dumps(to_jsonable(res), indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "RUN_6_RESOURCE_MODULES.md").write_text(
        _resources_markdown(res), encoding="utf-8")
    print(f"resources: {res['summary']['modules_instantiated']} modules, "
          f"{res['summary']['modules_eligible_for_value']} eligible for value")

    from models import locality

    loc = locality.run()
    (REPORTS_DIR / "LOCALITY_STREAM_REGISTER.json").write_text(
        json.dumps(to_jsonable(loc), indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "LOCALITY_STREAM_REGISTER.md").write_text(
        _locality_markdown(loc), encoding="utf-8")
    print(f"locality: {loc['counts']['streams_total']} streams, "
          f"{loc['counts']['streams_realizing_credit']} realizing credit, "
          f"clearance {loc['clearance']['LOCALITY_CLEARANCE']['answer']}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
