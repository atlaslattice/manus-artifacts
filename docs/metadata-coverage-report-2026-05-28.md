# Metadata Coverage Report 2026-05-28

> **Status:** CANDIDATE  
> **Artifact Type:** report  
> **Stable ID:** AL-EVID-003  
> **Date:** 2026-05-28

<!-- METADATA
stable_id: AL-EVID-003
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

## Candidate Status Note

This candidate report captures the current metadata coverage posture for Wave 1 metadata backfill planning and should not be treated as canon without ratification.

## Scope

This candidate report captures the current metadata coverage posture for the seeded artifact graph. Coverage is measured by the presence of stable IDs, artifact types, lifecycle states, repo paths, and explicit cross-links.

## Current Coverage Notes

- All seeded registry entries carry the required v0.1 metadata fields.
- Reverse-link generation now exposes inbound-link gaps directly.
- Topic and domain pages improve human discoverability around machine-readable records.

## Per-Domain Coverage Table

| Domain | Total files | Has ID | Has lifecycle | Has provenance | Has owner | Score % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| docs | 10 | 6 | 5 | 3 | 4 | 45% |
| projects | 12 | 8 | 7 | 6 | 8 | 60% |
| archive/spec | 15 | 9 | 8 | 7 | 8 | 53% |
| archive/boot/governance | 1 | 1 | 1 | 1 | 1 | 100% |
| council | 1 | 0 | 0 | 0 | 0 | 0% |
| health | 4 | 0 | 0 | 0 | 0 | 0% |
| research | 7 | 0 | 0 | 0 | 0 | 0% |

## Next Steps

1. Run `python scripts/backfill_metadata.py` to generate the machine-readable coverage report.
2. Backfill `stable_id`, `lifecycle_state`, `owner`, and `date_created` blocks in uncovered `docs/` and `projects/` artifacts.
3. Extend the same metadata pattern into `archive/spec/` and `archive/boot/governance/`.
4. Use `python scripts/validate_provenance_fields.py` to monitor progress without turning the report into a hard gate.
5. Queue follow-on registry updates for the candidate reports, maps, and validation receipt artifacts created in Waves 1 and 2.

## Next Improvements

- Add ownership, provenance origin, and last-updated fields in future schema revisions.
- Expand registry coverage to more archive subtrees and project surfaces.
- Track link completeness over time with generated reports.

## Related Topics

- [Knowledge graph topic](./topics/knowledge-graph.md)
- [Governance topic](./topics/governance.md)
