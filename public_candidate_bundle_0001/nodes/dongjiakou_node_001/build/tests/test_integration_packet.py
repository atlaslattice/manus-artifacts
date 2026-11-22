import hashlib
import json
from pathlib import Path
import pytest
from jsonschema import Draft202012Validator, ValidationError
from models.integration import packet

def test_offline_packet_preserves_qol_unknowns_and_ecological_vetoes():
    x=packet()
    assert x['source_revision'] is None
    assert not x['source_revision_verified']
    assert not x['actuator_authority']
    assert x['provider_calls']==x['model_calls']==0
    assert x['evidence_class']=='SIMULATED'
    assert x['payload']['qol']['composite_score'] is None
    assert len(x['payload']['vetoes'])==6
    assert x['payload']['realized_credit']==0

def test_content_digest_identifies_snapshot_bytes():
    x=packet();raw=json.dumps(x['payload'],sort_keys=True,separators=(',',':'),allow_nan=False).encode()
    assert x['payload_sha256']==hashlib.sha256(raw).hexdigest()
    assert packet()['payload_sha256']==x['payload_sha256']

def test_schema_independently_validates_and_rejects_actuation():
    s=json.loads((Path(__file__).resolve().parents[1]/'integration/packet.schema.json').read_text())
    x=packet();Draft202012Validator(s).validate(x)
    x['actuator_authority']=True
    with pytest.raises(ValidationError):Draft202012Validator(s).validate(x)

def test_revision_assertion_cannot_authenticate_a_commit():
    x=packet('a'*40)
    assert x['source_revision']=='a'*40
    assert not x['source_revision_verified']
    with pytest.raises(ValueError):packet('latest')
