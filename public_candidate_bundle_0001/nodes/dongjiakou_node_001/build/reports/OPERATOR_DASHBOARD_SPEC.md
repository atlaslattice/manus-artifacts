STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Node-001 Pilot Control Room — Operator Dashboard Specification

> **Document ID:** DJK-NODE-001-S6-OPERATOR-DASHBOARD-SPEC-0001  
> **Status:** SPECIFICATION AND MOCK ONLY — NOT BUILT, NOT DEPLOYED, NO PLANT CONNECTION  
> **Date:** 2026-10-06  
> **Repo:** `public_candidate_bundle_0001`  
> **Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

## 1. Purpose, audience, and governing principle

This document specifies a text mock and operator-facing behavior for the **Dongjiakou Node-001 pilot control room**. It is not an implementation plan, deployment package, or permission to connect to plant infrastructure.

**Audience:** plant operators, shift supervisors, and engineers. The interface must support safe shift decisions, evidence review, validator drill-down, model challenge, and handover without implying that a research result is a current plant state.

**Governing principle:** the dashboard must be as rigorous about what is **not known** as the research layer is. **UNKNOWN is displayed as UNKNOWN, never as zero and never hidden.** A zero is shown only when the evidence explicitly establishes a zero-credit baseline; a missing receipt is not a zero.

Current evidence is anchored to the 2025 operating receipt and executed parametric sensitivity. The integrated node remains a **PROPOSED_BOUNDARY**; HSN coordinates are **UNASSIGNED** and must not be invented.

## 2. Design principles and evidence contract

1. **No LLM actuator authority.** Models have no OT write credentials and cannot command equipment. Physical control remains with existing PLC/SCADA, hard interlocks, and approved deterministic control.
2. **The operator is the only entity that authorises physical action.** The safe path is: model recommendation → deterministic constraint validator → operator approval → PLC/SCADA.
3. **Every displayed number carries an evidence class and a source record.** A value without both is a display defect. Hover, keyboard focus, or drill-down must expose the source record ID, timestamp/period, transformation, and bound where applicable.
4. **Recommendations are not instructions.** Each recommendation shows model family, exact version/checkpoint reference, task class, confidence/uncertainty, challenger result, and validator verdict. Model agreement is not evidence and does not authorise action.
5. **Append-only accountability.** Approvals, rejections, validator findings, failures, source revisions, and handover notes are retained. Rejected or failed recommendations are never deleted.
6. **Component-level discipline.** A component veto cannot be offset by aggregate benefit; one physical kWh, m3, kg, or tonne receives at most one primary accounting credit.

### Evidence-class legend

| Class | Meaning in the dashboard | Permitted interpretation |
|---|---|---|
| **MEASURED** | Instrumented/current receipt with defined boundary and timestamp | Only class that can establish a current physical state |
| **REPORTED** | Dated operator, owner, or official reported quantity | Reported fact; not automatically a live state |
| **DERIVED** | Deterministic calculation from identified evidence | Calculation, not an independent receipt |
| **HISTORICAL** | Prior-period or counterfactual value | Cannot populate current state |
| **PLANNED** | Official plan or intended capacity | Cannot populate operating state or node access |
| **MODELED** | Model or scenario output | Scenario only; no primary physical credit without qualifying receipt |
| **SENSITIVITY** | Parametric technical/economic sensitivity | Bounded exploration, not a receipt |
| **PROPOSED** | Architecture, control, or allocation proposal | Not implemented and not current |
| **REFERENCE** | Policy/sector benchmark used for comparison | Not a Node-001 receipt |
| **UNKNOWN** | Not established by the available evidence | Must remain visibly UNKNOWN; never silently converted to zero |

**Hard display rule:** only **MEASURED** can establish a current physical state. REPORTED and DERIVED retain their labels and source records; HISTORICAL, PLANNED, MODELED, SENSITIVITY, PROPOSED, REFERENCE, and UNKNOWN must never be rendered as live operating facts.

## 3. Continuity header

The header is persistent on every screen and survives panel filtering. It prevents a shift from losing node identity, time basis, or evidence freshness.

