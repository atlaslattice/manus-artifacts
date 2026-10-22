"""Protected recovery, qualified capacity and cohort-specific QOL scenarios."""
import math
from copy import deepcopy
from .funding import evaluate as funding_evaluate
UNKNOWN = "UNKNOWN"
STUDIES = {
    "TAICHI2018": {"population":"High-fall-risk community-dwelling older adults; 670 participants",
        "intervention":"Tailored tai ji quan, two 60-minute classes/week, 24 weeks",
        "endpoint":"fall_incidence", "source":"https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2701631"},
    "SAUNA2022": {"population":"47 low-activity adults, mean age49, >=1 cardiovascular risk factor",
        "intervention":"Exercise plus postexercise sauna, eight weeks",
        "endpoint":"cardiorespiratory_fitness", "source":"https://journals.physiology.org/doi/prev/20220704-aop/abs/10.1152/ajpregu.00076.2022"},
    "COLD2016": {"population":"3018 adults18-65 without severe comorbidity",
        "intervention":"Hot-to-cold showers; not communal contrast immersion",
        "endpoint":"self_reported_sickness_absence", "source":"https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0161749"},
    "SOUND2017": {"population":"14 participants in a controlled binaural/acoustic beat experiment",
        "intervention":"Specific beat frequencies; null EEG/arousal enhancement",
        "endpoint":"eeg_band_power", "source":"https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2017.00557/full"}
}
def number(value, name, fraction=False, signed=False):
    if value is None:
        return None
    if type(value) not in (int,float) or not math.isfinite(value):
        raise ValueError(name + ": finite number required")
    if not signed and value < 0:
        raise ValueError(name + ": negative value")
    if fraction and not 0 <= value <= 1:
        raise ValueError(name + ": fraction outside [0,1]")
    if signed and not -1 <= value <= 1:
        raise ValueError(name + ": effect outside [-1,1]")
    return value

