#!/usr/bin/env python3
"""Synthetic sulfate portfolio 2025 MNR provincial freshwater capacity; no site assays."""
import csv
from pathlib import Path
p={'Shandong':964239,'Zhejiang':823906,'Hebei':490700,'Tianjin':456000,'Liaoning':161984,'Guangdong':98016,'Jiangsu':41510,'Fujian':29950,'Hainan':9750,'Guangxi':750}
SULFATE=96.06;H2SO4=98.079;S=32.065
def rows():
 for province,cap in p.items():
  for ratio in [0.5,1,1.5]:
   for grams in [2.7,4.5]:
    for recovery in [0.1,0.35,0.7]:
     for conversion in [0.4,0.7]:
      sulfate=cap*ratio*365*.75*grams/1000
      acid=sulfate*recovery*H2SO4/SULFATE*conversion
      yield {'province':province,'freshwater_design_t_day':cap,'brine_to_freshwater_ratio_ASSUMED':ratio,'sulfate_g_l_ASSUMED':grams,
       'sulfate_capture_ASSUMED':recovery,'acid_sulfur_conversion_ASSUMED':conversion,'uptime_ASSUMED':0.75,
       'sulfate_t_y':round(sulfate,1),'potential_pure_H2SO4_t_y':round(acid,1),'elemental_S_t_y':round(acid*S/H2SO4,1),
       'evidence':'NO SITE ASSAYS NO CHEMICAL PROCESS QUALIFICATION'}
def main():
 assert sum(p.values())==3076805
 d=list(rows()); fp=Path(__file__).with_name('national_sulfate_portfolio_v10.csv')
 with fp.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(d[0]));w.writeheader();w.writerows(d)
 for ratio,grams,rec,conv in [(0.5,2.7,.1,.4),(1,4.5,.35,.7),(1.5,4.5,.7,.7)]:
  matching=[x for x in d if x['brine_to_freshwater_ratio_ASSUMED']==ratio and x['sulfate_g_l_ASSUMED']==grams and x['sulfate_capture_ASSUMED']==rec and x['acid_sulfur_conversion_ASSUMED']==conv]
  print(ratio,grams,rec,conv,sum(x['potential_pure_H2SO4_t_y'] for x in matching))
if __name__=='__main__':main()
