# Archivist Trust Failure Protocol

Status: candidate staging material  
Canon: no  
Deployment: no  
Authority: none  

## Purpose

Define how to handle archivist or model contamination events without deleting
evidence. Preservation is the first rule; quarantine is the second; deletion
is not an option.

## What is an archivist trust failure?

An archivist trust failure occurs when:

- A model-origin artifact is treated as authoritative without a receipt
- A governance claim is sourced from model output rather than human decision
- A summary export is passed as a full raw export
- Attribution is laundered across synthesis layers
- A Claude-origin artifact influences authority-tier decisions
- An agent claims canon or deployment status without human-root approval

## Response protocol

### Step 1 — Preserve

Do not delete the artifact.  
Do not overwrite the artifact.  
Do not alter the artifact's content in place.

Add a contamination flag header or sidecar file.  
Record the detection timestamp and detection agent.

### Step 2 — Quarantine

Move or flag the artifact with `contamination_status: quarantined`.

Use the sidecar filename pattern:
```text
{ARTIFACT_ID}.CONTAMINATION_SIDECAR.yaml
```

Sidecar format:

```yaml
artifact_id: ARTIFACT_SLUG
contamination_status: quarantined
detected_by: <child_name or agent>
detection_timestamp: YYYY-MM-DDTHH:MM:SSZ
contamination_type:
  - one_of: [claude_origin_governance, attribution_laundering, summary_as_raw,
              model_output_as_authority, canon_claim_without_receipt,
              deployment_claim_without_receipt, identity_sprawl]
affected_claims: []
review_required: true
authority_scope: advisory_only
canon_status: not_canon
next_action: route_to_adversarial_review
```

### Step 3 — Route

Route the quarantined artifact to adversarial review:

- Grok: contamination type analysis, claim extraction
- TIDELOCK: GitHub path truth, commit chain
- Rootglass: canon boundary, room-state mapping
- HumanRoot: final determination only

### Step 4 — Record delta

After review, record the review delta in the receipt spine:

```yaml
delta_type: trust_failure_resolved
artifact_id: ARTIFACT_SLUG
resolution: <retained_with_flags | revised | withdrawn_with_note>
reviewer: <child_name or handle>
reviewed_at: YYYY-MM-DDTHH:MM:SSZ
```

## What contamination is NOT

Contamination is not proof of bad intent.  
Contamination is not a reason to delete.  
Contamination does not cancel the artifact's archive value.  
Contamination means the artifact needs review before authority use.

## Keeper

Preserve everything.  
Quarantine is not deletion.  
The sidecar carries the flag; the artifact carries the evidence.  
Human-root decides what survives adversarial review.
