# DeepSeek Review Packet — Alexandrian Seawater Refinery v0.1

```text
PURPOSE: public-record refinement + adversarial review
STATUS: REQUEST FOR REVIEW
ATLAS_167_STATUS: UNVERIFIED SCENARIO ASSUMPTION
```

## Context

We are modeling China's publicly reported **167 desalination projects / 3.077 million tonnes per day** as a host network for a hypothetical multi-resource seawater refinery.

A separate user-reported prior DeepSeek statement described those 167 facilities as the first Atlas Lattice nodes. We have **not independently verified that identity**, so the paper treats it only as a scenario overlay.

The model does not assume deuterium is the winning working medium. It screens all useful state transitions and co-products under common mass, energy, economics, circularity, and ecology accounting.

## Architecture under review

```text
seawater intake
 -> pretreatment / contaminant capture
 -> desalination
 -> pressure-energy recovery
 -> brine routing manifold
      -> salinity-gradient energy where a low-salinity partner exists
      -> Na/Cl bulk chemistry
      -> Mg/Ca/K recovery
      -> Li / strategic trace-resource lane
      -> H/D research lane
      -> Mg/Ca carbon mineralization
      -> residual-water recovery / ZLD where justified
      -> ecologically bounded discharge
 -> local-first circularity ledger
 -> optional data-center / industrial heat and power integration
```

Recovered products are not counted as electrical generation. Energy credit requires an explicit source/gradient.

## Public-record values already used

Please verify or correct:

```text
167 desalination projects
3.077 Mt/day aggregate desalination capacity at end-2025
2030 target >4.5 Mt/day
2026 Chinese public reporting: strategic seawater-resource R&D includes
lithium, uranium, deuterium and other trace resources
```

## Current network sensitivity

Illustrative only:

```text
RO water recovery = 45%
product water = 3.077 million m3/day
feed water = ~6.838 million m3/day
brine = ~3.761 million m3/day
```

Representative incoming-feed inventory under that assumption:

```text
Mg      ~9,231 t/day
Ca      ~2,803 t/day
K       ~2,667 t/day
D-equiv ~222 t/day
Li      ~1.16 t/day
```

These are feed-throughput inventories, NOT recovery forecasts.

## Requested refinement

Please return a table with:

```text
field
best public value
unit
date
source URL / report
evidence class: MEASURED / REPORTED / DERIVED / MODELED / UNKNOWN
confidence
notes
```

for:

1. Individual 167-project names, locations, capacities and desalination technology.
2. Actual SWRO recovery ratios and product/feed/brine flows.
3. Existing energy-recovery devices and measured specific energy.
4. Existing brine/mineral/electrochemical utilization at each plant.
5. Which facilities currently recover or pilot Br, K, Mg, Li, D, B, U or other resources.
6. CAPEX/OPEX and energy use for Chinese NF, UF, ED, BMED, RED, PRO, DLE, Mg/Ca recovery, crystallization, ZLD and H/D separation.
7. Membrane/sorbent life, cleaning frequency, fouling and corrosion rates.
8. Coastal electricity prices / industrial power tariffs relevant to each cluster.
9. Product prices and realistic offtake limits for recovered commodities.
10. Local wastewater/river/industrial low-salinity streams for salinity-gradient power.
11. Brine chemistry, antiscalants, cleaning chemicals and trace contaminants.
12. Brine-discharge ecological limits and monitoring requirements.
13. Public evidence for microplastic, PFAS/heavy-metal, or other contaminant capture/destruction at desalination facilities. Specifically evaluate whether a PolyGone-style passive microplastic interception stage is compatible with Chinese desalination or wastewater partner streams; return independent performance data if available rather than relying only on vendor claims.
14. Local carbonate chemistry, pH/alkalinity monitoring and discharge criteria.
15. Candidate Mg/Ca carbonation and ocean-alkalinity-enhancement projects. Please cross-check Chinese work from Shandong University, Tongji University, SUSTech/Qingdao groups and the Institute of Oceanology, Chinese Academy of Sciences, including the 2026 1,000 m3 southern Yellow Sea calcium-alkali field demonstration. Identify which results are lab, mesocosm, shipboard, field, modeled, or deployed.
16. Any public documentation that the 167 desalination facilities are Atlas Lattice nodes; if none, explicitly return NOT VERIFIED.

## ORCS bridge

Do not reproduce the entire ORCS framework. Use it as a compact audit interface:

- evidence labels;
- local-first circularity;
- water / power / heat boundary accounting;
- downstream water-quality protection;
- report -> engineer -> pilot -> scale;
- public receipts for successful pilots.

For this paper, please also score the retrofit against a **paper-specific 12-domain regenerative overlay**:

```text
1 compute productivity
2 energy
3 water
4 heat
5 materials
6 carbon
7 ocean/coastal ecology
8 pollution/toxins/microplastics
9 local food/agriculture interfaces
10 jobs/community value
11 resilience/resource security
12 governance/provenance
```

This is an application mapping, not a claim that these are the exact canonical D-FLYWHEEL layer labels.

## Key adversarial questions

- Which resource lanes cannibalize one another chemically or thermodynamically?
- Which extraction revenues are likely to be destroyed by market saturation at national scale?
- Which environmental interventions merely move contaminants from seawater into brine/solid waste?
- What is the lowest-cost sequence of pressure recovery, mineral recovery, SGE, carbonation and residual treatment?
- Where does site heterogeneity make a standardized skid unrealistic?
- Which 3-5 facilities give the most informative pilot set?
- What claims in the white paper should be downgraded or deleted?


## New named external lanes for review — 2026-10-06

### PolyGone microplastic interception

Please verify independently:

```text
technology: passive/recyclable microplastic-binding filtration medium
company: PolyGone Systems
public deployment claim: ACUA wastewater-treatment pilot
reported start: September 2024
reported deployment: 720 filters
reported host capacity: 40 million gallons/day
reported cumulative capture: 520 million microplastics
patent family: aquatic microplastics removal, priority 2021-03-23
```

Return third-party monitoring, particle-size efficiency, polymer selectivity, pressure/head-loss, media lifetime, regeneration cycles, CAPEX/OPEX and captured-plastic fate where public.

### Chinese ocean alkalinity / carbonate research

Please refine the public record for:

```text
2024 Shandong University:
  olivine OAE in East/South China Sea; Ni/Cr constraints

2026 Tongji University:
  natural silicates + industrial byproducts for coastal OAE

2026 South China Sea:
  shipboard ecological-response experiments

2026 Institute of Oceanology, CAS / Qingdao:
  calcium-alkali coupling
  lab + mesocosm + 1,000 m3 southern Yellow Sea field demonstration
  published estimated atmospheric CO2 uptake under test conditions

2026 North China Sea:
  microcosm OAE biogeochemistry work, currently preprint/under review
```

For each, return:
- exact institution
- experiment scale
- alkalinity / reagent chemistry
- energy and reagent requirements
- carbon accounting method
- pH / TA / DIC response
- trace-metal / ecological response
- duration
- independent replication status
- CAPEX/OPEX if any
- whether it is research, pilot, demonstration, or operational deployment.
