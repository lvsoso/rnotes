"""Post-process served probabilities only; never mutate model config."""
import argparse,json
from pathlib import Path
from metrics import read,paired,nll
p=argparse.ArgumentParser();p.add_argument('--gold',required=True);p.add_argument('--pred',required=True);p.add_argument('--output',required=True);a=p.parse_args()
g=read(a.gold);assert all(r['split']=='calibration' for r in g),'Calibration split required'
rows,failed=paired(g,read(a.pred));assert rows and not failed,'Resolve failed calibration requests before fitting'
grid=[.5+i*.025 for i in range(181)];best=min(grid,key=lambda t:nll(rows,t))
out=Path(a.output);assert not out.exists(),'Use a fresh output path'
out.write_text(json.dumps({'relative_temperature':best,'nll_before':nll(rows),'nll_after':nll(rows,best),'sample_count':len(rows),'boundary':best in [grid[0],grid[-1]],'scope':'Post-processing served five-class probabilities; do not write this number to model temperature.'},indent=2)+'\n');print(out.read_text())
