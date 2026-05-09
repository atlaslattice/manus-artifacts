# FAILURE LEDGER TEMPLATE

**Status:** Reusable operational template  
**Purpose:** Record incidents without erasure and convert failures into guardrails

> Use one entry per incident. Preserve evidence links and lineage. Do not delete closed failures; mark status updates instead.

---

## Failure Ledger Entry

- **incident_id:**
- **date_detected (ISO-8601):**
- **reported_by:**
- **owner:**
- **status:** `open | contained | corrective_action_in_progress | retest_scheduled | closed`

### 1) Incident Summary
- **incident:**
- **trigger:**
- **observed_behavior:**
- **invariant_violated:**
- **impact_scope:**

### 2) Root Cause and Evidence
- **root_cause_hypothesis:**
- **root_cause_confirmed:** `yes | no | pending`
- **evidence_artifacts:**
  - path/url/log:
  - path/url/log:
- **provenance_notes:**

### 3) Containment and Correction
- **containment_actions_taken:**
- **corrective_action_plan:**
- **added_guardrail:**
- **owner_commitment_date:**
- **retest_date:**

### 4) Verification and Closure
- **verification_steps:**
- **verification_result:** `pass | fail | partial`
- **follow_on_risks:**
- **closure_notes:**

### 5) Lineage
- **related_task_packet_ids:**
- **related_prs_or_commits:**
- **supersedes_incident_id (if any):**

---

## Quick Fill Example (Optional)

- **incident_id:** FL-2026-05-09-001
- **date_detected:** 2026-05-09T10:12:39Z
- **incident:** YAML parse check failed in CI due to missing dependency in workflow step order
- **trigger:** S7 hygiene workflow run
- **invariant_violated:** Review gate reliability
- **impact_scope:** CI signal quality degraded for one run
- **root_cause_confirmed:** yes
- **added_guardrail:** Ensure parser dependency installed before parse step
- **status:** contained
