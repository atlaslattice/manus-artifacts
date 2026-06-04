# ADR-0001 Public Scope Decision

> **Status:** CANDIDATE  
> **Artifact Type:** adr  
> **Stable ID:** AL-ADR-001  
> **Date:** 2026-05-28

## Context

Atlas Lattice is moving additional archive, governance, and graph-automation surfaces into the public repository. This ADR records the candidate decision to keep discoverability and machine-readable structure public by default.

## Decision

1. Registry, graph, and navigation surfaces should live in-repo.
2. Candidate status must be explicit on newly published documentation.
3. Public release does not imply canon ratification.

## Consequences

- New contributors can discover core surfaces without private context.
- Governance controls remain anchored in ratification and trust-state workflows.
- Future ADRs can refine publication boundaries without breaking this baseline.

## Related Topics

- [Governance topic](../topics/governance.md)
- [Knowledge graph topic](../topics/knowledge-graph.md)