def validate(config):
    if config["scenario_kind"] not in ("LOCAL_UNKNOWN","HYPOTHETICAL_SENSITIVITY"):
        raise ValueError("No local measured QOL scenario is supported")
    if not config.get("basis"):
        raise ValueError("Scenario basis required")
    if config.get("program_weekly_workdays_ceiling") != 5:
        raise ValueError("Candidate programme requires a five-day weekly work ceiling")
    if config.get("contractual_paid_leave_floor_working_days") != 10:
        raise ValueError("Candidate leave floor is ten working days, subject to entitlement audit")
    local = config["scenario_kind"] == "LOCAL_UNKNOWN"
    digital=config["digital_inclusion"]
    if digital["access_conditioned_on_research_consent"] is not False:
        raise ValueError("Basic digital access cannot depend on research consent")
    if digital["personal_memory_export_to_research"] is not False:
        raise ValueError("Private agent memory is separate from research")
    if digital["anonymization_verified"] != "UNKNOWN":
        raise ValueError("No anonymization assurance receipt exists")
    for key in ("resident_population","phone_inventory","computer_inventory",
                "annual_connectivity_cny","annual_device_amortization_cny",
                "annual_compute_cny","annual_support_cny"):
        number(digital[key],key)
        if local and digital[key] is not None:
            raise ValueError("Local digital provision/cost receipt missing")
    cohorts = config["cohorts"]
    ids = [c["cohort_id"] for c in cohorts]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate cohort")
    roles = config["operations"]["roles"]
    if len(roles) != len(set(roles)):
        raise ValueError("Duplicate role")
    for role, r in roles.items():
        number(r["qualified_hours_day"],role)
        if not r.get("provider") or not r.get("assessment_requirement") or not r.get("renewal_requirement"):
            raise ValueError("Training provider, assessment and renewal fields required")
        if local and r["qualified_hours_day"] is not None:
            raise ValueError("Local qualification receipt missing")
    services = config["operations"]["services"]
    service_ids = [s["service_id"] for s in services]
    if len(service_ids) != len(set(service_ids)):
        raise ValueError("Duplicate service")
    booked = {r:0 for r in roles}
    for s in services:
        number(s["equipment_capacity_participant_sessions_day"],s["service_id"])
        gate = s["safe_operation_gate"]
        if gate is not None and type(gate) is not bool:
            raise ValueError("Safety gate must be bool or null")
        if local and (gate is not None or s["equipment_capacity_participant_sessions_day"] is not None):
            raise ValueError("No local operating receipt")
        if not s["requirements"]:
            raise ValueError("Every service needs qualified operators")
        for r in s["requirements"]:
            if r["role_id"] not in roles:
                raise ValueError("Unknown operator role")
            a=number(r["allocated_qualified_hours_day"],"allocation")
            t=number(r["qualified_hours_per_participant_session"],"role labor coefficient")
            if t == 0:
                raise ValueError("Role labor denominator must be positive")
            if local and (a is not None or t is not None):
                raise ValueError("No local staffing/task-time receipt")
            if a is not None:booked[r["role_id"]]+=a
    for r,h in booked.items():
        available=roles[r]["qualified_hours_day"]
        if available is not None and h > available + 1e-9:
            raise ValueError("Shared qualified hours double-booked: "+r)
    for c in cohorts:
        for k in ("population","work_hours_day","sleep_opportunity_hours_day",
                  "actual_sleep_hours_day","commute_hours_day","care_chores_hours_day",
                  "intershift_off_duty_hours","on_site_break_hours_day","workdays_week"):
            v=number(c[k],k)
            if k != "population" and v is not None and v > 24:
                raise ValueError("Hours exceed24")
            if local and v is not None:
                raise ValueError("Local cohort/time-use receipt missing")
        if c["workdays_week"] is not None and (c["workdays_week"] > 5 or int(c["workdays_week"]) != c["workdays_week"]):
            raise ValueError("Scheduled workdays must be an integer no greater than five")
        if c["work_hours_day"] is not None and c["on_site_break_hours_day"] is not None and c["work_hours_day"] + c["on_site_break_hours_day"] > 24:
            raise ValueError("On-site work and break span exceeds24h")
        if c["actual_sleep_hours_day"] is not None and c["sleep_opportunity_hours_day"] is not None and c["actual_sleep_hours_day"] > c["sleep_opportunity_hours_day"]:
            raise ValueError("Actual sleep exceeds stated opportunity")
        leave=number(c["statutory_leave_working_days"],"statutory leave")
        if leave is not None and (leave>248 or int(leave)!=leave):
            raise ValueError("Full-year leave planning input must be whole working days")
        if local and leave is not None:
            raise ValueError("Local leave eligibility/tenure receipt missing")
    shares = {s:0 for s in service_ids}
    for e in config["effects"]:
        if e["cohort_id"] not in ids or e["service_id"] not in service_ids or e["study_id"] not in STUDIES:
            raise ValueError("Unknown cohort, service or study")
        if e["endpoint"] != STUDIES[e["study_id"]]["endpoint"]:
            raise ValueError("Study endpoint mismatch")
        if e["transfer_status"] != "UNKNOWN":
            raise ValueError("Local trial equivalence is not established")
        for k in ("eligible_fraction","adoption","adherence","capacity_share"):
            v=number(e[k],k,fraction=True)
            if local and v is not None:raise ValueError("No local coverage receipt")
        if e["capacity_share"] is not None:shares[e["service_id"]]+=e["capacity_share"]
        effect=number(e["relative_effect"],"relative_effect",signed=True)
        if effect is not None and (local or e["effect_evidence_class"] != "SENSITIVITY"):
            raise ValueError("No local efficacy receipt; hypothetical effects are SENSITIVITY")
        if effect is None and e["effect_evidence_class"] != "UNKNOWN":
            raise ValueError("Null effect must be UNKNOWN")
    if any(s>1+1e-9 for s in shares.values()):
        raise ValueError("Service capacity assigned more than once")
    return config

def operations(config):
    out = {}
    roles = config["operations"]["roles"]
    for s in config["operations"]["services"]:
        if s["safe_operation_gate"] is False:
            capacity=0
            reason="Explicitly closed safety gate; no service"
        else:
            vals=[s["equipment_capacity_participant_sessions_day"]]
            for r in s["requirements"]:
                a,t=r["allocated_qualified_hours_day"],r["qualified_hours_per_participant_session"]
                available=roles[r["role_id"]]["qualified_hours_day"]
                vals.append(None if None in (a,t,available) else a/t)
            capacity = UNKNOWN if s["safe_operation_gate"] is not True or any(v is None for v in vals) else min(vals)
            reason="UNKNOWN until safe operation, qualified available hours and all task coefficients are supplied"
        out[s["service_id"]]={"capacity_participant_sessions_day":capacity,"basis":reason,"realized_credit":0}
    return {"module":"OPS01","roles":deepcopy(roles),"services":out,"realized_credit":0,
            "qualification_rule":"Course attendance or training hours do not establish qualification; assessed competence and renewal receipts required"}

