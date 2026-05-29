# Canon-Status Frontmatter Standard

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #3
LAST_UPDATED: 2026-05-29
```

Defines the frontmatter block that every artifact in this repository must carry
to participate in the canon lifecycle.

---

## Required Frontmatter Block

Every artifact (`.md`, `.yaml`, `.json`, `.py`, etc.) should carry a status
block near the top of the file. For Markdown files, use a fenced code block:

````markdown
```
STATUS: <value>
AXIS: <axis-id> — <axis-name>  [optional for non-campaign docs]
RATIFICATION_EVENT_ID: <event-id>  [required when STATUS=RATIFIED]
CANON_STATUS: <value>
TRUST_STATE: <value>
LAST_UPDATED: YYYY-MM-DD
```
````

For YAML/JSON/Python, embed as a comment block at the top:

```yaml
# STATUS: CANDIDATE — NOT CANON
# AXIS: 04 — Metadata & Indexing
# LAST_UPDATED: 2026-05-29
```

---

## `STATUS` Allowed Values

| Value | Meaning |
|---|---|
| `DRAFT` | In a branch or PR; not yet committed to `main` |
| `CANDIDATE — NOT CANON` | Committed; under informal review |
| `UNDER_REVIEW` | Nominated for full council ratification |
| `RATIFIED` | Canonized; `ratification_event_id` required |
| `DEPRECATED` | Superseded; preserved for traceability |

---

## `CANON_STATUS` Allowed Values

| Value | Meaning |
|---|---|
| `DRAFT` | Not committed |
| `CANDIDATE` | Committed, not ratified |
| `RATIFIED` | Full council ratification complete |
| `DEPRECATED` | Retired from active use |

---

## `TRUST_STATE` Allowed Values

See [TRUST_STATE_TAXONOMY.md](./TRUST_STATE_TAXONOMY.md) for full definitions.

| Value | Short meaning |
|---|---|
| `WORKING` | Relay/working-vault layer; not for formal trust decisions |
| `CANDIDATE` | Committed artifact under review |
| `AUTHORITATIVE` | Ratified; use as source of truth |
| `DISPUTED` | Active contradiction or challenge open |
| `DEPRECATED` | Trust retired |

---

## Minimal Valid Frontmatter Examples

**Unratified artifact:**
```
STATUS: CANDIDATE — NOT CANON
LAST_UPDATED: 2026-05-29
```

**Ratified artifact:**
```
STATUS: RATIFIED
RATIFICATION_EVENT_ID: GOV-2026-001
CANON_STATUS: RATIFIED
TRUST_STATE: AUTHORITATIVE
LAST_UPDATED: 2026-05-29
```

---

## Enforcement

- Pre-flight validation (`scripts/validate_artifact_metadata.py`) checks for
  presence of `STATUS` and `LAST_UPDATED`.
- CI gate (`scripts/validate_lattice_quality_gates.py`) fails on missing fields
  for artifacts in campaign axes.

---

## Related

- [TRUST_STATE_TAXONOMY.md](./TRUST_STATE_TAXONOMY.md)
- [RATIFICATION_EVENT_ID_STANDARD.md](./RATIFICATION_EVENT_ID_STANDARD.md)
- [docs/ARTIFACT_METADATA_STANDARD.md](../ARTIFACT_METADATA_STANDARD.md)
