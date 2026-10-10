"""Candidate policy checks; no labor, safety or deployment authorization."""
from datetime import date
import math

def assess(case, as_of):
    today=date.fromisoformat(as_of)
    if not isinstance(case.get("sector"),str) or not case["sector"].strip():
        raise ValueError("sector required")
    for key in ("active_hours_day","break_hours_day","workdays_week"):
        v=case.get(key)
        if v is not None and (isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0):
            raise ValueError(key)
    days=case.get("workdays_week")
    if days is not None and (days>7 or int(days)!=days):
        raise ValueError("workdays_week")
    for key in ("qualified_workforce_gap","alternatives_exhausted","legal_clearance","recovery_clearance"):
        if case.get(key) is not None and type(case[key]) is not bool:
            raise ValueError(key)
    active=case.get("active_hours_day")
    breaks=case.get("break_hours_day")
    span=active+breaks if active is not None and breaks is not None else None
    weekly=active*days if active is not None and days is not None else None
    extended=active is not None and active>8
    gap=case.get("qualified_workforce_gap")
    flag=gap is True or (extended and gap is not False)
    reasons=[]
    if span is not None and span>12: reasons.append("TOTAL_SHIFT_SPAN_EXCEEDS_12H")
    if days is not None and days>5: reasons.append("FIVE_DAY_CEILING_EXCEEDED")
    if active is None or breaks is None or days is None:
        status="UNKNOWN"
    elif reasons:
        status="BLOCKED"
    elif extended:
        requirements=("qualified_workforce_gap","alternatives_exhausted","legal_clearance","recovery_clearance")
        for key in requirements:
            if case.get(key) is not True: reasons.append(key.upper()+"_NOT_RECEIPTED_TRUE")
        for key in ("accountable_owner","training_plan","recruitment_plan","evidence_receipts"):
            if not case.get(key): reasons.append(key.upper()+"_MISSING")
        try:
            expiry=date.fromisoformat(case.get("exception_expiry",""))
            if expiry<=today: reasons.append("EXCEPTION_EXPIRED")
        except (TypeError,ValueError): reasons.append("EXCEPTION_EXPIRY_MISSING_OR_INVALID")
        status="BLOCKED" if reasons else "CANDIDATE_EXCEPTION_FOR_REVIEW"
    elif weekly is not None and weekly<=40:
        status="STANDARD_HOURS_POLICY_MATCH"
    else:
        status="BLOCKED"
    return {"sector":case["sector"],"policy_status":status,"total_shift_span_hours":span if span is not None else "UNKNOWN",
        "weekly_active_hours":weekly if weekly is not None else "UNKNOWN","reasons":reasons,
        "automatic_workforce_action_flag":flag,
        "workforce_action":("ASSESS_GAP_AND_TRAIN_OR_RECRUIT_QUALIFIED_RELIEF" if flag else "NONE_TRIGGERED"),
        "gap_evidence":"PROPOSED_ASSESSMENT" if flag and gap is None else ("SCENARIO_INPUT" if gap is not None else "UNKNOWN"),
        "legal_authorization":"UNKNOWN","deployment_status":"UNVERIFIED","realized_credit":0}

def run(config):
    if config.get("evidence_class") not in ("UNKNOWN","SIMULATED"):
        raise ValueError("only UNKNOWN or SIMULATED policy scenarios")
    return {"module":"RECOVERY_POLICY_v0.11","evidence_class":config["evidence_class"],
        "default":"8h work / 8h family and recreation / 8h sleep opportunity; <=5 workdays/week",
        "exception_total_span_ceiling_hours":12,"as_of":config["as_of"],
        "sectors":[assess(c,config["as_of"]) for c in config["sectors"]],"realized_credit":0}
