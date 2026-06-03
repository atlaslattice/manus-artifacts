"""
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
"""
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_each_atlas_orcs_schema_has_a_valid_fixture() -> None:
    schema_dir = ROOT / 'schemas/atlas_orcs/v0_1'
    fixture_dir = ROOT / 'fixtures/atlas_orcs/v0_1'
    for schema_path in sorted(schema_dir.glob('*.schema.yaml')):
        fixture_path = fixture_dir / f'{schema_path.stem}.example.yaml'
        assert fixture_path.exists(), schema_path.name
        schema = yaml.safe_load(schema_path.read_text(encoding='utf-8'))
        fixture = yaml.safe_load(fixture_path.read_text(encoding='utf-8'))
        jsonschema.validate(fixture, schema)
