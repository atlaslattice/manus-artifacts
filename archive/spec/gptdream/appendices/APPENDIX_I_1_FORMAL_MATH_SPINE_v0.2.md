# Appendix I.1 — Formal Math Spine v0.2

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.2
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md
```

---

## I.1.0 Purpose

This appendix defines the formal mathematical spine underpinning Atlas / ORCS trust-state transitions and the `compatible()` anti-laundering predicate.

## I.1.1 Artifact state space

Let **S** be the set of trust states:

```
S = {raw, parsed, candidate, reviewed, ratified, active,
     under_review, superseded, revoked, quarantined, rejected}
```

Let **A** be an artifact. The trust state of A at time t is written `τ(A, t) ∈ S`.

## I.1.2 Permitted transition relation

Let **→_Γ** be the permitted transition relation under governance context Γ:

```
→_Γ ⊆ S × S

Permitted base transitions:
  raw         →_Γ  parsed
  parsed      →_Γ  candidate
  candidate   →_Γ  reviewed
  reviewed    →_Γ  ratified        [requires: ratification_event(A, Γ)]
  ratified    →_Γ  active          [requires: deployment_event(A, Γ)]
  active      →_Γ  under_review    [trigger: review_initiated OR expired_ratification]
  under_review →_Γ reviewed
  active      →_Γ  superseded      [requires: supersession_event(A, A', Γ)]
  any         →_Γ  revoked         [requires: revocation_event(A, Γ)]
  any         →_Γ  quarantined     [trigger: contradiction OR security_event]
  any         →_Γ  rejected
```

## I.1.3 Governance delta

A **governance delta** δ is a tuple:

```
δ = (event_type, authority_key, timestamp, artifact_id, previous_state, new_state, evidence_refs)
```

A transition `s →_Γ s'` is **permitted** iff:
1. `(s, s') ∈ →_Γ`
2. There exists a valid governance delta δ authorizing the transition
3. The authority_key in δ is recognized by Γ
4. The evidence_refs in δ are non-empty

## I.1.4 Anti-laundering predicate (informal)

An **edge** `(A, s, s', δ)` is **compatible** under Γ iff:
- The transition `s →_Γ s'` is permitted
- The governance delta δ is valid and non-forged

A **path** `(e₁, e₂, ..., eₙ)` is **compatible** under Γ iff:
- All edges eᵢ are compatible
- `NOT launder(path, Γ)`

where `launder(path, Γ)` holds iff:
- The path causes any of {authority, canon, deployment, proof, public_claim} status to increase
- without a corresponding explicit permitted governance delta

See `APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md` for complete predicate.

## I.1.5 Contradiction lemma

When artifact A' contradicts artifact A:

```
contradiction(A, A') → create contradiction_record(A, A')
                        NOT overwrite(A)
                        quarantine_candidate(A')
                        emit atlas-audit-event(contradiction)
```

A contradiction record preserves both A and A' with their full lineage.

## I.1.6 Summary inequality

For any summary artifact S derived from source artifact A:

```
epistemic_weight(S) < epistemic_weight(A)
S ≠ A                 (summary is not source)
receipt(S) ≠ truth(A) (receipt does not establish truth)
```

## I.1.7 Ratification requirement

```
τ(A, t) = ratified  →  ∃δ: ratification_event(A, δ) ∧ δ.timestamp ≤ t
                         ∧ δ.authority_key ∈ Γ.recognized_authorities
```

Expired ratification:

```
t > δ.expiry_timestamp  →  τ(A, t) = under_review
```

---

```text
NOT CANON. NOT DEPLOYABLE.
```
