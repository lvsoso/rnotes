"""Independent metric helper for five-class routing. Standard library only."""
import math
LABELS=['digital_human','translation','agent_workflow','clarify','other']
def read(path):
 import json
 return [json.loads(x) for x in open(path,encoding='utf-8') if x.strip()]
def paired(gold,preds):
 by={r['id']:r for r in preds};assert len(by)==len(preds),'Duplicate prediction id'
 assert set(by)=={r['id'] for r in gold},'Missing/extra prediction id'
 pairs=[];failed=[]
 for g in gold:
  r=by[g['id']]
  if r.get('status')!='ok':failed.append(r);continue
  assert r['labels']==LABELS,'Label order differs';p=r['probabilities']
  assert len(p)==5 and all(math.isfinite(x) and 0<=x<=1 for x in p),'Bad probability'
  total=sum(p);assert abs(total-1)<=0.001,'Probabilities do not sum to 1'
  # Accommodate upstream four-decimal serialization, record this choice in report.
  p=[x/total for x in p];pairs.append((g['qs'][0]['y'],p,r))
 return pairs,failed
def scaled(p,t):
 assert math.isfinite(t) and t>0
 if t==1:return list(p)
 z=[math.log(max(v,1e-12))/t for v in p];m=max(z);x=[math.exp(v-m) for v in z];s=sum(x);return [v/s for v in x]
def nll(rows,t=1):return sum(-math.log(max(scaled(p,t)[y],1e-12)) for y,p,_ in rows)/len(rows)
def quantile(v,q):
 if not v:return None
 v=sorted(v);x=(len(v)-1)*q;lo=int(x);hi=min(lo+1,len(v)-1);return v[lo]+(v[hi]-v[lo])*(x-lo)
def summarize(rows,failed,total,t=1,threshold=0):
 assert rows,'No successful predictions';cm=[[0]*5 for _ in range(5)];brier=0;bins=[[] for _ in range(10)];accepted=[]
 for y,p,r in rows:
  p=scaled(p,t);pred=max(range(5),key=lambda k:p[k]);conf=p[pred];cm[y][pred]+=1
  brier+=sum((v-(k==y))**2 for k,v in enumerate(p));bins[min(int(conf*10),9)].append((conf,pred==y))
  if conf>=threshold:accepted.append(pred==y)
 per=[]
 for k in range(5):
  tp=cm[k][k];support=sum(cm[k]);predn=sum(row[k] for row in cm);den=support+predn
  per.append({'label':LABELS[k],'support':support,'precision':tp/predn if predn else None,'recall':tp/support if support else None,'f1':2*tp/den if den else 0.0})
 n=len(rows);reliability=[{'bin':i,'n':len(b),'confidence':sum(x for x,_ in b)/len(b) if b else None,'accuracy':sum(y for _,y in b)/len(b) if b else None} for i,b in enumerate(bins)]
 return {'attempted':total,'success':n,'failures':len(failed),'failure_rate':len(failed)/total,'accuracy_on_success':sum(cm[k][k] for k in range(5))/n,'correct_per_attempt':sum(cm[k][k] for k in range(5))/total,'macro_f1_fixed_5_on_success':sum(x['f1'] for x in per)/5,'per_class':per,'brier_multiclass_sum':brier/n,'nll':nll(rows,t),'ece_10_equal_width':sum(abs(sum(x for x,_ in b)-sum(y for _,y in b)) for b in bins)/n,'confusion_matrix':cm,'reliability':reliability,'temperature_relative_to_served_p':t,'threshold':threshold,'coverage_per_attempt':len(accepted)/total,'selective_error':1-sum(accepted)/len(accepted) if accepted else None,'accepted_n':len(accepted),'latency_ms_all_attempts':{'p50':quantile([r['latency_ms'] for _,_,r in rows]+[r['latency_ms'] for r in failed],.5),'p95':quantile([r['latency_ms'] for _,_,r in rows]+[r['latency_ms'] for r in failed],.95)},'notes':['Successful probability vectors within 0.001 of sum 1 are normalized for rounding.','Macro F1 averages five fixed labels; absent classes have F1=0 and must be disclosed.','Failed requests reduce coverage and correct_per_attempt. Report them separately from probability metrics.']}
