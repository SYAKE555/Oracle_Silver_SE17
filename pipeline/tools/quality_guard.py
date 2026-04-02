#!/usr/bin/env python3
import json
import os
import re
import sys
import logging

# 中央化インポートマネージャーを使用
from import_manager import import_profile_loader, import_quality_config

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# 中央化プロファイルローダーを使用
profile_loader = import_profile_loader()
from profile_loader import (
    load_quality_profile, get_logic_thresholds, get_schema_config,
    get_critical_chars, get_recommended_chars, get_tech_fact_min_count,
    is_official_excerpt_bypass_enabled
)

class QualityGuard:
    """Diagnostic utility for technical content integrity."""
    
    def __init__(self, target_path):
        self.path = target_path
        self.errors = []
        self.data = []

    def validate_structure(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                content = f.read()
                if self.path.endswith('.js'):
                    # window.dataBuffer を明示的にマッチ（他の配列定義との誤マッチを防ぐ）
                    # 旧: r'\[.*\]' は先に出現する他の配列（例: var tags = [...]）にマッチして
                    # JSONパースエラーを引き起こす可能性があった
                    match = re.search(r'window\.dataBuffer\s*=\s*(\[.*\])\s*;', content, re.DOTALL)
                    if not match:
                        # フォールバック: 純粋なJSON配列ファイルの場合
                        match = re.search(r'^\s*(\[.*\])\s*$', content, re.DOTALL)
                    if not match: raise ValueError("No valid window.dataBuffer or JSON array found in JS file.")
                    json_str = match.group(1)
                else:
                    json_str = content
                self.data = json.loads(json_str)
                if not isinstance(self.data, list) or (self.data and not isinstance(self.data[0], dict)):
                    raise ValueError("Data is not a valid list of segment objects.")
            return True
        except Exception as e:
            self.errors.append(f"Structural fatal error: {str(e)}")
            return False

    def validate_granularity(self):
        required_keys = {"id", "category", "text", "type", "answer", "options", "logic", "plan", "weight", "textbook_ref", "tags", "difficulty"}
        # 中央化プロファイルから閾値を取得
        CRITICAL = get_critical_chars()
        RECOMMENDED = get_recommended_chars()
        TECH_FACTS = get_tech_fact_min_count()
        BYPASS = is_official_excerpt_bypass_enabled()
        SCHEMA_LEVEL = get_schema_config().get("missing_keys_level", "error")
        
        for item in self.data:
            item_id = item.get('id', 'UNKNOWN')
            
            # 1. Strict Schema Enforcement (The 12-key Basetract Standard)
            missing_keys = required_keys - set(item.keys())
            if missing_keys:
                msg = f"ID {item_id}: Missing required schema keys -> {missing_keys}"
                if SCHEMA_LEVEL == "error":
                    self.errors.append(msg)
                else:
                    logger.warning(f"[SCHEMA WARNING] {msg}")
                
            # 2. Granularity Check (specification.md の基準に準拠)
            #    - 40文字未満: Critical（絶対不可）
            #    - 100文字未満: Warning（品質勧告）
            #    hallucination_detector.py と同一基準を維持すること
            logic = item.get("logic", "")
            # フレキシブルlogic判定: 文字数チェック + 技術的事実カウントの二層構造
            # 仕様書 (specification.md) 3.1節に準拠
            TECH_FACT_PATTERN = re.compile(
                r'\b(?:\d+(?:\.\d+)*|RFC\s*\d+|[A-Z]{2,}(?:-\d+)?(?:\s+v?\d+(?:\.\d+)*)?'
                r'|(?:show|ip|no|set|get|ping|traceroute|sh)\s+\w+'
                r'|0x[0-9A-Fa-f]+|/\d+|:\d+)\b'
            )
            tech_fact_count = len(TECH_FACT_PATTERN.findall(logic))
            is_official_excerpt = BYPASS and "[OFFICIAL_EXCERPT]" in logic

            if len(logic) < CRITICAL and not is_official_excerpt:
                if tech_fact_count >= TECH_FACTS:
                    # 短文でも技術的事実が3つ以上あれば警告のみ（仕様書準拠）
                    self.errors.append(
                        f"ID {item_id}: Logic density advisory - short but has {tech_fact_count} technical facts "
                        f"({len(logic)}/{CRITICAL} chars, profile allows if ≥{TECH_FACTS} facts). Consider expanding for clarity."
                    )
                else:
                    self.errors.append(
                        f"ID {item_id}: Logic density critical failure ({len(logic)}/{CRITICAL} chars minimum, "
                        f"{tech_fact_count}/{TECH_FACTS} technical facts required)."
                    )
            elif len(logic) < RECOMMENDED and not is_official_excerpt:
                self.errors.append(
                    f"ID {item_id}: Logic density advisory ({len(logic)}/{RECOMMENDED} chars recommended)."
                )

    def execute_audit(self):
        logger.info(f"Initiating audit: {self.path}")
        if self.validate_structure():
            self.validate_granularity()
            if not self.errors:
                logger.info("Audit successful. No structural or granularity defects identified.")
            else:
                logger.error(f"Audit failed. Identified {len(self.errors)} defects:")
                for err in self.errors:
                    logger.error(f"  - {err}")
        else:
            logger.critical("Audit terminated: Fatal structural defect.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Usage: python3 quality_guard.py <path>")
        sys.exit(1)
    guard = QualityGuard(sys.argv[1])
    guard.execute_audit()
    # ← 修正: 監査失敗時に非ゼロ終了コードを返す
    #   CI/CDパイプラインや make コマンドとの統合に必要
    if guard.errors:
        sys.exit(1)
