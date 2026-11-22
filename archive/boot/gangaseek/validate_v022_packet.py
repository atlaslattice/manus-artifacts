"""GANGASEEK v0.2.2 *synthetic-only* envelope shape checker.

No cryptographic verification, decryption, host identity, source-rights check,
network, disk write, CANON/DEPLOYED authority, or live packet execution.
"""
from __future__ import annotations

import base64
import binascii
import json
import re
import sys
from pathlib import Path
from typing import Any

ALLOWED_STATUS = {"raw_missing", "raw_partial", "raw_complete_unhashed",
                  "raw_complete_hashed", "raw_source_unavailable"}
OPERATORS = {"O_AI", "O_MS", "O_GOOGLE", "O_STARLINK", "O_ALPHA", "O_X"}
TENANCY = {"SOVEREIGN", "ENTERPRISE", "PUBLIC", "PRIVATE", "RESEARCH"}
EPISTEMIC = {"synthetic", "unverified", "derived", "reviewed_candidate"}
HEADER_FIELDS = {"provenance_receipt", "epistemic_label", "authority_scope",
                 "tenancy_context", "source_operator", "target_operator", "swa_mask",
                 "timestamp", "coordinate", "tag_class", "state_plane"}
ENVELOPE_FIELDS = {"aead_algorithm", "nonce_base64", "aad_base64",
                   "ciphertext_base64", "tag_base64",
                   "padded_plaintext_bytes", "encoded_ciphertext_base64_chars",
                   "synthetic_fixture"}
TOP_FIELDS = {"schema_version", "status", "canon", "deployed", "source_ref",
              "raw_export_status", "header", "aead_envelope"}
COORD_FIELDS = {"notation", "house", "sphere", "node"}


def load_json(data: bytes) -> Any:
    """Reject duplicate JSON keys instead of silently overriding a grant."""
    def check(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        obj: dict[str, Any] = {}
        for key, val in pairs:
            if key in obj:
                raise ValueError(f"duplicate key: {key}")
            obj[key] = val
        return obj
    return json.loads(data.decode("utf-8"), object_pairs_hook=check)


def check_packet(packet: Any) -> dict[str, Any]:
    problems: list[str] = []

    def complain(label: str) -> None:
        problems.append(label)

    def fields(obj: Any, required: set[str], location: str) -> bool:
        if not isinstance(obj, dict):
            complain(location + "_not_object")
            return False
        if set(obj) != required:
            complain(location + "_missing_or_extra_fields")
        return True

    if not fields(packet, TOP_FIELDS, "packet"):
        return {"disposition": "HOLD", "errors": problems, "cryptographic_authenticity_verified": False,
                "authority_verified": False, "host_executed": False}

    if packet.get("schema_version") != "0.2.2-candidate":
        complain("version_mismatch")
    if packet.get("status") != "CANDIDATE_ONLY" or packet.get("canon") is not False or packet.get("deployed") is not False:
        complain("authority_or_deployment_inflation")
    if not isinstance(packet.get("source_ref"), str) or not packet["source_ref"].strip():
        complain("source_ref_required")
    if not isinstance(packet.get("raw_export_status"), str) or packet.get("raw_export_status") not in ALLOWED_STATUS:
        complain("invalid_raw_export_status")
    if packet.get("raw_export_status") in {"raw_complete_hashed", "raw_complete_unhashed"}:
        complain("source_completeness_not_verified_by_synthetic_packet")

    h = packet.get("header")
    if fields(h, HEADER_FIELDS, "header"):
        if not isinstance(h.get("provenance_receipt"), str) or not h["provenance_receipt"].strip():
            complain("missing_provenance_receipt")
        if not isinstance(h.get("epistemic_label"), str) or h.get("epistemic_label") not in EPISTEMIC:
            complain("invalid_epistemic_label")
        if not isinstance(h.get("authority_scope"), str) or h.get("authority_scope") not in {"NONE", "ADVISORY"}:
            complain("inferred_authority_forbidden")
        if not isinstance(h.get("tenancy_context"), str) or h.get("tenancy_context") not in TENANCY:
            complain("unknown_tenancy")
        if not all(isinstance(h.get(k), str) and h.get(k) in OPERATORS for k in ("source_operator", "target_operator")):
            complain("unknown_operator")
        mask = h.get("swa_mask")
        if not isinstance(mask, str) or re.fullmatch(r"0x[0-9A-Fa-f]{4}", mask) is None:
            complain("invalid_16_bit_swa_mask")
        elif int(mask, 16) & 0xC000:
            complain("reserved_swa_bits_unapproved")
        if not isinstance(h.get("timestamp"), str) or not h["timestamp"].strip():
            complain("timestamp_required")
        for k, maximum in (("tag_class", 3), ("state_plane", 15)):
            value = h.get(k)
            if type(value) is not int or not 0 <= value <= maximum:
                complain("invalid_" + k)
        c = h.get("coordinate")
        if fields(c, COORD_FIELDS, "coordinate"):
            if c.get("notation") != "HSN":
                complain("unsupported_coordinate_notation")
            for axis in ("house", "sphere", "node"):
                v = c.get(axis)
                if type(v) is not int or not 1 <= v <= 12:
                    complain("coordinate_" + axis + "_out_of_range")

    env = packet.get("aead_envelope")
    if fields(env, ENVELOPE_FIELDS, "aead_envelope"):
        if env.get("aead_algorithm") != "CHACHA20_POLY1305":
            complain("unknown_aead_algorithm")
        if env.get("synthetic_fixture") is not True:
            complain("only_synthetic_fixtures_allowed")
        if env.get("padded_plaintext_bytes") != 4096 or env.get("encoded_ciphertext_base64_chars") != 5464:
            complain("incorrect_byte_vs_encoding_lengths")
        encoded = env.get("ciphertext_base64")
        if not isinstance(encoded, str) or len(encoded) != 5464:
            complain("ciphertext_encoded_length_not_5464")
        for key, length in (("nonce_base64", 12), ("aad_base64", None),
                            ("ciphertext_base64", 4096), ("tag_base64", 16)):
            value = env.get(key)
            if not isinstance(value, str):
                complain(key + "_not_string")
                continue
            try:
                raw = base64.b64decode(value, validate=True)
                if base64.b64encode(raw).decode("ascii") != value:
                    complain(key + "_not_canonical_base64")
                if length is not None and len(raw) != length:
                    complain(key + "_decoded_length_wrong")
            except (ValueError, binascii.Error):
                complain(key + "_invalid_base64")

    return {"disposition": "HOLD" if problems else "CANDIDATE_STRUCTURE_ONLY",
            "errors": sorted(set(problems)), "cryptographic_authenticity_verified": False,
            "source_rights_verified": False, "authority_verified": False,
            "host_executed": False, "canon": False, "deployed": False}


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: python validate_v022_packet.py <synthetic-json-packet>", file=sys.stderr)
        return 64
    try:
        packet = load_json(Path(args[0]).read_bytes())
        result = check_packet(packet)
    except (OSError, UnicodeError, ValueError) as exc:
        result = {"disposition": "HOLD", "errors": [str(exc)],
                  "cryptographic_authenticity_verified": False}
    print(json.dumps(result, indent=2))
    return 0 if result["disposition"] == "CANDIDATE_STRUCTURE_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
