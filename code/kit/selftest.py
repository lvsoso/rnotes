from metrics import summarize,scaled,paired
p=[(.0,.0,1.,.0,.0)];rows=[(2,list(p[0]),{'id':'x','latency_ms':10})]
r=summarize(rows,[],1);assert r['brier_multiclass_sum']<1e-15 and r['accuracy_on_success']==1
r=summarize([(0,[0,0,1,0,0],{'latency_ms':10})],[],1);assert abs(r['brier_multiclass_sum']-2)<1e-10
q=scaled([.8,.05,.05,.05,.05],2);assert abs(sum(q)-1)<1e-12 and q[0]<.8
assert summarize(rows,[],1,threshold=1)['accepted_n']==1
print('PASS: metric arithmetic, temperature normalization, threshold boundary. No models or APIs executed.')
r=summarize([(0,[.2]*5,{'latency_ms':20})],[],1);assert abs(r['brier_multiclass_sum']-.8)<1e-12
r=summarize([(0,[.6,.1,.1,.1,.1],{'latency_ms':20})],[{'latency_ms':40}],2,threshold=.5);assert r['coverage_per_attempt']==.5 and r['failure_rate']==.5
try:paired([{'id':'x','qs':[{'y':0}]}],[])
except AssertionError:pass
else:raise AssertionError('Missing IDs must fail')
print('PASS: uniform Brier, failed-request accounting, ID integrity.')
