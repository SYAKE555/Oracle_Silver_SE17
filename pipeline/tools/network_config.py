#!/usr/bin/env python3
"""
Basetract Network Configuration — Centralized Settings
"""

import os
import json
from typing import Dict, Any

class NetworkConfig:
    """ネットワーク設定を中央管理するクラス"""
    
    DEFAULT_CONFIG = {
        "flask": {
            "host": "127.0.0.1",
            "port": 5000,
            "debug": False,
            "cors_origins": ["http://localhost:*", "http://127.0.0.1:*"],
            "api_key_header": "X-Basetract-Key"
        },
        "timeouts": {
            "flask_startup": 10,
            "flask_shutdown": 5,
            "http_request": 15,
            "crawler_request": 15,
            "ocr_request": 30,
            "ui_animation": 2000,
            "api_health_check": 5,
            "metrics_collection": 10,
            "performance_alert_threshold_ms": 500
        },
        "crawler": {
            "min_delay": 1.0,
            "max_delay": 3.0,
            "user_agents": [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            ],
            "blocked_patterns": [
                r'^localhost$', r'^127\.', r'^0\.0\.0\.0$',
                r'^192\.168\.', r'^10\.', r'^172\.(1[6-9]|2[0-9]|3[0-1])\.',
                r'^::1$', r'^fc', r'^fd'
            ]
        },
        "ocr": {
            "default_model": "gpt-4o-mini",
            "lang": "jpn+eng",
            "mime_types": {
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".png": "image/png",
                ".webp": "image/webp"
            }
        },
        "monitoring": {
            "health_check": {
                "enabled": True, 
                "interval_seconds": 30,
                "timeout_seconds": 5
            },
            "metrics": {
                "enabled": True, 
                "collection_interval_seconds": 60
            },
            "alerts": {
                "enabled": True, 
                "thresholds": {
                    "memory_usage_percent": 85,
                    "disk_usage_percent": 85,
                    "response_time_ms": 500
                },
                "notification_channels": ["log", "console"]
            }
        },
        "logging": {
            "level": "INFO",
            "format": "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
            "rotation": {
                "max_bytes": 10000000,
                "backup_count": 5
            }
        }
    }
    
    @classmethod
    def get_flask_config(cls) -> Dict[str, Any]:
        """Flask設定を取得する"""
        config = cls.DEFAULT_CONFIG["flask"].copy()
        config["host"] = os.getenv("FLASK_HOST", config["host"])
        config["port"] = int(os.getenv("FLASK_PORT", config["port"]))
        config["debug"] = os.getenv("FLASK_DEBUG", str(config["debug"])).lower() == "true"
        return config
    
    @classmethod
    def get_timeout_config(cls) -> Dict[str, int]:
        """タイムアウト設定を取得する"""
        config = cls.DEFAULT_CONFIG["timeouts"].copy()
        for key, default_value in config.items():
            env_value = os.getenv(f"TIMEOUT_{key.upper()}")
            if env_value:
                config[key] = int(env_value)
        return config
    
    @classmethod
    def get_crawler_config(cls) -> Dict[str, Any]:
        """クローラー設定を取得する"""
        config = cls.DEFAULT_CONFIG["crawler"].copy()
        config["min_delay"] = float(os.getenv("CRAWLER_MIN_DELAY", config["min_delay"]))
        config["max_delay"] = float(os.getenv("CRAWLER_MAX_DELAY", config["max_delay"]))
        return config

    @classmethod
    def get_ocr_config(cls) -> Dict[str, Any]:
        """OCR設定を取得する"""
        config = cls.DEFAULT_CONFIG["ocr"].copy()
        config["default_model"] = os.getenv("OCR_MODEL", config["default_model"])
        return config
    
    @classmethod
    def get_server_url(cls) -> str:
        """サーバーURLを構築する"""
        flask_config = cls.get_flask_config()
        return f"http://{flask_config['host']}:{flask_config['port']}"

    @classmethod
    def get_api_status_url(cls) -> str:
        """APIステータスエンドポイントのURLを構築する"""
        return f"{cls.get_server_url()}/api/status"

    @classmethod
    def get_monitoring_config(cls) -> Dict[str, Any]:
        """監視設定を取得する"""
        return cls.DEFAULT_CONFIG["monitoring"].copy()

    @classmethod
    def get_logging_config(cls) -> Dict[str, Any]:
        """ロギング設定を取得する"""
        config = cls.DEFAULT_CONFIG["logging"].copy()
        config["level"] = os.getenv("LOG_LEVEL", config["level"])
        return config

    @classmethod
    def get_timeout(cls, name: str) -> int:
        """特定のタイムアウト値を取得する"""
        return cls.get_timeout_config().get(name, 10)

# 便利なアクセサー関数
def get_flask_host() -> str:
    return NetworkConfig.get_flask_config()["host"]

def get_flask_port() -> int:
    return NetworkConfig.get_flask_config()["port"]

def get_server_url() -> str:
    return NetworkConfig.get_server_url()

def get_timeout(timeout_name: str) -> int:
    return NetworkConfig.get_timeout(timeout_name)

if __name__ == "__main__":
    print(json.dumps(NetworkConfig.get_flask_config(), indent=2))
