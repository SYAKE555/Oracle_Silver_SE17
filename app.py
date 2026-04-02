#!/usr/bin/env python3
"""
Basetract Standard API Server — Improved Version
改善点:
  - シークレットキーのハードコードを廃止 (起動時に環境変数必須)
  - DBコネクション管理を Flask g オブジェクトに統一
  - 入力バリデーションの追加
  - ローカルAPIキー認証の追加
  - エラーハンドラーの整備
  - 静的ファイル配信を追加（index.html, app/ ディレクトリ）
    ※ launcher が http://localhost:5000/ で開くために必須
"""

import os
import sys
import json
import sqlite3
import logging
import uuid
from logging.handlers import RotatingFileHandler
from functools import wraps
from datetime import datetime
import time

try:
    from flask import Flask, request, jsonify, session, g, send_from_directory
    from flask_cors import CORS
    from dotenv import load_dotenv
except ImportError:
    # 依存関係が未インストールの場合は bootstrap.py の実行を促す
    print("Error: Missing dependencies (flask, flask-cors, python-dotenv). Run pipeline/bootstrap.py first.")
    sys.exit(1)

# 中央化インポートマネージャーを使用
from import_manager import import_network_config, get_project_root
NetworkConfig = import_network_config()
PROJECT_ROOT = get_project_root()

app = Flask(__name__)

# Security: シークレットキーは環境変数から必須取得。未設定なら起動を拒否する。
_secret = os.getenv('FLASK_SECRET_KEY')
if not _secret:
    raise RuntimeError(
        "FLASK_SECRET_KEY is not set.\n"
        "Run: export FLASK_SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')\n"
        "and add it to your config/.env file."
    )
app.secret_key = _secret

# 中央化ネットワーク設定を取得
flask_config = NetworkConfig.get_flask_config()

# Hardened CORS: ローカル環境のみ許可
CORS(app, resources={r"/api/*": {"origins": flask_config["cors_origins"]}})

# Load Config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
CONFIG = {}
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        CONFIG = json.load(f)

# Logging
log_dir = os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'logs')
os.makedirs(log_dir, exist_ok=True)
handler = RotatingFileHandler(os.path.join(log_dir, 'app.log'), maxBytes=1_000_000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)


# --- Database Connection Management (Flask g pattern) ---
def get_db():
    """リクエストスコープでDBコネクションを管理する。"""
    if 'db' not in g:
        db_name = CONFIG.get('database_name', 'basetract_learning.db')
        # ← バグ修正: 相対パスだと起動ディレクトリによってDBファイルが散逸する
        #   PROJECT_ROOT に固定することで常にプロジェクト直下に作成される
        db_path = os.path.join(PROJECT_ROOT, db_name)
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
        # SQLite 外部キー制約は接続ごとに有効化が必要
        g.db.execute('PRAGMA foreign_keys = ON')
    return g.db

