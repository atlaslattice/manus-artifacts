# SolBrain Hydration — Current / Past / Planned Work
## 2026-10-06 continuity packet

```text
STATUS: REHYDRATION SUMMARY — NON-CANON INDEX
PURPOSE: Restore the latest receipt-grounded working state after a thread reset.
AUTHORITY: NONE
BACKGROUND_RUNTIME: NONE
MODEL_CONTINUITY_CLAIM: NONE
LATEST_REPO_HEAD_AT_WRITE: c6f6dc732c05bdd7c6313d56251b940a27afcb11
PRIMARY_WORKSTREAM: Alexandrian Seawater Refinery / Dongjiakou Node-001
STUDY_CLASSIFICATION: TECHNICAL FEASIBILITY + CONDITIONAL ECONOMICS
```

This file is a repo continuity scaffold, not native model memory. Rehydrate from receipts, not recollection.

## 1. Standing epistemic rules

```text
Unknown stays UNKNOWN.
Raw stays recoverable.
Null results are receipts.
A search that returns UNKNOWN is still an experiment with a result.
Cross-model agreement is not evidence.
The baseline gets to win.
No module receives benefit before measurement.
No energy or material stream may be double-counted.
A module with an unknown site parameter returns a transfer function, not a fictional point estimate.
Never let a plant have one timeless value when the plant itself keeps evolving.
Verified baseline -> one module at a time -> measure interaction -> stack only survivors.
```

Use explicit evidence labels: MEASURED / REPORTED / DERIVED / MODELED / PROPOSED / UNKNOWN.

## 2. Earlier foundation — PT2 / physics / provenance

Core architecture:

```text
H##.S##.N## = Atlas entry coordinate
(Z,N,q,...) = typed physics profile attached to an HSN address
co-indexing != physical coupling
```

Primary artifacts:

```text
public_candidate_bundle_0001/schemas/source_record_v0.1.json
public_candidate_bundle_0001/schemas/physics_profile_v0.1.1.json
public_candidate_bundle_0001/docs/SOURCE_PER_FIELD_POLICY_v0.1.md
public_candidate_bundle_0001/docs/PHYSICS_PROFILE_BLIND_BENCHMARK_v0.1.md
public_candidate_bundle_0001/docs/PHYSICS_INGESTION_PIPELINE_v0.1.md
archive/status/PHYSICS_CONTRACT_FIXTURE_TEST_RECEIPT_2026-10-05.md
archive/status/DELTA_LOG_2026-10-05_PT2_PHYSICS_FOUNDATION_CLOSEOUT.md
```

Hard-science lesson carried forward:

> one real object -> one immutable source chain -> one normalization path -> one validation -> one commit

That became:

> one real plant -> one complete provenance chain -> one validated simulation floor -> one retrofit at a time

## 3. Deuteron baseline -> ionic-energy reframing

The original deuteron-spin question was forced to beat a conventional spin-1 Zeeman/ergotropy baseline before any breakthrough claim.

At 1 T / 300 K:

```text
thermal ergotropy = 0
equal coherent ideal state ~0.002608 J/mol
full inversion ceiling ~0.005216 J/mol
```

Keeper: Do not simulate the breakthrough into existence. Make the hypothesis beat the baseline.

The target broadened to ionic energy:

```text
ion != fuel
useful energy comes from non-equilibrium state differences:
electrochemical potential
concentration
redox
charge separation
humidity
pressure / flow
externally prepared state
```

Design objective:

> Do not hunt for the ion with the most energy. Hunt for the cheapest repeatable and circular path between useful states with a recoverable free-energy difference.

Primary engine:

```text
public_candidate_bundle_0001/simulations/ionic_energy_state_engine_v0_1/
```

## 4. Year-1 closed-loop engine

Core relationship:

```text
annual makeup ~ inventory * cycles/year * (1-retention)
```

Important retention thresholds:

