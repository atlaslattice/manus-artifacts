# Drive→GitHub Promotion Ruleset v0.1 (CANDIDATE)

1. Every promoted artifact must include: source URI, source hash, receipt, provenance, canon status, reviewer, and ratification event.
2. Artifact classes are constrained to `dream`, `play`, or `work` and must satisfy class-specific validation requirements.
3. `canon_status` defaults to `NOT_CANON` unless explicit adjudication is attached.
4. `RATIFIED_CANON` is blocked unless reviewer and ratification_event are populated.
5. Promotion without complete required validations is blocked.
6. GitHub staging is authoritative for receipts and lineage tracking; not for automatic canon assignment.
