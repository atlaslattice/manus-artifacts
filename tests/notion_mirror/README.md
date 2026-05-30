# Notion Mirror Tests

status: candidate
canon_status: not_canon
deployment_status: not_deployable

These tests exercise safe validation rules for candidate Notion mirror root packets. They are intentionally local and boring: bad mirror packets fail safely with actionable errors before synthesis or graph promotion.

Run:

```bash
python -m pytest tests/notion_mirror -q
```