```text
1e6 cycles/year -> <=1 turnover/year requires ~99.9999% retention/cycle
1e9 cycles/year -> <=1 turnover/year requires ~99.9999999% retention/cycle
```

Cycle 100 can be cheaper than cycle 1 because CAPEX / first-fill are amortized, not because chemistry magically gets cheaper.

Artifacts:

```text
public_candidate_bundle_0001/simulations/ionic_energy_state_engine_v0_1/year1_closed_loop_deployment_v0_1.py
public_candidate_bundle_0001/simulations/ionic_energy_state_engine_v0_1/YEAR1_CLOSED_LOOP_TEST_RECEIPT_2026-10-06.md
```

## 5. Alexandrian Seawater Refinery — network concept

Primary white paper:

```text
public_candidate_bundle_0001/whitepapers/ALEXANDRIAN_SEAWATER_REFINERY_167_NODE_SIMULATION_v0_1.md
```

Core distinction:

> Products are not power. Gradients are power.

The 167-project / 3.077M m3/day Chinese desalination figure is a host-infrastructure baseline, not proof that all 167 are Atlas nodes or resource-extraction retrofits.

Architecture lanes:

```text
desalinated water
pressure / salinity-gradient recovery
bulk mineral recovery
trace-resource recovery
H/D lane
Mg/Ca routing
pollution interception
OAE / carbon-removal research
brine / residual-water handling
data / compute / regional service
```

Resource inventory != recovery yield.

Potential reduction of terrestrial lithium or uranium mining remains a POTENTIAL_DISPLACEMENT_HYPOTHESIS until yield, selectivity, energy, reagents, material life, markets, economics and ecology close.

ORCS rule: no facility may claim net positive while downstream water quality deteriorates.

## 6. Dongjiakou Node-001 — source chain and baseline

Primary directory:

```text
public_candidate_bundle_0001/nodes/dongjiakou_node_001/
```

Source-chain milestone:

```text
a720868558dec4a948aa96c9ec87ac404dc23ae1
Add Dongjiakou Node-001 source record chain
```

Core reported plant values:

```text
product capacity                    100,000 m3/day
process                             UF + RO
original project CAPEX              450M CNY
UF+RO process-train SEC             ~2.2 kWh/m3
chemical cost                       <0.15 CNY/m3
technology/application recovery     45-50%
ERD efficiency statement            >96%
```

Boundary discipline:

```text
2.2 kWh/m3 = UF+RO process-train receipt
current whole-site SEC = UNKNOWN
45-50% = technology/application range
current measured recovery = UNKNOWN
```

Maintenance event ledger:

```text
2023/24 combined UF+RO procurement: 6.850218M CNY; allocation UNKNOWN
2025 first-stage RO: 1,638 elements; 5.162976M CNY contract
2025/26 UF: 2,448 elements; 15.912M CNY tender ceiling
2026 first-stage RO: 4,914 elements; 15.3813114M CNY award incl tax
```

Do not turn those events into an invented fixed membrane lifetime or blindly add parent + child project budgets.

## 7. Run 0 — verified nameplate floor

Commit:

```text
7bc7d5c9a2a58a9a149372b7bde0bafaac0fbd52
```

With utilization U left unknown:

```text
annual product       = 36.5M * U m3/year
UF+RO electricity    = 80.3 * U GWh/year
chemical cost        <5.475M * U CNY/year
```

Mass balance:

```text
45% recovery -> feed 222,222.22 / reject-equivalent 122,222.22 m3/day
50% recovery -> feed 200,000.00 / reject-equivalent 100,000.00 m3/day
```

Run 0 assigns zero benefit to all retrofit modules.

## 8. Run 0.2 — dated operating baseline

Commit:

```text
63f7d04f3446b03f0a99709a584c66d02d435689
```

Dated utilization series:

```text
2020 U ~34.58%
2021 U ~33.40%
2025 U ~49.12%
```

Do not infer why utilization changed without a receipt.

