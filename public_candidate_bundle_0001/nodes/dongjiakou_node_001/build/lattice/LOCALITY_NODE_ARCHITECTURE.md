STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Locality Node Architecture

**Document ID:** ATLAS-LATTICE-LOCALITY-NODE-ARCHITECTURE-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON — **NON-DEPLOYABLE**
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

---

## 1. The shift

Dongjiakou is not a desalination plant with extras bolted on. It is a
**locality-scale parent node**, and the intelligence lives in the **metered
transfer edges between its subnodes** — not in pretending the locality is one
giant plant.

```
ATLAS LOCALITY NODE — DONGJIAKOU
|
|-- W01    Water / desalination
|-- C01    Compute + ORCS advisory lattice
|-- P01    Port / rail / logistics metabolism
|-- E01    Grid / wind / PV / storage
|-- E02    LNG cold-energy cascade / air separation
|-- R01    Resource extraction from brine
|-- BIO01  Organics / wastewater / nutrients
|-- M01    Additive manufacturing / 3D print
|-- MAT01  Steel slag / tires / construction materials
|-- CHEM01 Chemical-park process streams
|-- AGR01  Grain / food / controlled-environment agriculture
|-- CARB01 CO2 capture / utilization / mineralization
|-- ECO01  Coastal and ecological monitoring
`-- GOV01  Provenance / contracts / vetoes
```

**What this does not do:** it does not fold the whole locality into one positive
Node-001 number. W01 keeps its existing calculus, and Runs 0–3 **do not become
obsolete**. They become the audited history of one subnode.

> The locality is not a bigger plant. It is a metabolism.

---

## 2. Every arrow is a first-class ledger entry

A stream edge carries fifteen fields. An edge missing one is not a ledger entry.

| Field | Question it answers |
| --- | --- |
| `stream_id` | Which flow is this, uniquely? |
| `source_subnode` | Where does it come from? |
| `sink_subnode` | Where does it go? |
| `material_or_energy` | What is it? |
| `quantity` | How much, with units and period? |
| `quality_composition` | What grade or chemistry? |
| `temperature_pressure` | At what conditions? |
| `time_profile` | When does it arrive, hour by hour? |
| `ownership` | Who owns it? |
| `contract_status` | Is there an agreement, and of what kind? |
| `evidence_class` | MEASURED / REPORTED / DERIVED / MODELED / PLANNED / … / UNKNOWN |
| `conversion_losses` | What is lost in the transfer? |
| `residual_fate` | Where does it end up when it is done? |
| `vetoes` | Which vetoes does this edge engage? |
| `primary_credit_owner` | Who may count it? |

`time_profile` and `residual_fate` are the two fields most often missing in
conventional industrial symbiosis work, and they are the two that decide whether
a symbiosis is real. A heat stream that arrives when nothing needs heat is not a
heat stream.

---

## 3. The register, as built

`python3 simulator.py locality` emits the register. Current state:

| | |
| --- | --- |
| Subnodes declared | **15** |
| Streams registered | **22** — **6 physical**, **16 opportunity** |
| Streams realizing credit | **0** |
| Streams with incomplete schema | **0** |
| Locality clearance | **`NOT_ESTABLISHED`** |

**Zero streams realize credit.** Every edge carries an `edge_state`, and only
`MEASURED_PHYSICAL` can realize credit. Nothing at Dongjiakou is measured yet.

### 3.1 Two graphs, not one

A graph that draws an operational steel-slag link and a hypothetical CO2
coupling the same way looks connected when it is not. At 50, 100 or 500
localities that difference decides whether the map is usable.

| Graph | Contains | Count |
| --- | --- | --- |
| **Physical StreamGraph** | `MEASURED_PHYSICAL`, `REPORTED_PHYSICAL` — what flows today | **6** |
| **Opportunity Graph** | `CONTRACTED`, `UNDER_CONSTRUCTION`, `PLANNED`, `CANDIDATE_COUPLING`, `REFERENCE_ONLY` | **16** |

### 3.2 A stream may not claim a sink it has not got

We know the plant produced 17.93 Mm³ of water in 2025. We do **not** know that
its sink is the port. Likewise, brine is not drawn to resource recovery, because
recovery is a candidate fate, not the current one.

Both therefore route to an external boundary (`EXT01`) as `REPORTED_PHYSICAL`,
with **separate** `CANDIDATE_COUPLING` edges for the sinks that might later
close.

### 3.3 One owner, bounded allocation

Shared credit ownership is where double counting eventually sneaks back in. A
physical quantity now has exactly **one** ledger owner; anyone else receives a
**bounded allocation** under a conservation constraint:

```
sum(allocations) <= measured_generation
```

---

## 4. The veto rule, and why node clearance is not established

```
NODE_PASS = AND(all component vetoes pass)
```

| Veto | State | Why |
| --- | --- | --- |
| `INV-19` downstream water quality | **UNRESOLVED** | Raw station-level monitoring data missing |
| `ECO-01` primary ecological status | **UNRESOLVED** | Only secondary summaries available |
| `CERT-01` pressure/marine component certification | **UNRESOLVED** | No certification path for printed parts |
| `CARB-01` CO2 counted once | **UNRESOLVED** | No metered CO2 flow, no transfer ledger entry |
| `GRID-01` renewable attribute ownership | **UNRESOLVED** | No green-direct allocation or contract |

> **An unresolved veto is not a pass.**

A component that cannot be evaluated cannot be cleared. This is the structural
difference from a dashboard city: **a dashboard can show you the desalination
plant failing while the compute centre is profitable. A flywheel cannot pass if
any component fails.**

**`UNRESOLVED` and `FAIL` are semantically distinct.** Unresolved is an absence
of evidence; fail is evidence of a problem. Neither is a pass, but they call for
different responses — and conflating them would be its own error.

### 4.1 Validation is not clearance

These are two different questions and must never be read as one:

| State | Question | Answer |
| --- | --- | --- |
| `SIMULATOR_VALIDATION` | Did the software pass its epistemic checks? | **PASS** |
| `LOCALITY_CLEARANCE` | Has the physical locality node passed its vetoes? | **NOT_ESTABLISHED** |

They are perfectly compatible: **the simulator passed *because* it correctly
refused to clear the physical node.** Never present the gate count as evidence
that Dongjiakou itself has passed certification, ecology or grid gates.

---

## 5. The scale reframe

Two new numbers, and they are worth sitting with.

| Flow | Magnitude | Share of W01's 2025 process energy (39.446 GWh) |
| --- | --- | --- |
| LNG cold-energy cascade (26 GWh generation + 8 GWh avoided cooling) | **34 GWh/year** | **~86%** |
| 40 MW compute subnode at PUE 1.25 reference | **438 GWh/year** | **~1,110%** |

The locality's energy resources are large. The compute load is larger.

So the question is not:

> *"There are ~295 MW of renewables planned nearby, therefore run 40 MW of compute."*

It is:

> **"Can a 40 MW compute subnode be contracted, dispatched and thermally
> integrated into this locality while preserving water, ecological, grid, carbon
> and component vetoes hour by hour?"**

That is a better ORCS problem, and it is the one the architecture is built to ask.

**Correction carried into the record:** the LNG cascade figures were described in
one source as *"measured, operational."* They are not. Contemporary reporting
describes the project as having completed bidding and entered detailed design and
construction, with 26 GWh/year and 8 GWh/year as **projected at commissioning**.
The register therefore records
`E02_LNG_COLD_CASCADE = VERIFIED_PROJECT / UNDER_CONSTRUCTION / CURRENT_CREDIT_ZERO`.
This was independently re-checked: China Daily reports the facility "is expected
to generate 26 million kWh of electricity annually."

---

## 6. The portable schema

The next nodes are **not** clones of Dongjiakou. Define a generic node, then
instantiate a desalination-containing subclass:

```
LOCALITY_NODE
  + DESAL_SUBNODE          (optional after the desal cohort proves the ontology)
  + ORCS_COMPUTE_SUBNODE
  + site-specific modules
