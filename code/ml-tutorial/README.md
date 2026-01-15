# Kibana ML 教程

快速学习 Elasticsearch 和 Kibana 机器学习功能的独立教程。

## 前置条件

- Elasticsearch 7.9.1
- Kibana 7.9.1
- Python 3.7+

## 快速开始

```bash
# 1. 安装依赖
cd scripts
pip install -r requirements.txt

# 2. 生成测试数据
python3 generate_logs.py -n 10000 -o data --days 7

# 3. 导入数据
python3 import_to_es.py data/nginx-logs.ndjson

# 4. 访问 Kibana
open http://localhost:5601
```

## 目录结构

```
ml-tutorial/
├── README.md              # 本文件
├── docs/                  # 文档
│   ├── quick-start.md    # 快速开始
│   └── ...
├── scripts/               # 脚本
│   ├── generate_logs.py  # 数据生成
│   ├── import_to_es.py   # 数据导入
│   └── requirements.txt  # Python 依赖
├── config/                # 配置文件
│   ├── anomaly-detection/
│   ├── data-frame-analytics/
│   └── elasticsearch/
├── data/                  # 生成的数据
└── examples/              # 示例
```

## 文档

- [快速开始指南](docs/quick-start.md) - 30分钟完整流程
- [故障排查](docs/troubleshooting.md) - 常见问题解决

### Data Frame Analytics
- [DFA 概述](docs/data-frame-analytics/overview.md) - 了解批量分析
- [离群点检测](docs/data-frame-analytics/outlier-detection.md) - 发现异常数据
- [分类](docs/data-frame-analytics/classification.md) - 预测威胁类型
- [回归](docs/data-frame-analytics/regression.md) - 预测响应时间

## 认证方式

支持三种认证方式（优先级从高到低）：

```bash
# 1. 命令行参数
python3 import_to_es.py data.ndjson -u elastic -p changeme

# 2. URL 格式
python3 import_to_es.py data.ndjson -e http://elastic:changeme@localhost:9200

# 3. 环境变量
export ES_USERNAME=elastic
export ES_PASSWORD=changeme
python3 import_to_es.py data.ndjson
```
