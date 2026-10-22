import copy
import pytest
from wellbeing.recovery_policy_v011 import assess
from simulator_recovery_policy import compose
from simulator_wellbeing import compose as previous
import json
from pathlib import Path

TODAY="2026-10-10"
def standard():
    return dict(sector="test",active_hours_day=8,break_hours_day=0,workdays_week=5,qualified_workforce_gap=False)
def exception():
    return dict(sector="test",active_hours_day=10,break_hours_day=2,workdays_week=5,
        qualified_workforce_gap=True,alternatives_exhausted=True,legal_clearance=True,recovery_clearance=True,
        accountable_owner="hypothetical",training_plan="hypothetical",recruitment_plan="hypothetical",
        evidence_receipts=["synthetic"],exception_expiry="2026-10-17")
def test_standard():
    assert assess(standard(),TODAY)["policy_status"]=="STANDARD_HOURS_POLICY_MATCH"
def test_exception_is_review_not_authorization():
    r=assess(exception(),TODAY)
    assert r["policy_status"]=="CANDIDATE_EXCEPTION_FOR_REVIEW"
    assert r["automatic_workforce_action_flag"] and r["legal_authorization"]=="UNKNOWN"
@pytest.mark.parametrize("field",["qualified_workforce_gap","alternatives_exhausted","legal_clearance","recovery_clearance","accountable_owner","training_plan","recruitment_plan","evidence_receipts","exception_expiry"])
def test_missing_exception_gate_blocks(field):
    c=exception();c.pop(field)
    assert assess(c,TODAY)["policy_status"]=="BLOCKED"
def test_fourteen_hour_case_blocked_and_flagged():
    c=exception();c["active_hours_day"]=12
    r=assess(c,TODAY)
    assert r["total_shift_span_hours"]==14 and r["policy_status"]=="BLOCKED"
    assert r["automatic_workforce_action_flag"]
def test_six_day_week_blocked():
    c=standard();c["workdays_week"]=6
    assert assess(c,TODAY)["policy_status"]=="BLOCKED"
def test_unknown_gap_is_assessment_not_measured():
    c=exception();c["qualified_workforce_gap"]=None
    r=assess(c,TODAY)
    assert r["automatic_workforce_action_flag"] and r["gap_evidence"]=="PROPOSED_ASSESSMENT"
def test_expiry_blocks():
    c=exception();c["exception_expiry"]=TODAY
    assert assess(c,TODAY)["policy_status"]=="BLOCKED"
@pytest.mark.parametrize("value",[float("nan"),float("inf"),True,-1])
def test_invalid_hours(value):
    c=standard();c["active_hours_day"]=value
    with pytest.raises(ValueError): assess(c,TODAY)
def test_unknown_local():
    assert assess({"sector":"unknown"},TODAY)["policy_status"]=="UNKNOWN"
def test_wrapper_preserves_prior_outputs():
    root=Path(__file__).resolve().parents[1]
    n=json.loads((root/"nutrition/examples/local_unknown.json").read_text())
    q=json.loads((root/"wellbeing/examples/local_unknown.json").read_text())
    old=previous(n,q)
    new=compose(n,q,{"as_of":TODAY,"evidence_class":"UNKNOWN","sectors":[{"sector":"unknown"}]})
    new["candidate_extensions"].pop("RECOVERY_POLICY_v0.11")
    assert new==old
