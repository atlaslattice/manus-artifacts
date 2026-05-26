"""
CAS-001-A Anchor — Atlas/ORCS audit state check.
NOT CANON — NOT DEPLOYABLE — reference implementation only

CAS-001-A anchors every execution request to the Atlas/ORCS audit state.
No execution may proceed without creating an Atlas/ORCS audit event.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, List


class CASAnchorError(Exception):
    """Raised when CAS-001-A anchor fails."""
    pass


@dataclass
class CASAuditAnchor:
    """
    CAS-001-A: The Atlas/ORCS audit anchor for execution requests.
    Every execution request creates one of these records.
    The record is IMMUTABLE once created.
    """
    anchor_id: str
    request_id: str
    actor_id: str
    created_at: str
    gate_states: dict
    tidelock_required: bool
    tidelock_lane_metadata: Optional[dict] = None
    resolved: bool = False
    resolution: Optional[str] = None  # approved | rejected | held


@dataclass
class CASAnchorResult:
    passed: bool
    anchor: Optional[CASAuditAnchor]
    reason: str
    gate_name: str = "CAS-001-A"


class CASAnchorStore:
    """In-memory store for CAS-001-A anchors (the Atlas/ORCS audit chain)."""

    def __init__(self):
        self._anchors: dict[str, CASAuditAnchor] = {}

    def add(self, anchor: CASAuditAnchor) -> None:
        self._anchors[anchor.anchor_id] = anchor

    def get(self, anchor_id: str) -> Optional[CASAuditAnchor]:
        return self._anchors.get(anchor_id)

    def get_for_request(self, request_id: str) -> List[CASAuditAnchor]:
        return [a for a in self._anchors.values() if a.request_id == request_id]


def cas001a_anchor(
    request_id: str,
    actor_id: str,
    gate_states: dict,
    content_type: str,
    anchor_store: CASAnchorStore,
) -> CASAnchorResult:
    """
    CAS-001-A: Create an Atlas/ORCS audit anchor for this execution request.

    MANDATORY: Every execution request must create an anchor.
    This is the Atlas/ORCS audit state checkpoint — it CANNOT be bypassed.

    If the request involves repo/code execution, tidelock_required is set to True.
    """
    now = datetime.now(timezone.utc).isoformat()
    anchor_id = f"cas-{request_id}-{now}"

    # Determine if TIDELOCKBrain oversight is required
    tidelock_triggers = {"code", "execution_request", "repo_operation", "merge", "ci_cd"}
    tidelock_required = content_type in tidelock_triggers

    tidelock_lane_metadata = None
    if tidelock_required:
        tidelock_lane_metadata = {
            "lane": "tidelock",
            "reason": f"content_type={content_type} requires TIDELOCKBrain oversight",
            "tidelock_label": "tidelock",
        }

    # Create the anchor record
    anchor = CASAuditAnchor(
        anchor_id=anchor_id,
        request_id=request_id,
        actor_id=actor_id,
        created_at=now,
        gate_states=gate_states,
        tidelock_required=tidelock_required,
        tidelock_lane_metadata=tidelock_lane_metadata,
    )
    anchor_store.add(anchor)

    return CASAnchorResult(
        passed=True,
        anchor=anchor,
        reason=f"CAS-001-A: Audit anchor created ({anchor_id}). TIDELOCK required: {tidelock_required}",
    )
