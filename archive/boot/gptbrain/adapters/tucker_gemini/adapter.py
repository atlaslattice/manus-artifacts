"""
Tucker / Gemini adapter — GPTBrain S1 scaffold.

STATUS: SCAFFOLD — NOT CANON
ISSUE: manus-artifacts#22
RUNTIME_LABEL: REPO_TRACE_ONLY
DRY_RUN_ONLY: true
MOCK_GEMINI: available for local testing only
LIVE_GEMINI: blocked by default — requires human-root approval and secrets policy

This adapter exists to represent Tucker/Gemini in GPTBrain provenance and
boot context.  It does NOT wire live Gemini API calls.

Boundaries enforced here:
- provenance-visible does not mean executable
- boot-visible does not mean canon
- GPT/Gemini-assisted build lineage does not imply runtime dependency
- Tucker references are source/provenance-backed, not operational integration
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


# ---------------------------------------------------------------------------
# Safety constants
# ---------------------------------------------------------------------------

ADAPTER_MODE = "REPO_TRACE_ONLY"
LIVE_GEMINI_AUTHORIZED = False  # never True without human-root approval + secrets policy
DRY_RUN_ONLY = True
MOCK_GEMINI_OUTPUT = "[MOCK] Gemini dry-run response — no live API call was made."


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TuckerGeminiConfig:
    """
    Adapter configuration.

    live_authorized is always False in this scaffold.
    The presence of GEMINI_API_KEY in the environment does NOT authorize
    live calls — explicit human-root approval is required.
    """

    dry_run: bool = True
    use_mock: bool = True
    live_authorized: bool = False
    source_repo: str = "atlaslattice/tucker-gemini-GPT-"
    provenance_file: str = "ARTIFACT_PROVENANCE.md"

    def __post_init__(self) -> None:
        if self.live_authorized:
            raise ValueError(
                "live_authorized=True is blocked in this adapter scaffold. "
                "Human-root approval and a secrets policy are required before "
                "live Gemini calls can be authorized."
            )


def load_config() -> TuckerGeminiConfig:
    """Return the default safe config regardless of environment variables."""
    api_key_present = bool(os.environ.get("GEMINI_API_KEY"))
    # Presence of the key does NOT authorize live calls.
    _ = api_key_present  # acknowledged but not acted upon
    return TuckerGeminiConfig(dry_run=True, use_mock=True, live_authorized=False)


# ---------------------------------------------------------------------------
# Dry-run receipt
# ---------------------------------------------------------------------------

@dataclass
class DryRunReceipt:
    adapter: str = "tucker_gemini"
    mode: str = ADAPTER_MODE
    live_call_attempted: bool = False
    mock_used: bool = True
    timestamp_utc: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    notes: str = (
        "Dry-run receipt only. No live Gemini API call was attempted. "
        "Tucker/Gemini are provenance-wired, not runtime-wired."
    )


def dry_run(prompt: str, config: TuckerGeminiConfig | None = None) -> DryRunReceipt:
    """
    Simulate an adapter invocation without making any live API call.

    Returns a DryRunReceipt documenting that no live call was attempted.
    The prompt is accepted for interface compatibility but is not sent anywhere.
    """
    if config is None:
        config = load_config()

    if config.live_authorized:
        raise ValueError("live_authorized=True is blocked.")

    # No live call; return receipt.
    return DryRunReceipt(live_call_attempted=False, mock_used=config.use_mock)


def mock_gemini(prompt: str) -> str:
    """
    Return deterministic fake Gemini output for local testing.

    This function never contacts any external service.
    """
    return f"{MOCK_GEMINI_OUTPUT} [prompt_len={len(prompt)}]"


def propose_live(prompt: str) -> dict[str, Any]:
    """
    Stub for a future live-call proposal path.

    Always returns a blocked status until human-root approval and secrets
    policy are in place (tracked in issue #22).
    """
    return {
        "status": "BLOCKED",
        "reason": (
            "Live Gemini invocation is not authorized in this adapter scaffold. "
            "Human-root approval and a secrets policy must be established first "
            "(issue #22)."
        ),
        "live_call_attempted": False,
        "adapter_mode": ADAPTER_MODE,
    }


def repo_trace_only(source_repo: str = "atlaslattice/tucker-gemini-GPT-") -> dict[str, Any]:
    """
    Return a repo-trace record documenting Tucker's provenance path.

    This does not invoke any runtime path.
    """
    return {
        "trace_type": "REPO_TRACE_ONLY",
        "source_repo": source_repo,
        "runtime_invoked": False,
        "provenance_backed": True,
        "boot_visible": True,
        "canon_ratified": False,
        "notes": (
            "Tucker is provenance-wired and boot-visible. "
            "No runtime path is invoked by this trace."
        ),
    }
