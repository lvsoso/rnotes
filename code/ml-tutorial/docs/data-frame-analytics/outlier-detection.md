# 离群点检测指南

离群点检测用于发现数据中的异常点，无需预先标记数据。

## 工作原理

离群点检测使用无监督学习算法，计算每个数据点与其他点的距离，标记距离较远的点为离群点。

### 算法

Elasticsearch 使用 **distance-based k-nearest neighbors (kNN)** 算法：
1. 计算每个点到其 k 个最近邻居的距离
2. 距离较大的点被标记为离群点
3. 输出离群点分数（0-1，越接近 1 越异常）

## 应用场景

### 1. 性能异常检测
发现响应时间异常长或字节数异常大的请求。

### 2. 安全威胁检测
发现异常的请求模式，可能是攻击行为。

### 3. 流量模式异常
发现与正常流量模式不同的请求。

## 配置步骤

### 方式 1: Kibana UI

1. 进入 **Machine Learning > Data Frame Analytics**
2. 点击 **Create job**
3. 选择源索引：`nginx-logs-*`
4. 选择作业类型：**Outlier detection**
5. 选择分析字段：
   - `status`
   - `body_bytes_sent`
   - `request_time`
6. 设置目标索引：`nginx-outliers`
7. 点击 **Create**
8. 点击 **Start**

### 方式 2: API

```bash
# 创建离群点检测作业
curl -X PUT "localhost:9200/_ml/data_frame/analytics/nginx-outlier-detection" \
-H 'Content-Type: application/json' -d'
{
  "description": "检测 Nginx 日志中的异常请求",
  "source": {
    "index": ["nginx-logs-*"],
    "query": {
      "match_all": {}
    }
  },
  "dest": {
    "index": "nginx-outliers",
    "results_field": "ml"
  },
  "analysis": {
    "outlier_detection": {
      "compute_feature_influence": true,
      "outlier_fraction": 0.05,
      "standardization_enabled": true
    }
  },
  "analyzed_fields": {
    "includes": [
      "status",
      "body_bytes_sent",
      "request_time"
    ]
  },
  "model_memory_limit": "100mb"
}'

# 启动作业
curl -X POST "localhost:9200/_ml/data_frame/analytics/nginx-outlier-detection/_start"

# 查看进度
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-outlier-detection/_stats?pretty"
```

## 参数说明

### outlier_fraction
预期离群点的比例（默认 0.05 = 5%）

```json
"outlier_fraction": 0.05
```

- 值越小，只有最异常的点被标记
- 值越大，更多点被标记为离群点
- 建议：0.01 - 0.1

### standardization_enabled
是否标准化特征（推荐 true）

```json
"standardization_enabled": true
```

- true: 将所有特征缩放到相同范围
- false: 使用原始值
- 建议：true（特别是特征量级差异大时）

### compute_feature_influence
是否计算特征影响力（推荐 true）

```json
"compute_feature_influence": true
```

- true: 计算每个特征对离群点分数的贡献
- false: 只计算总分数
- 建议：true（便于理解为什么是离群点）

### method
算法方法（可选）

```json
"method": "distance_knn"
```

- `distance_knn`: 基于距离的 k 近邻（默认）
- `lof`: Local Outlier Factor
- `ensemble`: 集成方法

## 查看结果

### 查询离群点

```bash
# 查询所有离群点（分数 > 0.7）
curl -X GET "localhost:9200/nginx-outliers/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "range": {
      "ml.outlier_score": {
        "gte": 0.7
      }
    }
  },
  "sort": [
    {
      "ml.outlier_score": {
        "order": "desc"
      }
    }
  ]
}'
```

### 结果字段说明

```json
{
  "@timestamp": "2025-12-11T10:30:45.123Z",
  "status": 500,
  "body_bytes_sent": 50000,
  "request_time": 5.0,
  "ml": {
    "outlier_score": 0.95,
    "feature_influence": {
      "status": 0.3,
      "body_bytes_sent": 0.4,
      "request_time": 0.3
    }
  }
}
```

- `outlier_score`: 离群点分数（0-1）
  - 0: 正常
  - 1: 极度异常
  - > 0.7: 通常认为是离群点

- `feature_influence`: 特征影响力
  - 显示每个特征对离群点分数的贡献
  - 值越大，该特征越异常

## 实际案例

### 案例 1: 发现性能异常

**场景**: 发现响应时间异常长的请求

**配置**:
```json
{
  "analyzed_fields": {
    "includes": ["request_time", "body_bytes_sent"]
  },
  "outlier_fraction": 0.01
}
```

**结果**: 发现 1% 的请求响应时间 > 3 秒

### 案例 2: 发现安全威胁

**场景**: 发现异常的请求模式

**配置**:
```json
{
  "analyzed_fields": {
    "includes": ["status", "body_bytes_sent", "request_time"]
  },
  "outlier_fraction": 0.05
}
```

**结果**: 发现大量 403/404 状态码的请求（可能是扫描器）

### 案例 3: 发现流量异常

**场景**: 发现异常的流量模式

**配置**:
```json
{
  "analyzed_fields": {
    "includes": ["body_bytes_sent", "request_time"]
  },
  "outlier_fraction": 0.02
}
```

**结果**: 发现字节数异常大的请求（可能是数据泄露）

## 最佳实践

### 1. 特征选择
- 选择数值型字段
- 避免高基数字段（如 IP 地址）
- 选择与异常相关的字段

### 2. 参数调优
- 从默认参数开始
- 根据结果调整 `outlier_fraction`
- 启用 `compute_feature_influence` 便于分析

### 3. 结果分析
- 查看 `outlier_score` 分布
- 分析 `feature_influence` 找出异常原因
- 结合业务知识验证结果

### 4. 性能优化
- 限制源数据量（使用 query 过滤）
- 减少分析字段数量
- 调整 `model_memory_limit`

## 故障排查

### 问题 1: 作业失败

**症状**: 作业状态为 failed

**解决**:
```bash
# 查看详细错误
curl -X GET "localhost:9200/_ml/data_frame/analytics/nginx-outlier-detection/_stats?verbose=true&pretty"
```

常见原因：
- 内存不足：增加 `model_memory_limit`
- 字段类型错误：确保字段为数值型
- 数据量过大：使用 query 过滤

### 问题 2: 所有点都是离群点

**症状**: 大部分点的 `outlier_score` 都很高

**解决**:
- 减小 `outlier_fraction`
- 检查数据质量（是否有缺失值）
- 启用 `standardization_enabled`

### 问题 3: 没有离群点

**症状**: 所有点的 `outlier_score` 都很低

**解决**:
- 增加 `outlier_fraction`
- 检查特征选择是否合理
- 增加更多相关特征

## 下一步

- [分类指南](classification.md)
- [回归指南](regression.md)
- [配置文件参考](config/data-frame-analytics/README.md)
