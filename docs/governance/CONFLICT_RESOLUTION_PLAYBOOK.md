# Conflict-Resolution Playbook

## Summary

Standard procedure for identifying and resolving conflicts between artifacts in AtlasLattice.
Conflicts include: contradictory claims, duplicate scope, and policy gaps.

---

## Types of conflict

| Type | Description |
|---|---|
| **Factual conflict** | Two artifacts make contradictory factual claims. |
| **Scope overlap** | Two artifacts claim authority over the same domain or topic. |
| **Policy gap** | No authoritative artifact exists for a needed policy; two candidates conflict. |
| **Version drift** | A candidate artifact and a canon artifact have diverged over time. |
| **Provenance dispute** | Origin or authorship of content is contested. |

---

## Resolution procedure

### Step 1 — Identify the conflict

- Flag the conflict in a PR comment, issue, or governance decision record.
- Tag the artifact IDs of all affected artifacts.
- Classify the type of conflict (see table above).

### Step 2 — Triage severity

| Severity | Definition | Timeline |
|---|---|---|
| **Critical** | Conflicts with a CANON artifact or creates a safety/trust risk. | Resolve before merging. |
| **High** | Two candidates claim the same domain; could block ratification. | Resolve within 1 sprint. |
| **Medium** | Terminology or framing inconsistency. | Resolve before ratification. |
| **Low** | Minor overlap; no blocking effect. | Document and monitor. |

### Step 3 — Assemble context

- Retrieve both artifacts and their full source lineage.
- Identify which (if any) is the more canonical source.
- Check the [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md) for prior rulings.

### Step 4 — Propose resolution

Choose one of the following routes:

| Route | When to use |
|---|---|
| **Merge** | Scope overlaps; one artifact subsumes the other cleanly. |
| **Split** | Scope is legitimately distinct; separate into non-overlapping artifacts. |
| **Supersede** | A candidate is strictly better than an existing canon; promote and supersede. |
| **Withdraw** | One artifact is redundant or incorrect; archive it. |
| **Defer** | Conflict is not yet resolvable; document and flag for next review cycle. |

### Step 5 — Execute resolution

- Update affected artifact frontmatter (e.g., `canon_status`, `superseded_by`).
- Record the resolution in a [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md) entry.
- If a CANON artifact is affected, open an adjudication request for @atlaslattice.

### Step 6 — Verify closure

- [ ] Both artifacts' frontmatter reflect the resolved state.
- [ ] Decision recorded in governance index.
- [ ] Affected PRs or issues updated.
- [ ] No remaining contradictory claims in the repository.

---

## Escalation

If consensus is not reached at the contributor level, escalate to a council seat review.
If not resolved at council, escalate to @atlaslattice for binding adjudication.

---

## Cross-links

- [Claim Verification Checklist](./CLAIM_VERIFICATION_CHECKLIST.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md)
- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Adjudication Receipt Template](./ADJUDICATION_RECEIPT_TEMPLATE.md)

## Status

`candidate` — not canon until ratified.
