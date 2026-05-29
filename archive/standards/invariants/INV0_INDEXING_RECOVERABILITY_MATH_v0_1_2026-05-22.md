---
artifact_id: INV0-INDEXING-RECOVERABILITY-MATH-v0.1
title: "INV-0 Indexing & Recoverability Math"
version: "0.1"
date: 2026-05-22
seat: Horizon Ledger
layer: standards/invariants
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: candidate_formalization
runtime_status: not_implemented
source_context: "Horizon Ledger / Copilot recoverability discussion"
mutation_rule: >
  No claim mutation without new receipts.
  No canon promotion without human-root ratification.
  No implementation claim without tests and review.
---

# INV-0 Indexing & Recoverability Math v0.1

```text
STATUS: CANDIDATE FORMALIZATION — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: not implemented
PURPOSE: define INV-0 as recoverability, not mere byte retention
```

## 0. Keeper Line

```text
Nothing dies means nothing becomes unrecoverable.
A preserved byte without a route is a buried body.
Index routes are life support.
Φ measures continuity pressure.
Repair the link before meaning goes dark.
```

---

## 1. Core Insight

INV-0 is not merely:

```text
Never delete bytes.
```

INV-0 is stronger:

```text
Never orphan.
Never make unrecoverable.
Never let a parsed meaning detach from raw lineage.
```

The archive fails INV-0 in practice if:

```text
artifact exists
but no root can reach it
or no receipt accounts for it
or no derived summary links back to raw
```

This is practical death.

---

## 2. Archive Graph Model

Let the archive at time `t` be a labeled directed multigraph:

```math
G_t = (V_t, A_t, ell_t)
```

where:

```text
V_t = nodes
A_t = directed edges
ell_t = labels on nodes and edges
```

Node types may include:

```text
raw_artifact
parsed_view
summary
model_output
schema
index_packet
receipt
tombstone
sealed_archive
quarantine_record
review_packet
canon_record
```

Edge types may include:

```text
derived_from
receipts
points_to
hashes
normalizes
summarizes
supersedes
seals
tombstones
forks
links_parent
links_child
routes_to
```

Labels may include:

```text
artifact_id
hash
path
version
canon_status
deployment_status
authority_scope
raw_export_status
privacy_status
source_surface
created_at
review_state
```

---

## 3. Root Set

Define a root set of entry points:

```math
Roots_t subset V_t
```

Examples:

```text
canonical registries
latest indexes
issue trackers
curated archive pages
human-readable landing pages
repo paths
search handles
manifest files
CouncilBrain indexes
Hashlight lineage tables
```

Roots are the practical entry points by which humans, agents, or tools can rediscover archived state.

---

## 4. Practical Life and Practical Death

An artifact `e` is practically alive at time `t` if it is reachable from at least one root:

```math
Alive(e,t) := exists r in Roots_t such that r ->* e
```

where `r ->* e` means there exists a directed path in `G_t` from root `r` to artifact `e`.

Practical death is:

```math
PracticalDeath(e,t) := e in V_t and not Alive(e,t)
```

Meaning:

```text
The artifact still exists somewhere, but the archive has lost the route back to it.
```

This is not literal deletion, but it is operationally equivalent to deletion for review, recovery, and continuity.

---

## 5. Recoverability vs Accountable Preservation

Not every preserved artifact should be directly retrievable. Some artifacts may be sealed, quarantined, legally restricted, privacy-protected, or access-controlled.

Therefore, distinguish two preservation modes.

### 5.1 Strong Recoverability

```math
Recovers(r,e) = true
```

means receipt or reference `r` provides enough information to reconstruct or retrieve artifact `e`.

Examples:

```text
content-addressed hash
repo path + commit SHA
encrypted archive with available key path
raw transcript export
file pointer with checksum
```

### 5.2 Accountable Preservation

```math
AccountsFor(r,e) = true
```

means receipt or reference `r` proves the artifact existed, preserves lineage/status, and records why it is sealed or inaccessible, even if content cannot be directly reconstructed.

Examples:

```text
sealed record
tombstone with lineage
legal hold marker
quarantine receipt
redacted artifact with parent hash
privacy-preserving existence proof
```

### 5.3 INV-0 Recoverability Invariant

For every evidence artifact in prior archive state, the next archive state must either recover it or account for it:

