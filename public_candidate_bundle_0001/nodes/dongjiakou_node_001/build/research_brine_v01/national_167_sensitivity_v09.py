#!/usr/bin/env python3
"""Research-only national 167-node bounds; NOT confirmed identical facilities."""
import csv,math
from pathlib import Path
N=167; PURE_ACID_NODE_T=66937.50
ELEMENTAL_S_PER_ACID_T=32.065/98.079
def scenarios():
 for eligible_share in [0.10,0.25,0.50,1.00]:
  for uptime in [0.50,0.75,0.90]:
   eligible=N*eligible_share
   acid=eligible*uptime*PURE_ACID_NODE_T
   yield dict(eligible_node_fraction=eligible_share,eligible_node_equivalent=eligible,uptime=uptime,
    acid_potential_t_y=round(acid,1),sulfur_equivalent_t_y=round(acid*ELEMENTAL_S_PER_ACID_T,1),
    equivalent_2025_export_volume_pct=round(100*acid/4649000,2),
    brine_needed_if_DJK_copies_m3_day=round(eligible*150000,0),
    farm_adjacent_ha_measured="UNKNOWN",national_verified_gap_t="UNKNOWN",
    physical_receipts=0,export_authorized=False)
def main():
 p=Path(__file__).with_name("national_167_synthetic_scenarios_v09.csv")
 with p.open("w",newline="") as out:
  w=csv.DictWriter(out,fieldnames=list(next(scenarios())))
  w.writeheader(); w.writerows(scenarios())
 print("all-node ceiling",N*PURE_ACID_NODE_T,"pure acid tonnes annually")
 print("export historical ratio",4649000/PURE_ACID_NODE_T,"full-equivalent nodes, before reserves/gates")
 print("Output",p)
if __name__=="__main__": main()
