# Data Frame Analytics 概述

Data Frame Analytics (DFA) 是 Elasticsearch 机器学习的高级功能，用于对整个数据集进行分析和预测。

## 什么是 Data Frame Analytics？

DFA 对数据进行批量分析，创建训练模型，并将结果存储到新的索引中。与 Anomaly Detection（实时流式分析）不同，DFA 是批处理分析。

## 三种分析类型

### 1. 离群点检测 (Outlier Detection)

**目的**: 发现数据中的异常点

**工作原理**: 
- 使用无监督学习算法
- 计算每个数据点与其他点的距离
- 标记距离较远的点为离群点

**应用场景**:
- 性能异常检测（响应时间、字节数异常）
- 安全威胁检测（异常请求模式）
- 流量模式异常

**示例**: 发现响应时间异常长或字节数异常大的请求

### 2. 分类 (Classification)

**目的**: 预测离散类别

**工作原理**:
- 使用监督学习算法
- 从已标记的数据中学习
- 预测新数据的类别

**应用场景**:
- 威胁类型自动分类
- 攻击模式识别
- 安全事件分类

**示例**: 根据请求特征预测是否为 SQL 注入、XSS 等攻击类型

### 3. 回归 (Regression)

**目的**: 预测连续数值

**工作原理**:
- 使用监督学习算法
- 从历史数据中学习数值关系
- 预测新数据的数值

**应用场景**:
- 性能预测
- 容量规划
- SLA 监控

**示例**: 根据请求特征预测响应时间

## Anomaly Detection vs Data Frame Analytics

| 特性 | Anomaly Detection | Data Frame Analytics |
|------|-------------------|----------------------|
| 分析方式 | 实时流式分析 | 批量分析 |
| 数据处理 | 持续处理新数据 | 一次性处理全部数据 |
| 结果存储 | 存储在 ML 结果索引 | 存储在指定的目标索引 |
| 适用场景 | 实时监控、告警 | 数据探索、预测建模 |
| 学习方式 | 无监督学习 | 监督/无监督学习 |

## 工作流程

```
1. 准备数据
   ↓
2. 创建 DFA 作业
   ↓
3. 配置分析类型和参数
   ↓
4. 启动作业（训练模型）
   ↓
5. 查看结果（新索引）
   ↓
6. 使用模型进行预测
```

## 快速开始

### 1. 离群点检测示例

```bash
# 创建作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-outliers" \
-H 'Content-Type: application/json' -d'
{
  "source": {
    "index": ["nginx-logs-*"]
  },
  "dest": {
    "index": "nginx-outliers"
  },
  "analysis": {
    "outlier_detection": {}
  },
  "analyzed_fields": {
    "includes": ["status", "body_bytes_sent", "request_time"]
  }
}'

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-outliers/_start"

# 查看结果
curl -X GET "localhost:9200/nginx-outliers/_search?pretty"
```

### 2. 分类示例

```bash
# 创建作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-classification" \
-H 'Content-Type: application/json' -d'
{
  "source": {
    "index": ["nginx-logs-*"]
  },
  "dest": {
    "index": "nginx-classification"
  },
  "analysis": {
    "classification": {
      "dependent_variable": "threat_type"
    }
  },
  "analyzed_fields": {
    "includes": ["status", "body_bytes_sent", "request_time", "request_method"]
  }
}'

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-classification/_start"
```

### 3. 回归示例

```bash
# 创建作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-regression" \
-H 'Content-Type: application/json' -d'
{
  "source": {
    "index": ["nginx-logs-*"]
  },
  "dest": {
    "index": "nginx-regression"
  },
  "analysis": {
    "regression": {
      "dependent_variable": "request_time"
    }
  },
  "analyzed_fields": {
    "includes": ["status", "body_bytes_sent", "request_method", "threat_type"]
  }
}'

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-regression/_start"
```

## 关键概念

### Source Index (源索引)
包含原始数据的索引，用于训练模型。

### Destination Index (目标索引)
存储分析结果的新索引，包含原始数据和预测结果。

### Analyzed Fields (分析字段)
用于训练模型的字段，应选择与目标相关的特征。

### Dependent Variable (目标变量)
- 分类：要预测的类别字段
- 回归：要预测的数值字段
- 离群点检测：不需要

### Training Percent (训练比例)
用于训练的数据比例，剩余数据用于测试（默认 80%）。

## 最佳实践

1. **数据准备**
   - 确保数据质量（无缺失值、异常值）
   - 选择相关特征字段
   - 数据量建议 > 1000 条

2. **特征选择**
   - 选择与目标相关的字段
   - 避免包含 ID、时间戳等无关字段
   - 数值字段效果通常更好

3. **参数调优**
   - 从默认参数开始
   - 根据结果逐步调整
   - 注意内存限制

4. **结果验证**
   - 检查训练/测试准确率
   - 查看特征重要性
   - 验证预测结果合理性

## 下一步

- [离群点检测详细指南](outlier-detection.md)
- [分类详细指南](classification.md)
- [回归详细指南](regression.md)
- [配置文件参考](../../config/data-frame-analytics/README.md)

## 参考资源

- [Elasticsearch ML 官方文档](https://www.elastic.co/guide/en/machine-learning/current/ml-dfanalytics.html)
- [Data Frame Analytics API](https://www.elastic.co/guide/en/elasticsearch/reference/current/ml-df-analytics-apis.html)
