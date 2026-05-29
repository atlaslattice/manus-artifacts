from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def _schema_files() -> list[Path]:
    files = list((REPO_ROOT / "schemas").rglob("*.yaml"))
    files.extend((REPO_ROOT / "archive/product/receipt_habitat_v0_1/schemas").rglob("*.yaml"))
    return sorted(files)


def test_all_schema_yaml_files_parse():
    schema_files = _schema_files()
    assert schema_files, "expected at least one schema yaml file"
    for schema_file in schema_files:
        with schema_file.open("r", encoding="utf-8") as fh:
            assert yaml.safe_load(fh) is not None, f"failed to parse {schema_file}"
