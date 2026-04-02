#!/usr/bin/env python3
"""
Basetract Import Manager — Centralized Path Management
全ツールで一貫したインポートパス管理を提供するモジュール
"""

import os
import sys
from pathlib import Path
from typing import Optional

# プロジェクトルートのキャッシュ
_PROJECT_ROOT: Optional[Path] = None

def get_project_root() -> Path:
    """
    プロジェクトルートディレクトリを取得する。
    キャッシュを使用してパフォーマンスを最適化。
    """
    global _PROJECT_ROOT
    if _PROJECT_ROOT is None:
        # tools/ディレクトリからプロジェクトルートを特定
        current_dir = Path(__file__).resolve().parent
        _PROJECT_ROOT = current_dir.parent
    return _PROJECT_ROOT

def setup_tools_import() -> None:
    """
    tools/ディレクトリをPythonパスに追加する。
    重複追加を防止し、一貫性を保証する。
    """
    tools_dir = get_project_root() / "tools"
    tools_path = str(tools_dir)
    
    # 既存のパスをチェックして重複を防止
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)

def setup_config_import() -> None:
    """
    config/ディレクトリをPythonパスに追加する。
    """
    config_dir = get_project_root() / "config"
    config_path = str(config_dir)
    
    if config_path not in sys.path:
        sys.path.insert(0, config_path)

def safe_import(module_name: str, from_directory: Optional[str] = None):
    """
    安全なインポートを実行する。
    
    Args:
        module_name: インポートするモジュール名
        from_directory: 特定ディレクトリからのインポートが必要な場合
        
    Returns:
        モジュールオブジェクト
        
    Raises:
        ImportError: モジュールが見つからない場合
    """
    if from_directory:
        # 特定ディレクトリからの相対インポート
        target_dir = get_project_root() / from_directory
        target_path = str(target_dir)
        
        if target_path not in sys.path:
            sys.path.insert(0, target_path)
        
        try:
            return __import__(module_name)
        finally:
            # 一時追加したパスをクリーンアップ
            if target_path in sys.path:
                sys.path.remove(target_path)
    else:
        # 標準インポート
        try:
            return __import__(module_name)
        except ImportError:
            # tools/ディレクトリを追加して再試行
            setup_tools_import()
            return __import__(module_name)

# 便利なインポート関数
def import_quality_config():
    """quality_configモジュールを安全にインポートする。"""
    setup_tools_import()
    import quality_config
    return quality_config

def import_network_config():
    """network_configモジュールを安全にインポートする。"""
    setup_tools_import()
    import network_config
    return network_config

def import_profile_loader():
    """profile_loaderモジュールを安全にインポートする。"""
    setup_tools_import()
    import profile_loader
    return profile_loader

def import_ocr_engine():
    """ocr_engineモジュールを安全にインポートする。"""
    setup_tools_import()
    import ocr_engine
    return ocr_engine

def import_content_generator():
    """content_generatorモジュールを安全にインポートする。"""
    setup_tools_import()
    import content_generator
    return content_generator
