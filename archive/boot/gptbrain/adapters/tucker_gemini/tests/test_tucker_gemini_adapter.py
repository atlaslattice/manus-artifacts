"""
Tucker / Gemini adapter safety tests.

STATUS: IMPLEMENTATION TESTS — NOT CANON
ISSUE: manus-artifacts#22

These tests verify the adapter's safety boundaries:
1. provenance-visible / not runtime-wired source description
2. config never authorizes live calls even if GEMINI_API_KEY exists
3. config without key remains safe
4. dry-run receipt attempts no live call
5. mock Gemini returns deterministic fake output
6. propose-live is blocked by default
7. repo-trace-only does not invoke runtime
"""

from __future__ import annotations

import os

import pytest

from archive.boot.gptbrain.adapters.tucker_gemini.adapter import (
    ADAPTER_MODE,
    LIVE_GEMINI_AUTHORIZED,
    DRY_RUN_ONLY,
    DryRunReceipt,
    TuckerGeminiConfig,
    dry_run,
    load_config,
    mock_gemini,
    propose_live,
    repo_trace_only,
)


# ---------------------------------------------------------------------------
# 1. Provenance description — not runtime-wired
# ---------------------------------------------------------------------------

def test_adapter_mode_is_repo_trace_only() -> None:
    assert ADAPTER_MODE == "REPO_TRACE_ONLY"
    assert LIVE_GEMINI_AUTHORIZED is False
    assert DRY_RUN_ONLY is True


# ---------------------------------------------------------------------------
# 2. Config never authorizes live calls even if GEMINI_API_KEY is present
# ---------------------------------------------------------------------------

def test_config_does_not_authorize_live_even_with_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "fake-key-should-not-matter")
    config = load_config()
    assert config.live_authorized is False
    assert config.dry_run is True
    assert config.use_mock is True


def test_config_live_authorized_true_raises() -> None:
    with pytest.raises(ValueError, match="live_authorized=True is blocked"):
        TuckerGeminiConfig(live_authorized=True)


# ---------------------------------------------------------------------------
# 3. Config without key remains safe
# ---------------------------------------------------------------------------

def test_config_without_api_key_is_safe(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    config = load_config()
    assert config.live_authorized is False
    assert config.dry_run is True


# ---------------------------------------------------------------------------
# 4. Dry-run receipt attempts no live call
# ---------------------------------------------------------------------------

def test_dry_run_receipt_no_live_call() -> None:
    receipt = dry_run("test prompt")
    assert isinstance(receipt, DryRunReceipt)
    assert receipt.live_call_attempted is False
    assert receipt.mock_used is True
    assert receipt.adapter == "tucker_gemini"
    assert receipt.mode == "REPO_TRACE_ONLY"


def test_dry_run_accepts_any_prompt_without_network() -> None:
    # Should complete instantly with no external I/O.
    receipt = dry_run("a" * 1000)
    assert receipt.live_call_attempted is False


# ---------------------------------------------------------------------------
# 5. Mock Gemini returns deterministic fake output
# ---------------------------------------------------------------------------

def test_mock_gemini_returns_deterministic_output() -> None:
    result = mock_gemini("hello")
    assert "[MOCK]" in result
    assert "no live API call" in result


def test_mock_gemini_encodes_prompt_length() -> None:
    result = mock_gemini("abc")
    assert "prompt_len=3" in result


def test_mock_gemini_same_prompt_same_output() -> None:
    assert mock_gemini("x") == mock_gemini("x")


# ---------------------------------------------------------------------------
# 6. Propose-live is blocked by default
# ---------------------------------------------------------------------------

def test_propose_live_is_blocked() -> None:
    result = propose_live("any prompt")
    assert result["status"] == "BLOCKED"
    assert result["live_call_attempted"] is False
    assert "human-root approval" in result["reason"].lower()
    assert result["adapter_mode"] == "REPO_TRACE_ONLY"


# ---------------------------------------------------------------------------
# 7. Repo-trace-only does not invoke runtime
# ---------------------------------------------------------------------------

def test_repo_trace_only_does_not_invoke_runtime() -> None:
    trace = repo_trace_only()
    assert trace["runtime_invoked"] is False
    assert trace["trace_type"] == "REPO_TRACE_ONLY"
    assert trace["provenance_backed"] is True
    assert trace["boot_visible"] is True
    assert trace["canon_ratified"] is False


def test_repo_trace_only_uses_tucker_repo() -> None:
    trace = repo_trace_only()
    assert "tucker-gemini-GPT-" in trace["source_repo"]
