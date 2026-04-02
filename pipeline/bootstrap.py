#!/usr/bin/env python3
"""
Basetract Bootstrap Module
"""
import subprocess
import sys
import os
import logging

# 中央化ネットワーク設定をインポート
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
from network_config import NetworkConfig

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# pip install 名 → Python import 名 のマッピング
# pip名とimport名が異なるパッケージを明示的に管理する
IMPORT_MAP = {
    "beautifulsoup4": "bs4",
    "flask-cors": "flask_cors",
    "python-dotenv": "dotenv",
    "pywebview": "webview",
    "Pillow": "PIL",
    "pytesseract": "pytesseract",
}

DEPENDENCIES = [
    "requests",
    "beautifulsoup4",
    "flask",
    "flask-cors",
    "pywebview",
    "python-dotenv",
    # OCR エンジン（ocr_engine.py）
    "pytesseract",
    "Pillow",
    # AI 生成・レビュー機能
    "openai",
    # システム監視（app.py /api/health, /api/metrics で使用）
    "psutil",
]

def check_dependencies():
    logger.info("Verifying Basetract dependencies...")
    missing = []
    import importlib
    for dep in DEPENDENCIES:
        import_name = IMPORT_MAP.get(dep, dep.replace("-", "_"))
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing.append(dep)
            logger.warning(f"Missing: {dep} (import name: {import_name})")
    return missing

def install_dependencies(missing, auto_confirm=False):
    if not missing:
        logger.info("All dependencies satisfied.")
        return True

    logger.warning(f"Missing dependencies: {missing}")
    
    if auto_confirm:
        choice = 'y'
    else:
        print(f"\nInstall missing packages? {missing} (y/n)")
        choice = input().strip().lower()

    if choice == 'y':
        logger.info("Installing dependencies...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install"] + missing,
                stdout=subprocess.DEVNULL
            )
            logger.info("Installation complete.")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Installation failed: {e}")
            return False
    else:
        logger.info("Installation skipped.")
        return False

def verify_network_config():
    """Verify network configuration is accessible and display current settings."""
    try:
        flask_config = NetworkConfig.get_flask_config()
        timeout_config = NetworkConfig.get_timeout_config()
        
        logger.info("Network Configuration Verification:")
        logger.info(f"  Flask Host: {flask_config['host']}")
        logger.info(f"  Flask Port: {flask_config['port']}")
        logger.info(f"  Flask Debug: {flask_config['debug']}")
        logger.info(f"  Server URL: {NetworkConfig.get_server_url()}")
        logger.info("  Timeout Settings:")
        for key, value in timeout_config.items():
            logger.info(f"    {key}: {value}s")
        
        # Check for environment variable overrides
        env_overrides = []
        if os.getenv("FLASK_HOST"):
            env_overrides.append("FLASK_HOST")
        if os.getenv("FLASK_PORT"):
            env_overrides.append("FLASK_PORT")
        if os.getenv("FLASK_DEBUG"):
            env_overrides.append("FLASK_DEBUG")
        
        if env_overrides:
            logger.info(f"  Environment Overrides: {', '.join(env_overrides)}")
        else:
            logger.info("  Using default configuration")
            
        return True
        
    except Exception as e:
        logger.error(f"Network configuration verification failed: {e}")
        return False

def verify_env_file():
    """Check if .env file exists; warn if not."""
    config_dir = os.path.join(os.path.dirname(__file__), '..', 'config')
    env_path = os.path.join(config_dir, '.env')
    template_path = os.path.join(config_dir, 'secrets.template.env')

    if not os.path.exists(env_path):
        if os.path.exists(template_path):
            logger.warning(".env file not found. Copy config/secrets.template.env to config/.env and fill in your API keys.")
        else:
            logger.warning(".env file not found. AI-assisted features will be disabled.")
    else:
        logger.info(".env configuration file detected.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Basetract Bootstrap Utility")
    parser.add_argument("-y", "--yes", action="store_true", help="Auto-confirm dependency installation")
    args = parser.parse_args()

    logger.info("=== Basetract Bootstrap Starting ===")
    
    # Verify network configuration first
    if not verify_network_config():
        logger.warning("Network configuration issues detected. System may not function correctly.")
    
    missing = check_dependencies()
    success = install_dependencies(missing, auto_confirm=args.yes)
    verify_env_file()
    
    if not success and missing:
        logger.error("Some dependencies are missing. The system may not function correctly.")
        sys.exit(1)
    
    logger.info("Bootstrap complete. System ready for operation.")
    logger.info(f"Access the application at: {NetworkConfig.get_server_url()}")
