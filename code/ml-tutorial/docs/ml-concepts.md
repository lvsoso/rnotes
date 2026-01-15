# 机器学习概念说明

本文档介绍 Elasticsearch 机器学习的核心概念和原理。

## 异常检测基本原理

### 什么是异常？

异常是指偏离正常模式的数据点或行为。在 Nginx 日志中，异常可能包括：

- 请求速率突然增加（DDoS 攻击）
- 响应时间异常延长（性能问题）
- 错误率突然上升（系统故障）
- 单个 IP 的异常行为（扫描器、攻击者）

### 机器学习如何检测异常？

1. **学习正常模式**
   - 分析历史数据
   - 建立正常行为的统计模型
   - 理解数据的周期性和趋势

2. **计算异常分数**
   - 比较新数据与正常模式
   - 计算偏离程度
   - 输出异常分数（0-100）

3. **识别异常**
   - 分数 > 75: 严重异常
   - 分数 50-75: 中等异常
   - 分数 25-50: 轻微异常
   - 分数 < 25: 正常

## 检测器类型和用途

### 1. Count（计数）

**用途**: 检测事件数量的异常

**适用场景**:
- 请求速率异常
- DDoS 攻击检测
- 流量突增/突降

**示例**:
```json
{
  "function": "count",
  "detector_description": "请求计数异常"
}
```

**解读**: 当请求数量显著高于或低于正常水平时触发异常。

### 2. Mean（平均值）

**用途**: 检测数值字段平均值的异常

**适用场景**:
- 响应时间异常
- 字节数异常
- 性能指标异常

**示例**:
```json
{
  "function": "mean",
  "field_name": "request_time",
  "detector_description": "平均响应时间异常"
}
```

**解读**: 当平均响应时间显著高于或低于正常水平时触发异常。

### 3. Sum（总和）

**用途**: 检测数值字段总和的异常

**适用场景**:
- 总流量异常
- 总字节数异常
- 累计指标异常

**示例**:
```json
{
  "function": "sum",
  "field_name": "body_bytes_sent",
  "detector_description": "总字节数异常"
}
```

**解读**: 当总字节数显著高于或低于正常水平时触发异常。

### 4. Min/Max（最小/最大值）

**用途**: 检测数值字段最小/最大值的异常

**适用场景**:
- 极值检测
- 性能边界监控

**示例**:
```json
{
  "function": "max",
  "field_name": "request_time",
  "detector_description": "最大响应时间异常"
}
```

**解读**: 当最大响应时间显著高于正常水平时触发异常。

### 5. Rare（罕见值）

**用途**: 检测罕见的分类值

**适用场景**:
- 罕见 URL 访问
- 罕见用户代理
- 异常请求方法

**示例**:
```json
{
  "function": "rare",
  "by_field_name": "request_uri",
  "detector_description": "罕见 URL 访问"
}
```

**解读**: 当出现罕见的 URL 访问时触发异常。

### 6. Freq_Rare（频繁/罕见值）

**用途**: 检测值的频率变化

**适用场景**:
- 访问模式变化
- 行为模式变化

**示例**:
```json
{
  "function": "freq_rare",
  "by_field_name": "remote_addr",
  "detector_description": "IP 访问频率异常"
}
```

**解读**: 当某个 IP 的访问频率显著变化时触发异常。

## 实际案例

### 案例 1: DDoS 攻击检测

**场景**: 检测 DDoS 攻击导致的请求速率异常

**配置**:
```json
{
  "analysis_config": {
    "bucket_span": "5m",
    "detectors": [
      {
        "function": "count"
      }
    ],
    "influencers": ["remote_addr"]
  }
}
```

**正常模式**: 每 5 分钟 1000 个请求

**异常情况**: 
- 时间: 2025-12-11 14:30
- 请求数: 50000（50倍）
- 异常分数: 95
- 影响因素: 来自 103.109.247.8 的大量请求

**解读**: 检测到严重的请求速率异常，可能是 DDoS 攻击。

### 案例 2: SQL 注入检测

**场景**: 检测 SQL 注入攻击导致的错误率异常

**配置**:
```json
{
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "count"
      }
    ],
    "influencers": ["status", "request_uri", "remote_addr"]
  },
  "datafeed_config": {
    "query": {
      "bool": {
        "must": [
          {
            "range": {
              "status": {
                "gte": 400
              }
            }
          },
          {
            "match": {
              "threat_type": "sql_injection"
            }
          }
        ]
      }
    }
  }
}
```

**正常模式**: 每 15 分钟 10 个 SQL 注入尝试（被拦截）

**异常情况**:
- 时间: 2025-12-11 15:45
- SQL 注入尝试: 500（50倍）
- 异常分数: 88
- 影响因素: 
  - 状态码: 403
  - URL: /products.php?id=1' OR '1'='1
  - IP: 104.248.144.120

