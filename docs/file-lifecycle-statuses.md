# File Lifecycle Statuses

Status: candidate lifecycle standard (not canon)

## Lifecycle States

- **Draft**: work-in-progress, not yet committed to stable reference paths.
- **Candidate**: committed and reviewable, default state for most artifacts.
- **Ratified**: canonized with explicit governance event marker.
- **Active**: current preferred artifact for an operational function.
- **Superseded**: replaced by a newer artifact; kept for lineage.
- **Deprecated**: discouraged for new use; retained for traceability.
- **Archived**: retained as historical record with minimal active maintenance.

## State Transition Rules

- Candidate → Ratified requires explicit adjudication and ratification evidence.
- Active → Superseded/Deprecated requires replacement reference and rationale.
- Deprecated/Archived artifacts are preserved, not hard-deleted.
