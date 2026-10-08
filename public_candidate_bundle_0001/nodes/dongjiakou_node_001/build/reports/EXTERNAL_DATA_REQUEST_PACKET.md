STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# External Data Request Packet — Dongjiakou Node-001

**Document ID:** DJK-NODE-001-EXTERNAL-DATA-REQUEST-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

---

## 1. Cover note

The Dongjiakou Node-001 study is a technical feasibility and conditional
economics assessment of an integrated energy-water-compute-port node anchored on
the existing desalination works. The study is deliberately conservative: it
declines to state any figure it cannot source.

As a result, a specific and bounded set of receipts is now the only thing
standing between the current analysis and a deployable investment case. This
packet lists exactly what is needed, why it matters, and what a usable receipt
looks like.

Nothing in this packet requires commercially sensitive disclosure beyond what a
plant operator already holds. Where a value is genuinely confidential, a
**banded or indexed figure with a stated method** is sufficient; an exact figure
is not required. What is required is that the number is measured, dated, and
attributable to a defined boundary.

> We would rather receive ten measured values and forty honest unknowns than
> fifty plausible estimates.

---

## 2. How to read the priority column

| Priority | Meaning |
| --- | --- |
| **P0** | Blocks a current-cost, current-performance or compliance claim. Without it the study cannot move from feasibility to economics. |
| **P1** | Blocks promotion of a sensitivity to a deployment decision. |
| **P2** | Improves resolution or reduces uncertainty but does not block. |

---

## 3. Requested receipts by recipient

### 3.1 Plant operator / plant engineering

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-002 | **P0** | Whole-site specific energy consumption, with the measurement boundary stated | Energy management system export, or an audited energy report | Node energy baseline; compute share of node energy |
| DAR-003 | **P0** | Incremental auxiliary energy attributable to any retrofit, before and after | Before/after metering campaign | Any retrofit savings claim |
| DAR-004 | **P0** | Dated measured recovery fraction | SCADA export, operating log, or performance test report | Feed and reject mass balance as a current claim |
| DAR-005 | **P1** | Current feed, permeate, concentrate and blend stream map | As-built process flow diagram, or a flow survey | Any discharge quantity claim; INV-19 assessment |
| DAR-010 | **P1** | Survey of genuinely unused, dissipated hydraulic head | Hydraulic survey or flow and pressure logging with elevations | Hydro credit, currently fixed at zero |
| DAR-008 | **P1** | Current clean-in-place protocol and additive chemistry | CIP procedure and chemical consumption records | Sono-CIP assessment; compute-to-CIP heat coupling |
| DAR-023 | **P0** | OT/IT segmentation design and the approval gate before any control write path | Approved cybersecurity design document | Any pilot deployment at all |

**Note on DAR-004 and DAR-002.** The study currently uses 2.2 kWh/m³, which is
**process-train** specific energy, and a 45–50% recovery **technology range**.
Neither is a measured whole-site or plant-specific value. Presenting either as
current measured performance would overstate confidence, so both are held as
explicitly-labelled assumptions until a receipt exists.

### 3.2 Plant commercial / finance

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-001 | **P0** | Plant-specific 2026 electricity tariff | Utility invoice, signed retail contract, or market settlement statement | Every current CNY figure for the node |

**Why this single item is decisive.** The study holds a historical tariff of
0.555 CNY/kWh for 2018–2020. That figure is retained only as a labelled
counterfactual. Without a current plant-specific tariff, the entire current-cost
column of the node — solar savings, compute energy cost, and net economics —
remains **UNKNOWN**. This is the highest-leverage single receipt in the packet.

### 3.3 Plant laboratory

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-006 | **P1** | Current brine and concentrate composition | Accredited laboratory report with method and detection limits | Resource-recovery claims; the magnesium-to-struvite coupling |
| DAR-007 | **P1** | Observed fouling rate and cleaning frequency history | Maintenance management system export | Membrane-life KPI; adaptive fouling control claim |

**Note.** A membrane procurement event is **not** evidence of a fouling benefit.
The 2023/24 combined UF+RO procurement, the 2025 first-stage RO replacement, the
2025/26 UF tender and the 2026 first-stage RO replacement are recorded as
procurement events with their contract values. No causal fouling or performance
benefit is inferred from them.

### 3.4 Environmental compliance

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-009 | **P0** | Primary ecological monitoring data for the receiving water body | Regulatory monitoring report or accredited laboratory data | INV-19 assessment and any regenerative claim |

**Why this is a veto, not a KPI.** INV-19 holds. An integrated node cannot be
described as regenerative if downstream water quality deteriorates. A secondary
or summary ecological source is not a substitute for measured primary data, and
profit or carbon benefit elsewhere cannot offset a failed ecological gate.

### 3.5 Energy procurement / grid

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-019 | **P0** | Node-specific direct-green allocation: MW, MWh, contract price, term, and the eligible load set | Signed agreement or grid company allocation notice | Regional green credit, currently fixed at zero |
| DAR-016 | **P1** | Evidence of actual PV curtailment or export limitation | Inverter or revenue meter export, or a curtailment notice | Any compute neutrality claim |

**Note on the regional plan.** Public reporting describes approximately **214 MW**
of planned wind and approximately **81 MW** of planned PV around Qianwan and
Dongjiakou, plus about **5 MW** of planned port-area distributed PV. These are
**planned regional figures**, not a node allocation. The study therefore records
`node001_access` as UNKNOWN and the energy credit as zero. Planned capacity never
populates an operating state.

