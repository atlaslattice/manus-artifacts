from pathlib import Path

import pytest
import yaml
from jsonschema import ValidationError, validate


REPO_ROOT = Path(__file__).resolve().parents[1]
OAI_DIR = REPO_ROOT / "schemas/o_ai/v0_1"


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_oai_valid_examples_pass_schema():
    schema = _load_yaml(OAI_DIR / "o-ai-packet.schema.yaml")
    for example_name in ["valid_full_raw_packet.yaml", "valid_summary_only_packet.yaml"]:
        example = _load_yaml(OAI_DIR / "o-ai-packet-examples" / example_name)
        validate(example, schema)


@pytest.mark.parametrize("example_name", ["invalid_missing_access_scope.yaml", "invalid_execution_without_gates.yaml"])
def test_oai_invalid_examples_fail_schema(example_name: str):
    schema = _load_yaml(OAI_DIR / "o-ai-packet.schema.yaml")
    example = _load_yaml(OAI_DIR / "o-ai-packet-examples" / example_name)
    with pytest.raises(ValidationError):
        validate(example, schema)
