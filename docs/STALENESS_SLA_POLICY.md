# Staleness Severity + SLA Policy
Status: Candidate
Date: 2026-05-28

Defines severity, service-level targets, and escalation triggers for stale artifacts.

## Severity levels

| Level | Condition | Risk |
| --- | --- | --- |
| S0 | <=30 days since validated update | Low |
| S1 | 31-90 days without update on active surfaces | Moderate |
| S2 | 91-180 days without update or broken references | High |
| S3 | >180 days or governance-critical artifact stale | Critical |

## SLA targets

| Level | Owner acknowledgment | Mitigation plan | Resolution target |
| --- | --- | --- | --- |
| S1 | 5 business days | 10 business days | 30 days |
| S2 | 2 business days | 5 business days | 14 days |
| S3 | 24 hours | 48 hours | 7 days |

## Escalation triggers

- Any S3 condition auto-triggers governance incident triage.
- Two consecutive S2 misses in one domain escalate to council review packet.
- Any stale artifact linked from README Start Here paths must be mitigated within one cycle.

## Related

- [QUALITY_GATES.md](./QUALITY_GATES.md)
- [../governance/INCIDENT_RESPONSE_RUNBOOK.md](../governance/INCIDENT_RESPONSE_RUNBOOK.md)

## Evidence reviewed

- Evidence reviewed: [governance/GOVERNANCE_RISK_HEATMAP_THRESHOLDS.md](../governance/GOVERNANCE_RISK_HEATMAP_THRESHOLDS.md)
- Evidence reviewed: [governance/MISSION_CONTROL_CADENCE.md](../governance/MISSION_CONTROL_CADENCE.md)
