# Anomaly Detection 配置指南

Anomaly Detection（异常检测）是 Elasticsearch 机器学习的实时流式分析功能，用于持续监控数据并发现异常模式。

## 什么是 Anomaly Detection？

Anomaly Detection 使用无监督机器学习算法，自动学习数据的正常行为模式，并识别偏离正常模式的异常点。

### 与 Data Frame Analytics 的区别

| 特性 | Anomaly Detection | Data Frame Analytics |
|------|-------------------|----------------------|
| 分析方式 | 实时流式分析 | 批量分析 |
| 数据处理 | 持续处理新数据 | 一次性处理全部数据 |
| 适用场景 | 实时监控、告警 | 数据探索、预测建模 |
| 学习方式 | 无监督学习 | 监督/无监督学习 |

## 配置方式

### 方式 1: Kibana UI（推荐初学者）

#### 步骤 1: 创建作业

1. 访问 Kibana: http://localhost:5601
2. 进入 **Machine Learning > Anomaly Detection**
3. 点击 **Create job**
4. 选择索引模式：`nginx-logs-*`

#### 步骤 2: 选择作业类型

Kibana 提供多种作业向导：

- **Single Metric**: 单指标异常检测
- **Multi Metric**: 多指标异常检测
- **Population**: 群体异常检测
- **Advanced**: 高级自定义配置

#### 步骤 3: 配置检测器

根据需求选择检测函数：

- `count`: 计数异常
- `mean`: 平均值异常
- `sum`: 总和异常
- `min/max`: 最小/最大值异常
- `rare`: 罕见值检测

#### 步骤 4: 设置参数

- **Bucket span**: 时间桶大小（如 15m）
- **Influencers**: 影响因素字段
- **Job ID**: 作业唯一标识

#### 步骤 5: 启动作业

1. 点击 **Create job**
2. 点击 **Start**
3. 等待作业运行并收集数据

### 方式 2: API（推荐自动化）

## 6 种常见异常检测作业

### 1. 请求速率异常检测

**用途**: 检测请求数量的异常变化（如 DDoS 攻击）

**Kibana UI 配置**:
1. 选择 **Single Metric**
2. Aggregation: `Count`
3. Bucket span: `15m`
4. Influencers: `remote_addr`, `request_method`

**API 配置**:
```bash
# 创建作业
curl -X PUT "localhost:9200/_ml/anomaly_detectors/nginx-request-rate" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测请求速率异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "count",
        "detector_description": "请求计数异常"
      }
    ],
    "influencers": ["remote_addr", "request_method"]
  },
  "data_description": {
    "time_field": "@timestamp"
  },
  "model_plot_config": {
    "enabled": true
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

### 2. 响应时间异常检测

**用途**: 检测响应时间的异常变化（性能问题）

**Kibana UI 配置**:
1. 选择 **Single Metric**
2. Aggregation: `Mean`
3. Field: `request_time`
4. Bucket span: `15m`
5. Influencers: `request_uri`, `request_method`

**API 配置**:
```bash
curl -X PUT "localhost:9200/_ml/anomaly_detectors/nginx-response-time" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测响应时间异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "mean",
        "field_name": "request_time",
        "detector_description": "平均响应时间异常"
      }
    ],
    "influencers": ["request_uri", "request_method"]
  },
  "data_description": {
    "time_field": "@timestamp"
  }
}'

curl -X PUT "localhost:9200/_ml/datafeeds/datafeed-nginx-response-time" \
-H 'Content-Type: application/json' -d'
{
  "job_id": "nginx-response-time",
  "indices": ["nginx-logs-*"]
}'

curl -X POST "localhost:9200/_ml/anomaly_detectors/nginx-response-time/_open"
curl -X POST "localhost:9200/_ml/datafeeds/datafeed-nginx-response-time/_start"
```

### 3. 错误率异常检测

**用途**: 检测 HTTP 错误状态码的异常增加

**Kibana UI 配置**:
1. 选择 **Single Metric**
2. Aggregation: `Count`
3. Query: `status >= 400`
4. Bucket span: `15m`
5. Influencers: `status`, `request_uri`

**API 配置**:
```bash
curl -X PUT "localhost:9200/_ml/anomaly_detectors/nginx-error-rate" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测错误率异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "count",
        "detector_description": "错误请求计数异常"
      }
    ],
    "influencers": ["status", "request_uri"]
  },
  "data_description": {
    "time_field": "@timestamp"
  }
}'