2025 operating-volume baseline:

```text
product                     17.93M m3/year
UF+RO process electricity   39.446 GWh/year
chemical cost               <2.6895M CNY/year
```

Recovery-range sensitivity:

```text
45% -> feed 39.844M / reject-equivalent 21.914M m3/year
50% -> feed 35.860M / reject-equivalent 17.930M m3/year
```

## 9. Tariff / economics status

```text
2018-2020 plant-specific preferential tariff = 0.555 CNY/kWh incl tax
2026 effective Dongjiakou settlement = UNKNOWN
```

Shandong support through end-2025 includes demand/capacity-charge and electricity-market policy context. Do not substitute a generic provincial rate.

Qingdao 2025 municipal seawater-desalination operating subsidy budget is 188M CNY city-wide; no Dongjiakou allocation is inferred.

Study label remains:

```text
TECHNICAL FEASIBILITY + CONDITIONAL ECONOMICS
```

## 10. Run 1 — rooftop solar

Inputs:

```text
workshop footprint                  17,474.32 m2
modeled active coverage             60%
active module area                  10,484.592 m2
local Qingdao yield                 ~1,122.224 kWh/kWp-year
```

Results:

```text
S01-A 23%: 2.411 MWp -> 2.706 GWh/year -> 6.86% of 2025 UF+RO electricity
S01-B 24.8% coastal class: 2.600 MWp -> 2.918 GWh/year -> 7.40%
```

The jump from ~3.5% against U=1 nameplate to ~7% against actual 2025 output came from fixing the denominator, not changing solar generation.

Current CNY savings remain UNKNOWN because the current tariff is UNKNOWN.

## 11. Fouling / cleaning / ecology receipts

Receipt-search commits:

```text
2ef710ebab2a6195ec5cf3fd3748a1806b8ae2ee
e69d85f58f72be7ed67522edd9df87232492e77d
```

2026 modernization receipts:

```text
chemical-cleaning heat-pump system:
  4 heat-pump units
  3 x 30 m3 insulated tanks
  control system
  tender ceiling 860,000 CNY

self-cleaning pretreatment:
  10 customized filters
  maximum tender price 2.6M CNY
```

F01 must therefore beat a modernizing baseline, not untreated conventional RO.

Still missing:

```text
CIP frequency
CIP chemistry / dose
foulant species
normalized flux / differential-pressure history
before/after CIP performance
membrane operating hours / failure cause
```

Historical ecology provenance improved, including daily concentrate testing reports and OUC 2017/2022 follow-up summaries, but raw station-level data remain missing.

## 12. Run 2 — H01 unused-head hydro

Commit:

```text
e69d85f58f72be7ed67522edd9df87232492e77d
```

Hydraulic search found:

```text
historical intake ~1.7 km DN1600
seawater gravity-flows into intake-pump suction pool
5 SWRO high-pressure pumps
920 m3/h each
2100 kW motors each
~400-630 m process head
```

The 400-630 m is motor-supplied RO process pressure inside the RO/ERD loop and is NOT H01 opportunity.

No public disposable-head receipt was found.

```text
H_available = UNKNOWN
site hydro credit = 0
```

Run 2 transfer function at eta=0.8 using 2025 product volume:

```text
1 m  -> 0.0391 GWh/y -> 0.099% of process energy
5 m  -> 0.1954 GWh/y -> 0.495%
10 m -> 0.3907 GWh/y -> 0.991%
20 m -> 0.7815 GWh/y -> 1.981%
50 m -> 1.9537 GWh/y -> 4.953%
```

Keeper: A module with an unknown site parameter should return a transfer function, not a fictional point estimate.

## 13. Run 3 — C01 regenerative compute

Initial execution:

```text
1cdfd81fbc8b00acd70a62d1bc955bd781c30a57
Execute Dongjiakou C01 regenerative compute module
```

Hardened current commit / repo head:

