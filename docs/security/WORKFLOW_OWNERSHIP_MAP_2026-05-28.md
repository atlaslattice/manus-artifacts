---
artifact_id: DOC-WORKFLOW-OWNERSHIP-MAP-2026-05-28
title: Workflow Ownership Map
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Workflow Ownership Map

## Purpose

Map each current GitHub Actions workflow to its primary repository surface and default owner.

## Ownership Table

| Workflow | Surface | Primary owner | Backup reviewer | Notes |
|---|---|---|---|---|
| `docs-link-checks.yml` | Docs / markdown link integrity | @atlaslattice | Council | Public documentation path integrity |
| `gptbrain-reference-checks.yml` | `archive/boot/gptbrain/reference_impl/` | @atlaslattice | Council | Reference implementation quality gate |
| `lattice-kg-quality-gates.yml` | `docs/`, `schemas/`, `scripts/`, tests | @atlaslattice | Council | Core lattice quality workflow |
| `markdown-lint.yml` | Markdown corpus | @atlaslattice | Council | Non-blocking formatting visibility |
| `repo-hygiene-checks.yml` | Whole repo | @atlaslattice | Council | Workflow hygiene and merge-marker detection |
| `secret-scan.yml` | Whole repo / git history | @atlaslattice | @atlaslattice | Sensitive-content protection path |

## Ownership Rule

If no delegated owner is explicitly assigned, workflow ownership defaults to @atlaslattice.
