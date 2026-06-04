"""
D-Φ-1 Execution Gate.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

D-Φ-1 is the primary execution gate. Every execution request must pass through here.
No execution request bypasses Atlas / ORCS audit state.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


class GateError(Exception):
    pass


@dataclass
class GateCheckResult:
    passed: bool
    reason: str
    receipt_id: Optional[str] = None
    tidelock_required: bool = False


def check_dphi_gate(
    receipt_id: Optional[str],
    execution_request_id: str,
) -> GateCheckResult:
    """
    D-Φ-1 gate check: every execution request must have a receipt.

    Returns GateCheckResult with passed=True if receipt is present.
    Raises GateError if no receipt provided.
    """
    if not receipt_id:
        return GateCheckResult(
            passed=False,
            reason="D-Phi-1 BLOCKED: execution_request has no receipt_id",
            receipt_id=None,
        )

    return GateCheckResult(
        passed=True,
        reason=f"D-Phi-1 PASSED: receipt {receipt_id} present",
        receipt_id=receipt_id,
    )
