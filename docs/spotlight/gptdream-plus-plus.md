# GPTDream++ Spotlight

> **Status:** CANDIDATE  
> **Artifact Type:** flagship spotlight  
> **Date:** 2026-05-28  
> **Related:** [GPTDream++ Spec Vault README](../../archive/spec/gptdream/README.md), [Open Gift Package Guide](../../archive/spec/gptdream/OPEN_GIFT_PACKAGE_GUIDE_v0.1.md), [Vault Manifest](../../archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md)

## What It Is

<!-- METADATA
stable_id: AL-SYS-313
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

GPTDream++ is the repo's **personal-agent habitat and governance package**. It combines specification docs, schema bundles, execution gates, and adversarial tests into an open-source gift for durable agent memory and trust-aware execution.

## Dream Protocol

The "dream" language in this system is not about canonizing hallucination. It is about rehydration, continuity, and preserving candidate material so agents can resume work without pretending that dream residue equals fact.

## Vault Manifest

The [vault manifest](../../archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md) indexes the spec files, Atlas/ORCS schemas, O_AI packet schema, execution gate reference implementation, and adversarial harness that make the package legible.

## Open-Source Gift Framing

The [open gift package guide](../../archive/spec/gptdream/OPEN_GIFT_PACKAGE_GUIDE_v0.1.md) frames GPTDream++ as a public, candidate-state gift: useful to researchers and builders, but still bound by ratification and trust controls.

## Key Artifacts

- Core habitat protocol
- Vault manifest
- Atlas/ORCS schema bundle
- O_AI routing and packet specs
- Reference implementations
- Adversarial harness

## Test Suite Stats

Current adjacent validation surfaces show:

- **13** adversarial harness tests passing in `tests/adversarial/test_adversarial_harness.py`
- **17** GPTBrain reference-implementation tests passing in `archive/boot/gptbrain/reference_impl`
- **7** scaffold checks passing in `archive/boot/gptbrain/reference_impl/run_checks.sh`

These do not ratify GPTDream++, but they do make its candidate-state package more auditable.
