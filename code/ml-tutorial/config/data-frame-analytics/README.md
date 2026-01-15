# Data Frame Analytics 配置说明

本目录包含 3 种 Data Frame Analytics 作业配置。

## 配置文件

### 1. outlier-detection.json - 离群点检测

**用途**: 发现 Nginx 日志中的异常请求模式

**分析字段**:
- `status`: HTTP 状态码
- `body_bytes_sent`: 响应字节数
- `request_time`: 响应时间

**应用场景**:
- 性能异常检测（响应时间、字节数异常）
- 安全威胁检测（异常请求模式）
- 流量模式异常

**API 调用示例**:
```bash
# 创建离群点检测作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-outlier-detection" \
-H 'Content-Type: application/json' \
-d @outlier-detection.json

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-outlier-detection/_start"

# 查看进度
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-outlier-detection/_stats"

# 查看结果
curl -X GET "localhost:9200/nginx-outliers/_search?pretty"
```

### 2. classification.json - 威胁分类

**用途**: 预测请求的威胁类型

**目标变量**: `threat_type`

**特征字段**:
- `status`: HTTP 状态码
- `body_bytes_sent`: 响应字节数
- `request_time`: 响应时间
- `request_method`: 请求方法

**应用场景**:
- 威胁类型自动分类
- 攻击模式识别
- 安全事件分类

**API 调用示例**:
```bash
# 创建分类作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-threat-classification" \
-H 'Content-Type: application/json' \
-d @classification.json

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-threat-classification/_start"

# 查看进度
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-threat-classification/_stats"

# 查看结果
curl -X GET "localhost:9200/nginx-threat-classification/_search?pretty"
```

### 3. regression.json - 响应时间预测

**用途**: 预测请求的响应时间

**目标变量**: `request_time`

**特征字段**:
- `status`: HTTP 状态码
- `body_bytes_sent`: 响应字节数
- `request_method`: 请求方法
- `threat_type`: 威胁类型

**应用场景**:
- 性能预测
- 容量规划
- SLA 监控

**API 调用示例**:
```bash
# 创建回归作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-response-time-prediction" \
-H 'Content-Type: application/json' \
-d @regression.json

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-response-time-prediction/_start"

# 查看进度
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-response-time-prediction/_stats"

# 查看结果
curl -X GET "localhost:9200/nginx-response-time-prediction/_search?pretty"
```

## 通用操作

### 停止作业
```bash
curl -X POST "localhost:9200/_ml/data_frame/analytics/<job_id>/_stop"
```

### 删除作业
```bash
curl -X DELETE "localhost:9200/_ml/data_frame/analytics/<job_id>"
```

### 查看所有作业
```bash
curl -X GET "localhost:9200/_ml/data_frame/analytics/_stats"
```

## 参数说明

### 离群点检测参数
- `outlier_fraction`: 预期离群点比例（默认 0.05 = 5%）
- `standardization_enabled`: 是否标准化特征（推荐 true）
- `compute_feature_influence`: 是否计算特征影响力（推荐 true）

### 分类参数
- `dependent_variable`: 目标分类变量
- `training_percent`: 训练集比例（默认 80%）
- `num_top_classes`: 返回前 N 个预测类别（默认 2）

### 回归参数
- `dependent_variable`: 目标连续变量
- `training_percent`: 训练集比例（默认 80%）
- `prediction_field_name`: 预测结果字段名

## 注意事项

1. **数据量要求**: 建议至少 1000 条记录
2. **内存限制**: 根据数据量调整 `model_memory_limit`
3. **训练时间**: 取决于数据量和字段数量，通常 1-10 分钟
4. **结果索引**: 会自动创建目标索引存储结果

## 故障排查

### 作业失败
```bash
# 查看详细错误信息
curl -X GET "localhost:9200/_ml/data_frame/analytics/<job_id>/_stats?verbose=true"
```

### 内存不足
- 增加 `model_memory_limit`
- 减少 `analyzed_fields`
- 减少源数据量

### 训练时间过长
- 减少数据量（使用 query 过滤）
- 减少特征字段
- 增加 `max_num_threads`
