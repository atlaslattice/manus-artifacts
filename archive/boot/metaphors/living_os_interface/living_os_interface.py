"""Living OS metaphor: offline, candidate-only, deny-by-default interface.

No network calls, provider hooks, persistent identity, live authorization,
service execution, canon promotion, or consciousness-continuity behavior.
All approval declarations are unverified local fixtures, never host grants.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any


class BoundaryError(ValueError):
    """Invalid proposed interface action or candidate metadata."""


@dataclass(frozen=True)
class Service:
    name: str
    kind: str = "adapter"
    authority_scope: str = "none"


@dataclass(frozen=True)
class Gate:
    name: str
    service_name: str
    required_capability: str
    action: str = "read"


@dataclass(frozen=True)
class ApprovalContext:
    approved: bool
    approved_by: str
    scope: str
    reason: str
    evidence_ref: str = ""


@dataclass(frozen=True)
class GateDecision:
    status: str
    reason: str
    subject: str
    gate: str
    executed: bool = False
    authority_verified: bool = False


@dataclass(frozen=True)
class RehydrationResult:
    status: str
    artifact_id: str
    source_ref: str | None = None
    payload: Any = None
    identity_restored: bool = False
    source_verified: bool = False


class LivingOS:
    """In-memory interface sketch. It is not a privilege-enforcement system."""

    PERMITTED_SOURCES = frozenset({"synthetic", "public", "consented_work"})
    PERMITTED_ACTIONS = frozenset({"read", "write", "execute"})

    def __init__(self, name: str):
        self._required(name, "name")
        self.name = name
        self._services: dict[str, Service] = {}
        self._gates: dict[str, Gate] = {}
        self._capabilities: set[tuple[str, str]] = set()
        self._artifacts: dict[str, tuple[str, Any]] = {}
        self._events: list[dict[str, str]] = []

    @staticmethod
    def _required(value: Any, field: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise BoundaryError(f"{field}_required")

    @staticmethod
    def _approved(approval: ApprovalContext | None, scope: str) -> bool:
        return (
            isinstance(approval, ApprovalContext)
            and approval.approved is True
            and approval.approved_by == "HUMAN_ROOT"
            and approval.scope == scope
            and isinstance(approval.reason, str)
            and bool(approval.reason.strip())
        )

    def register_service(self, service: Service) -> None:
        if not isinstance(service, Service):
            raise BoundaryError("typed_service_required")
        self._required(service.name, "service_name")
        if service.authority_scope != "none":
            raise BoundaryError("services_cannot_claim_root_authority")
        if service.name in self._services:
            raise BoundaryError("duplicate_service")
        self._services[service.name] = service

    def register_gate(self, gate: Gate) -> None:
        if not isinstance(gate, Gate):
            raise BoundaryError("typed_gate_required")
        for label, value in (("gate_name", gate.name), ("service_name", gate.service_name),
                             ("required_capability", gate.required_capability)):
            self._required(value, label)
        if gate.action not in self.PERMITTED_ACTIONS:
            raise BoundaryError("unknown_gate_action")
        if gate.service_name not in self._services:
            raise BoundaryError("unregistered_service")
        if gate.name in self._gates:
            raise BoundaryError("duplicate_gate")
        self._gates[gate.name] = gate

    def grant_capability(self, subject: str, capability: str,
                         approval: ApprovalContext | None = None) -> bool:
        """Record a *declared* local permission; default refuses unapproved grants.

        A caller-supplied HUMAN_ROOT string is not authentication. This NEVER
        authorizes any actual host action, even if True is returned.
        """
        self._required(subject, "subject")
        self._required(capability, "capability")
        if not self._approved(approval, f"grant:{subject}:{capability}"):
            self._events.append({"action": "capability_grant", "result": "DENIED"})
            return False
        self._capabilities.add((subject, capability))
        self._events.append({"action": "capability_grant", "result": "LOCAL_FIXTURE_ONLY"})
        return True

    def request_gate(self, subject: str, gate_name: str,
                     approval: ApprovalContext | None = None) -> GateDecision:
        self._required(subject, "subject")
        self._required(gate_name, "gate_name")
        gate = self._gates.get(gate_name)
        if gate is None:
            decision = GateDecision("DENIED", "unknown_gate", subject, gate_name)
        elif (subject, gate.required_capability) not in self._capabilities:
            decision = GateDecision("DENIED", "missing_capability", subject, gate_name)
        elif not self._approved(approval, f"gate:{subject}:{gate_name}"):
            decision = GateDecision("DENIED", "missing_scoped_approval", subject, gate_name)
        else:
            decision = GateDecision("PREVIEW_ONLY", "declaration_unverified_no_service_executed",
                                    subject, gate_name)
        self._events.append({"action": "gate_request", "gate": gate_name,
                             "result": decision.status, "reason": decision.reason})
        return decision

    def register_artifact(self, artifact_id: str, payload: Any, *, source_ref: str,
                          source_mode: str = "synthetic") -> None:
        """Register only explicitly supplied local content, not remote memories."""
        self._required(artifact_id, "artifact_id")
        self._required(source_ref, "source_ref")
        if source_mode not in self.PERMITTED_SOURCES:
            raise BoundaryError("private_play_dream_or_unscoped_source_denied")
        if artifact_id in self._artifacts:
            raise BoundaryError("immutable_artifact_identifier")
        self._artifacts[artifact_id] = (source_ref, deepcopy(payload))
        self._events.append({"action": "artifact_register", "result": "LOCAL_FIXTURE_ONLY"})

    def rehydrate_context(self, artifact_id: str) -> RehydrationResult:
        """Retrieve a source-backed snapshot, never a person, mind, or agent."""
        self._required(artifact_id, "artifact_id")
        entry = self._artifacts.get(artifact_id)
        if entry is None:
            return RehydrationResult("NOT_FOUND", artifact_id)
        source_ref, payload = entry
        return RehydrationResult("CONTEXT_PACKET_ONLY", artifact_id,
                                 source_ref=source_ref, payload=deepcopy(payload))

    def audit_events(self) -> tuple[dict[str, str], ...]:
        return tuple(deepcopy(self._events))
