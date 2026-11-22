#!/usr/bin/env python3
"""Static deployment-risk triage for historical Krakoa MCP source.

Reads bytes only. Never imports/runs the subject, touches secrets, connects a
provider or authorizes deployment. A clean scan means REVIEW, never GO.
"""
from __future__ import annotations

import argparse
import ast
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

MAX_BYTES = 1024 * 1024
SENSITIVE_TOOLS = {
    "krakoa_sphere_write": "UNAUTHENTICATED_WRITE_SURFACE",
    "krakoa_shadow_sweep": "LOCAL_HISTORY_COLLECTION_SURFACE",
    "krakoa_haptic_pulse": "PHYSICAL_DEVICE_EFFECT_SURFACE",
    "krakoa_gcp_status": "CLOUD_PROCESS_SURFACE",
}
SENSITIVE_PATH_MARKERS = (
    ".bash_history", ".zsh_history", ".claude", "google-cloud-setup",
    "/home/claude/", "master_token", "private_key",
)
WRITE_METHODS = {"write_text", "write_bytes", "mkdir", "rmdir", "unlink", "rename"}
SHELL_METHODS = {"run", "Popen", "call", "check_call", "check_output", "system", "execv", "execve"}


def _name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return _name(node.value) + "." + node.attr
    return ""


def inspect_bytes(raw: bytes) -> dict[str, Any]:
    digest = sha256(raw).hexdigest()
    results: list[dict[str, Any]] = []

    def record(code: str, line: int, category: str = "HOLD") -> None:
        row = {"code": code, "line": line, "classification": category}
        if row not in results:
            results.append(row)

    if not raw or len(raw) > MAX_BYTES:
        record("SOURCE_MISSING_OR_OVER_SIZE", 0)
    else:
        try:
            source = raw.decode("utf-8")
            tree = ast.parse(source)
        except (UnicodeDecodeError, SyntaxError, ValueError, MemoryError):
            record("UNPARSEABLE_OR_INVALID_SOURCE", 0)
        else:
            for node in ast.walk(tree):
                line = getattr(node, "lineno", 0)
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name == "subprocess":
                            record("PROCESS_EXECUTION_IMPORT", line)
                elif isinstance(node, ast.ImportFrom):
                    if node.module and node.module.startswith("subprocess"):
                        record("PROCESS_EXECUTION_IMPORT", line)
                    if node.module and node.module.startswith("mcp.server"):
                        record("REAL_MCP_SERVER_IMPORT_UNREVIEWED", line)

                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if node.name in SENSITIVE_TOOLS:
                        record(SENSITIVE_TOOLS[node.name], line)

                if isinstance(node, ast.Call):
                    target = _name(node.func)
                    if target in {"mcp.run", "server.run", "app.run"}:
                        record("ACTIVE_SERVER_ENTRYPOINT_UNREVIEWED", line)
                    if target.startswith("subprocess.") or target in {"os.system", "os.popen"}:
                        record("PROCESS_EXECUTION_CALL", line)
                    if target.rsplit(".", 1)[-1] in WRITE_METHODS:
                        record("FILESYSTEM_MUTATION_CALL", line)
                    if target == "open":
                        # Missing mode is a read. Unknown/computed mode must HOLD.
                        mode = node.args[1] if len(node.args) >= 2 else None
                        for keyword in node.keywords:
                            if keyword.arg == "mode":
                                mode = keyword.value
                        if mode is not None:
                            if not isinstance(mode, ast.Constant) or not isinstance(mode.value, str):
                                record("DYNAMIC_FILE_OPEN_MODE", line)
                            elif any(flag in mode.value for flag in ("w", "a", "x", "+")):
                                record("FILESYSTEM_WRITE_OPEN", line)
                if isinstance(node, ast.Constant) and isinstance(node.value, str):
                    low = node.value.lower()
                    if any(marker in low for marker in SENSITIVE_PATH_MARKERS):
                        record("SENSITIVE_LOCAL_SOURCE_REFERENCE", line)

    results.sort(key=lambda x: (x["line"], x["code"]))
    return {
        "source_sha256": digest,
        "source_bytes": len(raw),
        "status": "HOLD" if results else "STATIC_REVIEW_ONLY",
        "findings": results,
        "deployment_authorized": False,
        "source_rights_verified": False,
        "principal_authenticated": False,
        "provider_calls_performed": 0,
        "source_executed": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Explicit local public-source Python path")
    args = parser.parse_args(argv)
    try:
        raw = args.source.read_bytes()
        result = inspect_bytes(raw)
    except OSError:
        result = {
            "status": "HOLD",
            "findings": [{"code": "SOURCE_UNAVAILABLE", "line": 0}],
            "deployment_authorized": False, "source_executed": False
        }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 2 if result["status"] == "HOLD" else 0


if __name__ == "__main__":
    raise SystemExit(main())
