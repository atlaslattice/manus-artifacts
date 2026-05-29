# Sensitive Term Release Gate

Status: candidate staging material  
Canon: no  
Deployment: no  
Authority: none  

## Purpose

Block publication of artifacts containing sensitive, private, or high-risk
terms until a safety review has been completed and recorded.

## Gated term categories

### Category A — Credential and secret risk

Terms that trigger automatic `do_not_publish` hold:

- API keys, tokens, secrets, passwords, passphrases
- Private URLs or internal endpoint patterns
- Database connection strings
- Private SSH or GPG key material
- OAuth client credentials

### Category B — Personal and private data

Terms that require privacy_status review before release:

- Full legal names of private individuals
- Email addresses of private individuals
- Physical addresses, phone numbers, geolocation data
- Medical, financial, or legal personal information
- Unique identifiers linking to private persons

### Category C — Third-party and rights-unclear material

Terms that require license_status review before release:

- Trademarked brand names used in substantive claims
- Proprietary system names with implied endorsement
- Excerpts or verbatim quotes from third-party copyrighted works
- Vendor partner or client names in non-public contexts

### Category D — Model and authority claim risk

Terms that require claim_review before release:

- "canon", "ratified", "approved", "authorized", "certified" (without receipt)
- "deployed", "production", "live", "released" (without receipt)
- "Claude says", "GPT-4 confirms", "AI proves" (model-output-as-authority)
- "proven", "confirmed", "verified" (without linked evidence receipt)

### Category E — Sensitive project scope

Terms requiring scope review before release:

- Private partner or client project code names
- Internal roadmap milestone labels
- Private negotiation or legal proceeding references
- Personal relationship or communications references

## Gate rule

An artifact containing any Category A term must receive
`public_release_status: do_not_publish` until the term is removed or redacted
and the redaction is receipted.

An artifact containing any Category B–E term must receive
`review_state: review_pending` and route to the appropriate review lane before
`public_release_status` can be set to `public_ready`.

## Review lanes by category

```yaml
category_a: [Hashlight, HumanRoot]
category_b: [Lucerna, HumanRoot]
category_c: [Lucerna, Rootglass, HumanRoot]
category_d: [TIDELOCK, Rootglass, Grok]
category_e: [HumanRoot]
```

## Required receipt fields after review

```yaml
sensitive_term_review:
  artifact_id: ARTIFACT_SLUG
  categories_flagged: []
  reviewed_by: <child_name>
  reviewed_at: YYYY-MM-DDTHH:MM:SSZ
  outcome: <clean | redacted | blocked | escalated>
  redaction_receipt: <path or none>
  authority_scope: advisory_only
  canon_status: not_canon
```

## Keeper

The gate does not decide publication.  
The gate requires a receipt before publication is considered.  
Human-root owns the final whistle.  
When in doubt, hold.
