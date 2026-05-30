# PII Redaction Rubric

*Atlas Lattice Foundation · Aetherforge Mission #16 · 2026-05-28*

status: candidate

> Defines what constitutes Personally Identifiable Information (PII) in the context of Atlas Lattice artifacts, and the standard process for detecting and redacting it before publication.

---

## Scope

This rubric applies to all content submitted to this repository, including:
- Archived documents, chat logs, and council records
- Dream journals and wake reports
- Code comments and commit messages
- Seed data files (`.jsonl`, `.yaml`)

---

## PII Classification

### Tier A — Always Redact Before Commit

| Category | Examples |
|----------|---------|
| Full legal name (non-public figure) | "John Smith at 123 Main St…" |
| Home or personal address | Any residential address |
| Phone numbers | Mobile, home, personal business |
| Government ID numbers | SSN, passport, driver's license |
| Financial account data | Account numbers, card numbers |
| Biometric data | Fingerprint patterns, face templates |
| Health / medical data | Diagnosis, prescription, test results |
| Authentication credentials | Passwords, API keys, tokens, secrets |
| Private email addresses | Personal, non-public email |

### Tier B — Review Before Commit (Context-Dependent)

| Category | Notes |
|----------|-------|
| Full name of a public figure | OK if used in factual, public-interest context |
| Professional email address | OK if public-record / org-level |
| GitHub usernames | OK for public contributors who've consented |
| IP addresses | OK if non-residential (server/CDN ranges); redact personal IP |
| Location data | City/country OK; neighborhood or precise GPS not OK |

### Tier C — Generally OK

- Organization names
- Public project names and titles
- Publicly published research citations
- AI agent identifiers (GPTBrain, TIDELOCKBrain, etc.)

---

## Redaction Process

### Step 1 — Pre-Commit Scan

Before committing any artifact containing imported or transcribed content, scan for Tier A items using search patterns:
- Email regex: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
- Phone regex: `(\+?[\d\s\-().]{7,15})`
- Secret patterns: covered by GitHub secret scanning

### Step 2 — Redaction Format

Replace PII with a consistent placeholder:

```
[REDACTED: category]
```

Examples:
- `[REDACTED: email]`
- `[REDACTED: phone]`
- `[REDACTED: address]`
- `[REDACTED: credential]`

### Step 3 — Commit Note

If redacting content in an existing file, add a note in the commit message:

```
[CHORE] Redact PII from <filename> — removed [category]
```

### Step 4 — Git History

If PII was accidentally committed to git history, it must be purged using `git filter-repo` or equivalent. Report to security@atlaslattice.org immediately.

---

## Archive Import Special Cases

When importing chat logs, council records, or external documents:
1. Run a Tier A scan before first commit.
2. Flag any Tier B items for human review.
3. Document the redaction decision in the artifact's frontmatter under `redaction_log`.

---

## Related Documents

- [Sensitive Content Review Process](./SENSITIVE_CONTENT_REVIEW_PROCESS.md)
- [Data Retention Policy](./DATA_RETENTION_POLICY.md)
- [Incident Response Runbook](./INCIDENT_RESPONSE_RUNBOOK.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
