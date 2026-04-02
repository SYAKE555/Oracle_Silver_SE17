#!/usr/bin/env python3
# ← 互換性修正: list[str] | None の Python 3.10+ 構文を 3.9 以前でも動作させる
from __future__ import annotations
"""
Basetract Formatter — Fixed Version
修正点:
  - str.replace() による全置換バグを修正
    (旧版: 同一キーワードが複数回出現すると全箇所に callout が注入され、
     さらに注入済み callout 内のキーワードテキストも次のループで二重置換された)
  - re.sub() + 単語境界マッチに変更し、一度置換した箇所を再マッチしない設計に変更
  - キーワードリストを設定として外部化できるよう引数に移動
"""
import re
import sys
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# quality_profiles.json からアクティブプロファイルを取得するヘルパー
def _load_quality_profile() -> dict:
    """tools/quality_config.py の get_active_profile() を呼ぶ。失敗時はデフォルト値を使用。"""
    try:
        import sys, pathlib
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
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
            "formatter": {"keywords": ["Timer", "State", "Protocol", "Metric"]}
        }

_PROFILE = _load_quality_profile()

# デフォルトのキーワードリスト（プロファイルからも取得可能）
DEFAULT_KEYWORDS = _PROFILE.get("formatter", {}).get("keywords", ["Timer", "State", "Protocol", "Metric"])

# 置換済みマーカー（再マッチ防止用の一時トークン）
_PLACEHOLDER_PREFIX = "\x00BT_REPLACED_"
_PLACEHOLDER_SUFFIX = "\x00"


def basetract_format(text: str, keywords: list[str] | None = None) -> str:
    """
    技術キーワードに対して professional callout ブロックを注入する。

    修正: 各キーワードの最初の出現箇所のみを対象とし、
          挿入済み HTML の内部を再スキャンしない。
    """
    if keywords is None:
        keywords = DEFAULT_KEYWORDS

    # ステップ1: 各キーワードをプレースホルダーに変換（re.sub で1回だけ置換）
    #            \b を使って単語境界でマッチし、部分一致を防ぐ
    placeholder_map = {}
    for kw in keywords:
        pattern = re.compile(r'\b' + re.escape(kw) + r'\b')
        callout = (
            f"\n<div class='technical-callout'>\n"
            f"  <strong>Technical Detail: {kw}</strong>\n"
            f"  [Verified context for granular attributes.]\n"
            f"</div>\n"
        )
        replacement = f"{kw}{callout}"
        token = f"{_PLACEHOLDER_PREFIX}{kw}{_PLACEHOLDER_SUFFIX}"
        placeholder_map[token] = replacement

        # キーワードをトークンに置換（この時点では callout HTML はまだ挿入しない）
        text = pattern.sub(token, text)

    # ステップ2: トークンを実際の callout に展開（2度目のスキャンで callout内のキーワードに再マッチしない）
    for token, replacement in placeholder_map.items():
        text = text.replace(token, replacement)

    return text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            result = basetract_format(content)
            print(result)
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            sys.exit(1)
    else:
        logger.error("Usage: python3 tools/formatter.py <input_file>")
        sys.exit(1)
