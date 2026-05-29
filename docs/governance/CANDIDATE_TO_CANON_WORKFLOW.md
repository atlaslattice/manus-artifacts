# Candidate → Canon Promotion Workflow

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #7
LAST_UPDATED: 2026-05-29
```

End-to-end workflow for promoting an artifact from `CANDIDATE` to `RATIFIED`
(canonical) status.

---

## Workflow Overview

```
DRAFT
  │ PR merged to main
  ▼
CANDIDATE ──────────────────────────────────────────────────────────┐
  │                                                                  │
  │ Submitter: opens nomination issue                                │ Rejected:
  ▼                                                                  │ stays CANDIDATE
UNDER_REVIEW                                                         │ + remediation issue
  │                                                                  │
  │ Council: reviews; @atlaslattice adjudicates                      │
  ├─── Passes all gates ──────────────────────────────────────────── ┘
  ▼
RATIFIED (AUTHORITATIVE)
  │ Optional
  ▼
website-canon label applied
```

---

## Step-by-Step

### Step 1 — Nominate

1. Open a GitHub Issue using the **Governance Review Request** template.
2. Include: artifact path, current status, motivation for promotion.
3. Add a row to `docs/canon-candidate-register.md` with `UNDER_REVIEW`.
4. Tag `@atlaslattice` and the council label.

### Step 2 — Pre-Flight Validation

Submitter or a council member runs:

```bash
python scripts/validate_artifact_metadata.py
python scripts/check_graph_link_integrity.py
```

Results are posted as a comment on the nomination issue.

### Step 3 — Council Review

Council members review the artifact and nomination issue asynchronously or in a
scheduled session. Review criteria:

- Content accuracy and internal consistency
- Provenance and citation quality
- No open disputes or contradictions with existing canon
- Metadata completeness (see [CANON_ADJUDICATION_CHECKLIST.md](./CANON_ADJUDICATION_CHECKLIST.md))

### Step 4 — Adjudication

@atlaslattice makes the final ratification decision:

- **Approve:** Assigns `ratification_event_id`, updates frontmatter.
- **Defer:** Requests specific changes; artifact returns to `CANDIDATE`.
- **Reject:** Closes issue with documented rationale.

### Step 5 — Ratification

1. Update artifact frontmatter to `RATIFIED` fields.
2. Record event in `GOVERNANCE_CHANGELOG_TEMPLATE.md`.
3. Update `docs/canon-candidate-register.md` — move entry to Ratification Log.
4. Regenerate `docs/LATTICE_GLOBAL_INDEX.md` if needed.
5. Close nomination issue with ratification event reference.

### Step 6 — Post-Ratification (Optional)

- Apply `website-canon` label if web publication is intended.
- Notify downstream agent systems that cite this artifact.

---

## SLA Targets

| Stage | Target Turnaround |
|---|---|
| Nomination → Review start | ≤ 7 days |
| Review → Adjudication | ≤ 14 days |
| Adjudication → Frontmatter update | ≤ 2 days |

---

## Related

- [CANON_ADJUDICATION_CHECKLIST.md](./CANON_ADJUDICATION_CHECKLIST.md)
- [RATIFICATION_EVENT_ID_STANDARD.md](./RATIFICATION_EVENT_ID_STANDARD.md)
- [CANON_DISPUTE_RESOLUTION.md](./CANON_DISPUTE_RESOLUTION.md)
