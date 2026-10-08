STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Dongjiakou Locality Stream Register v0.2

**Artifact ID:** `DJK-NODE-001-LOCALITY-STREAM-REGISTER-v0.2`
**Status:** PUBLIC_CANDIDATE_NON_CANON
**Boundary:** Dongjiakou locality node — a parent node containing subnodes

## v0.2 changes

- Realized credit now requires MEASURED_PHYSICAL. Modeled and projected streams carry none.
- Credit ownership is singular; allocation is separate and conservation-bounded.
- Every edge carries edge_state, and the register projects two graphs.
- No stream claims a sink that is not established; product and brine route to an external boundary.
- Simulator validation and locality clearance are reported separately.
- The flywheel layer summary is derived from the streams, not hand-written.
- The 34 GWh figure is renamed to an electrical-system impact, not a stream.
- Credit now requires edge_state == MEASURED_PHYSICAL AND evidence == MEASURED AND a valid owner; edge_state alone was a loophole.
- Allocation conservation rejects negative allocations and requires a stated matching unit/time basis.
- Each flywheel layer declares a layer_basis, so governance and ecology are not forced to masquerade as material flows.

## Governing rules

- A stream may be counted once.
- A component may not claim a stream it does not own.
- No module receives benefit before measurement.
- An aggregate may never backfill a subnode UNKNOWN.
- NODE_PASS = AND(all component vetoes pass).
- An unresolved veto is not a pass, and is not a failure either.

## Clearance — two questions that must not be read as one

| State | Question | Answer |
| --- | --- | --- |
| `SIMULATOR_VALIDATION` | Did the software pass its epistemic checks? | **PASS** |
| `LOCALITY_CLEARANCE` | Has the physical locality node passed its vetoes? | **NOT_ESTABLISHED** |

> SIMULATOR_VALIDATION = PASS is compatible with LOCALITY_CLEARANCE = NOT_ESTABLISHED. The simulator passed because it correctly refused to clear the physical node. Never present the gate count as evidence that Dongjiakou itself has passed certification, ecology or grid gates.

## Subnodes

| ID | Description |
| --- | --- |
| `W01` | Water / desalination (UF+RO, 100,000 m3/day nameplate) |
| `C01` | Compute + ORCS advisory lattice (a load, never a source) |
| `P01` | Port / rail / logistics metabolism |
| `E01` | Grid / wind / PV / storage |
| `E02` | LNG cold-energy cascade and air separation |
| `R01` | Resource extraction from brine (Li, D, Mg/Ca/K/Br, trace) |
| `BIO01` | Organics / wastewater / nutrients |
| `M01` | Additive manufacturing / 3D print (a load; material credit only for assayed contracted output) |
| `MAT01` | Steel slag / tires / construction materials |
| `CHEM01` | Chemical-park process streams |
| `AGR01` | Grain / food / controlled-environment agriculture |
| `CARB01` | CO2 capture / utilization / mineralization |
| `ECO01` | Coastal and ecological monitoring |
| `GOV01` | Provenance / contracts / vetoes |
| `EXT01` | External boundary — current sink or fate not established at subnode level |
| `IND01` | Contracted industrial offtake cluster — Qingdao Special Steel, Jinneng Chemical, Bangtuo New Materials, West Coast Water Affairs (which further supplies Haiwan Chemical and Huicheng Environmental Protection) |

## Physical StreamGraph — what actually flows today

_Flows that exist now. A stream may be counted once._

