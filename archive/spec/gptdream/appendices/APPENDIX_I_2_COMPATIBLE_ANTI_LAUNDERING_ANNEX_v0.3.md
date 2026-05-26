# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix I.2 — Compatible Anti-Laundering Annex v0.3

### I.2 — `compatible()` Anti-Laundering Annex

The `compatible()` function is the epistemic firewall against claim laundering.

Definition:

```text
compatible(A, B) = true
iff
  claim_class(A) ≤ claim_class(B) + 1
  AND conf(A) does not exceed conf(B) without new evidence
  AND no ratification event has been fabricated
```

Anti-laundering rules:

```text
1. A C1 claim citing another C1 claim does not become C2.
2. A candidate artifact cannot ratify another candidate artifact.
3. Assertion of compatibility does not substitute for evidence.
4. compatible() returning true does not authorize deployment.
5. Model output claiming compatible() without evidence is a C1 claim.
```

Laundering detection flags:

```text
- Artifact promoted to ratified_canon without traceable human-root event
- C1 claim chain presented as independently verified
- Citation loop (A cites B cites A, both C1)
- Dream output relabeled as fact in a subsequent session
- Storage on website treated as ratification without explicit signal
```
