# Repository Naming Conventions

Status: candidate naming standard (not canon)

## File Naming

- Prefer lowercase kebab-case for operational docs and scripts.
- Use explicit date suffixes (`YYYY-MM-DD`) for time-scoped artifacts when relevant.
- Use uppercase + underscores only when preserving established historical conventions.

## Directory Naming

- Prefer lowercase kebab-case directory names.
- Keep names semantic and domain-oriented (e.g., `ai-evidence`, `three-tier-autonomy`).

## Board and Program Artifacts

- Execution boards should include scope + date in filename:
  - `aetherforge-top10-taskboard-YYYY-MM-DD*.md`
  - `aetherforge-top50-taskboard-YYYY-MM-DD.md`
  - `aetherforge-144-task-campaign-YYYY-MM-DD.md`

## Stability Rule

- Avoid renaming legacy historical artifacts unless required for security or legal remediation.
- If renames are required, preserve redirect/reference links in index documents.
