#!/usr/bin/env python3
"""
Basetract Desktop Launcher — Fixed Version
修正点:
  - file:// で webview を開くと Flask API が使えない問題を修正
  - Flask を先に起動し、http://localhost:5000/ を webview で開く
  - Flask 起動確認ループを追加
  - フォールバック: pywebview なし → webbrowser で http:// を開く
  - 中央化ネットワーク設定を使用するよう変更
"""
import os
import sys
import time
import subprocess
import webbrowser
import logging

# 中央化インポートマネージャーを使用
from import_manager import import_network_config, import_profile_loader
NetworkConfig = import_network_config()

# app.py の絶対パスを解決
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PATH = os.path.join(BASE_DIR, "system/app.py")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

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
    from network_config import get_timeout
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


def start_app():
    """Flask を起動し、PyWebView または webbrowser で表示する。"""
    # セキュリティ検証: ファイルパスの安全性を確認
    try:
        _validate_file_security(APP_PATH)
        _validate_file_security(INDEX_PATH)
    except SecurityError as e:
        logger.error(f"Security validation failed: {e}")
        return

    if not os.path.exists(APP_PATH) and not os.path.exists(INDEX_PATH):
        logger.error(f"Required files not found at {BASE_DIR}. Is the structure correct?")
        return

    flask_proc = None
    target_url = URL

    if os.path.exists(APP_PATH):
        logger.info("Starting Flask server with environment inheritance...")
        
        # 環境変数の継承と検証
        env = os.environ.copy()
        if 'FLASK_SECRET_KEY' not in env:
            logger.warning("FLASK_SECRET_KEY not found in environment. Metrics may fail.")
        
        try:
            # カレントディレクトリをプロジェクトルートに設定して起動
            flask_proc = subprocess.Popen(
                [sys.executable, APP_PATH],
                cwd=BASE_DIR,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # プロセスが即座に終了していないか確認
            time.sleep(0.5)
            if flask_proc.poll() is not None:
                stdout, stderr = flask_proc.communicate()
                logger.error(f"Flask process failed to start. stderr: {stderr}")
                flask_proc = None
                target_url = f"file://{INDEX_PATH}" if os.path.exists(INDEX_PATH) else None
                
        except (OSError, subprocess.SubprocessError) as e:
            logger.error(f"Failed to start Flask process: {e}")
            flask_proc = None
            target_url = f"file://{INDEX_PATH}" if os.path.exists(INDEX_PATH) else None
        
        if flask_proc:
            logger.info("Waiting for Flask to be ready...")
            if not _wait_for_flask():
                logger.error("Flask failed to start. Falling back to file:// mode.")
                try:
                    flask_proc.terminate()
                    from network_config import get_timeout
                    shutdown_timeout = get_timeout("flask_shutdown")
                    flask_proc.wait(timeout=shutdown_timeout)
                except Exception:
                    flask_proc.kill()
                flask_proc = None
                target_url = f"file://{INDEX_PATH}" if os.path.exists(INDEX_PATH) else None
    else:
        logger.warning("app.py not found. Opening in static file:// mode (API features unavailable).")
        target_url = f"file://{index_path}"

    if not target_url:
        logger.error("No valid URL to open.")
        return

    # デスクトップアプリまたはブラウザ起動
    try:
        import webview
        logger.info(f"Starting Desktop App via PyWebView: {target_url}")
        webview.create_window(
            'Basetract Learning Interface',
            target_url,
            width=1440,
            height=900,
            min_size=(800, 600),
        )
        webview.start()
    except ImportError:
        logger.warning("pywebview not found. Falling back to system browser.")
        try:
            webbrowser.open(target_url)
        except Exception as e:
            logger.error(f"Failed to open browser: {e}")
            logger.info(f"Manually open: {target_url}")
    except Exception as e:
        logger.error(f"Failed to start desktop app: {e}")
        logger.info(f"Manually open: {target_url}")
    finally:
        # アプリ終了時にFlaskも停止
        if flask_proc and flask_proc.poll() is None:
            flask_proc.terminate()
            try:
                shutdown_timeout = get_timeout("flask_shutdown")
                flask_proc.wait(timeout=shutdown_timeout)
                logger.info("Flask server stopped.")
            except subprocess.TimeoutExpired:
                logger.warning("Flask server did not terminate gracefully, forcing kill.")
                flask_proc.kill()

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

class SecurityError(Exception):
    """セキュリティ関連エラー"""
    pass


if __name__ == "__main__":
    start_app()
