#!/usr/bin/env python3
import json
import re
import logging
import os

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# 中央化インポートマネージャーを使用
from import_manager import import_profile_loader
profile_loader = import_profile_loader()
load_quality_profile = profile_loader.load_quality_profile

_PROFILE = load_quality_profile()

class HallucinationDetector:
    """ASL (Assessment Segment Logic) validation component."""
    
    def __init__(self, critical_threshold=0.8):
        self.critical_threshold = critical_threshold

    def audit_segment(self, segment):
        """
        Performs technical consistency audit on a single assessment segment.
        Returns a list of identified inconsistencies.
        """
        # プロファイルから閾値を取得
        logic_cfg = _PROFILE.get("logic", {})
        CRITICAL = logic_cfg.get("critical_chars", 40)
        RECOMMENDED = logic_cfg.get("recommended_chars", 100)
        TECH_FACTS = logic_cfg.get("tech_fact_min_count", 3)
        BYPASS = logic_cfg.get("official_excerpt_bypass", True)
        
        issues = []
        text = segment.get("text", "")
        options = segment.get("options", [])
        answer = segment.get("answer", "")
        logic = segment.get("logic", "")
        
        # 1. Answer Integrity: Ensure the claimed answer exists in options
        if answer not in options:
            issues.append("Answer string mismatch: Claimed answer not found in options list.")
            
        # 2. Logical Coverage: Ensure logic contains key terms from the answer
        # Extracting core noun from answer (ignoring A. B. C. D. prefixes)
        clean_ans = re.sub(r'^[A-Z]\.\s*', '', answer).lower()
        if clean_ans not in logic.lower():
            issues.append("Logic gap: Explanation does not explicitly validate the correct answer.")
            
        # 3. Structural Density: Ensure text and logic have sufficient depth
        # 仕様書 (specification.md) の基準に合わせて統一:
        #   - logic 40文字未満は絶対不可（Minimum Gate）
        #   - logic 100文字未満は警告（Quality Advisory）
        #   ※ quality_guard.py の 100文字ハード閾値と二層構造で品質担保する
        if len(text) < 10:
            issues.append("Insufficient question density (text < 10 chars).")
        
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
                issues.append(
                    f"Logic density advisory - short but has {tech_fact_count} technical facts "
                    f"({len(logic)}/{CRITICAL} chars, profile allows if ≥{TECH_FACTS} facts)."
                )
            else:
                issues.append(
                    f"Logic density critical failure ({len(logic)}/{CRITICAL} chars minimum, "
                    f"{tech_fact_count}/{TECH_FACTS} technical facts required). Must contain specific technical facts."
                )
        elif len(logic) < RECOMMENDED and not is_official_excerpt:
            issues.append(
                f"Logic density advisory ({len(logic)}/{RECOMMENDED} chars recommended). Consider adding protocol-specific details."
            )
            
        # 4. Strict Schema Verification (12-Key Basetract Standard)
        required_keys = {"id", "category", "text", "type", "answer", "options", "logic", "plan", "weight", "textbook_ref", "tags", "difficulty"}
        missing_keys = required_keys - set(segment.keys())
        if missing_keys:
            issues.append(f"Schema violation: Missing required Basetract keys: {missing_keys}")
            
        return issues

    def scan_file(self, file_path):
        """Scans a JS or JSON file for hallucinations."""
        logger.info(f"Initiating hallucination audit: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Handle JS buffer format or pure JSON
            if file_path.endswith('.js'):
                # window.dataBuffer を明示的にマッチ（他の配列定義との誤マッチを防ぐ）
                # 旧: r'=\s*(\[.*\]);' は 'var x = [1]; window.dataBuffer = [...]' のとき
                # 最初の '= [1];' にマッチしてしまいJSONパースに失敗していた
                match = re.search(r'window\.dataBuffer\s*=\s*(\[.*\])\s*;', content, re.DOTALL)
                if not match:
                    # フォールバック: 純粋なJSON配列ファイル
                    match = re.search(r'^\s*(\[.*\])\s*$', content, re.DOTALL)
                if not match:
                    logger.error("Could not locate window.dataBuffer in JS file.")
                    return False
                data = json.loads(match.group(1))
            else:
                data = json.loads(content)
            
            if not isinstance(data, list):
                logger.error("Target data must be a list of segments.")
                return False

            total_errors = 0
            for i, segment in enumerate(data):
                segment_issues = self.audit_segment(segment)
                if segment_issues:
                    total_errors += 1
                    logger.warning(f"Segment {i} Audit Failed:")
                    for issue in segment_issues:
                        logger.warning(f"  - {issue}")
            
            if total_errors == 0:
                logger.info("Audit successful. No technical inconsistencies detected within scope.")
                return True
            else:
                logger.error(f"Audit failed. {total_errors} segments require manual correction.")
                return False

        except Exception as e:
            logger.error(f"Audit interrupted: {str(e)}")
            return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        logger.error("Usage: python3 hallucination_detector.py <target_file>")
        sys.exit(1)

    detector = HallucinationDetector()
    result = detector.scan_file(sys.argv[1])
    # ← 修正: 監査失敗時に非ゼロ終了コードを返す
    #   CI/CDパイプラインや make コマンドとの統合に必要
    sys.exit(0 if result else 1)
