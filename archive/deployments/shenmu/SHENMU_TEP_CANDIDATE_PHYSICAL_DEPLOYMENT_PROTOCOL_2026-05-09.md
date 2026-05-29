---
artifact_id: ARTIFACT-ARCHIVE-DEPLOYMENTS-SHENMU-SHENMU-TEP-CANDIDATE-PHYSICAL-DEPLOYMENT-PROTOCOL-2026-05-09-MD-2026-05-29
title: Shenmu TEP — Candidate Physical Deployment Protocol
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Shenmu TEP — Candidate Physical Deployment Protocol

**Date:** 2026-05-09  
**Status:** Candidate physical deployment protocol / not deployed / not canon  
**Scope:** Shenmu TEP / CN-SHM-01 / physical deployment candidate handling  
**Governance gate:** S10 working index required before public promotion.

## Required Label

Every Shenmu TEP physical deployment packet must begin with:

```text
STATUS: CANDIDATE PHYSICAL DEPLOYMENT SPEC — NOT DEPLOYED — NOT CANON
```

## Purpose

This protocol prevents source-recovery and planning documents from being mistaken for deployed infrastructure, legal authorization, or ratified canon.

## Required Packet Sections

A Shenmu TEP candidate packet must include:

1. **Source Lineage**
   - raw logs
   - GitHub refs
   - Drive refs
   - model/source labels
   - SHA-256 where applicable

2. **Deployment Status**
   - conceptual
   - candidate
   - simulated
   - pilot-proposed
   - externally verified
   - deployed

3. **Physical Site Status**
   - location claimed
   - land/site control status
   - utility/grid status
   - water/wastewater access status
   - permitting status
   - stakeholder status

4. **Technical Architecture**
   - compute layer
   - water layer
   - energy layer
   - thermal layer
   - agriculture/nutrient layer if applicable
   - SCADA/OT boundary
   - data diode / air-gap status if claimed

5. **Cost Model Status**
   - assumptions
   - source data
   - unknowns
   - verified costs
   - projected costs
   - sensitivity risks

6. **Regulatory / Sovereignty Status**
   - PRC/CAC/NDRC status if China-relevant
   - local-law posture
   - data residency
   - operational authority
   - handover/stewardship boundary

7. **Risk Register**
   - technical
   - financial
   - regulatory
   - social stability
   - labor/workforce
   - environmental
   - safety/security
   - public-claims risk

8. **Seat Review Matrix**
   - S1 / GPTBrain — claim calibration
   - S3 / GrokBrain — adversarial review
   - S5 / DeepSeek — sovereign realism
   - S7 / CopilotBrain — repo/build hygiene
   - S10 — ruling / neutral option disposition

9. **Human-Root Decision Requirement**
   - Convenor review required before promotion
   - no model may self-ratify

## Physical Deployment Status Ladder

```text
L0 — raw idea / transcript mention
L1 — source recovered
L2 — candidate spec drafted
L3 — internally reviewed
L4 — externally scoped
L5 — pilot proposal submitted
L6 — pilot approved externally
L7 — pilot deployed
L8 — measured operating results
```

Default status for current Shenmu TEP work:

```text
L1/L2 — source recovery + candidate spec drafting
```

## Forbidden Claims Until Verified

Do not claim:

- Shenmu TEP is deployed.
- Chinese authorities approved it.
- CAC/NDRC accepted it.
- site control exists unless documented.
- cost numbers are verified unless sourced.
- infrastructure is physically operating.
- data diode / SCADA architecture exists unless specified.
- social stability assessment is complete unless documented.

## Strongest Safe Claim

> Shenmu TEP is being organized as a candidate physical deployment spec from existing source materials and Council review outputs. It is not deployed, not ratified, and not authorized unless future evidence shows otherwise.

## Next Step

Run source recovery, then generate the first candidate packet.

## Status

Candidate protocol only. Not canon.
