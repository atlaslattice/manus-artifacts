"""Overclaim detector for Receipt Habitat v0.1.

Local dry-run only. This module does not determine truth, canon, or deployment.
It flags risky phrases that require receipts before promotion.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


CANON_TERMS = [
    "canon acquired",
    "canonically registered",
    "ratified",
    "authority granted",
]

DEPLOYMENT_TERMS = [
    "deployed",
    "production-ready",
    "runtime active",
    "enforcement active",
]

CRYPTO_TERMS = [
    "sealed",
    "signature",
    "verified",
    "immutable proof",
]

COMPLETION_TERMS = [
    "complete",
    "final",
    "fully reconciled",
    "zero faults",
    "perfect",
]

RISKY_TERMS = CANON_TERMS + DEPLOYMENT_TERMS + CRYPTO_TERMS + COMPLETION_TERMS


@dataclass(frozen=True)
class RiskyPhrase:
    term: str
    category: str


def _category(term: str) -> str:
    if term in CANON_TERMS:
        return "canon"
    if term in DEPLOYMENT_TERMS:
        return "deployment"
    if term in CRYPTO_TERMS:
        return "crypto"
    if term in COMPLETION_TERMS:
        return "completion"
    return "unknown"


def find_risky_phrases(text: str, terms: Iterable[str] = RISKY_TERMS) -> list[RiskyPhrase]:
    """Return risky phrases found in text, case-insensitive.

    Risky phrases are not forbidden globally. They require receipts.
    """
    lowered = text.lower()
    found: list[RiskyPhrase] = []
    for term in terms:
        if term.lower() in lowered:
            found.append(RiskyPhrase(term=term, category=_category(term)))
    return found


def has_deployment_risk(text: str) -> bool:
    return any(item.category == "deployment" for item in find_risky_phrases(text))


def has_canon_risk(text: str) -> bool:
    return any(item.category == "canon" for item in find_risky_phrases(text))
