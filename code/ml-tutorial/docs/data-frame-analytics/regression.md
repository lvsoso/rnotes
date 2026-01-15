# 回归指南

回归用于预测连续数值，例如预测请求的响应时间。

## 工作原理

回归使用监督学习算法，从历史数据中学习特征与数值的关系，然后预测新数据的数值。

### 算法

Elasticsearch 使用 **Boosted Tree** 算法：
1. 从训练数据中学习特征与数值的关系
2. 构建决策树集成模型
3. 对新数据进行数值预测
4. 输出预测值和特征重要性

## 应用场景

### 1. 性能预测
根据请求特征预测响应时间，用于性能优化。

### 2. 容量规划
预测资源使用情况，帮助容量规划。

### 3. SLA 监控
预测服务响应时间，确保满足 SLA 要求。

## 配置步骤

### 方式 1: Kibana UI

1. 进入 **Machine Learning > Data Frame Analytics**
2. 点击 **Create job**
3. 选择源索引：`nginx-logs-*`
4. 选择作业类型：**Regression**
5. 选择目标变量：`request_time`
6. 选择特征字段：
   - `status`
   - `body_bytes_sent`
   - `request_method`
   - `threat_type`
7. 设置目标索引：`nginx-response-time-prediction`
8. 点击 **Create**
9. 点击 **Start**

### 方式 2: API

```bash
# 创建回归作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-response-time-prediction" \
-H 'Content-Type: application/json' -d'
{
  "description": "预测 Nginx 请求的响应时间",
  "source": {
    "index": ["nginx-logs-*"],
    "query": {
      "match_all": {}
    }
  },
  "dest": {
    "index": "nginx-response-time-prediction",
    "results_field": "ml"
  },
  "analysis": {
    "regression": {
      "dependent_variable": "request_time",
      "training_percent": 80,
      "prediction_field_name": "predicted_request_time"
    }
  },
  "analyzed_fields": {
    "includes": [
      "status",
      "body_bytes_sent",
      "request_method",
      "threat_type"
    ]
  },
  "model_memory_limit": "200mb"
}'

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-response-time-prediction/_start"

# 查看进度
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-response-time-prediction/_stats?pretty"
```

## 参数说明

### dependent_variable
目标数值变量（必需）

```json
"dependent_variable": "request_time"
```

- 必须是数值字段（integer, long, float, double）
- 建议值域不要过大（可以先标准化）

### training_percent
训练集比例（默认 80）

```json
"training_percent": 80
```

- 80: 80% 用于训练，20% 用于测试
- 建议：70-90
- 数据量大时可以降低

### prediction_field_name
预测结果字段名（可选）

```json
"prediction_field_name": "predicted_request_time"
```

- 默认：`<dependent_variable>_prediction`
- 自定义字段名便于识别

### loss_function
损失函数（可选）

```json
"loss_function": "mse"
```

- `mse`: 均方误差（默认）
- `msle`: 均方对数误差（适合目标值范围大）
- `huber`: Huber 损失（对异常值鲁棒）

### loss_function_parameter
损失函数参数（可选）

```json
"loss_function_parameter": 1.0
```

- 仅用于 `huber` 损失函数
- 控制对异常值的敏感度

## 查看结果

### 查询预测结果

```bash
# 查询所有预测结果
curl -X GET "localhost:9200/nginx-response-time-prediction/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  },
  "size": 10
}'
```

### 结果字段说明

```json
{
  "@timestamp": "2025-12-11T10:30:45.123Z",
  "status": 200,
  "body_bytes_sent": 1024,
  "request_method": "GET",
  "threat_type": "none",
  "request_time": 0.123,
  "ml": {
    "predicted_request_time": 0.125,
    "prediction_score": 0.125,
    "is_training": false,
    "feature_importance": [
      {
        "feature_name": "body_bytes_sent",
        "importance": 0.4
      },
      {
        "feature_name": "threat_type",
        "importance": 0.3
      },
      {
        "feature_name": "status",
        "importance": 0.2
      },
      {
        "feature_name": "request_method",
        "importance": 0.1
      }
    ]
  }
}
```

- `predicted_request_time`: 预测的响应时间
- `prediction_score`: 预测分数（与预测值相同）
- `is_training`: 是否为训练数据
- `feature_importance`: 特征重要性

### 评估模型性能

