"""v2 regression/conservation checks; run under pytest in existing test suite."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import pytest
from simulator_v2 import run_v2, funding_decision, DEFAULT_SCENARIO
from models import locality, run6_resources
from models.common import to_jsonable

def test_v2_preserves_locality_physical_register():
    v2=run_v2()
    assert v2["baseline"]["v1_locality"]==to_jsonable(locality.run())
    assert v2["baseline"]["v1_resources"]==to_jsonable(run6_resources.run())
    assert v2["realized_credit"]==0
    assert v2["locality_clearance"]=="NOT_ESTABLISHED"

def test_qol_is_first_class():
    result=run_v2()
    assert set(result["modules"])=={"QOL01","ECO01","FUND01"}
    assert result["modules"]["QOL01"]["metrics"]["program_count"]>=5
    assert result["funding_review"]["qol_first_class"] is True
    assert result["funding_review"]["decision"]=="PENDING_DATA_AND_AUTHORIZATION"

def test_no_budget_fabrication():
    result=run_v2()
    assert result["funding_review"]["funding_required"] is None
    assert result["funding_review"]["funding_source_verified"] is False
    assert result["modules"]["ECO01"]["outfalls"][0]["nitrogen_input_t_year"] is None

def test_hypothetical_gap_stays_pending():
    q=run_v2()["modules"]["QOL01"]["metrics"]
    q=copy.deepcopy(q)
    q["finance"]={"unfunded_remainder":60.0,"basis":"TOTAL_PROJECT"}
    d=funding_decision(q)
    assert d["cost_gap"]==60
    assert d["decision"]=="PENDING_DATA_AND_AUTHORIZATION"
    assert d["ecological_value_monetized"] is False

def test_refuse_unsupported_auth_claim():
    with pytest.raises(ValueError):
        funding_decision({"finance":{"unfunded_remainder":60,"basis":"TOTAL_PROJECT"},"program_count":9},authorized_public_budget=60)

def test_cannot_relabel_dongjiakou_v1_baseline_as_mars(tmp_path):
    payload=json.loads(DEFAULT_SCENARIO.read_text())
    payload["locality_id"]="MARS-001"
    scenario=tmp_path/"mars.json"
    scenario.write_text(json.dumps(payload))
    with pytest.raises(ValueError,match="relabeled"): run_v2(scenario)
