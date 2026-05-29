# 🔒 Quarantine — Private Content Staging

## Summary

This directory holds content that has been identified for **private repository migration**. These files are staged here pending transfer to a dedicated private repository.

**Action required by @atlaslattice:** Move the contents of this folder to a new private GitHub repository (e.g., `atlaslattice/manus-artifacts-private`), then delete this folder from the public repo.

---

## Why Quarantine?

Per the repository governance rule:

> Anything with the word "hacker" or referring to banks must be quarantined and kept private. The rest should be public.

---

## Contents

### `free-bank/`

| File | Reason |
|------|--------|
| `banking-revolution-archive.md` | Primary content about banking revolution / bank disruption strategy |
| `Manus_Free_Bank_Technical_Blueprint.md` | Full technical blueprint for an AI-powered banking replacement ("The Free Bank") |

---

## Additional Files Flagged for Review

The following files in the main repository contain incidental references to hacking groups or banking systems. They are **large codebases** where the references are embedded as data/memory strings (1 occurrence each). They have been redacted in-place rather than quarantined in full:

| File | Reference |
|------|-----------|
| `codebases/email-processing/output_layer.py` | "Handala hacking group" in stored memory data (redacted) |
| `codebases/email-processing/remaining_innovations.py` | "Handala hacking group" in stored memory data (redacted) |
| `codebases/sovereign-oracle/output_layer.py` | "Handala hacking group" in stored memory data (redacted) |
| `codebases/sovereign-oracle/remaining_innovations.py` | "Handala hacking group" in stored memory data (redacted) |

---

## Migration Checklist

- [ ] Create private repo `atlaslattice/manus-artifacts-private`
- [ ] Copy `quarantine/` contents to private repo
- [ ] Delete `quarantine/` from this public repo
- [ ] Confirm no residual references remain in public README or index files

---

*Quarantine staging created: 2026-05-28 | Governance: world-class public repo policy*
