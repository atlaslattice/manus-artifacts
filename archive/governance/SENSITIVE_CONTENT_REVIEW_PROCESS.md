# Sensitive Content Review Process

*Atlas Lattice Foundation · Aetherforge Mission #17 · 2026-05-28*

status: candidate

> Defines the process for identifying, reviewing, and handling sensitive content before it is published or merged into the Atlas Lattice repository.

---

## What Is Sensitive Content?

Sensitive content is any material that:

1. Contains PII (see [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md))
2. Contains security credentials or secrets
3. Has legal constraints (copyright, export control, NDA)
4. Depicts or describes harm, violence, or legally restricted material
5. Includes non-public organizational or financial information
6. Contains AI-generated content with unclear provenance or consent

---

## Review Triggers

A sensitive content review is required when:

- Importing external documents, chat logs, or research archives
- Adding AI evidence logs with third-party system references
- Submitting content that references private individuals
- Including data from external APIs or databases
- Archiving council or organizational records

---

## Review Steps

### Step 1 — Author Pre-Check

Before opening a PR with potentially sensitive content:

1. Complete the [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md) scan.
2. Check for secrets using `git secrets` or GitHub secret scanning.
3. Verify copyright status of any included third-party text.
4. Add a note to the PR description: `Sensitive Content Review: [clean / items addressed / needs review]`.

### Step 2 — PR Label

Tag the PR with:
- `sensitive-content` — if it contains content that was reviewed and cleared
- `needs-sensitive-review` — if uncertain; blocks merge until reviewed

### Step 3 — Reviewer Checklist

The PR reviewer must confirm:

- [ ] No unredacted PII in Tier A categories
- [ ] No secrets or credentials present
- [ ] No copyrighted text reproduced without license/attribution
- [ ] No export-controlled technical data (see [Export Control Checklist](./EXPORT_CONTROL_SCREENING_CHECKLIST.md))
- [ ] No content depicting harm or illegal activity
- [ ] AI-generated content sources are noted in frontmatter

### Step 4 — Resolution

- If issues found: request changes; author must remediate before merge.
- If cleared: reviewer removes `needs-sensitive-review` label, adds `sensitive-content-cleared`.
- If unclear: escalate to Governance Lead or @atlaslattice.

---

## Post-Merge Monitoring

GitHub secret scanning is enabled on this repository. Any post-merge detection of secrets will trigger the [Incident Response Runbook](./INCIDENT_RESPONSE_RUNBOOK.md).

---

## Related Documents

- [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md)
- [Export Control Screening Checklist](./EXPORT_CONTROL_SCREENING_CHECKLIST.md)
- [Data Retention Policy](./DATA_RETENTION_POLICY.md)
- [Incident Response Runbook](./INCIDENT_RESPONSE_RUNBOOK.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
