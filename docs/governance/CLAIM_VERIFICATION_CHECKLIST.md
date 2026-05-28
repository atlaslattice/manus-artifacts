# Claim Verification Checklist

## Summary

Standard checklist applied before any artifact advances from `candidate` to `ratification_pending`.
Ensures claims are evidenced, provenance is traceable, and risks are surfaced.

---

## Checklist

### 1. Identity and scope

- [ ] Artifact has a unique `artifact_id` set in frontmatter.
- [ ] Title is clear and accurately describes the artifact's scope.
- [ ] Domain is correctly assigned.
- [ ] Author(s) are identified.

### 2. Provenance and lineage

- [ ] All source materials cited in `source_lineage` or equivalent section.
- [ ] No uncredited external content included.
- [ ] Predecessor artifacts (if any) are linked and their canon status is noted.
- [ ] Creation date is accurate and set in `created_utc`.

### 3. Claims integrity

- [ ] All factual claims include evidence or a citation.
- [ ] No overclaim: statements do not exceed what evidence supports.
- [ ] Speculative claims are explicitly labelled as speculation or future-state.
- [ ] AI-generated content is identified and not presented as human-verified fact.

### 4. Governance and canon boundaries

- [ ] `canon_status` is set to `CAND` (not `CANON`).
- [ ] `trust_state` is set to `UNVERIFIED` or `REVIEWED` (not `RATIFIED`).
- [ ] Artifact does not claim to be policy or authoritative standard on its own.
- [ ] Sensitive or private information is absent or properly scoped.

### 5. Conflicts and consistency

- [ ] No direct conflicts with existing canon artifacts detected.
- [ ] If a conflict exists, it is documented and flagged for council review.
- [ ] Terminology is consistent with the [Trust-State Glossary](./TRUST_STATE_GLOSSARY.md).

### 6. Navigation and links

- [ ] All internal links resolve to existing files.
- [ ] Cross-links to related artifacts are included.
- [ ] Artifact is reachable from a domain index or parent README.

### 7. Review readiness

- [ ] Artifact is in final review-ready form (not a draft stub).
- [ ] Length and structure are appropriate for the artifact type.
- [ ] Any open questions or unresolved items are explicitly flagged.

---

## Sign-off

```text
Reviewer: _______________   Date: _______________
Notes: _______________
```

---

## Cross-links

- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Conflict-Resolution Playbook](./CONFLICT_RESOLUTION_PLAYBOOK.md)
- [Trust-State Glossary](./TRUST_STATE_GLOSSARY.md)
- [Adjudication Receipt Template](./ADJUDICATION_RECEIPT_TEMPLATE.md)

## Status

`candidate` — not canon until ratified.
