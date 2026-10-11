#!/usr/bin/env python3
"""Constitution -> receipt-indexed local knowledge graph, and optional SHUGS
experimental packet ingestion. Never converts model claims to verified truth.
"""
import argparse,json,hashlib
from pathlib import Path
from atlas_fabric import ReceiptGraph
from dragonseek_os import load

def seed_constitution(graph):
    corpus=load()
    if not corpus["complete"]:
        raise ValueError("Constitution incomplete, refusing to seed graph")
    for item in corpus["entries"]:
        node_id="dragonseek:"+item["kind"]+":"+item["id"]
        label=item["id"]+" — "+item["name"]
        location=item["source_file"]
        graph.add_node(node_id=node_id,kind="Claim",title=label,
                       source=location,receipt="git-versioned:"+location,
                       status="canonical_candidate")
    for v in corpus["historical_variants"]:
        node="dragonseek:history:"+v["id"]+":"+v["name"].replace(" ","_")
        graph.add_node(node_id=node,kind="SourceArtifact",title=v["name"],
                       source=v["source_file"],receipt="git-versioned:"+v["source_file"],
                       status="contradicted")
        graph.add_edge(node,"dragonseek:invariants:INV-0","CONTRADICTS",
                       "dragonseek:constitutional_authority.json")
    return corpus["counts"]

def add_shugs_packet(graph,packet,source_path,receipt):
    """A locally supplied simulation packet can be indexed, NOT canonized."""
    if not isinstance(packet,dict) or not source_path or not receipt:
        raise ValueError("SHUGS packet source/receipt required")
    if not any(k in packet for k in ("N","n","results","lattice","metrics","parameters","lattice_optimum","n_scaling")):
        raise ValueError("SHUGS data schema unrecognized")
    raw=json.dumps(packet,sort_keys=True,ensure_ascii=False)
    if len(raw)>200000:raise ValueError("Oversized research packet")
    sha=hashlib.sha256(raw.encode()).hexdigest()
    node_id="shugs:proposed:"+sha[:24]
    graph.add_node(node_id=node_id,kind="ParsedPacket",
                   title="SHUGS fixed-lattice research packet — simulation only",
                   source=source_path,receipt=receipt+"; sha256:"+sha,
                   status="review_pending")
    return {"node_id":node_id,"sha256":sha,
            "classification":"THEORETICAL_OR_SIMULATED_NOT_PHYSICALLY_VALIDATED",
            "authority":"none","no_automatic_routing_effect":True}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--db",default=":memory:",help="local sqlite path")
    p.add_argument("--search",default="INV-0")
    p.add_argument("--shugs-json",help="Optional local simulation JSON")
    p.add_argument("--shugs-receipt",help="Source ref/commit for experimental packet")
    a=p.parse_args()
    graph=ReceiptGraph(a.db)
    counts=seed_constitution(graph)
    extra=None
    if a.shugs_json:
        if not a.shugs_receipt:p.error("--shugs-receipt required")
        f=Path(a.shugs_json)
        if f.stat().st_size>200000:p.error("Research JSON too large")
        extra=add_shugs_packet(graph,json.loads(f.read_text(encoding="utf-8")),
                               str(f),a.shugs_receipt)
    print(json.dumps({"state":"LOCAL_KG_SEEDED","counts":counts,
        "records":graph.search(a.search),"shugs_import":extra,
        "governance":"graph != memory != permission; no canon promotions"},
        ensure_ascii=False,indent=2))
if __name__=="__main__":main()
