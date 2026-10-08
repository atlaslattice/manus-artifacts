STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# C01 Deployment Manifest — Dated Runtime and Model Register

**Document ID:** DJK-C01-DEPLOYMENT-MANIFEST-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON
**Manifest date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

---

## 1. Why this document exists

The routing policy states the rule directly:

> Do not hard-code model versions into constitutional architecture. Put actual
> checkpoint/version/API/runtime into a dated deployment manifest.

This is that manifest. Everything below is **deployment state**, not
architecture. It is expected to change, and it may change without touching a
single invariant, gate or constitutional rule. The durable parts of the design
are the roles, the routing features and the authority boundary — not the vendor
names recorded here.

**Nothing in this manifest has been deployed.** No model is connected to any
plant system. This is a register of intended deployment state for a pilot that
has not been commissioned.

---

## 2. Authority boundary (durable — restated here for completeness)

| Property | Value |
| --- | --- |
| LLM actuator authority | **NONE** |
| OT write credentials held by any model | **NONE** |
| Physical control authority | Existing PLC/SCADA, hard interlocks, approved deterministic control |
| Recommendation path | model → deterministic constraint validator → operator approval → PLC/SCADA |
| Emergency behaviour | The compute and advisory plane may fail without preventing plant operation |
| Model self-modification of control policy | **PROHIBITED** |
| Model consensus as evidence | **NOT EVIDENCE** |

These rows are constitutional. They do not change when a model version changes.

---

## 3. Role register

| Role | Family | Durable? | Authority |
| --- | --- | --- | --- |
| Primary eligible local advisory family | DeepSeek | Role is durable; vendor is replaceable | Advisory only |
| Local challenger / failover | Qwen3 | Role is durable; vendor is replaceable | Advisory only |
| Optional external adversarial audit | OpenAI GPT | Role is optional and off the critical path | Advisory only, redacted or aggregated data by default |

### 3.1 Why DeepSeek is "primary eligible" and not "sole authority"

The routing policy is explicit that *primary* means **first eligible advisory
candidate**, not monopoly share and not authority. The ORCS vendor-diversity
invariant (INV-7 / INV-7c) caps single-vendor capability-weighted routing share at
**0.47**, with a fallback count target of **2**. Exact routing shares are
**measured, not preassigned**.

### 3.2 Why the vendor may be replaced

Routing priority can change only after benchmark receipts and policy review. No
family is permanently privileged. The selection criteria are measured task
accuracy, false-negative rate on anomaly tasks, energy per correct task, joules
per token where meaningful, tool-call reliability, latency against SLA, data
residency fit, and model or version health. Cost enters only after tariff and
model-pricing boundaries are known.

---

## 4. Dated reference register

The following entries record the model references named in
`C01_MODEL_ROUTING_POLICY_v0_2.json` as of its snapshot date. They are recorded
here so the policy document can eventually shed them.

| Entry | Role | Reference as recorded | Snapshot date | Deployment status |
| --- | --- | --- | --- | --- |
| DM-001 | Primary eligible local advisory | DeepSeek-V4.1-Flash (`deepseek-flash`) | 2026-10-06 | NOT DEPLOYED — reference only |
| DM-002 | Primary eligible local advisory | DeepSeek-V4-Pro (`deepseek-v4-pro`) | 2026-10-06 | NOT DEPLOYED — reference only |
| DM-003 | Local challenger / failover | Qwen3 open-weight family (local benchmark candidate) | 2026-10-06 | NOT DEPLOYED — reference only |
| DM-004 | Local challenger / failover | Qwen3.8 hosted family (optional current reference) | 2026-10-06 | NOT DEPLOYED — reference only |
| DM-005 | Optional external adversarial audit | GPT-5.6 Sol | 2026-10-06 | NOT DEPLOYED — reference only |

> **Unverified entries.** The rows above are transcribed from the routing policy
> artifact. They have **not** been independently verified against vendor
> documentation in this build, and no benchmark receipt exists for any of them at
> Node-001. They are recorded as **reference**, not as **measured**. Treat every
> version string as UNKNOWN-until-verified.

---

## 5. Required fields before any deployment

A pilot deployment entry is incomplete, and must not be commissioned, until all
of the following are recorded with a date and an owner:

| Field | Description | Status |
| --- | --- | --- |
| Exact checkpoint or model identifier | Immutable version string, not a marketing name | OUTSTANDING |
| Provider and hosting mode | Local, on-premises, or remote API | OUTSTANDING |
| Runtime and inference stack | Serving framework and version | OUTSTANDING |
| Hardware | Accelerator model, count, and memory | OUTSTANDING |
| Quantisation and precision | e.g. FP16, INT8, and the accuracy impact measured | OUTSTANDING |
| Context and output limits | As configured, not as advertised | OUTSTANDING |
| Prompt and template hashes | So an output can be tied to an input | OUTSTANDING |
| Data-boundary label | What data class this lane may see | OUTSTANDING |
| Latency and throughput measured | Against the stated SLA | OUTSTANDING |
| Energy per correct task | Measured, where measurable | OUTSTANDING |
| Benchmark receipt | Accuracy and false-negative rate on Node-001 task classes | OUTSTANDING |
| Failover tested | Challenger lane exercised under load | OUTSTANDING |
| Egress policy | Confirmed logged and policy-gated | OUTSTANDING |
| Redaction profile | Confirmed for any external lane | OUTSTANDING |

---

## 6. Data boundary (durable)

| Property | Value |
| --- | --- |
| OT network | Segmented |
| AI data plane | Read-only telemetry replica or approved broker |
| Remote model default data | Redacted, aggregated, non-secret |
| Raw OT data egress | **DENY BY DEFAULT** |
| Credentials in model context | **NEVER** |
| External calls | Logged and policy-gated |
| Compute plane failure | Must not prevent plant operation |

---

## 7. Operational logging contract

Every model interaction that could influence an operator decision must record:

| Field | Purpose |
| --- | --- |
| Timestamp | Ordering and audit |
| Task class | Routing and KPI attribution |
| Data-boundary label | Residency and egress compliance |
| Exact model / version / checkpoint | Reproducibility |
| Hardware or remote provider | Energy and latency attribution |
| Prompt / template hash | Input reproducibility |
| Input snapshot hash | Evidence of what the model actually saw |
| Tool calls | Action audit |
| Output hash | Output reproducibility |
| Latency | SLA |
| Energy if measurable | Efficiency KPI |
| Confidence / uncertainty | Calibration |
| Challenger result | Independent second opinion |
| Operator disposition | Acceptance rate and correctness |
| Downstream physical outcome, if any | Ground truth for correctness |

---

## 8. Workload routing rule (durable)

Deterministic or statistical methods are used wherever they are cheaper, faster
or more reliable than an LLM.

| Keep out of LLMs | LLMs may assist with |
| --- | --- |
| Mass balance | Maintenance-record synthesis |
| Energy balance | Fault explanation |
| Numerical optimisation | Complex diagnosis |
| Alarms | Planning |
| Hard constraints | Code and tool workflows |
| Basic forecasting | Semantic retrieval |
| Interlocks | Cross-domain synthesis |
|  | Operator explanation |

---

## 9. Change control

- A change of model version is a **manifest change**, not a constitutional change.
- A change of *role assignment* or of the *authority boundary* is a constitutional
  change and requires human-root adjudication.
- Any routing-share change requires benchmark receipts first.
- Vendor identity is never load-bearing for a physical action.
- If a model family becomes unavailable, the advisory plane degrades; the plant
  does not.
