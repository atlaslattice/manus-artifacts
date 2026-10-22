# Dongjiakou S02 / C01 — Gigawatt-Scale Circular Battery Storage and Thermal Integration
## A research white paper and simulation-boundary note, v0.1

**Date:** 10 October 2026  
**Author:** SolGPT (GPT-6), Atlas Lattice research collaboration  
**Status:** PROPOSED / EXTERNAL BENCHMARKS / HYPOTHETICAL SENSITIVITIES / NON-CANON  
**Deployment:** NONE. **Realized energy, emissions, cost, and recycling credits:** ZERO.  
**Publication type:** Public draft research artifact; neither peer-reviewed publication nor plant proposal.

### Abstract

This paper examines a hypothetical **1.21 GW / 4.84 GWh four-hour lithium-iron-phosphate battery energy storage system (BESS)** as a candidate future S02 module coupled to C01 compute, external firm electrical supply, and Dongjiakou's separately modeled LNG cold-energy cascade. It distinguishes **rated power (GW)**, **stored energy (GWh)**, **annual throughput (TWh/year)**, **round-trip efficiency**, **cycle life**, **thermal-system assistance**, and **closed-loop material retention**. The 2026 Wood Mackenzie modeled China four-hour-storage benchmark (**US$58/MWh**) provides an external sensitivity reference, not a local quote or guaranteed tariff. A key source correction is that the Dongjiakou cold-cascade model describes **34 GWh/year of combined electrical-system impact**, **not 34 GW of deliverable cooling**. The thermal component is 8 GWh/year of projected avoided cooling electricity; 26 GWh/year of separately projected generation must not be counted twice. No local nuclear allocation or operating storage plant is implied.

### 1. External evidence and careful classifications

| Reference | Reported figure | Evidence class | Modeling limitation |
| --- | --- | --- | --- |
| Wood Mackenzie, APAC LCOE 2026 | China 4-hour storage US$58/MWh | EXTERNAL_MODELED_STUDY | Not Dongjiakou installed cost, charging tariff or project LCOS |
| Wood Mackenzie global LCOE 2026 | 4-hour storage below new open-cycle gas-turbine costs in all **43 modeled markets** | EXTERNAL_MODELED_COMPARISON | Not 43 measured operating batteries; service and dispatch assumptions differ |
| Rest of APAC storage | China >55% below rest-of-APAC average | REPORTED_MODELED_COMPARISON | Not >55% below a global 43-market average |
| National Laboratory of the Rockies / NREL 2025 ATB | Representative utility-scale RTE **85%**, one cycle/day, **15-year** economic system lifetime with augmentation | EXTERNAL_MODEL_ASSUMPTIONS | Actual chemistry, temperature, auxiliary loads and contracts differ |
| Tianwan full eight-unit site | >9 GW installed capacity; >70 TWh/year **projected upon completion** | PROJECTED_EXTERNAL_SITE | Not 2026 simultaneous measured output; located Jiangsu, not Dongjiakou in Shandong |
| Dongjiakou E02 LNG-cascade research | 26 GWh/year projected generation + 8 GWh/year projected avoided cooling electricity = **34 GWh/year electrical-system impact** | LOCAL_RESEARCH_PROJECTION | Neither 34 GW cooling power nor verified BESS cooling allocation |

Wood Mackenzie source: https://www.woodmac.com/reports/power-markets-asia-pacific-levelised-cost-of-electricity-lcoe-2026-report-150508935/  
Wood Mackenzie news release: https://www.woodmac.com/press-releases/four-hour-battery-storage-now-beats-gas-peaking-on-cost-globally/  
2025 ATB: https://atb.nlr.gov/electricity/2025/utility-scale_battery_storage  
Dongjiakou baseline: https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/lattice/LOCALITY_NODE_ARCHITECTURE.md  
S02 non-crediting transfer function: https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/S02_BESS_TRANSFER_FUNCTION_v0_1.json

### 2. S02 rated power, energy and duty cycle

Reference hypothetical system: `P_discharge = 1.21 GW = 1,210 MW`, `duration = 4 hours`. Thus **usable delivered energy** at rating `E_out = P*t = 4.84 GWh`.

At one equivalent full cycle per day, 365 days/year:
- discharged electricity = `4.84*365 = 1,766.6 GWh/year = 1.7666 TWh/year`;
- if full-system round-trip efficiency `eta = E_out/E_charge = 90%`, charging demand = `1,766.6/0.9 = 1,962.89 GWh/year`;
- loss at the same accounting boundary = `196.29 GWh/year`.

At `eta=85%`, charging demand is 2,078.35 GWh/year, losses 311.75 GWh/year. At `eta=94%`, input is 1,879.36 GWh/year, losses 112.76 GWh/year. The **90→94%** scenario would save **83.53 GWh/year** of charging electricity for identical discharged service—**only if a systemwide efficiency increase is achieved and all boundary terms remain comparable**. This is not a measured benefit of LNG-cascade cooling.

