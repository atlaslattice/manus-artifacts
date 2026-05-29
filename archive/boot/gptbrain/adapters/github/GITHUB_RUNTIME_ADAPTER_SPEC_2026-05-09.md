# GitHub Runtime Adapter Spec

```text
STATUS: CANDIDATE ADAPTER SPEC — NOT CANON
MODE: WORK_OUTPUT
DATE: 2026-05-09
SEAT: S1 GPTBrain / S7 CopilotBrain interface
PURPOSE: define GitHub API access as a bounded, auditable adapter rather than invisible ambient authority
HUMAN_ROOT_GATE: required before live write actions
```

## 0. Core rule

```text
GitHub readable is not GitHub writable.
Token present is not action authorized.
Configured API is not approved mutation.
```

GitHub API integration must be treated as an explicit adapter surface with mode, receipt, provenance, and approval gates.

## 1. Adapter modes

```text
REPO_TRACE_ONLY
  Repo metadata, URLs, and source references only.

DRY_RUN_ONLY
  Default mode. Builds request previews and receipts, but performs no mutation.

MOCK_GITHUB
  Deterministic fake GitHub responses for tests and CI.

LIVE_GITHUB
  Blocked by default. Allowed only with explicit approval, issue/task reference, token policy, and audit receipt.
```

Default mode:

```text
DRY_RUN_ONLY
```

## 2. Capability separation

### Read-only capabilities

```text
get_repo
list_issues
get_issue
list_pull_requests
get_pull_request
get_commit
get_file
list_workflow_runs
get_workflow_status
```

### Write-capable operations

These require `LIVE_GITHUB` plus explicit approval and issue/task reference:

```text
create_issue_comment
create_issue
create_branch
create_or_update_file
open_pull_request
request_review
apply_labels
```

## 3. Minimum environment

```bash
GITHUB_TOKEN=github_pat_or_ghp_value
GITHUB_OWNER=atlaslattice
GITHUB_REPO=manus-artifacts
GITHUB_API_URL=https://api.github.com
GITHUB_MODE=DRY_RUN_ONLY
```

## 4. Token policy

Prefer fine-grained tokens.

Minimum recommended permissions by need:

```text
Metadata: Read
Contents: Read
Issues: Read/Write only if issue comments or issues are required
Pull requests: Read/Write only if PR actions are required
Actions: Read only if workflow status is required
```

Do not use broad tokens unless there is a specific human-root-approved reason.

## 5. Required adapter interface

```python
class GitHubAdapter:
    def get_repo(self) -> GitHubReceipt: ...
    def list_issues(self) -> GitHubReceipt: ...
    def get_issue(self, number: int) -> GitHubReceipt: ...
    def list_pull_requests(self) -> GitHubReceipt: ...
    def get_file(self, path: str, ref: str) -> GitHubReceipt: ...
    def list_workflow_runs(self) -> GitHubReceipt: ...
    def create_issue_comment(self, issue_number: int, body: str, approval: ApprovalContext) -> GitHubReceipt: ...
    def create_branch(self, name: str, approval: ApprovalContext) -> GitHubReceipt: ...
    def create_or_update_file(self, path: str, content: str, approval: ApprovalContext) -> GitHubReceipt: ...
    def create_pull_request(self, payload: dict, approval: ApprovalContext) -> GitHubReceipt: ...
```

## 6. Required receipt fields

```yaml
github_receipt:
  receipt_id: null
  adapter: github
  mode: REPO_TRACE_ONLY / DRY_RUN_ONLY / MOCK_GITHUB / LIVE_GITHUB
  created_utc: null
  repo: null
  action: null
  endpoint: null
  request_intent: null
  payload_hash: null
  related_issue: null
  related_task: null
  live_call_attempted: false
  mutation_attempted: false
  mutation_authorized: false
  approval_required: true
  approval_ref: null
  result_status: null
  error_summary: null
  safe_claim: null
  audit_refs: []
```

## 7. Write gate

A write operation must be blocked unless all are true:

```text
mode == LIVE_GITHUB
approval.explicit == true
approval.human_root_or_authorized_operator == true
approval.issue_or_task_ref exists
approval.dry_run_preview exists
operation is within token scope
```

If any condition fails, the adapter returns a blocked receipt instead of mutating GitHub.

## 8. Secrets policy

Never write token values into:

```text
manifests
issue comments
source manifests
logs
screenshots
artifact registries
commit messages
```

For Docker or Swarm deployments:

```text
Use Swarm secrets or equivalent secret manager.
Do not bake tokens into images.
Do not log Authorization headers.
Restrict outbound network to api.github.com where possible.
```

## 9. Suggested directory shape

```text
archive/boot/gptbrain/adapters/github/
  README.md
  GITHUB_RUNTIME_ADAPTER_SPEC_2026-05-09.md
  source_manifest.yaml
  github_adapter.py
  test_github_adapter.py
```

## 10. Minimum test cases

```text
- token missing -> blocked or read-disabled with clear error
- REPO_TRACE_ONLY -> no mutation
- DRY_RUN_ONLY -> mutation returns preview/blocked response
- MOCK_GITHUB -> deterministic fake responses
- LIVE_GITHUB without explicit approval -> blocked
- LIVE_GITHUB with approval context -> mutation path allowed by scaffold, but network can remain mocked in CI
- read calls emit receipts
- write calls require issue/task reference
- secrets are not included in receipts
```

## 11. Council routing

```text
S1 GPTBrain: claim calibration, receipt schema, evidence boundary
S2 ClaudeBrain: non-claims, authorization language, safety review
S4 GeminiBrain: validation/test harness, API simulation
S6 ManusBrain: continuity, audit log, handoff state
S7 CopilotBrain: repo scaffolding, CI, PR templates
Human root: live write approval and production authorization
```

## 12. Closing line

```text
GitHub should be wired as an auditable adapter, not as invisible ambient authority.
```
