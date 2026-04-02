#!/usr/bin/env python3
"""
Basetract Profile Loader — Centralized Profile Management
全ツールで共通利用するプロファイル読み込み機能を一元管理するモジュール
"""

import os
import sys
import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)

# デフォルトプロファイル設定（読み込み失敗時のフォールバック）
DEFAULT_PROFILE = {
    "logic": {
        "critical_chars": 40,
        "recommended_chars": 100,
        "tech_fact_min_count": 3,
        "official_excerpt_bypass": True
    },
    "schema": {
        "missing_keys_level": "error",
        "answer_in_options_strict": True
    },
    "ocr": {
        "confidence_min": 0.70,
        "noise_ratio_max": 0.10
    },
    "hallucination": {
        "keyword_match_required": True,
        "source_tracking_required": True
    },
    "mobile_patch": {
        "file_patterns": ["*.html"],
        "target_patterns": ["Edition", "technical_reference"],
        "max_width": 860,
        "enable_auto_patch": True
    },
    "formatter": {
        "keywords": ["Timer", "State", "Protocol", "Metric"]
    }
}

def load_quality_profile() -> Dict[str, Any]:
    """
    quality_profiles.json からアクティブプロファイルを取得する。
    失敗時はデフォルト値を使用する。
    
    Returns:
        Dict[str, Any]: アクティブプロファイル設定
    """
    try:
        # centralized import manager を使用
        try:
            from import_manager import import_quality_config
        except ImportError:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            from import_manager import import_quality_config
            
        quality_config = import_quality_config()
        profile = quality_config.get_active_profile()
        
        logger.debug("Successfully loaded quality profile from quality_profiles.json")
        return profile
        
    except Exception as e:
        logger.warning(f"quality_profiles.json の読み込みに失敗しました。デフォルト値を使用します: {e}")
        logger.debug(f"Using default profile: {DEFAULT_PROFILE}")
        return DEFAULT_PROFILE.copy()

def get_profile_section(section: str, default: Any = None) -> Any:
    """
    プロファイルの特定セクションを取得する。
    
    Args:
        section: 取得したいセクション名（例: "logic", "ocr"）
        default: セクションが存在しない場合のデフォルト値
        
    Returns:
        Any: プロファイルセクションの値
    """
    profile = load_quality_profile()
    return profile.get(section, default)

def get_profile_value(section: str, key: str, default: Any = None) -> Any:
    """
    プロファイルの特定値を取得する。
    
    Args:
        section: セクション名（例: "logic", "ocr"）
        key: キー名（例: "critical_chars", "confidence_min"）
        default: 値が存在しない場合のデフォルト値
        
    Returns:
        Any: プロファイル値
    """
    section_data = get_profile_section(section, {})
    return section_data.get(key, default)

# 便利なアクセサー関数
def get_logic_thresholds() -> Dict[str, Any]:
    """logic関連の閾値を取得する"""
    return get_profile_section("logic", {})

def get_ocr_thresholds() -> Dict[str, Any]:
    """OCR関連の閾値を取得する"""
    return get_profile_section("ocr", {})

def get_schema_config() -> Dict[str, Any]:
    """スキーマ検証設定を取得する"""
    return get_profile_section("schema", {})

def get_mobile_patch_config() -> Dict[str, Any]:
    """モバイルパッチ設定を取得する"""
    return get_profile_section("mobile_patch", {})

def get_formatter_config() -> Dict[str, Any]:
    """フォーマッター設定を取得する"""
    return get_profile_section("formatter", {})

def get_hallucination_config() -> Dict[str, Any]:
    """ハルシネーション検知設定を取得する"""
    return get_profile_section("hallucination", {})

# よく使われる値への直接アクセス
def get_critical_chars() -> int:
    """CRITICAL文字数閾値を取得"""
    return get_profile_value("logic", "critical_chars", 40)

def get_recommended_chars() -> int:
    """推奨文字数閾値を取得"""
    return get_profile_value("logic", "recommended_chars", 100)

def get_tech_fact_min_count() -> int:
    """技術的事実最小個数を取得"""
    return get_profile_value("logic", "tech_fact_min_count", 3)

def get_ocr_confidence_min() -> float:
    """OCR最低信頼度を取得"""
    return get_profile_value("ocr", "confidence_min", 0.70)

def is_official_excerpt_bypass_enabled() -> bool:
    """公式引用バイパスが有効かどうかを取得"""
    return get_profile_value("logic", "official_excerpt_bypass", True)
