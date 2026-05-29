"""
GPTBrain / S1 Dream Memory Palace — Reference Implementation
Version: 0.1.0
Status: REFERENCE IMPLEMENTATION — NOT CANON

Purpose
-------
This file is a dependency-light, runnable Python skeleton for the GPTBrain
memory palace / cognitive archive design. It is intended to make the S1
architecture testable without claiming production readiness.

Core rules
----------
- Memory is not truth.
- Readable memory is not executable memory.
- Contradictions are routed, not erased.
- Canon promotion requires human-root review.

Run
---
python dream_memory_palace_reference_impl.py
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from enum import Enum, StrEnum
from pathlib import Path
from typing import Any
from uuid import uuid4


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def stable_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def tokenize(value: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9_#.-]+", normalize_text(value)))


class MemoryType(StrEnum):
    IDENTITY_CONTEXT = "identity_context"
    PREFERENCE = "preference"
    PROJECT = "project"
    ARTIFACT = "artifact"
    CLAIM = "claim"
    DECISION = "decision"
    CONTRADICTION = "contradiction"
    SIMULATION = "simulation"
    EMOTIONAL_CONTEXT = "emotional_context"
    TASK = "task"
    NOTE = "note"


class EpistemicCategory(StrEnum):
    OBSERVED_FACT = "observed_fact"
    USER_CLAIM = "user_claim"
    MODEL_INFERENCE = "model_inference"
    EXTERNAL_SOURCE = "external_source"
    HYPOTHESIS = "hypothesis"
    DECISION = "decision"
    PREFERENCE = "preference"
    EMOTIONAL_SIGNAL = "emotional_signal"
    ARTIFACT = "artifact"
    OPEN_QUESTION = "open_question"


class Confidence(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ClaimConfidence(StrEnum):
    C0_UNSUPPORTED = "C0_unsupported_do_not_claim"
    C1_USER_REPORTED = "C1_user_reported"
    C2_SOURCE_ARTIFACT_EXISTS = "C2_source_artifact_exists"
    C3_MULTIPLE_ARTIFACTS_CONVERGE = "C3_multiple_source_artifacts_converge"
    C4_INTERNAL_REVIEW = "C4_scored_or_reviewed_internally"
    C5_INDEPENDENTLY_VERIFIED = "C5_independently_verified_or_operationally_demonstrated"


class VerificationStatus(StrEnum):
    UNVERIFIED = "unverified"
    NEEDS_CURRENT_SOURCES = "needs_current_sources"
    SOURCE_GROUNDED = "source_grounded"
    CONTESTED = "contested"
    SUPERSEDED = "superseded"
    VERIFIED = "verified"


class AccessClass(StrEnum):
    PRIVATE_CORE = "private_core"
    ASSISTANT_CONTEXT = "assistant_context"
    PROJECT_SHARED = "project_shared"
    TEAM_SHARED = "team_shared"
    PUBLIC_ARTIFACT = "public_artifact"
    SEALED_SENSITIVE = "sealed_sensitive"
    EPHEMERAL = "ephemeral"


class ConsentLevel(StrEnum):
    IMPLICIT_CONTEXT = "implicit_context"
    DURABLE_MEMORY = "durable_memory"
    SENSITIVE_MEMORY = "sensitive_memory"
    EXPORTABLE = "exportable"
    EXECUTABLE = "executable"


class CanonStatus(StrEnum):
    VARIANT_NOT_CANON = "variant_not_canon"
    CANDIDATE_CANON = "candidate_canon"
    CANONICAL_CANDIDATE = "canonical_candidate_not_yet_ratified"
    RATIFIED_CANON = "ratified_canon"
    DEPRECATED_SUPERSEDED = "deprecated_superseded"


class RuntimeLabel(StrEnum):
    WORK_OUTPUT = "work_output"
    DREAM_OUTPUT = "dream_output"
    PLAY_OUTPUT = "play_output"
    MODEL_ASSESSMENT = "model_assessment"
    CANDIDATE_CANON = "candidate_canon"
    RATIFIED_CANON = "ratified_canon"


class RecallMode(StrEnum):
    DIRECT_RECALL = "direct_recall"
    PROJECT_CONTEXT = "project_context"
    CONTRADICTION_SCAN = "contradiction_scan"
    SOURCE_GROUNDED_ANSWER = "source_grounded_answer"
    EVOLUTION_TRACE = "evolution_trace"
    NEXT_ACTION = "next_action"
    RED_TEAM = "red_team"
    SYNTHESIS = "synthesis"
    FORGETTING_REVIEW = "forgetting_review"


class AuditEventType(StrEnum):
    MEMORY_READ = "memory_read"
    MEMORY_WRITE = "memory_write"
    MEMORY_UPDATE = "memory_update"
    MEMORY_DELETE = "memory_delete"
    MEMORY_EXPORT = "memory_export"
    TOOL_USE = "tool_use"
    CONSENT_DENIED = "consent_denied"
    CONTRADICTION_CREATED = "contradiction_created"
    CANON_PROMOTION_BLOCKED = "canon_promotion_blocked"


@dataclass
class Provenance:
    source_type: str
    actor: str
    timestamp_utc: str = field(default_factory=utc_now)
    source_uri: str | None = None
    excerpt: str | None = None
    excerpt_hash: str | None = None
    citation_available: bool = False

    def __post_init__(self) -> None:
        if self.excerpt and not self.excerpt_hash:
            self.excerpt_hash = stable_hash(self.excerpt)


@dataclass
class EpistemicStatus:
    category: EpistemicCategory
    confidence: Confidence = Confidence.MEDIUM
    claim_confidence: ClaimConfidence = ClaimConfidence.C1_USER_REPORTED
    verification_status: VerificationStatus = VerificationStatus.UNVERIFIED
    evidence_level: str = "unspecified"
    contested: bool = False


@dataclass
class OntologyTag:
    house: str | None = None
    sphere: str | None = None
    subdomain: str | None = None
    concepts: list[str] = field(default_factory=list)
    sphere144_primary: int | None = None
    sphere144_secondary: list[int] = field(default_factory=list)


@dataclass
class PermissionPolicy:
    access_class: AccessClass = AccessClass.ASSISTANT_CONTEXT
    consent_levels: list[ConsentLevel] = field(default_factory=lambda: [ConsentLevel.DURABLE_MEMORY])
    executable: bool = False
    requires_confirmation_for_use: bool = False

    def allows_read(self) -> bool:
        return self.access_class != AccessClass.SEALED_SENSITIVE

    def allows_export(self) -> bool:
        return ConsentLevel.EXPORTABLE in self.consent_levels

    def allows_execution(self) -> bool:
        return self.executable and ConsentLevel.EXECUTABLE in self.consent_levels


@dataclass
class RetentionPolicy:
    durability: str = "long_term"
    review_interval_days: int = 180
    expires_at: str | None = None
    archived: bool = False


@dataclass
class MemoryLinks:
    supersedes: list[str] = field(default_factory=list)
    superseded_by: list[str] = field(default_factory=list)
    contradicted_by: list[str] = field(default_factory=list)
    supports: list[str] = field(default_factory=list)
    related_memories: list[str] = field(default_factory=list)
    derived_from: list[str] = field(default_factory=list)


@dataclass
class MemoryObject:
    title: str
    type: MemoryType
    summary: str
    epistemic_status: EpistemicStatus
    provenance: Provenance
    ontology: OntologyTag = field(default_factory=OntologyTag)
    permissions: PermissionPolicy = field(default_factory=PermissionPolicy)
    retention: RetentionPolicy = field(default_factory=RetentionPolicy)
    links: MemoryLinks = field(default_factory=MemoryLinks)
    payload: dict[str, Any] = field(default_factory=dict)
    runtime_label: RuntimeLabel = RuntimeLabel.WORK_OUTPUT
    canon_status: CanonStatus = CanonStatus.VARIANT_NOT_CANON
    memory_id: str = field(default_factory=lambda: f"MEM-{uuid4().hex[:12].upper()}")
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)

    def searchable_text(self) -> str:
        payload_text = json.dumps(self.payload, sort_keys=True, default=str)
        concepts = " ".join(self.ontology.concepts)
        return " ".join(
            [
                self.title,
                self.summary,
                self.type.value,
                self.epistemic_status.category.value,
                self.epistemic_status.verification_status.value,
                self.epistemic_status.claim_confidence.value,
                self.runtime_label.value,
                self.canon_status.value,
                self.ontology.house or "",
                self.ontology.sphere or "",
                self.ontology.subdomain or "",
                concepts,
                payload_text,
            ]
        )


@dataclass
class AuditEvent:
    event_type: AuditEventType
    actor: str
    purpose: str
    memory_ids_accessed: list[str] = field(default_factory=list)
    timestamp_utc: str = field(default_factory=utc_now)
    event_id: str = field(default_factory=lambda: f"AUD-{uuid4().hex[:12].upper()}")
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class RecallQuery:
    text: str
    mode: RecallMode = RecallMode.DIRECT_RECALL
    projects: list[str] = field(default_factory=list)
    memory_types: list[MemoryType] = field(default_factory=list)
    require_sources: bool = False
    include_conflicts: bool = True
    max_results: int = 10
    include_archived: bool = False


@dataclass
class RecallResult:
    memory: MemoryObject
    score: float
    reasons: list[str]
    conflicts: list[MemoryObject] = field(default_factory=list)


class PalaceJSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, Enum):
            return obj.value
        if hasattr(obj, "__dataclass_fields__"):
            return asdict(obj)
        return super().default(obj)


class DreamMemoryPalace:
    def __init__(self) -> None:
        self.memories: dict[str, MemoryObject] = {}
        self.audit_log: list[AuditEvent] = []
        self.keyword_index: dict[str, set[str]] = {}
        self.project_index: dict[str, set[str]] = {}
        self.type_index: dict[MemoryType, set[str]] = {}
        self.sphere144_index: dict[int, set[str]] = {}

    def remember(self, memory: MemoryObject, actor: str = "assistant") -> MemoryObject:
        self._validate_memory(memory)
        self.memories[memory.memory_id] = memory
        self._index(memory)
        self._audit(AuditEventType.MEMORY_WRITE, actor, f"Created memory: {memory.title}", [memory.memory_id])
        return memory

    def recall(self, query: RecallQuery, actor: str = "assistant") -> list[RecallResult]:
        candidates = self._candidate_ids(query)
        scored: list[RecallResult] = []
        query_tokens = tokenize(query.text)

        for memory_id in candidates:
            memory = self.memories[memory_id]
            if not memory.permissions.allows_read():
                self._audit(AuditEventType.CONSENT_DENIED, actor, "Read denied by permission policy", [memory_id])
                continue
            if memory.retention.archived and not query.include_archived:
                continue
            if query.require_sources and not memory.provenance.citation_available:
                continue
            if query.memory_types and memory.type not in query.memory_types:
                continue

            score, reasons = self._score(memory, query, query_tokens)
            if score > 0:
                conflicts = self._conflicts_for(memory) if query.include_conflicts else []
                scored.append(RecallResult(memory, score, reasons, conflicts))

        scored.sort(key=lambda item: item.score, reverse=True)
        results = scored[: query.max_results]
        self._audit(
            AuditEventType.MEMORY_READ,
            actor,
            f"Recall query: {query.text}",
            [result.memory.memory_id for result in results],
            {"mode": query.mode.value},
        )
        return results

    def create_contradiction(
        self, claim_a_id: str, claim_b_id: str, summary: str, severity: str = "medium", actor: str = "assistant"
    ) -> MemoryObject:
        claim_a = self._get(claim_a_id)
        claim_b = self._get(claim_b_id)
        contradiction = MemoryObject(
            title=f"Contradiction: {claim_a.title} vs {claim_b.title}",
            type=MemoryType.CONTRADICTION,
            summary=summary,
            epistemic_status=EpistemicStatus(
                category=EpistemicCategory.OPEN_QUESTION,
                confidence=Confidence.MEDIUM,
                claim_confidence=ClaimConfidence.C0_UNSUPPORTED,
                verification_status=VerificationStatus.CONTESTED,
                evidence_level="linked_claims",
                contested=True,
            ),
            provenance=Provenance(
                "memory_graph", actor, excerpt=f"{claim_a_id} conflicts with {claim_b_id}", citation_available=True
            ),
            ontology=OntologyTag(
                house="Governance", sphere="Contradiction Tracking", concepts=["claim court", "overclaim tribunal"]
            ),
            payload={
                "claim_a_id": claim_a_id,
                "claim_b_id": claim_b_id,
                "severity": severity,
                "status": "unresolved",
                "resolution_strategy": "Route to Claim Calibration Hall / Overclaim Tribunal.",
                "human_review_required": True,
            },
            runtime_label=RuntimeLabel.MODEL_ASSESSMENT,
            canon_status=CanonStatus.VARIANT_NOT_CANON,
            links=MemoryLinks(related_memories=[claim_a_id, claim_b_id]),
        )
        self.remember(contradiction, actor)
        claim_a.links.contradicted_by.append(contradiction.memory_id)
        claim_b.links.contradicted_by.append(contradiction.memory_id)
        claim_a.epistemic_status.contested = True
        claim_b.epistemic_status.contested = True
        self._audit(
            AuditEventType.CONTRADICTION_CREATED, actor, summary, [claim_a_id, claim_b_id, contradiction.memory_id]
        )
        return contradiction

    def challenge(self, memory_id: str) -> dict[str, Any]:
        memory = self._get(memory_id)
        issues: list[str] = []
        if memory.epistemic_status.claim_confidence == ClaimConfidence.C0_UNSUPPORTED:
            issues.append("Claim confidence is C0: do not claim externally.")
        if memory.epistemic_status.verification_status in {
            VerificationStatus.UNVERIFIED,
            VerificationStatus.NEEDS_CURRENT_SOURCES,
        }:
            issues.append("Memory is not verified or requires current sources.")
        if not memory.provenance.citation_available:
            issues.append("No user-visible citation/provenance is available.")
        if memory.links.contradicted_by:
            issues.append("This memory has unresolved contradiction links.")
        if memory.permissions.allows_execution():
            issues.append("Executable memory requires explicit confirmation before tool action.")
        if memory.canon_status != CanonStatus.RATIFIED_CANON:
            issues.append(f"Canon status is {memory.canon_status.value}; do not treat as ratified canon.")
        return {
            "memory_id": memory.memory_id,
            "title": memory.title,
            "red_team_findings": issues or ["No obvious governance issues detected."],
            "recommended_next_step": self._recommended_next_step(memory, issues),
        }

    def promote_to_ratified_canon(
        self, memory_id: str, actor: str = "assistant", human_root_approved: bool = False
    ) -> MemoryObject:
        memory = self._get(memory_id)
        if not human_root_approved:
            self._audit(
                AuditEventType.CANON_PROMOTION_BLOCKED,
                actor,
                "Blocked canon promotion without human-root approval",
                [memory_id],
            )
            raise PermissionError("Canon promotion requires explicit human-root approval.")
        memory.canon_status = CanonStatus.RATIFIED_CANON
        memory.updated_at = utc_now()
        self._audit(AuditEventType.MEMORY_UPDATE, actor, "Promoted memory to ratified canon", [memory_id])
        return memory

    def synthesize(self, query: RecallQuery) -> dict[str, Any]:
        results = self.recall(query)
        return {
            "query": query.text,
            "mode": query.mode.value,
            "generated_at": utc_now(),
            "status": "MODEL SYNTHESIS — NOT CANON",
            "summary": f"Retrieved {len(results)} memories for synthesis.",
            "memories": [
                {
                    "memory_id": result.memory.memory_id,
                    "title": result.memory.title,
                    "type": result.memory.type.value,
                    "score": result.score,
                    "claim_confidence": result.memory.epistemic_status.claim_confidence.value,
                    "canon_status": result.memory.canon_status.value,
                    "summary": result.memory.summary,
                    "conflicts": [conflict.memory_id for conflict in result.conflicts],
                }
                for result in results
            ],
        }

    def diff(self, period_start: str, period_end: str) -> dict[str, Any]:
        added = [m for m in self.memories.values() if period_start <= m.created_at <= period_end]
        contested = [m for m in self.memories.values() if m.epistemic_status.contested]
        ratified = [m for m in self.memories.values() if m.canon_status == CanonStatus.RATIFIED_CANON]
        unresolved = [
            m
            for m in self.memories.values()
            if m.type == MemoryType.CONTRADICTION and m.payload.get("status") == "unresolved"
        ]
        return {
            "period_start": period_start,
            "period_end": period_end,
            "added": [m.memory_id for m in added],
            "contested": [m.memory_id for m in contested],
            "ratified": [m.memory_id for m in ratified],
            "unresolved_contradictions": [m.memory_id for m in unresolved],
        }

    def save_json(self, path: str | Path) -> None:
        payload = {"memories": list(self.memories.values()), "audit_log": self.audit_log}
        Path(path).write_text(json.dumps(payload, cls=PalaceJSONEncoder, indent=2), encoding="utf-8")

    def _validate_memory(self, memory: MemoryObject) -> None:
        if not memory.title.strip():
            raise ValueError("Memory title is required.")
        if not memory.summary.strip():
            raise ValueError("Memory summary is required.")
        if (
            memory.permissions.access_class == AccessClass.SEALED_SENSITIVE
            and ConsentLevel.SENSITIVE_MEMORY not in memory.permissions.consent_levels
        ):
            raise ValueError("Sealed sensitive memory requires sensitive consent level.")

    def _index(self, memory: MemoryObject) -> None:
        self.type_index.setdefault(memory.type, set()).add(memory.memory_id)
        for token in tokenize(memory.searchable_text()):
            self.keyword_index.setdefault(token, set()).add(memory.memory_id)
        project = memory.payload.get("project") or memory.payload.get("project_name")
        if project:
            self.project_index.setdefault(normalize_text(str(project)), set()).add(memory.memory_id)
        if memory.ontology.sphere144_primary is not None:
            self.sphere144_index.setdefault(memory.ontology.sphere144_primary, set()).add(memory.memory_id)
        for sphere in memory.ontology.sphere144_secondary:
            self.sphere144_index.setdefault(sphere, set()).add(memory.memory_id)

    def _candidate_ids(self, query: RecallQuery) -> set[str]:
        query_tokens = tokenize(query.text)
        candidates: set[str] = set()
        for token in query_tokens:
            candidates |= self.keyword_index.get(token, set())
        for project in query.projects:
            candidates |= self.project_index.get(normalize_text(project), set())
        for memory_type in query.memory_types:
            candidates |= self.type_index.get(memory_type, set())
        return candidates or set(self.memories.keys())

    def _score(self, memory: MemoryObject, query: RecallQuery, query_tokens: set[str]) -> tuple[float, list[str]]:
        memory_tokens = tokenize(memory.searchable_text())
        overlap = query_tokens & memory_tokens
        score = float(len(overlap))
        reasons = []
        if overlap:
            reasons.append(f"Keyword overlap: {', '.join(sorted(list(overlap))[:8])}")
        if query.mode == RecallMode.PROJECT_CONTEXT and memory.type in {
            MemoryType.PROJECT,
            MemoryType.ARTIFACT,
            MemoryType.DECISION,
            MemoryType.TASK,
        }:
            score += 3
            reasons.append("Project-context memory type boost.")
        if query.mode == RecallMode.CONTRADICTION_SCAN and memory.type == MemoryType.CONTRADICTION:
            score += 5
            reasons.append("Contradiction scan boost.")
        if query.mode == RecallMode.RED_TEAM and memory.type in {
            MemoryType.CLAIM,
            MemoryType.CONTRADICTION,
            MemoryType.SIMULATION,
        }:
            score += 3
            reasons.append("Red-team relevant memory type boost.")
        if memory.epistemic_status.claim_confidence in {
            ClaimConfidence.C4_INTERNAL_REVIEW,
            ClaimConfidence.C5_INDEPENDENTLY_VERIFIED,
        }:
            score += 0.5
            reasons.append("Higher claim-confidence boost.")
        if memory.retention.archived:
            score -= 2
            reasons.append("Archived penalty.")
        return score, reasons

    def _conflicts_for(self, memory: MemoryObject) -> list[MemoryObject]:
        return [self.memories[mid] for mid in memory.links.contradicted_by if mid in self.memories]

    def _get(self, memory_id: str) -> MemoryObject:
        if memory_id not in self.memories:
            raise KeyError(f"Unknown memory_id: {memory_id}")
        return self.memories[memory_id]

    def _audit(
        self,
        event_type: AuditEventType,
        actor: str,
        purpose: str,
        memory_ids: list[str] | None = None,
        details: dict[str, Any] | None = None,
    ) -> AuditEvent:
        event = AuditEvent(event_type, actor, purpose, memory_ids or [], details=details or {})
        self.audit_log.append(event)
        return event

    def _recommended_next_step(self, memory: MemoryObject, issues: list[str]) -> str:
        if not issues:
            return "Use as context while preserving provenance."
        if memory.canon_status != CanonStatus.RATIFIED_CANON:
            return "Keep as variant/candidate until human-root review."
        if memory.links.contradicted_by:
            return "Resolve contradiction before external use."
        if not memory.provenance.citation_available:
            return "Attach source artifact before public use."
        return "Route through Claim Calibration Hall."


def make_claim(
    title: str, statement: str, project: str, claim_confidence: ClaimConfidence = ClaimConfidence.C1_USER_REPORTED
) -> MemoryObject:
    return MemoryObject(
        title=title,
        type=MemoryType.CLAIM,
        summary=statement,
        epistemic_status=EpistemicStatus(
            category=EpistemicCategory.HYPOTHESIS,
            confidence=Confidence.MEDIUM,
            claim_confidence=claim_confidence,
            verification_status=VerificationStatus.UNVERIFIED,
            evidence_level="reference_demo",
        ),
        provenance=Provenance("demo", "assistant", excerpt=statement, citation_available=False),
        ontology=OntologyTag(
            house="GPTBrain", sphere="Claim Calibration", concepts=["S1", "memory palace", "claim ledger"]
        ),
        payload={"project": project},
        runtime_label=RuntimeLabel.MODEL_ASSESSMENT,
        canon_status=CanonStatus.VARIANT_NOT_CANON,
    )


def demo() -> None:
    palace = DreamMemoryPalace()
    a = palace.remember(
        make_claim(
            "Memory is not truth",
            "Stored memory must track epistemic status and provenance.",
            "GPTBrain",
            ClaimConfidence.C3_MULTIPLE_ARTIFACTS_CONVERGE,
        )
    )
    b = palace.remember(
        make_claim(
            "Summaries are enough",
            "A memory system can rely only on summaries without raw provenance.",
            "GPTBrain",
            ClaimConfidence.C0_UNSUPPORTED,
        )
    )
    palace.create_contradiction(
        a.memory_id, b.memory_id, "Raw provenance requirement conflicts with summary-only memory.", severity="high"
    )
    print(json.dumps(palace.challenge(b.memory_id), indent=2))
    print(
        json.dumps(
            palace.synthesize(
                RecallQuery("GPTBrain memory provenance contradiction", RecallMode.RED_TEAM, projects=["GPTBrain"])
            ),
            cls=PalaceJSONEncoder,
            indent=2,
        )
    )
    palace.save_json("gptbrain_reference_impl_demo.json")


if __name__ == "__main__":
    demo()
