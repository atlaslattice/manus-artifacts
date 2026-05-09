# TASK PACKET SCHEMA

**Version:** v0.1  
**Status:** Canonical handoff schema proposal (operational template; not runtime-enforced yet)

## 1) Purpose

Define one typed packet format for all swarm handoffs so work is auditable, assignable, and resumable.

## 2) Canonical Packet Fields

Required fields:
- `task_id` (string): globally unique ID (e.g., `SWARM-2026-05-09-001`)
- `title` (string): concise task name
- `objective` (string): measurable intended outcome
- `mode` (enum): `sleep | dream | play | reflection | work | recovery | council`
- `priority` (enum): `p0 | p1 | p2 | p3`
- `requested_by` (string): initiator identity
- `sources` (array): source references with path/url/hash
- `constraints` (array): scope, policy, or technical constraints
- `assigned_agent` (string): current owner
- `required_reviewers` (array): reviewer identities/lanes
- `approval_gate` (object): gate type and required approver class
- `status` (enum): `queued | assigned | active | review | blocked | ratified | archived | quarantined`
- `next_action` (string): explicit next executable step
- `artifact_paths` (array): output file paths tied to this task
- `evidence` (array): evidence entries with confidence and citation
- `risk_flags` (array): flagged risks/invariant concerns
- `provenance` (object): lineage metadata (created_at, updated_at, source_commit, parent_task)

Recommended supplemental fields:
- `depends_on` (array of task IDs)
- `handoff_log` (array of state transitions)
- `notes` (string)

## 3) JSON Type Template

```json
{
  "task_id": "string",
  "title": "string",
  "objective": "string",
  "mode": "sleep|dream|play|reflection|work|recovery|council",
  "priority": "p0|p1|p2|p3",
  "requested_by": "string",
  "sources": [
    {
      "kind": "repo_path|url|issue|pr|log",
      "ref": "string",
      "hash": "string"
    }
  ],
  "constraints": ["string"],
  "assigned_agent": "string",
  "required_reviewers": ["string"],
  "approval_gate": {
    "type": "none|human_required|constitutional_review_required",
    "approver": "string"
  },
  "status": "queued|assigned|active|review|blocked|ratified|archived|quarantined",
  "next_action": "string",
  "artifact_paths": ["string"],
  "evidence": [
    {
      "claim": "string",
      "citation": "string",
      "confidence": "low|medium|high"
    }
  ],
  "risk_flags": ["string"],
  "provenance": {
    "created_at": "ISO-8601",
    "updated_at": "ISO-8601",
    "source_commit": "string",
    "parent_task": "string|null"
  },
  "depends_on": ["string"],
  "handoff_log": [
    {
      "from_status": "string",
      "to_status": "string",
      "by": "string",
      "at": "ISO-8601",
      "reason": "string"
    }
  ],
  "notes": "string"
}
```

## 4) Example Packet (YAML)

```yaml
task_id: SWARM-2026-05-09-001
title: Draft swarm governance dossier
objective: Add repo-ready governance and execution docs for swarm operation
mode: work
priority: p0
requested_by: human/s10
sources:
  - kind: repo_path
    ref: /home/runner/work/manus-artifacts/manus-artifacts/synthesis_plan.md
    hash: git:HEAD
  - kind: repo_path
    ref: /home/runner/work/manus-artifacts/manus-artifacts/archive/architecture/LATTICE_AS_AGENT_HABITAT_LIFECYCLE_NOTE_2026-05-08.md
    hash: git:HEAD
constraints:
  - Preserve constitutional language and anti-self-ratification
  - Do not overclaim runtime implementation state
assigned_agent: s7-copilot-builder
required_reviewers:
  - s2-constitution-review
  - human-approver
approval_gate:
  type: human_required
  approver: human/s10
status: review
next_action: Request constitutional review and human ratification decision
artifact_paths:
  - /home/runner/work/manus-artifacts/manus-artifacts/docs/SWARM_OPERATIONS_SPEC.md
  - /home/runner/work/manus-artifacts/manus-artifacts/docs/TASK_PACKET_SCHEMA.md
evidence:
  - claim: Pipeline stages and missing glue modules are defined
    citation: /home/runner/work/manus-artifacts/manus-artifacts/synthesis_plan.md
    confidence: high
risk_flags:
  - governance_drift
  - self_ratification_if_unreviewed
provenance:
  created_at: "2026-05-09T10:32:00Z"
  updated_at: "2026-05-09T10:55:00Z"
  source_commit: HEAD
  parent_task: null
depends_on: []
handoff_log:
  - from_status: queued
    to_status: active
    by: orchestrator
    at: "2026-05-09T10:40:00Z"
    reason: Intake accepted and scoped
  - from_status: active
    to_status: review
    by: builder
    at: "2026-05-09T10:55:00Z"
    reason: Draft artifacts complete; awaiting review
notes: Candidate packet for initial swarm governance dossier.
```

## 5) Packet State Movement Rules

Expected movement:
- `queued -> assigned -> active -> review -> ratified -> archived`

Alternative branches:
- `active -> blocked` when dependencies or constraints fail.
- `review -> active` when revisions are requested.
- `review -> quarantined` when invariant or provenance violations are found.
- `blocked -> recovery` mode handling, then return to `assigned` or `active`.

Agent movement constraints:
- Orchestrator owns `queued/assigned` transitions.
- Builder owns `active` updates but cannot finalize `ratified`.
- Review/Safety lanes control `review/block/quarantine` decisions.
- Human approver is required for `ratified` when gate requires human.
- Vault/Continuity closes to `archived` after ratification and lineage capture.

## 6) Non-Claim Boundary

This schema is the canonical handoff contract for swarm governance in this repository. It is currently a specification and template, not proof of full runtime enforcement.