```text
+------------------------------------------------------------------------------------------------+
| DONGJIAKOU NODE-001 | component anchor: W01_DESAL | operating year: 2025 | HSN: UNASSIGNED   |
| Evidence freshness: [SOURCE-SNAPSHOT / timestamp required] | Reference head: 4756036f9c428fa... |
| Current physical state: MEASURED receipts only | Advisory plane: READ-ONLY | OT write: NONE   |
| Shift: [operator] [start/end] | Last handover: [record ID] | [View source register] [Acknowledge] |
+------------------------------------------------------------------------------------------------+
```

The freshness field must show a timestamp and age when a source snapshot exists; otherwise it displays **UNKNOWN**, not “current.” The reference head is fixed to the metadata value above. A stale or missing snapshot raises a visible WARN but does not create a plant alarm.

## 4. Desalination panel

Purpose: show the receipt-backed W01 desalination baseline while separating reported production, derived utilization, process-train energy, and unknown whole-site/current tariff fields.

Known evidence: capacity **100,000 m3/day** (**REPORTED**, source record required in source register); 2025 product **17.93 Mm3** (**REPORTED**, `RUN_0_OPERATING_2025_v0_2`, operating year 2025); utilization **U = 0.4912328767** (**DERIVED**, same run); UF+RO process-train SEC **2.2 kWh/m3** (**REPORTED**, same run); derived process-train energy **39.446 GWh** (**DERIVED**, same run). The SEC is explicitly **process-train, NOT whole-site**.

```text
+-------------------------------- DESALINATION / W01_DESAL --------------------------------------+
| Capacity             100,000 m3/day                 [REPORTED | source: receipt ID required]   |
| 2025 product         17.93 Mm3                      [REPORTED | RUN_0_OPERATING_2025_v0_2]     |
| Utilization U        0.4912328767                   [DERIVED  | RUN_0_OPERATING_2025_v0_2]     |
| UF+RO SEC            2.2 kWh/m3                     [REPORTED | RUN_0_OPERATING_2025_v0_2]     |
| Process-train energy 39.446 GWh/year                [DERIVED  | RUN_0_OPERATING_2025_v0_2]     |
|                                                                                            |
| Whole-site SEC       UNKNOWN                         [UNKNOWN | whole-site boundary receipt]     |
| Current tariff       UNKNOWN                         [UNKNOWN | RUN_0 / RUN_3]                  |
| Current electricity  UNKNOWN                         [UNKNOWN | current-cost receipt]           |
| Current recovery     UNKNOWN                         [UNKNOWN | dated measured recovery]        |
| Marine discharge     UNKNOWN                         [UNKNOWN | feed-minus-product is modeled] |
| NOTE: 2.2 kWh/m3 is process-train SEC, NOT whole-site SEC.                                     |
+-----------------------------------------------------------------------------------------------+
```

The historical 2018–2020 tariff counterfactual is available only in a drill-down labelled **HISTORICAL / COUNTERFACTUAL**, never as a 2025 or 2026 cost.

## 5. Compute (C01) panel

Purpose: show bounded C01 sensitivity without implying self-powering, current PUE, heat credit, or net-positive operation. The four tiers are 100/250/500/1000 kW IT at full-load factor `L=1` for the published sensitivity. Actual load factor and actual PUE are **UNKNOWN**.

The panel must show IT energy, facility energy at PUE=1, facility energy at PUE=1.25, share of the 2025 UF+RO process energy, and S01 PV annual-energy ratios. Values below are **SENSITIVITY** outputs from `RUN_3_COMPUTE_v0_2`; PUE=1.25 is **REFERENCE**, not a receipt.

