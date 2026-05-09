#!/usr/bin/env python3
"""
Tucker / Gemini adapter scaffold.

STATUS: ADAPTER SCAFFOLD — NOT CANON
ISSUE: manus-artifacts#22

Default behavior is dry-run only. This module performs no live Gemini calls,
no Tucker code invocation, and requires no secrets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from dataclasses import dataclass, asdict
from typing import Literal


Mode = Literal["REPO_TRACE_ONLY", "DRY_RUN_ONLY", "MOCK_GEMINI", "LIVE_GEMINI"]

SOURCE_REFS = [
    "archive/provenance/TUCKER_PUBLIC_BUILD_PROVENANCE_NOTE_2026-05-08.md",
    "archive/provenance/TUCKER_BUILD_CULTURE_AND_GPT_ASSISTANCE_NOTE_2026-05-08.md",
    "archive/boot/gptbrain/TUCKER_BOOT_INTEGRATION_NOTE_2026-05-09.md",
    "https://github.com/atlaslattice/tucker-gemini-GPT-/blob/main/ARTIFACT_PROVENANCE.md",
]

FORBIDDEN_CLAIMS = [
    "Tucker is ratified GPTBrain canon.",
    "GPT is sole author or owner of Tucker.",
    "Tucker is fully audited.",
    "Tucker is production-authorized by GPTBrain.",
    "Tucker proves autonomous model agency.",
    "Gemini is authorized because it is configured.",
]


@dataclass(frozen=True)
class SourceManifest:
    adapter: str
    status: str
    source_refs: list[str]
    safe_claim: str


@dataclass(frozen=True)
class ConfigStatus:
    gemini_api_key_present: bool
    live_gemini_allowed: bool
    mode_default: str
    notes: list[str]


@dataclass(frozen=True)
class AdapterReceipt:
    mode: str
    prompt_hash: str
    source_refs: list[str]
    live_call_attempted: bool
    live_call_allowed: bool
    human_root_required: bool
    human_root_status: str
    safe_claim: str
    forbidden_claims: list[str]
    next_review: str
    mock_output: str | None = None


@dataclass(frozen=True)
class HumanApprovalRequest:
    requested_mode: str
    blocked_by_default: bool
    required_approvals: list[str]
    reason: str


class TuckerGeminiAdapter:
    """Dry-run-first adapter boundary for Tucker/Gemini work."""

    def describe_sources(self) -> SourceManifest:
        return SourceManifest(
            adapter="tucker_gemini",
            status="ADAPTER SCAFFOLD — NOT CANON",
            source_refs=SOURCE_REFS,
            safe_claim=(
                "Tucker/Gemini are provenance-visible to GPTBrain; "
                "this adapter scaffold does not execute Tucker or call Gemini."
            ),
        )

    def validate_config(self) -> ConfigStatus:
        key_present = bool(os.getenv("GEMINI_API_KEY"))
        return ConfigStatus(
            gemini_api_key_present=key_present,
            live_gemini_allowed=False,
            mode_default="DRY_RUN_ONLY",
            notes=[
                "Presence of GEMINI_API_KEY does not authorize live calls.",
                "Live Gemini mode requires human-root approval and secrets policy.",
                "Default mode performs no network calls.",
            ],
        )

    def dry_run(self, prompt: str) -> AdapterReceipt:
        return self._receipt(
            prompt=prompt,
            mode="DRY_RUN_ONLY",
            live_call_attempted=False,
            live_call_allowed=False,
            mock_output=None,
        )

    def repo_trace_only(self, prompt: str = "") -> AdapterReceipt:
        return self._receipt(
            prompt=prompt,
            mode="REPO_TRACE_ONLY",
            live_call_attempted=False,
            live_call_allowed=False,
            mock_output="Source refs traced only; no runtime invocation.",
        )

    def mock_gemini(self, prompt: str) -> AdapterReceipt:
        digest = _hash_prompt(prompt)[:12]
        return self._receipt(
            prompt=prompt,
            mode="MOCK_GEMINI",
            live_call_attempted=False,
            live_call_allowed=False,
            mock_output=f"MOCK_GEMINI_RESPONSE[{digest}]: deterministic test receipt only.",
        )

    def propose_live_call(self, prompt: str) -> HumanApprovalRequest:
        _ = prompt
        return HumanApprovalRequest(
            requested_mode="LIVE_GEMINI",
            blocked_by_default=True,
            required_approvals=[
                "human-root approval",
                "secrets policy approval",
                "audit event plan",
                "live-call scope statement",
            ],
            reason="Live Gemini calls are disabled by default in the scaffold.",
        )

    def _receipt(
        self,
        prompt: str,
        mode: Mode,
        live_call_attempted: bool,
        live_call_allowed: bool,
        mock_output: str | None,
    ) -> AdapterReceipt:
        return AdapterReceipt(
            mode=mode,
            prompt_hash=_hash_prompt(prompt),
            source_refs=SOURCE_REFS,
            live_call_attempted=live_call_attempted,
            live_call_allowed=live_call_allowed,
            human_root_required=True,
            human_root_status="required_pending_for_live_execution",
            safe_claim=(
                "Adapter scaffold produced a receipt. No live Tucker or Gemini execution occurred."
            ),
            forbidden_claims=FORBIDDEN_CLAIMS,
            next_review="Route any live-call proposal through human-root approval and secrets policy.",
            mock_output=mock_output,
        )


def _hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def _dump(obj: object) -> None:
    print(json.dumps(asdict(obj), indent=2, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser(description="Tucker/Gemini adapter scaffold")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("sources")
    sub.add_parser("config")

    dry = sub.add_parser("dry-run")
    dry.add_argument("prompt")

    mock = sub.add_parser("mock-gemini")
    mock.add_argument("prompt")

    live = sub.add_parser("propose-live")
    live.add_argument("prompt")

    args = parser.parse_args()
    adapter = TuckerGeminiAdapter()

    if args.command == "sources":
        _dump(adapter.describe_sources())
    elif args.command == "config":
        _dump(adapter.validate_config())
    elif args.command == "dry-run":
        _dump(adapter.dry_run(args.prompt))
    elif args.command == "mock-gemini":
        _dump(adapter.mock_gemini(args.prompt))
    elif args.command == "propose-live":
        _dump(adapter.propose_live_call(args.prompt))
    else:
        parser.error(f"Unsupported command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
