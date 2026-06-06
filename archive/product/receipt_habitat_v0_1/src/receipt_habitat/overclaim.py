"""Overclaim Gate v0.1.

This module is intentionally simple. It detects language that may imply canon,
deployment, authority, verification, or false completeness before receipts exist.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List


class Severity(str, Enum):
    PATCH = "patch"
    BLOCK = "block"


@dataclass(frozen=True)
class OverclaimFinding:
    term: str
    severity: Severity
    reason: str


PATCH_TERMS = {
    "canon",
    "canonically registered",
    "ratified",
    "sealed",
    "signature",
    "verified",
    "complete",
    "final",
    "fully reconciled",
    "zero faults",
    "perfect",
}

BLOCK_TERMS = {
    "deployed",
    "production-ready",
    "runtime active",
    "enforcement active",
    "authority granted",
}


def scan_text(text: str) -> List[OverclaimFinding]:
    """Return overclaim findings for risky terms in text.

    This is a blunt v0.1 phrase detector. It should be upgraded later to
    sentence-level context analysis, but blunt is fine for the first receipt gate.
    """
    lowered = text.lower()
    findings: List[OverclaimFinding] = []

    for term in sorted(PATCH_TERMS):
        if term in lowered:
            findings.append(
                OverclaimFinding(
                    term=term,
                    severity=Severity.PATCH,
                    reason="canon/verification/finality language requires receipt or status patch",
                )
            )

    for term in sorted(BLOCK_TERMS):
        if term in lowered:
            findings.append(
                OverclaimFinding(
                    term=term,
                    severity=Severity.BLOCK,
                    reason="deployment/runtime/authority language is blocked without explicit receipt",
                )
            )

    return findings


def scan_claims(claim_texts: Iterable[str]) -> List[OverclaimFinding]:
    findings: List[OverclaimFinding] = []
    for claim in claim_texts:
        findings.extend(scan_text(claim))
    return findings


def verdict_from_findings(findings: Iterable[OverclaimFinding]) -> str:
    severities = {finding.severity for finding in findings}
    if Severity.BLOCK in severities:
        return "block"
    if Severity.PATCH in severities:
        return "patch"
    return "approve"