```text
c6f6dc732c05bdd7c6313d56251b940a27afcb11
Harden Dongjiakou C01 compute module and model routing
```

Current v0.2 artifacts:

```text
C01_COMPUTE_ARCHITECTURE_v0_2.md
C01_MODEL_ROUTING_POLICY_v0_2.json
C01_MODEL_SOURCE_SNAPSHOT_v0_2.json
RUN_3_COMPUTE_v0_2.json
RUN_3_TEST_RECEIPT_2026-10-06_v0_2.md
SOURCE_RECORD_DELTA_v0_5.json
run3_compute_v0_2.py
DEEPSEEK_RESPONSE_RUN3_v0_2.md
```

Core rule:

> Compute is a load, not an energy source.

2025 UF+RO baseline:

```text
39.446 GWh/year
average ~4.503 MW
```

IT-only full-load tiers:

```text
100 kW IT  -> 0.876 GWh/y
250 kW IT  -> 2.190 GWh/y
500 kW IT  -> 4.380 GWh/y
1 MW IT    -> 8.760 GWh/y
```

Facility equations:

```text
E_IT       = P_IT * 8760 * L
E_facility = E_IT * PUE
```

Actual Node-001 PUE remains UNKNOWN. PUE=1.25 exists only as a sector/policy reference.

At L=1 / PUE=1.25:

```text
100 kW IT -> 1.095 GWh/y facility -> 2.78% of UF+RO
250 kW IT -> 2.738 GWh/y          -> 6.94%
500 kW IT -> 5.475 GWh/y          -> 13.88%
1 MW IT   -> 10.950 GWh/y         -> 27.76%
```

Solar anti-double-counting:

```text
PV_credit_compute + PV_credit_desalination <= measured PV generation
```

At the PUE=1.25 / L=1 reference, 250 kW IT facility energy (~2.738 GWh/y) is close in annual magnitude to S01 PV (~2.706-2.918 GWh/y). This is NOT a self-powered claim; hourly matching, storage, curtailment and priority remain UNKNOWN.

Thermal coupling:

```text
Q_useful <= E_IT * f_capture * f_temperature_match * f_temporal_match
```

The real 2026 CIP heat-pump system is a candidate thermal sink, but CIP setpoint, thermal duty, COP map, schedule and compute coolant temperatures remain UNKNOWN.

Therefore:

```text
useful heat credit = 0
avoided heat-pump electricity = 0
```

Recommended C01 gates:

```text
100 kW IT = first commissioning tier
250 kW IT = earned expansion tier
500 kW = gated
1 MW = gated
```

C01 net-positive claim remains NOT PROVEN.

Keeper:

> Compute must pay rent in measured service, recovered heat, flexibility, resilience, or verified efficiency — not in promises.

## 14. Proposed AI operations fabric

Physical control remains conventional.

```text
Ring A: PLC/SCADA + hard interlocks + approved deterministic control
Ring B: conventional statistics / forecasting / optimization / alarms
Ring C: AI advisory fabric
Ring D: human approval
```

Current repo routing concept:

```text
PRIMARY ELIGIBLE LOCAL ADVISORY FAMILY
  DeepSeek family

LOCAL CHALLENGER / FAILOVER
  Qwen3 family / benchmark-selected local checkpoint

OPTIONAL EXTERNAL ADVERSARIAL AUDIT
  GPT family
  current repo snapshot reference: GPT-5.6 Sol
```

Exact model versions are deployment-manifest state, not constitutional dependencies. Re-verify before deployment.

Authority boundary:

```text
LLM actuator authority = NONE
OT write credentials for models = NONE
model -> deterministic constraint validator -> operator approval -> PLC/SCADA
```

Cross-model agreement is not evidence. No model family is permanently privileged.

## 15. C01 workloads and pay-rent metrics

Priority workloads:

```text
1. anomaly triage / root-cause support
2. membrane / fouling forecasting
3. predictive maintenance + procurement/event ledger
4. energy / PV / load forecasting
5. brine-routing + resource-recovery simulation
6. ecological telemetry QA + provenance
7. operator documentation / translation
```

