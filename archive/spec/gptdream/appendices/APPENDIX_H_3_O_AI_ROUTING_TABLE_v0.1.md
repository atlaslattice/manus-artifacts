# Appendix H.3 — O_AI Routing Table v0.1

Status: **NOT CANON**  
Deployment: **NOT DEPLOYABLE**  
Date: 2026-05-26

## H.3.1 Routing states

| State | Requirement | Outcome |
|---|---|---|
| Intake | packet received | candidate pending |
| Schema Validated | schema pass | continue |
| Receipts Verified | >=1 receipt | continue |
| Atlas/ORCS Audited | `atlas_orcs_audit_state` present and pass | continue |
| Human Gated | adjudication complete | approved-candidate or rejected |

## H.3.2 Bypass prohibition

No execution route may bypass Atlas/ORCS audit state.

## H.3.3 Canon-surface wording

Website is a **canon surface when explicitly ratified/published there**.