### 3.6 C01 compute commissioning

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-012 | **P0** | Measured PUE with the boundary stated | Commissioning measurement or sub-metering | Facility energy claim; net-positive assessment |
| DAR-013 | **P0** | Measured WUE with the water source identified | Commissioning measurement | Water KPI; INV-19 assessment |
| DAR-014 | **P0** | Compute cooling water source and its accounting treatment | As-built design documentation and metering | Water accounting |
| DAR-015 | **P1** | Hourly PV AC output and hourly compute load on a common timebase | Inverter telemetry and facility metering | Hourly matching claim; storage sizing |
| DAR-017 | **P1** | Thermal coupling set: coolant supply and return temperature, recoverable thermal power, CIP target temperature and schedule, CIP thermal duty, heat-pump COP map | Thermal metering and heat pump performance map | Useful-heat credit, currently fixed at zero |
| DAR-018 | **P1** | Before/after KPI evidence for model-assisted operation | Controlled pilot measurement with a defined baseline period | Any model service benefit claim |

**Note on PUE.** The study uses PUE = 1.25 strictly as a **sector policy
reference**, alongside the PUE = 1 thermodynamic floor, so that the reference
never hides the facility-level load. It is not a Node-001 receipt. Actual Node-001
PUE is UNKNOWN.

### 3.7 Solar and rooftop

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-011 | **P0** | Structural assessment of the workshop roof and available interconnection capacity | Structural engineer report and utility interconnection study | Any PV deployment decision |

**Note.** The 17,474.32 m² workshop footprint and the 60% active module coverage
are **modelled** site-layout assumptions. Roof structural suitability and
interconnection limits are both UNKNOWN.

### 3.8 BIO01 biometabolic development

| Ref | Priority | Requested receipt | Format acceptable | What it unlocks |
| --- | --- | --- | --- | --- |
| DAR-020 | **P1** | Node-specific feedstock allocation or on-node generation receipt, with measured biogas quantity and methane composition | Feedstock supply agreement, gas metering, gas composition analysis | Biogas energy credit |
| DAR-021 | **P1** | Digestate nutrient mass, product assay, compost quality, and verified reclaimed-water reuse displacement | Accredited assay, off-take contract, reuse metering | Nutrient, compost and water credits |
| DAR-022 | **P0** | Selection and characterisation of an eligible high-COD wastewater sidestream | Sampling campaign and existing influent characterisation | Wastewater methane credit |

**Note.** The Qingdao dry anaerobic digestion precedent — approximately 260,000
tonnes of food waste producing approximately 5,260,000 m³ of biogas, a derived
reference of about 20.23 m³ per tonne — is a **retrospective operating reference
from another site**. It is used only as a transfer-function coefficient, never as
a Dongjiakou design yield. No municipal food-waste feedstock is assumed available,
because regional treatment capacity already exists.

---

## 4. What a usable receipt looks like

A receipt is usable when all five of the following are true:

1. **Primary.** It is a measurement, an invoice, an agreement or a laboratory
   result — not a summary, a press item, or a model output.
2. **Dated.** The measurement period is stated.
3. **Boundaried.** The physical or accounting boundary is stated, so the number
   cannot be silently re-used under a different boundary.
4. **Attributable.** It names a specific asset, account or sampling point.
5. **Method-stated.** The measurement or analytical method is given, with
   detection limits where relevant.

A receipt that fails any of these is recorded but does not close an UNKNOWN.

---

## 5. What happens to the data

- Receipts are recorded against a source record identifier and assigned an
  evidence class: **MEASURED**, **REPORTED**, **DERIVED**, **HISTORICAL**,
  **PLANNED**, **MODELED**, **SENSITIVITY**, **PROPOSED**, **REFERENCE** or
  **UNKNOWN**.
- Where a receipt contradicts an existing value, **both are preserved** and the
  disagreement is annotated. History is never overwritten.
- Commercial values may be supplied banded or indexed. The method matters more
  than the exact figure.
- No model has actuator authority over plant equipment. Model output is a
  recommendation that must pass a deterministic constraint validator and then an
  operator's approval before any PLC or SCADA action. Models receive no OT write
  credentials.
- Nothing in this study authorises construction, procurement, or a change to any
  operating plant.

---

## 6. Minimum viable receipt set

If only a small number of items can be provided, these six move the study
furthest, in order:

| Order | Ref | Receipt | Effect |
| --- | --- | --- | --- |
| 1 | DAR-001 | 2026 plant-specific electricity tariff | Converts the entire current-cost column from UNKNOWN to measurable |
| 2 | DAR-002 | Whole-site SEC with boundary | Establishes the true node energy baseline |
| 3 | DAR-004 | Dated measured recovery fraction | Converts the mass balance from a range to a plant fact |
| 4 | DAR-009 | Primary ecological monitoring data | Resolves the INV-19 veto, which gates the whole node |
| 5 | DAR-012 | Measured PUE with boundary | Converts the compute facility energy from a scenario to a measurement |
| 6 | DAR-011 | Roof structural and interconnection assessment | Converts the PV case from a layout sensitivity to a project |

---

## 7. Lattice-scale requests

The Dongjiakou node is intended as the first instantiated node of a wider lattice
covering Chinese localities with seawater desalination capacity. Two additional
requests apply at that scale:

| Ref | Priority | Request | Why |
| --- | --- | --- | --- |
| DAR-L01 | **P0** | A sourced, evidence-classed register of candidate localities | A lattice-scale claim requires a sourced node register; localities and capacities must be REPORTED or better, never inferred |
| DAR-L02 | **P0** | Per-node current resource and production statistics under a common schema | Cross-node comparison requires a shared schema and per-node provenance |

A lattice-level aggregate may never be attributed back to a single node, and a
single physical resource may not receive a credit in more than one node.
