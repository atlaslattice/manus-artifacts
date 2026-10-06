# Dongjiakou Node-001 — Run 3 v0.2 Test Receipt

Date: 2026-10-06

Status: EXECUTED PARAMETRIC TECHNICAL SENSITIVITY / NON-CANON

## Improvements over v0.1

- separates IT energy from facility energy via PUE
- adds PUE=1.25 sector/policy reference without pretending it is Node-001 measured PUE
- adds 100/250/500/1000 kW facility-level energy and carbon transfer values
- preserves solar anti-double-counting
- keeps useful heat credit at zero pending thermal receipts
- corrects dated model references
- adds DeepSeek/Qwen/GPT vendor-replaceable advisory routing
- adds ORCS INV-7/INV-7c provider diversity and INV-19 water veto
- keeps all LLMs outside physical actuator authority

## Key result

At full load and PUE=1.25 reference:

```text
100 kW  -> 1.095 GWh/y
250 kW  -> 2.738 GWh/y
500 kW  -> 5.475 GWh/y
1 MW    -> 10.950 GWh/y
```

The 250 kW annual facility-energy magnitude is near the S01 annual PV result (2.706-2.918 GWh/y), but this is not hourly matching, not self-sufficiency, and not permission to double-count PV.

## Zero-credit fields

```text
useful heat benefit            0
plant energy savings from AI   0
maintenance savings from AI    0
PV curtailment reduction       0
social/economic value          0
```

until measured.

## Authority

```text
LLM actuator authority = NONE
model -> deterministic validator -> operator -> PLC/SCADA
```