# SWARM OPERATIONS SPEC

**Version:** v0.1  
**Status:** Operational design spec (candidate canon, not ratified)  
**Scope:** Repo governance and execution workflow for multi-agent swarm operations  
**Authority Boundary:** Human-root approval required for ratification/publication actions

## 1) Purpose and Goals

This document converts the repository's existing council/agent concepts into an auditable operating model.

Primary goals:
- Make swarm work assignable by lane and role.
- Make every handoff traceable with provenance and status.
- Preserve raw/candidate/canon boundaries.
- Enforce anti-self-ratification and human approval rules.
- Keep failure and recovery behavior explicit and non-erasing.

References:
- `/home/runner/work/manus-artifacts/manus-artifacts/synthesis_plan.md`
- `/home/runner/work/manus-artifacts/manus-artifacts/archive/architecture/LATTICE_AS_AGENT_HABITAT_LIFECYCLE_NOTE_2026-05-08.md`
- `/home/runner/work/manus-artifacts/manus-artifacts/archive/boot/seats/MANUSBRAIN_S6_EXECUTION_AGENT_SPEC_2026-05-08.md`
- `/home/runner/work/manus-artifacts/manus-artifacts/docs/unified-field-v4.0.md`

## 2) Operating Principles

1. **Human sovereignty:** no autonomous final authority.
2. **Zero erasure:** artifacts and incidents are preserved with lineage.
3. **Provenance first:** every claim maps to source evidence.
4. **Label integrity:** raw, draft, review, ratified, superseded states are explicit.
5. **No self-ratification:** creator and ratifier must differ.
6. **Mode discipline:** dream/play outputs cannot cause operational side effects.
7. **Auditability:** task state, transitions, and decisions are logged in repo artifacts.

## 3) Core Lanes and Role Contracts

### A. Orchestrator Lane
- **Mission:** intake, classify, route, and advance task packets through workflow states.
- **Inputs:** new requests, backlog items, blocked/resume signals, lifecycle mode state.
- **Outputs:** assigned packet, transition log, escalation notices, next-action queue.
- **Allowed actions:** create/update task packets; assign lanes; move packet states.
- **Forbidden actions:** direct ratification; bypassing approval gates; deleting incident records.
- **Escalation rules:** escalate to Safety lane on invariant ambiguity; escalate to human owner on approval-gated transitions.
- **KPIs:** assignment latency, blocked age, transition completeness.

### B. Evidence Lane
- **Mission:** gather sources, separate fact vs interpretation, score evidence confidence.
- **Inputs:** packet objective, source pointers, prior artifacts.
- **Outputs:** evidence bundle, provenance map, confidence notes, unresolved questions.
- **Allowed actions:** retrieve and summarize sources; attach citations and confidence flags.
- **Forbidden actions:** canon claims without reviewer signoff; source fabrication.
- **Escalation rules:** escalate missing/contradictory provenance to Safety and Orchestrator.
- **KPIs:** provenance completeness rate, citation defect rate.

### C. Safety / Constitution Lane
- **Mission:** enforce guardrails, invariants, and approval gates before promotion.
- **Inputs:** packet, evidence, proposed transitions, risk flags.
- **Outputs:** gate decision (allow/hold/block), guardrail notes, required approvals.
- **Allowed actions:** block unsafe transitions; require additional review; quarantine outputs.
- **Forbidden actions:** implementation edits disguised as review; self-approval loops.
- **Escalation rules:** escalate high-impact or unresolved constitutional conflict to human authority.
- **KPIs:** prevented unsafe transitions, false-pass rate, time-to-gate decision.

### D. Builder Lane
- **Mission:** produce implementation artifacts (docs/code/config/tests) per packet objective.
- **Inputs:** approved packet scope, constraints, evidence, acceptance criteria.
- **Outputs:** candidate artifact(s), change log, assumptions, risk notes.
- **Allowed actions:** produce scoped artifacts; update packet artifact paths and status.
- **Forbidden actions:** self-ratification; claiming completion without evidence/review.
- **Escalation rules:** escalate dependency or spec conflict to Orchestrator.
- **KPIs:** cycle time, first-pass review acceptance, rework rate.

### E. Review Lane
- **Mission:** adversarial quality check of builder outputs and packet integrity.
- **Inputs:** candidate artifacts, tests/check results, evidence bundle.
- **Outputs:** review verdict (pass/revise/reject), defects list, approval recommendation.
- **Allowed actions:** request revisions; verify constraints and evidence links.
- **Forbidden actions:** silent edits without trace; unilateral ratification.
- **Escalation rules:** unresolved disputes route to Council lane.
- **KPIs:** defect detection yield, post-ratification defect recurrence.

### F. Vault / Continuity Lane
- **Mission:** maintain continuity, lineage, failure ledger, and archival state.
- **Inputs:** final packet state, review records, incidents, decision logs.
- **Outputs:** archived packet, lineage links, continuity summary, ledger entries.
- **Allowed actions:** persist artifacts and metadata; preserve superseded lineage.
- **Forbidden actions:** history rewriting; deleting failed attempts.
- **Escalation rules:** escalate missing context or recovery failures to Orchestrator + human owner.
- **KPIs:** recovery success rate, archival completeness, unresolved continuity gaps.

## 4) Standard End-to-End Workflow

1. **Intake (Queued):** request converted into a typed task packet.
2. **Triage (Assigned):** Orchestrator sets lane ownership, priority, and constraints.
3. **Evidence Pass (Evidence):** source bundle and provenance metadata attached.
4. **Safety Gate 1 (Pre-Build):** constitutional checks before implementation.
5. **Build (Active):** Builder creates candidate artifacts.
6. **Review (Review):** independent review lane validates quality and constraints.
7. **Safety Gate 2 (Pre-Ratification):** final guardrail and approval checks.
8. **Ratification (Ratified):** only after human approval gate passes.
9. **Archive (Archived):** continuity lane records lineage, status, and closure.

## 5) Human Approval and Anti-Self-Ratification Rules

- Any item marked `approval_gate: human_required` cannot move to `ratified` without explicit human approval evidence.
- The same agent/lane cannot both **author** and **ratify** the same artifact.
- Council outputs are advisory until adjudicated and approved.
- Dream/play/reflection outputs cannot be published as canon.
- If reviewer and author identities are not distinct, packet status must remain `review` or `blocked`.

## 6) Status Labels

Recommended shared labels:
- `RAW`
- `DRAFT`
- `REVIEW_REQUIRED`
- `COUNCIL_OUTPUT`
- `RATIFIED`
- `SUPERSEDED`
- `QUARANTINED`

## 7) Audit Artifact Minimums

Each task must retain:
- task packet ID and status history
- source/provenance list
- decision and escalation log
- review outcomes and approver identity
- final artifact paths
- failure ledger linkage (if incident occurred)

## 8) Non-Claim Boundary

This spec defines governance and workflow expectations for repo operation. It does **not** claim that all automations are already implemented in runtime code.