```text
+-------------------------------- C01 COMPUTE / SENSITIVITY -------------------------------------+
| IT load factor L: UNKNOWN (published rows below use L=1) | Actual PUE: UNKNOWN                |
| WARNING: PUE=1.25 is a SECTOR POLICY REFERENCE, NOT A NODE-001 RECEIPT.                     |
| Tier       IT energy   Facility @PUE1  Facility @PUE1.25  UF+RO share PUE1/PUE1.25  S01 A/B ratio|
| 100 kW     0.876 GWh   0.876 GWh       1.095 GWh          2.221% / 2.776%          2.471 / 2.665|
| 250 kW     2.190 GWh   2.190 GWh       2.7375 GWh         5.552% / 6.940%          0.989 / 1.066|
| 500 kW     4.380 GWh   4.380 GWh       5.475 GWh         11.104% / 13.880%         0.494 / 0.533|
| 1,000 kW   8.760 GWh   8.760 GWh       10.950 GWh        22.208% / 27.759%         0.247 / 0.266|
| PUE=1 rows: SENSITIVITY | PUE=1.25 rows: SENSITIVITY + REFERENCE basis | process baseline: 39.446 GWh|
| Useful heat credit: 0 GWh_th/year explicit zero baseline; electric value: UNKNOWN until measured sink |
| Net-positive: NOT_PROVEN | node energy neutrality: UNKNOWN | hourly PV overlap: UNKNOWN           |
| First commissioning tier: 100 kW IT [PROPOSED/RECOMMENDED] | next: 250 kW after pilot gates     |
| 500 kW and 1 MW: GATED SCALE CASES; no automatic progression.                                      |
+------------------------------------------------------------------------------------------------+
```

S01 A and S01 B are annual-energy ratios to facility energy at PUE=1.25; they do not establish hourly matching. Existing S01 PV is not incremental to the node and may be allocated once only. Low-grade heat is not electric value: only displaced measured heat-pump electricity or another verified sink earns credit.

## 6. Recommendation queue

The queue is advisory and append-only. It must never use imperative language such as “start,” “open,” or “set” without a clearly marked proposal and an operator control. The current routing architecture lists **DeepSeek** as the primary eligible local advisory family, **Qwen3** as local challenger/failover, and optional external **OpenAI GPT** as a non-critical-path adversarial audit. Exact deployment checkpoints are deployment-manifest state and must be pinned before use.

```text
+-------------------------------- RECOMMENDATION QUEUE -------------------------------------------+
| ID      Task class        Model/version/checkpoint    Confidence  Challenger     Validator      |
| R-0001  [class]           DeepSeek [exact ref]        [0.00/UNK]  Qwen3 [result]  [PASS/WARN]   |
|         Proposal: [plain-language recommendation; never an instruction]                        |
|         Evidence: [class] [source record IDs] | uncertainty: [text] | outcome: [pending]       |
|         [ APPROVE PHYSICAL ACTION ] disabled until validator PASS + required evidence          |
|         [ APPROVE ADVISORY ONLY ] [ REJECT ] [ ESCALATE / REQUEST RECEIPT ]                   |
|                                                                                               |
| R-0002  ...                                                                                   |
| Status values: PENDING / APPROVED-ADVISORY / APPROVED-ACTION / REJECTED / FAILED / EXPIRED    |
| Rejected and failed rows remain searchable with reason, actor, timestamp, and downstream result.|
+------------------------------------------------------------------------------------------------+
```

Required record fields are timestamp, task class, data-boundary label, exact model/version/checkpoint, hardware/provider, prompt/template hash, input snapshot hash, tool calls, output hash, latency, measurable energy, confidence/uncertainty, challenger result, operator disposition, and downstream physical outcome. **Disagreement escalates; agreement still does not authorise physical action.**

## 7. Validator status panel

The panel lists all gates from `build/validators/gates.py`. Each gate is individually reportable and supports drill-down into detail and findings. A validation run fails when any gate is **FAIL** or **VETO**.

