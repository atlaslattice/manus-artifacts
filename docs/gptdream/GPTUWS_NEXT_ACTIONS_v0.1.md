# GPTUWS Next Actions v0.1

```text
STATUS: NEXT-ACTION LIST — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
CREATED_UTC: 2026-06-07
```

## P0 — Choose target implementation surface

Human-root should choose one:

```text
A. Keep GPTUWS as docs-only candidate in manus-artifacts for now.
B. Create new repo: atlaslattice/gptuws.
C. Create branch in atlaslattice/uws.
D. Integrate under atlaslattice/aluminum-os.
```

Recommended:

```text
Start docs-only in manus-artifacts, then create atlaslattice/gptuws once the module plan is stable.
```

## P1 — Scaffold repository or module folders

Create:

```text
Module_01/
Module_02/
...
Module_12/
A2A/
integration/
benchmark_results/
```

## P2 — Implement minimal runnable skeleton

Start with:

```text
Module_01/evidence_command_surface.py
Module_03/janus_state_memory.py
Module_03/a2a_message_bus.py
Module_06/eval_benchmark_runner.py
Module_12/gptuws_integration_suite.py
```

## P3 — Add tests

Every module gets at least one test file or explicit test waiver.

## P4 — Write first GPT_OUTBOX.md

Use:

```text
docs/gptdream/GPTUWS_A2A_GPT_OUTBOX_TEMPLATE_v0.1.md
```

## P5 — Run first 17-checkpoint audit

Use:

```text
docs/gptdream/GPTUWS_17_CHECKPOINT_AUDIT_TEMPLATE_v0.1.md
```

## Keeper

```text
Do not build everything at once.
Choose surface.
Scaffold.
Run tests.
Write outbox.
Audit.
Then expand.
```