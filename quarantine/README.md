# 🔒 Quarantine Zone — Private-Repo Required

> **Status:** QUARANTINED  
> **Reason:** Contains content with the word "hacker" or content that primarily refers to banking/financial systems  
> **Action Required:** Move to a dedicated **private** repository before this content is safe to remain in a public repo

---

## Why Quarantine?

This directory holds artifacts that match the Atlas Lattice privacy policy:

> *"Anything with the word 'hacker' or referring to banks needs to be quarantined and private."*
> — @atlaslattice, 2026-05-28

These files are **not yet private**. They exist here as a transitional staging zone only.

---

## ⚠️ Required Action (human-root: @atlaslattice)

1. Create a **private** GitHub repository (e.g., `atlaslattice/private-banking-research`)
2. Move the contents of this `quarantine/` directory into that private repo
3. Delete `quarantine/` from this public repo entirely
4. Update links in `docs/domains/projects.md` and README if desired

Until step 3 is done, this content remains technically visible in the public repo.

---

## Quarantined Artifacts

| Path | Reason |
|------|--------|
| `quarantine/projects/free-bank/` | Primary banking revolution project — refers to banks |
| `quarantine/codebases/free-bank/` | Free Bank Technical Blueprint — refers to banks |
| `quarantine/codebases/other/fill_forms.py` | References `Form29_Writ_Garnishment_Bank.pdf` |
| `quarantine/codebases/other/overlay_text_form29.py` | References `Form29_Writ_Garnishment_Bank.pdf` |
| `quarantine/codebases/other/biohacker_sheldon_grok_v5.json` | Contains the word "hacker" (biohacker) |

---

## ORCS Privacy Route

```yaml
quarantine_zone_id: AL-QUARANTINE-001
date: 2026-05-28
trigger_policy: word="hacker" OR content_refers_to=banking
route_group: PRIVATE_FINANCE_OR_BANKING_CONTEXT
visibility: quarantine (transitional — move to private)
public_export_allowed: false
human_root_required: true
action_required: move-to-private-repo
```

---

*Filed by: TIDELOCK / Copilot Agent | 2026-05-28*
