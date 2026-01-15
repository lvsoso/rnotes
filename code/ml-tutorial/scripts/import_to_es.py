#!/usr/bin/env python3
"""
导入 NDJSON 日志到 Elasticsearch
用于 ML 教程的简化版导入脚本
"""

import json
import argparse
import time
import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

try:
    from elasticsearch import Elasticsearch, helpers
    ES_AVAILABLE = True
except ImportError:
    ES_AVAILABLE = False


def parse_auth_from_url(url):
    """从 URL 中解析用户名和密码
    
    例如: http://user:pass@localhost:9200
    返回: (username, password, clean_url)
    """
    try:
        parsed = urlparse(url)
        if parsed.username and parsed.password:
            clean_url = f"{parsed.scheme}://{parsed.hostname}"
            if parsed.port:
                clean_url += f":{parsed.port}"
            if parsed.path:
                clean_url += parsed.path
            return parsed.username, parsed.password, clean_url
    except Exception:
        pass
    return None, None, url


def get_auth_credentials(username=None, password=None, es_host=None):
    """获取认证信息，按优先级：命令行参数 > URL > 环境变量
    
    返回: (username, password, clean_es_host)
    """
    final_username = None
    final_password = None
    clean_host = es_host or "http://localhost:9200"
    
    # 优先级 1: 命令行参数
    if username:
        final_username = username
    if password:
        final_password = password
    
    # 优先级 2: 从 URL 中提取
    if es_host:
        url_username, url_password, clean_host = parse_auth_from_url(es_host)
        if url_username and not final_username:
            final_username = url_username
        if url_password and not final_password:
            final_password = url_password
    
    # 优先级 3: 环境变量
    if not final_username:
        final_username = os.environ.get('ES_USERNAME')
    if not final_password:
        final_password = os.environ.get('ES_PASSWORD')
    
    return final_username, final_password, clean_host


