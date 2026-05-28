---
artifact_id: GOV-CANON-CONFLICT-RESOLUTION-PROCESS-v0-1-2026-05-28
title: Canon Conflict Resolution Process
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Canon Conflict Resolution Process

> **Purpose:** Provide a structured path for resolving conflicts between two or more canon-candidate artifacts that make incompatible or contradictory claims.

## Types of Conflicts

| Type | Description | Examples |
|---|---|---|
| **Factual conflict** | Two artifacts assert contradictory facts | Two evidence artifacts give different dates for the same event |
| **Policy conflict** | Two governance artifacts specify incompatible rules | Ratification quorum defined differently in two docs |
| **Structural conflict** | Two artifacts define the same schema/ID namespace differently | Duplicate `artifact_id` values |
| **Scope conflict** | Two artifacts claim ownership of the same domain | Two canon-ownership entries for the same path |
| **Temporal conflict** | A newer artifact invalidates an older ratified one | Updated ADR supersedes prior ADR |

## Resolution Pipeline

```
CONFLICT DETECTED → CONFLICT REPORT OPENED → MEDIATION → ADJUDICATION → RESOLUTION RECORD
```

### Step 1 — Conflict Detection

Any contributor or CI validation may detect and report a conflict. Open an issue or PR linking both conflicting artifacts.

### Step 2 — Conflict Report

File a conflict report entry in the [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md):

```yaml
conflict_id: CONF-YYYY-MM-DD-NNN
date_raised: YYYY-MM-DD
raised_by: "@user"
artifact_a: "ARTIFACT-ID-A"
artifact_b: "ARTIFACT-ID-B"
conflict_type: factual | policy | structural | scope | temporal
description: "one-line summary of the conflict"
status: OPEN
```

### Step 3 — Mediation

Council reviews both artifacts and proposes a resolution path:
- **Merge** — consolidate into a single updated artifact
- **Supersede** — mark one as `ARCHIVED`, the other as authoritative
- **Amend** — patch one or both artifacts to remove contradiction
- **Defer** — escalate to @atlaslattice for adjudication

### Step 4 — Adjudication

@atlaslattice makes the final call using the [Adjudication Evidence Template](./ADJUDICATION_EVIDENCE_TEMPLATE_v0_1.md). Resolution is binding.

### Step 5 — Resolution Record

- Conflict register entry updated: `status: RESOLVED`, `resolution_date`, `resolution_summary`
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md) entry added
- Affected artifact frontmatter updated

## SLA

Conflicts blocking a launch gate must be resolved within the critical-path SLA defined in [Governance SLA Targets](./GOVERNANCE_SLA_TARGETS_v0_1.md).

## Related Artifacts

- [Canon Demotion / Rollback Policy](./CANON_DEMOTION_ROLLBACK_POLICY_v0_1.md)
- [Adjudication Evidence Template](./ADJUDICATION_EVIDENCE_TEMPLATE_v0_1.md)
- [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md)
