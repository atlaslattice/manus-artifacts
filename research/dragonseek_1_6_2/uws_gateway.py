#!/usr/bin/env python3
"""UWS Full-Capability Gateway v0.2 (ATLAS ARI / DragonSeek).
Runs the user's actual UWS CLI across supported provider operations.
No command runs on import. No shell execution. No model-self-approved writes.
All external mutations require a trusted host callback or interactive human terminal.
Not an external deployment, official provider endorsement, or a credential manager.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from typing import Callable, Optional

READ_METHODS = frozenset({
    "list","get","search","query","lookup","fetch","read","find","show",
    "status","describe","discover","count","resolve","inspect","check",
    "export","download","metadata","watch","validate",
})
MUTATING_METHODS = frozenset({
    "create","insert","add","update","patch","modify","replace","append",
    "send","forward","reply","draft","copy","move","rename","upload",
    "import","write","post","put","delete","remove","destroy","trash",
    "purge","clear","archive","unarchive","restore","publish","unpublish",
    "share","unshare","grant","revoke","invite","respond","accept","decline",
    "execute","run","install","uninstall","deploy","start","stop","restart",
    "login","logout","setup","reset","submit","approve","reject","set",
})
SENSITIVE_METHODS = frozenset({
    "send","forward","delete","remove","destroy","purge","trash","clear",
    "revoke","share","unshare","grant","publish","deploy","reset",
    "install","uninstall","execute","run","respond",
})
TOKEN_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]{0,100}$")
MAX_JSON_LENGTH = 200_000

def _canonical(v):
    return json.dumps(v, sort_keys=True, ensure_ascii=False,
                      separators=(",",":"), allow_nan=False)

def proposal(command, *, params=None, body=None):
    """Validate structural command tokens; UWS owns the actual provider schema."""
    if (not isinstance(command,list) or not 1<=len(command)<=12
            or any(not isinstance(t,str) or not TOKEN_PATTERN.fullmatch(t)
                   for t in command)):
        return {"state":"DENIED","reason":"UWS command must use structural tokens, no flags or shell syntax"}
    if params is not None and not isinstance(params,dict):
        return {"state":"DENIED","reason":"--params must be a JSON object"}
    if body is not None and not isinstance(body,dict):
        return {"state":"DENIED","reason":"--json body must be a JSON object"}
    try:
        if len(_canonical({"params":params,"body":body}).encode())>MAX_JSON_LENGTH:
            return {"state":"DENIED","reason":"Command parameters too large"}
        digest=hashlib.sha256(_canonical({"command":command,"params":params,
                                         "body":body}).encode()).hexdigest()[:16]
    except (TypeError,ValueError,OverflowError):
        return {"state":"DENIED","reason":"Command arguments must be valid JSON"}
    verb=command[-1].lower()
    # An ambiguous command is classified as a write until a trusted human
    # validates its semantics. JSON bodies can be used by read operations too.
    operation="READ" if verb in READ_METHODS else "WRITE_OR_UNKNOWN"
    risk=("HIGH" if verb in SENSITIVE_METHODS else
          "APPROVAL_REQUIRED" if operation!="READ" else "LOW")
    return {"state":"PROPOSED","proposal_id":digest,
            "command":list(command),"operation":operation,"risk":risk,
            "has_query_params":params is not None,"has_request_body":body is not None,
            "requires_human_approval":operation!="READ",
            "provider_schema_validation":"DELEGATED_TO_UWS",
            "no_external_action_yet":True}

def _argv(binary,command,params,body,*,dry_run=False):
    argv=[binary,*command]
    if params is not None:argv.extend(["--params",_canonical(params)])
    if body is not None:argv.extend(["--json",_canonical(body)])
    argv.extend(["--format","json"])
    if dry_run:argv.append("--dry-run")
    return argv

def interactive_approval(plan):
    """Use only from a trusted local foreground human terminal."""
    if not sys.stdin.isatty():return False
    print("UWS external write request",file=sys.stderr)
    print("Operation:", " ".join(plan["command"]), file=sys.stderr)
    print("Risk:",plan["risk"],"ID:",plan["proposal_id"],file=sys.stderr)
    print("UWS native --dry-run preview:",file=sys.stderr)
    print(plan.get("preflight_preview", "(empty)"),file=sys.stderr)
    return input("Type APPROVE "+plan["proposal_id"]+" to authorize: ").strip()==(
        "APPROVE "+plan["proposal_id"])

def run_uws(command, *, params=None, body=None, execute=False,
            approval_callback:Optional[Callable[[dict],bool]]=None,
            timeout=30, binary=None):
    """Functional read and write UWS invocation, with explicit mutation gate.

    A trusted UI/terminal provides approval_callback. Never pass a model-made
    approval value as the callback. No automatic execution when execute=False.
    """
    plan=proposal(command,params=params,body=body)
    if plan["state"]!="PROPOSED":return plan
    if not execute:
        return {**plan,"state":"PLAN_ONLY","executed":False}
    path=binary or os.getenv("UWS_BINARY") or shutil.which("uws")
    if not path:
        return {**plan,"state":"UNAVAILABLE","executed":False,
                "reason":"Install/build UWS locally and connect provider OAuth first"}
    argv=_argv(path,command,params,body)
    if plan["requires_human_approval"]:
        # UWS's native request preview precedes human approval.
        try:
            preview=subprocess.run(_argv(path,command,params,body,dry_run=True),
                capture_output=True,text=True,timeout=min(max(timeout,1),60),
                shell=False,check=False)
        except (OSError,subprocess.TimeoutExpired):
            return {**plan,"state":"PREFLIGHT_ERROR","executed":False}
        if preview.returncode!=0:
            return {**plan,"state":"PREFLIGHT_ERROR","executed":False,
                    "returncode":preview.returncode}
        # Private data in the provider preview is not logged in the public repo.
        if approval_callback is None or not callable(approval_callback):
            return {**plan,"state":"APPROVAL_REQUIRED","executed":False,
                    "message":"Use an interactive terminal or trusted host approval callback"}
        try:approved=approval_callback({**plan,"preflight_preview":preview.stdout[:20000]})
        except Exception:
            approved=False
        if approved is not True:
            return {**plan,"state":"NOT_APPROVED","executed":False}
    try:
        p=subprocess.run(argv,capture_output=True,text=True,
            timeout=min(max(timeout,1),120),shell=False,check=False)
    except (OSError,subprocess.TimeoutExpired):
        return {**plan,"state":"EXECUTION_ERROR","executed":False}
    if p.returncode!=0:
        # Do not return provider error bodies: they can include private data.
        return {**plan,"state":"PROVIDER_ERROR","executed":False,
                "returncode":p.returncode}
    if len(p.stdout)>2_000_000:
        return {**plan,"state":"RESPONSE_TOO_LARGE","executed":True}
    try:data=json.loads(p.stdout)
    except (ValueError,TypeError):
        return {**plan,"state":"NON_JSON_RESPONSE","executed":True,
                "message":"UWS command completed; output not valid JSON"}
    return {**plan,"state":"EXECUTED","executed":True,"data":data,
            "visibility":"PRIVATE_LOCAL_RESPONSE_DO_NOT_PUBLISH"}

def main():
    ap=argparse.ArgumentParser(description="Local full-capability UWS gateway")
    ap.add_argument("--params",help="JSON object of API URL query parameters")
    ap.add_argument("--body",help="JSON object for API body")
    ap.add_argument("--execute",action="store_true",
                    help="Execute read now; writes require interactive approval")
    ap.add_argument("--timeout",type=int,default=30)
    ap.add_argument("command",nargs="+",help="UWS service resource method tokens")
    a=ap.parse_args()
    try:
        out=run_uws(a.command,params=json.loads(a.params) if a.params else None,
            body=json.loads(a.body) if a.body else None,execute=a.execute,
            timeout=a.timeout,approval_callback=interactive_approval if a.execute else None)
    except (ValueError,json.JSONDecodeError) as e:
        out={"state":"INVALID_INPUT","reason":str(e)}
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return 0 if out["state"] in ("EXECUTED","PLAN_ONLY") else 2
if __name__=="__main__":sys.exit(main())
