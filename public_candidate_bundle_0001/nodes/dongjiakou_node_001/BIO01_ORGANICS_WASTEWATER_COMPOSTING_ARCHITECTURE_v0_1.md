# Dongjiakou BIO01 — Integrated Organics, Wastewater & Composting Module v0.1

**Status:** PROPOSED ARCHITECTURE + EXECUTED PARAMETRIC TRANSFER FUNCTION. **Zero node credit.**

## Finding first

The biometabolic lane is technically credible and well matched to the existing Dongjiakou/Qingdao industrial ecology, but the node does not yet have a receipted organics allocation, COD load, digestate composition, nutrient yield, biogas composition, compost product, or new wastewater diversion contract.

Therefore the architecture is added now while all benefit credits remain zero.

Submodules:

```text
BIO01-A  food / organic solids -> anaerobic digestion
BIO01-B  eligible high-COD wastewater -> anaerobic sidestream pretreatment
BIO01-C  digestate liquid -> nutrient recovery + polishing / reuse
BIO01-D  digestate solids + clean bulking carbon -> enclosed composting
```

## Local fit

Qingdao already operates a 500 t/day food-waste project based on screening + dry anaerobic digestion. A 2024 operating report gives 260,000 t cumulative food-waste processing and 5.26M m3 cumulative biogas.

Dongjiakou already has biological wastewater infrastructure: an industrial WWTP reported at 23,200 m3/day with an AO mainline for organic industrial + domestic wastewater and high reclaimed-water reuse, plus a port WWTP using MBBR biological treatment.

BIO01 is therefore not 'invent a bioreactor where none exists.' It is: selectively add resource-recovery stages where they demonstrably improve the existing water/waste network.

## Feedstock priority rule

```text
Priority 1: organics generated inside the future node boundary
  - canteen / worker food waste
  - A01 greenhouse residues
  - approved food-processing residues
  - nonhazardous biosolids compatible with digestion

Priority 2: contracted nearby industrial organic residues

Priority 3: verified regional surplus under government/operator allocation

Never assumed:
  - diversion from an existing Qingdao food-waste plant
  - municipal food waste without contract
```

Qingdao already has central food-waste capacity and a West Coast food-waste line. Existing treatment capacity is a constraint, not free feedstock.

## Stream admission gates

Candidate admissible streams:

```text
source-separated food waste
food-processing wastewater with suitable biodegradability
domestic/sanitary wastewater
digestate liquor
compatible organic sludge
```

Segregated unless proven compatible:

```text
RO concentrate / high-salinity brine
CIP acid / alkali cleaning waste
metal-rich industrial wastewater
hydrocarbon / solvent streams
high-sulfide toxic streams
hazardous waste
```

Required admission data:

```text
flow; COD/BOD; TSS/VSS; pH/alkalinity; salinity/conductivity; N/P;
sulfate/sulfide; oil & grease; heavy metals; toxic organics; temperature;
pathogen/sanitary classification where relevant
```

## BIO01-A — food-waste anaerobic digestion

Preferred first architecture: enclosed preprocessing -> dry or wet anaerobic digestion selected from measured solids content -> gas cleanup -> measured use.

Outputs are biogas, dewaterable digestate solids, digestate liquid, and rejected contaminants.

Biogas receives no energy credit until wet gas flow, CH4 fraction, contaminants, pressure, flare/use split, conversion efficiency, parasitic energy and methane leakage are measured.

### Local transfer-function reference

```text
260,000 t food waste -> 5.26M m3 cumulative biogas
derived retrospective ratio = 20.2308 m3 biogas/t
```

This is a local historical reference, not a design yield.

```text
1 t/day verified feed   -> 7,384 m3/y biogas reference
5 t/day                 -> 36,921 m3/y
10 t/day                -> 73,842 m3/y
25 t/day                -> 184,606 m3/y
50 t/day                -> 369,212 m3/y
```

No kWh is assigned because node methane fraction and conversion pathway are UNKNOWN.

## BIO01-B — wastewater anaerobic sidestream

Dongjiakou's existing AO and MBBR infrastructure remains the polishing/compliance baseline.

BIO01-B is considered only for a segregated, compatible, high-biodegradable-COD stream where anaerobic pretreatment can plausibly reduce aerobic load and recover methane.

Technical ceiling:

```text
CH4_theoretical_STP <= 0.35 m3 CH4 / kg biodegradable COD removed
```

