# 分类指南

分类用于预测离散类别，例如预测请求的威胁类型。

## 工作原理

分类使用监督学习算法，从已标记的数据中学习，然后预测新数据的类别。

### 算法

Elasticsearch 使用 **Boosted Tree** 算法：
1. 从训练数据中学习特征与类别的关系
2. 构建决策树集成模型
3. 对新数据进行类别预测
4. 输出预测类别和概率

## 应用场景

### 1. 威胁类型分类
根据请求特征自动分类威胁类型（SQL 注入、XSS、扫描器等）。

### 2. 攻击模式识别
识别不同的攻击模式和行为。

### 3. 安全事件分类
自动分类安全事件的严重程度。

## 配置步骤

### 方式 1: Kibana UI

1. 进入 **Machine Learning > Data Frame Analytics**
2. 点击 **Create job**
3. 选择源索引：`nginx-logs-*`
4. 选择作业类型：**Classification**
5. 选择目标变量：`threat_type`
6. 选择特征字段：
   - `status`
   - `body_bytes_sent`
   - `request_time`
   - `request_method`
7. 设置目标索引：`nginx-threat-classification`
8. 点击 **Create**
9. 点击 **Start**

### 方式 2: API

```bash
# 创建分类作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-threat-classification" \
-H 'Content-Type: application/json' -d'
{
  "description": "预测 Nginx 请求的威胁类型",
  "source": {
    "index": ["nginx-logs-*"],
    "query": {
      "match_all": {}
    }
  },
  "dest": {
    "index": "nginx-threat-classification",
    "results_field": "ml"
  },
  "analysis": {
    "classification": {
      "dependent_variable": "threat_type",
      "training_percent": 80,
      "num_top_classes": 3,
      "prediction_field_name": "predicted_threat_type"
    }
  },
  "analyzed_fields": {
    "includes": [
      "status",
      "body_bytes_sent",
      "request_time",
      "request_method"
    ]
  },
  "model_memory_limit": "200mb"
}'

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-threat-classification/_start"

# 查看进度
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-threat-classification/_stats?pretty"
```

## 参数说明

### dependent_variable
目标分类变量（必需）

```json
"dependent_variable": "threat_type"
```

- 必须是分类字段（keyword 类型）
- 建议类别数 2-100
- 类别分布不要过于不平衡

### training_percent
训练集比例（默认 80）

```json
"training_percent": 80
```

- 80: 80% 用于训练，20% 用于测试
- 建议：70-90
- 数据量大时可以降低

### num_top_classes
返回前 N 个预测类别（默认 2）

```json
"num_top_classes": 3
```

- 返回概率最高的 N 个类别
- 建议：2-5
- 用于查看备选预测

### prediction_field_name
预测结果字段名（可选）

```json
"prediction_field_name": "predicted_threat_type"
```

- 默认：`<dependent_variable>_prediction`
- 自定义字段名便于识别

### class_assignment_objective
分类目标（可选）

```json
"class_assignment_objective": "maximize_accuracy"
```

- `maximize_accuracy`: 最大化准确率（默认）
- `maximize_minimum_recall`: 最大化最小召回率（平衡类别）

## 查看结果

### 查询预测结果

