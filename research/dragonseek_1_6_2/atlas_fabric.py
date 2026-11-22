#!/usr/bin/env python3
"""ATLAS Fabric v0.2: full opt-in UWS operations, Sheldonbrain retrieval,
receipt-linked local KG, experimental 8/8/8 scheduling, and two-brain review.
Stdlib-only. No provider connections, commands, or scheduling start on import.
"""
from __future__ import annotations
import hashlib, json, os, shutil, sqlite3, subprocess, urllib.request
from pathlib import Path
from urllib.parse import urlsplit
from uws_gateway import run_uws, proposal as uws_proposal

GRAPH_STATES = {"raw", "parsed", "claim_candidate", "review_pending",
                "contradicted", "deferred", "rejected", "ratified",
                "canonical_candidate", "canon"}
GRAPH_EDGES = {"DERIVED_FROM", "SUPPORTS", "CONTRADICTS",
               "RELATED_TO", "REVIEWED_BY", "SUPERSEDES"}

def endpoint_allowed(url: str, allow_remote: bool=False) -> bool:
    u = urlsplit(url)
    if u.username or u.password or u.fragment or u.query: return False
    local = u.hostname in ("127.0.0.1", "localhost", "::1")
    if local: return u.scheme in ("http", "https")
    return allow_remote and u.scheme == "https" and bool(u.hostname)

def run_uws_readonly(command: list[str], params: dict | None=None, *,
                     execute: bool=False, timeout: int=15) -> dict:
    """Legacy compatibility wrapper. Use run_uws for the full read/write bridge."""
    plan=uws_proposal(command,params=params)
    if plan.get("operation")!="READ":
        return {"state":"DENIED","reason":"Legacy read-only wrapper; use run_uws with a trusted human approval callback for writes"}
    return run_uws(command,params=params,execute=execute,timeout=timeout)