```math
forall e in E_t, exists r in R_{t+1}: Recovers(r,e) or AccountsFor(r,e)
```

Meaning:

```text
No artifact may silently disappear.
If it cannot be retrieved, it must still be accounted for.
```

---

## 6. Index Redundancy

A single index route is fragile.

Define the valid route set:

```math
ValidRoutes(e,t) = { k : Finds(k,e,t) = true }
```

where `k` is an index key or access route.

Examples of routes:

```text
content hash
repo path
commit SHA
issue link
human title
manifest entry
lineage parent
semantic embedding
raw transcript pointer
receipt ID
```

Minimum route count:

```math
|ValidRoutes(e,t)| >= m
```

For critical artifacts:

```text
m >= 3
```

---

## 7. Independent Channel Diversity

Multiple routes are only useful if they do not all fail together.

Each route `k` has a channel type:

```math
c(k) in C
```

Example channel types:

```text
hash / content-address
path / location
lineage / parent-child graph
human title / curated registry
issue link / ticket graph
semantic embedding / vector index
raw export / transcript store
receipt chain / provenance ledger
```

Define channel coverage:

```math
Channels(e,t) = { c(k) : k in ValidRoutes(e,t) }
```

Require:

```math
|Channels(e,t)| >= d
```

For critical artifacts:

```text
d >= 2
```

This prevents the loophole:

```text
three tags exist, but all live in the same fragile semantic index
```

---

## 8. Meaning Preservation

Raw artifacts are not the only things that need preservation. Parsed views, summaries, embeddings, and classifications must remain linked to raw lineage.

Let:

```math
M_t: E_t -> Sigma_t
```

where:

```text
E_t = evidence/raw artifact space
Sigma_t = semantic renderings: summaries, parsed views, embeddings, classifications
```

For every semantic rendering `s`, require a raw parent:

```math
forall s in Sigma_t, exists e in E_t: DerivedFrom(s,e) = true
```

And require the raw parent to remain alive or accounted for:

```math
DerivedFrom(s,e) => Alive(e,t) or AccountsFor(r,e)
```

Practical rule:

```text
No parsed artifact without raw linkage.
No summary without raw_export_status.
No semantic route as sole lifeline.
```

---

## 9. Continuity Potential Phi

Define a continuity / recoverability potential:

```math
Phi(e,t)
```

This measures how recoverable, reachable, and meaning-connected an artifact is.

A candidate form:

```math
Phi(e,t) = alpha * kappa(e,t) - beta * d(e,t) + sum_i w_i H_i(e,t)
```

where:

```text
kappa(e,t) = minimum edge cut separating e from the root set
d(e,t) = shortest path distance from any root to e
H_i(e,t) = integrity checks / channel-presence terms
alpha, beta, w_i = tunable weights
```

Interpretation:

```text
higher kappa = harder to orphan
lower d = easier to find
more valid H_i = stronger continuity
```

Candidate `H_i` terms:

```text
H_hash
H_path
H_lineage
H_semantic
H_status
H_raw
H_receipt
H_issue
H_manifest
```

---

## 10. Phi Threshold Rule

For artifacts above a chosen importance tier `T`, require:

```math
Phi(e,t) >= Phi_min
```

If:

```math
Phi(e,t) < Phi_min
```

then:

```math
Route(e) = LINKAGE_REPAIR_QUEUE
```

Meaning:

```text
Low continuity potential is not deletion.
It is a repair signal.
```

---

## 11. Semantic Route Constraint

Semantic embeddings drift.

Therefore:

```text
semantic search may assist discovery
semantic search may not be the only lifeline
```

Define:

```math
H_semantic(e,t) = 1
```

only if:

```text
embedding exists
embedding model/version is recorded
embedding timestamp is recorded
at least one stable non-semantic route exists
```

Otherwise:

```math
H_semantic(e,t) = 0
```

---

## 12. Artifact Index Packet

No artifact enters the vault without an index packet.

