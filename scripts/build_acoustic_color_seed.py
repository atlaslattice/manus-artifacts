from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "archive/knowledge_graph/ACOUSTIC_COLOR_SEED.json"


def build_seed_payload() -> dict:
    bands = [
        {"band": "infra", "hz_min": 0.1, "hz_max": 20.0, "color_hex": "#6a0dad"},
        {"band": "bass", "hz_min": 20.0, "hz_max": 60.0, "color_hex": "#4b0082"},
        {"band": "low_mid", "hz_min": 60.0, "hz_max": 250.0, "color_hex": "#0000ff"},
        {"band": "mid", "hz_min": 250.0, "hz_max": 2000.0, "color_hex": "#00ff00"},
        {"band": "upper_mid", "hz_min": 2000.0, "hz_max": 4000.0, "color_hex": "#ffff00"},
        {"band": "presence", "hz_min": 4000.0, "hz_max": 6000.0, "color_hex": "#ff7f00"},
        {"band": "brilliance", "hz_min": 6000.0, "hz_max": 20000.0, "color_hex": "#ff0000"},
    ]
    return {
        "status": "candidate",
        "canon": False,
        "mapping_model": "rainbow-yin-yang-v0.1",
        "bands": bands,
    }


def write_seed(path: Path = OUTPUT_PATH) -> dict:
    payload = build_seed_payload()
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return payload


def main() -> int:
    payload = write_seed(OUTPUT_PATH)
    print(f"acoustic-color-seed-written bands={len(payload['bands'])} path={OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
