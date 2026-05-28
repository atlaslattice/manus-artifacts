# Artifact Integrity Checksum Policy

Status: candidate integrity policy (not canon)

## Purpose

Ensure release artifacts are verifiable and tamper-evident via checksums.

## Policy

1. Generate checksums for release-critical artifacts.
2. Publish checksum manifest alongside release notes.
3. Validate checksum integrity in CI before release publication.
4. Treat checksum mismatch as release blocker.

## Minimum Required Fields

- Artifact path/name
- Hash algorithm (recommended: SHA-256 or stronger)
- Hash value
- Generation timestamp
- Generating workflow/job reference

## Operational Notes

- Re-generate checksums after any artifact rebuild.
- Preserve prior manifests for historical verification trails.
