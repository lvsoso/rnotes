新版入口：先读 START_HERE.txt。已附 300 条四份切分教学数据和 20 条挑战例，详见 data/tutorial/。

Jev and Laya routing experiment helper kit
Checked 2026-10-03. Read the DOCX/PDF guide first.
These original helper scripts are supplied as editable educational examples.
They are not part of Jev, Laya, or the Datawhale upstream projects.
No API/model inference/training has been executed while preparing this kit.
Static Python compilation and small arithmetic tests were run. Hardware execution remains a checkpoint.

Files
prepare_demo.py       10 synthetic smoke examples; not human-gold or a benchmark
validate_splits.py    own reviewed train/dev/calibration/test schema and group leakage
run_laya.py           canonical SDK or cookbook client adapter
run_jev.py            optional TypeSafe API call; requires --allow-api, may incur costs
fit_temperature.py   held-out calibration post-processing of served probabilities
metrics.py            macro-F1, Brier, ECE, coverage, selective error and latency
evaluate.py          report from aligned gold/predictions; not a chart builder
selftest.py           tiny local arithmetic checks

Outputs must use fresh paths. Original model outputs remain in raw JSON.
Only state and question schema are sent to the model, never y/soft or review metadata.
Do not upload company data to an API without the required company approval.
Do not paste API keys into chat, screenshots, code, or Git. Configure them safely on your own machine.
Predictions contain input-associated data and may be sensitive. Keep the working folder private.
No script in this kit executes routed tools or actions.

Quick check, in this folder
python selftest.py
python prepare_demo.py

Canonical Laya, after separately installing compatible PyTorch and laya
python run_laya.py --input data/smoke.jsonl --output runs/smoke.jsonl --model convaiinnovations/laya-multilingual --device cpu
python evaluate.py --gold data/smoke.jsonl --pred runs/smoke.jsonl --output runs/smoke_metrics.json
Numbers from this synthetic smoke test demonstrate the pipeline only.

See guide for isolated environments, pinned source, model hashes, data splitting,
CUDA fine-tuning, calibration, fair baselines, and evidence capture.

GPU and environment clarification — 2026-10-03
The CPU quick check above remains available. For the user's checked NVIDIA
AutoDL server, explicitly use CUDA (run_laya.py defaults to CPU):
python run_laya.py --input data/smoke.jsonl --output runs/smoke_cuda.jsonl --model convaiinnovations/laya-multilingual --device cuda
python evaluate.py --gold data/smoke.jsonl --pred runs/smoke_cuda.jsonl --output runs/smoke_cuda_metrics.json
Do not rerun into an existing output path; choose a fresh run directory.
The underlying torch/GPU check passed, but this does not validate Laya yet.
See DEPENDENCIES.txt for the actual checked environment, official Laya minimums,
and the distinction between canonical SDK and cookbook requirements.
Text-only Laya needs neither torchvision nor torchaudio; Jev API needs no torch.

📸 截图操作清单（与指南步骤标记、最新 27 页 PPT 一致）
编号是一份证据组，可包含多张图。截图是讲解材料，不能代替 JSON/CSV。
先保存原始结果，再打开终端、JSON 编辑器、HTML 报告或汇总表进行截图。
服务器无需桌面；可把日志/报告安全下载后在本地打开。统一放 evidence/。
截图前遮蔽密钥、账户信息和未授权原文，保留模型/数据/设备版本。

ENV 环境检查，可选附件，不计模型结果
- 时机：第 03 节 Python/torch/CUDA/nvidia-smi 检查结束后
- 画面：Python、解释器、torch、torch CUDA runtime、available、GPU 名称
- 留档：before-install/inference/training requirements lock 和终端文本
- 文件例：ENV_AutoDL_4090D.png；PPT 可放备注，不替代 E01–E06

