#!/usr/bin/env python3
"""
Basetract Monitoring Module
"""

import os, sys
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List

# インポートマネージャーを介した設定取得
from import_manager import import_network_config
NetworkConfig = import_network_config()

class BasetractMonitor:
    """システム監視クラス"""
    
    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or NetworkConfig.get_server_url()
        self.config = NetworkConfig.get_monitoring_config()
        self.log_cfg = NetworkConfig.get_logging_config()
        self.logger = self._setup_logging()
        
    def _setup_logging(self):
        """ロギング設定"""
        log_dir = Path(__file__).resolve().parent.parent / "pipeline" / "logs"
        log_dir.mkdir(exist_ok=True)
        
        from logging.handlers import RotatingFileHandler
        
        logger = logging.getLogger("basetract_monitor")
        log_level = str(self.log_cfg["level"])
        logger.setLevel(getattr(logging, log_level))
        
        rotation = self.log_cfg["rotation"]
        file_handler = RotatingFileHandler(
            log_dir / "monitor.log",
            maxBytes=rotation["max_bytes"],
            backupCount=rotation["backup_count"]
        )
        file_handler.setFormatter(logging.Formatter(self.log_cfg["format"]))
        logger.addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(self.log_cfg["format"]))
        logger.addHandler(console_handler)
        
        return logger
    
    def check_health(self):
        """ヘルスチェック実行"""
        import requests
        import time
        
        flask_cfg = NetworkConfig.get_flask_config()
        key_name = flask_cfg.get("api_key_header", "X-Basetract-Key")
        headers = {key_name: os.getenv("BASETRACT_API_KEY", "")}
        
        try:
            start_time = time.time()
            response = requests.get(
                f"{self.base_url}/api/health",
                headers=headers,
                timeout=self.config["health_check"]["timeout_seconds"]
            )
            response_time = (time.time() - start_time) * 1000
            
            if response.status_code == 200:
                health_data = response.json()
                status = health_data.get("status", "unknown")
                self.logger.info(f"Health check: {status} ({response_time:.2f}ms)")
                self._check_alerts(health_data)
                return health_data
            else:
                self.logger.error(f"Health check failed: HTTP {response.status_code}")
                return None
        except Exception as e:
            self.logger.error(f"Health check error: {e}")
            return None
    
    def _check_alerts(self, health_data):
        """アラート閾値チェック"""
        alerts = []
        components = health_data.get("components", {})
        thresholds = self.config["alerts"]["thresholds"]
        
        # 各種閾値チェック
        for key, value in thresholds.items():
            if key == "memory_usage_percent":
                usage = components.get("memory", {}).get("usage_percent", 0)
                if usage > value:
                    alerts.append(f"High memory usage: {usage}%")
            elif key == "disk_usage_percent":
                usage = components.get("disk", {}).get("usage_percent", 0)
                if usage > value:
                    alerts.append(f"High disk usage: {usage}%")
        
        for alert in alerts:
            self._send_alert(alert)
    
    def _send_alert(self, message):
        """アラート通知送信"""
        alert_message = f"[ALERT] {datetime.now().isoformat()}: {message}"
        for channel in self.config["alerts"]["notification_channels"]:
            if channel == "log":
                self.logger.warning(alert_message)
            elif channel == "console":
                print(f"🚨 {alert_message}")
    
    def collect_metrics(self):
        """メトリクス収集"""
        import requests
        flask_cfg = NetworkConfig.get_flask_config()
        key_name = flask_cfg.get("api_key_header", "X-Basetract-Key")
        headers = {key_name: os.getenv("BASETRACT_API_KEY", "")}
        
        try:
            response = requests.get(
                f"{self.base_url}/api/metrics",
                headers=headers,
                timeout=NetworkConfig.get_timeout("metrics_collection")
            )
            if response.status_code == 200:
                metrics = response.json()
                self.logger.info(f"Metrics collected")
                return metrics
            return None
        except Exception as e:
            self.logger.error(f"Metrics collection error: {e}")
            return None

    def generate_status_report(self):
        """ステータスレポート生成"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "health_status": self.check_health(),
            "system_metrics": self.collect_metrics()
        }
        reports_dir = Path(__file__).resolve().parent.parent / "pipeline" / "reports"
        reports_dir.mkdir(exist_ok=True)
        report_file = reports_dir / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        return report

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Basetract Monitoring")
    parser.add_argument("--check-health", action="store_true")
    parser.add_argument("--generate-report", action="store_true")
    args = parser.parse_args()
    
    monitor = BasetractMonitor()
    if args.check_health:
        print(json.dumps(monitor.check_health(), indent=2))
    elif args.generate_report:
        print(json.dumps(monitor.generate_status_report(), indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
