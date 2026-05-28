---
artifact_id: SEC-POLICY-THREAT-MODELS-001
title: Subsystem Threat Models
status: candidate
created: 2026-05-28
owner: council
tags: [security, threat-model, architecture, supply-chain]
---

# Subsystem Threat Models

> Documents the threat model for each major subsystem of the Atlas Lattice repository.

status: candidate

---

## Threat Modeling Framework

This document uses a simplified STRIDE-based threat model:

| Threat type | Definition |
|------------|-----------|
| **S**poofing | Attacker impersonates a legitimate user or component |
| **T**ampering | Unauthorized modification of data or artifacts |
| **R**epudiation | Denial of actions without verifiability |
| **I**nformation Disclosure | Exposure of sensitive data |
| **D**enial of Service | Disruption of availability |
| **E**levation of Privilege | Gaining unauthorized permissions |

---

## Subsystem 1: GitHub Repository

**Trust boundary:** Public internet → GitHub platform → Repository contents

| Threat | STRIDE | Likelihood | Impact | Mitigation |
|--------|--------|-----------|--------|-----------|
| Unauthorized commit to main | T, E | Low | High | Branch protection, required reviews |
| Malicious PR from forked repo | T | Medium | Medium | Required status checks; CODEOWNERS |
| Compromised contributor account | S, T, E | Low | High | MFA required; CODEOWNERS review |
| Supply chain via malicious Action | T, E | Medium | High | SHA pinning; minimal permissions |

---

## Subsystem 2: CI/CD Pipeline

**Trust boundary:** GitHub Actions runner → Repository → External services

| Threat | STRIDE | Likelihood | Impact | Mitigation |
|--------|--------|-----------|--------|-----------|
| Secret exfiltration via compromised action | I | Medium | Critical | SHA pinning; minimal `GITHUB_TOKEN` perms |
| Cache poisoning | T | Low | High | Cache keys include lockfile hash |
| GITHUB_TOKEN abuse | E | Low | High | Read-only default permissions |
| Workflow modification | T | Low | High | `.github/workflows/` in CODEOWNERS |

---

## Subsystem 3: Knowledge Graph Data

**Trust boundary:** Contributors → Markdown files → KG index → Public users

| Threat | STRIDE | Likelihood | Impact | Mitigation |
|--------|--------|-----------|--------|-----------|
| Injection of false provenance claims | T, R | Medium | Medium | Ratification process; audit trail |
| Orphan artifact manipulation | T | Low | Low | Orphan detection CI gate |
| Schema drift breaking consumers | D | Low | Medium | Schema validation CI gate |
| PII exposure in work logs | I | Medium | High | PII redaction rubric; pre-commit check |

---

## Subsystem 4: GPTBrain/TIDELOCKBrain Archives

**Trust boundary:** AI agents → Dream journals/work logs → Hydration consumers

| Threat | STRIDE | Likelihood | Impact | Mitigation |
|--------|--------|-----------|--------|-----------|
| Injection of false memory claims | T, R | Low | Medium | Work logs are candidate-only; @atlaslattice ratification required |
| AI evidence logs used to impersonate @atlaslattice | S | Low | High | Canon hierarchy: only @atlaslattice ratifies |
| Sensitive internal context leaked in public logs | I | Medium | Medium | AI evidence integrity check; PII rubric |

---

## Review Cadence

Threat models are reviewed annually and updated when:
- A new subsystem is added
- A high-severity vulnerability is discovered
- A significant architecture change occurs

Next review: **2027-05-28**

---

*Atlas Lattice Foundation · status: candidate*
