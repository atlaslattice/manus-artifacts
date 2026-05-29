# GPTDream++ Open Protocol Surface
Status: Candidate
Date: 2026-05-27

This index defines the public protocol surface for GPTDream++.
Goal: make specs, schemas, reference implementations, and tests easy to discover and validate as an open-source gift.

## Package structure

- **Specs (candidate protocol doctrine)**
  - [GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md](./GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md)
  - [LANE_ROUTING_CONVENTIONS_v0.1.md](./LANE_ROUTING_CONVENTIONS_v0.1.md)
  - [appendices/](./appendices/)
- **Schemas (machine-parseable contracts)**
  - [../../../schemas/README.md](../../../schemas/README.md)
- **Reference implementations (executable behavior references)**
  - [../../../reference_impl/README.md](../../../reference_impl/README.md)
- **Tests (public verification evidence)**
  - [../../../tests/README.md](../../../tests/README.md)

## Candidate vs canon boundary

- This surface is public and open-source, but remains Candidate unless promoted through governance workflow.
- Canon authority requires ratification and adjudication; publication polish alone is not canon proof.

## Validation entry points

- `python -m pytest -q tests/test_schema_parsing.py tests/adversarial tests/test_oai_packet_examples.py tests/test_native_thread_packet_examples.py reference_impl/atlas_orcs/tests/test_compatible.py`
- `cd archive/boot/gptbrain/reference_impl && python -m pytest -q && bash run_checks.sh`

## Related

- [../../../docs/CANON_BOUNDARY.md](../../../docs/CANON_BOUNDARY.md)
- [../../../docs/QUALITY_GATES.md](../../../docs/QUALITY_GATES.md)