@app.teardown_appcontext
def close_db(error):
    """リクエスト終了時にコネクションを安全にクローズする。"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """
    analytics_schema.sql を読み込んでDBを初期化する。
    ← 改善: app独自のインラインDDLをやめ、analytics_schema.sql と一元管理する
       （旧実装はFKなし・CHECKなし・インデックスなしの不完全テーブルを作成していた）
    """
    db = get_db()
    schema_path = os.path.join(PROJECT_ROOT, 'app', 'data', 'analytics_schema.sql')
    if os.path.exists(schema_path):
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
        db.executescript(schema_sql)
        app.logger.info(f"Database initialized from: {schema_path}")
    else:
        # フォールバック: スキーマファイル未デプロイ時の最小テーブル
        app.logger.warning("analytics_schema.sql not found at %s. Using minimal fallback schema.", schema_path)
        db.executescript('''
            PRAGMA foreign_keys = ON;
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL DEFAULT 'anonymous',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS questions (
                id TEXT PRIMARY KEY,
                topic TEXT,
                question_data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS learning_history (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                question_id TEXT,
                result INTEGER CHECK(result IN (0, 1)),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
    db.commit()


# --- Local API Key Authentication ---
def require_api_key(f):
    """ローカル環境向けのシンプルなAPIキー認証デコレーター。"""
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-Basetract-Key') or request.args.get('api_key')
        expected = os.getenv('BASETRACT_API_KEY')
        # APIキーが設定されていない場合はローカル開発モードとして素通りを許可
        if expected and api_key != expected:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated


# --- Input Validation Helpers ---
def validate_question_payload(data):
    """問題データのバリデーション。Basetract 12キースキーマを検証する。"""
    required_keys = {"id", "category", "text", "type", "answer", "options",
                     "logic", "plan", "weight", "textbook_ref", "tags", "difficulty"}
    missing = required_keys - set(data.keys())
    if missing:
        return False, f"Missing required keys: {missing}"
    if data.get("type") not in ("choice", "text"):
        return False, "Field 'type' must be 'choice' or 'text'."
    if not isinstance(data.get("options"), list):
        return False, "Field 'options' must be a list."
    return True, None


# --- Static File Serving ---

@app.route('/', methods=['GET'])
def index():
    """ルートリクエストに index.html を返す。"""
    return send_from_directory(PROJECT_ROOT, 'index.html')

@app.route('/mobile.html', methods=['GET'])
def mobile():
    return send_from_directory(PROJECT_ROOT, 'mobile.html')

@app.route('/app/<path:filename>', methods=['GET'])
def app_static(filename):
    """app/ ディレクトリ以下の静的ファイルを配信する。"""
    app_dir = os.path.join(PROJECT_ROOT, 'app')
    return send_from_directory(app_dir, filename)


# --- Routes ---
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "status": "active",
        "project": CONFIG.get('project_name'),
        "version": "7.0-synced"
    })

@app.route('/api/questions', methods=['GET'])
@require_api_key
def get_questions():
    topic = request.args.get('topic')
    db = get_db()
    if topic:
        rows = db.execute('SELECT * FROM questions WHERE topic = ?', (topic,)).fetchall()
    else:
        rows = db.execute('SELECT * FROM questions').fetchall()
    return jsonify([dict(r) for r in rows])

@app.route('/api/questions', methods=['POST'])
@require_api_key
def add_question():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    valid, err = validate_question_payload(data)
    if not valid:
        return jsonify({"error": err}), 422

    db = get_db()
    try:
        db.execute(
            'INSERT INTO questions (id, topic, question_data) VALUES (?, ?, ?)',
            (data['id'], data.get('category', 'Uncategorized'), json.dumps(data, ensure_ascii=False))
        )
        db.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": f"Question ID '{data['id']}' already exists."}), 409

    app.logger.info(f"Question added: {data['id']}")
    return jsonify({"status": "created", "id": data['id']}), 201

@app.route('/api/history', methods=['POST'])
@require_api_key
def record_history():
    data = request.get_json(silent=True)
    if not data or 'question_id' not in data or 'result' not in data:
        return jsonify({"error": "Fields 'question_id' and 'result' are required."}), 400

    db = get_db()
    db.execute(
        'INSERT INTO learning_history (id, user_id, question_id, result) VALUES (?, ?, ?, ?)',
        (str(uuid.uuid4()), data.get('user_id', 'anonymous'), data['question_id'], int(bool(data['result'])))
    )
    db.commit()
    return jsonify({"status": "recorded"}), 201


# --- Error Handlers ---
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

@app.route('/api/health', methods=['GET'])
def health_check():
    """Comprehensive system health check endpoint."""
    try:
        import psutil
        start_time = time.time()
        
        # Database connectivity check
        db = get_db()
        db.execute('SELECT 1')
        db_status = "healthy"
        
        # Configuration check
        config_status = "healthy" if CONFIG and 'project_name' in CONFIG else "missing"
        
        # File system check
        project_root_accessible = os.access(PROJECT_ROOT, os.R_OK)
        fs_status = "healthy" if project_root_accessible else "error"
        
        # Memory usage check
        memory = psutil.virtual_memory()
        memory_status = "healthy" if memory.percent < 90 else "warning"
        
        # Disk space check
        disk = psutil.disk_usage(PROJECT_ROOT)
        disk_status = "healthy" if disk.percent < 90 else "warning"
        
        # Response time check
        response_time = (time.time() - start_time) * 1000  # ms
        performance_status = "healthy" if response_time < 100 else "slow"
        
        overall_status = "healthy"
        if any(status in ["error", "missing"] for status in [db_status, config_status, fs_status]):
            overall_status = "unhealthy"
        elif any(status in ["warning", "slow"] for status in [memory_status, disk_status, performance_status]):
            overall_status = "degraded"
        
        health_data = {
            "status": overall_status,
            "timestamp": datetime.utcnow().isoformat(),
            "version": "7.0-synced",
            "uptime": time.time() - start_time,
            "response_time_ms": round(float(response_time), 2),
            "components": {
                "database": {
                    "status": db_status,
                    "type": "sqlite"
                },
                "configuration": {
                    "status": config_status,
                    "project": CONFIG.get('project_name', 'unknown')
                },
                "filesystem": {
                    "status": fs_status,
                    "accessible": bool(project_root_accessible)
                },
                "memory": {
                    "status": memory_status,
                    "usage_percent": float(memory.percent),
                    "available_gb": round(float(memory.available) / (1024**3), 2)
                },
                "disk": {
                    "status": disk_status,
                    "usage_percent": float(disk.percent),
                    "free_gb": round(float(disk.free) / (1024**3), 2)
                },
                "performance": {
                    "status": performance_status,
                    "response_time_ms": round(float(response_time), 2)
                }
            },
            "endpoints": {
                "questions": "/api/questions",
                "history": "/api/history",
                "status": "/api/status"
            }
        }
        
        status_code = 200 if overall_status == "healthy" else (503 if overall_status == "unhealthy" else 200)
        return jsonify(health_data), status_code
        
    except Exception as e:
        app.logger.error(f"Health check failed: {e}")
        return jsonify({
            "status": "unhealthy",
            "timestamp": datetime.utcnow().isoformat(),
            "error": str(e),
            "components": {}
        }), 500

@app.route('/api/metrics', methods=['GET'])
@require_api_key
def system_metrics():
    """Detailed system metrics endpoint."""
    try:
        import psutil
        
        # System metrics
        cpu_percent = float(psutil.cpu_percent(interval=1))
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage(PROJECT_ROOT)
        
        # Database metrics
        db = get_db()
        question_count = int(db.execute('SELECT COUNT(*) FROM questions').fetchone()[0])
        history_count = int(db.execute('SELECT COUNT(*) FROM learning_history').fetchone()[0])
        
        # Application metrics
        log_size = 0
        log_path = os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'logs', 'app.log')
        if os.path.exists(log_path):
            log_size = int(os.path.getsize(log_path))
        
        metrics = {
            "timestamp": datetime.utcnow().isoformat(),
            "system": {
                "cpu_percent": cpu_percent,
                "memory": {
                    "total_gb": round(float(memory.total) / (1024**3), 2),
                    "available_gb": round(float(memory.available) / (1024**3), 2),
                    "used_gb": round(float(memory.used) / (1024**3), 2),
                    "percent": float(memory.percent)
                },
                "disk": {
                    "total_gb": round(float(disk.total) / (1024**3), 2),
                    "free_gb": round(float(disk.free) / (1024**3), 2),
                    "used_gb": round(float(disk.used) / (1024**3), 2),
                    "percent": float(disk.percent)
                }
            },
            "application": {
                "database": {
                    "questions_count": question_count,
                    "history_count": history_count,
                    "type": "sqlite"
                },
                "logs": {
                    "app_log_size_bytes": log_size,
                    "app_log_size_mb": round(float(log_size) / (1024**2), 2)
                },
                "configuration": {
                    "project_name": CONFIG.get('project_name', 'unknown'),
                    "flask_debug": flask_config['debug'],
                    "flask_host": flask_config['host'],
                    "flask_port": flask_config['port']
                }
            }
        }
        
        return jsonify(metrics)
        
    except Exception as e:
        app.logger.error(f"Metrics collection failed: {e}")
        return jsonify({"error": "Metrics collection failed", "details": str(e)}), 500

@app.errorhandler(500)
def internal_error(e):
    app.logger.error(f"Internal error: {e}")
    return jsonify({"error": "Internal server error"}), 500


# --- Entry Point ---
if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.logger.info(f"Basetract API starting — project: {CONFIG.get('project_name')}")
    app.logger.info(f"Configuration: host={flask_config['host']}, port={flask_config['port']}, debug={flask_config['debug']}")
    app.run(host=flask_config['host'], port=flask_config['port'], debug=flask_config['debug'])
