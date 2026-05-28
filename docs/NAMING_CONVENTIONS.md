---
title: Naming Conventions
artifact_id: GOVERNANCE-NAMING-CONVENTIONS-2026-05-28
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-28
provenance: Created from Aetherforge Mission #30 execution in repository architecture layer.
---

# Naming Conventions

## Objective

Define stable naming rules so artifacts are easier to discover, automate, and govern.

## Directory Naming

- Prefer lowercase kebab-case for folders: `archive/spec/gptdream/`
- Use singular, purpose-led names for durable domains: `docs/`, `projects/`, `schemas/`
- Avoid spaces and camelCase in path segments

## File Naming

- Prefer uppercase snake case for foundational policy and protocol docs:
  - `CANON_STATUS_MODEL.md`
  - `RATIFICATION_WORKFLOW.md`
- Prefer descriptive kebab-case with date suffix for campaign/taskboard artifacts:
  - `aetherforge-next144-taskboard-2026-05-28.md`
- Use ISO date format `YYYY-MM-DD` in filenames when time-order matters
- Keep one extension only (`.md`, `.py`, `.yml`, `.yaml`, `.json`)

## Metadata and IDs

- `title` should match the human-readable artifact name
- `artifact_id` format: `DOMAIN-SUBDOMAIN-NAME-YYYY-MM-DD`
- `last_updated` must use ISO format `YYYY-MM-DD`
- Governance artifacts must include `canon_status`, `ratification_event_id`, and `trust_state`

## Status Vocabulary

- Use canonical status values from governance docs (`candidate`, `ratified`, `canonical`, etc.)
- Do not invent local one-off status labels in individual files

## Change Safety Rules

- Prefer rename-only changes when standardizing names to preserve content fidelity
- Update all internal links in the same change set
- Avoid unnecessary path churn once an artifact is externally referenced

## Adoption Guidance

- Apply these conventions to all new files immediately
- Migrate legacy paths opportunistically during related edits
- If a convention conflict appears, governance docs take precedence over local usage
