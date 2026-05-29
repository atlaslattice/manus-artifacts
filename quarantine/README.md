# Quarantine Zone

```text
STATUS: QUARANTINE — PENDING PRIVATE REPO MIGRATION
DIRECTIVE: PRIVACY ROUTING — MOVE TO PRIVATE REPOSITORY
DATE: 2026-05-28
```

## Why this folder exists

Per Dave / human-root directive (2026-05-28):

> "anything with the word 'hacker' or referring to banks needs to be quarantined and private the rest should be public"

This folder holds artifacts that must be migrated to a **private** repository before continued development. They are staged here as a transit zone until that migration happens.

## Contents pending private migration

| Path | Reason |
|------|--------|
| `codebases/free-bank/` | Bank-focused technical blueprint — financial project content |
| `projects/free-bank/` | Banking revolution archive — financial project content |

## Recommended private repo targets

Per `archive/boot/gptbrain/ATLASLATTICE_PRIVATE_REPO_ROUTING_NOTE.md`:

```yaml
route_group: PRIVATE_FINANCE_OR_BANKING_CONTEXT
visibility: private
public_export_allowed: false
human_root_required: true
```

Suggested private repo: `atlaslattice/free-bank` or `atlaslattice/banking-revolution`

## How to complete migration

1. Create a private repository (e.g. `atlaslattice/atlas-private-finance`)
2. Move all files from this quarantine folder into that private repo
3. Delete this quarantine folder from `manus-artifacts` (public)
4. Update any private navigation surfaces accordingly

## Files currently quarantined

- [`codebases/free-bank/Manus_Free_Bank_Technical_Blueprint.md`](./codebases/free-bank/Manus_Free_Bank_Technical_Blueprint.md)
- [`projects/free-bank/banking-revolution-archive.md`](./projects/free-bank/banking-revolution-archive.md)
