from pathlib import Path

import pytest
import yaml
from jsonschema import ValidationError, validate


REPO_ROOT = Path(__file__).resolve().parents[1]
NATIVE_DIR = REPO_ROOT / "schemas/native_thread/v0_1"


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_native_thread_valid_example_passes_schema():
    schema = _load_yaml(NATIVE_DIR / "native-thread-ingestion-packet.schema.yaml")
    example = _load_yaml(NATIVE_DIR / "examples/valid_summary_only_packet.yaml")
    validate(example, schema)


def test_native_thread_invalid_example_fails_schema():
    schema = _load_yaml(NATIVE_DIR / "native-thread-ingestion-packet.schema.yaml")
    example = _load_yaml(NATIVE_DIR / "examples/invalid_summary_only_full_ingestion.yaml")
    with pytest.raises(ValidationError):
        validate(example, schema)
