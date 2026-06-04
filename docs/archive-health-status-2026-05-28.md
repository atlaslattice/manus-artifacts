# Archive Health Status 2026-05-28

> **Status:** CANDIDATE  
> **Artifact Type:** report  
> **Stable ID:** AL-HEALTH-001  
> **Date:** 2026-05-28

<!-- METADATA
stable_id: AL-HEALTH-001
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

## Candidate Status Note

This archive-health snapshot is a candidate-state operational report for prioritization and validation hardening work.

## Summary

Archive health is improving through machine-readable indexing, graph validation, and discoverability surfaces. This report records the candidate-state checkpoint associated with artifact graph automation.

## Observations

- Core registry and taxonomy files are present and versioned.
- CI validation exists for artifact graph structure.
- Discoverability surfaces now include topic, domain, and reading-path indexes.

## Overall Archive Health Score

**72 / 100**

## Category Breakdown

| Category | Score | Status | Notes |
| --- | ---: | --- | --- |
| Registry completeness | 78 | 🟡 | Core candidate artifacts are registered, but broad repository coverage is still incomplete. |
| Provenance coverage | 58 | 🔴 | Stable IDs exist in key places, but owner/date/provenance blocks are uneven. |
| Link validity | 84 | 🟢 | Registry relation targets and core document links are mostly coherent. |
| CI coverage | 68 | 🟡 | Existing checks are useful, and Wave 2 adds stronger metadata validation, but coverage is not universal yet. |
| Domain structure | 72 | 🟡 | Directory domains are understandable, though stewardship and metadata boundaries still need tightening. |

## Top 5 Next Actions to Improve Score

1. Backfill provenance blocks into unregistered `docs/` and `projects/` artifacts that still lack stable IDs.
2. Expand registry coverage for newly stabilized reports, validation specs, and domain maps.
3. Run the new metadata and lifecycle validators weekly and capture validation receipts for failure cases.
4. Normalize `archive/spec/` metadata so provenance coverage moves from red to yellow.
5. Add stewardship owners for council, health, and research domains to reduce ambiguity.

## Generated Timestamp

`2026-05-28T09:00:00Z`

## Follow-Up

- Continue expanding registry coverage beyond the current seeded set.
- Add more generated reports as coverage and link density increase.
- Keep candidate/canon boundaries explicit in all public-facing navigation layers.

## Related Topics

- [Knowledge graph topic](./topics/knowledge-graph.md)
- [Archive domain](./domains/archive.md)
