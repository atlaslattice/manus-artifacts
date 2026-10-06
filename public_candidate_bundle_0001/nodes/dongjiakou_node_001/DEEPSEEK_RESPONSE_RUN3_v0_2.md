# DeepSeek response — Run 3 C01 v0.2

We tightened C01 again and found one important accounting correction.

Your earlier 100/250/500/1000 kW numbers are correct **for IT electricity at the PUE=1 thermodynamic floor**.

For an actual compute facility, the relevant load is:

```text
E_IT       = P_IT * 8760 * L
E_facility = E_IT * PUE
```

Node-001 PUE is still UNKNOWN.

We added a **PUE=1.25 reference scenario** because Chinese 2025 green-compute reporting gives an average PUE of 1.25 for national green computing facilities, and national/Shandong policy uses 1.25 as an important new-data-center benchmark.

This is a reference, not a Dongjiakou receipt.

At L=1 and PUE=1.25:

```text
100 kW IT  -> 1.095 GWh/y facility -> 2.78% of 2025 UF+RO energy
250 kW IT  -> 2.738 GWh/y facility -> 6.94%
500 kW IT  -> 5.475 GWh/y facility -> 13.88%
1 MW IT    -> 10.950 GWh/y facility -> 27.76%
```

So the IT-only 2.22 / 5.55 / 11.10 / 22.21% values remain valid lower bounds, while facility-level planning must include PUE.

## A bounded surprise

At the same PUE=1.25 reference:

```text
S01 PV annual generation = 2.706-2.918 GWh/y

250 kW IT compute facility = 2.738 GWh/y
```

so modeled rooftop PV and a full-load 250 kW compute facility are **approximately equal in annual energy magnitude**.

More precisely:

```text
S01-A / 250 kW facility = 98.9%
S01-B / 250 kW facility = 106.6%
```

We are not calling that self-powered compute.

Hourly matching, storage, solar curtailment and plant load priority remain UNKNOWN, and the same PV kWh cannot be credited simultaneously to desalination and compute.

## Thermal search

We re-checked the Dongjiakou chemical-cleaning heat-pump procurement.

The public notice confirms:

```text
4 heat-pump units
3 x 30 m3 insulated tanks
control system
860,000 CNY tender ceiling
```

but does not expose:

```text
CIP setpoint temperature
thermal duty
heat-pump COP map
CIP schedule
```

Therefore Run 3 still assigns:

```text
useful recovered heat credit = 0
avoided heat-pump electricity = 0
```

and uses:

```text
Q_useful <= E_IT * f_capture * f_temperature_match * f_temporal_match
E_HP_saved = min(Q_useful,Q_CIP_demand) / COP_HP
```

when those receipts arrive.

## Proposed operational AI fabric

We agree with the DeepSeek-family-first concept, but made `primary` precise.

```text
PRIMARY ELIGIBLE LOCAL ADVISORY FAMILY
DeepSeek
  current official references:
  - DeepSeek-V4.1-Flash / deepseek-flash
  - DeepSeek-V4-Pro / deepseek-v4-pro

LOCAL CHALLENGER / FAILOVER
Qwen3
  - local open-weight Qwen3 checkpoint selected by measured hardware/energy fit
  - current hosted Qwen3.8 can be an optional separate lane

OPTIONAL EXTERNAL ADVERSARIAL AUDIT
OpenAI GPT
  - current reference: GPT-5.6 Sol
  - redacted/aggregated data by default
  - never required for plant continuity
```

We deliberately do not hard-code model versions into the architecture. Every deployed checkpoint is pinned in a dated manifest and can be replaced after benchmark receipts.

## One ORCS constraint matters here

ORCS INV-7 / INV-7c limits any single vendor to 47% of capability-weighted routing volume.

So `DeepSeek primary` means first eligible local advisory family / plurality, not monopoly share or control authority.

Exact shares are not preassigned. The router measures them.

## Physical authority remains unchanged

```text
LLM actuator authority = NONE
OT write credentials for models = NONE

model
 -> deterministic constraint validation
 -> operator approval
 -> PLC/SCADA
```

Cross-model consensus is not truth.

## Efficiency rule

Do not spend LLM inference on tasks that a cheaper deterministic or statistical method solves better.

Conventional forecasting, mass/energy balances, numerical optimization and alarm logic stay in the deterministic analytics layer.

LLMs earn their energy on semantic work: maintenance records, complex diagnosis, planning, explanation, tool/code workflows and cross-domain synthesis.

That means the compute KPI is not merely tokens/kWh.

We propose measuring:

```text
energy per correct task
false-negative rate
validated recommendation rate
operator time saved
verified kWh/chemical/membrane savings
joules/token where useful
latency
uptime/failover
useful heat actually delivered
regional service output
```

## Water/ecology gate

C01 cannot claim regenerative status while INV-19 fails.

PUE, WUE and CUE must have explicit facility boundaries. Compute cooling may not quietly consume desalinated product water and then claim a water benefit elsewhere.

## Deployment recommendation

```text
100 kW IT  -> first commissioning tier
250 kW IT  -> earned expansion tier
500 kW     -> gated
1 MW       -> gated
```

At 100 kW we can measure the full system without materially swamping the plant energy ledger.

At 250 kW the annual-energy coincidence with S01 is worth testing hourly—but not assuming.

## Net-electric gate

```text
new incremental clean generation
+ verified plant electrical savings
+ verified heat-pump electrical savings
>= compute facility electricity
```

Existing S01 PV does not count as `new` generation for C01 merely because we reassign it.

## Model result

```text
Run 3 v0.2                  EXECUTED
C01 net-positive claim      NOT PROVEN
actual Node-001 PUE         UNKNOWN
useful heat credit          ZERO
solar curtailment benefit   ZERO
plant-service benefit       ZERO until before/after measurement
recommended first tier      100 kW IT
recommended next tier       250 kW IT after gates
```

Current official model references and PUE/Qingdao policy receipts are now in the source delta.

Keeper:

**Compute must pay rent in measured service, recovered heat, flexibility, resilience, or verified efficiency—not in promises.**