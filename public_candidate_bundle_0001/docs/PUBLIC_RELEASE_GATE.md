# Public Release Gate

**Status:** public candidate  
**Canon:** no  
**Deployment:** no  
**Authority:** none  

## Core rule

```text
PUBLIC-SAFE
+ RECEIPT-LABELED
+ NON-SENSITIVE
+ NON-DEPLOYABLE
+ WORLD-CLASS CONDITION
= release candidate
```

This gate exists so Atlas Lattice / Rainbow Yin Yang Lattice can become public, forkable, and useful without accidentally publishing private raw cargo, unsupported authority claims, or sensitive material.

## Release lanes

```text
GREEN  = publish candidate
YELLOW = hold for review
RED    = do not publish
```

## GREEN — publish candidate

An artifact may be classified GREEN when it is:

```text
public-safe
receipt-labeled
non-sensitive
non-deployable
rights/license status reviewed or low-risk
bounded as non-canon / not deployed / authority none
clear about strongest safe claim
clear about overclaims to avoid
```

## YELLOW — hold for review

An artifact should be classified YELLOW when it has value but needs review before public release.

Common YELLOW reasons:

```text
raw export incomplete
rights unclear
privacy status unclear
public-safe summary needed
Claude-originated or Claude-touched governance content
contains strong claims needing evidence
possible sensitive/security/financial language
needs redaction
needs human-root review
```

## RED — do not publish

An artifact should be classified RED for public release when it contains:

```text
credentials, keys, tokens, env files, or secrets
private personal data
unreviewed raw transcripts with private context
operational security-intrusion instructions
financial-institution targeting instructions
weapons or harmful operational details
confidential strategy or negotiation material
unclear copyrighted raw dumps
unsupported claims of deployment, canon, legal authority, official endorsement, or scientific proof
```

RED does not mean destroy. RED means preserve privately, quarantine, or route for review.

## Required fields before public release

Every artifact intended for public release should carry:

```yaml
required_public_release_fields:
  - artifact_id
  - title
  - source_surface
  - source_uri_or_path
  - public_release_class
  - privacy_status
  - rights_status
  - redline_scan
  - strongest_safe_claim
  - overclaims_to_avoid
  - canon_status
  - deployment_status
  - authority_scope
  - review_lane
  - missing_receipts
  - next_action
```

## Quarantine is not condemnation

Quarantine is review hygiene. It preserves artifacts while preventing accidental public release.

```text
Critique is allowed.
Defensive analysis may be legitimate.
Sensitive artifacts are preserved.
Public release waits for review.
Quarantine is not condemnation.
```

## Graph boundary

A public graph node or edge does not promote an artifact to truth.

```text
graph edge ≠ promotion
cluster ≠ canon
centrality ≠ authority
GitHub visibility ≠ proof
model output ≠ evidence unless labeled as model output
```

## Floodgate posture

The goal is to release aggressively only when safety and evidence conditions are met.

```text
Flood the gates with receipts, not secrets.
Public-safe does not mean canon.
World-class means well-labeled, reviewable, and non-inflated.
```

## Madden translation

Open the gates, but keep the metal detector on.  
Green gets cleaned and labeled.  
Yellow goes upstairs for review.  
Red gets benched before it hurts somebody.
