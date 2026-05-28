# License Compliance Scan Policy

Status: candidate compliance policy (not canon)

## Policy Statement

Dependencies and distributed artifacts must remain compatible with repository
license obligations before release publication.

## Control Requirements

1. Run license-compliance scan before release tagging.
2. Flag unknown or copyleft-risk licenses for maintainer review.
3. Block public release if unresolved license conflicts remain.
4. Record exceptions with explicit rationale and approval.

## Reporting

- Scan date and tool
- Dependency + detected license list
- Policy decision per flagged dependency
- Final release go/no-go outcome
