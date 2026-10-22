#!/usr/bin/env python3
"""DJK S01 v0.3: integrated synthetic chemistry -> qualification -> 30y allocation.
Research only; no plant, soil, hub, shell, acid or customs claim is verified.
"""
import json,sys
from pathlib import Path
CA, SO4, GYP, H2SO4, S, CACO3, CO2 = 40.078,96.06,172.171,98.079,32.065,100.087,44.01

def run(d):
    n=int(d["years"]); assert 1<=n<=100
    f=d["brine"]; q=f["m3_day"]; ca=f["calcium_mg_l"]; so=f["sulfate_mg_l"]
    assert q>=0 and 0<=f["recovery_fraction"]<=1
    if ca is None or so is None:
        return {"status":"EVIDENCE_GATES_CLOSED","realized_t":0,"brine_gypsum_t_y":None,
                "reason":"No measured Ca/SO4 and metered brine flow; no realized allocation"}
    assert ca>=0 and so>=0
    # q(m3/d)*concentration(mg/L)/atomic mass (g/mol) gives mol/day.
    gyp=min(q*ca/CA,q*so/SO4)*GYP/1e6*f["days_year"]*f["recovery_fraction"]
    qualified=f["batch_assay_pass"] is True and f["lab_measured"] is True
    # When a batch is unqualified, it cannot be labeled a usable product.
    shell=d["shell"]
    shell_available=max(0,shell["wet_shell_t_y"]*shell["dry_fraction"]*shell["caco3_fraction"])
    shell_qualified=(shell["assay_pass"] is True and shell["soil_acidic_test_pass"] is True
                     and shell["field_trial_pass"] is True)
    # Shell CaCO3 does not substitute for CaSO4 on alkaline sodic fields.
    shell_acid=shell["recovered_sulfuric_acid_t_y"]
    assert shell_acid>=0
    # Only if independently certified waste-acid and shell conversion are operational.
    shell_react=(min(shell_available/CACO3,shell_acid/H2SO4)*GYP
        if shell["acid_assay_pass"] and shell["conversion_qualified"] else 0.0)
    # Acid is a reagent INPUT; resulting gypsum contains inherited sulfur, never new sulfur credit.
    shell_acid_consumed=shell_react*H2SO4/GYP
    shell_co2=shell_react*CO2/GYP
    industrial=d["industrial"]; acid_yield=d["acid_t_per_brine_dry_gypsum_t"]
    assert 0<=acid_yield<=H2SO4/GYP
    hub=(industrial["measured_batch_assay_pass"] is True and industrial["hub_acceptance"] is True)
    national=d["national_sulfur"]; shortfall=national["balance_s_t_y"] is not None and national["balance_s_t_y"]<0
    cap=d["ag_fraction_cap_when_short"] if shortfall else 1
    assert 0<=cap<=1
    inv=0.0; rows=[]
    for year in range(1,n+1):
        produced=gyp if qualified else 0.0
        # Unqualified precipitate is residual to be contained; NOT free inventory.
        unqualified=gyp-produced
        eligible=0.0
        for z in d["soil_classes"]:
            if (z["soil_measured"] and z["sodic_reclamation_verified"] and z["gypsum_batch_safe"]
                and z["trial_verified"] and z["drainage_safe"] and z["farm_consent"]):
                initial=z["ha"]*z["initial_t_ha"]*(1-z["decline"])**(year-1) if year<=z["reclamation_years"] else 0
                eligible+=initial+z["ha"]*z["maintenance_t_ha_y"]
        available=produced+inv
        ag=min(available,eligible,available*cap)
        acid_feed=(available-ag) if hub else 0.0
        inv=available-ag-acid_feed
        assert abs(produced+(rows[-1]["ending_inventory_t"] if rows else 0)-ag-acid_feed-inv)<0.002
        rows.append({"year":year,"brine_gypsum_produced_t":round(gyp,3),
          "qualified_gypsum_t":round(produced,3),"unqualified_residual_t":round(unqualified,3),
          "eligible_sodic_soil_gypsum_demand_t":round(eligible,3),
          "gypsum_to_soil_t":round(ag,3),"gypsum_to_acid_hub_t":round(acid_feed,3),
          "potential_acid_from_BRINE_sulfur_t":round(acid_feed*acid_yield,3),
          "ending_inventory_t":round(inv,3),"realized_t":0})
    return {"status":"SYNTHETIC_ZERO_REALIZED","annual_max_dry_gypsum_t":round(gyp,3),
      "chemical_limiting":"calcium" if q*ca/CA<=q*so/SO4 else "sulfate",
      "shell":{"nominal_dry_caco3_t_y":round(shell_available,3),
         "soil_qualified":shell_qualified,
         "potential_shell_gypsum_t_y":round(shell_react,3),
         "spent_sulfuric_acid_input_t_y":round(shell_acid_consumed,3),
         "reaction_co2_t_y":round(shell_co2,3),
         "shell_gypsum_counted_as_NEW_sulfur_t":0},
      "annual":rows,"national_export_authorized":False,
      "notes":["No gypsum/shell substitution on alkaline sodic soils without trial; shell soil trial here is acidic-soil only.",
       "Sulfuric acid used to dissolve shell calcium carbonate provides sulfate; do not re-credit as newly recovered sulfur.",
       "Unqualified material treated as a residual requiring lawful management, not indefinitely stockpiled.",
       "National import displacement stays zero until traceable buyer and national customs receipts."]}

if __name__=="__main__":
    path=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name("integrated_synthetic.json"))
    print(json.dumps(run(json.loads(path.read_text())),indent=2))
