# Governance Operations Handbook

## Summary

Operational guide for running governance in the AtlasLattice repository.
Covers the regular cadence, roles, procedures, and escalation paths.

---

## Roles

| Role | Description | Who |
|---|---|---|
| **Human Root / Adjudicator** | Final authority on all canon decisions. | @atlaslattice |
| **Council Seat** | Reviews candidates, signs off on ratification readiness. | S1–S7 brain seats |
| **Contributor** | Submits candidates, runs claim verification checklists. | Any contributor |
| **Steward** | Maintains registries, indexes, and governance records. | Assigned per wave |

---

## Regular cadence

| Frequency | Activity |
|---|---|
| **Per PR** | Claim verification checklist completed before merge. |
| **Weekly** | Review open candidates in the [Candidate Registry](./CANDIDATE_REGISTRY.md); advance or defer. |
| **Monthly** | Run drift detection (`python scripts/validate_artifact_metadata.py`); update [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md). |
| **Quarterly** | Architecture refactor cycle; review superseded artifacts; publish trust report. |
| **Annually** | Full transparency report; benchmark against world-class standards. |

---

## Artifact promotion procedure

1. **Contributor** submits PR with `canon_status: CAND` in frontmatter.
2. **Contributor** completes the [Claim Verification Checklist](./CLAIM_VERIFICATION_CHECKLIST.md) in the PR.
3. **Council Seat(s)** review and leave approval comments.
4. Once all required council seats approve, **Steward** updates status to `RAT_PEND`.
5. **@atlaslattice** adjudicates: issues an [Adjudication Receipt](./ADJUDICATION_RECEIPT_TEMPLATE.md) and (if ratified) a [Ratification Event](./RATIFICATION_EVENT_TEMPLATE.md).
6. **Steward** updates artifact frontmatter, registries, and decision index.

---

## Conflict handling

See [Conflict-Resolution Playbook](./CONFLICT_RESOLUTION_PLAYBOOK.md) for the standard procedure.

---

## Source-of-truth discipline

See [Source-of-Truth Mirror Policy](./SOURCE_OF_TRUTH_MIRROR_POLICY.md).

Key rule: **GitHub is the canonical substrate.** All other layers are relay or publication.

---

## Governance records

| Record type | Location | Template |
|---|---|---|
| Adjudication receipts | `docs/governance/receipts/` | [Template](./ADJUDICATION_RECEIPT_TEMPLATE.md) |
| Ratification events | `docs/governance/events/` | [Template](./RATIFICATION_EVENT_TEMPLATE.md) |
| ADRs | `docs/decisions/` | `docs/decisions/ADR-NNNN-*.md` |
| Decision index | `docs/governance/GOVERNANCE_DECISION_INDEX.md` | — |

---

## Escalation path

```
Contributor issue → Council seat review → @atlaslattice adjudication
                                ↑
                  (unresolved conflict or policy gap)
```

---

## Governance health checks

Run regularly to verify governance hygiene:

```bash
python scripts/validate_artifact_metadata.py   # frontmatter compliance
python scripts/check_markdown_links.py         # link integrity
python scripts/detect_orphaned_artifacts.py    # orphan detection
```

---

## Cross-links

- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Canon Metadata Standard](./CANON_METADATA_STANDARD.md)
- [Canon Registry](./CANON_REGISTRY.md)
- [Candidate Registry](./CANDIDATE_REGISTRY.md)
- [Claim Verification Checklist](./CLAIM_VERIFICATION_CHECKLIST.md)
- [Conflict-Resolution Playbook](./CONFLICT_RESOLUTION_PLAYBOOK.md)
- [Source-of-Truth Mirror Policy](./SOURCE_OF_TRUTH_MIRROR_POLICY.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md)
- [Trust-State Glossary](./TRUST_STATE_GLOSSARY.md)

## Status

`candidate` — not canon until ratified.
