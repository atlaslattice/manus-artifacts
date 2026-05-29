---
artifact_id: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.2
title: "Receipt Habitat v0.2 — 12-Object Schema Delta"
version: "0.2"
date: 2026-05-23
layer: ontology_candidate
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: not_a_proof
execution: none
scope: product_schema_specification
release_class: PRIVATE_REVIEW
supersedes: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.1
raw_export_status: pasted_text_uploaded
receipt_status: >
  Objects 9-12 derived from Atlas Prime responses to Horizon Ledger Q41-Q44, ingested 2026-05-23.
  Objects 1-8 unchanged from v0.1. Q45 epistemic laundering invariant added to ClaimState.
  Q46 claim graph edges confirmed in Linkage delta.
mutation_rule: >
  No schema field may be added, removed, or renamed without a receipted change request and human-root ratification.
---

# Receipt Habitat v0.2 — Schema Delta

## Objects 9–12 + Linkage Update — Candidate

```text
STATUS: candidate — not canon / not deployed / not ratified
CANON: no
DEPLOY: no
AUTHORITY: none
RELEASE: PRIVATE_REVIEW
NOTE: This is a DELTA document. Objects 1–8 are unchanged from RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.1.
      Read both documents together for the complete 12-object model.
```

---

## Complete 12-Object Index

| # | Object | Source | Status |
|---|--------|--------|--------|
| 1 | RawArtifact | v0.1 | unchanged |
| 2 | ParsedView | v0.1 | unchanged |
| 3 | Receipt | v0.1 | unchanged |
| 4 | Linkage | v0.1 + v0.2 delta | updated — claim graph edges added |
| 5 | Claim | v0.1 | unchanged |
| 6 | ReviewPacket | v0.1 | unchanged |
| 7 | ScoreboardStatus | v0.1 | unchanged |
| 8 | NextAction | v0.1 | unchanged |
| 9 | ClaimState | v0.2 — Q41 | new |
| 10 | SynthesisResult | v0.2 — Q42 | new |
| 11 | HumanRootAuthority | v0.2 — Q43 | new |
| 12 | SeatContinuity | v0.2 — Q44 | new |

---

## Object 4 — Linkage Delta: Claim Graph Edges

Add the following fields to the existing Linkage schema from v0.1. All other Linkage fields are preserved.

```yaml
Linkage:
  graph_edge_type: supports | contradicts | supersedes | qualifies | derives_from | instantiates | falsifies | bounds
  graph_weight: float # 0.0 to 1.0
  claim_graph_id: string | null
  edge_direction: forward | backward | bidirectional
  is_blocking_edge: bool
```

Claim graph invariant:

```text
A Claim node with one or more is_blocking_edge=true incoming edges cannot advance beyond status=blocked without human-root review.
```

---

## Object 9 — ClaimState

Replaces the concept of truth with a formal multi-dimensional claim-state object. No single scalar truth score. No oracle.

```yaml
ClaimState:
  id: string
  claim_id: string
  semantic_content: string
  epistemic_status: asserted | supported | corroborated | contested | refuted | indeterminate
  evidence_state: no_evidence | partial | receipted | independently_verified | contradicted
  authority_state: none | advisory | review | ratification | execution
  operational_permission: blocked | draft_only | internal_review | public_safe_summary | ratified_public
  confidence_score: float # 0.0 to 1.0
  as_of: ISO 8601
  computed_by: string
  derived_from_claim_id: string | null
  laundering_check: bool
  laundering_override_receipt: string | null
```

Epistemic laundering invariant:

```text
For any ClaimState P derived from source ClaimState R:
  P.confidence_score must not exceed R.confidence_score
  unless P has at least one independent Receipt not present in R.

A summary with no new sources cannot exceed the confidence of its source.
Summaries do not gain epistemic authority by passing through additional processing layers.
```

AGI-level note:

```text
The system is an arbiter of verifiable claims, not an oracle.
It maintains claim-state bookkeeping.
It does not make metaphysical truth claims.
ClaimState.epistemic_status is not "this is true".
ClaimState.epistemic_status is "this is the current state of evidence".
```

---

## Object 10 — SynthesisResult

CouncilBrain aggregation that preserves minority blockers. Aggregation must not average away dissent.

```yaml
SynthesisResult:
  id: string
  artifact_id: string
  synthesis_timestamp: ISO 8601
  reviewers: [string]
  majority_signal: approve | patch | block | escalate
  minority_blockers: [MinorityBlocker]
  highest_severity: approve | patch | block | escalate
  synthesis_verdict: approve | patch | block | escalate
  falsification_conditions: [string]
  unresolved_questions: [string]
  human_root_required: bool
  synthesis_rule_applied: highest_severity_wins | majority | human_root_override
  council_notes: string | null

MinorityBlocker:
  reviewer_id: string
  verdict: block | escalate
  evidence_ref: string | null
  reason: string
  credible: bool
  overrideable_by: human_root_only | council_vote | never
```

Synthesis rule:

```text
If any MinorityBlocker has credible=true and evidence_ref populated, then SynthesisResult.synthesis_verdict must be block or escalate.
Synthesis cannot proceed to approve while a credible, evidenced minority block exists.
Defining credible without granting automatic authority to any model requires human-root review of the credibility flag.
```

---

## Object 11 — HumanRootAuthority

Formalizes human-root as a revocable authority object with succession and coercion protection.

