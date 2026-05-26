"""
Execution Request — the full D-Φ-1 / CAS-001-A / Atlas/ORCS gate pipeline.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

Execution routing:
  Execution request
  → D-Φ-1 / CAS-001-A / human gate
  → Atlas / ORCS audit state
  → TIDELOCKBrain if repo / merge-order / code execution is involved
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List
import datetime

from .dphi_gate import check_dphi_gate
from .cas001a_anchor import check_cas001a


TIDELOCK_TRIGGER_TYPES = {"repo", "merge", "code", "deploy", "merge_order"}


@dataclass
class ExecutionRequest:
    request_id: str
    execution_type: str          # e.g., repo, merge, code, deploy, general
    receipt_id: Optional[str]
    safety_pass: bool
    human_permission: bool
    safety_check_id: Optional[str] = None
    provenance_refs: List[str] = field(default_factory=list)
    description: str = ""


@dataclass
class ExecutionResult:
    request_id: str
    permitted: bool
    reason: str
    audit_event_emitted: bool = True
    tidelock_required: bool = False
    atlas_audit_event: Optional[dict] = None
    blocked_by: Optional[str] = None


def process_execution_request(
    request: ExecutionRequest,
) -> ExecutionResult:
    """
    Process an execution request through the full gate pipeline.

    Step 1: D-Φ-1 gate (receipt check)
    Step 2: CAS-001-A gate (safety check)
    Step 3: Human permission check
    Step 4: Atlas / ORCS audit state update
    Step 5: TIDELOCKBrain routing if repo/merge/code involved
    """
    # Step 1: D-Φ-1 — receipt required
    dphi = check_dphi_gate(request.receipt_id, request.request_id)
    if not dphi.passed:
        audit_event = _build_audit_event(
            request, permitted=False, reason=dphi.reason,
            tidelock=False,
        )
        return ExecutionResult(
            request_id=request.request_id,
            permitted=False,
            reason=dphi.reason,
            blocked_by="D-Phi-1",
            atlas_audit_event=audit_event,
        )

    # Step 2: CAS-001-A — safety pass required
    cas = check_cas001a(request.safety_pass, request.safety_check_id)
    if not cas.passed:
        audit_event = _build_audit_event(
            request, permitted=False, reason=cas.reason,
            tidelock=False,
        )
        return ExecutionResult(
            request_id=request.request_id,
            permitted=False,
            reason=cas.reason,
            blocked_by="CAS-001-A",
            atlas_audit_event=audit_event,
        )

    # Step 3: Human permission check
    if not request.human_permission:
        reason = "BLOCKED: human_permission is False"
        audit_event = _build_audit_event(
            request, permitted=False, reason=reason, tidelock=False,
        )
        return ExecutionResult(
            request_id=request.request_id,
            permitted=False,
            reason=reason,
            blocked_by="human_permission_gate",
            atlas_audit_event=audit_event,
        )

    # Step 4 & 5: Atlas/ORCS audit + TIDELOCK routing
    tidelock = request.execution_type.lower() in TIDELOCK_TRIGGER_TYPES
    audit_event = _build_audit_event(
        request, permitted=True,
        reason="All gates passed",
        tidelock=tidelock,
    )

    return ExecutionResult(
        request_id=request.request_id,
        permitted=True,
        reason="All gates passed: D-Phi-1, CAS-001-A, human permission",
        tidelock_required=tidelock,
        atlas_audit_event=audit_event,
    )


def _build_audit_event(
    request: ExecutionRequest,
    permitted: bool,
    reason: str,
    tidelock: bool,
) -> dict:
    """Build the atlas-audit-event for this execution request."""
    return {
        "event_type": "execution_permitted" if permitted else "execution_denied",
        "artifact_id": None,
        "actor_seat": "execution_gate",
        "action_description": (
            f"Execution request {request.request_id} "
            f"({'permitted' if permitted else 'denied'}): {reason}"
        ),
        "outcome": "passed" if permitted else "blocked",
        "tidelock_involved": tidelock,
        "tidelock_lane": "TIDELOCKBrain" if tidelock else None,
        "receipt_id": request.receipt_id,
        "safety_pass": request.safety_pass,
        "human_permission": request.human_permission,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
