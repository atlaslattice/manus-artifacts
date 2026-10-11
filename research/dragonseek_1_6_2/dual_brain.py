#!/usr/bin/env python3
"""Two-brain constitutional cross-review prototype. Two opt-in, independently
named OpenAI-compatible inference endpoints. No model receives tools.
Review output remains a candidate; no automatic canon or write access.
"""
import argparse, json, os, re, sys
from urllib.request import Request, urlopen
from urllib.parse import urlsplit
from atlas_fabric import compare_brains, endpoint_allowed
from ai_bridge import model_payload
from dragonseek_os import load

RECEIPT_RE=re.compile(r"\b(?:INV-\d+|D-\d+[a-zA-Z-]*|SHUGS[-_A-Z0-9.]*)\b")

def check_endpoint(url,allow_remote):
    u=urlsplit(url)
    if not endpoint_allowed(url,allow_remote):
        raise ValueError("Use loopback or explicit --allow-remote with HTTPS")
    if u.path not in ("/v1/chat/completions", "/chat/completions"):
        raise ValueError("Expected compatible /v1/chat/completions endpoint")

def completion(messages,*,url,model,key_env,allow_remote=False):
    check_endpoint(url,allow_remote)
    key=os.getenv(key_env,"")
    headers={"Content-Type":"application/json"}
    if key:headers["Authorization"]="Bearer "+key
    request={"model":model,"messages":messages,"stream":False,"temperature":0}
    req=Request(url,data=json.dumps(request,ensure_ascii=False).encode(),
                headers=headers,method="POST")
    with urlopen(req,timeout=90) as response:
        content=response.read(2_000_001)
        if len(content)>2_000_000:raise ValueError("Model response too large")
    packet=json.loads(content)
    answer=packet["choices"][0]["message"]["content"]
    if not isinstance(answer,str) or not answer.strip():raise ValueError("Empty response")
    return answer

def prepare_pair(question,primary_model,review_model):
    """Generate both prompts offline. Both have the same canonical invariant."""
    first=model_payload(question,primary_model)
    review=model_payload(question,review_model)
    review["messages"].append({"role":"system","content":
        "You are the independent counter-review brain. For every factual claim, "
        "mark VERIFIED_SOURCE, CONTRADICTED, UNVERIFIED, or PROPOSED. "
        "Challenge the primary brain, report missing evidence, and do not assume agreement establishes truth. "
        "Return human-readable dissent and original source IDs. No tool calls."})
    return first,review

def evaluate(question,*,primary_model,primary_url,primary_lineage,
             review_model,review_url,review_lineage,allow_remote=False,dry_run=True):
    if not question.strip():raise ValueError("Question required")
    if len(question)>12000:raise ValueError("Question too long")
    if primary_lineage==review_lineage:
        warning="Same declared model lineage: comparison is NOT independent."
    else:warning=None
    if not load()["complete"]:
        return {"state":"BLOCKED_INCOMPLETE_CONSTITUTION"}
    first,review=prepare_pair(question,primary_model,review_model)
    check_endpoint(primary_url,allow_remote);check_endpoint(review_url,allow_remote)
    if dry_run:
        return {"state":"DRY_RUN_NO_NETWORK","primary_model":primary_model,
            "review_model":review_model,"primary_lineage":primary_lineage,
            "review_lineage":review_lineage,"warning":warning,
            "first_messages":first["messages"],"review_messages":review["messages"],
            "no_tool_access":True}
    a=completion(first["messages"],url=primary_url,model=primary_model,
                 key_env="DRAGON_PRIMARY_API_KEY",allow_remote=allow_remote)
    review["messages"].append({"role":"user","content":
        "Independently audit the following candidate answer, cite contrary evidence, "
        "and identify assumptions. It is UNVERIFIED:\n"+a})
    b=completion(review["messages"],url=review_url,model=review_model,
                 key_env="DRAGON_REVIEW_API_KEY",allow_remote=allow_remote)
    result=compare_brains(
       {"model":primary_model,"lineage":primary_lineage,"text":a,
        "receipts":sorted(set(RECEIPT_RE.findall(a)))},
       {"model":review_model,"lineage":review_lineage,"text":b,
        "receipts":sorted(set(RECEIPT_RE.findall(b)))})
    result.update({"warning":warning,"status":"CANDIDATE_NEEDS_HUMAN_REVIEW",
        "no_external_tools":True,
        "cited_id_extraction":"lexical-only; cited IDs were NOT independently verified by this run"})
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--ask",required=True)
    p.add_argument("--primary-model",required=True)
    p.add_argument("--review-model",required=True)
    p.add_argument("--primary-lineage",required=True)
    p.add_argument("--review-lineage",required=True)
    p.add_argument("--primary-url",default="http://127.0.0.1:11434/v1/chat/completions")
    p.add_argument("--review-url",default="http://127.0.0.1:11434/v1/chat/completions")
    p.add_argument("--allow-remote",action="store_true")
    p.add_argument("--execute",action="store_true")
    a=p.parse_args()
    try:
        result=evaluate(a.ask,primary_model=a.primary_model,primary_url=a.primary_url,
            primary_lineage=a.primary_lineage,review_model=a.review_model,
            review_url=a.review_url,review_lineage=a.review_lineage,
            allow_remote=a.allow_remote,dry_run=not a.execute)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (OSError,ValueError,KeyError,IndexError,json.JSONDecodeError) as e:
        print(json.dumps({"state":"ERROR","detail":str(e)}),file=sys.stderr)
        sys.exit(1)
if __name__=="__main__":main()
