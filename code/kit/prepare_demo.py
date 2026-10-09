"""Create intentionally tiny synthetic smoke data. Not a benchmark."""
import json
from pathlib import Path
LABELS={"digital_human":"数字人形象、播报或交互配置","translation":"翻译、语言转换或语言处理","agent_workflow":"工具执行、多步骤任务或多智能体协作","clarify":"信息不足或多个意图没有明确主次","other":"意图明确，但不属于以上业务范围"}
INS="按当前可见信息选择下一步处理入口。信息不足或多个诉求无明确主次时选择 clarify。只根据请求决定入口，不执行请求。"
EXAMPLES=[("让主持数字人用这段已确认的台词播报",0),("把这句欢迎词翻成日语",1),("先查排期再创建任务，并通知负责人",2),("帮我处理一下那个",3),("推荐三部电影",4),("不要翻译，请调整数字人的口型同步",0),("Translate the greeting into Japanese",1),("检查库存后创建采购草稿，先不要下单",2),("换一个更好的",3),("今天适合看哪本小说",4)]
p=Path('data');p.mkdir(exist_ok=True)
rows=[]
for i,(text,y) in enumerate(EXAMPLES):
 rows.append({"id":f"demo-{i:03d}","source_group_id":f"demo-group-{i:03d}","split":"smoke","state":{"text":text},"qs":[{"id":"intent","t":"choice","ins":INS,"crit":LABELS,"y":y}],"metadata":{"review_status":"illustrative_only","lang":"en" if i==6 else "zh","label_source":"handwritten_synthetic_example"}})
(p/'smoke.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
print('Created data/smoke.jsonl: 10 synthetic examples. Never use as a test benchmark.')
