# DJK-W01 Brine Portfolio A/B/C — research-only extension v0.1
**2026-10-09 · PUBLIC_CANDIDATE_NON_CANON · ZERO REALIZED FINANCIAL, WATER OR ECOLOGICAL CREDIT**

**Run:** `python3 research_brine_v01/portfolio.py` from the build root; optional alternate JSON as first argument. This standalone standard-library script does **not** modify the existing simulator or connect to plant controls. The JSON fixture is wholly hypothetical.

## Physical industrial node selection
Dongjiakou industrial park, operating desalination-related infrastructure, and LNG cold-energy construction/research are strong *site-screening hypotheses*, not proof that intake flow, municipal discharge, mineral assays, cold-energy output or dedicated waste streams are available to Atlas. Validate plants' as-built design, construction stage, operator authorizations and measurements before a bankable forecast.

**Scenario A:** conventional brine-management baseline with zero mineral products.
**Scenario B:** shared alkali/industrial-slag pretreatment + selective magnesium recovery; near-term heat integration sensitivity.
**Scenario C:** bromine, KCl, magnesium hydroxide, and qualified bulk salt portfolio plus heat integration; total integration is a research envelope only.

## Mass conservation and pricing
Inputs are **seawater intake** in m³/day and concentration in mg/L. Elemental feed ceiling: `t/year = intake_m3/day × concentration_mg/L × days/year / 1e6`. Br capture never exceeds elemental Br intake. Mg→Mg(OH)₂, K→KCl use stoichiometric mass factors and display both element and product basis. Sodium chloride is a *nominal equivalent mass* placeholder: true Na, Cl, sulfate and ion activity/speciation require measured water chemistry; do not claim saleable NaCl inventory from `NaCl` mass alone. Independent element identifiers avoid a repeat claim on the same feed constituent; more complex shared compounds require a full elemental allocation matrix (next version).

**Lattice invariant: INTERNAL_AT_COST.** Products sent to any Atlas Lattice node—including surrounding **grain agriculture**, mineral processors or construction nodes—transfer at independently auditable *fully loaded production + delivery cost*. There is no market-rate markup inside the network. The source node may recognize transfer receipts, but a network-level consolidation **eliminates** equal internal recipient purchases; they do not create profits for China 2.0. External buyers' realized sales, avoided real purchased feedstock, and proven disposal/energy savings are separate opportunities. A graph of opportunity is not proof of external market demand. The script's consolidated ledger deliberately treats internal resource benefits as **nonmonetized until a legitimate avoided-purchase comparison is added**, a conservative lower bound, rather than creating fictitious revenue.

Do not claim `node cash` is consolidated network profitability: it includes accounting flows, while `network_consolidated_cash` eliminates internal transfers. Each B/C budget includes assumed incremental fixed OPEX and incremental CAPEX, excluding financing, taxes, land, residual and complete utility costs unless included in the explicit assumed unit costs. The "baseline disposal" and the "avoided disposal" benefit are distinct; avoidance capped at actual modeled disposal baseline. Heat-savings also capped by baseline OPEX. No independent carbon/GRV/QOL value is treated as received cash.

## Grain agriculture is both potential supplier and beneficiary
**Inputs:** straw/manure/food-processing residue/digester centrate and qualified clean biomass ash or digestate can provide energy, nutrients, and possibly alkalinity after contaminant/strength testing; seasonal grains and rotations need actual spatial collection and acceptance data. **Outputs:** tested reclaimed water, potassium and N/P fertilizers, soil amendments and process heat; transferred internally at cost. **Gates:** actual field maps, crop and soil salinity, trace contaminants and heavy metals, pathogens, irrigation permits/GB 5084-2021, measured nutrient balance, land/transport constraints, local community effects and seasonal drought demand. NEVER irrigate grains with untreated industrial brine or use unqualified residues on crops.

