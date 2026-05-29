# Validation Tests Index
Status: Candidate
Date: 2026-05-27

This directory contains test suites that validate schema contracts and protocol behavior for the GPTDream++ public package surface.

## Test groups

- Schema parsing and guardrails: `test_schema_parsing.py`, `test_evidence_vault_schema_guards.py`
- Packet examples: `test_oai_packet_examples.py`, `test_native_thread_packet_examples.py`
- Cross-pack guards: `test_atlas_orcs_oai_native_thread_guards.py`
- Adversarial harness: `adversarial/`
- Implementation compatibility: `../reference_impl/atlas_orcs/tests/test_compatible.py`

## Baseline run command

`python -m pytest -q tests/test_schema_parsing.py tests/adversarial tests/test_oai_packet_examples.py tests/test_native_thread_packet_examples.py reference_impl/atlas_orcs/tests/test_compatible.py`

## Related

- [../archive/spec/gptdream/README.md](../archive/spec/gptdream/README.md)
- [../reference_impl/README.md](../reference_impl/README.md)
