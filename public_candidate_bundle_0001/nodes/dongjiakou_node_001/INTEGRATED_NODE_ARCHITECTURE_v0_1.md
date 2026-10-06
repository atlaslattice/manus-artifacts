# Dongjiakou Integrated Energy-Water-Compute Node Architecture v0.1

**Status:** PROPOSED NODE-BOUNDARY ARCHITECTURE / NON-CANON. Existing component runs remain valid. No aggregate net-positive claim.

## Boundary move

DeepSeek's architectural correction is accepted: Dongjiakou desalination should remain a receipt-backed **component**, while any future wind/PV, storage, compute, port loads and grid interface sit inside a larger integrated node only when the physical/contractual system actually connects them.

```text
H##.S##.N##     integrated Atlas entry address (not assigned yet)
  |- W01 desalination
  |- G01 regional wind/PV
  |- S01 rooftop PV
  |- B01 electrical/water/thermal storage
  |- C01 compute + advisory control plane
  |- P01 port loads
  `- GRID01 import/export/direct-green/VPP
```

No specific HSN address is invented in this artifact. The coordinate is assigned only through the existing Atlas coordinate/taxonomy process.

## Component runs are preserved

```text
Run 0    nameplate baseline       -> W01 desal component
Run 0.2  2025 operating baseline -> W01 desal component
Run 1    rooftop PV               -> S01 + W01 coupling
Run 2    unused-head hydro        -> W01 transfer function
Run 3    regenerative compute     -> C01 + W01 coupling
```

Nothing is invalidated by expanding the boundary.

## Anti-veto-laundering rule

A node-level positive score cannot offset a component-level hard failure.

```text
NODE_PASS = AND(component_veto_pass_i for every veto-bearing component)
```

Examples:

- downstream-water-quality failure at W01 fails the node regardless of compute revenue;
- cyber/OT isolation failure at C01 fails C01 and therefore the integrated-node claim;
- a port/load commercial win cannot compensate for permit noncompliance;
- renewable generation cannot erase a material or ecology violation elsewhere.

## Cross-subsidy transparency

Three ledgers remain separate:

```text
component standalone ledger
inter-component transfer ledger
aggregate node ledger
```

If compute subsidizes desalination, report exactly that. Do not rename a subsidy as a thermodynamic synergy.

## Control-plane role

C01 may justify itself partly by verified node optimization, but compute is still an electrical load.

Candidate services:

```text
generation/load forecasting
water-storage dispatch support
BESS dispatch advisory
flexible-compute scheduling
maintenance planning
membrane/fouling forecasting
brine-routing simulation
ecological telemetry QA
provenance/event-ledger maintenance
port/regional energy-service analytics
```

Pay-rent metric remains:

```text
verified physical/service benefit / compute facility kWh
```

with benefit disaggregated by type rather than collapsed into one score.

### Proposed model fabric

```text
PRIMARY ELIGIBLE LOCAL ADVISORY FAMILY
DeepSeek

LOCAL CHALLENGER / FAILOVER
Qwen3

OPTIONAL EXTERNAL ADVERSARIAL AUDIT
OpenAI GPT
```

Exact checkpoint names are deployment-manifest state. Model agreement is not evidence. No LLM has PLC/SCADA actuator authority.

## Governance matrix

Every component carries both `regulatory_regime` and `contractual_basis`.

| Component | Regulatory regime | Contract/evidence status |
|---|---|---|
| W01 desal | water + environment + PPP | partial historical/current receipts |
| G01 regional generation | energy + direct-green + interconnection | official regional plan; Node-001 access unknown |
| B01 storage | grid + asset safety | proposed / gated |
| C01 compute | compute/data + cybersecurity + energy | proposed pilot |
| P01 port loads | port + energy | specific eligible-load set unknown |
| GRID01 | grid + multi-user direct-green + VPP | policy pathway verified; contract unknown |

## Green-direct load-set search

The September 2026 Qingdao Port Green Transformation Three-Year Action Plan is stronger than a generic regional-renewables claim. It explicitly says:

```text
~214 MW wind + ~81 MW PV around Qianwan/Dongjiakou
dedicated transmission lines
direct-green supply for the two port areas
source-grid-load-storage architecture
port virtual power plant by 2028
```

However, the official plan does **not** publish an end-user/load list naming the Dongjiakou desalination plant or a future Atlas compute block.

National 2026 multi-user direct-green policy supports green-demand users, industrial/zero-carbon parks and gives priority support to compute facilities. That establishes a policy path, not project enrollment.

Therefore:

```text
regional green-direct project      REPORTED/OFFICIAL PLAN
port-area eligible load concept    REPORTED
specific Node-001 participation    UNKNOWN
Node-001 allocation MW/MWh         UNKNOWN
direct-green contract price        UNKNOWN
Node-001 green-direct credit       0
```

## Integrated-node optimization

Do not optimize a single aggregate score by default.

Return a Pareto front over component-resolved outcomes:

```text
water-service reliability
grid import/export
renewable use and curtailment
compute service delivered
storage throughput/degradation
useful heat delivered
chemical/material consumption
ecological status
carbon boundary
component and aggregate economics when receipts exist
```

Every optimum must retain the component ledger that produced it.

## Expansion gate

The integrated node becomes more than a conceptual overlay only after at least one cross-component physical/contractual link is received, e.g.:

```text
green-direct participation/meter
shared BESS meter/dispatch
measured C01-to-CIP heat transfer
measured compute flexible-load dispatch
shared VPP enrollment
```

Until then, the larger boundary is a useful architecture with zero unearned cross-component credit.

## Keeper

**Expand the node when the physical system genuinely spans more than one plant. Preserve component auditability. Never let an aggregate net-positive claim hide a component-level veto.**