```text
+-------------------------------- VALIDATOR STATUS ----------------------------------------------+
| Run: [ID] | overall: [PASS/WARN/FAIL/VETO] | executed: [timestamp] | [Export findings]          |
| G01 UNKNOWN cannot enter Monte Carlo                         [N/A] [open findings]              |
| G02 UNKNOWN cannot silently become zero                      [PASS]                             |
| G03 Historical values cannot populate current state          [PASS]                             |
| G04 Planned capacity cannot populate operating state         [PASS]                             |
| G05 Feed-product residual cannot become marine discharge      [PASS]                             |
| G06 One PV kWh cannot receive two primary credits             [PASS]                             |
| G07 One recovered mass cannot be double-credited              [PASS]                             |
| G08 Compute heat needs a measured sink                         [PASS]                             |
| G09 Service benefit needs before/after KPI evidence            [PASS]                             |
| G10 Ecological veto cannot be offset                           [PASS]                             |
| G11 LLM actuator authority is NONE                             [PASS]                             |
| G12 Model consensus is not evidence                            [PASS]                             |
| G13 RO high-pressure head cannot be counted twice              [PASS]                             |
| G14 Existing S01 solar cannot be counted twice                  [PASS]                             |
| G15 Conservation and bound checks                              [PASS]                             |
| G16 Net-positive requires measured terms                        [PASS]                             |
| Click/focus any row: invariant, detail, finding paths, source IDs, and remediation receipt.    |
+------------------------------------------------------------------------------------------------+
```

Allowed statuses are **PASS / WARN / FAIL / VETO / NOT_APPLICABLE**. VETOes include ecological/compliance conditions such as INV-19; economic benefit never offsets a veto.

## 8. Credit ledger panel

The ledger is append-only and makes double-counting visible. Every entry shows resource, quantity, units, evidence class, receipt IDs, and the applicable availability bound. A positive primary credit is prohibited when the bound is UNKNOWN; one resource may have at most one primary credit.

```text
+-------------------------------- CREDIT LEDGER -------------------------------------------------+
| Entry ID | Resource | Quantity/units | Evidence | Receipt IDs | Bound | Bound basis/status       |
| [ID]     | S01_PV_energy | UNKNOWN kWh/year | UNKNOWN | [IDs] | UNKNOWN | no measured PV receipt |
| [ID]     | G01_regional_green_energy | 0 kWh/year | UNKNOWN | [IDs] | 0 | node allocation UNKNOWN |
| [ID]     | C01_useful_heat | 0 GWh_th/year | UNKNOWN | [IDs] | 0 | no measured thermal sink|
| [ID]     | C01_model_service_benefit | 0 dimensionless | UNKNOWN | [IDs] | 0 | no before/after KPI     |
| [ID]     | BIO01_* / H01_* / B01_* | 0 or UNKNOWN | class | [IDs] | bound | [basis]                |
| Flags: [DOUBLE_PRIMARY_CREDIT] [CREDIT_WITHOUT_ESTABLISHED_AVAILABILITY] [BOUND_EXCEEDED]     |
+------------------------------------------------------------------------------------------------+
```

Explicit zero-credit baselines must carry a reason. Planned regional generation, existing S01 PV, storage, useful heat, biological products, and unused head remain zero credit or UNKNOWN as supported by the ledger bounds; they must not be inferred from capacity or architecture.

## 9. UNKNOWN ledger panel

This is a first-class work queue, grouped by subsystem. Each row states what receipt would close it; “not yet known” is an actionable status, not a blank.

| Subsystem | Open unknown | Display | Receipt that would close it |
|---|---|---|---|
| Desalination | Whole-site SEC, current tariff/cost, dated recovery, current marine discharge | **UNKNOWN** | Boundary-tagged meter interval, tariff/contract, validated recovery and discharge records |
| C01 compute | Load factor, actual PUE, WUE, cooling-water source | **UNKNOWN** | Commissioning telemetry with boundary and interval definitions |
| C01 heat | Capture fraction, temperatures, CIP demand/setpoint, COP, temporal match | **UNKNOWN** | Calibrated thermal meters, process demand trace, heat-pump map, matched interval receipt |
| S01 PV | Measured generation, roof/curtailment, hourly overlap | **UNKNOWN / NOT_ESTABLISHED** | Revenue-grade generation and curtailment telemetry allocated once |
| Green access | Node allocation, eligible load set, contract price | **UNKNOWN** | Executed allocation/interconnection/contract receipt |
| Storage | Hourly mismatch, capacity, efficiency, degradation, envelope | **UNKNOWN** | Commissioning and interval performance receipt |
| BIO01 | Feedstock allocation, gas composition/use, nutrient mass/assay, reclaimed-water displacement | **UNKNOWN / zero credit** | Allocation/contract, lab assay, flow meter, verified displacement/off-take |
| Service benefit | Before/after KPI effect | **UNKNOWN / zero credit** | Pre-registered baseline, post-intervention measurement, validated comparison |

