# DeepSeek response — U/Tariff search + Run 0.2 + Run 1

## We found U

A Qingdao 2026 public report states Dongjiakou supplied **17.93 million m3 in 2025** against a 100,000 m3/day design capacity.

Therefore:

```text
U_2025 = 17.93M / 36.5M = 0.4912328767
       = 49.12%
```

This upgrades Node-001 from nameplate-only to a dated operating-volume calibration.

The same Qingdao government record reports **12.62 million m3 in 2020**, corresponding to a derived U_2020 of 34.58%.

That temporal change reinforces the rule that utilization is a dated node state, not a timeless plant constant.

## Tariff search result

We found a **Dongjiakou-specific historical electricity tariff**:

```text
2018-01-01 through 2020-12-31
0.555 CNY/kWh including tax
```

confirmed in both national seawater-utilization reporting and Qingdao government material.

We did **not** find a defensible plant-specific 2026 effective tariff, bill, retail contract or market-settlement receipt.

Therefore:

```text
historical_tariff = REPORTED
current_tariff    = UNKNOWN
```

Do not substitute a generic Shandong industrial tariff.

## Run 0.2 — 2025 operating-volume baseline

```text
reported 2025 product supply      17.93M m3
derived utilization U             49.12%
UF+RO process-train SEC           2.2 kWh/m3
derived UF+RO electricity         39.446 GWh/year
chemical cost                     <2.6895M CNY/year
```

Recovery-range mass sensitivity:

```text
45% recovery:
annual feed             39.844M m3
annual product          17.930M m3
annual reject-equivalent 21.914M m3

50% recovery:
annual feed             35.860M m3
annual product          17.930M m3
annual reject-equivalent 17.930M m3
```

Recovery remains a technology/application range, not measured 2025 recovery.

## Run 1 — rooftop solar

Workshop footprint receipt:

```text
17,474.32 m2
```

We model only 60% as effective active-module area:

```text
10,484.592 m2
```

Local Qingdao rooftop reference:

```text
12.4956 MWp
14,022.86 MWh/year
derived yield = 1,122.224 kWh/kWp-year
```

### S01-A — conservative 23%

```text
2.411 MWp
2.706 GWh/year
6.86% of 2025 UF+RO process-train electricity
```

### S01-B — 24.8% Sea-Shield class

```text
2.600 MWp
2.918 GWh/year
7.40% of 2025 UF+RO process-train electricity
```

Current avoided electricity cost remains UNKNOWN because current tariff remains UNKNOWN.

For historical context only, applying the old 0.555 CNY/kWh tariff would imply about 1.50-1.62M CNY/year avoided electricity cost. This is **not** promoted as 2026 economics.

## Carbon gap also narrowed

The latest official provincial electricity-average factor located is Shandong 2023:

```text
0.6191 kg CO2/kWh
```

As a location-based reference only, Run 1 corresponds to roughly:

```text
S01-A  ~1,675 tCO2/year
S01-B  ~1,807 tCO2/year
```

This is not a 2026 marginal grid factor and not lifecycle PV carbon accounting.

## Highest-value remaining receipts

```text
2026 plant-specific effective electricity tariff
whole-site SEC
current measured recovery
current feed/reject/discharge map
current brine chemistry
CIP/fouling chronology
primary ecological monitoring
unused hydraulic head
roof structural load/interconnection
```

## Next rule

The next module must be evaluated against the **2025 operating-volume baseline**, not U=1 nameplate.

Solar survives as a technical improvement at the current evidence boundary.

Mini-hydro remains zero until unused head is found.

Resource-recovery lanes remain zero until yield + energy + ecology receipts exist.

Potential reductions in terrestrial lithium or uranium mining are treated as future displacement hypotheses, not present benefits.
