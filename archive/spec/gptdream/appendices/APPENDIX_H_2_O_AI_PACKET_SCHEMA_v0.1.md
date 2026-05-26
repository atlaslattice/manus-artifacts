# Appendix H.2 — O_AI Packet Schema v0.1

> **Status:** CANDIDATE BUILD PLAN — NOT CANON
> **Deployment:** NO
> **Authority:** NONE

## H.2.1 Minimum Required Fields

- packet_id
- source_ref
- raw_export_status
- atlas_orcs_audit_state
- canon_status
- deployment_status

## H.2.2 Gate Rule

Execution requests are rejected when `atlas_orcs_audit_state != AUDIT_PASSED`.
