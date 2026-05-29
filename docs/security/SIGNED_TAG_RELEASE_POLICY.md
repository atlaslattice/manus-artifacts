# Signed Tag and Release Policy

Status: candidate release-security policy (not canon)

## Policy

All public release tags should be signed to provide authenticity and integrity
assurance for downstream users.

## Requirements

1. Use annotated tags (`git tag -a`) for releases.
2. Sign release tags with approved maintainer signing keys.
3. Publish signed tag references in release notes.
4. Reject unsigned release tags for official milestone snapshots.

## Verification

- Verify tag signature before release publication.
- Include verification evidence in release checklist artifacts.

## Exceptions

- Emergency hotfix tags may be temporarily unsigned only with explicit incident
  documentation and a follow-up signed replacement tag.
