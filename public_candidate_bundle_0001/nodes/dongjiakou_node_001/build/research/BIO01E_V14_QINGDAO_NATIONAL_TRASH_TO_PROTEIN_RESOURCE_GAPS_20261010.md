# BIO01-E v1.4 — Hybrid trash-to-protein resource gap screening

**2026-10-10 · PROPOSED / REPORTED baseline / SIMULATED process / NON-CANON / ZERO REALIZED CREDIT**. Additive report; no prior canonical source modified.

## Geographic boundary and assumptions
Qingdao REPORTED 200,000 wet tonnes/year (rounded citywide collected food waste, exact current contract source pending). China historical 349 Mt/year (2014–2018 average farm-to-fork FLW): not a collected waste inventory; use national as an intentionally generous sensitivity case, not projection.
Qingdao mixed-waste fraction proxy from multi-city restaurant waste (not Qingdao measurement): vegetable 29%, grain 25%, animal 17%, aquatic 11%, other 18%. Former category N/P estimates SIMULATED gross N 2151.5 t/y and gross elemental P 342.44t/y. Model F. venenatum A3/5, dry biomass per compatible sugar .5, finished wet product 27% solids and 12% protein. Model P demand 1% of dry biomass and minimum product protein N/protein = 1/6.25, not proven industrial rate. All source-specific assays pending.

## Scenario equations
Fungal protein from carbon (t/y) = (food-waste compatible sugar + CO2-derived food-compatible sugar) * (0.5/0.27*0.12).
Fungal protein from N = (gross recovered-and-approved N + separate recovered-and-approved N) * 6.25.
Fungal protein from P = (gross recovered-and-approved P + separate recovered-and-approved P) / 0.01 * (0.12/0.27).
Constrained carbon/N/P upper bound = min(the above). Remaining constraints can further reduce achievable output.

| Qingdao t/year except noted | Low | Medium | High |
|---|---:|---:|---:|
| Food waste baseline | 200000 | 200000 | 200000 |
| Food waste compatible sugar | 12900 | 23300 | 33700 |
| CO2-derived compatible sugar EQUIVALENT | 0 | 2000 | 10000 |
| CO2 minimum t/year | 0 | 2933 | 14667 |
| CO2 sugar hypothetical electricity GWh | 0 | 24 | 120 |
| N qualified from existing input | 215.15 | 753.03 | 1290.90 |
| Extra separately sourced N | 0 | 200 | 400 |
| P qualified from existing input | 34.24 | 119.85 | 205.46 |
| Extra separately sourced P | 0 | 20 | 75 |
| Carbon protein ceiling | 2866.67 | 5622.22 | 9711.11 |
| N protein ceiling | 1344.69 | 5956.41 | 10568.13 |
| P protein ceiling | 1521.96 | 6215.73 | 12465.07 |
| **Constrained protein upper bound** | **1344.69** | **5622.22** | **9711.11** |
| % Qingdao modeled dietary protein 230289.45t/y | 0.584% | 2.441% | 4.217% |

CO2-to-glucose elemental minimum = (264/180)=1.4667 tCO2/t glucose-equivalent. Actual CO2 and electricity will be higher or nonlinear; **12MWh/t qualified glucose-equivalent electricity is solely a sensitivity assumption**. This does not establish a viable commercial CO2-to-glucose process. Heterotrophic A3/5 cannot consume captured CO2 directly; compatibility and sterile food-grade qualification are prerequisites. Additional N/P are hypothetical source-verified net input targets from other nonoverlapping streams; not magically generated from counted Qingdao feedstock.

## National upper-bound scaling
Historic national 349Mt/200kt =1745 multiplier; assume 10/25/50% controlled accessible fraction respectively. Protein upper bounds = **0.234648/2.452694/8.472944 Mt/year**. Against hypothetical national 1.4 billion people at 60g/day => 30.66Mt/y reference protein requirements, **0.765/7.999/27.635%**. National HYBRID high supplemental CO2 minimum ~12.80Mt/y, assumed CO2 conversion electricity ~104.7 TWh/y. These are **not forecasts**: national waste stage composition differs, availability/food-safety constraints are not verified, site chemistry and capture tonnage missing.

## Resource gap solutions / gates
Carbon: preferably source-separated food-industry sugars and hydrolysates (including bran, molasses, whey permeate); CO2 electroconversion plus microbial intermediates is a separate energy-consuming optional pathway.
N: digestate/wastewater ammonia capture and food-industry protein hydrolysate only when purified and approved for human-food fermenter medium. P: selective nutrient/struvite recovery, purification and food process testing. S, K, Mg and traces: compost/digestate mineral analysis, recovered salts only after purity tests or ordinary purchased media. Water: utility reclaimed condensate, separate food-grade polishing, never unprocessed wastewater in fermenter. Heat/power: biogas CHPs, industrial waste heat cascading, renewable electricity and storage, with all energy parasitics and emissions. Oxygen: air/blowers and qualified coproduct oxygen only if actual source certified. Compost/AD: reject/culture byproducts accounted separately and no double use of same C/N/P. Carbon utilization not permanent sequestration.

## Required gating tests
CO2 actual emissions/capture and conversion purity/cost; net recoverable food-grade N/P (heavy metal/PAH contamination risk); growth/media assays *F. venenatum* A3/5 at 5L, pilot and commercial; RNA processing losses and food approval in PRC; local residue contracts and hygienic collection; mass/energy/utility balances, real LCA, cost, adoption. The calculations do NOT prove that these amounts of edible mycoprotein can be manufactured.

## References
- https://www.sciencedirect.com/science/article/pii/S0960852426013714 (food waste on Fusarium, small-scale, 2026)
- https://pubmed.ncbi.nlm.nih.gov/37263428/ (recovered nitrogen SCP safety)
- https://www.sciencedirect.com/science/article/pii/S2666498425000090 (CO2-to-acetate SCP, bacterial, 2025; confirm PII when citing)
- https://arxiv.org/abs/2605.12409 (F. venenatum A3/5 alternative C sources, preprint)
- Notion additive page: https://app.notion.com/p/3f50c1de73d981d4a6f1dc29a38256a4
