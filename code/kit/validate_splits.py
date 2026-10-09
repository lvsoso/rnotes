"""Schema/leakage check, no model dependencies. Requires human-reviewed own data."""
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--dir',required=True);a=p.parse_args()
root=Path(a.dir);seen={};ids=set();manifest={}; expected=['digital_human','translation','agent_workflow','clarify','other']
for split in ['train','dev','calibration','test']:
 path=root/(split+'.jsonl');rows=[json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
 assert rows, f'{split} is empty';counts=Counter()
 for r in rows:
  assert r['split']==split,(r['id'],'wrong split');assert r['id'] not in ids, 'duplicate id';ids.add(r['id'])
  g=r['source_group_id'];assert g and seen.setdefault(g,split)==split, 'group leakage'
  assert r['metadata']['review_status'] in ['approved','human_reviewed'], 'human review missing'
  assert r['metadata'].get('reviewer'), 'reviewer missing'
  assert isinstance(r['state'],(str,dict)) and r['state'], 'empty state'
  assert len(r['qs'])==1 and r['qs'][0]['id']=='intent', 'this kit expects one intent question'
  q=r['qs'][0];assert q['t']=='choice' and list(q['crit'])==expected, 'label order mismatch'
  assert isinstance(q['y'],int) and 0<=q['y']<5,'invalid label'
  if 'soft' in q:
   assert len(q['soft'])==5 and all(isinstance(v,(float,int)) and 0<=v<=1 for v in q['soft']) and abs(sum(q['soft'])-1)<1e-6,'invalid soft target'
  counts[expected[q['y']]]+=1
 manifest[split]={'records':len(rows),'groups':len({r['source_group_id'] for r in rows}),'class_counts':dict(counts),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
 if len(counts)<5:print('WARNING:',split,'has missing classes')
(root/'train-dev.jsonl').write_text((root/'train.jsonl').read_text(encoding='utf-8').rstrip()+'\n'+(root/'dev.jsonl').read_text(encoding='utf-8').rstrip()+'\n',encoding='utf-8')
(root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Schema and source_group_id checks passed. Near duplicates and label quality still require manual audit.')
