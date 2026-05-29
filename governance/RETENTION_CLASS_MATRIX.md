# Retention Class Matrix
Status: Candidate
Date: 2026-05-28

Classification matrix for immutable, rolling, and ephemeral artifacts.

| Artifact class | Retention class | Minimum duration | Notes |
| --- | --- | --- | --- |
| Canon decisions | Immutable | Permanent | Never deleted; only superseded |
| Governance packets | Rolling | 7 years | Archived snapshots required |
| Validation receipts | Rolling | 3 years | Keep latest + historical samples |
| Draft planning notes | Ephemeral | 180 days | Preserve if promoted to candidate |
| Temporary scratch artifacts | Ephemeral | 30 days | Must not be canonical sources |

## Related

- [RETENTION_POLICY.md](./RETENTION_POLICY.md)
- [SUCCESSION_STEWARDSHIP.md](./SUCCESSION_STEWARDSHIP.md)
