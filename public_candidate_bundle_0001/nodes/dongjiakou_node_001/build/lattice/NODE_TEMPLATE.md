STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Lattice Node Template

**Document ID:** ATLAS-LATTICE-NODE-TEMPLATE-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`
**Reference implementation:** `DONGJIAKOU-NODE-001`

---

## 1. Purpose

This template defines what makes a locality a *node* of the Atlas Lattice, and
what a node must produce before it may be compared with, or aggregated alongside,
any other node.

Node-001 (Dongjiakou, Qingdao, Shandong) is the reference implementation. Every
subsequent node is instantiated by copying this contract, not by inventing a new
one. The value of the lattice is comparability; a node that cannot be compared is
not a node.

> **A node is a bounded, receipted accounting unit, not a place on a map.**

---

## 2. Node identity

| Field | Rule |
| --- | --- |
| `node_id` | `DONGJIAKOU-NODE-001` style: locality name plus zero-padded ordinal |
| `hsn_coordinate` | `H##.S##.N##` — **assigned only after an explicit taxonomy assignment** |
| Coordinate discipline | Do **not** invent a coordinate. Node-001's coordinate is currently `UNASSIGNED` |

The lattice address space is 12 Houses × 12 Spheres × 12 Nodes = 1,728 cells plus
property bands. A candidate node register may exist long before coordinates are
assigned. **Registration is not assignment.**

---

## 3. Required component set

A node is a composition of ledgers. Each component keeps its **own** evidence
profile and its **own** ledger. An aggregate node benefit may never erase a
component-level veto.

| Component ID | Type | Credit rule |
| --- | --- | --- |
| `W01_DESAL` | Desalination | Receipt-backed only |
| `G01_REGIONAL_GREEN` | Regional generation access | Zero until a node allocation exists |
| `S01_ROOFTOP_PV` | On-site generation | Measured generation may be allocated **once only** |
| `B01_STORAGE` | Storage (electrical, water, thermal) | Zero until measured hourly mismatch demonstrates a service |
| `C01_COMPUTE` | Compute and control plane | Load, never a source. Actuator authority **NONE** |
| `P01_PORT_LOADS` | Port and industrial loads | Green eligibility UNKNOWN until the eligible load set is named |
| `GRID01` | Grid interface | Import, export, multi-user direct-green, VPP |
| `BIO01_BIOMETABOLIC` | Organics, wastewater, nutrient recovery | Zero until feedstock, chemistry and off-take receipts close |
| `M01_ADDITIVE_MANUFACTURING` | 3D print manufacturing (port spares, marine components, construction elements) | Load, not a source. Material credit only for assayed, contracted output |
| `R01_RESOURCE_EXTRACTION` | Ion, mineral and trace-resource extraction from brine | **Zero** until all eight resource-module questions are receipted |
| `I01_POLLUTION_INTERCEPTION` | Contaminant capture in pretreatment | Credit only for measured removed load with a verified destruction or sequestration fate |
| `OAE01_ALKALINITY_RESEARCH` | Ocean alkalinity enhancement / carbon-removal research | **Research lane only. No credit. Veto-bearing.** |

A node may omit a component only by recording the omission explicitly. Silence is
not omission.

### 3.1 The node is a refinery, not a plant

The programme framing is the **Alexandrian Seawater Refinery**: a desalination
node is a multi-resource refinery whose product set extends well beyond water.

> **Products are not power. Gradients are power.**

Recovered products are never counted as electrical generation. An energy credit
requires an explicit identified gradient. Resource inventory is not recovery
yield.

### 3.2 Resource modules are not interchangeable

Every resource module — lithium, uranium, deuterium, Mg/Ca/K/Br, microplastics,
persistent contaminants — must answer all eight questions in
`models/run6_resources.py` before earning value: **yield, selectivity, energy,
reagents, material life, residual fate, market ceiling and ecology.**

Two of those are **veto-bearing**: `ecology` and `residual_fate`. A module that
cannot say where its spent brine, eluate, reagent and exhausted material
actually go has not earned a credit, regardless of its yield.

Modules are evaluated **one at a time**. Stacking survivors requires measured
sequence-dependent interference edges, which cannot exist before individual
modules have receipts.

> A module with an unknown site parameter returns a transfer function, not a
> fictional point estimate.

---

## 4. Required evidence classes

Every populated value carries exactly one class. The vocabulary is closed.

| Class | Meaning | May carry a primary credit? | May populate a current state? |
| --- | --- | --- | --- |
| **MEASURED** | Primary instrumented data at this node | Yes | Yes |
| **REPORTED** | Published or reported value with a source record | Yes | Yes, if the report is current |
| **DERIVED** | Arithmetic over cited inputs | Yes | Only if its inputs may |
| **HISTORICAL** | Dated past state | No | **No** |
| **PLANNED** | Future intent | No | **No** |
| **MODELED** | Site-layout or design assumption | No | **No** |
| **SENSITIVITY** | Parametric transfer function | No | No |
| **PROPOSED** | Architecture proposal | No | No |
| **REFERENCE** | External benchmark, not a node receipt | No | No |
| **UNKNOWN** | Not established | No | No |

Only **MEASURED** can establish a current physical state at a node.

---

## 5. Required run set

Each node instantiates the same deterministic run set. The reference
implementation's parameters are in
`../runs/reproduction_spec.json`.

