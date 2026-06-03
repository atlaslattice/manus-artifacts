---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: DOCS-DOCS-20260603-troubleshooting-decision-tree
path: docs/TROUBLESHOOTING_DECISION_TREE.md
domain: docs
lane: contributors
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# Troubleshooting Decision Tree

```text
Start
├─ Broken tests? -> run pytest and inspect failures
├─ Link errors? -> run validate_markdown_links.py
├─ Metadata violations? -> run detect_missing_metadata.py
└─ Governance failures? -> run governance validators
```
