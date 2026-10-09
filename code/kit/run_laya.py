"""Source-checked Laya adapter. Model execution must be validated on your hardware."""
import argparse,json,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--model',required=True);p.add_argument('--cookbook-root');p.add_argument('--device',default='cpu');p.add_argument('--warmup',type=int,default=3);a=p.parse_args()
out=Path(a.output);assert not out.exists(),'Use a fresh output path';out.parent.mkdir(parents=True,exist_ok=True)
rows=[json.loads(x) for x in Path(a.input).read_text(encoding='utf-8').splitlines() if x.strip()]
assert rows and a.warmup>=0
if a.cookbook_root:
 sys.path.insert(0,str(Path(a.cookbook_root).resolve()))
 from laya.client import LayaClient
 agent=LayaClient(model_dir=a.model,device=a.device);predict=agent.system_one
else:
 import laya
 agent=laya.load(a.model,device=a.device);predict=agent.predict
import torch
def sync():
 if a.device.startswith('cuda'):torch.cuda.synchronize()
 elif a.device=='mps':torch.mps.synchronize()
def request(r):
 q=r['qs'][0];assert q['t']=='choice'
 return r['state'],{q['id']:{'type':'choice','instructions':q['ins'],'criteria':q['crit']}}
for i in range(a.warmup):predict(*request(rows[i%len(rows)]))
sync()
with out.open('w',encoding='utf-8') as f:
 for r in rows:
  q=r['qs'][0];sync();start=time.perf_counter()
  try:
   result=predict(*request(r));sync();ms=(time.perf_counter()-start)*1000
   ans=result['answers'][q['id']];labels=list(q['crit']);values=[float(ans['probabilities'][k]) for k in labels]
   record={'id':r['id'],'labels':labels,'probabilities':values,'prediction':ans['choice'],'latency_ms':ms,'status':'ok','raw':result}
  except Exception as e:
   record={'id':r['id'],'status':'error','latency_ms':(time.perf_counter()-start)*1000,'error':type(e).__name__+': '+str(e)}
  f.write(json.dumps(record,ensure_ascii=False)+'\n');f.flush()
print(out)
