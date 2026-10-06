# Dongjiakou Node-001 — Highest-Value Receipt Search

Date: 2026-10-06  
Status: receipt search complete for this pass; unresolved fields remain UNKNOWN.

DeepSeek's five requested targets were searched directly rather than replaced with generic assumptions.

| Target | Result |
|---|---|
| 2026 effective electricity tariff | **NOT FOUND** — historical 0.555 CNY/kWh remains the last plant-specific receipt located |
| Whole-site SEC / delta_aux | **NOT RESOLVED** — current 2.2 kWh/m3 is UF+RO; historical 2023 plant-level quote ~2.5 kWh/m3 is boundary/time mismatched |
| Dated current recovery | **NOT RESOLVED** — 45–50% remains the published technology/application range |
| Current brine chemistry | **NOT RESOLVED** — daily manual concentrate testing is reported, but analytical values were not located |
| CIP/fouling chronology | **PARTIALLY OPENED** — 2026 site-specific cleaning and pretreatment upgrade procurements were found; operating fouling time series remains missing |

## New site-specific operating/maintenance receipts

### Chemical-cleaning system modernization

A 2026 Qingdao public-resources tender is explicitly for a **chemical-cleaning air-source heat-pump heating system** at Dongjiakou.

The procurement describes:

```text
4 air-source heat-pump units
3 x 30 m3 insulated stainless tanks
1 control system
associated piping / equipment
tender ceiling: 860,000 CNY
parent equipment-upgrade project: 70M CNY
15% ultra-long special treasury bond; balance self-funded
```

This is strong evidence that chemical cleaning is a real, actively modernized plant subsystem.

It does **not** tell us cleaning frequency, foulant class, cleaning chemicals, normalized flux decline or avoided membrane replacements.

### Pretreatment modernization

A separate 2026 procurement calls for **10 customized domestic self-cleaning filters**, with a maximum tender price of 2.6M CNY.

This moves F01 from an abstract "maybe improve pretreatment" idea to an incremental question against an already-upgrading plant:

> Can adaptive chemistry / sensing / control improve outcomes beyond Dongjiakou's existing UF + anti-fouling membranes + dynamic control + new self-cleaning-filter modernization?

No benefit is credited yet.

## Historical energy boundary

A 2023 Qingdao interview quoted Dongjiakou at roughly **2.5 kWh per tonne of product water**.

That is useful historical context, but it is not used to set current delta_aux because:

```text
2023 value       historical
boundary         not sufficiently explicit
2025 value       UF+RO = ~2.2 kWh/m3
plant configuration changed over time
```

So:

```text
current whole-site SEC = UNKNOWN
```

remains correct.

## Ecological evidence improved, but raw data still matters

A national draft standard on desalination concentrate discharge summarizes multi-year monitoring around Qingdao Baifa and Dongjiakou. It reports temperature, salinity, dissolved oxygen, nutrients, sediment and biological indicators remained within normal variation and that no obvious ecological effect from concentrate discharge was identified in the summarized evaluation.

A separate 2023 intake/outfall demonstration report says Dongjiakou:

```text
manually tests outlet concentrate daily
commissioned Ocean University of China follow-up studies in 2017 and 2022
reported rapid salinity dispersion
reported salinity approaching ambient about 100 m from the outfall
```

These findings strengthen the historical ecological evidence chain.

They do **not** replace the underlying station-level monitoring tables. ORCS ecological status therefore stays below VERIFIED until primary data / permits / current monitoring are inspected.

## Current tariff search

We searched for:

```text
plant-specific 2026 electricity tariff
retail electricity contract
market settlement
electricity procurement
agency-purchase tariff
operator financial disclosure
```

No defensible 2026 plant-specific electricity price was located.

This is a real negative result. The economic model should continue to emit:

```text
technical energy delta = computable
current CNY delta      = UNKNOWN
```

rather than backfilling a provincial generic rate.

## Result for the module sequence

Run 1 solar survives unchanged.

Run 2 hydro remains zero until actual unused hydraulic head is found.

F01 is now **better specified**, because we have direct evidence of active chemical-cleaning and self-cleaning-filter upgrades, but it is not yet runnable as a causal savings model.

F02 remains proposed only; no Dongjiakou ultrasound/cavitation receipt was found.

Resource recovery and OAE continue to receive zero Dongjiakou credit until node-specific yield, input-energy and ecology receipts exist.

## Best next receipts

The highest-value documents are now even more specific:

```text
1. Dongjiakou 2026 electricity bill / retail settlement
2. DCS annual whole-site kWh + product m3
3. 2025/2026 feed-flow and product-flow historian export
4. brine laboratory sheet from the reported daily manual tests
5. CIP event log: date, trigger, chemistry, duration, before/after normalized flux and DP
6. raw 2017/2022 OUC monitoring reports and current discharge permit
7. hydraulic profile / PRV schedule / pump duty points
```

### Keeper

**A search that returns UNKNOWN is still an experiment with a result.**
