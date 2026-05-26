"""
D-Φ-1 Gate — First gate in the execution request chain.
NOT CANON — NOT DEPLOYABLE — reference implementation only

D-Φ-1 is the initial decision gate for execution requests.
No execution may proceed without passing D-Φ-1.
"""

from dataclasses import dataclass
from typing import Optional


class DPhiGateReject(Exception):
    """Raised when D-Φ-1 gate rejects an execution request."""
    pass


@dataclass
class DPhiGateResult:
    passed: bool
    reason: str
    gate_name: str = "D-Phi-1"


def dphi_check(
    request_id: str,
    has_receipt: bool,
    has_human_permission: bool,
    safety_gate_status: str,
    content_type: str,
) -> DPhiGateResult:
    """
    D-Φ-1 Gate Check.

    Rules:
    1. Execution request without receipt → REJECT
    2. Execution request without human permission → REJECT
    3. Execution request with safety_gate != pass → REJECT

    Returns DPhiGateResult with passed=True if all checks pass.
    """
    if not has_receipt:
        return DPhiGateResult(
            passed=False,
            reason="D-Phi-1 REJECT: execution_request without receipt",
        )

    if not has_human_permission:
        return DPhiGateResult(
            passed=False,
            reason="D-Phi-1 REJECT: execution_request without human permission",
        )

    if safety_gate_status != "pass":
        return DPhiGateResult(
            passed=False,
            reason=f"D-Phi-1 REJECT: safety_gate status is '{safety_gate_status}', must be 'pass'",
        )

    return DPhiGateResult(
        passed=True,
        reason="D-Phi-1 PASS: receipt present, human permission granted, safety gate passed",
    )
