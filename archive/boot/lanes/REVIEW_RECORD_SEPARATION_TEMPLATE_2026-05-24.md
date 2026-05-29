---
artifact_id: REVIEW-RECORD-SEPARATION-TEMPLATE-2026-05-24
title: "Review Record Separation Template"
date: 2026-05-24
lane: cross_lane_review_standard
status: candidate_artifact
release_class: PRIVATE_REVIEW
created_by: "GPT / Varix Lumenfoss"
---

# Review Record Separation Template

## Purpose

Use this format when writing review, audit, cleanup, intake, or readiness notes.

The goal is to keep five kinds of information separate:

```text
1. Presence
2. Status
3. Provenance
4. Interpretation
5. Limits
```

## Presence

Record only whether the checked item exists at the checked location.

Examples:

```text
file exists on master
issue exists
PR exists
folder exists
```

## Status

Record only the current checked state.

Examples:

```text
open
draft
candidate_review
none
```

## Provenance

Record identifiers and source trace details.

Examples:

```text
blob SHA
claimed commit SHA
issue number
PR number
source hash
verification date
```

If commit history was not checked, say so.

## Interpretation

Record the safe meaning or operational reading.

Examples:

```text
materially corroborated
mostly cleared
monitor
readiness requires recheck
```

## Limits

Always include a short limits section.

Examples:

```text
presence is not approval
pointer needs signoff before promotion
synthesis is not final by itself
```

## Formatting Rule

Do not treat a claimed commit SHA as current content identity unless Git history was checked.

If only a file listing was checked, use:

```text
present on master
current content identifier observed
claimed commit SHA pending history check
```

## Verification Stamp

```yaml
verification_scope: presence | status | provenance | interpretation
verified_against_branch: master
verified_on: 2026-05-24
```

## Minimal Template

```markdown
# Review Note

## Presence
- checked_target:
- present:
- location:

## Status
- current_state:
- review_status:

## Provenance
- verified_against_branch:
- verified_on:
- content_sha:
- claimed_commit_sha:
- commit_history_checked:
- source_hash:

## Interpretation
- safe_synthesis:
- blocker_disposition:
- next_safest_action:

## Limits
- presence_is_not_approval: true
- promotion_requires_signoff: true
```

## Keeper

```text
State is not provenance.
Presence is not approval.
Interpretation is not authority.
```