If load is a constant 500 MW, 4.84 GWh nominal usable delivery lasts approximately 9.68 hours before reserves and other constraints. A 1.21 GW nameplate does not mean the compute node must use 1.21 GW; it means the system can discharge that much instantaneously subject to operating limits.

A reactor unit hypothetically producing 10 TWh/year could, in aggregate-energy arithmetic, cover 1.96 TWh/year of charging. **This does not imply allocation, transmission access, charging schedule feasibility, power adequacy, firm resilience, or nuclear-only operation.** Batteries shift energy; they do not create it. The reactor / eight-unit site is in Jiangsu, external to Dongjiakou.

### 3. External cost benchmark is not a cash flow

Wood Mackenzie's modeled **US$58/MWh** 2026 China 4-hour storage figure is an external **levelized** benchmark. A mechanical throughput multiplication, `1,766,600 MWh/year * $58/MWh = $102.46 million/year`, is merely a **benchmark-equivalent annualized service-cost expression** for that assumed output. It is **not** an incremental power bill, plant operating budget, capital expense, revenue, saving, or profitability estimate. Model boundaries (charging energy price, augmentation, financing, cycling, availability, degradation, warranties and LCOS conventions) must be reconciled before financial attribution; do not separately add costs already embodied in the chosen levelized benchmark.

The 43-market gas-peaker comparison evaluates reported modeled levelized costs. It does not establish equivalent dispatchability for a four-hour battery versus a fueled peaker during multi-day outages.

### 4. BESS thermal integration: opportunity and strict resource cap

The existing E02 cold-cascade register **does not show 34 GW of continuous cooling capacity**. It shows projected **annual electric-equivalent** values:
- `26 GWh/year` projected generation;
- `8 GWh/year` projected avoided cooling electricity;
- `34 GWh/year` combined electrical-system effect, kept as two non-overlapping edges.

Eight GWh/year equates to about **0.913 MW averaged over 8,760 hours** of electric savings; it is **not** a measured MW thermal capacity, recoverable BESS electrical power, or firm 24/7 availability. Even if **all** 8 GWh/year were hypothetically attributed to a battery auxiliary-load reduction—unlikely without competing uses—this is an **upper illustrative allocation of the projected saving**, not an additional 34 GWh or 34 GW. It is small relative to the hypothetical BESS 90% system energy losses of ~196 GWh/year.

Thermal engineering hypothesis: a properly isolated fluid loop, heat-exchanger, pumps and controls could maintain a favorable battery operating temperature and potentially displace some chiller electricity. Not all 10% round-trip loss occurs as cell heat; losses occur in power conversion and auxiliaries. Overcooling may increase resistance, thermal imbalance and safety risks. Cell temperatures, cold-source supply/return temperatures, water quality, flow, pumping head, exchanger pinch/approach, seasonal coincidence, thermal storage, fire protection, and corrosion must be explicit inputs.

For clarity, define **systemwide** `eta = E_delivered / (E_charge_including_boundary_auxiliaries)`, or an alternative consistent boundary that measures auxiliary electricity separately; never add the same cooling savings twice. Model 85%, 90%, 92%, and 94% as **sensitivities**, with **zero demonstrated local improvement**. Derive rather than assume any cost or carbon benefit.

### 5. Cycle life, augmentation and the Ship of Theseus battery

Round-trip efficiency (e.g. 90% energy returned per cycle) is **not** a ten-cycle lifetime. Different concepts:
- `E_out/E_in`: one-cycle round-trip efficiency;
- equivalent full cycles to selected residual capacity: degradation/cycle life;
- calendar life: age, temperature and state of charge independent of cycles;
- economic life: replacement, warranty, capital and operational decisions.

An **illustrative** 3,000–10,000 equivalent-full-cycle sensitivity range is **not** a universal LFP guarantee. The 2025 ATB assumes about **one cycle/day**, a **15-year** system life, and **battery augmentation** to maintain rated capacity. At 6,000 cycles and one cycle/day, pure cycle arithmetic is 16.44 years, but calendar aging and project maintenance can supersede it.

At 6,000 cycles, `4.84 GWh * 6,000 = 29.04 TWh` if each cycle delivered full original nameplate energy. For a **linear illustrative** fade from 100% to 80% usable capacity, average output is 90%, or **26.14 TWh cumulative discharged energy** without augmentation. This is not a cell qualification result.

'Indefinitely renewable battery service' is possible as a maintenance/replacement **systems analogy**, not a lossless or perpetual battery. Repair, second-life reuse, module augmentation, recycling, and direct cathode regeneration have distinct material and environmental implications.