```bash
# 查看模型统计信息
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-response-time-prediction/_stats?pretty"
```

关键指标：
- `regression.mse`: 均方误差（越小越好）
- `regression.r_squared`: R² 分数（0-1，越接近 1 越好）
- `regression.huber`: Huber 损失（如果使用）

### 计算预测误差

```bash
# 查询预测误差较大的记录
curl -X GET "localhost:9200/nginx-response-time-prediction/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "must": [
        {
          "exists": {
            "field": "ml.predicted_request_time"
          }
        }
      ]
    }
  },
  "script_fields": {
    "prediction_error": {
      "script": {
        "source": "Math.abs(doc['\''request_time'\''].value - doc['\''ml.predicted_request_time'\''].value)"
      }
    }
  },
  "sort": [
    {
      "_script": {
        "type": "number",
        "script": {
          "source": "Math.abs(doc['\''request_time'\''].value - doc['\''ml.predicted_request_time'\''].value)"
        },
        "order": "desc"
      }
    }
  ],
  "size": 10
}'
```

## 实际案例

### 案例 1: 响应时间预测

**场景**: 根据请求特征预测响应时间

**配置**:
```json
{
  "dependent_variable": "request_time",
  "analyzed_fields": {
    "includes": ["status", "body_bytes_sent", "request_method", "threat_type"]
  },
  "training_percent": 80
}
```

**结果**:
- R² 分数：0.85
- 能够较准确预测响应时间
- 发现 `body_bytes_sent` 是最重要的特征

### 案例 2: 字节数预测

**场景**: 预测响应字节数

**配置**:
```json
{
  "dependent_variable": "body_bytes_sent",
  "analyzed_fields": {
    "includes": ["status", "request_method", "threat_type"]
  },
  "training_percent": 75,
  "loss_function": "msle"
}
```

**结果**:
- R² 分数：0.78
- 使用 MSLE 处理字节数范围大的问题

## 最佳实践

### 1. 数据准备
- 确保目标变量是连续数值
- 处理异常值和缺失值
- 特征与目标要有相关性

### 2. 特征选择
- 选择与预测目标相关的特征
- 数值型和分类型特征都可以使用
- 避免泄露信息的特征

### 3. 参数调优
- 从默认参数开始
- 根据 R² 分数调整特征
- 目标值范围大时使用 `msle`
- 有异常值时使用 `huber`

### 4. 模型评估
- 查看 R² 分数（> 0.7 通常认为不错）
- 检查预测误差分布
- 分析特征重要性

## 故障排查

### 问题 1: R² 分数低

**症状**: R² < 0.5

**解决**:
- 增加更多相关特征
- 检查数据质量
- 检查特征与目标的相关性
- 尝试特征工程（组合特征）

### 问题 2: 预测值范围不合理

**症状**: 预测值超出合理范围

**解决**:
- 检查训练数据是否有异常值
- 使用 `huber` 损失函数
- 对目标变量进行标准化

### 问题 3: 过拟合

**症状**: 训练误差低，测试误差高

**解决**:
- 增加训练数据
- 减少特征数量
- 降低 `training_percent`

### 问题 4: 预测误差不均匀

**症状**: 某些范围预测准确，某些范围误差大

**解决**:
- 检查训练数据分布
- 增加误差大范围的样本
- 使用 `msle` 平衡不同范围

## 使用预测模型

训练完成后，可以使用模型对新数据进行预测：

```bash
# 使用推理 API 进行预测
curl -X POST "localhost:9200/_ml/trained_models/nginx-response-time-prediction/_infer" \
-H 'Content-Type: application/json' -d'
{
  "docs": [
    {
      "status": 200,
      "body_bytes_sent": 5000,
      "request_method": "GET",
      "threat_type": "none"
    }
  ]
}'
```

## 性能优化建议

基于预测结果优化性能：

1. **识别慢请求模式**
   - 查找预测响应时间高的请求特征
   - 优化这些请求的处理逻辑

2. **容量规划**
   - 根据预测的响应时间分布
   - 规划服务器资源

3. **SLA 监控**
   - 设置响应时间阈值告警
   - 预测是否会违反 SLA

## 下一步

- [分类指南](classification.md)
- [离群点检测指南](outlier-detection.md)
- [配置文件参考](config/data-frame-analytics/README.md)