E02 本地 Laya 输出 → PPT 第 14 页
- 时机：第 06 节 run_laya.py、evaluate.py 成功完成之后
- 打开输入与预测中同一 id；只截 runner 打印的文件路径不算结果
- 画面：输入、top-1、完整五类概率、status、latency_ms、model/device 命令
- 留档：输入/预测 JSONL、metrics JSON、依赖和设备、权重 SHA256
- 文件例：E02_laya_smoke_cuda.png；注明“10 条合成 smoke，只验证链路”

E01 LLM labels-only 输出 → PPT 第 14 页
- 时机：第 07 节已批准 provider/model 返回真实 labels-only 响应之后
- 本包没有通用 LLM runner，不能把上游示例代码截图当运行结果
- 画面：与 E02 相同的输入/候选、标签、模型 ID、耗时、usage、尝试次数
- 留档：原始请求/响应、真实标签与成本；缺失用量写未知
- evaluate.py 要求五类概率，不能直接用于 labels-only；标签指标须另算，禁止补造概率
- 文件例：E01_llm_labels_only.png；Jev 可选 E01_jev_optional.png

E03 train/dev 曲线 → PPT 第 15 页
- 时机：第 09 节训练结束并运行 visualize_training.py，打开实际 HTML 后
- 画面：train/dev loss、epoch、选中 checkpoint、dev 选模规则、组数和 seed
- 留档：完整 run、training_log.csv/jsonl、experiment.json、HTML
- 文件例：E03_head_train_dev.png；不画 test 曲线，不造示意测量值

E05 温度拟合记录 → PPT 第 17 页辅助证据
- 时机：第 11 节 fit_temperature.py 完成之后
- 画面：relative_temperature、nll_before、nll_after、sample_count、boundary
- 留档：独立 calibration 预测/输入和温度 JSON
- 文件例：E05_temperature_calibration.png；最终两图见下条 E05

E04 锁定测试结果 → PPT 第 16 页
- 时机：第 12 节所有冻结候选完成相同 test 后，汇总真实指标
- 概率模型用 metrics JSON；labels-only 的 macro-F1/召回/混淆矩阵另行按标签计算
- 画面：模型、macro-F1、clarify recall、失败率、p95、支持数、校准标记
- 附混淆矩阵；高置信错路由注明阈值与分母，不能用 ECE 代替
- LLM labels-only 没有概率的指标标 N/A，不补造概率
- 留档：test manifest、逐条预测、JSON、汇总 CSV、硬件/并发/重试条件
- 文件例：E04_test_metrics.png、E04_confusion_matrix.png

E05 可靠性与覆盖率 → PPT 第 17 页
- 时机：calibration 冻结温度/阈值，test 评估完成，并用真实 JSON 作图后
- A 图：raw/calibrated 的 reliability（每桶 n/confidence/accuracy）
- B 图：coverage_per_attempt 与 selective_error（每点 accepted_n）
- 预先确定阈值网格；同一预测可生成多阈值报告，标出冻结工作点
- test 上的曲线只作描述展示，不在 test 上重新挑业务阈值/温度
- accepted_n=0 时错误率未定义，不写成 0
- 留档：绘图代码/CSV、全部点的 JSON、温度和冻结阈值
- 文件例：E05A_reliability.png、E05B_coverage_error.png
- evaluate.py 计算单个阈值的指标，不自动绘图；需用 Notebook/表格汇总

E06 失败与回退 → PPT 第 18 页
- 时机：第 06/09/12 节遇到实际错误/信息不足时保存，第 14 节整理卡片
- 画面：匿名 case_id、输入、人工依据、实际 top-1/五类概率、影响与回退
- 本包不执行回退；写清“拟定/未实现”，只有实际执行过才能写“已执行”
- 复测未执行写“待复测”；没有失败时不能编造失败率或案例
- 留档：原始预测、人工裁决、版本和复测记录；敏感内容用合成复现句
- 文件例：E06_case001_fallback.png

PPT 第 21 页是 E01–E06 回填汇总。所有结果数字仍需实际运行后填写。
此版本补充截图指引、依赖/设备说明及合成教学数据，没有执行模型下载、推理、训练
或任何付费 API，也没有改变 run_laya.py 的 CPU 默认值。
