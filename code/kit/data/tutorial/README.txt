Jev 五分类路由：合成教学数据说明

一、这份数据能做什么
包含 320 条逐条编写的合成请求：主数据 300 条，另有 20 条单独保留的 challenge 挑战样本。
用途是练习“训练—验证—校准—测试”流程、观察路由错误和检查代码是否正常运行。
所有请求与标签解释均由 AI 编写并检查，没有人工审核，不是真实业务样本，也不是正式性能基准。
不要把这里的准确率、置信度或阈值解释为真实业务能力或上线效果。

二、文件清单
train.jsonl             150 条，每类 30 条；用于训练
dev.jsonl                50 条，每类 10 条；用于选择设置和检查开发效果
calibration.jsonl        50 条，每类 10 条；用于演示阈值或置信度校准
test.jsonl               50 条，每类 10 条；最后一次独立评估
challenge.jsonl          20 条，每类 4 条；额外检查否定、引号指令和易混淆情况
train-dev.jsonl         200 条；严格按 train + dev 拼接，保留原来的 split 值
label_order.json         五个候选标签的固定顺序
label_policy_v1.txt      完整标注规则，尤其要先看边界与优先级
data_preview.csv        全部 320 条的可读预览，含文本、标签、索引、分组、语言、理由与来源声明
manifest.json           样本数、分组数、语言统计和 SHA-256 文件校验值
build_dataset.py        显式列出全部样本的构建脚本，不使用词语排列组合来扩充数量
../../validate_tutorial.py  检查脚本位于 kit/，不在本数据目录内；只使用 Python 标准库

三、快速检查
在教程 jevlab 根目录运行：
python kit/validate_tutorial.py --dir kit/data/tutorial

需要重新生成教学数据时，仍从 jevlab 根目录运行：
python kit/data/tutorial/build_dataset.py
python kit/validate_tutorial.py --dir kit/data/tutorial

构建脚本把文件写到它自身所在的 kit/data/tutorial/。生成后再运行检查脚本，使 manifest.json 与当前文件保持一致。

四、字段和模型输入
每行 JSONL 都有 id、source_group_id、split、state.text、一个 qs 中的 intent 问题，以及 metadata。
qs[0].y 是从 0 开始的类别索引；候选顺序固定为：
0 digital_human
1 translation
2 agent_workflow
3 clarify
4 other
所有行采用同一问题说明和同一候选描述；没有 soft 概率标签。

state / qs 与本教程推理结构兼容。盲测时，答案 y 和 metadata.rationale 只能用于评分或检查，不能拼进模型提示词。应调用管线已有的 state、题目和候选编码逻辑，不要把整个 JSON 对象当成输入文字。
训练、推理、校准和评分时，候选顺序都不能变化。

五、训练审核开关
固定版本的训练器默认拒绝这些未经人工审核的合成数据。
只有明确传入 --allow-assistant-reviewed-pilot，才能让 reviewed-data loader 接收 train-dev.jsonl。
这是公开标明来源的小型教学试验开关，不代表人工真值。
不要为了通过检查，把 review_status 改成 approved 或 human_reviewed。
原来的 validate_splits.py 人工审核门槛仍然不满足；本文件夹的 validate_tutorial.py 只检查合成教学数据。
calibration、test、challenge 不应交给只接收 train/dev 的训练 loader。

六、如何使用五个划分
只用 train 学习；用 dev 选择设置；用 calibration 演示阈值校准；最后评估 test；challenge 另外报告。
challenge 不参与训练、模型选择、阈值选择，也不在 train-dev 中。
这些校准样本故意按类别均衡，并非真实类别分布。只有 50 条，不能证明生产环境中的置信度可靠。
本包没有预先编造或填入模型性能数字。

七、分组与局限
直接改写或互译的样本共享 source_group_id，并留在同一个划分。
具体情景事先分配到各划分，没有把同源行随机拆开。
train 有 144 个分组；dev、calibration、test 各 45 个；challenge 有 20 个，共 299 组。
划分内部用 id 的哈希值做确定性打散，避免同一类别连续排列。

检查脚本能发现显式分组跨划分和规范化后的原文重复，不能证明所有语义近似都已消除。
所有样本仍来自同一 AI 作者风格，各划分仍反复出现同类语言模式和规则。
不同地点、人物或物品的情景变化，不等于严格的分布外测试。
这套数据能验证教学流程，不能证明业务泛化能力。真实使用需要有代表性的数据、独立人工审核和更严格的去重与划分。

八、语言与标注边界
以中文为主，包含英语，以及一条西班牙语、一条法语指令；具体数量见 manifest.json。
metadata.lang 表示指令的主要语言，不是被提及的翻译目标语言；这些样本不构成多语言能力认证。
translation 在本教程中包含翻译、转写、校对、已有文字改写和明确的语言分析；从零创作诗歌、故事或口号通常属于 other。
“缺少执行参数”不等于“无法判断入口”：例如“把欢迎词翻成日语”即使没附欢迎词，仍属于 translation。
只有入口本身不明，或互斥需求没有明确选择时，才用 clarify。
预测到 agent_workflow 也不代表可以直接发送、删除、登录或修改数据；执行阶段仍必须检查权限和确认要求。