```

Consequences:

| Consequence | Statement |
| --- | --- |
| The 167 desalination projects become a **discovery universe**, not a node count | Some localities contain multiple desal projects, so the locality count need not equal 167 |
| Dongjiakou becomes the **first fully resolved template** | Not a special case accidentally hard-coded into the system |
| `DESAL_SUBNODE` becomes **optional** | An inland steel town, agricultural basin, mining district, island, data-centre corridor or municipal region can use the same StreamGraph without pretending to have seawater RO |

That is how "beyond 167" scales rigorously rather than rhetorically.

---

## 7. Why this is not smart cities 1.0

> The system is not smarter because it has more sensors. It is smarter because
> **physical flows are metered**, **every component retains an auditable ledger**,
> **optimization is Pareto rather than a fake universal score**, and **a local
> failure cannot be washed out by profit somewhere else.**

The Pareto rule is load-bearing and is enforced in the register:

> There is no single number that can rank a locality, because a scalar score is
> exactly what allows a local failure to be washed out by a gain somewhere else.

---

## 8. What changed, and what did not

| Changed | Did not change |
| --- | --- |
| The boundary: plant → locality | Runs 0–3 and their reproduced numbers |
| The unit of analysis: component → metered edge | The evidence vocabulary |
| The compute question: "can we power it" → "can we dispatch and integrate it" | C01 is a load, never a source |
| The node set: 167 projects → a discovery universe | UNKNOWN stays UNKNOWN |
| New subnodes added: E02, M01, MAT01, CHEM01, AGR01, CARB01, ECO01, GOV01 | No credit before measurement |

---

## 9. Next receipts, in priority order

| Priority | Receipt | Unlocks |
| --- | --- | --- |
| 1 | Dongjiakou circular-economy implementation plan | Which flows and partners are contractual |
| 2 | Chemical-park utility map (heat, steam, CO2, wastewater by plant) | AGR01 sizing, CARB01 coupling |
| 3 | LNG cold-energy cascade EIA | E02 thermal specs, CO2 liquefaction potential |
| 4 | Pilot base project list | Which of the 30 concurrent slots are materials / 3D printing |
| 5 | Node-001 green-direct eligibility confirmation | The 40 MW argument |
| 6 | Dongjiakou construction-waste allocation | M01 feedstock |

If these land, the downstream layer becomes a **measured industrial symbiosis**. If
they do not, the components stay zero-credit. Same discipline as everything else.

---

## 10. Keeper

> The node is not "smart" because it has sensors. It is smart because every flow
> is metered, every component is auditable, and no aggregate net-positive claim
> can hide a local veto.

> **The architecture is the intelligence.**
