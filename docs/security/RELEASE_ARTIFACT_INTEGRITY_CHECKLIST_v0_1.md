---
artifact_id: DOC-RELEASE-ARTIFACT-INTEGRITY-CHECKLIST-v0-1-2026-05-28
title: Release Artifact Integrity Checklist
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Release Artifact Integrity Checklist

Use this checklist before publishing a release, major archive snapshot, or trust report.

- [ ] All required workflows passing or waivers documented
- [ ] No open unresolved secret-scan findings
- [ ] No unreviewed critical/high dependency alerts
- [ ] README and top-level indexes point to current release artifacts
- [ ] All release-linked artifacts have valid frontmatter and reachable links
- [ ] Any exceptions are logged in the [Security Exceptions Ledger](./SECURITY_EXCEPTIONS_LEDGER_2026-05-28.md)
- [ ] Any ratification-sensitive artifacts clearly marked `CANDIDATE` or `RATIFIED`
- [ ] Release note or trust report references the current [Security Posture Report](./SECURITY_POSTURE_REPORT_2026-05-28.md)
