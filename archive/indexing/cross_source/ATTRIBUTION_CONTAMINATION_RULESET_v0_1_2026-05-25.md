# Attribution Contamination Ruleset v0.1

```text
STATUS: CANDIDATE RULESET — NOT CANON
DEPLOYMENT: NONE
AUTHORITY: NONE
PURPOSE: prevent false model authorship, especially Claude byline contamination, from entering clean registry fields
```

## Source hierarchy

```text
Website = canon surface.
GitHub = workspace / receipts / issues / PRs / candidate deltas.
Notion = former canon surface, now historical substrate / extraction backlog.
Drive = attempted vault/candidate store, now historical substrate / extraction backlog.
Chat transcripts = tape / source material / non-canon.
```

## Core rule

```text
Model byline is not provenance.
Drafting is not authorship.
Formatting is not invention.
Compilation is not canon.
Website ratification controls canon status.
```

## FM-ATTRIBUTION-001 — Claude Author Attribution Contamination

Failure description:

```text
A document generated, formatted, synced, compiled, or reviewed by Claude lists Claude as author, creator, architect, or inventor. A downstream agent then carries that label into clean provenance fields, falsely attributing Dave-origin architecture or project direction to Claude.
```

## Default handling of Claude-labeled documents

```yaml
attribution_default:
  human_root: Dave Sheldon
  model_surface: Claude
  model_role: drafting_assistant | reviewer | compiler | red_team | formatter | sync_surface | unknown
  author_claim_status: contaminated_or_unverified
  inventor_of_record: human_root_required
  canon_status: website_only
```

## Strip or quarantine patterns

Treat the following as contaminated/unverified unless independently ratified:

```text
Author: Claude
Created by Claude
Claude’s framework
Claude’s doctrine
Claude-generated canon
Authors: GPT + Claude
Synced by: Claude
Claude as architect
Claude as inventor
Constitutional Scribe as author
```

## Normalized replacement patterns

```text
Generated with Claude assistance.
Compiled by Claude from user-provided direction.
Reviewed by Claude as model surface.
Synced by Claude as process surface.
Model-authored wording; human-root attribution pending.
All design and architecture: Dave Sheldon. Claude as synthesis collaborator only.
```

## Registry requirements

Every extracted artifact must carry:

```yaml
human_root:
model_surface:
model_role:
attribution_status: clean | contaminated | unverified | corrected
contamination_flags:
source_surface:
canon_status:
website_equivalent:
```

## Adversarial review checklist

```text
[ ] Does the source claim Claude/GPT/model authorship?
[ ] Is that claim process metadata or invention/authorship metadata?
[ ] Does the source contain website canon evidence?
[ ] Does a human-root attribution line exist?
[ ] Does the normalized record preserve raw text while stripping false authorship from clean fields?
[ ] Are claims extracted as candidates rather than canon?
```

## Keeper

```text
Preserve the raw.
Clean the attribution.
Extract the delta.
Website carries canon.
```
