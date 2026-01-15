# 快速开始指南

30分钟完成从数据生成到 ML 结果查看的全流程。

## 步骤 1: 环境准备 (5分钟)

```bash
# 启动 Elasticsearch 和 Kibana
docker-compose up -d

# 等待服务启动
sleep 30

# 验证
curl http://localhost:9200
curl http://localhost:5601/api/status
```

## 步骤 2: 生成数据 (5分钟)

```bash
cd ml-tutorial/scripts

# 安装依赖
pip install -r requirements.txt

# 生成 10000 条日志，跨度 7 天
python3 generate_logs.py -n 10000 -o data --days 7

# 验证
ls -lh data/nginx-logs.ndjson
wc -l data/nginx-logs.ndjson
```

预期输出：10000 行 NDJSON 数据

## 步骤 3: 导入数据 (5分钟)

```bash
# 导入到 Elasticsearch
python3 import_to_es.py data/nginx-logs.ndjson

# 验证
curl http://localhost:9200/nginx-logs-*/_count
```

预期输出：`{"count":10000,...}`

## 步骤 4: 创建 ML 作业 (10分钟)

### 方式 1: Kibana UI

1. 访问 http://localhost:5601
2. 进入 Machine Learning > Anomaly Detection
3. 点击 "Create job"
4. 选择索引模式：`nginx-logs-*`
5. 选择作业类型：Single Metric
6. 配置检测器：
   - Function: `count`
   - Bucket span: `15m`
7. 启动作业

### 方式 2: API

```bash
# 创建请求速率异常检测作业
curl -X PUT "localhost:9200/_ml/anomaly_detectors/nginx-request-rate" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测请求速率异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [{"function": "count"}]
  },
  "data_description": {
    "time_field": "@timestamp"
  }
}'

# 创建数据源
curl -X PUT "localhost:9200/_ml/datafeeds/datafeed-nginx-request-rate" \
-H 'Content-Type: application/json' -d'
{
  "job_id": "nginx-request-rate",
  "indices": ["nginx-logs-*"]
}'

# 启动作业
curl -X POST "localhost:9200/_ml/anomaly_detectors/nginx-request-rate/_open"
curl -X POST "localhost:9200/_ml/datafeeds/datafeed-nginx-request-rate/_start"
```

## 步骤 5: 查看结果 (5分钟)

1. 进入 Machine Learning > Anomaly Explorer
2. 选择作业：`nginx-request-rate`
3. 查看异常时间线和异常分数
4. 点击异常点查看详情

## 常见问题

**Q: Elasticsearch 连接失败？**
```bash
# 检查服务状态
docker ps
# 查看日志
docker logs <container_id>
```

**Q: 导入数据失败？**
```bash
# 检查认证
python3 import_to_es.py data.ndjson -u elastic -p changeme
```

**Q: ML 作业无数据？**
```bash
# 检查索引
curl http://localhost:9200/_cat/indices/nginx-logs-*
# 检查数据源状态
curl http://localhost:9200/_ml/datafeeds/datafeed-nginx-request-rate/_stats
```

## 下一步

- [Anomaly Detection 配置指南](anomaly-detection-setup.md)
- [Data Frame Analytics 教程](data-frame-analytics/)
- [ML 概念说明](ml-concepts.md)
