#!/usr/bin/env python3
import json,sys
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
ROOT=Path(__file__).resolve().parent
EXPECTED={'invariants':3,'doctrines':6}
def load():
 out=[];missing=[]
 for kind,num in EXPECTED.items():
  for n in range(1,num+1):
   p=ROOT/'registry'/f'{kind}_{n:02d}.json'
   if not p.exists():missing.append(str(p.relative_to(ROOT)));continue
   try:
    obj=json.loads(p.read_text())
    for e in obj['entries']:
     e['kind']=kind;e['source']=obj['source'];out.append(e)
   except (ValueError,KeyError) as exc:missing.append(f'{p.name}: {exc}')
 return out,missing
def main():
 cmd=sys.argv[1] if len(sys.argv)>1 else 'status'
 if cmd=='serve':
  print('http://127.0.0.1:8765/index.html',flush=True)
  ThreadingHTTPServer(('127.0.0.1',8765),partial(SimpleHTTPRequestHandler,directory=str(ROOT))).serve_forever()
  return
 items,missing=load()
 result={'source':'historical Aluminum OS registries','ratification':'user reported; independent record not verified','entries':len(items),'missing':missing,'known_conflicts':['INV-0 historical definitions differ']}
 if cmd in ('search','context'):
  query=' '.join(sys.argv[2:]).casefold()
  result['matches']=[e for e in items if query in (e['id']+' '+e['name']+' '+e['body']).casefold()][:20 if cmd=='search' else 8]
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
