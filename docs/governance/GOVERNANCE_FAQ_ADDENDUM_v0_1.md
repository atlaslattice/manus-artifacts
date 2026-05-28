---
artifact_id: GOV-GOVERNANCE-FAQ-ADDENDUM-v0-1-2026-05-28
title: Governance FAQ Addendum
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Governance FAQ Addendum

> **Purpose:** Answer the most common governance questions for contributors and collaborators. Complements [docs/FAQ.md](../FAQ.md).

---

## Canon and Ratification

**Q: What's the difference between CANDIDATE and RATIFIED?**  
A: `CANDIDATE` = published and eligible for review, but not yet adjudicated. `RATIFIED` = full council review + @atlaslattice adjudication complete. Only RATIFIED artifacts carry `trust_state: CANON`.

**Q: Can I rely on a CANDIDATE artifact?**  
A: Yes, as a working reference — but treat it as subject to change. Do not cite a CANDIDATE in a formal ratified artifact without noting its candidate status.

**Q: Who can ratify an artifact?**  
A: Council reviews are advisory; final ratification requires @atlaslattice adjudication. See [Ratification Lifecycle](./RATIFICATION_LIFECYCLE_v0_1.md).

**Q: Can an artifact be ratified without a council vote?**  
A: Only in emergency (P0) situations and only by @atlaslattice acting alone. This must be logged immediately in the Governance Decision Index.

---

## Contributing Artifacts

**Q: How do I submit a new artifact for consideration?**  
A: Open a PR with the artifact, set `status: CANDIDATE`, and add frontmatter. Link it from a parent index. The PR is the opening of the review thread.

**Q: Do I need to fill in all frontmatter fields?**  
A: At minimum: `artifact_id`, `title`, `status`, `owner`, `created`, `source_of_truth`. All other fields are recommended. Artifacts failing metadata validation may be bounced back.

**Q: What if my artifact overlaps with an existing CANDIDATE?**  
A: Check the [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md) and the duplicate artifact detection pass. If overlap is confirmed, initiate the [Canon Conflict Resolution Process](./CANON_CONFLICT_RESOLUTION_PROCESS_v0_1.md).

---

## Domain and Ownership

**Q: Who owns a given artifact?**  
A: The `owner` frontmatter field is authoritative. For domain-level ownership, see [Canon Ownership Map](./CANON_OWNERSHIP_DOMAIN_MAP_v0_1.md).

**Q: What happens if there's no owner field?**  
A: Ownership defaults to @atlaslattice. Add an `owner` field in a metadata backfill PR.

---

## Expiration and Demotion

**Q: Can a RATIFIED artifact be demoted?**  
A: Yes. See [Canon Demotion/Rollback Policy](./CANON_DEMOTION_ROLLBACK_POLICY_v0_1.md). Emergency demotion is immediate; standard demotion follows the adjudication process.

**Q: My CANDIDATE artifact is approaching its TTL — what do I do?**  
A: Either promote it (open a ratification review), request an extension with written rationale, or let it expire to ARCHIVED. See [Candidate Expiration Rules](./CANDIDATE_EXPIRATION_RULES_v0_1.md).

---

## Process and SLAs

**Q: How long does ratification take?**  
A: Target P2 (standard): response within 5 business days, resolution within 30 days. See [Governance SLA Targets](./GOVERNANCE_SLA_TARGETS_v0_1.md).

**Q: Where can I track open governance decisions?**  
A: [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md) and [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md).

---

## Aetherforge / Game Layer

**Q: Does the Aetherforge game framing change governance rules?**  
A: No. Game framing is motivational scaffolding only. All governance rules apply equally to all artifacts regardless of how they are framed.

**Q: Can dream/REM artifacts become canon?**  
A: Yes, if taken through the full ratification cycle. By default they carry `status: CANDIDATE` and `trust_state: NON_CANON`. See [Non-Canon Dream Artifact Policy](../../archive/boot/gptbrain/agents/TIDELOCKBrain/NON_CANON_DREAM_ARTIFACT_POLICY.md).

---

_Last updated: 2026-05-28. Update this FAQ alongside any governance policy changes._
