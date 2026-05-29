# ORCS Mirror State Crosswalk v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none


## Object-to-state map

| Graph object / flag | ORCS state |
| --- | --- |
| `raw_source` | `raw` |
| `parsed_fact` | `parsed` |
| `claim` | `candidate` |
| contamination flags | `quarantined` |
| explicit review packet | `under_review` |
| superseded item | `superseded` |

No Notion page enters `ratified` without a ratification event.

## Compatible-path note

Compatible paths may route candidate material into review lanes, but compatibility is not ratification.

## Laundering example

A summary-only Notion page that says "this is canon" remains `candidate` or `quarantined` until raw provenance and ratification evidence exist. Copying it into GitHub does not launder the claim.

## Review-state transition table

| From | To | Requirement |
| --- | --- | --- |
| `raw` | `parsed` | Raw/source pointer exists. |
| `parsed` | `candidate` | Extracted claim cites source. |
| `candidate` | `under_review` | Review packet opened. |
| `under_review` | `quarantined` | Contamination or blocker found. |
| `under_review` | `superseded` | Newer candidate supersedes it. |
| `under_review` | `ratified` | Explicit ratification event. |

## Failure-state routing table

| Failure | Route |
| --- | --- |
| Missing raw | `quarantined` / `preserve_only` |
| Summary-only completeness claim | `quarantined` / `reject_authority` |
| Unsupported authority | `quarantined` / `reject_authority` |
| Duplicate | `candidate` with duplicate link; no deletion |

## Definition of done

Notion material can enter review without becoming authority.
