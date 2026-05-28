# Governance Risk Heatmap with Thresholds
Status: Candidate
Date: 2026-05-28

This heatmap defines threshold-driven escalation for governance and trust risks.
It converts qualitative concern into consistent response timing.

## Scoring model

- Likelihood scale: 1 (rare) to 5 (frequent)
- Impact scale: 1 (low) to 5 (severe)
- Heat score: `Likelihood x Impact`

## Threshold bands

| Heat score | Band | Required response | Review cadence |
| --- | --- | --- | --- |
| 1-4 | Green | Track in routine stewardship notes | Monthly |
| 5-9 | Yellow | Mitigation owner assigned with dated plan | Bi-weekly |
| 10-15 | Orange | Council review packet + mitigation checkpoint | Weekly |
| 16-25 | Red | Incident runbook trigger + adjudicator escalation | Immediate + daily until stabilized |

## Domain overlays

| Domain | Default minimum band | Trigger examples |
| --- | --- | --- |
| Governance | Yellow | unresolved canon conflicts, missing approvals |
| Systems | Yellow | doctrine/metadata drift, broken controls |
| Projects | Yellow | readiness overstatement, unsupported launch claims |
| Research | Orange | high-impact claims without provenance |
| Health | Orange | sensitive publication without framing or verification |
| Vault | Yellow | continuity blind spots and inaccessible records |

## Escalation gates

1. Any Red risk triggers `governance/INCIDENT_RESPONSE_RUNBOOK.md` immediately.
2. Two consecutive Orange reviews without downward movement trigger council escalation.
3. Any unresolved Yellow older than 30 days is promoted for mission-control review.

## Operating notes

- Heatmap updates should align with `governance/RISK_REGISTER.md`.
- Threshold decisions should be recorded in mission-control outputs.
- Bands describe minimum response; stewards can escalate earlier.

## Citations

- Source: [RISK_REGISTER.md](./RISK_REGISTER.md)
- Source: [INCIDENT_RESPONSE_RUNBOOK.md](./INCIDENT_RESPONSE_RUNBOOK.md)
- Source: [MISSION_CONTROL_CADENCE.md](./MISSION_CONTROL_CADENCE.md)