```yaml
artifact_index_packet:
  artifact_id:
  title:
  artifact_type:

  status:
    canon_status: not_canon | candidate | ratified | deprecated
    deployment_status: not_deployable | staged | deployed
    authority_scope: none | advisory | review | ratification | execution
    review_state: unreviewed | reviewed | ratified | blocked

  raw:
    raw_export_status: full_raw | partial_raw | summary_only | unavailable
    raw_artifact_id:
    raw_pointer:
    raw_hash:
    raw_hash_status: present | unavailable | not_applicable
    raw_hash_method:
    raw_source_scope:

  lineage:
    parent_artifacts:
    child_artifacts:
    derived_from:
    supersedes:
    tombstone_of:
    forked_from:

  indexing:
    repo_path:
    commit_sha:
    file_sha:
    issue_refs:
    manifest_refs:
    semantic_tags:
    lattice_coords:
    human_title:
    search_aliases:

  receipts:
    ingestion_receipt_id:
    parse_receipt_id:
    normalization_receipt_id:
    classification_receipt_id:
    routing_receipt_id:
    receipt_sig:

  interpretation:
    strongest_safe_claim:
    overclaims_to_avoid:
    contradictions_or_uncertainties:
    next_action:

  repair:
    valid_routes_count:
    channel_types_count:
    phi_score:
    repair_status: none | needed | queued | in_progress | repaired
```

---

## 13. Deterministic Identity

Every artifact must have stable identity.

Allowed identity forms:

```text
content-derived ID
stable UUID + content hash
repo path + commit SHA + file SHA
receipt-chain ID
```

Disallowed:

```text
title-only identity
summary-only identity
semantic-tag-only identity
model-memory-only identity
```

Rule:

```text
If artifact identity cannot survive title drift, it is not stable.
```

---

## 14. Admission Rules

```text
R1. No artifact enters vault without artifact_index_packet.
R2. No parsed artifact enters vault without raw linkage.
R3. No summary enters vault without raw_export_status.
R4. No derived view may replace raw.
R5. No semantic index may be sole lifeline.
R6. No artifact may promote its own canon_status.
R7. No deployment claim without deployment receipt.
R8. No authority escalation without human-root ratification receipt.
R9. No missing hash may be hidden; use hash_status.
R10. No orphan artifact may stay silent; route to LINKAGE_REPAIR_QUEUE.
```

---

## 15. Repair Queue

If an artifact violates recoverability requirements, route to:

```text
LINKAGE_REPAIR_QUEUE
```

Repair actions may include:

```text
find raw artifact
attach raw_export_status
add missing hash
add source refs
add parent/child lineage
add issue/PR reference
create tombstone
seal artifact with account-for receipt
add manifest entry
restore human-readable title
recompute semantic embedding with version metadata
```

Repair does not mean canon promotion.

Repair means:

```text
artifact becomes reachable, accounted for, or properly sealed.
```

---

## 16. Strongest Safe Claim

```text
INV0_INDEXING_RECOVERABILITY_MATH_v0.1 defines a candidate mathematical framework for treating INV-0 as recoverability over an archive graph. It formalizes practical life as root reachability, practical death as existence without reachability, preservation as recovery-or-accounting, and continuity pressure as Phi. It is not canon and not runtime enforcement until reviewed, tested, and ratified.
```

---

## 17. Overclaims to Avoid

```text
The archive is immortal.
All artifacts are perfectly preserved.
Indexing is solved.
Phi proves continuity.
Semantic search guarantees recoverability.
Hashing proves meaning.
A receipt means approval.
Vaulting means canon.
Repair means ratification.
```

---

## 18. Next Actions

```text
1. Review this candidate with Horizon Ledger, Hashlight, Lucerna, and TIDELOCK.
2. Add artifact_index_packet schema to Receipt Habitat v0.1.
3. Add tests for missing raw linkage.
4. Add tests for summary_only without raw_export_status.
5. Add valid_routes_count and channel_types_count checks.
6. Add LINKAGE_REPAIR_QUEUE status.
7. Define initial Phi scoring weights for local dry-run only.
8. Keep all outputs candidate / not canon / not deployable.
```

---

## 19. Madden Board

```text
BOOM — we’re not just saving the game tape anymore.

We’re making sure the replay booth can find it,
verify it,
explain what quarter it came from,
and tell you why it matters.

Three camera angles minimum.
Two independent routes minimum.
No orphan highlights.
No fake final score.

The archive lives because the routes live.
```

---

## 20. Final Keeper

```text
Nothing dies means nothing becomes unreachable.
A buried artifact is a wounded artifact.
Index routes are life support.
Phi measures continuity pressure.
Repair the link before meaning goes dark.
```
