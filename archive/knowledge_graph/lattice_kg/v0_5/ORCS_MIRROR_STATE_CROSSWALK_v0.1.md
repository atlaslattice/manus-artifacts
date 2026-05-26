# ORCS Mirror State Crosswalk v0.1

status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority: none

## Object-to-state mapping

| Graph object or flag | ORCS state |
| --- | --- |
| `raw_source` | `raw` |
| `parsed_fact` | `parsed` |
| `claim` | `candidate` |
| contamination flags | `quarantined` |
| explicit review packet | `under_review` |
| superseded item | `superseded` |

## Ratification rule

No Notion page enters `ratified` without a ratification event. A title, GitHub file path, mirror receipt, or review packet is not enough.

## Compatible-path note

Compatible paths preserve raw evidence, parsed claims, review state, contradictions, and supersession records. They do not launder unverified authority into canon.

## Laundering example

A summary-only Notion export says “this is the complete source of truth.” The crosswalk routes it to `quarantined` because `summary_only`, `missing_raw`, and `unsupported_authority` are present. It may become a preserved receipt or delta extraction, but it cannot become `ratified` without raw evidence and a ratification event.

## Review-state transition table

| From | Trigger | To | Guard |
| --- | --- | --- | --- |
| `raw` | parsed packet cites raw | `parsed` | raw/source pointer exists |
| `parsed` | claim extracted | `candidate` | `derived_from` path exists |
| `candidate` | contamination flag found | `quarantined` | preserve source |
| `candidate` | review packet opened | `under_review` | reviewer and scope recorded |
| `under_review` | ratification event recorded | `ratified` | event ID and authority boundary present |
| any | newer cited version displaces | `superseded` | no deletion |

## Failure-state routing table

| Failure | Route |
| --- | --- |
| Missing raw export | `blocked` and request raw source |
| Summary claims completeness | `quarantined` |
| Unsupported authority language | `quarantined` |
| Privacy unresolved | `blocked` pending privacy review |
| Conflicting versions | preserve both and create contradiction |