curl -X PUT "localhost:9200/_ml/datafeeds/datafeed-nginx-error-rate" \
-H 'Content-Type: application/json' -d'
{
  "job_id": "nginx-error-rate",
  "indices": ["nginx-logs-*"],
  "query": {
    "range": {
      "status": {
        "gte": 400
      }
    }
  }
}'

curl -X POST "localhost:9200/_ml/anomaly_detectors/nginx-error-rate/_open"
curl -X POST "localhost:9200/_ml/datafeeds/datafeed-nginx-error-rate/_start"
```

### 4. IP 行为异常检测

**用途**: 检测单个 IP 的异常行为（如扫描器、攻击者）

**Kibana UI 配置**:
1. 选择 **Multi Metric**
2. Split field: `remote_addr`
3. Aggregation: `Count`
4. Bucket span: `15m`

**API 配置**:
```bash
curl -X PUT "localhost:9200/_ml/anomaly_detectors/nginx-ip-behavior" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测 IP 行为异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "count",
        "partition_field_name": "remote_addr",
        "detector_description": "每个 IP 的请求计数异常"
      }
    ],
    "influencers": ["remote_addr", "request_uri"]
  },
  "data_description": {
    "time_field": "@timestamp"
  }
}'

curl -X PUT "localhost:9200/_ml/datafeeds/datafeed-nginx-ip-behavior" \
-H 'Content-Type: application/json' -d'
{
  "job_id": "nginx-ip-behavior",
  "indices": ["nginx-logs-*"]
}'

curl -X POST "localhost:9200/_ml/anomaly_detectors/nginx-ip-behavior/_open"
curl -X POST "localhost:9200/_ml/datafeeds/datafeed-nginx-ip-behavior/_start"
```

### 5. URL 访问模式异常检测

**用途**: 检测特定 URL 的访问模式异常

**Kibana UI 配置**:
1. 选择 **Population**
2. Population field: `request_uri`
3. Aggregation: `Count`
4. Bucket span: `15m`

**API 配置**:
```bash
curl -X PUT "localhost:9200/_ml/anomaly_detectors/nginx-url-pattern" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测 URL 访问模式异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "count",
        "over_field_name": "request_uri",
        "detector_description": "URL 访问模式异常"
      }
    ],
    "influencers": ["request_uri", "remote_addr"]
  },
  "data_description": {
    "time_field": "@timestamp"
  }
}'

curl -X PUT "localhost:9200/_ml/datafeeds/datafeed-nginx-url-pattern" \
-H 'Content-Type: application/json' -d'
{
  "job_id": "nginx-url-pattern",
  "indices": ["nginx-logs-*"]
}'

curl -X POST "localhost:9200/_ml/anomaly_detectors/nginx-url-pattern/_open"
curl -X POST "localhost:9200/_ml/datafeeds/datafeed-nginx-url-pattern/_start"
```

### 6. 综合异常评分

**用途**: 综合多个指标的异常检测

**Kibana UI 配置**:
1. 选择 **Advanced**
2. 添加多个检测器：
   - Count
   - Mean of request_time
   - Sum of body_bytes_sent
3. Bucket span: `15m`

**API 配置**:
```bash
curl -X PUT "localhost:9200/_ml/anomaly_detectors/nginx-综合" \
-H 'Content-Type: application/json' -d'
{
  "description": "综合异常评分",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "count",
        "detector_description": "请求计数"
      },
      {
        "function": "mean",
        "field_name": "request_time",
        "detector_description": "平均响应时间"
      },
      {
        "function": "sum",
        "field_name": "body_bytes_sent",
        "detector_description": "总字节数"
      }
    ],
    "influencers": ["remote_addr", "request_uri", "status"]
  },
  "data_description": {
    "time_field": "@timestamp"
  }
}'

curl -X PUT "localhost:9200/_ml/datafeeds/datafeed-nginx-综合" \
-H 'Content-Type: application/json' -d'
{
  "job_id": "nginx-综合",
  "indices": ["nginx-logs-*"]
}'