def import_to_elasticsearch(log_file, es_host="http://localhost:9200", 
                           index_prefix="nginx-logs", batch_size=1000,
                           username=None, password=None):
    """导入 NDJSON 日志到 Elasticsearch
    
    Args:
        log_file: NDJSON 日志文件路径
        es_host: Elasticsearch 地址
        index_prefix: 索引前缀
        batch_size: 批量导入大小
        username: 用户名（可选）
        password: 密码（可选）
    """
    
    if not ES_AVAILABLE:
        print("❌ 错误：未安装 elasticsearch 模块")
        print("请运行: pip install elasticsearch==7.9.0")
        return False
    
    # 获取认证信息
    auth_username, auth_password, clean_es_host = get_auth_credentials(
        username, password, es_host
    )
    
    # 连接 Elasticsearch
    print(f"🔌 连接到 Elasticsearch: {clean_es_host}")
    if auth_username:
        print(f"🔐 认证用户: {auth_username}")
    
    # 创建 Elasticsearch 客户端
    es_config = [clean_es_host]
    if auth_username and auth_password:
        es = Elasticsearch(es_config, http_auth=(auth_username, auth_password))
    else:
        es = Elasticsearch(es_config)
    
    # 测试连接
    max_retries = 3
    for attempt in range(max_retries):
        try:
            cluster_info = es.info()
            print(f"✅ 已连接到 Elasticsearch")
            print(f"📊 集群: {cluster_info['cluster_name']}")
            print(f"📦 版本: {cluster_info['version']['number']}")
            print()
            break
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"  ⏳ 连接中... (尝试 {attempt + 1}/{max_retries})")
                time.sleep(2)
            else:
                print(f"❌ 无法连接到 Elasticsearch: {clean_es_host}")
                print(f"错误信息: {e}")
                print()
                print("💡 故障排查:")
                print("  1. 确保 Elasticsearch 正在运行: docker ps")
                print("  2. 检查端口: curl http://localhost:9200")
                print("  3. 如果启用了认证，请提供用户名和密码:")
                print("     方式1: -u username -p password")
                print("     方式2: http://user:pass@localhost:9200")
                print("     方式3: 环境变量 ES_USERNAME, ES_PASSWORD")
                return False
    
    # 读取并导入日志
    docs = []
    total_count = 0
    success_count = 0
    failed_count = 0
    
    print(f"📂 读取日志文件: {log_file}")
    
    with open(log_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            try:
                # 解析 JSON
                parsed = json.loads(line)
                
                # 确保有时间戳
                if '@timestamp' not in parsed:
                    parsed['@timestamp'] = datetime.now().isoformat()
                
                # 提取日期用于索引名称
                timestamp = parsed['@timestamp']
                date_str = timestamp.split('T')[0].replace('-', '.')
                
                # 构建 bulk action
                action = {
                    "_index": f"{index_prefix}-{date_str}",
                    "_source": parsed
                }
                docs.append(action)
                total_count += 1
                
                # 批量导入
                if len(docs) >= batch_size:
                    try:
                        results = helpers.bulk(es, docs, raise_on_error=False, stats_only=False)
                        if isinstance(results, tuple):
                            success, errors = results
                            success_count += success
                            if errors:
                                failed_count += len(errors)
                        else:
                            success_count += results
                        print(f"  ⏳ 已处理 {total_count} 条 (成功: {success_count}, 失败: {failed_count})")
                    except Exception as e:
                        print(f"  ⚠️  批量导入错误: {e}")
                        failed_count += len(docs)
                    docs = []
                    
            except json.JSONDecodeError as e:
                print(f"  ⚠️  第 {line_num} 行 JSON 解析失败: {e}")
                failed_count += 1
    
    # 导入剩余数据
    if docs:
        try:
            results = helpers.bulk(es, docs, raise_on_error=False, stats_only=False)
            if isinstance(results, tuple):
                success, errors = results
                success_count += success
                if errors:
                    failed_count += len(errors)
            else:
                success_count += results
        except Exception as e:
            print(f"  ⚠️  最终批次错误: {e}")
            failed_count += len(docs)
    
    print()
    print("=" * 60)
    print(f"✅ 导入完成！")
    print(f"📊 总计: {total_count} 条")
    print(f"✓ 成功: {success_count} 条")
    if failed_count > 0:
        print(f"✗ 失败: {failed_count} 条")
    print("=" * 60)
    
    # 刷新索引
    try:
        es.indices.refresh(index=f"{index_prefix}-*")
        print(f"🔄 索引已刷新")
    except:
        pass
    
    # 验证导入结果
    try:
        count_result = es.count(index=f"{index_prefix}-*")
        total_docs = count_result['count']
        print(f"📈 索引 '{index_prefix}-*' 中共有 {total_docs} 条文档")
    except Exception as e:
        print(f"⚠️  无法统计: {e}")
    
    print()
    print("💡 验证命令:")
    print(f"  curl {clean_es_host}/{index_prefix}-*/_count")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="导入 NDJSON 日志到 Elasticsearch",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本用法
  python3 import_to_es.py ../data/nginx-logs.ndjson
  
  # 指定 ES 地址和索引
  python3 import_to_es.py ../data/nginx-logs.ndjson -e http://localhost:9200 -i my-logs
  
  # 使用认证（命令行参数）
  python3 import_to_es.py ../data/nginx-logs.ndjson -u elastic -p changeme
  
  # 使用认证（URL 格式）
  python3 import_to_es.py ../data/nginx-logs.ndjson -e http://elastic:changeme@localhost:9200
  
  # 使用认证（环境变量）
  export ES_USERNAME=elastic
  export ES_PASSWORD=changeme
  python3 import_to_es.py ../data/nginx-logs.ndjson

认证优先级: 命令行参数 > URL > 环境变量
        """
    )
    
    parser.add_argument(
        "log_file",
        help="NDJSON 日志文件路径"
    )
    parser.add_argument(
        "-e", "--es-host",
        default="http://localhost:9200",
        help="Elasticsearch 地址（默认: http://localhost:9200）"
    )
    parser.add_argument(
        "-i", "--index",
        default="nginx-logs",
        help="索引前缀（默认: nginx-logs）"
    )
    parser.add_argument(
        "-b", "--batch-size",
        type=int,
        default=1000,
        help="批量导入大小（默认: 1000）"
    )
    parser.add_argument(
        "-u", "--username",
        default=None,
        help="Elasticsearch 用户名"
    )
    parser.add_argument(
        "-p", "--password",
        default=None,
        help="Elasticsearch 密码"
    )
    
    args = parser.parse_args()
    
    log_path = Path(args.log_file)
    if not log_path.exists():
        print(f"❌ 文件不存在: {log_path}")
        return 1
    
    if not ES_AVAILABLE:
        print("=" * 60)
        print("❌ 缺少依赖")
        print("=" * 60)
        print()
        print("需要安装 Elasticsearch Python 客户端：")
        print()
        print("  pip install elasticsearch==7.9.0")
        print()
        print("=" * 60)
        return 1
    
    print("=" * 60)
    print("🚀 Nginx 日志导入工具")
    print("=" * 60)
    print(f"📂 日志文件: {log_path}")
    print(f"🎯 目标索引: {args.index}-*")
    print(f"📦 批量大小: {args.batch_size}")
    print("=" * 60)
    print()
    
    success = import_to_elasticsearch(
        log_path,
        args.es_host,
        args.index,
        args.batch_size,
        args.username,
        args.password
    )
    
    if success:
        print()
        print("🎉 数据导入成功！")
        print()
        print("📝 下一步:")
        print("  1. 访问 Kibana: http://localhost:5601")
        print("  2. 创建索引模式: Management > Index Patterns")
        print(f"     索引模式: {args.index}-*")
        print("     时间字段: @timestamp")
        print("  3. 开始创建 ML 作业")
        print()
        return 0
    else:
        print("❌ 导入失败")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
