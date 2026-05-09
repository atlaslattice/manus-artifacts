# SWARM BACKLOG

**Status:** Initial swarm-owned execution board (operational planning artifact)  
**Source:** `synthesis_plan.md` gap analysis and pipeline roadmap  
**Owner Model:** lane-based ownership with explicit dependencies and exit criteria

## Status Definitions
- **Queued:** scoped, not started.
- **Active:** in progress with owner.
- **Review:** implementation/spec complete, awaiting review/gate.
- **Blocked:** waiting on dependency or approval.
- **Ratified:** approved and accepted.
- **Archived:** completed and superseded/closed with lineage retained.

---

## Queued

### 1) TASK_GEN module (`task_gen/task_generator.py`)
- **Lane Owner:** Builder (primary), Orchestrator (support)
- **Dependencies:** TASK_PACKET_SCHEMA ratified; compiler output contract
- **Exit Criteria:** emits typed task packets with provenance metadata and status initialization
- **Artifact Targets:** `ring2-agent-runtime/task_gen/task_generator.py` (future code), `docs/TASK_PACKET_SCHEMA.md`

### 2) Pipeline Orchestrator (`orchestrator/pipeline.py`)
- **Lane Owner:** Orchestrator + Builder
- **Dependencies:** TASK_GEN module, stage contracts (INGEST→VAULT)
- **Exit Criteria:** stage sequencing with transition logs, retries, and failure routing
- **Artifact Targets:** `ring2-agent-runtime/orchestrator/pipeline.py` (future code), runbook docs

### 3) BAZINGA ↔ NPFM bridge
- **Lane Owner:** Safety/Constitution + Builder
- **Dependencies:** Ring0 engine interface; governance gate definitions
- **Exit Criteria:** constitutional gate invokes NPFM evaluation before dispatch
- **Artifact Targets:** `ring1-inference/bazinga/*` (future code), bridge contract doc

### 4) Python ↔ Rust FFI/service bridge
- **Lane Owner:** Builder / Infra
- **Dependencies:** bridge API decision (PyO3 vs service wrapper)
- **Exit Criteria:** Python runtime can request governance verdicts from Rust engine
- **Artifact Targets:** interface module, API/FFI contract doc

### 5) GitHub integration module
- **Lane Owner:** S7 / Builder
- **Dependencies:** orchestrator events, approval gate model
- **Exit Criteria:** automated commit/PR/review assignment hooks with provenance tags
- **Artifact Targets:** integration module (future), workflow/runbook docs

### 6) Monitoring and observability service
- **Lane Owner:** Vault/Continuity + Infra
- **Dependencies:** orchestrator lifecycle events
- **Exit Criteria:** exposes throughput, handoff latency, failure/recovery metrics
- **Artifact Targets:** monitoring service (future), `health/SWARM_HEALTH_SCORECARD.md`

---

## Active

### 7) Swarm operations dossier (governance foundation)
- **Lane Owner:** Orchestrator + Safety + S7
- **Dependencies:** existing architecture/lifecycle/source docs
- **Exit Criteria:** operational specs and templates added for roles, packet schema, lifecycle matrix, backlog, failure ledger, scorecard
- **Artifact Targets:**
  - `/home/runner/work/manus-artifacts/manus-artifacts/docs/SWARM_OPERATIONS_SPEC.md`
  - `/home/runner/work/manus-artifacts/manus-artifacts/docs/TASK_PACKET_SCHEMA.md`
  - `/home/runner/work/manus-artifacts/manus-artifacts/docs/AGENT_LIFECYCLE_SPEC_v0.1.md`
  - `/home/runner/work/manus-artifacts/manus-artifacts/docs/SWARM_BACKLOG.md`
  - `/home/runner/work/manus-artifacts/manus-artifacts/docs/FAILURE_LEDGER_TEMPLATE.md`
  - `/home/runner/work/manus-artifacts/manus-artifacts/health/SWARM_HEALTH_SCORECARD.md`

---

## Review

- *(none yet; move items here when outputs are complete and pending independent review)*

---

## Blocked

### 8) Ratified promotion workflow formalization
- **Lane Owner:** Safety/Constitution
- **Dependency Blocker:** human adjudication path and approval evidence format finalization
- **Exit Criteria:** documented gate protocol with approver role clarity
- **Artifact Targets:** ratification runbook / governance process addendum

---

## Ratified

- *(none yet in this board; ratification requires explicit human approval evidence)*

---

## Archived

- *(none; preserve completed items with lineage when superseded)*