| Stream | Source | Sink | Flow | Quantity | Evidence | Edge state | Credit owner | Allocation owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `S-W01-IND-01` | W01 | IND01 | product water to contracted industrial offtakers | 17,930,000 m3/year actual (2025); 70,000 m3/day contractual take-or-pay minimum | REPORTED | **REPORTED_PHYSICAL** | W01 | NONE |
| `S-W01-EXT-02` | W01 | EXT01 | reject-equivalent brine / concentrate | 21,914,444 m3/year at 45% recovery; 17,930,000 at 50% | MODELED | **REPORTED_PHYSICAL** | W01 | NONE |
| `S-P01-EXT-01` | P01 | EXT01 | port throughput and logistics metabolism | 30 berths operating; first 400,000 t ore terminal handled >40 Mt in 2024 at ~90% utilisation | OPERATIONAL | **REPORTED_PHYSICAL** | P01 | NONE |
| `S-MAT01-M01-01` | MAT01 | M01 | steel slag and water slag to building materials | operational processing link at Qingdao Special Steel | OPERATIONAL | **REPORTED_PHYSICAL** | MAT01 | NONE |
| `S-MAT01-M01-02` | MAT01 | M01 | waste tire pyrolysis products | operational demonstration base; oil, carbon black, steel wire, gas | OPERATIONAL | **REPORTED_PHYSICAL** | MAT01 | NONE |
| `S-MAT01-EXT-01` | MAT01 | EXT01 | regional construction waste generation | Qingdao 27.879 Mt generated / 14.653 Mt utilised (2025) | REPORTED | **REPORTED_PHYSICAL** | MAT01 | NONE |

## Opportunity Graph — what could flow

_Nothing here carries realized credit. Ordered by strength of commitment._

| Stream | Source | Sink | Flow | Quantity | Evidence | Edge state | Credit owner | Allocation owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `S-E02-GRID-01` | E02 | E01 | LNG cold-energy power generation | 26,000,000 kWh/year PROJECTED at commissioning | VERIFIED_PROJECT | **UNDER_CONSTRUCTION** | NONE | E02 |
| `S-E02-IND-01` | E02 | P01 | LNG cold-energy cooling service, avoiding external grid consumption | 8,000,000 kWh/year avoided PROJECTED | VERIFIED_PROJECT | **UNDER_CONSTRUCTION** | NONE | E02 |
| `S-E02-CHEM01-01` | E02 | CHEM01 | cold-energy air separation output (LN2, LO2, LAr) | ~660 t/day air separation unit | VERIFIED_PROJECT | **UNDER_CONSTRUCTION** | NONE | E02 |
| `S-AGR01-BIO01-01` | AGR01 | BIO01 | food-processing residues and wastewater | 1.5 Mt/yr feed protein, 370 kt/yr refined oil, 15 kt/yr lecithin planned from 2027 | UNDER_CONSTRUCTION | **UNDER_CONSTRUCTION** | NONE | AGR01 |
| `S-E01-C01-01` | E01 | C01 | regional wind and PV allocation | ~214 MW wind + ~81 MW PV proposed; node allocation UNKNOWN | PLANNED | **PLANNED** | NONE | E01 |
| `S-S01-C01-01` | E01 | C01 | on-site rooftop PV (S01_A / S01_B) technical sensitivity | 2.70619355 / 2.917982611 GWh/year MODELED; panels not installed | MODELED | **CANDIDATE_COUPLING** | NONE | E01/S01 |
| `S-C01-W01-C1` | C01 | W01 | compute waste heat to CIP thermal duty | UNKNOWN | UNKNOWN | **CANDIDATE_COUPLING** | NONE | NONE |
| `S-BIO01-W01-C1` | BIO01 | W01 | reclaimed water displacing product water | UNKNOWN | UNKNOWN | **CANDIDATE_COUPLING** | NONE | NONE |
| `S-W01-P01-C1` | W01 | P01 | product water routed to port demand | candidate: portion of 17.93 Mm3/year, allocation UNKNOWN. REVIEW ROUND 1 EVIDENCE AGAINST: the named PPP offtakers are Qingdao Special Steel, Jinneng Chemical, Bangtuo New Materials and West Coast Water Affairs. The port is NOT among them. | UNKNOWN | **CANDIDATE_COUPLING** | NONE | P01 |
| `S-W01-R01-C1` | W01 | R01 | reject-equivalent brine routed to resource extraction | candidate: portion of 21.914 Mm3/year, allocation UNKNOWN | UNKNOWN | **CANDIDATE_COUPLING** | NONE | R01 |
| `S-CHEM01-CARB01-01` | CHEM01 | CARB01 | CO2 from chemical and LNG processes | UNKNOWN | UNKNOWN | **CANDIDATE_COUPLING** | NONE | NONE |
| `S-CARB01-M01-01` | CARB01 | M01 | CO2 to 3D-printed concrete curing | UNKNOWN | UNKNOWN | **CANDIDATE_COUPLING** | NONE | CARB01 |
| `S-CARB01-AGR01-01` | CARB01 | AGR01 | CO2 enrichment for controlled-environment agriculture | UNKNOWN | UNKNOWN | **CANDIDATE_COUPLING** | NONE | NONE |
| `S-MAT01-M01-C1` | MAT01 | M01 | construction waste to additive manufacturing feedstock — CAPABILITY GAP, NOT SURPLUS | candidate: the zone has no processing capacity of its own. A Qingdao planning document identifies Dongjiakou and its surroundings as LACKING construction waste resource-utilisation enterprises, and recommends siting one to two facilities there. | UNKNOWN | **CANDIDATE_COUPLING** | NONE | M01 |
| `S-P01-C01-01` | P01 | C01 | shore power and port electrical demand | UNKNOWN | UNKNOWN | **CANDIDATE_COUPLING** | NONE | NONE |
| `S-CHEM01-AGR01-01` | CHEM01 | AGR01 | industrial waste heat to greenhouses | 68 C class heat — reference from Xinfa Liaocheng, a DIFFERENT site | SECONDARY | **REFERENCE_ONLY** | NONE | NONE |

