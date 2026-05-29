# Incident Response Runbook — Secret/Leak Events

Status: candidate security runbook (not canon)

## Purpose

Provide a repeatable response flow for suspected secret exposure, credential
leaks, or sensitive-data publication incidents.

## Severity Levels

- **SEV-1**: Active credential/token leak with confirmed access risk.
- **SEV-2**: Potential leak, unconfirmed exploitability.
- **SEV-3**: False positive or low-risk historic artifact.

## Response Flow

1. **Triage**
   - Record detection source (scanner, issue, report, workflow).
   - Confirm whether data resembles live credentials or sensitive payloads.
2. **Containment**
   - Revoke/rotate affected credentials immediately.
   - Restrict affected integration access where possible.
3. **Eradication**
   - Remove/redact leaked data from current tree.
   - Evaluate history-rewrite need using public-readiness criteria.
4. **Recovery**
   - Re-run scanners and quality checks.
   - Confirm replacement credentials are functional and limited-scope.
5. **Post-Incident**
   - Log timeline, root cause, and prevention actions.
   - Update policies/checklists if control gaps were found.

## Evidence Requirements

- Detection timestamp (UTC)
- Affected paths/commits
- Rotation/revocation confirmation
- Validation rerun outputs
- Incident closure decision and approver

## Escalation

- Security issues follow `/.github/SECURITY.md`.
- Canon-impacting incidents require governance visibility before ratification.
