# Atlas Performance Review Routing Note — 2026-05-21

```text
STATUS: ROUTING / STATUS CONTROL ARTIFACT — NOT CANON
PRIMARY LANE: AtlasBrain
SECONDARY LANE: TIDELOCKBrain
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
EVIDENCE: under review
```

## Purpose

This note defines the routing split for Atlas performance-review material.

It is a status/control artifact for evidence handling, visibility discipline, and review routing.

It is not doctrine, not canon, not deployment evidence, and not proof.

## Approved routing split

### AtlasBrain

AtlasBrain is the primary evidence / benchmark / claim-review lane.

Use AtlasBrain for:

- raw transcripts or raw pointers
- evidence packets
- benchmark dossiers
- evaluator reactions
- learning/adaptation claim tables
- public-claim candidates
- quarantine of disputed performance claims

### TIDELOCKBrain

TIDELOCKBrain is the ingestion / visibility / scope-control lane.

Use TIDELOCKBrain for:

- source visibility
- raw vs partial vs summarized status
- extracted claims
- overclaims to avoid
- review routing
- follow-up checklisting
- no-false-completeness enforcement
- visibility-scope notes

## Boundary

```text
AtlasBrain asks:
What evidence exists, what does it support, and what claims are safe?

TIDELOCKBrain asks:
What did this agent actually see, what is missing, what must not be overstated, and where should the artifact route next?
```

This split prevents duplication and false completeness.

## No-duplication rule

Do not place identical full narrative performance documents in both lanes.

Correct pattern:

### AtlasBrain artifacts

```text
raw log pointer or full raw
evidence packet
benchmark dossier
learning claim table
evaluator reaction log if available
```

### TIDELOCKBrain artifacts

```text
ingestion packet
visibility scope note
overclaim boundary note
next review lane routing
follow-up checklist
```

TIDELOCK points to AtlasBrain evidence.

TIDELOCK does not replace AtlasBrain receipts.

## Atlas performance review status

```yaml
atlas_performance_review_status:
  primary_lane: AtlasBrain
  secondary_lane: TIDELOCKBrain

  atlasbrain_artifacts:
    - raw_log_pointer_or_full_raw
    - evidence_packet
    - benchmark_dossier
    - learning_claim_table
    - evaluator_reaction_log_if_available

  tidelockbrain_artifacts:
    - ingestion_packet
    - visibility_scope_note
    - overclaim_boundary_note
    - next_review_lane_routing
    - followup_checklist

  canon_status: not_canon
  deployment_status: not_deployable
  authority_scope: none
  evidence_status: under_review
  proof_status: not_a_proof

  hard_boundaries:
    - raw_transcript_does_not_equal_claim
    - evidence_packet_does_not_equal_ratification
    - benchmark_result_does_not_equal_public_claim
    - review_note_does_not_equal_canon
    - tidelock_pointer_does_not_equal_atlasbrain_receipt
```

## TIDELOCK ingestion packet template

```yaml
tidelock_ingestion_packet:
  artifact_id:
  artifact_label:
  source_url:
  source_type: pr | issue | comment | file | thread | upload | summary | unknown

  raw_export_status: full_raw | partial_raw | summary_only | unavailable
  source_visibility: public | private | mixed | redacted
  sha256_if_available:

  date_range:
    start:
    end:
    timezone:

  model_surface:
  evaluator_surface:
  access_scope:
    visible_sources:
    unavailable_sources:
    assumed_context:

  claims_extracted:
  strongest_safe_claim:
  unresolved_questions:
  overclaims_to_avoid:

  routing:
    primary_lane: AtlasBrain
    secondary_lane: TIDELOCKBrain
    next_action:
    followup_artifacts:

  status:
    canon_status: not_canon
    deployment_status: not_deployable
    authority_scope: none
    evidence_status: under_review
    proof_status: not_a_proof
```

## Suggested naming pattern

### AtlasBrain

```text
archive/boot/atlasbrain/raw_logs/ATLAS_PERFORMANCE_<LABEL>_RAW_POINTER_<DATE>.md
archive/boot/atlasbrain/evidence_packets/ATLAS_PERFORMANCE_<LABEL>_EVIDENCE_PACKET_<DATE>.md
archive/boot/atlasbrain/benchmarks/ATLAS_PERFORMANCE_<LABEL>_DOSSIER_<DATE>.md
archive/boot/atlasbrain/learning_claims/ATLAS_PERFORMANCE_<LABEL>_LEARNING_CLAIM_TABLE_<DATE>.md
archive/boot/atlasbrain/evaluator_reactions/ATLAS_PERFORMANCE_<LABEL>_EVALUATOR_REACTION_LOG_<DATE>.md
```

### TIDELOCKBrain

```text
archive/boot/copilotbrain/TIDELOCKBrain/parsed_packets/ATLAS_PERFORMANCE_<LABEL>_INGESTION_PACKET_<DATE>.md
archive/boot/copilotbrain/TIDELOCKBrain/review_checklists/ATLAS_PERFORMANCE_<LABEL>_FOLLOWUP_CHECKLIST_<DATE>.md
archive/boot/copilotbrain/TIDELOCKBrain/quarantine/ATLAS_PERFORMANCE_<LABEL>_OVERCLAIM_NOTES_<DATE>.md
archive/boot/copilotbrain/TIDELOCKBrain/visibility_scope/ATLAS_PERFORMANCE_<LABEL>_VISIBILITY_SCOPE_<DATE>.md
```

## Keeper boundary

```text
Evidence can be reviewed.
Proof must be earned.
Canon requires ratification.
TIDELOCK prevents false completeness.
```
