# Governance Incident Severity Ladder
Status: Candidate
Date: 2026-05-28

Defines P0-P3 governance incident levels and runbook routing.

| Severity | Definition | Initial response target | Auto-route |
| --- | --- | --- | --- |
| P0 | Canon integrity breach or trust-critical failure | 1 hour | Incident runbook + council emergency lane |
| P1 | High-risk governance failure with external impact | 4 hours | Incident runbook + risk register escalation |
| P2 | Moderate process breakdown | 1 business day | Mission-control weekly lane |
| P3 | Minor policy non-compliance | 3 business days | Standard governance backlog |

## Auto-trigger rules

- Any missing canon-trust fields on promoted artifacts is at least P1.
- Repeated SLA misses on governance-critical docs escalate one level.

## Evidence reviewed

- Evidence reviewed: [INCIDENT_RESPONSE_RUNBOOK.md](./INCIDENT_RESPONSE_RUNBOOK.md)
- Evidence reviewed: [GOVERNANCE_RISK_HEATMAP_THRESHOLDS.md](./GOVERNANCE_RISK_HEATMAP_THRESHOLDS.md)