```bash
# 查询所有预测结果
curl -X GET "localhost:9200/nginx-threat-classification/_search?pretty" -H 'Content-Type: application/json' -d'
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
  "status": 403,
  "body_bytes_sent": 1024,
  "request_time": 0.5,
  "request_method": "GET",
  "threat_type": "sql_injection",
  "ml": {
    "predicted_threat_type": "sql_injection",
    "prediction_probability": 0.95,
    "prediction_score": 0.95,
    "top_classes": [
      {
        "class_name": "sql_injection",
        "class_probability": 0.95,
        "class_score": 0.95
      },
      {
        "class_name": "xss",
        "class_probability": 0.03,
        "class_score": 0.03
      },
      {
        "class_name": "none",
        "class_probability": 0.02,
        "class_score": 0.02
      }
    ],
    "is_training": false,
    "feature_importance": [
      {
        "feature_name": "status",
        "importance": 0.4
      },
      {
        "feature_name": "request_time",
        "importance": 0.3
      },
      {
        "feature_name": "body_bytes_sent",
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

- `predicted_threat_type`: 预测的类别
- `prediction_probability`: 预测概率（0-1）
- `top_classes`: 前 N 个预测类别及其概率
- `is_training`: 是否为训练数据
- `feature_importance`: 特征重要性

### 评估模型性能

```bash
# 查看模型统计信息
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-threat-classification/_stats?pretty"
```

关键指标：
- `classification.accuracy`: 准确率
- `classification.multiclass_confusion_matrix`: 混淆矩阵
- `classification.recall`: 召回率
- `classification.precision`: 精确率

## 实际案例

### 案例 1: 威胁类型分类

**场景**: 自动分类请求的威胁类型

**配置**:
```json
{
  "dependent_variable": "threat_type",
  "analyzed_fields": {
    "includes": ["status", "body_bytes_sent", "request_time", "request_method"]
  },
  "training_percent": 80
}
```

**结果**: 
- 准确率：92%
- 能够准确识别 SQL 注入、XSS、扫描器等威胁

### 案例 2: 攻击严重程度分类

**场景**: 分类攻击的严重程度（low, medium, high, critical）

**配置**:
```json
{
  "dependent_variable": "risk_level",
  "analyzed_fields": {
    "includes": ["threat_type", "status", "request_time"]
  },
  "training_percent": 75
}
```

**结果**:
- 准确率：88%
- 能够根据威胁类型和请求特征预测风险等级

## 最佳实践

### 1. 数据准备
- 确保目标变量有足够的样本（每个类别 > 100）
- 类别分布不要过于不平衡（最大类/最小类 < 10:1）
- 特征与目标要有相关性

### 2. 特征选择
- 选择与分类目标相关的特征
- 避免泄露信息的特征（如包含答案的字段）
- 数值型和分类型特征都可以使用

### 3. 参数调优
- 从默认参数开始
- 根据准确率调整 `training_percent`
- 使用 `class_assignment_objective` 平衡类别

### 4. 模型评估
- 查看混淆矩阵识别误分类模式
- 检查特征重要性确认特征选择
- 在测试集上验证性能

## 故障排查

### 问题 1: 准确率低

**症状**: 模型准确率 < 70%

**解决**:
- 增加更多相关特征
- 检查数据质量（缺失值、异常值）
- 增加训练数据量
- 检查类别是否可分（特征是否足够）

### 问题 2: 类别不平衡

**症状**: 某些类别预测很差

**解决**:
```json
"class_assignment_objective": "maximize_minimum_recall"
```
- 使用平衡目标
- 增加少数类别的样本
- 使用过采样/欠采样

### 问题 3: 过拟合

**症状**: 训练准确率高，测试准确率低

**解决**:
- 增加训练数据
- 减少特征数量
- 降低 `training_percent`（增加测试集）

### 问题 4: 内存不足

**症状**: 作业失败，提示内存不足

**解决**:
```json
"model_memory_limit": "500mb"
```
- 增加内存限制
- 减少特征数量
- 减少训练数据量

## 使用预测模型

训练完成后，可以使用模型对新数据进行预测：

```bash
# 使用推理 API 进行预测
curl -X POST "localhost:9200/_ml/trained_models/nginx-threat-classification/_infer" \
-H 'Content-Type: application/json' -d'
{
  "docs": [
    {
      "status": 403,
      "body_bytes_sent": 1024,
      "request_time": 0.5,
      "request_method": "GET"
    }
  ]
}'
```

## 下一步

- [回归指南](regression.md)
- [离群点检测指南](outlier-detection.md)
- [配置文件参考](config/data-frame-analytics/README.md)
