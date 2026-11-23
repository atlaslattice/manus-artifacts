---
artifact_id: AETHERFORGE-QUEST-PACKET-TEMPLATE-v0.1-2026-05-25
title: Aetherforge Quest Packet Template v0.1
status: candidate_template
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: not_a_proof
---

# Aetherforge Quest Packet Template v0.1

```text
STATUS: CANDIDATE QUEST TEMPLATE — NOT CANON
CANON: NO
DEPLOYMENT: NO
AUTHORITY: NONE
PROOF: NO
```

Use this template for playable archive-hardening tasks.

```yaml
quest_id: null
title: null
quest_type: null
status: candidate_quest
canon_status: not_canon
deployment_status: inert
authority_scope: none
proof_status: not_a_proof
source:
  source_surface: notion | drive | github | gamma | website | swarm | pasted_text | unknown
  source_locator: null
  source_title: null
  raw_export_status: unavailable | pending | attached | hashed | verified | partial | not_supported
  source_hash: null
risk:
  risk_level: low | medium | high | critical
  contamination_flags: []
  overclaims_to_avoid: []
classification:
  artifact_type: raw | proxy | candidate | dream_play | simulation | governance | presentation | code | transcript | unknown
  epistemic_label: verifiable | design_choice | creative_overlay | not_verified | mixed
  review_state: unreviewed | quarantined | indexed | reviewed | promoted | rejected | superseded
routing:
  primary_lane: GPTBrain | AtlasBrain | CouncilBrain | Hashlight | Lucerna | TIDELOCK | Rootglass | Human-root
  secondary_lanes: []
  required_reviewers: []
receipts:
  receipt_requests: []
  attached_receipts: []
play:
  player_role: null
  boss_or_hazard: null
  win_condition: null
  reward_type: null
extraction:
  useful_delta: null
  safe_rewrite: null
  proposed_github_issue: null
  proposed_next_action: null
keeper_line: null
```

## Required sections

### 1. Source context

What artifact is being played?

### 2. Why this is a quest

What risk, mess, opportunity, or delta makes it playable?

### 3. Failure modes

What could go wrong if this artifact is trusted too quickly?

### 4. Receipts required

What evidence is needed before any stronger claim can be made?

### 5. Safe delta

What useful improvement can be extracted without promoting the artifact?

### 6. Routing

Which lane receives it next?

### 7. Keeper

One sentence that preserves the boundary.

## Keeper

```text
The artifact may become useful before it becomes true.
```