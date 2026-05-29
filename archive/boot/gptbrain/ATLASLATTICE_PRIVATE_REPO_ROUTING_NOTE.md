# Atlas Lattice Private Repository Routing Note

```text
STATUS: PRIVACY ROUTING NOTE — NOT CANON
DATE: 2026-05-09
RUNTIME_LABEL: WORK_OUTPUT / MODEL_ASSESSMENT
PURPOSE: define safe handling for private Atlas Lattice repositories discovered through the GitHub connector
CANON WARNING: this note does not disclose private repo names, ratify canon, authorize access expansion, or authorize public export.
```

## 0. Operating boundary

Some Atlas Lattice repositories are private.

`atlaslattice/manus-artifacts` is public.

Therefore, private repository names, contents, routes, issues, and implementation details must not be copied into public artifacts unless Dave / human-root explicitly approves disclosure.

## 1. Public artifact rule

In public artifacts, private repositories must be represented as:

```yaml
repo_full_name: REDACTED_CONNECTOR_ONLY
visibility: private
public_export_allowed: false
human_root_required: true
```

## 2. Connector-only routing rule

GPTBrain / ORCS may use private repo context inside an active authorized connector session for:

```text
- private summary for Dave
- route classification
- risk assessment
- duplicate detection
- private issue planning
- private implementation handoff
```

But must not publicly publish:

```text
- private repo names
- private repo URLs
- private file paths
- private issue titles
- private implementation details
- private domain names if sensitive
```

without explicit human-root approval.

## 3. Suggested private route groups

```text
PRIVATE_RESEARCH_ARCHIVES
PRIVATE_DOMAIN_CRITIQUES
PRIVATE_INFRA_OR_CONTEXT_REPOS
PRIVATE_POLICY_DRAFTS
PRIVATE_HEALTH_OR_SAFETY_CONTEXT
PRIVATE_FINANCE_OR_BANKING_CONTEXT
PRIVATE_LAB_OR_EXPERIMENT_CONTEXT
```

## 4. Minimum private route packet

```yaml
repo_route_id: <stable internal id>
repo_full_name: REDACTED_CONNECTOR_ONLY
visibility: private
route_group: <private route group>
source: github_connector
claim_class: parsed_artifact
confidence: C2
runtime_label: WORK
public_export_allowed: false
human_root_required: true
notes: private route exists; details withheld from public artifact
```

## 5. Private-to-public promotion requirements

Before private repo details can be surfaced publicly:

```text
[ ] Dave / human-root explicitly approves disclosure
[ ] sensitive content reviewed
[ ] secrets checked
[ ] personal/private context removed or redacted
[ ] public-safe route name chosen
[ ] claim confidence assigned
[ ] export logged
```

## 6. Madden booth call

BOOM. Public islands go on the tourist map.
Private islands stay under fog until Dave opens the gate.

The archipelago is wired, but privacy is part of the bridge.
