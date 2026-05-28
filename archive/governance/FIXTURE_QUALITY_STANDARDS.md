---
artifact_id: TEST-POLICY-FIXTURE-QUALITY-001
title: Fixture Quality Standards
status: candidate
created: 2026-05-28
owner: council
tags: [testing, fixtures, quality, standards]
---

# Fixture Quality Standards

> Defines the standards for creating and maintaining test fixtures in the Atlas Lattice repository.

status: candidate

---

## What Are Fixtures?

**Fixtures** are reusable pieces of test infrastructure: sample data files, pytest fixtures (setup/teardown), mock objects, and test schemas. Quality fixtures make tests readable, maintainable, and reliable.

---

## Fixture Types

| Type | Location | Standard |
|------|---------|---------|
| pytest fixtures | `conftest.py` files at appropriate scope | Module-scoped by default; session-scoped for expensive setup |
| Sample data files | `tests/examples/` | Must be valid against their schema; documented |
| Invalid examples | `tests/examples/invalid/` | Must be clearly labeled with the expected failure reason |
| Mock objects | Inline in tests or `tests/mocks/` | Document what they mock and why |
| Golden files | `tests/golden/` | Per the Golden Tests Strategy |

---

## Fixture Naming

```python
# Good: descriptive, noun-form names
@pytest.fixture
def valid_session_packet():
    return {...}

@pytest.fixture
def session_packet_missing_required_fields():
    return {...}

# Bad: vague, verb-form, or generic names
@pytest.fixture
def packet():
    return {...}

@pytest.fixture
def test_data():
    return {...}
```

---

## Fixture Scope Guidelines

| Scope | Use when |
|-------|---------|
| `function` (default) | Fixture modifies state; test isolation is important |
| `module` | Expensive setup shared within a test file; read-only data |
| `session` | Very expensive setup (e.g., loading large schemas); read-only across all tests |

Never use `session` scope for fixtures that modify shared state.

---

## Sample Data File Requirements

All sample data files in `tests/examples/` must:
1. Include a comment or companion `.meta.json` file explaining what they represent
2. Be valid against their declared schema (verified by contract tests)
3. Be named descriptively: `{schema_name}_{scenario}.json` (e.g., `session_packet_minimal.json`)
4. For invalid examples: include `_invalid` in the name and a `// reason: ...` comment explaining the expected failure

---

## Fixture Anti-Patterns

| Anti-pattern | Problem | Fix |
|-------------|---------|-----|
| Hardcoded file paths | Breaks on different OS/working directory | Use `Path(__file__).parent / "examples"` |
| Real credentials in fixtures | Security risk | Use fake/placeholder values |
| Shared mutable state | Test interference | Use function-scoped fixtures |
| Fixtures with side effects (writing to disk, network calls) | Slow, brittle | Mock the side effect; use `tmp_path` for disk |
| Fixture that duplicates production logic | Drifts from real behavior | Import and use the real function; don't replicate it |

---

*Atlas Lattice Foundation · status: candidate*
