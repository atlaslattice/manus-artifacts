# Dongjiakou Node-001 — Second-Layer Receipt Search + Run 2 H01

Date: 2026-10-06

## Targeted search result

We searched the exact layers requested after Run 1:

- Shandong pricing / DRC-policy layer
- Qingdao subsidy / audit / fiscal layer
- EIA / intake / hydraulic layer

### Current tariff

No 2026 Dongjiakou-specific effective electricity price was located.

A stronger policy boundary was found: Shandong's support policy waived demand/capacity charges for qualifying two-part-tariff desalination electricity through the end of 2025 and supported qualified desalination enterprises participating in electricity-market transactions.

Therefore:

```text
2018-2020 preferential energy price = REPORTED
through-2025 capacity-charge policy = REPORTED
2026 effective plant settlement     = UNKNOWN
```

A generic provincial rate is still prohibited.

### Subsidy/audit layer

A 2025 Qingdao municipal budget reports 188M CNY of city-wide seawater-desalination operating subsidies.

This is aggregate context only. No share is allocated to Dongjiakou without a plant-specific schedule.

### 2.5 kWh/m3 clarification

A stronger Qingdao Daily / Guanhai source says Dongjiakou's plant tonne-water electricity consumption had fallen to about 2.5 kWh/m3.

That supports:

```text
HISTORICAL_PLANT_LEVEL_REPORTED_SEC
```

but not:

```text
HISTORICAL_FENCE_LINE_METERED_SEC
```

because no meter scope, auxiliary boundary, intake/product-pumping accounting, or underlying energy series is exposed.

The later 2.2 kWh/m3 receipt is explicitly UF+RO. Therefore delta_aux = 0.3 remains prohibited.

### Hydraulic search

Historical/project details report an approximately 1.7 km DN1600 nearshore intake and say seawater gravity-flows into the intake-pump suction pool.

Engineering literature on the real plant reports:

```text
5 SWRO high-pressure pumps
920 m3/h each
2100 kW motors each
selected pump efficiency 86.1%
operating head roughly 400-630 m
```

Those hundreds of metres are motor-supplied RO process pressure and sit inside the RO/ERD loop. They are not H01 hydro opportunity.

The current intake-relocation project exposes 1565 m of new intake, 840,000 t/day intake design, and a 300,000 t/day long-term desalination planning scale, but no public PRV schedule, product-line pressure drop, usable outfall head, or other dissipated-head point.

Therefore:

```text
H_available = UNKNOWN
Run 2 baseline hydro credit = 0
```

## Run 2 executed

Run 2 is a technical transfer function rather than a guessed point estimate.

Using the reported 2025 product-water volume:

```text
V = 17.93M m3/year
average flow ~= 0.5686 m3/s
```

Hydraulic energy:

```text
E = rho * g * V * H * eta
```

Ideal coefficient:

```text
48.843 MWh/year per metre of H at eta=1
```

Illustrative eta=0.8 coefficient:

```text
39.074 MWh/year per metre
4.461 kW average per metre
~0.0991% of 2025 UF+RO electricity per metre
```

Sensitivity at eta=0.8:

```text
1 m  -> 0.0391 GWh/y -> 0.099%
5 m  -> 0.1954 GWh/y -> 0.495%
10 m -> 0.3907 GWh/y -> 0.991%
20 m -> 0.7815 GWh/y -> 1.981%
50 m -> 1.9537 GWh/y -> 4.953%
```

This is not evidence that any of those heads exist.

The plant question is now simple: where, if anywhere, is pressure/head currently destroyed across a valve, pressure zone, gravity drop, or post-ERD discharge condition?

## Extra temporal receipt

A Qingdao Water Group financing disclosure reports 2021 average Dongjiakou supply of 33,400 m3/day, corresponding to U_2021 = 33.4%.

The dated utilization series is now:

```text
2020  U ~34.58%
2021  U ~33.40%
2025  U ~49.12%
```

## Current status

```text
Run 0.2 operating baseline     EXECUTED
Run 1 solar                    EXECUTED / survives technically
Run 2 unused-head hydro        EXECUTED as transfer function
Run 2 site output              0 credited until H_available is measured

2026 tariff                    UNKNOWN
whole-site current SEC         UNKNOWN
current measured recovery      UNKNOWN
current brine chemistry        UNKNOWN
```

Keeper: A module with an unknown site parameter should return a transfer function, not a fictional point estimate.