#!/usr/bin/env python3
"""Dongjiakou Node-001 v2: v1-preserving unified locality + QOL + ecology + funding view.
Proposed research simulator only: NOT cleared for deployment; NOT an operator.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from models import locality, run6_resources
from models.common import to_jsonable
from qol_ecology.companion import calculate as qoleco_calculate

ROOT=Path(__file__).resolve().parent
DEFAULT_SCENARIO=ROOT/"qol_ecology"/"dongjiakou_candidate.json"

def funding_decision(qol, *, authorized_public_budget=None, verified_financing=None):
    """Benefit is a first-class decision input, never a fabricated cash receipt.
    Unknown budget/need => decision PENDING, never FUNDED.
    """
    fin=qol["finance"]
    gap=fin["unfunded_remainder"]
    services=qol["program_count"]
    if authorized_public_budget is not None or verified_financing is not None:
        # v2 deliberately does not accept caller-injected 'verified' status as a receipt
        raise ValueError("Authorised financing requires an independent receipt-verified finance module")
    return {
        "qol_first_class": True, "cost_gap":gap, "cost_basis":fin["basis"],
        "funding_required":gap, "funding_source_verified":False,
        "quality_of_life_programs":services,
        "ecological_value_monetized":False,
        "assessment":"PUBLIC_BENEFIT_REVIEW_REQUIRED",
        "decision":"PENDING_DATA_AND_AUTHORIZATION",
        "explanation":"Non-commercial benefits can justify a subsidy proposal but cannot mechanically fill a cash budget gap."
    }

def run_v2(scenario=None):
    scenario=Path(scenario or DEFAULT_SCENARIO)
    payload=json.loads(scenario.read_text(encoding="utf-8"))
    if payload.get("locality_id")!="DJK-001":
        # Generic locality portability will require a corresponding v1 physical inventory.
        raise ValueError("v2 Dongjiakou physical baseline cannot be relabeled as another locality")
    v1_locality=to_jsonable(locality.run())
    v1_resource=to_jsonable(run6_resources.run())
    social=qoleco_calculate(payload)
    # No v1 physical values, status or bookkeeping are changed by integration.
    return {"version":"2.0-alpha","locality_id":"DJK-001",
        "evidence_class":"PROPOSED","canonical":False,"deployment":False,
        "baseline":{"v1_locality":v1_locality,"v1_resources":v1_resource},
        "modules":{"QOL01":{"status":"PROPOSED","metrics":social},
                   "ECO01":{"status":"PROPOSED","outfalls":social["outfalls"]},
                   "FUND01":{"status":"PROPOSED","decision":funding_decision(social)}},
        "funding_review":funding_decision(social),
        "realized_credit":0,"locality_clearance":"NOT_ESTABLISHED",
        "no_double_count":"Non-monetary benefit is shown separately from commercial revenues and financing.",
        "source_ids":[x["id"] for x in payload["sources"]]}

def main(argv=None):
    argv=list(argv or sys.argv[1:])
    if len(argv)>1: raise SystemExit("Usage: simulator_v2.py [scenario.json]")
    print(json.dumps(run_v2(argv[0] if argv else None),indent=2,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
