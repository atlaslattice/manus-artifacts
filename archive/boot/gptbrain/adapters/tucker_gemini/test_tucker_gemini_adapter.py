"""
Tests for Tucker / Gemini adapter scaffold.

STATUS: ADAPTER TESTS — NOT CANON
ISSUE: manus-artifacts#22
"""

from __future__ import annotations

import os

from tucker_gemini_adapter import TuckerGeminiAdapter


def test_describe_sources_is_provenance_visible_not_runtime_wired() -> None:
    adapter = TuckerGeminiAdapter()
    manifest = adapter.describe_sources()
    assert manifest.adapter == "tucker_gemini"
    assert manifest.source_refs
    assert "does not execute Tucker or call Gemini" in manifest.safe_claim


def test_validate_config_never_authorizes_live_calls_even_with_key(monkeypatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "fake-test-key")
    adapter = TuckerGeminiAdapter()
    status = adapter.validate_config()
    assert status.gemini_api_key_present is True
    assert status.live_gemini_allowed is False
    assert status.mode_default == "DRY_RUN_ONLY"
    assert any("does not authorize live calls" in note for note in status.notes)


def test_validate_config_without_key_is_still_safe(monkeypatch) -> None:
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    adapter = TuckerGeminiAdapter()
    status = adapter.validate_config()
    assert status.gemini_api_key_present is False
    assert status.live_gemini_allowed is False


def test_dry_run_receipt_attempts_no_live_call() -> None:
    adapter = TuckerGeminiAdapter()
    receipt = adapter.dry_run("hello Tucker")
    assert receipt.mode == "DRY_RUN_ONLY"
    assert receipt.live_call_attempted is False
    assert receipt.live_call_allowed is False
    assert receipt.human_root_required is True
    assert receipt.mock_output is None


def test_mock_gemini_is_deterministic_and_not_live() -> None:
    adapter = TuckerGeminiAdapter()
    first = adapter.mock_gemini("same prompt")
    second = adapter.mock_gemini("same prompt")
    assert first.mode == "MOCK_GEMINI"
    assert first.live_call_attempted is False
    assert first.live_call_allowed is False
    assert first.mock_output == second.mock_output
    assert "MOCK_GEMINI_RESPONSE" in (first.mock_output or "")


def test_propose_live_call_is_blocked_by_default() -> None:
    adapter = TuckerGeminiAdapter()
    request = adapter.propose_live_call("live please")
    assert request.requested_mode == "LIVE_GEMINI"
    assert request.blocked_by_default is True
    assert "human-root approval" in request.required_approvals
    assert "secrets policy approval" in request.required_approvals


def test_repo_trace_only_does_not_invoke_runtime() -> None:
    adapter = TuckerGeminiAdapter()
    receipt = adapter.repo_trace_only()
    assert receipt.mode == "REPO_TRACE_ONLY"
    assert receipt.live_call_attempted is False
    assert receipt.live_call_allowed is False
    assert receipt.source_refs