| Run | Content | Baseline credit |
| --- | --- | --- |
| `RUN_0` | Nameplate baseline and per-utilisation coefficients | n/a |
| `RUN_0.2` | Dated operating-year calibration | n/a |
| `RUN_1` | On-site generation sensitivity | Zero |
| `RUN_2` | Unused-head parametric transfer function | Zero |
| `RUN_3` | Compute facility transfer function | Zero heat, zero service |
| `RUN_4A` | Biometabolic transfer functions | Zero across all products |
| `S02` | Storage equivalence transfer function | Zero |

Every run must be reproducible by a pure function of sourced inputs, with no
Monte Carlo and no UNKNOWN imputation.

---

## 6. Inherited gate set

A node inherits the full validator gate set (G01–G16) unmodified. A node **may
add** gates. A node **may not remove or weaken** an inherited gate.

| Gate | Invariant |
| --- | --- |
| G01 | UNKNOWN cannot enter Monte Carlo |
| G02 | UNKNOWN cannot silently become zero |
| G03 | Historical values cannot populate current state |
| G04 | Planned capacity cannot populate operating state |
| G05 | Feed-product residual cannot become marine discharge |
| G06 | One PV kWh cannot receive two primary credits |
| G07 | One recovered mass cannot be double-credited |
| G08 | Compute heat needs a measured sink |
| G09 | Service benefit needs before/after KPI evidence |
| G10 | Ecological veto cannot be offset |
| G11 | LLM actuator authority is NONE |
| G12 | Model consensus is not evidence |
| G13 | RO high-pressure head cannot be counted twice |
| G14 | Existing on-site generation cannot be counted twice |
| G15 | Conservation and bound checks over the credit ledger |
| G16 | Net-positive requires measured terms |

**Every gate must have a negative control.** A gate that cannot be made to fail is
not a gate.

---

## 7. Node pass criteria

A node may be reported as passing only when all of the following hold:

1. Every veto-bearing component passes its **own** veto set.
2. No component-level ecological, safety or compliance veto is offset by profit,
   carbon or energy benefit elsewhere in the node.
3. Every credit entry names a physical resource, an evidence class, a receipt and
   a sourced availability bound.
4. No physical kWh, m³, kg or tonne receives more than one primary credit.
5. Every current-state quantity is either MEASURED or explicitly UNKNOWN.
6. Cross-subsidy between components is reported explicitly and is never renamed
   synergy.
7. The unresolved-UNKNOWN ledger is published alongside the result.

**A profitable or low-carbon component cannot offset a failed ecological veto.**

---

## 8. Lattice interface — how nodes combine without double counting

This section is the part that makes a lattice more than a list.

### 8.1 Single-credit rule at lattice scale

> One physical resource receives at most one primary credit **across the entire
> lattice**, not merely within a node.

A resource that could plausibly be claimed by two nodes — regional generation, a
shared transmission corridor, a shared watershed or receiving water body, a
shared waste feedstock — must be **partitioned explicitly** before either node
claims it.

### 8.2 Import and export declaration

A node must declare, for every cross-boundary flow:

| Field | Description |
| --- | --- |
| `flow_id` | Stable identifier |
| `direction` | import or export |
| `counterparty_node` | The other node, or `REGIONAL` |
| `resource` | The physical resource |
| `quantity` | With units |
| `evidence_class` | Class of the quantity |
| `receipt` | Source record |
| `credit_claim` | Which side takes the primary credit, and why |

### 8.3 Aggregate discipline

- A lattice aggregate is reported as an aggregate. It is **never** attributed back
  to a single node.
- An aggregate may not be used to backfill a node-level UNKNOWN.
- Node-level vetoes are not diluted by lattice-level performance.
- A lattice total is meaningful only for nodes that share a measurement boundary
  definition and a common schema.

### 8.4 Non-comparability must be declared

If two nodes cannot be compared — different boundaries, different evidence
quality, different sector mix — that must be stated. Silence implies comparability
and is therefore a false claim.

---

## 9. Instantiation checklist

To instantiate a new node:

1. Assign `node_id`. Leave `hsn_coordinate` UNASSIGNED until a taxonomy assignment
   exists.
2. Populate the required component set, or record explicit omissions.
3. Create the source manifest with SHA-256 digests for every evidence artifact.
4. Instantiate the run set as pure functions of sourced inputs.
5. Inherit the gate set unmodified.
6. Build the credit ledger and declare a sourced availability bound for every
   resource the node could credit.
7. Publish the unresolved-UNKNOWN ledger.
8. Publish the failure ledger.
9. Declare cross-boundary imports and exports, and which side takes each primary
   credit.
10. Reproduce every derived number against the node's own committed artifacts.
11. Run the gate suite with negative controls.
12. Route the result for human review. **Do not deploy.**

---

## 10. What a node is not

- A node is not a claim of authority over a locality.
- A node is not a partnership, an agreement, or a permit.
- A node is not a deployment.
- A node is not canon.
- A registered candidate node is not an assigned coordinate.
- A lattice aggregate is not evidence about any particular place.

---

## 11. Keeper

> Compute must pay rent in measured service, recovered heat, flexibility,
> resilience, or verified efficiency — not in promises.

> A lattice is only as honest as its least-documented node.
