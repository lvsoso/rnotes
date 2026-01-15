#!/usr/bin/env python3
"""
Nginx 日志生成脚本
生成包含多种网络安全场景的 Nginx 日志，用于 Elasticsearch ML 训练
"""

import argparse
import random
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Tuple

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)",
    "Nikto/2.1.6",
    "sqlmap/1.5.7#stable (http://sqlmap.org)",
    "python-requests/2.26.0",
]

IP_POOLS = {
    "normal": ["192.168.1.100", "192.168.1.101", "10.0.0.50", "172.16.0.10", "203.0.113.10"],
    "suspicious": ["45.142.212.61", "185.220.101.32", "89.248.172.16"],
    "attack": ["103.109.247.8", "104.248.144.120", "159.65.142.76"],
}

URLS = {
    "normal": ["/", "/index.html", "/api/v1/users", "/login", "/dashboard"],
    "sql_injection": ["/products.php?id=1' OR '1'='1", "/search?q=admin'--", "/login.php?user=admin' OR 1=1--"],
    "xss": ["/search?q=<script>alert('XSS')</script>", "/comment?text=<img src=x onerror=alert(1)>"],
    "path_traversal": ["/download?file=../../../../etc/passwd", "/view?page=../../../../../../windows/system32/config/sam"],
    "scanner": ["/admin", "/wp-admin", "/.git/config", "/.env", "/phpmyadmin"],
}

STATUS_CODES = {
    "success": [200, 201, 204],
    "client_error": [400, 401, 403, 404],
    "server_error": [500, 502, 503],
}