curl -X POST "localhost:9200/_ml/anomaly_detectors/nginx-综合/_open"
curl -X POST "localhost:9200/_ml/datafeeds/datafeed-nginx-综合/_start"
```

## 关键参数说明

### bucket_span
时间桶大小，决定分析的时间粒度

```json
"bucket_span": "15m"
```

**选择建议**:
- 高频数据（每秒多条）: `5m` - `15m`
- 中频数据（每分钟几条）: `15m` - `1h`
- 低频数据（每小时几条）: `1h` - `1d`

**影响**:
- 太小：噪音多，误报率高
- 太大：延迟高，可能错过短期异常

### influencers
影响因素字段，帮助理解异常原因

```json
"influencers": ["remote_addr", "request_method"]
```

**选择建议**:
- 选择与异常相关的分类字段
- 避免高基数字段（如唯一 ID）
- 通常 2-5 个字段

### detectors
检测器配置，定义检测的指标和方法

```json
"detectors": [
  {
    "function": "count",
    "partition_field_name": "remote_addr"
  }
]
```

**常用函数**:
- `count`: 计数
- `mean`: 平均值
- `sum`: 总和
- `min/max`: 最小/最大值
- `rare`: 罕见值
- `freq_rare`: 频繁/罕见值

**字段类型**:
- `partition_field_name`: 分区字段（为每个值单独建模）
- `by_field_name`: 分组字段（在组内检测异常）
- `over_field_name`: 群体字段（检测群体中的异常个体）

## 查看结果

### Kibana UI

1. 进入 **Machine Learning > Anomaly Explorer**
2. 选择作业
3. 查看异常时间线
4. 点击异常点查看详情

### API 查询

```bash
# 查询异常结果
curl -X GET "localhost:9200/_ml/anomaly_detectors/nginx-request-rate/results/records" \
-H 'Content-Type: application/json' -d'
{
  "sort": "record_score",
  "desc": true,
  "size": 10
}'

# 查询作业统计
curl -X GET "localhost:9200/_ml/anomaly_detectors/nginx-request-rate/_stats"
```

## 参数调优建议

### 1. 初始配置
- 使用默认 `bucket_span`（15m）
- 选择 2-3 个相关 influencers
- 从简单的单指标开始

### 2. 根据结果调整
- **误报多**: 增大 `bucket_span`
- **漏报多**: 减小 `bucket_span`
- **异常不明确**: 增加 influencers

### 3. 性能优化
- 限制 influencers 数量（< 5）
- 使用 datafeed query 过滤数据
- 避免高基数字段

## 故障排查

### 问题 1: 作业无数据

**症状**: 作业运行但没有结果

**诊断**:
```bash
# 检查 datafeed 状态
curl -X GET "localhost:9200/_ml/datafeeds/datafeed-nginx-request-rate/_stats"

# 检查索引数据
curl -X GET "localhost:9200/nginx-logs-*/_count"
```

**解决**:
- 确认索引有数据
- 检查 datafeed query 是否正确
- 确认时间字段格式正确

### 问题 2: 异常分数都很低

**症状**: 所有异常分数 < 25

**解决**:
- 等待更长时间（至少 2-3 个 bucket_span）
- 检查数据是否真的有异常
- 调整检测器配置

### 问题 3: 误报率高

**症状**: 很多正常情况被标记为异常

**解决**:
- 增大 `bucket_span`
- 减少 influencers
- 检查数据质量

### 问题 4: 作业失败

**症状**: 作业状态为 failed

**诊断**:
```bash
curl -X GET "localhost:9200/_ml/anomaly_detectors/nginx-request-rate/_stats?verbose=true"
```

**常见原因**:
- 内存不足
- 字段类型错误
- 数据格式问题

## 管理作业

### 停止作业
```bash
# 停止 datafeed
curl -X POST "localhost:9200/_ml/datafeeds/datafeed-nginx-request-rate/_stop"

# 关闭作业
curl -X POST "localhost:9200/_ml/anomaly_detectors/nginx-request-rate/_close"
```

### 删除作业
```bash
# 删除 datafeed
curl -X DELETE "localhost:9200/_ml/datafeeds/datafeed-nginx-request-rate"

# 删除作业
curl -X DELETE "localhost:9200/_ml/anomaly_detectors/nginx-request-rate"
```

### 查看所有作业
```bash
curl -X GET "localhost:9200/_ml/anomaly_detectors/_stats"
```

## 下一步

- [Data Frame Analytics 概述](data-frame-analytics/overview.md)
- [快速开始指南](quick-start.md)
- [故障排查](troubleshooting.md)