## Energy integration
LNG regasification provides a useful **cold sink**, not an intrinsically free heat source. Match cold recovery, industrial waste heat, evaporator heat grades, heat-pump electrical use, pumping, construction status and simultaneous demand in a seasonal pinch/exergy model. These synthetic savings are independent scenario inputs, **not measured Dongjiakou savings**.

## Checks and missing receipts
Baseline and scenarios share the exact same feed. Missing measurements: actual intake/RO recovery, brine by-source elemental lab panels, waste alkaline stream tons/assay, feed pretreatment and fouling, MgOH2 purity, bromine oxidation/handling costs, brine residual disposition, industrial salt/KCl purity, firm internal agriculture demand vs external offtake, heat profiles, installed CAPEX, real OPEX and wastewater flow receipts. Reconcile with [DJK-W01 mineral audit](https://app.notion.com/p/3f40c1de73d9814bb6b7fff1b2c4c475?pvs=204). **No project impact, capital funding, throughput, zero liquid discharge achievement or profit is claimed.**

## AGR01/CHEM01 multi-decade allocation v0.1 (added October 9)
Run from build root:
```bash
python3 research_brine_v01/gypsum_allocation.py research_brine_v01/allocation_synthetic.json > /tmp/gypsum_30y.json
python3 -m unittest discover -s research_brine_v01 -p 'test_*.py' -v
```
This 30-year scenario explores reclamation-demand decay, industrial acceptance, annual storage, a conservative national-sulfur-shortfall agricultural allocation cap, and a separate no-double-counting ledger. Synthetic example: 70,000 t/y *hypothetical qualified dry gypsum*; neither the input nor any allocation is a measured Dongjiakou result. All soil-test, field-trial, agricultural-batch-assay, drainage/consent, industrial-assay and acid-hub acceptance gates default to **false or null**: first run therefore outputs **0 t/y agriculture, 0 t/y acid, 70,000 t increment to inventory each year**, reaching 2.1 million theoretical tonnes after 30 years. Storage capacity, costs and degradation are not modeled: this default demonstrates missing evidence, **not an actionable recommendation to accumulate material**. A physical implementation must cap storage and route unqualified residuals lawfully.

Model constraints:
- Agriculture **0 t/ha default**, with allocated tonnes only when *every* soil-test, batch-specific product assay, field-trial, drainage-plan and farm-consent gate passes. Applications depend on site-specific soil chemistry; trial inputs are synthetic and must NOT be issued as fertilizer rates.
- An industrial acid-feed allocation requires **measured** batch purity/moisture *and* verified regional hub acceptance. The placeholder industry limits (85% purity, 10% moisture) are **not an actual EPC specification**. Ag-related GB 38400-2019 and NY/T 525 may not govern mineral-gypsum directly: specific applicable fertilizer/soil-amendment requirements must be confirmed with Chinese regulators and agronomic inspectors. Heavy metals Cd/Pb/As/Cr/Hg, chloride, sodium, boron and anti-scalant contamination require tested acceptance before a true agricultural pass.
- A structural national sulfur shortfall does **not** automatically eliminate verified and essential soil-reclamation requirements; in the synthetic example a tunable `sulfur_shortfall_ag_cap_fraction=0.4` is an **illustrative GOV01 policy scenario**, not an adopted rule. Approved governance should balance actual soil/watershed benefit and national sulfur need, not blindly favor unqualified acid feed.
- Production, crop-class demand, product quality, regulatory permits, real national balance and cold-energy access are independent evidence gates. National import elimination requires actual trade statistics; no modeled mass becomes verified import displacement.
- Batch-level multi-product optimization, dynamic reserves, independent sampling receipt formats, actual projected multi-year national sulfur demand, storage costs, risk and process energy are **out of scope** for this research prototype.
- Branch-only new module and tests; the original locality simulator remains intact. Tests are **authored but not verified executed**. Mandatory local/CI test and peer review before PR promotion.
