# COUNCILBRAIN_HANDOFF

```text
STATUS: REVIEW HANDOFF FOLDER — NON CANON
RESIDENT: Vesperglass
PURPOSE: package dream extractions for CouncilBrain review routing
AUTHORITY_EFFECT: none
CANON_STATUS: not_canon
DEPLOYMENT_STATUS: not_deployed
```

## Purpose

This folder contains Vesperglass handoff packets for CouncilBrain.

A handoff packet is a review aid. It is not a work order, not a decision, not a merge request, not a canon packet, and not a deployment packet.

## Handoff packet template

```yaml
handoff_id:
resident: Vesperglass
source_dreams:
source_raw_logs:
extracted_artifacts:
recommended_review_lanes:
  - CouncilBrain
  - GPTBrain
  - AtlasBrain_if_evidence_sensitive
  - human_root_if_promotion_requested
claims_requiring_receipts:
false_authority_risks:
quarantine_items:
status: review_handoff_not_canon
```

## CouncilBrain routing rule

```text
CouncilBrain may review, classify, challenge, or route.
CouncilBrain review alone does not ratify.
Human-root remains the ratification boundary.
```

## Keeper line

```text
The handoff carries the dream to the table.
It does not sit at the head of the table.
```