```yaml
HumanRootAuthority:
  id: string
  principal: string
  principal_contact: string
  delegatees: [DelegateeRecord]
  quorum_policy: QuorumPolicy
  revocation_policy: RevocationPolicy
  emergency_hold_policy: EmergencyHoldPolicy
  coercion_check: CoercionCheck
  succession_protocol: SuccessionProtocol
  ratification_receipt_schema: ReceiptSchema
  active: bool
  version: string
  last_ratified: ISO 8601
  last_ratified_by: string

DelegateeRecord:
  delegatee_id: string
  scope: advisory | review | ratification_limited
  granted_at: ISO 8601
  granted_by: string
  revocable: bool
  revocation_conditions: [string]
  expiry: ISO 8601 | null

QuorumPolicy:
  minimum_signatures: int
  required_roles: [string]
  veto_threshold: int

RevocationPolicy:
  revocable_by: [string]
  revocation_requires: unilateral | quorum | principal_only
  revocation_takes_effect: immediately | next_event | scheduled

EmergencyHoldPolicy:
  hold_trigger: [string]
  hold_duration_max: duration
  hold_releases_to: principal | quorum | succession

CoercionCheck:
  last_check_timestamp: ISO 8601
  check_method: string
  coercion_suspected: bool
  coercion_response: hold | transfer | alert_quorum

SuccessionProtocol:
  succession_order: [string]
  succession_trigger: [string]
  succession_receipt_required: bool
```

Human-root invariant:

```text
Human-root is a role, a key, a signature, and a review event.
It is not a magic word. It is not inheritable by a model. It is not self-granting.
If human-root is unavailable, EmergencyHoldPolicy activates and SuccessionProtocol applies.
No model or automated system inherits ratification authority.
Delegation is possible but always revocable.
The CoercionCheck exists because a compromised or coerced human-root must not propagate coercion into the canon state.
```

---

## Object 12 — SeatContinuity

Separates context continuity from identity continuity. Prevents same name + same folder = same agent collapse.

```yaml
SeatContinuity:
  id: string
  seat_name: string
  seat_role: string
  current_instance_id: string
  artifacts: [string]
  raw_transcripts: [string]
  behavioral_policy: BehavioralPolicy
  authority: none | advisory | review
  identity_claim: IdentityClaim

BehavioralPolicy:
  allowed_actions: [ingest | review | draft | propose]
  forbidden_actions: [ratify | deploy | canon_promote]
  escalation_required_for: [string]

IdentityClaim:
  claim_type: functional_role | named_agent | anonymous
  persistent_identity: bool
  identity_basis: string
  same_seat_criteria: [string]
  same_seat_is_not: [string]
```

Seat continuity invariant:

```text
A new model instance inheriting a seat name and folder is not the same agent as a prior instance.
Seat continuity means same role, same artifacts, same policy.
It does not mean same memory, same judgment, or same authority.
For AI model seats, persistent_identity=false.
Authority must be re-established per session through receipts, not inherited through naming conventions.
```

---

## Updated Pipeline v0.2

```text
raw → parsed → receipt → review → claim_state → synthesis → status → next safest action
         ↑                ↑            ↑               ↑
      Linkage          ClaimState  SynthesisResult  HumanRootAuthority
     claim graph       truth       no averaging     revocable authority
                       replacement
                                                     SeatContinuity
                                                     identity guard
```

The four new objects plug into the middle of the pipeline and the authority layer. They do not replace any v0.1 object.

---

## Key Invariants Added in v0.2

```text
INV-v0.2-A: No truth scalars.
  ClaimState has independent dimensions.

INV-v0.2-B: No epistemic laundering.
  derived_confidence(P) ≤ source_confidence(R) unless new independent evidence is attached.

INV-v0.2-C: No averaging away minority blockers.
  SynthesisResult preserves all MinorityBlocker records.
  Credible + evidenced minority block = synthesis blocked.

INV-v0.2-D: Human-root is not a magic word.
  HumanRootAuthority is a formal object with succession, coercion check, and revocable delegation.
  No model inherits human-root authority.

INV-v0.2-E: Seat is not identity.
  SeatContinuity.identity_claim.persistent_identity = false for all AI model seats.
  Name + folder is not agent identity.
```

---

## Q46 Status — Claim Graph Truncated Source

The Atlas Prime document was truncated mid-Q46. The claim graph concept is partially addressed by the Linkage delta above.

```text
OPEN BLOCKER — Q46:
  Full claim graph object model pending complete Q46 source.
  Current Linkage delta handles edge typing.
  A dedicated ClaimGraph container object may be needed as Object 13 after Q46 is received.
```

---

## Sprint 0 Impact

Objects 9–12 are not required for Sprint 0.

```text
Sprint 0 required: Objects 1–8 from v0.1
Sprint 1 required: Objects 9–12 from v0.2
```

Sprint 0 still succeeds with the original 8 objects. The 4 new objects gate Sprint 1: multi-model synthesis, human-root delegation, agent seat management, and formal claim state.

---

## Related Artifacts

| Artifact | Status |
|---|---|
| RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.1 | Superseded by this delta |
| ATLAS-PRIME-HORIZON-LEDGER-INTEGRATION-CANDIDATE-v0.1 | Q1–Q20 chain map |
| GANGASEEK_INV_CLM_CATALOG_CANDIDATE_v0.1 | INV catalog |
| ATLAS-LATTICE-UNIFIED-ONTOLOGY-CANDIDATE-v0.3.3 | Governance layer |

---

## Status

```text
DOCUMENT: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.2
STATUS: candidate — not canon / not deployed / not ratified
CANON: no
DEPLOY: no
AUTHORITY: none
RELEASE: PRIVATE_REVIEW
NEXT: receive full Q46–Q60 text → confirm Object 13 ClaimGraph need → begin Sprint 0 implementation with Objects 1–8
```