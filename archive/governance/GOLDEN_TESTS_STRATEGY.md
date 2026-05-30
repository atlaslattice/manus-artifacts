---
artifact_id: TEST-POLICY-GOLDEN-TESTS-001
title: Golden Tests for Key Artifacts
status: candidate
created: 2026-05-28
owner: council
tags: [testing, golden-tests, regression, schemas]
---

# Golden Tests for Key Artifacts

> Defines the golden test strategy for high-value artifacts — ensuring their output remains stable across changes.

status: candidate

---

## What Are Golden Tests?

A **golden test** (also called a snapshot test) captures the expected output of a function or process and stores it as a "golden file". Future test runs compare actual output against the golden file. Any unexpected change fails the test.

Golden tests are especially valuable for:
- Schema parsing (ensuring a schema produces the same Python object structure)
- KG index outputs (ensuring the graph structure is stable)
- Reference implementation outputs (ensuring protocol behavior is stable)

---

## Priority Golden Test Targets

| Artifact | Golden test file | What is captured |
|----------|-----------------|-----------------|
| `schemas/atlas_orcs/v0_1/session_packet.yml` | `tests/golden/session_packet_parsed.json` | Parsed Python object as JSON |
| `schemas/o_ai/v0_1/message.yml` | `tests/golden/oai_message_parsed.json` | Parsed Python object as JSON |
| `kg/global_index.json` (sample) | `tests/golden/kg_index_sample.json` | First 5 nodes of the KG index |
| `reference_impl/atlas_orcs/` main entrypoint | `tests/golden/orcs_output_sample.json` | Output of reference impl on a standard input |
| `archive/governance/METADATA_HEADERS_STANDARD.md` structure | `tests/golden/governance_doc_structure.txt` | Heading structure (h1, h2, h3 list) |

---

## Golden Test Format

```python
import json
import pytest
from pathlib import Path

GOLDEN_DIR = Path("tests/golden")

def test_session_packet_golden():
    """Ensure session_packet schema parses to the expected structure."""
    from scripts.build_lattice_global_index import parse_schema
    actual = parse_schema("schemas/atlas_orcs/v0_1/session_packet.yml")
    golden_path = GOLDEN_DIR / "session_packet_parsed.json"
    
    if not golden_path.exists():
        # First run: create the golden file
        golden_path.write_text(json.dumps(actual, indent=2))
        pytest.skip("Golden file created — re-run tests")
    
    expected = json.loads(golden_path.read_text())
    assert actual == expected, f"Golden test failed. Run with --update-golden to regenerate."
```

---

## Updating Golden Files

When a change is intentional (e.g., a schema is updated), regenerate golden files:

```bash
python -m pytest tests/golden/ --update-golden
```

Or manually delete the `.json` golden file and re-run tests — it will regenerate on first run.

**Always commit updated golden files in the same PR as the change that caused the update.**

---

## CI Behavior

- Golden tests run as part of the boring machine validation suite
- If a golden file is missing: test fails with instructions to generate it
- If a golden file differs: test fails with a diff
- If `--update-golden` flag is passed: golden files are regenerated (CI should never pass this flag)

---

*Atlas Lattice Foundation · status: candidate*