def run(config):
    validate(config)
    ops=operations(config)
    cohorts=[]
    byid={c["cohort_id"]:c for c in config["cohorts"]}
    for c in config["cohorts"]:
        w,s,t,h=[c[k] for k in ("work_hours_day","sleep_opportunity_hours_day","commute_hours_day","care_chores_hours_day")]
        b=c["on_site_break_hours_day"]
        d=c["workdays_week"]
        leave=c["statutory_leave_working_days"]
        span=UNKNOWN if None in (w,b) else w+b
        personal=UNKNOWN if None in (w,s,b) else 24-w-s-b
        discretionary=UNKNOWN if None in (w,s,t,h,b) else 24-w-s-t-h-b
        rest=c["intershift_off_duty_hours"]
        cohorts.append({"cohort_id":c["cohort_id"],"definition":c["definition"],
            "population":UNKNOWN if c["population"] is None else c["population"],
            "on_site_span_hours_day":span,
            "weekly_active_work_hours":UNKNOWN if None in (w,d) else w*d,
            "weekly_on_site_span_hours":UNKNOWN if span==UNKNOWN or d is None else span*d,
            "candidate_paid_leave_working_days":"NOT_APPLICABLE" if d==0 else UNKNOWN if leave is None else max(10,leave),
            "candidate_paid_leave_five_day_weeks":"NOT_APPLICABLE" if d==0 else UNKNOWN if leave is None else max(10,leave)/5,
            "nominal_annual_attendance_days_reference":"NOT_APPLICABLE" if d==0 else UNKNOWN if leave is None else 248-max(10,leave),
            "leave_note":"Full-year reference only; eligibility/proration and actual calendar/roster audit pending. Public holidays and weekly rest excluded from annual leave. Operator available hours must also subtract training, absence and relief needs.",
            "above_40h_standard_reference":UNKNOWN if None in (w,d) else w*d>40,
            "personal_hours_including_obligations":personal,
            "discretionary_hours_after_commute_and_care":discretionary,
            "time_budget_feasible":UNKNOWN if discretionary==UNKNOWN else discretionary>=0,
            "sleep_opportunity_hours_day":UNKNOWN if s is None else s,
            "actual_sleep_hours_day":UNKNOWN if c["actual_sleep_hours_day"] is None else c["actual_sleep_hours_day"],
            "niosh_10h_off_duty_reference_met":UNKNOWN if rest is None else rest>=10,
            "note":"Off-duty time is a roster input; on-site breaks are not family time. 40h is a standard-work reference, not a complete legality determination. NIOSH is guidance, not Chinese law."})
    outcomes=[]
    for e in config["effects"]:
        n=byid[e["cohort_id"]]["population"]
        inputs=(n,e["eligible_fraction"],e["adoption"],e["adherence"])
        demand=UNKNOWN if any(v is None for v in inputs) else math.prod(inputs)
        capacity=ops["services"][e["service_id"]]["capacity_participant_sessions_day"]
        share=e["capacity_share"]
        served=UNKNOWN if demand==UNKNOWN or capacity==UNKNOWN or share is None else min(demand,capacity*share)
        delta=UNKNOWN if served==UNKNOWN or n in (None,0) or e["relative_effect"] is None else served/n*e["relative_effect"]*100
        outcomes.append({"cohort_id":e["cohort_id"],"study_id":e["study_id"],"source_evidence":STUDIES[e["study_id"]],
            "endpoint":e["endpoint"],"transfer_status":"UNKNOWN",
            "eligible_adherent_demand_participant_sessions_day":demand,
            "capacity_limited_participant_sessions_day":served,
            "scenario_endpoint_change_percent_within_cohort":delta,
            "effect_evidence_class":e["effect_evidence_class"],"realized_credit":0})
    d=config["digital_inclusion"]
    n=d["resident_population"]
    digital_out={"module":"DIG01","inputs":deepcopy(d),
        "phone_inventory_capacity_percent":UNKNOWN if n in (None,0) or d["phone_inventory"] is None else min(100,100*d["phone_inventory"]/n),
        "computer_inventory_capacity_percent":UNKNOWN if n in (None,0) or d["computer_inventory"] is None else min(100,100*d["computer_inventory"]/n),
        "annual_operating_and_amortized_cost_cny":UNKNOWN if any(d[k] is None for k in ("annual_connectivity_cny","annual_device_amortization_cny","annual_compute_cny","annual_support_cny")) else sum(d[k] for k in ("annual_connectivity_cny","annual_device_amortization_cny","annual_compute_cny","annual_support_cny")),
        "actual_resident_access":"UNKNOWN","anonymization_verified":"UNKNOWN",
        "agent_task_or_health_performance_gain":"UNKNOWN","realized_credit":0}
    return {"module":"QOL01","scenario_id":config["scenario_id"],"scenario_kind":config["scenario_kind"],
        "basis":config["basis"],"cohorts":cohorts,"effects_by_cohort":outcomes,"operations":ops,
        "population_combined_benefit":"UNKNOWN","frequency_specific_sound_benefit":"UNKNOWN",
        "digital_inclusion":digital_out,"funding":funding_evaluate(config["funding"]),
        "realized_credit":0,"deployment":False,"canon":False}

