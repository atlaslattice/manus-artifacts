# Node-001 Regional Green-Power Lane v0.1

## Receipt landed

The 214 MW wind + 81 MW PV regional claim is supported by the Qingdao Municipal Government's Qingdao Port Green Transformation Three-Year Action Plan (2026-2028).

Official plan:

```text
~214 MW wind
~81 MW PV
dedicated transmission lines
supply target: Qianwan + Dongjiakou port areas
goal: strive to begin green-direct implementation by 2028
```

The same plan also calls for:

```text
20.1 MW Qianwan north wind
>30 GWh/year generation target when built
>=15 MW new distributed PV across the port system
~5 MW PV in Dongjiakou port-area wastewater/canopy sites
1 virtual power plant by 2028
source-grid-load-storage integrated control
```

## Critical boundary

The plan is for the two port areas. We have not found a receipt showing:

```text
Dongjiakou desalination plant is an enrolled port load
Node-001 receives a MW or MWh allocation
Node-001 can sign the direct-connection contract
the desalination operator is a project participant
the dedicated line reaches the plant meter
PPA / direct-green price
wheeling/network charges
```

Therefore:

```text
regional_green_direct_exists_as_plan = REPORTED
Node001_access                         = UNKNOWN
Node001_green_direct_energy_credit    = 0
```

## Policy pathway

National 2026 policy permits multi-user green-power direct connection among multiple legal entities and explicitly supports green-demand users, industrial/zero-carbon parks and compute facilities.

Shandong policy also expands eligibility for existing coastal-port loads, compute infrastructure and multi-user projects.

This makes a port + desalination + compute direct-green architecture policy-plausible, not automatically approved.

## Scale observation

Node-001's 2025 UF+RO process energy is:

```text
39.446 GWh/year
average process power ~4.503 MW
```

The proposed regional portfolio is approximately 295 MW renewable nameplate.

The only safe conclusion is that Node-001 is a small load relative to the planned regional nameplate.

Do not infer annual coverage from nameplate. Capacity factors, allocation, losses, curtailment, line capacity and contract terms are still required.

## Green-power transfer function

Let:

```text
G_t = metered eligible regional renewable generation
a_t = contracted Node-001 allocation fraction / delivery rule
L_t = Node-001 load
```

Then:

```text
green_direct_used_t = min(L_t, a_t * G_t after contractual/network limits)
```

Annual direct-green share is computed from the hourly sum, not from 295 MW nameplate.

## Price warning

Shandong's 2026 renewable mechanism prices reported from the provincial DRC/Energy Bureau are 0.310 CNY/kWh wind and 0.261 CNY/kWh PV.

These are generator-side policy settlement references, not Node-001 retail/PPA/direct-connection prices, and are not inserted into Node economics.

## Keeper

**The regional supply opportunity is now verified. Node-001 access is not.**