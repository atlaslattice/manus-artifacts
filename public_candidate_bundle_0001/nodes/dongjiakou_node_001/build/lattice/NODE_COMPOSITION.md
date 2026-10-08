STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Node Composition — What an Atlas Locality Node Actually Contains

**Document ID:** ATLAS-LATTICE-NODE-COMPOSITION-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON — **NON-DEPLOYABLE**
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`
**Reference node:** Dongjiakou, Qingdao, Shandong — `DONGJIAKOU-NODE-001`

---

## 1. The claim, and the test of it

The framing offered is *smart cities 2.0 — except actually smart*: a locality node
that is port-operating, data-centre-driven, additive-manufacturing-enabled, and
built on green desalination 2.0 with ion extraction.

"Actually smart" is not a marketing word here. It has a test:

> **A node is actually smart if every claim it makes can be traced to a receipt,
> and it publishes what it does not know as loudly as what it does.**

Smart cities 1.0 failed in a specific, repeatable way: sensors were deployed,
dashboards were built, and the numbers were never tied to a physical consequence.
The failure was not technological. It was **evidential**.

So the composition below is specified twice: once as a physical stack, and once as
the evidence that each element must produce before it may be counted.

---

## 2. The node stack

A locality node is a **multi-resource refinery plus its host economy**, not a
desalination plant with extras bolted on.

```
                    ┌─────────────────────────────────────────────┐
   SEAWATER ───────▶│  I01  pollution interception (pretreatment) │
                    └────────────────────┬────────────────────────┘
                                         ▼
                    ┌─────────────────────────────────────────────┐
                    │  W01  GREEN DESALINATION 2.0                │
                    │       UF + RO, energy recovery, membrane    │
                    │       lifecycle, adaptive fouling control   │
                    └───────┬──────────────────────┬──────────────┘
                            │ product water        │ brine / concentrate
                            ▼                      ▼
        ┌───────────────────────┐    ┌──────────────────────────────────┐
        │  municipal + port +   │    │  R01  RESOURCE EXTRACTION        │
        │  industrial + compute │    │       Na/Cl bulk chemistry       │
        │  water supply         │    │       Mg / Ca / K / Br routing   │
        └───────────┬───────────┘    │       Li  (trace-resource lane)  │
                    │                │       D   (isotope lane)         │
                    │                │       U, trace, strategic        │
                    │                │       carbon mineralization      │
                    │                └──────────┬───────────────────────┘
                    │                           │ residual water
                    │                           ▼
                    │                ┌──────────────────────────────────┐
                    │                │  ecologically bounded discharge   │
                    │                │  INV-19 VETO — not a score        │
                    │                └──────────────────────────────────┘
                    ▼
   ┌──────────────────────────┐   ┌──────────────────────────┐
   │  C01  COMPUTE            │   │  S01 / B01  ENERGY       │
   │  data-centre-driven      │◀─▶│  on-site PV, storage,    │
   │  advisory fabric         │   │  direct-green access     │
   │  LOAD, not a source      │   │  G01  regional green     │
   └────────────┬─────────────┘   └──────────────────────────┘
                │ waste heat (currently zero credit)
                ▼
   ┌──────────────────────────┐   ┌──────────────────────────┐
   │  M01  ADDITIVE MFG       │   │  P01  PORT OPERATIONS    │
   │  3D print spares, marine │◀─▶│  the demand signal and   │
   │  components, construction│   │  the logistics spine     │
   └──────────────────────────┘   └──────────────────────────┘
                │
                ▼
   ┌──────────────────────────┐   ┌──────────────────────────┐
   │  BIO01  BIOMETABOLIC     │   │  OAE01  RESEARCH LANE    │
   │  organics, wastewater,   │   │  alkalinity enhancement  │
   │  nutrient, compost       │   │  NO CREDIT. VETO-BEARING │
   └──────────────────────────┘   └──────────────────────────┘
