#!/usr/bin/env python3
"""Sheldonbrain parser adapter v0.1. Normalize user-supplied JSON/JSONL exports
into local source-linked packets without uploading, executing or canonizing them.
The original source file is never modified. Hidden thinking traces are excluded.
"""
import argparse,hashlib,json
from pathlib import Path
from atlas_fabric import ReceiptGraph

def normalize(data,source_id):
    """Supports the observed Grok nested conversation schema and role-based chat logs."""
    records=[]
    if isinstance(data,dict) and isinstance(data.get("conversations"),list):
        for ci,conversation in enumerate(data["conversations"]):
            key=conversation.get("conversation",{}).get("id",f"conversation_{ci}")
            for mi,w in enumerate(conversation.get("responses",[])):
                msg=w.get("response",{})
                role={"human":"user","assistant":"assistant"}.get(msg.get("sender"),"unknown")
                text=msg.get("message")
                if isinstance(text,str) and text:
                    records.append({"source_id":source_id,"thread":str(key),"message_index":mi,
                                    "role":role,"text":text,"status":"PARSED_NOT_CANON",
                                    "source_schema":"grok_export_nested"})
    elif isinstance(data,dict) and isinstance(data.get("messages"),list):
        for mi,msg in enumerate(data["messages"]):
            text=msg.get("content") or msg.get("text")
            if isinstance(text,str) and text:
                records.append({"source_id":source_id,"thread":str(data.get("id","imported_chat")),
                                "message_index":mi,"role":str(msg.get("role","unknown")),
                                "text":text,"status":"PARSED_NOT_CANON",
                                "source_schema":"generic_role_messages"})
    else:
        raise ValueError("Unsupported export: expected conversations/responses or messages")
    return records

def parse_local(path,*,max_bytes=5_000_000):
    p=Path(path)
    if not p.is_file() or p.stat().st_size>max_bytes:raise ValueError("Missing/oversized source")
    raw=p.read_bytes()
    source_hash=hashlib.sha256(raw).hexdigest()
    data=json.loads(raw.decode("utf-8-sig"))
    records=normalize(data,"sha256:"+source_hash)
    return {"source_sha256":source_hash,"records":records,
            "count":len(records),"status":"LOCAL_PARSED_NON_CANON",
            "privacy":"Local only; do not commit the source or derived text to public repositories"}

def add_to_graph(graph,packet):
    source="local-import:"+packet["source_sha256"]
    graph.add_node(node_id=source,kind="SourceArtifact",title="Private chat export",
                   source=source,receipt="sha256:"+packet["source_sha256"])
    for item in packet["records"]:
        safe={k:v for k,v in item.items() if k!="text"}
        ident=hashlib.sha256(json.dumps(safe,sort_keys=True).encode()).hexdigest()[:24]
        node="parsed:"+ident
        graph.add_node(node_id=node,kind="ParsedPacket",title="Parsed message (content stays local)",
                       source=source,receipt=item["source_id"],status="parsed")
        graph.add_edge(node,source,"DERIVED_FROM",item["source_id"])
    return len(packet["records"])

def main():
    a=argparse.ArgumentParser()
    a.add_argument("source_json",help="Local chat JSON file, never uploaded")
    a.add_argument("--graph-db",help="Optional local receipt graph path")
    a.add_argument("--out",help="Optional new local parsed JSON file; never overwrites")
    x=a.parse_args()
    packet=parse_local(x.source_json)
    if x.graph_db:
        graph=ReceiptGraph(x.graph_db)
        add_to_graph(graph,packet)
    if x.out:
        with open(x.out,"x",encoding="utf-8") as f:
            json.dump(packet,f,ensure_ascii=False,indent=2)
    print(json.dumps({"state":packet["status"],"count":packet["count"],
                      "sha256":packet["source_sha256"],
                      "written_to":x.out or None,"graph":x.graph_db or None}))
if __name__=="__main__":main()