This is stoichiometric ceiling logic, not a plant yield. Required node inputs are eligible flow, COD, biodegradable fraction, COD removed, dissolved methane loss, sulfate competition, parasitic energy and polishing energy.

If inputs are missing, BIO01-B returns a transfer function rather than a point forecast.

## BIO01-C — liquid digestate / nutrient recovery

Liquid digestate is not fertilizer by default.

Candidate sequence:

```text
digestate separation
 -> nutrient assay
 -> struvite / ammonium recovery where chemistry supports it
 -> biological / membrane polishing
 -> verified nonpotable reuse or existing WWTP
```

Track P conversion, P product yield, product purity, N recovery, Mg consumption, chemical consumption, energy, recycle loss and residual nutrient load separately.

### Seawater-refinery coupling

A future Mg-bearing stream from the seawater-refinery lane may be evaluated as a struvite reagent source.

```text
Mg sold as commodity
OR
Mg transferred to nutrient recovery
```

The same Mg mass cannot earn both credits. Any seawater-derived Mg used in fertilizer production must pass impurity, contaminant and product-regulation gates.

## BIO01-D — digestate composting

Composting is a post-digestion stabilization/valorization lane, not a guaranteed product.

Candidate feed:

```text
dewatered digestate solids
+ clean lignocellulosic / green-waste bulking material
```

Preferred concept:

```text
enclosed in-vessel or membrane-covered aerated composting
-> captured odor / ammonia treatment
-> maturation
-> screening
-> independent product testing
```

No compost mass or fertilizer value is credited until measured.

Release gate:

```text
pathogen indicators
stability / maturity
N-P-K
salinity
heavy metals
microplastics
persistent contaminants where relevant
phytotoxicity / germination
moisture / organic matter
applicable product / land-application regulation
```

If the gate fails, material remains a residual requiring further treatment.

## Water loop

Candidate routing:

```text
eligible wastewater
 -> BIO01-B
 -> existing AO/MBBR or advanced polishing
 -> reclaimed water
 -> industrial reuse / A01 irrigation / approved cooling use
```

Water credit equals freshwater actually displaced, not permeate produced.

Dongjiakou already reports high reclaimed-water reuse, so a new BIO module must beat or extend a strong incumbent baseline.

## Heat coupling

Potential measured couplings:

```text
C01 compute heat -> digester/preheat only if temperature grade and timing fit
biogas CHP heat -> digester / compost / A01
compost heat -> low-grade recovery only if engineered and metered
```

No thermal GWh is converted directly to electrical credit.

## C01 control-plane role

C01 may advise on feedstock characterization, digester stability, gas-yield anomalies, odor/methane leak triage, nutrient-recovery optimization, compost QA and mass-balance reconciliation.

Existing governance remains:

```text
AI recommendation
 -> deterministic validator
 -> operator approval
 -> PLC/SCADA
```

LLM actuator authority = NONE. DeepSeek / Qwen3 / GPT routing remains vendor-replaceable and advisory. Cross-model agreement is not evidence.

## Vetoes

```text
uncontrolled methane leakage
odor / VOC noncompliance
digestate or compost contaminant failure
pathogen-control failure
wastewater discharge / reuse noncompliance
marine-water-quality degradation
hazardous / saline / toxic stream misrouting
nutrient runoff risk
double counting of biogas, carbon, nutrients, water or Mg
```

## Accounting invariants

```text
food waste entering digester is counted once
biogas carbon is counted once
CH4 burned for energy cannot also be claimed as stored carbon
digestate N/P transferred to compost cannot also be claimed as recovered fertilizer elsewhere
reclaimed water is credited only when it displaces another water source
seawater Mg is commodity OR nutrient-recovery input, not both
municipal food waste is not node feedstock without allocation
```

## Scale gate

Start with feedstock proof, not reactor size. Pilot is earned only after >=90 days source-separated feed characterization, wastewater compatibility assay, mass-balance closure, odor/methane-control design, an off-take/disposal route for every output, and an interface agreement with existing treatment operators.

## Existing Atlas NERM compatibility

The prior NERM architecture already contains anaerobic digestion, nutrient recovery and reclaimed-water concepts.

For Node-001, NERM numerical yields, CAPEX, revenue and 'ready for deployment' labels are not inherited automatically. BIO01 re-validates each lane from Dongjiakou/Qingdao receipts and current literature.

## Keeper

**Waste is only a resource after the input, conversion, output, residual and off-take are all measured. A bioreactor does not erase a waste stream; it changes its state and inherits responsibility for every product.**