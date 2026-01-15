#!/bin/bash
# Kibana ML API 示例

ES_HOST="http://localhost:9200"

# ============================================
# Anomaly Detection 示例
# ============================================

# 1. 创建请求速率异常检测作业
curl -X PUT "${ES_HOST}/_ml/anomaly_detectors/nginx-request-rate" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测请求速率异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [{"function": "count"}],
    "influencers": ["remote_addr"]
  },
  "data_description": {"time_field": "@timestamp"}
}'

# 2. 创建响应时间异常检测作业
curl -X PUT "${ES_HOST}/_ml/anomaly_detectors/nginx-response-time" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测响应时间异常",
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [{
      "function": "mean",
      "field_name": "request_time"
    }]
  },
  "data_description": {"time_field": "@timestamp"}
}'

# 3. 创建数据源
curl -X PUT "${ES_HOST}/_ml/datafeeds/datafeed-nginx-request-rate" \
-H 'Content-Type: application/json' -d'
{
  "job_id": "nginx-request-rate",
  "indices": ["nginx-logs-*"]
}'

# 4. 启动作业
curl -X POST "${ES_HOST}/_ml/anomaly_detectors/nginx-request-rate/_open"
curl -X POST "${ES_HOST}/_ml/datafeeds/datafeed-nginx-request-rate/_start"

# 5. 查询作业状态
curl -X GET "${ES_HOST}/_ml/anomaly_detectors/nginx-request-rate/_stats"

# 6. 查询异常结果
curl -X GET "${ES_HOST}/_ml/anomaly_detectors/nginx-request-rate/results/records"

# 7. 停止作业
curl -X POST "${ES_HOST}/_ml/datafeeds/datafeed-nginx-request-rate/_stop"
curl -X POST "${ES_HOST}/_ml/anomaly_detectors/nginx-request-rate/_close"

# ============================================
# Data Frame Analytics 示例
# ============================================

# 1. 创建离群点检测作业
curl -X PUT "${ES_HOST}/_ml/data_frame/analytics/nginx-outliers" \
-H 'Content-Type: application/json' -d'
{
  "source": {"index": "nginx-logs-*"},
  "dest": {"index": "nginx-outliers"},
  "analysis": {
    "outlier_detection": {
      "n_neighbors": 30,
      "method": "distance_knn"
    }
  },
  "analyzed_fields": {
    "includes": ["status", "body_bytes_sent", "request_time"]
  }
}'

# 2. 启动分析
curl -X POST "${ES_HOST}/_ml/data_frame/analytics/nginx-outliers/_start"

# 3. 查询状态
curl -X GET "${ES_HOST}/_ml/data_frame/analytics/nginx-outliers/_stats"

# 4. 查询结果
curl -X GET "${ES_HOST}/nginx-outliers/_search?size=10&sort=ml.outlier_score:desc"
