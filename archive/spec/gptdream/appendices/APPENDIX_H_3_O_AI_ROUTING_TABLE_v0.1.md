# Appendix H.3 — O_AI Routing Table v0.1

> **Status:** CANDIDATE BUILD PLAN — NOT CANON
> **Deployment:** NO
> **Authority:** NONE

## H.3.1 Allowed Routing States

1. Ingest -> `AUDIT_REQUIRED`
2. Review -> `AUDIT_PASSED` or `AUDIT_FAILED`
3. Execute -> only when `AUDIT_PASSED`

## H.3.2 Forbidden Route

`Ingest -> Execute` without Atlas/ORCS audit state is forbidden.