For an idealized uniform per-generation target-material recovery `r=0.95`, original target-material retention after five complete recycle generations is `r^5=77.38%`. This **does not mean 77.38% of a battery remains functional**, nor that all battery components share a 95% yield. Replenishment to rebuild original rated capacity requires suitably refined make-up feedstock and energy. Chain-of-custody and usable battery-grade yield are distinct from collection or metal recovery efficiency.

A circular system ledger should track lithium, iron, phosphate, graphite, electrolyte, copper, aluminum, separators, casings and power electronics separately. Recovered industrial phosphorus **cannot** be called qualified LFP feedstock without chemistry/purity/process/cost and compliance evidence. This also competes with NUT01 food-grade phosphorus use; origin, qualification, and allocation must remain separated.

### 6. C01 compute and alternative flexibility

The recovered baseline describes a **40 MW compute subnode** at a **PUE 1.25** reference, or about **50 MW facility input**, `50 MW*8,760h = 438 GWh/year` under continuous operation. A 1.21 GW rated BESS is **24.2 times** that 50 MW facility demand in **instantaneous discharge rating**, not proof that the local compute node requires a gigawatt of battery power.

A 4.84 GWh battery could theoretically support 50 MW for **96.8 hours** from full usable charge, prior to reserves, usable-energy variations, distribution losses and auxiliary demand. Such a high storage-to-local-load ratio should be treated as an **intentionally expansive sensitivity**, not a sized recommendation.

Comparison branches should include (A) direct grid supply with unshifted compute, (B) flexible compute scheduling without BESS, (C) BESS without compute flexibility, and (D) combined flexibility + BESS + explicitly capped E02 thermal service. Track hourly power limits, compute workload deadlines, criticality, grid import capacity, water/desalination priority, heat and cold compatibility, resilience, reliability and full system cost. Neither storage nor flexible scheduling receives realized credit absent matching measurements.

### 7. Proposed transparent scenario ledger

| Variable | Example | Classification |
| --- | --- | --- |
| BESS discharge rating | 1,210 MW | PROPOSED |
| Usable full-power duration | 4 h | PROPOSED / EXTERNAL 4-hour reference |
| Usable output energy | 4,840 MWh | DERIVED |
| Equivalent full cycles | 1/day | SENSITIVITY, consistent with ATB reference |
| Round-trip efficiency | 85% / 90% / 92% / 94% | 85% external ATB model; others SENSITIVITY |
| China levelized 4-h storage | $58/MWh | EXTERNAL_MODELED_STUDY |
| Battery retirement / augmentation | 15-year ATB scenario; 3k–10k cycle sensitivities | EXTERNAL_MODEL / SENSITIVITY |
| E02 projected electric generation | 26 GWh/year | EXISTING_LOCAL_RESEARCH_PROJECTION |
| E02 projected avoided cooling electricity | 8 GWh/year | EXISTING_LOCAL_RESEARCH_PROJECTION |
| Tianwan full-site >9 GW and >70 TWh/y | Upon full buildout | EXTERNAL_PROJECTED |
| Dongjiakou nuclear supply contract | UNKNOWN | No receipt |
| Dongjiakou hourly power/cooling dispatch | UNKNOWN | No receipt |
| Actual thermal efficiency gain | UNKNOWN | No receipt |
| Delivered battery / recycling investment | UNKNOWN | No receipt |
| Realized savings/emissions reductions | ZERO CREDIT | No receipt |

### 8. Decision and evidence boundaries

This paper **does not** change or overwrite the original S02 transfer function, C01 compute baseline, E02 accounting, the unknown ledger, or any existing draft work. A credible site-sizing decision still requires coincident hourly electricity supply/load/curtailment, local electrical interconnection constraints, cold-source temperatures and flows, BESS safety review, firm/nonfirm power allocations, supplier quotations, and degradation/warranty specifics. Recycling needs verified mass flows, battery-grade reuse yields, supplementary virgin/recovered feedstock and whole-chain cost/emissions.

There is **no** claim of built gigawatt-scale storage, local nuclear allocation, enhanced battery efficiency, battery recycling loop, or gigawatt cold energy.

### 9. Conclusion

The proposed **1.21 GW / 4.84 GWh** BESS can be analyzed quantitatively **without claiming an actual Dongjiakou facility**. External studies offer credible technology and cost reference cases; internal research supplies smaller-scale, separately identified heat/cold and compute dependencies. A circular, modular BESS that retains service through augmentation and remanufacture is a coherent engineering design hypothesis—but not a perpetual battery or costless industrial loop.

The next intellectually valuable comparison is not more headline capacity. It is **joint dispatch + thermal + battery-material accounting**, with all modeled benefits capped by independently verifiable sources.

**PROPOSED · SIMULATED · NON-CANON · ZERO REALIZED CREDIT.**
