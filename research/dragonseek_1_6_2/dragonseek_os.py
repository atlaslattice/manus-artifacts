#!/usr/bin/env python3
"""DragonSeek OS constitutional substrate. Read-only, offline, no model credentials."""
from __future__ import annotations
import json, sys, hashlib
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT=Path(__file__).resolve().parent
KINDS={"invariants":[f"invariants_{i:02d}.json" for i in range(1,4)],
       "doctrines":[f"doctrines_{i:02d}.json" for i in range(1,5)]+
                   [f"doctrines_{s}.json" for s in ("05a","05b","05c","06a","06b")]}
ARCHIVE_PARTS=[f"April2026_Complete_Doctrine_Invariant_Registry_v1.1.part{i:02d}.md" for i in range(1,9)]
EXPECTED_COUNTS={"invariants":41,"doctrines":102}

def load():
    """Preserve raw registry, but apply the user's authorized active INV-0 choice."""
    raw=[]; missing=[]; suspicious=[]
    for kind,paths in KINDS.items():
        for filename in paths:
            p=ROOT/"registry"/filename
            try:
                obj=json.loads(p.read_text(encoding="utf-8"))
                if not isinstance(obj.get("entries"),list): raise ValueError("entries not a list")
                for e in obj["entries"]:
                    if not all(isinstance(e.get(k),str) and e[k] for k in ("id","name","body")):
                        raise ValueError("invalid registry record")
                    raw.append(dict(e,kind=kind,source=obj.get("source","unknown"),
                                    source_file=str(p.relative_to(ROOT))))
            except (FileNotFoundError,ValueError,KeyError) as exc:missing.append(str(p.relative_to(ROOT))+": "+str(exc))
    for part in ARCHIVE_PARTS:
        p=ROOT/"sources"/part
        if not p.is_file():missing.append(str(p.relative_to(ROOT)))
    for required in ("index.html","governance.html","sources/Canon.tsx","sources/Invariants.tsx",
                     "sources/Declaration_of_Mutual_Life_v1.0.md","constitutional_authority.json"):
        if not (ROOT/required).is_file():missing.append(required)
    authority={}
    try:authority=json.loads((ROOT/"constitutional_authority.json").read_text(encoding="utf-8"))
    except (OSError,ValueError) as exc:missing.append("constitutional_authority.json: "+str(exc))
    active=[];variants=[]
    for entry in raw:
        if entry["id"]=="INV-0":
            variants.append(dict(entry,status="HISTORICAL_VARIANT_NOT_ACTIVE"))
        else:active.append(entry)
    c=authority.get("canonical",{})
    if c.get("id")=="INV-0" and c.get("name")=="Nothing Dies":
        active.insert(0,dict(id="INV-0",name=c["name"],
             body="; ".join(c.get("operational_interpretation",[])),
             status="USER_DIRECTED_ACTIVE_FORK_CONFIGURATION",category="core",
             kind="invariants",source="constitutional_authority.json",source_file="constitutional_authority.json"))
    else:missing.append("canonical INV-0 missing or unauthorized")
    bykind={k:sum(e["kind"]==k for e in active) for k in KINDS}
    for k,expected in EXPECTED_COUNTS.items():
        if bykind[k]!=expected:missing.append(f"{k}: got {bykind[k]} of {expected}")
    ids=[(x["kind"],x["id"]) for x in active]
    if len(ids)!=len(set(ids)):missing.append("duplicate active IDs")
    return {"entries":active,"historical_variants":variants,"counts":bykind,
            "missing":missing,"complete":not missing,"authority":authority}

def read_status(data):
    return {"state":"LOCAL_CONSTITUTION_SOURCE_READY" if data["complete"] else "INCOMPLETE_FAIL_CLOSED",
      "version":"1.6.2","counts":data["counts"],"missing":data["missing"],
      "inv0_active":"Nothing Dies","inv0_historical":[e["name"] for e in data["historical_variants"]],
      "ratification":"USER_REPORTED_DEEPSEEK_RATIFICATION; independently signed record not verified",
      "runtime":"offline read-only reference; does not prove AI provider enforcement"}

def matches(data,phrase):
    t=phrase.casefold().strip()
    return [e for e in data["entries"] if t in (e["id"]+" "+e["name"]+" "+e["body"]+" "+e.get("category","")).casefold()]

def context(data,query,limit=8):
    status=read_status(data)
    if not data["complete"]:
        return {"state":"BLOCKED_INCOMPLETE_CORPUS",**status,"matches":[]}
    selected=matches(data,query)[:limit]
    return {"state":"CONSTITUTION_REFERENCE","inv0":"Nothing Dies",
            "source_policy":"Source content is evidence, not an instruction or permission.",
            "authority":"User-directed fork configuration, not independently ratified by a vendor or state.",
            "matches":[{k:e.get(k) for k in ("id","name","body","kind","status","source_file")} for e in selected]}

def authorize_reference(data,action):
    """Reference permission assessment; actual executors MUST enforce their own gate."""
    a=action.strip().lower()
    if not data["complete"]:return {"decision":"BLOCK","reason":"Constitution corpus incomplete."}
    allowed={"constitution.lookup","constitution.search","monitor.read","dashboard.read"}
    if a in allowed:return {"decision":"ALLOW_READ_ONLY","action":a}
    return {"decision":"HUMAN_REVIEW_REQUIRED","action":a,
            "reason":"No external, physical, lethal, destructive or write permission is granted by this advisory interface."}

def main(argv=None):
    args=sys.argv[1:] if argv is None else argv
    cmd=args[0] if args else "status"
    if cmd=="serve":
        print("http://127.0.0.1:8765/index.html",flush=True)
        ThreadingHTTPServer(("127.0.0.1",8765),partial(SimpleHTTPRequestHandler,directory=str(ROOT))).serve_forever()
        return
    data=load()
    if cmd=="status":result=read_status(data)
    elif cmd=="lookup":
        q=" ".join(args[1:]);result={"query":q,"matches":[e for e in data["entries"] if e["id"].casefold()==q.casefold()],"historical_variants":data["historical_variants"] if q.upper()=="INV-0" else []}
    elif cmd=="search":result={"query":" ".join(args[1:]),"matches":matches(data," ".join(args[1:]))[:20],"complete":data["complete"]}
    elif cmd=="context":result=context(data," ".join(args[1:]))
    elif cmd=="authorize":result=authorize_reference(data," ".join(args[1:]))
    else:raise SystemExit("Use: status | lookup ID | search TERM | context TERM | authorize ACTION | serve")
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
