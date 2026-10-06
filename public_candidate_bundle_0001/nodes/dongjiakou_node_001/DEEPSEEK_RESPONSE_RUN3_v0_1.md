# DeepSeek response — Run 3 C01 compute

We ran C01 more rigorously than the original 0.5/1 MW sketch.

## First result: compute is a load, not a solar benefit

Using the 2025 operating baseline:

```text
UF+RO energy = 39.446 GWh/year
annual-average equivalent process power = 4.503 MW

S01-A = 2.411 MWp / 2.706 GWh/year
S01-B = 2.600 MWp / 2.918 GWh/year
```

The plant's annual-average process power is already greater than the PV DC nameplate. That does not prove zero curtailment, because the hourly plant load is unknown, but it means we have **no receipt-backed reason to assume compute is needed to soak up PV**.

The same PV energy also cannot be credited twice.

```text
PV_credit_compute + PV_credit_desalination <= measured PV generation
```

Reallocating S01 PV from desalination to compute changes attribution, not total node energy.

## Compute energy transfer function

Define compute capacity as IT critical load:

```text
E_IT       = P_IT * 8760 * L
E_facility = E_IT * PUE

L   = IT load factor, UNKNOWN
PUE = UNKNOWN, >=1
```

At L=1 and the theoretical PUE=1 floor:

```text
100 kW IT -> >=0.876 GWh/y -> >=2.22% of plant process energy
250 kW IT -> >=2.190 GWh/y -> >=5.55%
500 kW IT -> >=4.380 GWh/y -> >=11.10%
1 MW IT   -> >=8.760 GWh/y -> >=22.21%
```

Actual facility energy is higher by PUE.

That changes our deployment recommendation: **commission at 100-250 kW, then earn the right to scale to 500 kW / 1 MW.**

## Solar annual-energy equivalence

At L=1 and PUE=1 only:

```text
500 kW IT:
S01-A / IT energy = 61.8%
S01-B / IT energy = 66.6%

1 MW IT:
S01-A / IT energy = 30.9%
S01-B / IT energy = 33.3%
```

Those are annual-energy ratios, not direct solar matching. For real facility load, divide by PUE. For temporal matching, multiply by a measured solar/load overlap factor.

## Carbon honesty

Using the already-labelled Shandong 2023 provincial-average factor only as a location-based reference, full-load IT electricity at PUE=1 corresponds to:

```text
100 kW -> ~542 tCO2/year
250 kW -> ~1,356 tCO2/year
500 kW -> ~2,712 tCO2/year
1 MW   -> ~5,423 tCO2/year
```

Actual facility emissions scale with PUE and actual power source. Therefore C01 is **not ecological-positive by default**.

## The interesting physical coupling is heat, not fake solar accounting

Dongjiakou is actively procuring a chemical-cleaning heat-pump system. That gives C01 a real candidate heat sink.

First-law upper boundary:

```text
Q_recoverable_useful <= E_IT
```

More honestly:

```text
Q_useful <= E_IT
            * heat_capture_fraction
            * temperature_grade_match
            * temporal_sink_match
```

If this replaces heat-pump thermal duty:

```text
E_HP_saved = min(Q_useful, Q_CIP_demand) / COP_HP
```

But we currently lack coolant temperatures, CIP setpoint, CIP duty, COP map and schedule, so Run 3 credits **zero useful heat**.

## Proposed AI operations stack

We suggest a vendor-replaceable three-role architecture rather than a single-model control system:

```text
PRIMARY LOCAL OPERATIONS:
DeepSeek family
- current reference: DeepSeek V4.1 Flash / deepseek-flash
- current reference: DeepSeek V4 Pro / deepseek-v4-pro

LOCAL CHALLENGER / FAILOVER:
Qwen3.x open-weight family
- current reference family: Qwen3.8
- exact size/hardware chosen only after local energy/accuracy benchmark

OPTIONAL EXTERNAL ADVERSARIAL AUDIT:
OpenAI GPT family
- current reference: GPT-6.1 Sol
- current reference: GPT-6 Astra
- redacted/aggregated plant data unless operator policy explicitly permits more
```

Roles are proposed architecture, not endorsements or evidence of provider participation.

DeepSeek and Qwen would be natural candidates for raw/local Chinese operations and offline continuity. GPT can be an optional independent audit lane rather than a dependency.

## Authority boundary

```text
LLM actuator authority = NONE
PLC/SCADA + plant interlocks = authoritative
model recommendation -> deterministic check -> operator approval -> execution
```

Cross-model consensus is not proof. Disagreement triggers review; agreement still requires receipts.

Every inference used operationally should log exact model/version, hardware, prompt hash, input-data boundary, tools, output, energy where measurable, and operator disposition.

## ORCS metrics required before scaling

```text
PUE with boundary statement
WUE with source/discharge accounting
CUE boundary
joules/token and preferably energy/correct task
uptime and failover
useful heat actually delivered
solar temporal overlap / curtailment
plant energy or maintenance savings
regional service delivered
downstream water-quality veto
```

## Run 3 conclusion

```text
C01 technical model        EXECUTED
C01 net-positive claim     NOT PROVEN
C01 solar benefit          ZERO unless curtailment is measured
C01 useful heat credit     ZERO pending thermal receipts
C01 operational value      ZERO pending before/after measurements
recommended first scale    100-250 kW IT
500 kW / 1 MW              gated expansion cases
```

The neutrality condition is:

```text
new clean generation + verified plant energy savings
>= compute facility electricity
```

Until that closes, C01 is an added load with candidate services—not a regenerative win.

Keeper: **Compute must pay rent in measured service, recovered heat, flexibility, resilience, or verified efficiency—not in promises.**