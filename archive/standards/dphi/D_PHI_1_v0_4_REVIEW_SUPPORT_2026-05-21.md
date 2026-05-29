# D-Φ-1 v0.4 — Review Support Note

```text
STATUS: REVIEW SUPPORT — CANDIDATE — NOT CANON
DATE: 2026-05-21
DEPLOYMENT: none
AUTHORITY: none
PURPOSE: focus review questions after v2.1 wire/overlay separation
```

## Purpose

This note supports the D-Φ-1 v0.4 controlled review window by linking the recent v2.1 wire/overlay separation back to the active doctrine lane.

It is not a new doctrine, not a canon promotion, and not a deployment claim.

## Review focus

```text
1. Predicate correctness
2. artifact_status / authority_scope enforcement
3. Edge legality vs path legality
4. Receipt and replay protection
5. FALSE / UNRESOLVED / HOLD / QUARANTINE behavior
6. What blocks merge or ratification
```

## Relevant v2.1 wire lessons

```text
Layer 1 proves packet shape.
D0 proves sequence.
lantern_hash proves residue.
Governance proves authority.
```

The v2.1 Śūnya correction is useful to D-Φ-1 only as a packet-boundary and typed-absence reference.
It does not expand doctrine by itself.

## Boundary lines

```text
A packet passing shape checks is not authority.
A hash matching bytes is not ratification.
An eligibility set is not promotion.
A verifier pass is a green light to review, not a green light to deploy.
```

## Questions for reviewers

1. Does D-Φ-1 distinguish edge legality from path legality?
2. Does every candidate transition carry explicit artifact_status and authority_scope?
3. Does unresolved evidence route to HOLD rather than false promotion?
4. Does FALSE kill the candidate transition without deleting lineage?
5. Does HOLD expire to quarantine or require explicit review?
6. Are replay protections specified at the correct boundary?
7. Are canonical byte representations defined before hash claims?
8. Does any route let visibility, retrieval, simulation, or memory imply permission?

## Failure states to test

```text
FALSE:
  transition fails; lineage preserved; no execution

UNRESOLVED:
  transition holds; requires additional receipts or reviewer action

HOLD:
  bounded pause; must have expiration or next review trigger

QUARANTINE:
  preservation with warning; no deletion; no promotion
```

## Keeper doctrine

```text
Interpretation before legality.
Legality before execution.
Receipts before promotion.
Human-root before canon.
```