class NginxLogGenerator:
    def __init__(self, num_logs: int, output_dir: str, days: int = 7):
        self.num_logs = num_logs
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.start_time = datetime.now() - timedelta(days=days)
        self.end_time = datetime.now()
        
        self.traffic_distribution = {
            "normal": 0.60,
            "sql_injection": 0.10,
            "xss": 0.08,
            "path_traversal": 0.05,
            "scanner": 0.07,
            "ddos": 0.05,
            "bot": 0.05,
        }
        
        self.structured_logs = []

    def random_timestamp(self) -> datetime:
        time_diff = self.end_time - self.start_time
        random_seconds = random.randint(0, int(time_diff.total_seconds()))
        return self.start_time + timedelta(seconds=random_seconds)

    def get_threat_info(self, traffic_type: str) -> Tuple[str, str, str]:
        threat_mapping = {
            "normal": ("none", "low", ""),
            "sql_injection": ("sql_injection", "high", "SQL Injection Attempt"),
            "xss": ("xss", "high", "Cross-Site Scripting Attempt"),
            "path_traversal": ("path_traversal", "high", "Path Traversal Attack"),
            "scanner": ("scanner", "medium", "Security Scanner Activity"),
            "ddos": ("ddos", "critical", "Potential DDoS Attack"),
            "bot": ("bot", "low", "Bot/Crawler Activity"),
        }
        return threat_mapping.get(traffic_type, ("unknown", "low", ""))

    def generate_access_log(self, traffic_type: str) -> dict:
        timestamp = self.random_timestamp()
        
        if traffic_type == "normal":
            ip = random.choice(IP_POOLS["normal"])
            user_agent = random.choice(USER_AGENTS[:4])
            method = random.choice(["GET", "POST"])
            url = random.choice(URLS["normal"])
            status = random.choice(STATUS_CODES["success"] + [404])
        elif traffic_type == "sql_injection":
            ip = random.choice(IP_POOLS["attack"])
            user_agent = random.choice(USER_AGENTS[:4] + USER_AGENTS[9:])
            method = "GET"
            url = random.choice(URLS["sql_injection"])
            status = random.choice([403, 404, 500])
        elif traffic_type == "xss":
            ip = random.choice(IP_POOLS["attack"])
            user_agent = random.choice(USER_AGENTS[:4])
            method = "GET"
            url = random.choice(URLS["xss"])
            status = random.choice([403, 200])
        elif traffic_type == "path_traversal":
            ip = random.choice(IP_POOLS["attack"])
            user_agent = random.choice(USER_AGENTS[9:])
            method = "GET"
            url = random.choice(URLS["path_traversal"])
            status = random.choice([403, 404])
        elif traffic_type == "scanner":
            ip = random.choice(IP_POOLS["suspicious"] + IP_POOLS["attack"])
            user_agent = random.choice(USER_AGENTS[6:9])
            method = random.choice(["GET", "HEAD"])
            url = random.choice(URLS["scanner"])
            status = random.choice([404, 403, 401])
        elif traffic_type == "ddos":
            ip = random.choice(IP_POOLS["attack"])
            user_agent = random.choice(USER_AGENTS)
            method = "GET"
            url = random.choice(URLS["normal"])
            status = random.choice([200, 503, 429])
        else:  # bot
            ip = random.choice(IP_POOLS["normal"])
            user_agent = random.choice(USER_AGENTS[4:6])
            method = "GET"
            url = random.choice(URLS["normal"])
            status = 200
        
        bytes_sent = random.randint(200, 50000)
        request_time = round(random.uniform(0.001, 2.5), 3)
        
        if traffic_type in ["sql_injection", "ddos"]:
            request_time = round(random.uniform(0.5, 5.0), 3)
        
        threat_type, risk_level, attack_signature = self.get_threat_info(traffic_type)
        referer = random.choice(["-", "https://www.google.com/", "https://example.com/"])
        
        return {
            "@timestamp": timestamp.isoformat(),
            "remote_addr": ip,
            "request_method": method,
            "request_uri": url,
            "status": status,
            "body_bytes_sent": bytes_sent,
            "http_referer": referer,
            "http_user_agent": user_agent,
            "request_time": request_time,
            "threat_type": threat_type,
            "risk_level": risk_level,
            "attack_signature": attack_signature,
            "traffic_type": traffic_type,
        }

    def generate_logs(self):
        print(f"生成 {self.num_logs} 条日志...")
        
        traffic_counts = {
            traffic_type: int(self.num_logs * percentage)
            for traffic_type, percentage in self.traffic_distribution.items()
        }
        
        all_traffic = []
        for traffic_type, count in traffic_counts.items():
            all_traffic.extend([traffic_type] * count)
        
        while len(all_traffic) < self.num_logs:
            all_traffic.append("normal")
        
        random.shuffle(all_traffic)
        
        for i, traffic_type in enumerate(all_traffic, 1):
            if i % 1000 == 0:
                print(f"  已生成 {i}/{self.num_logs} 条...")
            
            log_entry = self.generate_access_log(traffic_type)
            self.structured_logs.append(log_entry)
        
        print(f"日志生成完成！共 {len(self.structured_logs)} 条")

    def save_logs(self):
        ndjson_file = self.output_dir / "nginx-logs.ndjson"
        with open(ndjson_file, "w", encoding="utf-8") as f:
            for log in self.structured_logs:
                f.write(json.dumps(log) + "\n")
        print(f"NDJSON 日志已保存到: {ndjson_file}")
        
        stats_file = self.output_dir / "log_statistics.json"
        stats = {
            "total_logs": self.num_logs,
            "time_range": {
                "start": self.start_time.isoformat(),
                "end": self.end_time.isoformat(),
            },
            "traffic_distribution": self.traffic_distribution,
            "generated_at": datetime.now().isoformat(),
        }
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        print(f"统计信息已保存到: {stats_file}")


def main():
    parser = argparse.ArgumentParser(description="生成 Nginx 日志用于 ML 训练")
    parser.add_argument("-n", "--num-logs", type=int, default=10000, help="日志条数（默认: 10000）")
    parser.add_argument("-o", "--output-dir", type=str, default="../data", help="输出目录（默认: ../data）")
    parser.add_argument("--days", type=int, default=7, help="时间跨度天数（默认: 7）")
    
    args = parser.parse_args()
    start_time = datetime.now() - timedelta(days=args.days)
    
    generator = NginxLogGenerator(
        num_logs=args.num_logs,
        output_dir=args.output_dir,
        days=args.days
    )
    
    generator.generate_logs()
    generator.save_logs()
    
    print("\n✅ 完成！")
    print(f"数据文件: {args.output_dir}/nginx-logs.ndjson")
    print("\n下一步:")
    print("  1. 导入数据: python import_to_es.py ../data/nginx-logs.ndjson")
    print("  2. 访问 Kibana: http://localhost:5601")


if __name__ == "__main__":
    main()