## Edge-state distribution

| Edge state | Count |
| --- | --- |
| CANDIDATE_COUPLING | 10 |
| PLANNED | 1 |
| REFERENCE_ONLY | 1 |
| REPORTED_PHYSICAL | 6 |
| UNDER_CONSTRUCTION | 4 |

**22 streams** = 6 physical + 16 opportunity. **0 realize credit** (credit requires `MEASURED_PHYSICAL`).

## Evidence-class distribution

| Class | Count |
| --- | --- |
| MODELED | 2 |
| OPERATIONAL | 3 |
| PLANNED | 1 |
| REPORTED | 2 |
| SECONDARY | 1 |
| UNDER_CONSTRUCTION | 1 |
| UNKNOWN | 9 |
| VERIFIED_PROJECT | 3 |

## Flywheel layers (derived from the register, not hand-written)

| # | Layer | Subnodes | Streams | Physical | Realized credit | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Compute productivity | C01 | 4 | 0 | 0 | **OPPORTUNITY_ONLY** |
| 2 | Energy | E01, E02 | 5 | 0 | 0 | **OPPORTUNITY_ONLY** |
| 3 | Water | W01 | 6 | 2 | 0 | **PHYSICAL_FLOW_PRESENT** |
| 4 | Heat | E02, CHEM01 | 5 | 0 | 0 | **OPPORTUNITY_ONLY** |
| 5 | Materials | MAT01, M01 | 5 | 3 | 0 | **PHYSICAL_FLOW_PRESENT** |
| 6 | Carbon | CARB01, CHEM01 | 5 | 0 | 0 | **OPPORTUNITY_ONLY** |
| 7 | Ocean / coastal ecology | ECO01 | 0 | 0 | 0 | **AWAITING_PRIMARY_ECOLOGICAL_EVIDENCE** |
| 8 | Pollution / toxins | BIO01 | 2 | 0 | 0 | **OPPORTUNITY_ONLY** |
| 9 | Food / agriculture | AGR01 | 3 | 0 | 0 | **OPPORTUNITY_ONLY** |
| 10 | Jobs / community | — | 0 | 0 | 0 | **NO_METERED_STREAM** |
| 11 | Resilience | P01 | 4 | 1 | 0 | **PHYSICAL_FLOW_PRESENT** |
| 12 | Governance / provenance | GOV01 | 0 | 0 | 0 | **CONTROLLED_BY_VETO_AND_PERMIT_STATE** |

## Veto evaluation

> NODE_PASS = AND(all component vetoes pass)