```

---

## 3. Component register

| ID | Component | Role | Credit posture |
| --- | --- | --- | --- |
| `W01_DESAL` | Green desalination 2.0 | Water supply | Receipt-backed only |
| `R01_RESOURCE_EXTRACTION` | Ion, mineral and trace-resource extraction | Product refinery | **Zero** until all eight questions receipted |
| `I01_POLLUTION_INTERCEPTION` | Contaminant capture | Environmental | Only for measured removed load with verified fate |
| `S01_ROOFTOP_PV` | On-site generation | Supply | Allocated **once** |
| `B01_STORAGE` | Electrical, water, thermal storage | Flexibility | Zero until measured hourly mismatch |
| `G01_REGIONAL_GREEN` | Regional generation access | Supply | Zero until a node allocation exists |
| `C01_COMPUTE` | Compute and advisory plane | **Load** | Never a source. Actuator authority **NONE** |
| `M01_ADDITIVE_MANUFACTURING` | 3D print manufacturing | Local production | Load. Material credit only for assayed, contracted output |
| `P01_PORT_LOADS` | Port operations | Demand + logistics | Green eligibility UNKNOWN until the load set is named |
| `BIO01_BIOMETABOLIC` | Organics, wastewater, nutrients | Circular loop | Zero until feedstock, chemistry and off-take receipts close |
| `OAE01_ALKALINITY_RESEARCH` | Ocean alkalinity enhancement | Research | **No credit. Veto-bearing.** |

---

## 4. Why "data-centre-driven" is the right framing and the wrong claim

The compute layer is what makes a locality node *reflexive*: it can observe the
plant, forecast, triage anomalies, and explain itself to an operator. That is real
value and it is why compute sits at the centre of the diagram.

But the framing must not slip into the claim.

> **Compute is a load, not an energy source.**

The 100 kW commissioning tier draws 0.876 GWh/year of IT energy and 1.095 GWh/year
of facility energy at the PUE 1.25 *reference* — about **2.78%** of the node's
2025 process-train energy. A 1 MW tier would be **27.76%**. That is a material new
load, not a free one.

And the central rule stands:

> **Compute must pay rent in measured service, recovered heat, flexibility,
> resilience, or verified efficiency — not in promises.**

Net-positive is currently `NOT_PROVEN`, and it is unmeasurable until M1–M25 exist
(see `NET_POSITIVE_PATHWAY.md`). Three of its four terms have no instrument.

---

## 5. Why additive manufacturing plus the port is the sleeper

This is the part of the composition most likely to pay off first, and it is worth
saying why.

A port and a desalination plant share a **chronic, high-value, low-volume spare
parts problem**: impellers, valve bodies, pump components, brackets, marine
fittings, corrosion-resistant replacement parts. The conventional pattern is long
lead times, large minimum order quantities, and warehouse inventory held against
uncertainty.

Additive manufacturing changes the economics of that specific problem:

| Property | Consequence |
| --- | --- |
| No tooling cost | Economical at quantity one |
| Digital inventory | The spare is a file, not a shelf item |
| Local production | Lead time measured in hours, not months |
| Design iteration | A failed part can be redesigned, not reordered |

**The honest accounting posture:** M01 is a **load**. It earns a material or
service credit only for assayed, contracted output. The plausible value is
avoided downtime and avoided inventory, which must be **measured** as a
before/after KPI — the same discipline applied to every other component.

And the same gate applies: a printed part is not a certified part. Marine and
pressure-boundary components carry certification requirements, and a node that
prints an uncertified pressure part has created a safety problem, not a saving.
**Certification is a veto-bearing requirement, not a line item.**

---

## 6. How the components actually interlock

The interlock is the point. Isolated components are a list; interlocks are a node.

| Interlock | Physical coupling | Status |
| --- | --- | --- |
| Desalination → resource extraction | Brine is the refinery feedstock | Brine volume is modelled; chemistry is UNKNOWN |
| Compute → desalination thermal | Compute waste heat to CIP thermal duty | **Zero credit.** No setpoint, duty, COP or overlap |
| PV → compute and desalination | Shared generation | `PV_credit_compute + PV_credit_desalination <= measured PV generation` |
| Port → additive manufacturing | Demand for spares and marine components | Concept. No contracted demand |
| Additive manufacturing → desalination | Locally printed spares and components | Concept. No certification path defined |
| Wastewater → desalination | Reclaimed water displacing product water | Zero until verified displacement |
| Organics → energy | Biogas to heat or power | Zero until metered gas and conversion |
| Resource extraction → ecology | Residual brine and eluate fate | **INV-19 VETO** |

Every interlock is a **potential double-counting site**, which is why the single
credit rule applies at the interlock rather than at the component.

---

## 7. The sequence — and why it is not negotiable

```
verified baseline
  -> one module at a time
  -> measure interaction
  -> stack only survivors
```

This is the programme's own rule and it is the reason the node is built in this
order rather than all at once.

| Stage | What happens | Exit criterion |
| --- | --- | --- |
| 0 | Verified baseline | Run 0 / 0.2 reproduce; whole-site SEC measured |
| 1 | One module at a time | A module has all eight receipts or returns a transfer function |
| 2 | Measure interaction | Interlock effects measured, not assumed |
| 3 | Stack only survivors | Run 7 with sequence-dependent interference edges |

**Run 7 cannot begin before Run 6 has receipts.** Interference between modules is
a real physical phenomenon and cannot be reasoned into existence from first
principles — it has to be measured. And Run 8's stochastic analysis carries a
hard rule: **UNKNOWN may not be sampled.**

---

## 8. What would make this smart cities 1.0 again

The failure modes are known. They are listed here so they can be caught early.

| Failure mode | How it would appear here |
| --- | --- |
| Dashboard without consequence | KPIs trended but no physical action gated on them |
| Model authority creep | A model recommendation reaching PLC/SCADA without operator approval |
| Inventory sold as yield | Resource concentration quoted as recovered product |
| Gradient sold as product | *"Products are not power. Gradients are power."* — the reverse error |
| Aggregate laundering | A favourable node netted against an unfavourable one |
| Planned capacity as operating state | Regional MW counted as node allocation |
| Secondary data as primary | A summary promoted to a measured ecological receipt |
| Consensus as evidence | Three models agreeing treated as verification |
| Veto offsetting | Profit or carbon used to answer an ecological failure |
| Vendor lock as architecture | A model version baked into a constitutional rule |

Each of these has a **gate** in this package. G01–G16 cover the node, L01–L10
cover the lattice, and both sets are enforced by code that fails the build.

---

## 9. Propagation beyond Node-001

Node-001 is the proving ground. If it survives, the *pattern* propagates — not
the numbers.

```
Node-001  Dongjiakou, Qingdao        reference implementation, this package
Node-002  Baifa                      lithium-recovery calibration lane
Node-003  Tianjin Nangang            domestic-equipment lane
Node-004  Lubei                      mature cascading-brine lane
Node-005  Yellow Sea                 OAE field-calibration lane
   ...
then a fleet digital twin with SITE HETEROGENEITY PRESERVED
```

> **Never assume one SEC, one recovery, one tariff or one ecology state for the
> whole fleet.**

The architecture is portable. The evidence is not. A node that inherits another
node's measured value has committed the original error in a new place.

---

## 10. Keeper

> Products are not power. Gradients are power.

> Ask every state transition to pay rent.

> Follow transformations, not just objects.

> The lattice tells us where to look. Evidence tells us what is real.

> Dream freely. Promote nothing without receipts.
