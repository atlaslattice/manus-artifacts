# Tests

status: candidate

Repository test surfaces for schema, adversarial, and artifact validation.

## Local Validation

```bash
python -m pytest -q tests/adversarial tests/notion_mirror
```

## Index
- [Adversarial tests](./adversarial/)
- [Notion mirror tests](./notion_mirror/)

All tests are candidate verification surfaces unless explicitly ratified as canon.