| Veto | State | Why |
| --- | --- | --- |
| `INV-19` | **UNRESOLVED** | Review round 1 advanced this without resolving it. The outfall is now located with coordinates (119°44'33.10"E, 35°34'47.17"N, between the west breakwater and the eastern trestle section) and an approval instrument exists (鲁海渔函[2015]330号). A 2024 peer-reviewed study finds impact confined within 200 m of the outfall. But that study is a SECONDARY analysis, and no discharge permit number or permitted limits were located. A secondary summary may never be promoted to a primary ecological receipt. |
| `ECO-01` | **UNRESOLVED** | Confirmed as a genuine gap, not a search failure. Review round 1 searched directly for the 2017 and 2022 Ocean University of China station-level series and returned NULL. Only secondary summaries are publicly available. This remains the critical path for the node. |
| `CERT-01` | **UNRESOLVED** | Narrowed, but still unresolved. Concrete structural AM has a current standards path, so the veto does not block material reuse or structural printing. It blocks additively manufactured MARINE and PRESSURE-BOUNDARY components, for which no classification-society or pressure-vessel code pathway was located. This makes the veto sharper, not softer: it now names exactly what cannot be cleared. |
| `CARB-01` | **UNRESOLVED** | No CO2 flow is metered and no transfer ledger entry exists yet. |
| `GRID-01` | **UNRESOLVED** | The POLICY route is now confirmed but node participation is not. The Qingdao Port Green Transformation Three-Year Action Plan (2026-2028) is official and names roughly 214 MW wind and 81 MW PV around Qianwan and Dongjiakou with dedicated transmission lines. National 2026 green-direct rules allow multi-user park projects and give PRIORITY support to compute facilities at >=60% self-consumption and >=30% load share. No document names this node as an enrolled user, and no PPA, meter or allocation exists. A plan is not an allocation. |

**Verdict: `NODE_PASS_NOT_ESTABLISHED`**

An unresolved veto is not a pass, and an unresolved veto is not a failure either. It is an absence of evidence. A component that cannot be evaluated cannot be cleared, and no profit elsewhere resolves it.

## Scale comparison

| Quantity | Value |
| --- | --- |
| `w01_2025_process_energy_gwh` | 39.446 |
| `e02_generation_gwh` | 26.0 |
| `e02_cooling_avoided_gwh` | 8.0 |
| `projected_grid_electricity_impact_gwh` | 34.0 |
| `e02_impact_share_of_w01_process_energy` | 0.8619378390711353 |
| `e02_status` | VERIFIED_PROJECT_UNDER_CONSTRUCTION_CURRENT_CREDIT_ZERO |
| `c01_40mw_it_gwh` | 350.4 |
| `c01_40mw_facility_gwh_at_pue_1_25` | 438.0 |
| `c01_40mw_share_of_w01_process_energy` | 11.10378745626933 |
| `c01_40mw_share_of_e02_impact` | 12.882352941176471 |

26 GWh is projected generation; 8 GWh is projected avoided grid consumption from cooling. They are separate edges and are never summed into one physical energy stream. The total is an electrical-system impact only.

The LNG cold-energy cascade is projected at a 34 GWh/year electrical-system impact across generation and avoided cooling, about 86% of W01's entire 2025 process energy. A 40 MW compute subnode would draw 438 GWh/year at the PUE 1.25 reference, about 11x W01's process energy and about 13x that whole impact. The locality's energy resources are large; the compute load is larger. Neither figure may be netted against the other, and both are zero credit.

## Pareto rule

The optimizer is a Pareto front, not a scalar score. There is no single number that can rank a locality, because a scalar score is exactly what allows a local failure to be washed out by a gain somewhere else.

## What this changes

Runs 0-3 do not become obsolete. They become the audited history of one subnode. The locality is not a bigger plant; it is a metabolism, and the intelligence lives in the metered edges between subnodes.

## Next receipts

- Dongjiakou circular-economy implementation plan: which arrows the locality may legally connect
- Chemical-park utility map: waste heat, steam, CO2, wastewater by plant
- LNG cold-energy cascade EIA: thermal output specs and CO2 liquefaction potential
- Pilot base project list: which of the 30 concurrent slots are materials/3D printing
- Node-001 green-direct eligibility confirmation
- Dongjiakou construction-waste allocation (contractual)
