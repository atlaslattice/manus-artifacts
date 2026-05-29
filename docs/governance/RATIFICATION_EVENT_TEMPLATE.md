# Ratification Event Template

## Summary

Records the formal ratification event that elevates an artifact to `CANON` status.
One event file is created per successful ratification.

---

## Template

```yaml
---
ratification_event_id: "RAT-YYYY-NNN"
artifact_id: "<artifact_id>"
artifact_title: "<title>"
artifact_path: "<path/to/artifact.md>"
ratified_by: "@atlaslattice"
ratification_utc: "YYYY-MM-DDTHH:MM:SSZ"
council_seats_present: []       # list of GitHub usernames or seat IDs
council_vote: UNANIMOUS | MAJORITY | CONDITIONAL
effective_utc: "YYYY-MM-DDTHH:MM:SSZ"
adjudication_receipt_id: "ADJ-YYYY-NNN"
---
```

## Ratification statement

```text
[Formal statement confirming that the artifact meets the canonical standard and is hereby
elevated to CANON status, effective as of the date above.]
```

## Scope of canon

```text
[Describe exactly what is being canonized — the full artifact, a specific version, or
a specific section. Scope must be explicit.]
```

## Conditions of canon maintenance

```text
[Any conditions under which canon status could be revoked or requires re-review.]
```

## Supersedes (if applicable)

```text
Prior canon artifact(s) superseded by this ratification: <artifact_id(s) or "none">
```

---

## Filing instructions

1. Copy this template to `docs/governance/events/RAT-YYYY-NNN.md`.
2. Fill all YAML fields.
3. Update the artifact's frontmatter:
   - `canon_status: CANON`
   - `trust_state: RATIFIED`
   - `ratification_event_id: RAT-YYYY-NNN`
4. Add the artifact to the [Canon Registry](./CANON_REGISTRY.md).
5. Remove the artifact from the [Candidate Registry](./CANDIDATE_REGISTRY.md).
6. Link from the [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md).

---

## Cross-links

- [Adjudication Receipt Template](./ADJUDICATION_RECEIPT_TEMPLATE.md)
- [Canon Registry](./CANON_REGISTRY.md)
- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md)

## Status

`candidate` — not canon until ratified.
