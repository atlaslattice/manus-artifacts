"""
Execution Request Processing
NOT CANON — NOT DEPLOYABLE — reference implementation only

Processes execution requests through the full gate chain:
  D-Φ-1 / CAS-001-A / human gate → Atlas/ORCS audit state → TIDELOCKBrain

See: archive/spec/gptdream/appendices/APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, List

from dphi_gate import dphi_check, DPhiGateResult, DPhiGateReject
from cas001a_anchor import cas001a_anchor, CASAnchorStore, CASAnchorResult


class ExecutionRequestError(Exception):
    """Raised when an execution request fails the gate chain."""
    pass


@dataclass
class GateChainState:
    """State of all gates in the execution request chain."""
    provenance_gate: str = "pending"
    safety_gate: str = "pending"
    governance_gate: str = "pending"
    data_residency_gate: str = "pending"
    human_permission_gate: str = "pending"
    receipt_gate: str = "pending"

    def all_pass(self) -> bool:
        return all(
            v == "pass" for v in [
                self.provenance_gate, self.safety_gate, self.governance_gate,
                self.data_residency_gate, self.human_permission_gate, self.receipt_gate,
            ]
        )

    def to_dict(self) -> dict:
        return {
            "provenance_gate": self.provenance_gate,
            "safety_gate": self.safety_gate,
            "governance_gate": self.governance_gate,
            "data_residency_gate": self.data_residency_gate,
            "human_permission_gate": self.human_permission_gate,
            "receipt_gate": self.receipt_gate,
        }


@dataclass
class ExecutionRequest:
    """An execution request that must pass the full gate chain."""
    request_id: str
    content_type: str  # code | execution_request | repo_operation | merge | ci_cd
    actor_id: str
    gate_states: GateChainState
    description: str
    receipt_id: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class ExecutionRequestResult:
    """Result of processing an execution request through the gate chain."""
    request_id: str
    approved: bool
    rejection_reason: Optional[str]
    dphi_result: Optional[DPhiGateResult]
    cas_result: Optional[CASAnchorResult]
    tidelock_required: bool
    tidelock_lane_metadata: Optional[dict]
    audit_anchor_id: Optional[str]
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


def process_execution_request(
    request: ExecutionRequest,
    anchor_store: CASAnchorStore,
) -> ExecutionRequestResult:
    """
    Process an execution request through the full gate chain.

    Gate chain:
    1. D-Φ-1 — receipt, human permission, safety check
    2. CAS-001-A — Atlas/ORCS audit anchor (MANDATORY, cannot be bypassed)
    3. TIDELOCKBrain routing (if repo/code execution)
    4. Final approval check

    Returns ExecutionRequestResult.
    Raises ExecutionRequestError only for critical failures before CAS-001-A.
    """
    gates = request.gate_states

    # Step 1: D-Φ-1 Gate
    dphi_result = dphi_check(
        request_id=request.request_id,
        has_receipt=bool(request.receipt_id) and gates.receipt_gate == "pass",
        has_human_permission=gates.human_permission_gate == "pass",
        safety_gate_status=gates.safety_gate,
        content_type=request.content_type,
    )

    if not dphi_result.passed:
        return ExecutionRequestResult(
            request_id=request.request_id,
            approved=False,
            rejection_reason=dphi_result.reason,
            dphi_result=dphi_result,
            cas_result=None,
            tidelock_required=True,
            tidelock_lane_metadata=None,
            audit_anchor_id=None,
        )

    # Step 2: CAS-001-A — Atlas/ORCS audit anchor (MANDATORY)
    cas_result = cas001a_anchor(
        request_id=request.request_id,
        actor_id=request.actor_id,
        gate_states=gates.to_dict(),
        content_type=request.content_type,
        anchor_store=anchor_store,
    )

    tidelock_required = cas_result.anchor.tidelock_required if cas_result.anchor else True
    tidelock_lane_metadata = cas_result.anchor.tidelock_lane_metadata if cas_result.anchor else None

    # Step 3: Full gate chain check
    if not gates.all_pass():
        failing = [k for k, v in gates.to_dict().items() if v != "pass"]
        if cas_result.anchor:
            cas_result.anchor.resolved = True
            cas_result.anchor.resolution = "rejected"
        return ExecutionRequestResult(
            request_id=request.request_id,
            approved=False,
            rejection_reason=f"Gate chain not fully passed. Failing gates: {failing}",
            dphi_result=dphi_result,
            cas_result=cas_result,
            tidelock_required=tidelock_required,
            tidelock_lane_metadata=tidelock_lane_metadata,
            audit_anchor_id=cas_result.anchor.anchor_id if cas_result.anchor else None,
        )

    # All gates pass — execution approved
    if cas_result.anchor:
        cas_result.anchor.resolved = True
        cas_result.anchor.resolution = "approved"

    return ExecutionRequestResult(
        request_id=request.request_id,
        approved=True,
        rejection_reason=None,
        dphi_result=dphi_result,
        cas_result=cas_result,
        tidelock_required=tidelock_required,
        tidelock_lane_metadata=tidelock_lane_metadata,
        audit_anchor_id=cas_result.anchor.anchor_id if cas_result.anchor else None,
    )