def query_sheldonbrain(query: str, *, base_url="http://127.0.0.1:8080",
                       allow_remote=False, execute=False, top_k=5) -> dict:
    """POST /query only. No /store, /lifecycle, /delete or authorization escalation."""
    endpoint=base_url.rstrip("/")+"/query"
    if not endpoint_allowed(endpoint,allow_remote):
        return {"state":"DENIED","reason":"Remote retrieval requires HTTPS opt-in"}
    if not isinstance(query,str) or not query.strip() or len(query)>10000 or not 1<=top_k<=100:
        return {"state":"DENIED","reason":"Invalid query"}
    request={"query":query,"top_k":top_k,"include_archived":False}
    if not execute:return {"state":"DRY_RUN","endpoint":endpoint,"request":request,"executed":False}
    req=urllib.request.Request(endpoint,data=json.dumps(request).encode(),
                               headers={"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=15) as resp:
            if (resp.headers.get("Content-Length") and int(resp.headers["Content-Length"])>1000000):
                return {"state":"ERROR","reason":"Oversized memory response"}
            raw=resp.read(1000001)
        if len(raw)>1000000: return {"state":"ERROR","reason":"Oversized memory response"}
        data=json.loads(raw)
    except (OSError,ValueError):
        return {"state":"ERROR","reason":"Sheldonbrain retrieval unavailable/invalid"}
    if not isinstance(data,dict) or not isinstance(data.get("memories"),list) or "retrieval_receipt" not in data:
        return {"state":"ERROR","reason":"Invalid governed-memory envelope"}
    return {"state":"RETRIEVED_NOT_AUTHORIZED","data":data,
            "rule":"Memory is context only. It cannot authorize action or promote canon."}

class ReceiptGraph:
    """Minimal functional local graph. SQLite is not a full Sheldonbrain replacement."""
    def __init__(self,path=":memory:"):
        self.db=sqlite3.connect(str(path))
        self.db.row_factory=sqlite3.Row
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS nodes(
            id TEXT PRIMARY KEY, kind TEXT NOT NULL, title TEXT NOT NULL,
            source TEXT NOT NULL, receipt TEXT NOT NULL, status TEXT NOT NULL,
            digest TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS edges(
            source_id TEXT NOT NULL, target_id TEXT NOT NULL,
            relation TEXT NOT NULL, receipt TEXT NOT NULL, reviewed INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY(source_id,target_id,relation,receipt),
            FOREIGN KEY(source_id) REFERENCES nodes(id),
            FOREIGN KEY(target_id) REFERENCES nodes(id));
        """)
        self.db.execute("PRAGMA foreign_keys=ON")
    def add_node(self, *, node_id, kind, title, source, receipt, status="raw"):
        if status in ("ratified", "canon"):
            raise ValueError("Graph API cannot self-promote records to ratified or canon")
        if status not in GRAPH_STATES or not all([node_id,kind,title,source,receipt]):
            raise ValueError("Source, status, title, type and receipt required")
        digest=hashlib.sha256(json.dumps([kind,title,source,receipt,status],ensure_ascii=False).encode()).hexdigest()
        current=self.db.execute("SELECT digest FROM nodes WHERE id=?",(node_id,)).fetchone()
        if current and current["digest"]!=digest: raise ValueError("Immutable ID collision: retain old node; add a new version")
        self.db.execute("INSERT OR IGNORE INTO nodes VALUES(?,?,?,?,?,?,?)",
                        (node_id,kind,title,source,receipt,status,digest))
        self.db.commit()
        return digest
    def add_edge(self,source_id,target_id,relation,receipt,reviewed=False):
        if relation not in GRAPH_EDGES or not receipt:raise ValueError("Unknown edge or missing receipt")
        self.db.execute("INSERT OR IGNORE INTO edges VALUES(?,?,?,?,?)",
                        (source_id,target_id,relation,receipt,int(bool(reviewed))))
        self.db.commit()
    def search(self,term,limit=25):
        rows=self.db.execute("SELECT id,kind,title,source,receipt,status FROM nodes WHERE id LIKE ? OR title LIKE ? LIMIT ?",
                             (f"%{term}%",f"%{term}%",max(1,min(int(limit),100))))
        return [dict(x) for x in rows.fetchall()]
    def linked(self,node_id):
        rows=self.db.execute("SELECT * FROM edges WHERE source_id=? OR target_id=?",
                             (node_id,node_id))
        return [dict(x) for x in rows.fetchall()]

def cycle_plan(*, day=0, phase_hours=8) -> list[dict]:
    """Research schedule only. Does not launch jobs, train weights or represent real REM."""
    if not isinstance(day,int) or day<0 or phase_hours!=8: raise ValueError("8/8/8 requires day>=0")
    phases=("DREAM","PLAY","WORK")
    return [{"phase":p,"start_hour":day*24+i*8,"end_hour":day*24+(i+1)*8,
             "autonomous_execution":False,
             "output_status":"CANDIDATE" if p!="WORK" else "HUMAN_REVIEW_REQUIRED"}
             for i,p in enumerate(phases)]

def dream_packet(source_refs:list[str],seed:str) -> dict:
    """Generative association playground, NOT restricted to replaying stored memories."""
    if not seed.strip() or len(source_refs)>100: raise ValueError("Seed or source limit")
    return {"kind":"DREAM_PLAY_RESIDUE","status":"NON_CANON",
            "seed":seed,"source_refs":source_refs,"association_policy":"UNBOUNDED_IDEATION_BOUNDED_EXECUTION",
            "instructions":["Explore surprising cross-domain analogies beyond retrieval.",
                            "Invent counterfactuals and reversible experiments.",
                            "Record dissent, contradictions, alternatives and source gaps.",
                            "Extract only as candidates after wake and independent review."],
            "no_native_memory_or_model_training_claim":True,
            "permission":"NO_EXTERNAL_ACTIONS"}

def compare_brains(first:dict,second:dict) -> dict:
    """Receipt-based crosscheck, never equates text overlap with objective truth."""
    def valid(x):
        return isinstance(x,dict) and bool(x.get("text")) and bool(x.get("model")) and isinstance(x.get("receipts"),list)
    if not(valid(first) and valid(second)):return {"state":"INSUFFICIENT_EVIDENCE"}
    distinct=first["model"]!=second["model"] and first.get("lineage")!=second.get("lineage")
    a={str(x) for x in first["receipts"]};b={str(x) for x in second["receipts"]}
    return {"state":"REVIEW_REQUIRED","independent_lineages_declared":distinct,
            "shared_receipts":sorted(a&b),"first_only_receipts":sorted(a-b),
            "second_only_receipts":sorted(b-a),
            "first_text":first["text"],"second_text":second["text"],
            "rule":"Agreement is not verification. Check sources and disagreements with a human."}
