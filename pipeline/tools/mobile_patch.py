import os
import re
import logging
import json
import sys
from pathlib import Path

# ← 修正: print() → logging に統一（他ツールとの一貫性）
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# quality_profiles.json からアクティブプロファイルを取得するヘルパー
def _load_quality_profile() -> dict:
    """tools/quality_config.py の get_active_profile() を呼ぶ。失敗時はデフォルト値を使用。"""
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from quality_config import get_active_profile
        return get_active_profile()
    except Exception as e:
        logger.warning(f"quality_profiles.json の読み込みに失敗しました。デフォルト値を使用します: {e}")
        return {
            "logic": {"critical_chars": 40, "recommended_chars": 100,
                      "tech_fact_min_count": 3, "official_excerpt_bypass": True},
            "schema": {"missing_keys_level": "error", "answer_in_options_strict": True},
            "ocr": {"confidence_min": 0.70, "noise_ratio_max": 0.10},
            "hallucination": {"keyword_match_required": True, "source_tracking_required": True},
            "mobile_patch": {
                "file_patterns": ["*.html"],
                "target_patterns": ["Edition", "technical_reference"],
                "max_width": 860,
                "enable_auto_patch": True
            }
        }

_PROFILE = _load_quality_profile()

NUCLEAR_CSS = """
<style>
/* ── BASETRACT INFRASTRUCTURE REVISION ── */
/* ── Nuclear Responsive Override (Phase 15) ── */
@media (max-width: {max_width}px) {{
    #app, body {{
        flex-direction: column !important;
        display: flex !important;
    }}
    #sidebar, .side-nav {{
        position: relative !important;
        width: 100% !important;
        height: auto !important;
        transform: none !important;
        left: 0 !important;
        margin-left: 0 !important;
        border-right: none !important;
        border-bottom: 2px solid #000 !important;
    }}
    #main, .main-content, .content-viewport {{
        margin-left: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        padding: 20px 10px !important;
    }}
    /* Force tables and code blocks to respect the parent width and scroll horizontally on mobile */
    pre, code, table, .table-wrapper {{
        max-width: 100% !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
    }}
    /* Text constraints */
    p, li, div, h1, h2, h3, h4, h5 {{
        overflow-wrap: break-word !important;
        word-break: break-word !important;
    }}
    /* Hide decorative components that break width */
    .mesh-bg {{ display: none !important; }}
}}
</style>
"""

def patch_file(filepath):
    logger.info(f"Attempting to patch {filepath}...")
    if not os.path.exists(filepath):
        logger.warning(f"Skipping {filepath}, not found.")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid double patching
    if "Nuclear Responsive Override (Phase 15)" in content:
        logger.info(f"Already patched {filepath}.")
        return

    # プロファイルから設定を取得
    mobile_cfg = _PROFILE.get("mobile_patch", {})
    max_width = mobile_cfg.get("max_width", 860)
    
    # CSSテンプレートにプロファイル値を注入
    css_with_profile = NUCLEAR_CSS.format(max_width=max_width)

    # We inject the style block just before the </body> tag to ensure it overrides
    # any inline or previously declared stylesheets in the double-wrapped HTML.
    if "</body>" in content:
        # Find the LAST occurrence of </body> to ensure it's the outermost wrapper
        parts = content.rsplit("</body>", 1)
        if len(parts) == 2:
            new_content = parts[0] + css_with_profile + "\n</body>" + parts[1]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            logger.info(f"Successfully patched {filepath} with Nuclear Responsive CSS (max_width: {max_width}px).")
        else:
            logger.error(f"Failed to split {filepath} at </body>.")
    else:
        logger.error(f"Failed to find </body> in {filepath}.")

def should_patch_file(filename: str) -> bool:
    """プロファイル設定に基づいてファイルをパッチすべきか判定する。"""
    mobile_cfg = _PROFILE.get("mobile_patch", {})
    if not mobile_cfg.get("enable_auto_patch", True):
        return False
    
    file_patterns = mobile_cfg.get("file_patterns", ["*.html"])
    target_patterns = mobile_cfg.get("target_patterns", ["Edition", "technical_reference"])
    
    # ファイル名パターンチェック
    import fnmatch
    for pattern in file_patterns:
        if fnmatch.fnmatch(filename, pattern):
            # ターゲットパターンチェック
            for target in target_patterns:
                if target in filename:
                    return True
    return False

if __name__ == "__main__":
    import sys
    # If arguments provided, patch those files
    args_len = len(sys.argv)
    if args_len > 1:
        for i in range(1, args_len):
            patch_file(sys.argv[i])
    else:
        # Profile-based behavior: sweep current directory for matching files
        logger.info("Scanning directory for files matching profile patterns...")
        patched_count = 0
        for filename in os.listdir("."):
            if should_patch_file(filename):
                patch_file(filename)
                patched_count += 1
        
        if patched_count == 0:
            logger.info("No files matched the profile patterns. Consider updating mobile_patch configuration.")
        else:
            logger.info(f"Processed {patched_count} files based on profile configuration.")
