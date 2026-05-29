# Retention Policy
Status: Candidate
Date: 2026-05-26

This policy defines rules for retention, immutability, supersession, archival, and deletion.
The archive should evolve without erasing the record of how it evolved.

## Core rules

- Public artifacts should be retained unless there is a documented legal, safety, or policy reason not to.
- Material changes to authoritative artifacts should prefer new versions or explicit supersession over silent rewrite.
- Archived and deprecated artifacts should remain linkable whenever feasible.

## Immutability rule

Canon or historically significant artifacts should be treated as effectively immutable except for clearly labeled corrections, metadata fixes, or safety-required notices.
If the substance changes materially, publish a successor artifact instead.

## Supersession rule

When one artifact replaces another, update lineage fields and add a narrative note explaining the relationship.
Supersession is preferred to deletion because it preserves public interpretability.

## Archival vs deletion

Archive when the artifact still has provenance, historical, or explanatory value.
Delete only when retention is impermissible or actively harmful and that decision is itself documented at the governance level where possible.

## Long-term retention guarantee

The operating assumption for this repository is durable public retention on GitHub as canonical substrate, subject to platform, legal, and safety constraints.
Relay copies may exist, but the GitHub record governs.
