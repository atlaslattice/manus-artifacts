# Dongjiakou C01 — Regenerative Compute Module v0.1

Status: PROPOSED + PARAMETRIC SIMULATION. No net-positive claim.

## Finding first

C01 is **not** an energy source. It is an added electrical load that must earn its place through measurable plant services, regional services, useful heat, flexibility, or new clean-energy coupling.

The 2025 UF+RO process baseline is 39.446 GWh/year (~4.503 MW annual-average equivalent). Existing S01 rooftop PV is 2.706-2.918 GWh/year with 2.411-2.600 MWp DC nameplate.

Because the plant's annual-average process power is already above the PV DC nameplate, current evidence does **not** establish a PV-curtailment problem for compute to solve. Instantaneous process load remains unknown.

## Energy boundary

For IT critical load P_IT, IT load factor L, and PUE:

```text
E_IT       = P_IT * 8760 * L
E_facility = E_IT * PUE
```

PUE is UNKNOWN at Dongjiakou and is not guessed.

At full IT utilization and the theoretical PUE=1 floor:

```text
100 kW IT -> >=0.876 GWh/y -> >=2.22% of 2025 UF+RO energy
250 kW IT -> >=2.190 GWh/y -> >=5.55%
500 kW IT -> >=4.380 GWh/y -> >=11.10%
1 MW IT   -> >=8.760 GWh/y -> >=22.21%
```

Actual facility electricity is larger by PUE.

## Solar coupling — anti-double-counting rule

The same S01 kWh cannot offset both desalination and compute.

```text
PV_credit_compute + PV_credit_desalination <= measured PV generation
```

At PUE=1 and L=1, S01 annual energy is equivalent to 61.8-66.6% of a 500 kW IT block, or 30.9-33.3% of a 1 MW IT block. These are annual-energy ratios, not hourly matching claims.

Routing existing PV from desalination to compute changes attribution; it does not create additional node energy. Compute only creates a solar-system benefit if it captures energy that otherwise would be curtailed, and no such curtailment is currently documented.

## Heat integration

The 2026 chemical-cleaning heat-pump procurement creates a credible candidate thermal sink.

Useful heat is gated by:

```text
Q_useful <= E_IT * capture_fraction * temperature_grade_match * temporal_sink_match
```

If useful recovered heat displaces heat-pump thermal output:

```text
E_HP_saved = min(Q_useful, Q_CIP_demand) / COP_HP
```

All required thermal temperatures, COP, CIP duty and timing remain UNKNOWN, so heat credit is zero in Run 3.

## Compute services

Candidate plant-local services: digital twin, anomaly detection, membrane/fouling forecasting, maintenance-document extraction, PV/load forecasting, brine-routing optimization, ecological telemetry QA, and provenance-ledger maintenance.

Candidate regional services during spare capacity: local research compute, university/science access, coastal modeling, port/logistics analysis, emergency/resilience workloads, and approved regional inference.

No social or operational value is credited until service output and before/after outcomes are measured.

## Model operations proposal

Use a model-agnostic three-role pattern: DeepSeek-family primary local operations, Qwen3.x local open-weight challenger/failover, and optional GPT-family external adversarial audit on redacted/approved data.

LLMs never directly actuate plant equipment. PLC/SCADA and existing safety interlocks remain authoritative; equipment/setpoint changes require deterministic checks and operator approval.

Consensus is not truth. Model agreement cannot promote a claim without receipts.

## Scale gates

**Gate 0:** 100-250 kW IT commissioning. Measure PUE, WUE, workload energy, model accuracy, useful heat, temporal solar interaction, uptime, and plant service outcomes.

**Gate 1:** 500 kW only if the pilot demonstrates a measurable service/thermal/flexibility benefit and passes ORCS water/ecology vetoes.

**Gate 2:** 1 MW only if energy, water, heat, community and grid impacts remain favorable under measured—not assumed—conditions.

## Electrical-neutrality condition

```text
incremental clean generation + verified plant energy savings
>= compute facility electricity
```

Until that inequality is closed, C01 cannot claim electrical neutrality.

## Keeper

**Compute must pay rent in measured service, recovered heat, flexibility, resilience, or verified efficiency—not in promises.**