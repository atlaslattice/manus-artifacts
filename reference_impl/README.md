# Reference Implementations

> *Status: CANDIDATE — not canon until ratified by @atlaslattice*

## What This Folder Is

The `reference_impl/` domain contains executable reference implementations for the candidate protocols and governance contracts described elsewhere in the archive. These are not full production systems; they are focused scaffolds meant to prove that key ideas can be encoded, checked, and tested.

There are currently three implementation families: `atlas_orcs` (Python), `execution_gate`, and `native_thread`. Together they cover trust-state logic, execution gating, and ingestion validation, with test suites providing the clearest entry point for understanding expected behavior.

## Start Here

→ [Atlas/ORCS Schema Contract Tests](./atlas_orcs/tests/test_schema_contracts.py)

## Contents

| Resource | Description |
|---|---|
| [`atlas_orcs/`](./atlas_orcs/) | Python implementation of Atlas/ORCS state, ratification, audit, and compatibility logic. |
| [`execution_gate/`](./execution_gate/) | Reference execution gate for D-Φ-1 / CAS-001-A style permission checks. |
| [`native_thread/`](./native_thread/) | Native thread ingestion validator and related code surface. |
| [`atlas_orcs/tests/`](./atlas_orcs/tests/) | Test suite covering state machine, compatibility logic, and schema contracts. |
| [`execution_gate/tests/test_execution_gate.py`](./execution_gate/tests/test_execution_gate.py) | Focused tests for execution-gate behavior and audit-event generation. |

## Related Domains

- [Schemas](../schemas/) — the implementations exist to validate and operationalize these machine-readable contracts.
- [Archive](../archive/) — GPTDream++ spec artifacts describe the protocol layer these implementations target.
- [Codebases](../codebases/) — broader code surfaces and experiments complement these narrower reference scaffolds.

---
*Atlas Lattice Foundation · Austin, Texas*
