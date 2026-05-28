# Canon and Trust Hierarchy (Authoritative Working Reference)

Status: candidate hierarchy reference (not canon)

## Canon Boundary

- No artifact is canon until full council ratification and adjudication by @atlaslattice.
- GitHub is the durable canonical substrate for receipts, history, and implementation state.
- Website surfaces are canon only when explicitly ratified/published as canon.

## Publication States

1. **DRAFT** — in local branch, issue, or PR discussion.
2. **CANDIDATE** — committed artifact under review.
3. **RATIFIED** — canonized by explicit governance event.
4. **DEPRECATED** — superseded but preserved for traceability.

## Minimum Fields for Canon Promotion

- `ratification_event_id`
- `canon_status`
- `trust_state`

## Decision and Audit Route

- Execution route for canon-affecting changes requires audit-aware governance flow.
- TIDELOCKBrain logging is required when merge-order or code execution decisions are involved.

## Practical Rule for Contributors

- Treat all current content as candidate unless an explicit ratification marker is present.