**解读**: 检测到大量 SQL 注入尝试，可能是自动化攻击工具。

### 案例 3: 性能异常检测

**场景**: 检测响应时间异常延长

**配置**:
```json
{
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "function": "mean",
        "field_name": "request_time"
      }
    ],
    "influencers": ["request_uri", "request_method"]
  }
}
```

**正常模式**: 平均响应时间 0.2 秒

**异常情况**:
- 时间: 2025-12-11 16:00
- 平均响应时间: 2.5 秒（12.5倍）
- 异常分数: 82
- 影响因素:
  - URL: /api/v1/users
  - 方法: GET

**解读**: /api/v1/users 接口响应时间异常延长，可能是数据库查询慢或服务器负载高。

## 关键概念

### Bucket Span（时间桶）

时间桶是分析的基本时间单位。

**示例**: `bucket_span: "15m"`

- 数据被分成 15 分钟的时间段
- 每个时间段独立分析
- 异常分数针对每个时间段计算

**选择建议**:
- 数据频率高: 5-15 分钟
- 数据频率中: 15-60 分钟
- 数据频率低: 1-24 小时

### Influencers（影响因素）

影响因素帮助理解异常的原因。

**示例**: `influencers: ["remote_addr", "request_uri"]`

- 当检测到异常时，显示哪些 IP 和 URL 最相关
- 帮助快速定位问题根源

**选择建议**:
- 选择分类字段（keyword 类型）
- 避免高基数字段（如唯一 ID）
- 通常 2-5 个字段

### Partition/By/Over Fields

这些字段定义了如何分组和比较数据。

#### Partition Field（分区字段）
为每个值单独建模

**示例**: 
```json
{
  "function": "count",
  "partition_field_name": "remote_addr"
}
```

**含义**: 为每个 IP 单独建立正常模式，检测该 IP 自身的异常行为。

#### By Field（分组字段）
在组内检测异常

**示例**:
```json
{
  "function": "mean",
  "field_name": "request_time",
  "by_field_name": "request_uri"
}
```

**含义**: 为每个 URL 计算平均响应时间，检测哪个 URL 的响应时间异常。

#### Over Field（群体字段）
检测群体中的异常个体

**示例**:
```json
{
  "function": "count",
  "over_field_name": "remote_addr"
}
```

**含义**: 在所有 IP 中，检测哪个 IP 的请求数量异常（相对于其他 IP）。

### Anomaly Score（异常分数）

异常分数表示数据点的异常程度。

**分数范围**: 0-100

**严重程度**:
- 0-25: 正常
- 25-50: 轻微异常（警告）
- 50-75: 中等异常（需要关注）
- 75-100: 严重异常（需要立即处理）

**影响因素**:
- 偏离程度：偏离越大，分数越高
- 历史数据：学习时间越长，模型越准确
- 数据质量：数据越稳定，异常越明显

## 最佳实践

### 1. 数据准备
- 确保时间字段格式正确
- 数据质量要好（无大量缺失值）
- 有足够的历史数据（至少 2-3 个 bucket_span）

### 2. 配置选择
- 从简单配置开始（单指标）
- 选择合适的 bucket_span
- 选择相关的 influencers

### 3. 结果解读
- 关注高分异常（> 75）
- 查看 influencers 理解原因
- 结合业务知识判断

### 4. 持续优化
- 根据误报/漏报调整参数
- 添加更多相关 influencers
- 尝试不同的检测器函数

## 进阶资源

### 官方文档
- [Elasticsearch ML 概述](https://www.elastic.co/guide/en/machine-learning/current/ml-overview.html)
- [异常检测算法](https://www.elastic.co/guide/en/machine-learning/current/ml-algorithms.html)
- [检测器函数参考](https://www.elastic.co/guide/en/machine-learning/current/ml-functions.html)

### 相关文档
- [Anomaly Detection 配置指南](anomaly-detection-setup.md)
- [Data Frame Analytics 概述](data-frame-analytics/overview.md)
- [快速开始指南](quick-start.md)

## 常见问题

### Q: 需要多少历史数据？

**A**: 建议至少有 2-3 个 bucket_span 的数据。例如，如果 bucket_span 是 15 分钟，至少需要 30-45 分钟的数据。数据越多，模型越准确。

### Q: 为什么没有检测到异常？

**A**: 可能的原因：
1. 数据确实没有异常
2. bucket_span 太大，平滑了异常
3. 学习时间不够
4. 检测器配置不合适

### Q: 如何减少误报？

**A**: 
1. 增大 bucket_span
2. 减少 influencers
3. 等待更长时间让模型学习
4. 检查数据质量

### Q: 异常分数如何计算？

**A**: 异常分数基于统计概率计算，考虑：
- 数据点与正常模式的偏离程度
- 历史数据的变异性
- 时间序列的趋势和周期性

分数越高，表示越不可能是正常情况。
