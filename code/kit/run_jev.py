"""Optional paid API runner. Sends state/criteria to TypeSafe; use only approved data."""
import argparse,json,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--allow-api',action='store_true');a=p.parse_args()
assert a.allow_api,'Read data/privacy/cost policy, then explicitly pass --allow-api'
from typesafe_sdk import Choice,RetryPolicy,TypeSafeClient
out=Path(a.output);assert not out.exists(),'Use a fresh output path';out.parent.mkdir(parents=True,exist_ok=True)
rows=[json.loads(x) for x in Path(a.input).read_text(encoding='utf-8').splitlines() if x.strip()]
with TypeSafeClient(model='jev-1.13.0',timeout=30.0,retry=RetryPolicy(max_retries=0)) as client,out.open('w',encoding='utf-8') as f:
 for r in rows:
  q=r['qs'][0];assert q['t']=='choice';start=time.perf_counter()
  try:
   response=client.system_one(state=r['state'],questions={q['id']:Choice(instructions=q['ins'],criteria=q['crit'])})
   ms=(time.perf_counter()-start)*1000;ans=response.choices[q['id']];labels=list(q['crit'])
   result={'id':r['id'],'labels':labels,'probabilities':[float(ans.probabilities[k]) for k in labels],'prediction':ans.choice,'latency_ms':ms,'status':'ok','model':response.model,'request_id':response.request_id,'raw':response.raw_http_response.json()}
  except Exception as e:
   result={'id':r['id'],'status':'error','latency_ms':(time.perf_counter()-start)*1000,'error':type(e).__name__+': '+str(e)}
  f.write(json.dumps(result,ensure_ascii=False)+'\n');f.flush()
print(out)
