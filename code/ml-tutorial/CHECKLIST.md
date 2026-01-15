# 教程使用前检查清单

在开始使用本教程之前，请完成以下检查：

## 环境准备检查

- [ ] Elasticsearch 7.9.1 已安装并运行在 http://localhost:9200
  ```bash
  curl http://localhost:9200
  ```

- [ ] Kibana 7.9.1 已安装并运行在 http://localhost:5601
  ```bash
  curl http://localhost:5601/api/status
  ```

- [ ] Python 3.7+ 已安装
  ```bash
  python3 --version
  ```

- [ ] pip 已安装并更新
  ```bash
  pip3 install --upgrade pip
  ```

## 教程文件检查

- [ ] 教程目录完整
  ```bash
  ls -la ml-tutorial/
  ```
  应包含：README.md, docs/, scripts/, config/, data/, examples/

- [ ] Python 脚本存在
  ```bash
  ls ml-tutorial/scripts/
  ```
  应包含：generate_logs.py, import_to_es.py, requirements.txt

- [ ] 文档文件完整
  ```bash
  ls ml-tutorial/docs/
  ```
  应包含：quick-start.md, ml-concepts.md, troubleshooting.md 等

## 数据生成前检查

- [ ] 安装 Python 依赖
  ```bash
  cd ml-tutorial/scripts
  pip3 install -r requirements.txt
  ```

- [ ] 确保有足够的磁盘空间（至少 1GB）
  ```bash
  df -h .
  ```

- [ ] 确保数据目录可写
  ```bash
  mkdir -p ml-tutorial/data
  touch ml-tutorial/data/test
  rm ml-tutorial/data/test
  ```

## 常见问题快速索引

### 数据生成问题

**Q: 提示权限错误**
```bash
# 检查目录权限
ls -la ml-tutorial/data/
# 修改权限
chmod 755 ml-tutorial/data/
```

**Q: 提示模块不存在**
```bash
# 重新安装依赖
pip3 install -r scripts/requirements.txt --force-reinstall
```

### 数据导入问题

**Q: 连接 Elasticsearch 失败**
- 检查 Elasticsearch 是否运行：`curl http://localhost:9200`
- 检查端口是否正确：默认 9200
- 检查防火墙设置

**Q: 认证失败**
- 检查用户名密码：默认 elastic/changeme
- 尝试不同认证方式：
  ```bash
  # 命令行参数
  python3 import_to_es.py data.ndjson -u elastic -p changeme

  # URL 格式
  python3 import_to_es.py data.ndjson -e http://elastic:changeme@localhost:9200

  # 环境变量
  export ES_USERNAME=elastic
  export ES_PASSWORD=changeme
  python3 import_to_es.py data.ndjson
  ```

### ML 作业创建问题

**Q: 作业创建失败**
- 检查数据是否已导入：`curl http://localhost:9200/nginx-logs-*/_count`
- 确保时间字段映射正确
- 检查 ML 插件是否安装

**Q: 看不到异常结果**
- 等待至少 2-3 个 bucket_span 的时间
- 检查数据是否真的有异常
- 尝试调整 bucket_span 参数

## 性能优化建议

### 小规模测试（推荐）
- 数据量：1,000 - 10,000 条
- 时间跨度：1-3 天
- bucket_span：5-15 分钟

### 生产环境
- 数据量：100,000+ 条
- 时间跨度：7-30 天
- bucket_span：30-60 分钟
- 确保足够的内存和存储

## 故障排查资源

1. [故障排查文档](docs/troubleshooting.md) - 详细的问题解决步骤
2. [ML 概念说明](docs/ml-concepts.md) - 理解参数含义
3. [API 示例](examples/api-examples.sh) - 参考命令
4. [Elasticsearch 官方文档](https://www.elastic.co/guide/)

## 测试教程

运行端到端测试验证环境：
```bash
cd ml-tutorial
./test_e2e.sh
```

## 需要帮助？

如果遇到问题，请：
1. 查看 [故障排查文档](docs/troubleshooting.md)
2. 运行测试脚本诊断：`./test_e2e.sh`
3. 检查 Elasticsearch 日志：`/var/log/elasticsearch/`
4. 检查 Kibana 日志：`/var/log/kibana/`

---

✅ 完成以上检查后，您就可以开始使用教程了！

从 [快速开始指南](docs/quick-start.md) 开始您的 ML 学习之旅。