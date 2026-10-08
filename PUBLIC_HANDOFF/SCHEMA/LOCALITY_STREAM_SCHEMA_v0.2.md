# Atlas Lattice Portable Locality + Stream Schema v0.2

```text
STATUS: PUBLIC_CANDIDATE_NON_CANON
DEPLOYABLE: NO
DATE: 2026-10-08
PURPOSE: portable schema for locality nodes, stream edges, evidence state, loop closure, sulfur logistics and compute
```

## 1. Parent object

```yaml
LOCALITY_NODE:
  node_id: string
  locality_name: string
  boundary_definition: string
  population_or_industrial_metabolism: optional
  evidence_state: enum
  locality_clearance: enum
  subnodes: []
  external_boundary: EXT01
  stream_edges: []
  vetoes: []
```

The parent is a **locality metabolism**, not a giant plant.

## 2. Core functional subnodes

```text
W01    water / desalination
C01    compute / digital twin / advisory inference
P01    port / rail / local logistics
P02    sulfur / gypsum regional logistics spine
E01    grid / renewable / storage
E02    LNG cold-energy / air-separation candidate
R01    resource recovery / brine mineral separation
BIO01  organics / wastewater / nutrient recovery
M01    additive manufacturing
MAT01  construction / slag / materials
CHEM01 chemical process streams
AGR01  food / grain / controlled-environment agriculture
CARB01 carbon capture / utilization / mineralization
ECO01  ecological monitoring and vetoes
GOV01  provenance / contracts / evidence / allocation
EXT01  external boundary
```

Facility subnodes may be added where a real physical facility exists inside the boundary.

## 3. Stream-edge schema

Every stream edge must carry:

```yaml
stream_id: string
source_subnode: string
sink_subnode: string
material_or_energy: string
quantity:
  value: number | UNKNOWN
  unit: string
  period: string
quality_composition: object | UNKNOWN
temperature_pressure: object | UNKNOWN
time_profile: object | UNKNOWN
ownership: string | UNKNOWN
contract_status: enum
evidence_class: enum
edge_state: enum
conversion_losses: object | UNKNOWN
residual_fate: string | UNKNOWN
vetoes: []
primary_credit_owner: string | NONE
allocations: []
facility_origin: optional
source_record_ids: []
```

## 4. Evidence vocabulary

Recommended states:

```text
MEASURED
REPORTED
DERIVED
MODELED
SIMULATED
PLANNED
PROPOSED
CONTRACTED
UNDER_CONSTRUCTION
REFERENCE_ONLY
QUARANTINED
UNKNOWN
```

Only an explicitly qualified **MEASURED_PHYSICAL** edge may realize physical credit.

## 5. Graph separation

Maintain at least two graphs:

### Physical graph
Only established physical streams.

### Opportunity graph
CONTRACTED / UNDER_CONSTRUCTION / PLANNED / CANDIDATE / REFERENCE_ONLY streams.

Never draw a candidate sink as if it were the current physical fate.

## 6. Conservation / credit

```text
sum(allocations) <= measured_generation
```

Rules:

- one physical quantity has one primary owner;
- no negative allocations;
- units/time bases must match;
- aggregate values may not backfill a subnode UNKNOWN;
- one tonne / one MWh / one molecule event cannot earn two primary credits.

## 7. Loop-closure contract

A loop becomes `CLOSED_MEASURED` only when all pass:

1. SOURCE
2. MASS
3. QUALITY
4. RIGHT_TO_TRANSFER
5. TIME
6. DISPLACEMENT_OR_COUNTERFACTUAL
7. RESIDUAL_FATE
8. ALLOCATION

A circle of arrows is not a closed loop.

## 8. Locality clearance

```text
NODE_PASS = AND(all component vetoes pass)
```

`UNRESOLVED` is not `PASS` and is not the same as `FAIL`.

Software validation is distinct from physical locality clearance.

## 9. AGR01 invariant

AGR01 is a food/nutrient integration surface, not a siting requirement.

> The locality defines the node. Agriculture adapts to the locality.

Possible AGR implementations:

- open-field agriculture;
- peri-urban/regional catchment;
- greenhouse/CEA;
- rooftop/built-surface production;
- neighboring-node exchange.

Preferred hierarchy:

```text
local use
-> nearby/regional use
-> inter-node exchange
-> long-haul residual surplus
```

## 10. Gypsum / sulfur allocation

No hectare is presumed to need gypsum.

Qualified gypsum may route to:

- AGR01 soil amendment where measured need exists;
- CHEM01 / regional sulfuric-acid conversion;
- MAT01/CARB01 transformation;
- reserve;
- residual disposal.

One tonne receives one primary disposition.

Do not create salinity/sodicity to manufacture gypsum demand.

## 11. P02 logistics schema

```yaml
P02_EDGE:
  source_facility: string
  source_evidence_state: enum
  qualified_CaSO4_t_per_month: number | UNKNOWN
  moisture: number | UNKNOWN
  chemistry: object | UNKNOWN
  origin_node: string
  destination_hub: string | UNKNOWN
  transport_mode: string | UNKNOWN
  distance_km: number | UNKNOWN
  delivered_fraction: number | UNKNOWN
  transport_cost: number | UNKNOWN
  storage_capacity: number | UNKNOWN
  seasonal_inventory: number | UNKNOWN
  receiving_specification: object | UNKNOWN
  accepted_conversion_yield: number | UNKNOWN
  coproduct_fate: string | UNKNOWN
  contract_status: enum
  primary_credit_owner: string | NONE
```

```text
PAIRABLE_H2SO4 =
SUM(qualified_CaSO4_i * delivered_fraction_i * accepted_conversion_yield_i)
```

P02 creates no sulfur; it proves pairing.

## 12. C01 compute invariant

Every locality node has C01 compute capacity, but there is no fixed-MW doctrine.

```text
C01_CAPACITY =
f(
  projected workload,
  latency,
  resilience,
  population/industry,
  sensor density,
  model mix,
  storage,
  network,
  power,
  cooling/heat reuse,
  growth margin
)
```

Compute is always a load.

Useful heat is credited only through a named, measured sink.

## 13. Control / orchestration / model separation

```text
CONTROL:
  PLC / SCADA / deterministic safety systems

ORCHESTRATION:
  workflow, versioning, provenance, artifact and task routing

MODELS:
  advisory research / optimization / audit / challenge
```

No plant operation depends on model availability.

Models advise. Deterministic control executes.

## 14. Tiered deployment

### Tier 1
Desalination-only sulfur nodes.

### Tier 2
Agriculture-integrated locality nodes plus all qualified CaSO4 sources.

### Tier 3
Full lattice optimization.

Tier 3 is optimal, not prerequisite.

## 15. Epistemic doctrine

```text
UNKNOWN stays UNKNOWN.
Raw stays recoverable.
Null results are receipts.
Cross-model agreement is not evidence.
REFERENCE narrows ignorance. It does not create a receipt.
The baseline gets to win.
Products are not power. Gradients are power.
Ask every state transition to pay rent.
Compute is a load, not an energy source.
One physical event gets one primary credit.
Maximum potential is a ceiling, not an instruction.
The lattice tells us where to look. Evidence tells us what is real.
Dream freely. Promote nothing without receipts.
```
