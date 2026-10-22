"""Offline packet export contract; no provider, model, OS or control-plane calls."""
import hashlib
import json
import re
from pathlib import Path
from resource_gap.simulate import validate
from .current_state import run

ROOT=Path(__file__).resolve().parents[1]/'integration'


def packet(revision=None):
    if revision is not None and not re.fullmatch('[0-9a-f]{40}',revision):
        raise ValueError('Revision must be a full commit SHA or omitted for unverified worktree')
    payload=run()
    encoded=json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
    result=dict(schema_version='0.1',packet_type='LOCALITY_REVIEW_SNAPSHOT',
        node_id='DONGJIAKOU-NODE-001',evidence_class='SIMULATED',
        publication_status='PUBLIC_REVIEW_CANDIDATE',authority='NONE',
        source_revision=revision,source_revision_verified=False,
        payload_sha256=hashlib.sha256(encoded).hexdigest(),
        capabilities=['READ_PUBLIC_EVIDENCE','RUN_OFFLINE_SCENARIOS','EXPORT_REVIEW_PACKET'],
        actuator_authority=False,provider_calls=0,model_calls=0,
        invariant_namespace='djk-locality-001',payload=payload)
    validate(result,json.loads((ROOT/'packet.schema.json').read_text()))
    return result
