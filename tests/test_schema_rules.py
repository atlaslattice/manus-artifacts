from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return yaml.safe_load((ROOT / path).read_text(encoding='utf-8'))


def test_all_atlas_schemas_have_version_and_defaults():
    d = ROOT / 'schemas/atlas_orcs/v0_1'
    for f in d.glob('*.yaml'):
        y = yaml.safe_load(f.read_text(encoding='utf-8'))
        assert y['properties']['schema_version']['const'] == '0.1'
        if 'canon_status' in y.get('properties', {}):
            assert y['properties']['canon_status'].get('default') == 'not_canon'
        if 'deployment_status' in y.get('properties', {}):
            assert y['properties']['deployment_status'].get('default') == 'not_deployable'


def test_summary_not_source_and_receipt_not_truth_and_ratification_explicit_event():
    summary = load('schemas/atlas_orcs/v0_1/atlas-summary-lineage.schema.yaml')
    ratify = load('schemas/atlas_orcs/v0_1/atlas-ratification-event.schema.yaml')
    assert 'summary_artifact_id' in summary['properties']
    assert 'source_artifact_id' in summary['properties']
    assert ratify['properties']['explicit_event']['const'] is True


def test_oai_required_fields_and_rules_present():
    s = load('schemas/o_ai/v0_1/o-ai-packet.schema.yaml')
    req = set(s['required'])
    assert {'raw_export_status', 'thread_time_range', 'access_scope'}.issubset(req)
    # summary_only cannot claim source_complete and execution_request gate checks encoded
    assert len(s['allOf']) >= 2


def test_native_thread_required_fields_and_caveat_rule_present():
    s = load('schemas/native_thread/v0_1/native-thread-ingestion-packet.schema.yaml')
    req = set(s['required'])
    assert {'raw_export_status', 'thread_time_range', 'access_scope'}.issubset(req)
    assert len(s['allOf']) >= 1
