# Appendix I — Atlas/ORCS Epistemic Governance Profile v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md**
> **DATE: 2026-05-26**

---

## I.0 Purpose

Atlas/ORCS is the epistemic governance engine for the GPTDream++ habitat. It provides:

- **Atlas**: The artifact trust state machine — tracks where every artifact is in its lifecycle
- **ORCS**: The Operation, Ratification, and Contradiction System — the governance layer that drives state transitions

Together they ensure that **authority is a state transition, not a vibe.**

---

## I.1 Core Governance Axioms

1. **No artifact is canon without a ratification event.** Period.
2. **No deployment status changes without a governance event.**
3. **Contradiction creates a contradiction record, not an overwrite.**
4. **Summary cannot replace source.** A summary is a derived artifact; it does not inherit the source's authority.
5. **Receipt ≠ truth.** A GitHub receipt proves something was filed here; it does not prove the claims within are true.
6. **Expired ratification → `under_review`.** Ratification is time-bound; stale ratifications demote artifacts.
7. **Quarantined artifacts preserve lineage.** Quarantine is not deletion.

---

## I.2 Atlas Trust States

```
          ┌─────────────────────────────────────────────────────┐
          │              Atlas State Machine                      │
          │                                                       │
          │    raw ──▶ parsed ──▶ candidate ──▶ reviewed         │
          │              │                          │             │
          │              ▼                          ▼             │
          │          quarantined             ratified ──▶ active │
          │              │                          │             │
          │              │              ┌───────────┤             │
          │              │              ▼           ▼             │
          │              │         under_review  superseded       │
          │              │              │                         │
          │              │              ▼                         │
          │              └─────────▶ revoked                     │
          │                            │                          │
          │                            ▼                          │
          │                         rejected                      │
          └─────────────────────────────────────────────────────┘
```

### State Definitions

| State | Description |
|-------|-------------|
| `raw` | Unprocessed input; no validation performed |
| `parsed` | Structure validated; content not yet assessed |
| `candidate` | Reviewed for structure; candidate for governance processing |
| `reviewed` | Council or automated review completed; awaiting ratification |
| `ratified` | Explicit ratification event recorded; may be promoted to active |
| `active` | Currently operative artifact; ratification in-force |
| `under_review` | Previously active; ratification expired or challenged |
| `superseded` | A newer version is active; this version preserved for lineage |
| `revoked` | Explicitly revoked by governance event; lineage preserved |
| `quarantined` | Isolated due to safety or integrity concern; lineage preserved |
| `rejected` | Failed validation or governance review; archived |

---

## I.3 ORCS Operation Types

| Operation | Code | Description |
|-----------|------|-------------|
| Parse | `ORCS-PARSE` | Validate structure and assign initial state |
| Review | `ORCS-REVIEW` | Council or automated review |
| Ratify | `ORCS-RATIFY` | Explicit ratification event (requires authority) |
| Promote | `ORCS-PROMOTE` | Move to active state (requires prior ratification) |
| Supersede | `ORCS-SUPERSEDE` | Mark as superseded by newer version |
| Revoke | `ORCS-REVOKE` | Explicit revocation (requires authority) |
| Quarantine | `ORCS-QUARANTINE` | Isolate for safety/integrity review |
| Contradict | `ORCS-CONTRADICT` | Create contradiction record (never overwrite) |
| Challenge | `ORCS-CHALLENGE` | Request review of active artifact |
| Expire | `ORCS-EXPIRE` | Trigger on ratification timeout → `under_review` |
| Audit | `ORCS-AUDIT` | Log audit event (no state change) |

---

## I.4 Ratification Requirements

To ratify an artifact:

1. Artifact must be in `reviewed` state
2. Ratification request must include:
   - `ratifier_id` (who is ratifying)
   - `ratification_scope` (what is being ratified)
   - `expiry` (when does this ratification expire)
   - `council_quorum` (how many council members reviewed)
3. Ratification is logged as an explicit `atlas-ratification-event`
4. Self-ratification is **prohibited** — an artifact cannot ratify itself
5. For full canon, @atlaslattice adjudication is additionally required

---

## I.5 Contradiction Handling

When a contradiction is detected:

```
Contradiction detected
        │
        ▼
Create contradiction_record
  - artifact_id_a
  - artifact_id_b  
  - contradiction_type
  - detected_by
  - timestamp
        │
        ▼
Both artifacts remain in their current state
        │
        ▼
Atlas/ORCS flags for council review
        │
        ▼
Contradiction_record logged in contradiction_ledger
```

**Never overwrite.** Never silently resolve. Always log.

---

## I.6 Appendix Sub-Sections

| Sub-Appendix | Title | File |
|-------------|-------|------|
| I.1 | Formal Math Spine | `APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md` |
| I.2 | Compatible Anti-Laundering Annex | `APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md` |
| I.3 | Atlas/ORCS Schema Bundle | `APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md` |

---

## I.7 Canon Boundary

This appendix is **NOT CANON**. Atlas/ORCS becomes canon only after full council ratification + @atlaslattice adjudication + website publication.

---

*End of APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md*
