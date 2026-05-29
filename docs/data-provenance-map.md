# Data Provenance Map

Status: candidate provenance map (not canon)

## Primary provenance classes

- **Git-native authored artifacts**: docs, workflows, governance, and implementation files committed directly in this repository.
- **Relay-ingested artifacts**: content synchronized from external working vaults (Drive/Notion) into GitHub.
- **Agent-generated artifacts**: machine-assisted drafts, analyses, and templates requiring review.
- **Human-adjudicated artifacts**: governance and canon-bound decisions explicitly approved by authority flow.

## Provenance signal locations

- Commit history and PR trails (GitHub canonical substrate)
- Artifact metadata fields where present
- Governance references and ratification markers
- AI evidence logs under `/docs/ai-evidence/`

## Trust guidance

- Prefer artifacts with explicit source, review, and ratification context.
- Treat unratified artifacts as candidate-state references.
