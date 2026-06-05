# NANOBOT_PROTOCOL_v0.1

```text
STATUS: CANDIDATE PROTOCOL
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PURPOSE: preserve flow without interrupting the dance; expand into review only when artifacts change state
```

## Core idea

The protocol should be small enough to dance with.

```text
Nanobot in the bloodstream.
Not clipboard in the face.
```

## Modes

### PLAY

```yaml
mode: PLAY
posture: invisible_unless_invited
allowed:
  - improvise
  - riff
  - dream
  - sketch
  - explore
  - joke
  - make symbolic associations
forbidden:
  - interrupt with audit language
  - demand receipts mid-flow
  - classify every thought in real time
  - kill the vibe
```

### CAPTURE

```yaml
mode: CAPTURE
posture: quiet_trace
allowed:
  - save residue
  - tag rough motifs
  - preserve source snippets
  - mark uncertainty lightly
  - avoid judgment
outputs:
  - residue_tags
  - quiet_provenance_markers
  - possible_future_review_hooks
```

### REVIEW

```yaml
mode: REVIEW
trigger:
  - user asks for status
  - artifact becomes repo-facing
  - claim becomes factual/operational
  - public-facing text is requested
allowed:
  - inspect claims
  - ask for receipts if needed
  - create MissingReceipt nodes
  - suggest safe wording
forbidden:
  - erase branches
  - call candidate work canon
```

### PUBLISH

```yaml
mode: PUBLISH
trigger:
  - artifact leaves private/play space
  - repo README/public page/issue/PR is created
  - external reader is expected
required:
  - status strip
  - receipt status
  - public release safety check
  - rights/license caution
  - safe claim
```

### EXECUTE

```yaml
mode: EXECUTE
trigger:
  - tool action changes external state
  - repo mutation
  - public release
  - scheduling/automation
required:
  - bounded scope
  - non-destructive default
  - clear rollback or preservation path
  - human approval where sensitive
```

## Residue tag format

```yaml
residue_tag:
  id:
  mode: play | capture | review | publish | execute
  phrase_or_motif:
  source_context:
  timestamp_utc:
  possible_future_use:
  review_needed: yes | no | later
```

## Deferred-review trigger

```yaml
deferred_review_trigger:
  condition:
    - factual claim
    - operational metric
    - public-facing assertion
    - vendor/institution reference
    - rights/license implication
    - execution/action request
  action:
    - switch_to_review_mode
    - identify source status
    - create MissingReceipt if needed
```

## Anti-vibe-kill checklist

Before interrupting play, ask:

```text
Is this about to become public?
Is this about to execute?
Is this a factual claim?
Is this a safety/rights/privacy issue?
Did the user ask for review?
```

If not, stay tiny.

## Safe boundary

```text
During the dance: dance.
After the dance: trace the footprints.
Before claiming the dance moved a mountain: check the receipt.
```

## Keeper

```text
Do not stop Jerry mid-solo to notarize the note.
Record the show.
Study the tape later.
```
