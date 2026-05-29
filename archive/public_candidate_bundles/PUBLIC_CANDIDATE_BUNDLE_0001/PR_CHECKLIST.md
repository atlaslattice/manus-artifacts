# PUBLIC_CANDIDATE_BUNDLE_0001 PR Checklist

Status: candidate staging material  
Canon: no  
Deployment: no  
Authority: none  

Use this checklist before any public candidate bundle change is merged or treated as release-ready.

## Required fields

- [ ] source_id present
- [ ] source_root present
- [ ] raw_export_status present
- [ ] receipt_status present
- [ ] public_release_status present
- [ ] privacy_status present
- [ ] redaction_status present
- [ ] license_status present
- [ ] canon_status present
- [ ] deployment_status present
- [ ] authority_scope present
- [ ] review_state present

## Required receipts

- [ ] source URL or path attached
- [ ] Drive / Notion / GitHub ID recorded where applicable
- [ ] commit SHA recorded for GitHub artifacts
- [ ] SHA-256 recorded for frozen exports where available
- [ ] missing receipts logged when unavailable

## Public-release checks

- [ ] no secrets, keys, tokens, credentials, or env files
- [ ] no private personal data
- [ ] no unreviewed raw transcripts
- [ ] no private negotiation material
- [ ] no third-party material without rights review
- [ ] no unsupported vendor or partner claims
- [ ] no deployment/runtime claims without current receipts
- [ ] no Claude-origin governance authority claims

## Graph doctrine checks

- [ ] graph edge is not promotion
- [ ] cluster is not canon
- [ ] central node is not authority
- [ ] public GitHub is not proof
- [ ] model output is not authority
- [ ] human-root decision required for canon/authority

## Merge note

A checked box means review status, not truth.  
Merge means preservation and inspection, not canon.
