#!/usr/bin/env python3
"""
Basetract Web Launcher — Fixed Version
修正点:
  - file:// で開くと Flask API (/api/*) へのfetchがCORSエラーで完全に失敗する問題を修正
  - Flask を先にバックグラウンドで起動し、http://localhost:5000/ をブラウザで開く
  - Flask起動を待ってからブラウザを開く（接続確認ループ追加）
  - app.py が存在しない場合のフォールバックとして index.html を file:// で開く
  - 中央化ネットワーク設定を使用するよう変更
"""
import os
import sys
import time
import logging
import webbrowser
import subprocess
# ← 修正: threading は使用していないため削除（デッドコード）

# 中央化ネットワーク設定をインポート
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
from network_config import NetworkConfig, get_timeout

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# 動的設定
flask_config = NetworkConfig.get_flask_config()
HOST = flask_config["host"]
PORT = flask_config["port"]
URL = NetworkConfig.get_server_url()


def _wait_for_flask() -> bool:
    """Flask が起動するまで最大 timeout 秒待機する。"""
    import urllib.request
    timeout = get_timeout("flask_startup")
    deadline = time.time() + timeout
    api_status_url = NetworkConfig.get_api_status_url()
    
    while time.time() < deadline:
        try:
            urllib.request.urlopen(api_status_url, timeout=1)
            return True
        except Exception:
            time.sleep(0.3)
    return False


def launch():
    """Flask を起動してからブラウザを開く。"""
    app_path = os.path.abspath("app.py")
    index_path = os.path.abspath("index.html")

    # セキュリティ検証: ファイルパスの安全性を確認
    try:
        _validate_file_security(app_path)
        _validate_file_security(index_path)
    except SecurityError as e:
        logger.error(f"Security validation failed: {e}")
        return

    if os.path.exists(app_path):
        logger.info(f"Starting Flask server: {app_path}")
        
        # プロセス管理の改善: セキュリティとエラーハンドリング強化
        try:
            # バックグラウンドでFlaskを起動（非ブロッキング）
            proc = subprocess.Popen(
                [sys.executable, app_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # プロセスが正常に開始したか確認
            if proc.poll() is not None:
                # プロセスが即座に終了した場合
                stdout, stderr = proc.communicate()
                logger.error(f"Flask process failed to start. stderr: {stderr}")
                _fallback_to_static(index_path)
                return
                
        except (OSError, subprocess.SubprocessError) as e:
            logger.error(f"Failed to start Flask process: {e}")
            _fallback_to_static(index_path)
            return
        
        # Flask起動を待ってからブラウザを開く（接続確認ループ追加）
        logger.info("Waiting for Flask server to be ready...")
        if not _wait_for_flask():
            logger.error("Flask failed to start within timeout. Falling back to static mode.")
            try:
                proc.terminate()
                shutdown_timeout = get_timeout("flask_shutdown")
                proc.wait(timeout=shutdown_timeout)  # プロセス終了を待機
            except subprocess.TimeoutExpired:
                logger.warning("Flask process did not terminate gracefully, forcing kill.")
                proc.kill()
            _fallback_to_static(index_path)
            return
        
        # ブラウザ起動
        try:
            logger.info(f"Opening browser: {URL}")
            webbrowser.open(URL)
        except Exception as e:
            logger.error(f"Failed to open browser: {e}")
            logger.info(f"Manually open: {URL}")
    else:
        logger.info("app.py not found. Opening static index.html")
        _fallback_to_static(index_path)

def _validate_file_security(filepath: str) -> None:
    """ファイルパスのセキュリティを検証する。"""
    if not filepath:
        raise SecurityError("Empty file path")
    
    # 絶対パスに正規化
    real_path = os.path.realpath(filepath)
    
    # 現在のワーキングディレクトリ内か確認
    cwd = os.path.realpath(os.getcwd())
    if not real_path.startswith(cwd):
        raise SecurityError(f"File path outside working directory: {filepath}")
    
    # シンボリックリンクチェック
    if os.path.islink(filepath):
        raise SecurityError(f"Symbolic links not allowed: {filepath}")
    
    # 拡張子チェック
    allowed_extensions = {'.py', '.html'}
    _, ext = os.path.splitext(real_path)
    if ext not in allowed_extensions:
        raise SecurityError(f"Disallowed file extension: {ext}")

def _fallback_to_static(index_path: str) -> None:
    """静的ファイルモードにフォールバックする。"""
    if os.path.exists(index_path):
        static_url = f"file://{index_path}"
        logger.info(f"Falling back to static mode: {static_url}")
        try:
            webbrowser.open(static_url)
        except Exception as e:
            logger.error(f"Failed to open static file: {e}")
            logger.info(f"Manually open: {static_url}")
    else:
        logger.error("Neither app.py nor index.html available for fallback.")

class SecurityError(Exception):
    """セキュリティ関連エラー"""
    pass


if __name__ == "__main__":
    launch()