```text
+-------------------------------- UNKNOWN LEDGER ------------------------------------------------+
| OPEN (12) | W01_DESAL (4) | C01 (7) | S01 (3) | GRID/GREEN (3) | BIO01 (4) | [filter]      |
| UNKNOWN: actual PUE               close with: boundary-tagged commissioning telemetry        |
| UNKNOWN: hourly PV/compute overlap close with: synchronized generation/load intervals         |
| UNKNOWN: current tariff           close with: executed current tariff/contract receipt        |
| Each row: owner | opened | impact | required receipt | age | [assign] [mark received]           |
+------------------------------------------------------------------------------------------------+
```

## 10. Failure ledger panel

Failures are preserved without shame or erasure. The panel is an engineering learning and accountability surface, not a punitive scorecard.

```text
+-------------------------------- FAILURE LEDGER ------------------------------------------------+
| Failure ID | Date/time | Gate/task | What failed | Evidence | Operator disposition | State    |
| F-0001     | [time]    | Gxx/Rxxxx | [plain text] | [IDs]    | [reject/escalate]    | OPEN     |
| F-0002     | [time]    | [task]    | [challenger disagreement / tool error / stale data] | ... | ... | CLOSED |
| No delete. Corrections append a new record linked to the original. [Filter] [Export]         |
+------------------------------------------------------------------------------------------------+
```

A failure must show whether it was model, data, validator, network-boundary, human-interface, or plant-process related; no failure may be relabelled as success merely because another model agreed.

## 11. KPI trend specification

The trend store must keep boundary, numerator/denominator, time window, evidence class, and source record with every point. Until the relevant receipt exists, the dashboard marks the KPI **UNKNOWN** rather than plotting zero.

| KPI | Initial status | Required boundary/definition |
|---|---|---|
| PUE | **UNKNOWN** | C01 facility energy / IT energy, measured interval |
| WUE | **UNKNOWN** | Compute water consumption boundary and interval |
| CUE | **UNKNOWN** | Carbon boundary, grid factor/source, and time basis |
| Energy per validated task | **UNKNOWN** | Measured energy divided by validated task outcome |
| Recommendation acceptance rate | **UNKNOWN** | Accepted recommendations / eligible recommendations, with dispositions retained |
| Recommendation correctness | **UNKNOWN** | Verified downstream outcome against recommendation claim |
| False-negative rate | **UNKNOWN** | Missed anomalies/events against a defined labeled set |
| Operator time saved | **UNKNOWN** | Before/after measured operator task time, not model assertion |
| Verified plant kWh saved | **UNKNOWN** | Metered displacement with baseline and receipt |
| Verified chemicals saved | **UNKNOWN** | Measured chemical use against validated baseline |
| Membrane-life effect | **UNKNOWN** | Measured condition/life outcome with comparable baseline |
| Useful recovered heat delivered | **UNKNOWN** | Metered useful heat delivered to a verified sink |
| Uptime | **UNKNOWN** | Defined service/asset availability boundary |
| Failover reliability | **UNKNOWN** | Challenger/failover success under measured tests |
| Latency | **UNKNOWN** | End-to-end task latency by task class and SLA |
| Regional service output | **UNKNOWN** | Validated output for named regional service boundary |

**Tokens/kWh alone is not a sufficient KPI.** A low token count or low energy figure is not value without correctness, safety, latency, operator effect, and verified plant outcome.

## 12. Alarm and interlock philosophy

**Hard constraints, alarms, and interlocks are deterministic and never routed through an LLM.** Existing PLC/SCADA and approved deterministic/statistical control retain physical authority. An LLM may explain a deterministic alarm or propose a diagnostic hypothesis, but it cannot suppress, rewrite, acknowledge on behalf of an operator, or bypass an alarm/interlock.

