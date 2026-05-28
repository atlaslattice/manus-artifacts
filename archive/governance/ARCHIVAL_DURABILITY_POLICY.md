---
artifact_id: LAUNCH-POLICY-ARCHIVAL-DURABILITY-001
title: Archival Durability and Backup Verification Policy
status: candidate
created: 2026-05-28
owner: council
tags: [launch, archival, durability, backup, preservation]
---

# Archival Durability and Backup Verification Policy

> Defines the approach to ensuring long-term durability of Atlas Lattice artifacts.

status: candidate

---

## Durability Vision

As a world-class knowledge archive, Atlas Lattice must be durable. The artifacts housed here represent unique intellectual property and protocols that should be available to future generations. Durability means: the archive survives hardware failure, platform changes, and organizational transitions.

---

## Current Durability Layer: GitHub

**GitHub as canonical substrate** (see ADR-0001) provides:
- Distributed git repository (every clone is a backup)
- 99.9% uptime SLA from GitHub
- Archived repositories persist even for defunct organizations
- GitHub Archive Program stores public repositories in the Arctic Code Vault

For all current and near-term purposes, GitHub provides sufficient durability.

---

## Enhanced Durability Measures

### 1. Contributor Forks as Distributed Backups

Every fork of the repository is a full backup. Encouraging forks increases durability:
- "Fork this repository" is prominently mentioned in the README
- Open Data Export Packs (see OPEN_DATA_EXPORT_PACKS.md) are distributed downloads, not just GitHub assets

---

### 2. Annual Backup Drill

Each year, verify that:
1. The repository can be fully cloned from scratch
2. All tests pass on a fresh clone
3. The KG index rebuilds cleanly from scratch
4. Release assets are downloadable

**Drill record:** Stored in `archive/governance/BACKUP_DRILL_LOG.md`

---

### 3. External Archive Candidates (Phase 2)

For long-term durability beyond GitHub:
- **Software Heritage** (https://www.softwareheritage.org) — academic archive of public repositories
- **Zenodo** (https://zenodo.org) — CERN's open research archive; accepts GitHub releases
- **IPFS/Filecoin** — decentralized storage for critical artifacts

These will be evaluated as Atlas Lattice approaches v1.0.

---

## Durability Checklist

| Item | Status | Target |
|------|--------|--------|
| GitHub as primary store | ✅ Active | Ongoing |
| Open Data Pack releases | 📋 Planned | v2026.Q3.0 |
| Software Heritage registration | 📋 Planned | 2027 |
| Annual backup drill | 📋 Planned | 2027-05-28 |
| Zenodo releases | 📋 Planned | v1.0 |

---

*Atlas Lattice Foundation · status: candidate*
