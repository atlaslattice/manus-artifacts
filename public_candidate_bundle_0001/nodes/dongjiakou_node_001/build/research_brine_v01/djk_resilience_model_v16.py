"""DJK research comparator v1.6. All default prices and engineering costs synthetic."""
from math import isclose
MW_SO4,MW_GYPSUM,MW_CACL2,MW_S,MW_ACID=96.06,172.171,110.984,32.065,98.079
DEFAULT=dict(brine_m3_day=150000,uptime=0.75,so4_g_l=4.5,sulfate_capture=0.35,liquor_m3_y=300000,
cacl2_kg_m3=95,ca_recovery=0.80,gypsum_qualification=0.90,acid_yield_t_per_gypsum_t=0.40,
conversion_availability=0.80,liquor_cost_cny_m3=90,precipitation_cost_cny_t_gypsum=85,
acid_conversion_cost_cny_t_acid=700,acid_finishing_cost_cny_t_acid=135,fixed_cost_cny_y=4000000,
capital_cny=160000000,discount=0.10,years=15,smelter_normal_cny_t=1050,smelter_shock_cny_t=1950,
sulfur_normal_cny_t=1350,sulfur_shock_cny_t=2700,shock_fraction=0.20)
def run(p=None):
 p=dict(DEFAULT,**(p or {}))
 sulfate=p['brine_m3_day']*365*p['uptime']*p['so4_g_l']/1000
 gs=sulfate*p['sulfate_capture']*MW_GYPSUM/MW_SO4
 cacl2=p['liquor_m3_y']*p['cacl2_kg_m3']/1000
 gc=cacl2*p['ca_recovery']*MW_GYPSUM/MW_CACL2
 gypsum=min(gs,gc)*p['gypsum_qualification']
 acid=gypsum*p['acid_yield_t_per_gypsum_t']*p['conversion_availability']
 if acid<=0:raise ValueError('No acid produced')
 cost=(p['liquor_m3_y']*p['liquor_cost_cny_m3']+gypsum*p['precipitation_cost_cny_t_gypsum']+
 acid*(p['acid_conversion_cost_cny_t_acid']+p['acid_finishing_cost_cny_t_acid'])+p['fixed_cost_cny_y'])
 ann=sum((1+p['discount'])**(-y) for y in range(1,p['years']+1))
 price=(1-p['shock_fraction'])*p['smelter_normal_cny_t']+p['shock_fraction']*p['smelter_shock_cny_t']
 return dict(gypsum_t_y=gypsum,pure_h2so4_t_y=acid,sulfur_t_y=acid*MW_S/MW_ACID,
 annual_cost_cny=cost,levelized_cny_t=(cost+p['capital_cny']/ann)/acid,
 npv_vs_smelter_cny=-p['capital_cny']+ann*(acid*price-cost),binding='CALCIUM' if gc<gs else 'SULFATE')
if __name__=='__main__':print(run())
