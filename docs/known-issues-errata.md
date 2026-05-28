# Known Issues and Errata

Status: candidate errata register (not canon)

## Scope

This register tracks non-sensitive known issues, documentation gaps, and
incorrect statements discovered after publication.

## Active Errata

| ID | Area | Issue | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| ERR-2026-05-28-001 | Link integrity | Some historical markdown files contain unresolved or placeholder links. | Validation noise in full-repo link scans. | Keep quality-gate scripts focused on high-signal surfaces and incrementally remediate legacy links. | Open |
| ERR-2026-05-28-002 | Test surface | Full `pytest` collection includes sub-project tests that require extra local dependencies and import paths. | Local baseline test run can fail during collection outside CI-targeted suites. | Use workflow-scoped test commands and project-specific test surfaces for gating. | Open |
| ERR-2026-05-28-003 | Board drift | Wave-3 taskboard checkboxes lagged behind already-shipped artifacts. | Progress reporting mismatch. | Reconciled board status and aligned with delivered files in this sprint. | Resolved |

## Reporting New Errata

1. Open a GitHub issue using the task/ops template.
2. Include file path(s), expected behavior, and observed behavior.
3. Add evidence links (commit/PR/workflow) for reproducibility.

## Review Cadence

- Review open errata during each Wave closeout.
- Promote resolved high-impact errata into changelog/release notes.
