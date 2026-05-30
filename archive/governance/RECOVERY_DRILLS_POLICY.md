---
artifact_id: TEST-POLICY-RECOVERY-DRILLS-001
title: Recovery Drills Policy
status: candidate
created: 2026-05-28
owner: council
tags: [testing, reliability, recovery, drills]
---

# Recovery Drills Policy

> Defines scheduled exercises to verify that recovery procedures work when needed.

status: candidate

---

## Why Recovery Drills?

A recovery procedure that has never been tested is a procedure that may not work under stress. Drills verify that:
- Runbooks are accurate and up to date
- Team members know what to do
- Recovery actually works (not just theoretically)

---

## Drill Types

### Drill 1: Secret Rotation Drill

**Scenario:** A GitHub PAT or service token is presumed compromised.
**Frequency:** Annually
**Steps:**
1. Identify a non-critical token to rotate
2. Follow the secret rotation procedure in [INCIDENT_RESPONSE_RUNBOOK.md](./INCIDENT_RESPONSE_RUNBOOK.md)
3. Verify no CI failures after rotation
4. Record drill outcome in `archive/governance/RECOVERY_DRILL_LOG.md`

---

### Drill 2: Branch Recovery Drill

**Scenario:** A bad commit reaches main; rollback is needed.
**Frequency:** Annually (or after first incident)
**Steps:**
1. On a test branch (not main), create a "bad commit" with an intentional error
2. Follow the rollback procedure: revert commit via PR
3. Verify CI passes after revert
4. Record drill outcome

---

### Drill 3: KG Index Rebuild Drill

**Scenario:** KG index is corrupted or deleted.
**Frequency:** Annually
**Steps:**
1. Backup current `kg/` directory
2. Delete `kg/global_index.json`
3. Run `python scripts/build_lattice_global_index.py`
4. Verify index rebuilt correctly and quality gates pass
5. Restore backup; record outcome

---

### Drill 4: Incident Response Tabletop

**Scenario:** A high-severity vulnerability is reported via the public disclosure process.
**Frequency:** Annually
**Steps:**
1. Present a fictional CVE scenario to the security champion
2. Walk through [INCIDENT_RESPONSE_RUNBOOK.md](./INCIDENT_RESPONSE_RUNBOOK.md) step by step (don't execute — tabletop only)
3. Identify gaps or unclear steps
4. Update the runbook with improvements
5. Record outcome

---

## Recovery Drill Log

All drills are recorded in `archive/governance/RECOVERY_DRILL_LOG.md`:

```markdown
| Date | Drill type | Outcome | Issues found | Follow-up actions |
|------|-----------|---------|-------------|------------------|
| YYYY-MM-DD | Secret Rotation | Pass | None | — |
```

---

## Schedule

| Drill | Next scheduled | Owner |
|-------|--------------|-------|
| Secret Rotation Drill | 2027-05-28 | @atlaslattice |
| Branch Recovery Drill | 2027-05-28 | @atlaslattice |
| KG Index Rebuild Drill | 2027-05-28 | Engineering |
| Incident Response Tabletop | 2027-05-28 | Security Champion |

---

*Atlas Lattice Foundation · status: candidate*
