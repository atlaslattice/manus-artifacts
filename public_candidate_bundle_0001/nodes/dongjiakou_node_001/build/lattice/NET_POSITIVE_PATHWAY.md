STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Net-Positive Data Centre Operations — Verifiable-Data Pathway

**Document ID:** DJK-C01-NET-POSITIVE-PATHWAY-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON — **NON-DEPLOYABLE**
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`
**Scope:** Node-001 C01 compute pilot, and the general rule for any lattice node

---

## 1. The goal, stated precisely

> Net-positive data centre operations, and optimisations in ORCS and lattice
> metrics, using **only verifiable data — not theory**.

This document converts that goal into a testable condition, identifies exactly
which terms are currently unmeasured, and specifies the measurement set that
would settle it. It does not assert that C01 is or can be net-positive.

**Current answer: `C01_net_positive = NOT_PROVEN`.** That is not a pessimistic
finding; it is the honest state of the evidence.

---

## 2. The governing inequality

C01 may claim net-positive operation only when the following holds, with every
term **measured**:

```
new incremental clean generation
+ verified plant electrical savings
+ verified heat-pump electrical savings
>= compute facility electricity
```

Three constraints attach to that inequality and are not negotiable:

1. **Existing S01 PV does not become "new C01 generation" if reassigned.**
   Reassigning an existing kWh changes attribution. It does not create a kWh.
2. **Thermal quantity is not electric value.** Heat earns electric credit only as
   displaced, measured heat-pump electricity or another verified sink.
3. **Social and regional service must be measured, not assumed.**

---

## 3. Term-by-term status at Node-001

| Term | Status | Why |
| --- | --- | --- |
| New incremental clean generation | **UNKNOWN** | No verified curtailment capture and no node allocation. Regional wind/PV is PLANNED, not allocated. |
| Verified plant electrical savings | **UNKNOWN** | No before/after measurement campaign. Whole-site SEC is unmeasured. |
| Verified heat-pump electrical savings | **UNKNOWN** | Useful-heat credit is zero: no CIP setpoint, thermal duty, coolant temperatures, COP map or temporal overlap. |
| Compute facility electricity | **SCENARIO ONLY** | 1.095 GWh/year at 100 kW IT under the PUE = 1.25 *reference*. Actual Node-001 PUE is UNKNOWN; load factor L is UNKNOWN. |

**Therefore net-positive is not merely unproven — it is currently *unmeasurable*,
because three of the four terms have no instrument behind them.**

That is the real blocker, and it is an instrumentation problem, not a
technology problem.

---

## 4. Why this must pass ORCS, not just arithmetic

ORCS — the Ontology-Routed Context Spine — is the governance profile
`Γ_t = (Θ_t, W_t, Φ_t, R_t)`, and it supplies the rule that makes this
disciplined rather than rhetorical.

> **The ledger records. Atlas promotes. ORCS governs. CAS anchors.**

The load-bearing invariant is:

```
Π^q_{Γ_t}(S_t) ⊆ E(S_t)
```

**Atlas promotes from retained evidence. Atlas does not create truth.** A
net-positive claim is an evidence entry, and it can only be promoted if it is
already inside the retained evidence set. Theory cannot be promoted into it,
because theory is not in `E(S_t)`.

### 4.1 A net-positive claim as a promotion candidate

| Field | Requirement |
| --- | --- |
| Claim class `q` | `deployment_candidate` at most. Never `ratified_canon` without an explicit human-root event. |
| Confidence `C(e)` | Corroboration from independent instruments, not from repeated model output |
| Receipt `R(e)` | Metered, dated, boundary-stated, asset-attributed receipts |
| Policy fit `P(e)` | Satisfies the accounting rules in section 5 |
| Audit `A(e)` | Operator disposition and independent review on record |

And the boundary that Appendix I states explicitly:

> **A high score produces promotion eligibility, not automatic ratification or
> truth.** Threshold crossing creates eligibility. Ratification requires an
> explicit authority event: human-root / S10.

The must-not-infer block applies with full force:

```
Recorded ≠ promoted
Promoted ≠ ratified
Ratified ≠ deployed
Canonicalized ≠ true
Hashed ≠ meaningful
Receipt-bearing ≠ approved
```

---

## 5. What counts as verifiable data

| Counts as evidence | Does **not** count |
| --- | --- |
| Calibrated meter readings at a stated boundary | Model output |
| Signed contracts, tariffs, settlement statements | Vendor performance claims |
| Accredited laboratory analyses with method and detection limits | Theoretical or stoichiometric ceilings |
| Regulatory monitoring data | Secondary summaries of primary data |
| Witnessed commissioning test records | Design or nameplate values |
| Before/after measurement with a defined counterfactual | Single-period snapshots |
| Independent audit findings | Cross-model consensus |

**Model consensus is not evidence.** A statistic extracted by a model is
**PROPOSED** class until a human verifies it against the primary document.

---

## 6. The measurement set that would settle the inequality

Each row is the minimum instrumentation for one term. Nothing here is theoretical;
every item is an instrument, a meter, a contract or an assay.

### 6.1 Compute facility electricity (the denominator)

| # | Measurement | Instrument / source | Boundary | Frequency |
| --- | --- | --- | --- | --- |
| M1 | IT energy | IT rack PDU or UPS output meter | IT equipment | 1 min |
| M2 | Total facility energy | Incoming utility meter or main panel meter | Whole compute facility | 1 min |
| M3 | Derived PUE | M2 / M1, boundary stated | Facility | 15 min rolling |
| M4 | IT load factor L | M1 against installed capacity | IT equipment | hourly |
| M5 | Cooling energy | Chiller / pump / fan sub-meters | Cooling plant | 1 min |
| M6 | Water consumption and source | Water meter, source identified | Facility | daily |

M1–M6 close the denominator. Until they exist, facility electricity is a scenario
and no ratio derived from it is a measurement.

### 6.2 Verified plant electrical savings (term 2)

| # | Measurement | Instrument / source | Boundary | Frequency |
| --- | --- | --- | --- | --- |
| M7 | Whole-site SEC before/after | Site energy meter and product flow meter | Site boundary | daily |
| M8 | Process-train SEC before/after | Process-area meter | Process train | daily |
| M9 | Incremental auxiliary load of the intervention | Sub-meter on new loads | Intervention | 1 min |
| M10 | Counterfactual definition | Written protocol with normalisation basis | n/a | once |

M7–M10 must exist *before* an intervention so a genuine before/after is possible.
A saving claimed without M9 is a saving that ignores the load it introduced.

### 6.3 Verified heat-pump electrical savings (term 3)

| # | Measurement | Instrument / source | Boundary | Frequency |
| --- | --- | --- | --- | --- |
| M11 | Coolant supply and return temperature | Temperature sensors, calibrated | Compute cooling loop | 1 min |
| M12 | Recoverable thermal power | Flow meter × ΔT | Cooling loop | 1 min |
| M13 | CIP target temperature and schedule | Plant CIP records | CIP subsystem | per cycle |
| M14 | CIP thermal duty | Heat meter on CIP | CIP subsystem | per cycle |
| M15 | Heat-pump COP map vs temperature | Manufacturer test data, verified on site | Heat pump | once + spot checks |
| M16 | Displaced electricity | Sub-meter on the displaced heater/chiller | CIP subsystem | 1 min |

Then:

```
Q_useful    <= E_IT * f_capture * f_temperature_match * f_temporal_match
E_HP_saved  =  min(Q_useful, Q_CIP_demand) / COP_HP
```

All three matching factors must be measured. **A missing factor is UNKNOWN, never
1.0.**

### 6.4 New incremental clean generation (term 1)

| # | Measurement | Instrument / source | Boundary | Frequency |
| --- | --- | --- | --- | --- |
| M17 | PV AC output | Revenue-grade inverter meter | Generator | 1 min |
| M18 | Curtailment or export limitation | Inverter or revenue meter, or utility notice | Interconnection point | event |
| M19 | New generation specifically added for C01 | Interconnection agreement and as-built records | Generator | once |
| M20 | Contractual renewable attributes | PPA or direct-green agreement | Contract | once |

**M18 is the pivotal measurement.** Without verified curtailment capture or
genuinely new generation, C01 cannot be argued electrically neutral by
reassigning existing S01 output. M17 alone does not establish incrementality.

### 6.5 Service and regional benefit (measured, not assumed)

| # | Measurement | Instrument / source | Boundary | Frequency |
| --- | --- | --- | --- | --- |
| M21 | Recommendation acceptance rate | Operator disposition log | Advisory plane | per event |
| M22 | Recommendation correctness | Verified physical outcome | Advisory plane | per event |
| M23 | False-negative rate on anomaly tasks | Ground-truth comparison | Advisory plane | per event |
| M24 | Operator time saved | Time study with a defined baseline | Operations | periodic |
| M25 | Regional service output | Contracted and delivered service record | Node boundary | per period |

Until M21–M25 exist, **model service benefit remains zero.** Tokens per kWh is
not a sufficient KPI and is not accepted as evidence of service.

---

## 7. ORCS and lattice metrics

### 7.1 Node-level metrics

Every node reports the same metric set, each tagged MEASURED or UNKNOWN. An
UNKNOWN metric is reported as UNKNOWN — never as zero, never omitted.

| Metric | Class required to report a value | Current Node-001 status |
| --- | --- | --- |
| PUE | MEASURED, boundary stated | UNKNOWN (1.25 is a reference only) |
| WUE | MEASURED, source identified | UNKNOWN |
| CUE | MEASURED, **with explicit boundary** | UNKNOWN |
| Energy per validated task | MEASURED | UNKNOWN |
| Recommendation acceptance rate | MEASURED | UNKNOWN |
| Recommendation correctness | MEASURED | UNKNOWN |
| False-negative rate | MEASURED | UNKNOWN |
| Operator time saved | MEASURED | UNKNOWN |
| Verified plant kWh saved | MEASURED | UNKNOWN |
| Verified chemicals saved | MEASURED | UNKNOWN |
| Membrane-life effect | MEASURED | UNKNOWN |
| Useful recovered heat delivered | MEASURED | UNKNOWN (credit fixed at 0) |
| Uptime | MEASURED | UNKNOWN |
| Failover reliability | MEASURED | UNKNOWN |
| Latency | MEASURED | UNKNOWN |
| Regional service output | MEASURED | UNKNOWN |

> **CUE without a stated boundary is not a metric.** A carbon figure whose
> boundary is unstated cannot be compared to any other figure, and therefore
> cannot be aggregated.

### 7.2 Lattice-level metric rules

| Rule | Statement |
| --- | --- |
| L01 | One physical resource receives at most one primary credit across the entire lattice |
| L02 | A shared resource must be explicitly partitioned before either node claims it |
| L03 | An aggregate may never be attributed back to a single node |
| L04 | An aggregate may never backfill a node-level UNKNOWN |
| L05 | A node veto is never diluted by lattice-level performance |
| L06 | Nodes are comparable only under a shared boundary definition; non-comparability must be declared |
| L07 | A registered candidate node is not an assigned coordinate |
| L08 | Model-extracted statistics are PROPOSED class until human-verified against the primary document |
| L09 | Coverage and exclusions must be stated with every aggregate |
| L10 | No lattice figure may justify a physical action at any node |

**Consequence for net-positive claims:** a lattice cannot be net-positive by
netting a surplus node against a deficit node and calling the result a
net-positive data centre operation. Net-positive is a **node-level** claim about a
**node-level** boundary. Aggregation is reporting, not offsetting.

---

## 8. The staged path

### Stage A — Instrument before claiming (no compute required)

Install M1–M6 at the 100 kW tier. Record baseline for at least one full
seasonal cycle. **No net-positive claim is made or implied during Stage A.**

**Exit criterion:** PUE, WUE and facility electricity are MEASURED with stated
boundaries, and the load factor L is characterised.

### Stage B — Establish the savings baseline

Execute M7–M10 as a written before/after protocol. This must precede any
intervention, or the counterfactual is lost.

**Exit criterion:** verified plant electrical savings are MEASURED.

### Stage C — Prove or disprove the heat loop

Execute M11–M16. This is the highest-uncertainty term. A negative result is a
useful result: if the CIP thermal duty does not overlap temporally with compute
heat availability, the loop does not close and the credit stays zero.

**Exit criterion:** either a measured, non-zero E_HP_saved, or a documented
finding that the loop does not close.

### Stage D — Establish incrementality

Execute M17–M20. If M18 shows no verified curtailment and M19 shows no new
generation, then **term 1 is zero** and net-positive must be argued from terms 2
and 3 alone.

**Exit criterion:** term 1 is either a measured positive number or a documented
zero.

### Stage E — Evaluate the inequality honestly

With terms measured, evaluate:

```
term1 + term2 + term3  vs  compute facility electricity
```

All four must be measured. If the inequality fails, the honest output is
**`C01_net_positive = FALSE`** at that tier — which is a legitimate and valuable
engineering result, and it gates the 250 kW expansion accordingly.

### Stage F — Earn the expansion

The 250 kW tier is an **earned** tier. It is unlocked by measured performance at
100 kW, not by schedule. The 500 kW and 1 MW tiers remain gated.

---

## 9. Falsification conditions

This pathway is designed to be falsifiable. Net-positive is **disproved** at a
tier if any of the following is measured:

1. Facility electricity exceeds the sum of verified generation and savings.
2. PUE is measured materially above the reference, raising the denominator.
3. Verified curtailment is zero and no new generation was added — term 1 is zero.
4. The CIP thermal duty does not temporally overlap compute heat availability —
   term 3 collapses to zero.
5. Incremental auxiliary load (M9) exceeds the claimed saving (M7/M8).
6. Model service benefit cannot be demonstrated with a before/after KPI.
7. An ecological veto fails — in which case the node fails regardless of the
   energy arithmetic.

**A falsified net-positive claim is a success of the method, not a failure of the
project.** The purpose of this package is to make that outcome visible rather
than to avoid it.

---

## 10. Non-claims

This document does **not** claim:

- that C01 is or will be net-positive
- that any measured saving exists at Node-001 today
- that regional planned generation is available to the node
- that existing S01 PV can be counted as new C01 generation
- that useful heat can be credited without a measured sink
- that ORCS scoring constitutes ratification
- that a lattice aggregate can offset a node-level deficit
- that anything here authorises construction, procurement or a plant change

```
C01_net_positive = NOT_PROVEN
```

---

## 11. Keeper

> Compute must pay rent in measured service, recovered heat, flexibility,
> resilience, or verified efficiency — not in promises.

> The ledger records. Atlas promotes. ORCS governs. CAS anchors. Nobody pretends
> the scoreboard created the game.