The advisory plane is non-critical. If models, brokers, validators, or external calls fail, the plant must continue on its approved operating controls; the failure is logged and shown as an advisory-plane fault, not converted into a plant command. A validator FAIL/VETO blocks the relevant recommendation, not safe baseline plant operation.

## 13. Data boundary and security

- The **OT network is segmented** from the AI data plane.
- The AI data plane reads a **read-only telemetry replica or approved broker**; it does not obtain an OT write path.
- **Raw OT data egress is denied by default.** Remote-model inputs are redacted, aggregated, and non-secret unless explicitly policy-approved.
- **Credentials are never exposed in model context.** Secrets are held outside prompts, logs, and model-visible tool results.
- **External calls are logged and policy-gated**, with destination, purpose, data-boundary label, model/provider, request/response hashes, and operator/policy decision.
- Source snapshots, prompt/template hashes, input hashes, output hashes, tool calls, and downstream outcomes are retained for replay and audit.

## 14. Accessibility and shift handover

Use plain English labels, high contrast, scalable text, keyboard navigation, visible focus, non-colour status labels, and text alternatives for every icon or chart. Do not use colour as the only distinction between PASS/WARN/FAIL/VETO/UNKNOWN. Screen-reader order follows continuity header, evidence legend, safety/validator state, then operational panels. Units and time zones are explicit; percentages include denominators.

Shift handover must produce an immutable summary containing: current evidence snapshot and freshness; open UNKNOWNs and receipt owners; active alarms (from deterministic systems); validator run and any WARN/FAIL/VETO; pending, approved, rejected, and failed recommendations; credit-ledger changes; failure-ledger changes; operator notes; and the next required receipt. The incoming operator must acknowledge the handover without implying that UNKNOWN items were accepted as safe or zero.

## 15. What this dashboard must never show

- A model output as an actuator command, automatic setpoint, or implicit instruction.
- A green **zero** where the evidence is UNKNOWN.
- A historical tariff, planned generation, annual PV ratio, or PUE=1.25 reference as a current Node-001 receipt.
- Whole-site SEC inferred from the 2.2 kWh/m3 process-train SEC.
- Modelled feed-minus-product residual as measured marine discharge.
- C01 as an energy source, net-positive operation, self-powering, or electric heat credit without measured receipts.
- Regional planned capacity as Node-001 access or energy credit.
- Existing S01 PV as incremental generation or more than one primary credit.
- Cross-model agreement as evidence or operator approval.
- A positive service benefit without before/after KPI evidence.
- A recommendation, rejection, failure, or validator finding erased from history.
- Credentials, raw OT secrets, unrestricted raw OT data, or an unlogged external call.
- A dashboard health indicator that masks stale evidence, unknown boundaries, or an unresolved veto.

## 16. Source register for this specification

| Source record | Use in dashboard |
|---|---|
| `RUN_0_OPERATING_2025_v0_2.json` | 2025 product, derived utilization, process-train SEC/energy, tariff UNKNOWN and counterfactual warning |
| `RUN_3_COMPUTE_v0_2.json` | C01 tiers, PUE scenarios, process-energy shares, S01 ratios, unknown parameters, anti-double-counting and heat-credit rules |
| `INTEGRATED_NODE_PROFILE_v0_2.json` | Component boundaries, proposed status, vetoes, green-access UNKNOWN, control-plane rule, conservation/accounting rules |
| `C01_MODEL_ROUTING_POLICY_v0_2.json` | Model roles, challenger routing, logging, authority boundary, segmented network, external-call policy |
| `build/validators/gates.py` | G01–G16 names, invariants, statuses, failure behavior, deterministic validation path |
| `build/validators/ledger.py` | Append-only credit entries, evidence classes, resource bounds, single-primary-credit and UNKNOWN-bound rules |

**Implementation boundary:** this document is the complete mock/specification deliverable. No dashboard is built, deployed, connected, or authorised by it.
