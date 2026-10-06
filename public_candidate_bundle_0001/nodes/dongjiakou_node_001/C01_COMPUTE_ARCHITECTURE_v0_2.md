# Dongjiakou C01 — Regenerative Compute Module v0.2

Status: PROPOSED ARCHITECTURE + EXECUTED PARAMETRIC SIMULATION. No net-positive claim.

## Core finding

Compute is an electrical load. It earns its place only through measured plant service, regional service, useful heat, flexibility, resilience, or verified efficiency gains.

The 2025 UF+RO process baseline is 39.446 GWh/year. Existing S01 rooftop PV is 2.706-2.918 GWh/year.

Run 3 v0.2 separates IT load from facility load:

```text
E_IT       = P_IT * 8760 * L
E_facility = E_IT * PUE
```

`L` and Node-001 PUE are not yet measured. A PUE=1.25 case is included only as a sector/policy reference because Chinese 2025 green-compute reporting and policy use 1.25 as an important benchmark.

## Facility energy at the PUE=1.25 reference

```text
100 kW IT  -> 1.095 GWh/y facility -> 2.78% of 2025 UF+RO energy
250 kW IT  -> 2.738 GWh/y facility -> 6.94%
500 kW IT  -> 5.475 GWh/y facility -> 13.88%
1 MW IT    -> 10.950 GWh/y facility -> 27.76%
```

These are full-load reference cases, not forecasts.

## Solar coupling

Existing S01 PV may not be credited twice.

```text
PV_credit_compute + PV_credit_desalination <= measured PV generation
```

At the PUE=1.25 reference and L=1:

```text
100 kW facility: PV annual energy / compute facility energy = 247-266%
250 kW facility:                                                99-107%
500 kW facility:                                                49-53%
1 MW facility:                                                  25-27%
```

The 250 kW result is notable: its annual facility-energy magnitude is close to modeled annual rooftop-PV generation. This is not a self-powered claim. Hourly overlap, storage, curtailment and plant priority remain unknown.

Existing S01 PV is already a node asset. Routing it to compute changes attribution, not total node generation.

## Thermal coupling

Nearly all IT electrical energy ultimately appears as heat, but useful heat is constrained by capture, temperature grade and timing.

```text
Q_useful <= E_IT * f_capture * f_temperature_match * f_temporal_match
```

The 2026 Dongjiakou chemical-cleaning heat-pump procurement is a credible candidate sink, but the public notice does not expose CIP setpoint temperature, thermal duty, COP map or schedule.

Therefore:

```text
useful heat credit = 0
heat-pump electricity saving = 0
```

until those receipts exist.

Thermal GWh is never added directly to electrical savings. Only measured avoided heat-pump electricity or another verified displacement earns electrical credit.

## Water boundary

ORCS INV-19 Water Cohesion remains a veto: no compute module may claim net-positive status if downstream water quality deteriorates.

Node-001 compute WUE and cooling-water source are UNKNOWN. The preferred design path is closed-loop liquid cooling with minimal water consumption and no default use of potable/desalinated product water, but that remains PROPOSED until engineered.

## Operations architecture

### Ring A — physical control

Existing PLC/SCADA, hard interlocks and approved deterministic control remain authoritative.

### Ring B — deterministic analytics

Time-series forecasting, optimization, alarms, mass/energy balance and constraint checks should use conventional statistical/optimization methods where they are sufficient. An LLM is not used merely because one is available.

### Ring C — AI advisory fabric

Proposed model roles:

```text
PRIMARY ELIGIBLE LOCAL ADVISORY FAMILY
DeepSeek
- DeepSeek-V4.1-Flash reference for efficient/high-volume advisory work
- DeepSeek-V4-Pro reference for harder engineering reasoning

LOCAL CHALLENGER / FAILOVER
Qwen3
- local open-weight Qwen3 checkpoint chosen by hardware + energy benchmark
- hosted Qwen3.8 may be an optional policy-permitted lane

OPTIONAL EXTERNAL ADVERSARIAL AUDIT
OpenAI GPT
- current reference: GPT-5.6 Sol
- redacted/aggregated data by default
- never a plant-continuity dependency
```

Exact model versions are deployment-manifest state, not constitutional dependencies.

### Ring D — human approval

```text
model recommendation
  -> deterministic constraint validator
  -> operator review/approval
  -> PLC/SCADA execution
```

LLM actuator authority is NONE.

Cross-model agreement is not evidence. Disagreement escalates; agreement still requires plant constraints, operator approval and measured outcomes.

## Vendor diversity

ORCS INV-7 / INV-7c limits a single vendor to 47% of capability-weighted routing volume.

`DeepSeek primary` therefore means default first eligible advisory family / plurality, not monopoly share. Qwen and an approved independent third lane provide failover and cross-validation where policy permits.

Exact routing shares are measured, not preassigned.

## OT / cybersecurity boundary

- AI has no OT write credentials.
- AI consumes a read-only telemetry replica or approved broker.
- Raw OT data egress is denied by default.
- Credentials never enter model context.
- External model calls are policy-gated and logged.
- Compute/advisory failure must not stop the desalination plant.
- Model/routing updates require signed manifest, canary test, rollback path and operator change control.

## Workload hierarchy

Plant-critical advisory workloads are prioritized:

1. anomaly triage and root-cause support
2. membrane/fouling forecasting
3. predictive maintenance and procurement/event ledger
4. energy/PV/load forecasting
5. brine-routing and resource-recovery simulation
6. ecological telemetry QA and provenance
7. operator documentation/translation

Spare capacity may serve regional workloads only after plant obligations are satisfied: marine science, university research, coastal modeling, emergency/resilience analysis and approved regional inference.

## Pay-rent metrics

Before expansion, measure:

```text
PUE / WUE / CUE with explicit boundary
IT kWh by workload
energy per correct task
latency and uptime
false-negative rate on anomaly tasks
validated recommendations
operator time saved
avoided unplanned downtime if causally demonstrated
verified process kWh saved
verified chemical reduction
verified membrane-life extension
useful heat delivered at measured temperature
heat-pump kWh actually displaced
hourly PV overlap / verified curtailment captured
regional compute-hours delivered
training / research access receipts
downstream water-quality status
```

No metric receives a value before measurement.

## Scale gates

**Pilot A — 100 kW IT.** First commissioning tier. Establish PUE/WUE, workload-energy measurements, routing logs, failover, thermal telemetry and plant-service value.

**Pilot B — 250 kW IT.** Earned expansion. Interesting because facility energy at the 1.25 reference (~2.738 GWh/y) is close to S01 annual PV output, but hourly matching must be measured.

**500 kW / 1 MW.** Do not deploy merely because rack capacity exists. Require proven service value, acceptable water/ecology, verified energy strategy and thermal/flexibility benefit.

## Net-electric gate

```text
new incremental clean generation
+ verified plant electrical savings
+ verified heat-pump electrical savings
- compute facility electricity
>= 0
```

Existing S01 PV is not `new incremental clean generation` for C01 unless the comparison baseline explicitly excludes it.

## Keeper

**Compute must pay rent in measured service, recovered heat, flexibility, resilience, or verified efficiency—not in promises.**