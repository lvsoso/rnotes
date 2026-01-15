# 故障排查

## Elasticsearch 连接问题

**症状**: 无法连接到 Elasticsearch

```bash
# 检查服务
docker ps | grep elasticsearch

# 检查端口
curl http://localhost:9200

# 查看日志
docker logs <container_id>
```

**解决方案**:
- 确保 Docker 容器运行中
- 等待 30 秒让服务完全启动
- 检查端口映射是否正确

## 认证失败

**症状**: 401 Unauthorized

```bash
# 方式1: 命令行参数
python3 import_to_es.py data.ndjson -u elastic -p changeme

# 方式2: URL
python3 import_to_es.py data.ndjson -e http://elastic:changeme@localhost:9200

# 方式3: 环境变量
export ES_USERNAME=elastic
export ES_PASSWORD=changeme
```

## 数据导入失败

**症状**: 导入时出错

```bash
# 检查文件格式
head -n 1 data.ndjson | python3 -m json.tool

# 检查索引
curl http://localhost:9200/_cat/indices/nginx-logs-*

# 手动测试导入
curl -X POST "localhost:9200/nginx-logs-test/_doc" \
-H 'Content-Type: application/json' -d @- < data.ndjson
```

## ML 作业无数据

**症状**: 作业运行但无结果

```bash
# 检查作业状态
curl http://localhost:9200/_ml/anomaly_detectors/<job_id>/_stats

# 检查数据源
curl http://localhost:9200/_ml/datafeeds/<datafeed_id>/_stats

# 检查索引数据
curl http://localhost:9200/nginx-logs-*/_count

# 检查时间范围
curl http://localhost:9200/nginx-logs-*/_search?size=1&sort=@timestamp:desc
```

**解决方案**:
- 确保数据时间范围正确
- 检查数据源配置的索引模式
- 确认作业已启动：`_open` 和 `_start`

## Python 依赖问题

**症状**: ModuleNotFoundError

```bash
# 安装依赖
pip install -r requirements.txt

# 或直接安装
pip install elasticsearch==7.9.0
```

## 内存不足

**症状**: Elasticsearch 启动失败或崩溃

```bash
# 调整 Docker 内存限制
# 编辑 docker-compose.yml
environment:
  - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
```

## 索引模板问题

**症状**: 字段类型错误

```bash
# 删除错误的索引
curl -X DELETE "localhost:9200/nginx-logs-*"

# 应用索引模板
curl -X PUT "localhost:9200/_template/nginx-logs" \
-H 'Content-Type: application/json' \
-d @config/elasticsearch/index-template.json

# 重新导入数据
python3 import_to_es.py data/nginx-logs.ndjson
```