Measure before scale:

```text
PUE / WUE / CUE with explicit boundary
IT kWh by workload
energy per correct task
false-negative rate
validated recommendation rate
operator time saved
verified kWh / chemical / membrane savings
useful heat delivered at measured temperature
heat-pump kWh actually displaced
hourly PV overlap / verified curtailment captured
regional compute-hours delivered
downstream water-quality status
```

## 16. Stable unresolved external asks

```text
2026 Dongjiakou effective electricity settlement / bill
whole-site annual kWh and meter boundary
dated current feed / product / reject flows
current measured recovery
daily brine chemistry sheet
CIP event historian
normalized flux / DP / salt-rejection history
current additive chemistry
raw 2017/2022 OUC ecological monitoring
current discharge permit / criteria
PRV / delivery-pressure / pump duty-point schedule
roof structural + PV interconnection limits
CIP temperature / thermal duty / heat-pump COP / schedule
```

## 17. Planned next work

Immediate next move:

```text
thermal receipt search for C01
-> if thermal inputs close, rerun C01 thermal coupling
-> if not, useful heat credit remains ZERO
-> then proceed to F01 adaptive fouling
```

Run 4 — F01 adaptive fouling comparator must include:

```text
UF pretreatment
anti-fouling membrane technology
dynamic UF-RO control
current chemical conditioning
2026 self-cleaning filters
2026 CIP heat-pump modernization
```

Run 5 — F02 sono-CIP remains experimental. No privileged acoustic frequency. Membrane integrity is a veto gate.

Run 6 — resource/ecology modules one at a time: Li / U / D / Mg-Ca-K-Br / microplastics / persistent contaminants where supported / OAE.

Every resource module needs yield, selectivity, energy, reagents, material life, residual fate, market ceiling and ecology before earning value.

Run 7 — stack only survivors with sequence-dependent interference edges.

Run 8 — adversarial / stochastic analysis, with the hard rule:

```text
UNKNOWN may not be sampled.
```

## 18. Network-scale future

Only after Node-001 survives:

```text
Node 002 — Baifa / lithium-recovery calibration lane
Node 003 — Tianjin Nangang / domestic-equipment lane
Node 004 — Lubei / mature cascading-brine lane
Node 005 — Yellow Sea OAE field-calibration lane
```

Then build the 167-site digital twin with site heterogeneity preserved. Never assume one SEC, recovery, tariff or ecology state for the whole fleet.

## 19. Keeper lines

```text
Products are not power. Gradients are power.
Ask every state transition to pay rent.
Unknown stays unknown.
The baseline gets to win.
A search that returns UNKNOWN is still a result.
A module with an unknown site parameter returns a transfer function, not a fictional point estimate.
Never let a plant have one timeless value when the plant itself keeps evolving.
Compute is a load, not an energy source.
Cross-model agreement is not evidence.
Compute must pay rent in measured service, recovered heat, flexibility, resilience, or verified efficiency — not in promises.
Follow transformations, not just objects.
The lattice tells us where to look. Evidence tells us what is real.
Dream freely. Promote nothing without receipts.
```

## 20. Fast boot for a new chat

If this thread dies, paste:

> Hydrate SolBrain from `archive/boot/gptbrain/SolBrain/REHYDRATION/SOLBRAIN_HYDRATION_CURRENT_STATE_2026-10-06.md`. Then fetch the latest Dongjiakou Node-001 artifacts from `public_candidate_bundle_0001/nodes/dongjiakou_node_001/`. Tell me what is verified, what is modeled, what is still UNKNOWN, and continue from the smallest next falsifiable move.

At this snapshot, the smallest next move is:

```text
thermal receipt search for C01
-> rerun C01 if thermal inputs close
-> otherwise keep heat credit zero
-> proceed to F01 adaptive fouling
```