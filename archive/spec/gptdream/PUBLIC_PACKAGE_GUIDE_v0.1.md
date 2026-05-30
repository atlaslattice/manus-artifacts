# GPTDream++ Public Package Guide v0.1

status: candidate  
canon_status: not_canon  
deployment_status: not_deployable  
authority: none  
updated: 2026-05-27

---

## Goal

Provide one public entrypoint for adopters who want to explore GPTDream++ as an open-source protocol stack.

## Package Layout

| Layer | Path | Notes |
|------|------|-------|
| Core protocol | `archive/spec/gptdream/GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md` | Candidate protocol definition |
| Appendix bundle | `archive/spec/gptdream/appendices/` | Interop, routing, Atlas/ORCS governance, failure modes |
| Schema bundle | `schemas/atlas_orcs/v0_1/`, `schemas/o_ai/v0_1/`, `schemas/native_thread/v0_1/` | Machine-readable contract layer |
| Reference implementations | `reference_impl/atlas_orcs/`, `reference_impl/execution_gate/`, `reference_impl/native_thread/` | Python implementation surfaces |
| Adversarial tests | `tests/adversarial/` | Security and robustness probes |
| Vault manifest | `archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md` | Index of included artifacts |

## Validation-First Usage

Run established checks before publishing changes to protocol, schemas, or reference implementations:

```bash
cd archive/boot/gptbrain/reference_impl
python -m pytest -q
bash run_checks.sh
```

## Governance Boundary

Everything in this package is candidate state by default.  
Canon promotion requires council review, adjudication by @atlaslattice, and explicit ratification evidence.
