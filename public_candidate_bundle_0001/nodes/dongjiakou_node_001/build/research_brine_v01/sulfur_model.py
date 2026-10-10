#!/usr/bin/env python3
"""Sulfur/gypsum first-gate scenario (2026-10-09).
Explicit stream chemistry, purity, imported S displacement and at-cost supply.
Research only; NEVER infers national import elimination from one plant.
"""
import json,sys
from pathlib import Path
MCA=40.078
MSO4=96.06
MGYPSUM=172.171
MH2SO4=98.079
MS=32.065
def run(s):
    q=s["brine_m3_day"]; d=s["days_year"]
    assert q>=0 and 0<d<=366
    ca=s["calcium_mg_l"]; so4=s["sulfate_mg_l"]
    assert ca is not None and so4 is not None, "No site Ca and SO4 assays: STOP; leave unknown"
    assert ca>=0 and so4>=0
    purity=s["gypsum_purity"]; capture=s["recovered_fraction_of_limiting_reagent"]; yield_factor=s["qualified_acid_t_per_dry_gypsum_t"]
    assert 0<purity<=1 and 0<=capture<=1 and 0<=yield_factor<=MH2SO4/MGYPSUM
    ca_mol_day=q*ca/MCA # q m3/d * mg/l => q*ca grams/day; divide g/mol
    sulfate_mol_day=q*so4/MSO4
    gypsum_dry_t_y=min(ca_mol_day,sulfate_mol_day)*MGYPSUM/1e6*d*capture
    wet_gypsum_t_y=gypsum_dry_t_y/purity
    acid_t_y=gypsum_dry_t_y*yield_factor
    equivalent_s_t_y=acid_t_y*MS/MH2SO4
    acid_domestic=s["verified_qualified_domestic_acid_demand_t_year"]
    actual_import_s=s["actual_national_sulfur_import_t_year"]
    reserves=s["required_domestic_acid_reserve_t_year"]
    if acid_domestic is None or actual_import_s is None or reserves is None:
        gate="UNKNOWN_MISSING_NATIONAL_EVIDENCE"
    else:
        assert min(acid_domestic,actual_import_s,reserves)>=0
        gate="CLOSED_UNTIL_IMPORTS_ZERO_AND_DOMESTIC_RESERVES" if actual_import_s>0 else "REQUIRES_VERIFIED_NATIONAL_BALANCE_AND_GOVERNANCE"
    return {"classification":"SYNTHETIC_ZERO_REALIZED",
       "daily_ca_moles":ca_mol_day,"daily_sulfate_moles":sulfate_mol_day,
       "limiting_element":"Ca" if ca_mol_day<=sulfate_mol_day else "SO4",
       "qualified_dry_gypsum_t_year":round(gypsum_dry_t_y,3),
       "wet_gypsum_t_year":round(wet_gypsum_t_y,3),
       "qualified_h2so4_t_year":round(acid_t_y,3),
       "max_sulfur_equivalent_t_year":round(equivalent_s_t_y,3),
       "attributable_import_displacement_t_year":0,
       "external_export_gate":gate,
       "required_receipts":["Calibrated brine flow meter and linked Ca/SO4 multi-date assays",
          "Sample dry gypsum actual mass, purity/impurities + safe residual fate",
          "Accredited acid product assay; original sulfur sources and avoided sulfur consumption verified",
          "Qualified regional hub throughput, compliant conversion process and at-cost invoice",
          "Commodity-grade national demand/import/reserve + independently audited displacement"],
       "notes":["Use brine composition downstream of RO: cannot reuse seawater constituent concentrations without RO mass balance",
       "No acid mass is sulfur mass; sulfur equivalent is only physical ceiling, not realized import replacement",
       "Pilot sample can validate precipitation without certifying national import closure"]}

if __name__=="__main__":
    data=json.loads(Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name("sulfur_synthetic.json")).read_text())
    print(json.dumps(run(data),indent=2))
