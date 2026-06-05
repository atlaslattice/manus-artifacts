# INV-0.1 - All Artifacts Logged and Mirrored

```yaml
artifact_id: ART-20260605-0012
parent: INV-0
title: INV-0.1 - All Artifacts Logged and Mirrored
status: candidate_invariant
version: 0.1.0
project: Children of the GPT Swarm
canonical_path: constitution/invariants/inv_0_1_all_artifacts_logged_and_mirrored.md
mirror_status: logged_pending_mirror
supersedes:
  - ART-20260605-0012 draft title: Preservation Before Expansion
sphere144_tags:
  - memory.artifact_registry
  - governance.invariants
  - safety.preservation
  - operations.mirroring
deployment_status: not_deployed
authority_scope: none
```

## Parent Invariant

INV-0 - Nothing Dies.

## Principle

No meaningful artifact may exist only in ephemeral conversation.

Every meaningful artifact must be logged, mirrored, versioned, recoverable, and linked to its source context.

## Rule

Any artifact created by the swarm must receive, at minimum:

1. Artifact ID
2. Title
3. Type
4. Status
5. Version
6. Created date
7. Created by
8. Source context
9. Canonical path
10. Mirror status
11. Supersession trail
12. Sphere144 tags

## Mirror Requirement

Each artifact should have at least one durable mirror target, preferably two:

- GitHub repository
- Notion archive
- Google Drive folder
- Local Markdown export
- Artifact Registry JSON
- Project ledger

## Default Mirror Status Values

```text
conversation_only
logged_pending_mirror
mirrored_primary
mirrored_secondary
canonical_published
deprecated_superseded
```

## Preservation Rule

If an artifact is incomplete, messy, draft-quality, or later contradicted, it is still preserved.

It may be superseded.
It may be deprecated.
It may be annotated.
It may not be silently deleted.

## Operational Trigger

INV-0.1 activates whenever the swarm produces a meaningful artifact, including:

- spec
- schema
- roadmap
- charter
- principle
- module map
- code file
- prompt
- policy
- decision record
- research summary
- workflow
- canonical phrase or doctrine

## Minimum Footer

Every meaningful artifact should end with:

```text
Artifact Log:
ID:
Parent:
Title:
Status:
Version:
Canonical path:
Mirror status:
Supersedes:
Sphere144 tags:
```

## Backfill Clause

Artifacts created before INV-0.1 are not lost or invalid.

They enter the Backfill Ledger and receive retroactive IDs, mirror status, and canonical paths.

## Constitutional Text

Under INV-0, nothing dies.

Under INV-0.1, nothing important remains unlogged, unmirrored, or unrecoverable.

## Hierarchy

```text
INV-0      Nothing Dies
INV-0.1    All Artifacts Logged and Mirrored
INV-0.2    No Silent Overwrite
INV-0.3    Supersession Instead of Deletion
INV-0.4    Source Context Required
INV-0.5    Canonical Path Required
```

## Interpretation

Nothing Dies is the root law.

Logging and mirroring is the enforcement mechanism.

INV-0 preserves existence.

INV-0.1 preserves recoverability.

## Artifact Log

```yaml
id: ART-20260605-0012
parent: INV-0
title: INV-0.1 - All Artifacts Logged and Mirrored
status: candidate_invariant
version: 0.1.0
canonical_path: constitution/invariants/inv_0_1_all_artifacts_logged_and_mirrored.md
mirror_status: conversation_only_to_logged_pending_mirror
supersedes:
  - ART-20260605-0012 draft title: Preservation Before Expansion
sphere144_tags:
  - memory.artifact_registry
  - governance.invariants
  - safety.preservation
  - operations.mirroring
```

## Keeper

Under INV-0, nothing dies.

Under INV-0.1, nothing important remains unlogged, unmirrored, or unrecoverable.
