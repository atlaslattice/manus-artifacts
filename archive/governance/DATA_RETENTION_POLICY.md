# Data Retention Policy

*Atlas Lattice Foundation · Aetherforge Mission #19 · 2026-05-28*

status: candidate

> Defines how long different categories of data are retained in the Atlas Lattice repository, and how data is handled when retention periods expire.

---

## Policy Principles

1. **Preserve provenance** — the knowledge graph depends on traceable history; deletion is the exception, not the norm.
2. **Minimize unnecessary personal data** — PII not essential to the archive's mission should not be retained.
3. **Honor subject requests** — individuals may request removal of their personal information per applicable law.
4. **Maintain durability** — archival content is retained indefinitely in frozen state.

---

## Retention Schedule

| Data Category | Retention Period | Disposition at End |
|---------------|-----------------|-------------------|
| Ratified canon artifacts | Indefinite | Archived permanently |
| Candidate artifacts (ratified or superseded) | Indefinite | Status updated; never deleted |
| Candidate artifacts (abandoned / stale > 2 years) | 2 years from last activity | Moved to `archive/_quarantine/`; deprecation notice added |
| Council session records | Indefinite | Frozen archive |
| CI/CD workflow logs (GitHub) | 90 days (GitHub default) | Auto-purged by GitHub |
| Issue and PR records | Indefinite (GitHub managed) | Retained by platform |
| Dream journals / REM artifacts | Indefinite | KG archive |
| Contributor PII (if accidentally committed) | 0 days — redact immediately | Git history purge on discovery |
| Security incident reports | 7 years | Archived securely; sensitive portions redacted |
| API access logs (future) | 1 year | Anonymized aggregate retention |

---

## Handling Stale Artifacts

Artifacts with no commits or meaningful activity for **24 months** are eligible for quarantine:

1. Add a `STALE` header to the document.
2. Move to `archive/_quarantine/<section>/`.
3. Leave a redirect stub at the original path.
4. Log in the quarterly council session.

This does **not** apply to ratified canon artifacts, which are retained permanently.

---

## Personal Data Removal Requests

If an individual requests removal of their personal information from this repository:

1. Verify the request is from the individual themselves or their authorized representative.
2. Identify all occurrences in the repository (including git history).
3. Apply the [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md).
4. If git history purge is required, use `git filter-repo` and force-push with team coordination.
5. Acknowledge completion within **30 days** of the verified request.

Contact: `privacy@atlaslattice.org`

---

## Backup and Durability

The primary canonical substrate is **GitHub**. Durability is provided by:
- GitHub's infrastructure and built-in redundancy
- Future: periodic archival export to IPFS or equivalent decentralized store (Mission #142)

---

## Related Documents

- [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md)
- [Sensitive Content Review Process](./SENSITIVE_CONTENT_REVIEW_PROCESS.md)
- [Incident Response Runbook](./INCIDENT_RESPONSE_RUNBOOK.md)
- [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
