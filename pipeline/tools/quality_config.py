#!/usr/bin/env python3
"""
quality_config.py — Basetract クオリティプロファイル管理ツール

使用方法:
  python3 tools/quality_config.py --show              現在のプロファイルと設定値を表示
  python3 tools/quality_config.py --list              利用可能な全プロファイルを一覧表示
  python3 tools/quality_config.py --set small         プロファイルを切り替え
  python3 tools/quality_config.py --set medium
  python3 tools/quality_config.py --set large
  python3 tools/quality_config.py --set custom
  python3 tools/quality_config.py --custom logic.critical_chars=60 ocr.confidence_min=0.75
  python3 tools/quality_config.py --compare           3プリセットの数値を横並び比較
  python3 tools/quality_config.py --export            現在の設定をJSONで標準出力

他のツール（quality_guard.py, hallucination_detector.py）から利用する場合:
  from tools.quality_config import get_active_profile
  profile = get_active_profile()
  critical_chars = profile['logic']['critical_chars']
"""

import json
import os
import sys
import argparse
from pathlib import Path
from copy import deepcopy

# ===== パス設定 =====
_SCRIPT_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _SCRIPT_DIR.parent
_PROFILES_PATH = _PROJECT_ROOT / "config" / "quality_profiles.json"


# ===== コアAPI =====

def load_config() -> dict:
    """quality_profiles.json を読み込む。破損JSONやアクセスエラーに完全対応。"""
    if not _PROFILES_PATH.exists():
        raise FileNotFoundError(
            f"quality_profiles.json が見つかりません: {_PROFILES_PATH}\n"
            f"config/ ディレクトリに quality_profiles.json を配置してください。"
        )
    
    try:
        with open(_PROFILES_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                raise ValueError("quality_profiles.json が空ファイルです")
            
            config = json.loads(content)
            
            # 設定構造の基本検証
            if not isinstance(config, dict):
                raise ValueError("quality_profiles.json のルート要素が辞書ではありません")
            
            if "profiles" not in config:
                raise ValueError("quality_profiles.json に 'profiles' キーがありません")
            
            if not isinstance(config["profiles"], dict):
                raise ValueError("'profiles' キーの値が辞書ではありません")
            
            if "active_profile" not in config:
                raise ValueError("quality_profiles.json に 'active_profile' キーがありません")
            
            if config["active_profile"] not in config["profiles"]:
                available = list(config["profiles"].keys())
                raise ValueError(f"アクティブプロファイル '{config['active_profile']}' が存在しません。利用可能: {available}")
            
            return config
            
    except json.JSONDecodeError as e:
        raise ValueError(f"quality_profiles.json のJSONフォーマットが破損しています (行 {e.lineno}, 列 {e.colno}): {e.msg}")
    except PermissionError:
        raise PermissionError(f"quality_profiles.json の読み込み権限がありません: {_PROFILES_PATH}")
    except OSError as e:
        raise OSError(f"quality_profiles.json の読み込み中にシステムエラーが発生しました: {e}")
    except Exception as e:
        raise RuntimeError(f"quality_profiles.json の読み込み中に予期せぬエラーが発生しました: {e}")


def save_config(config: dict) -> None:
    """quality_profiles.json を保存する。書き込みエラーに完全対応。"""
    try:
        # 設定構造の基本検証
        if not isinstance(config, dict):
            raise ValueError("保存する設定は辞書である必要があります")
        
        if "profiles" not in config:
            raise ValueError("設定に 'profiles' キーがありません")
        
        if "active_profile" not in config:
            raise ValueError("設定に 'active_profile' キーがありません")
        
        if config["active_profile"] not in config["profiles"]:
            available = list(config["profiles"].keys())
            raise ValueError(f"アクティブプロファイル '{config['active_profile']}' が存在しません。利用可能: {available}")
        
        # バックアップ作成
        backup_path = _PROFILES_PATH.with_suffix('.json.backup')
        if _PROFILES_PATH.exists():
            import shutil
            shutil.copy2(_PROFILES_PATH, backup_path)
        
        # 原子性書き込み（一時ファイル→リネーム）
        temp_path = _PROFILES_PATH.with_suffix('.json.tmp')
        try:
            with open(temp_path, "w", encoding="utf-8") as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
                f.flush()  # ディスクへの書き込みを強制
                os.fsync(f.fileno())  # ファイルシステム同期
            
            # 原子性リネーム
            os.replace(temp_path, _PROFILES_PATH)
            
        except Exception:
            # 一時ファイルが残っていたらクリーンアップ
            if temp_path.exists():
                temp_path.unlink()
            raise
            
    except PermissionError:
        raise PermissionError(f"quality_profiles.json の書き込み権限がありません: {_PROFILES_PATH}")
    except OSError as e:
        raise OSError(f"quality_profiles.json の保存中にシステムエラーが発生しました: {e}")
    except Exception as e:
        raise RuntimeError(f"quality_profiles.json の保存中に予期せぬエラーが発生しました: {e}")


def get_active_profile() -> dict:
    """
    現在アクティブなプロファイルの設定値を返す。
    quality_guard.py / hallucination_detector.py からインポートして使用する。

    返り値の例:
    {
      "name": "標準",
      "logic": {"critical_chars": 40, "recommended_chars": 100, ...},
      "schema": {"missing_keys_level": "error", ...},
      "ocr": {"confidence_min": 0.70, ...},
      "hallucination": {"keyword_match_required": True, ...}
    }
    """
    config = load_config()
    active = config.get("active_profile", "medium")
    profiles = config.get("profiles", {})
    if active not in profiles:
        print(f"[警告] active_profile '{active}' が見つかりません。'medium' にフォールバックします。",
              file=sys.stderr)
        active = "medium"
    return profiles[active]


def set_active_profile(profile_name: str) -> None:
    """アクティブなプロファイルを切り替える。"""
    config = load_config()
    valid = list(config["profiles"].keys())
    if profile_name not in valid:
        raise ValueError(f"無効なプロファイル名: '{profile_name}'. 有効な値: {valid}")
    config["active_profile"] = profile_name
    save_config(config)
    print(f"✅ プロファイルを '{profile_name}' ({config['profiles'][profile_name]['name_ja']}) に変更しました。")


def set_custom_value(key_path: str, value: str) -> None:
    """
    カスタムプロファイルの特定パラメータを設定する。
    key_path 例: 'logic.critical_chars', 'ocr.confidence_min'
    """
    config = load_config()
    param_defs = config.get("parameter_definitions", {})
    custom = config["profiles"]["custom"]

    if key_path not in param_defs:
        raise ValueError(
            f"不明なパラメータ: '{key_path}'\n"
            f"有効なパラメータ: {list(param_defs.keys())}"
        )

    param_def = param_defs[key_path]
    param_type = param_def.get("type", "string")
    parts = key_path.split(".")
    section, key = parts[0], parts[1]

    # 型変換
    if param_type == "integer":
        typed_value = int(value)
        min_v = param_def.get("min")
        max_v = param_def.get("max")
        if min_v is not None and typed_value < min_v:
            raise ValueError(f"{key_path}: 最小値は {min_v} です（入力値: {typed_value}）")
        if max_v is not None and typed_value > max_v:
            raise ValueError(f"{key_path}: 最大値は {max_v} です（入力値: {typed_value}）")
    elif param_type == "float":
        typed_value = float(value)
        min_v = param_def.get("min")
        max_v = param_def.get("max")
        if min_v is not None and typed_value < min_v:
            raise ValueError(f"{key_path}: 最小値は {min_v} です（入力値: {typed_value}）")
        if max_v is not None and typed_value > max_v:
            raise ValueError(f"{key_path}: 最大値は {max_v} です（入力値: {typed_value}）")
    elif param_type == "boolean":
        typed_value = value.lower() in ("true", "1", "yes", "on")
    elif param_type == "enum":
        valid_vals = param_def.get("values", [])
        if value not in valid_vals:
            raise ValueError(f"{key_path}: 有効な値は {valid_vals} です（入力値: '{value}'）")
        typed_value = value
    else:
        typed_value = value

    if section not in custom:
        custom[section] = {}
    custom[section][key] = typed_value
    save_config(config)
    print(f"✅ カスタム設定: {key_path} = {typed_value}")


# ===== 表示関数 =====

def _fmt_bool(v: bool) -> str:
    return "✅ 有効" if v else "❌ 無効"


def _fmt_level(v: str) -> str:
    return "🔴 ERROR（停止）" if v == "error" else "🟡 WARNING（継続）"


def print_profile(profile: dict, profile_name: str = "") -> None:
    """プロファイルの設定値を整形して表示する。"""
    label = f"[{profile_name}] " if profile_name else ""
    print(f"\n{'='*60}")
    print(f"  {label}{profile.get('name_ja', profile.get('name', ''))}")
    print(f"  {profile.get('description', '')}")
    print(f"{'='*60}")

    logic = profile.get("logic", {})
    print(f"\n📐 logicフィールド品質基準")
    print(f"  ・CRITICAL閾値（文字数）  : {logic.get('critical_chars', '—')} 文字")
    print(f"  ・推奨文字数              : {logic.get('recommended_chars', '—')} 文字")
    print(f"  ・技術的事実 最低個数     : {logic.get('tech_fact_min_count', '—')} 個")
    print(f"  ・公式引用バイパス        : {_fmt_bool(logic.get('official_excerpt_bypass', False))}")

    ocr = profile.get("ocr", {})
    print(f"\n🔍 OCR品質基準")
    print(f"  ・最低信頼スコア          : {ocr.get('confidence_min', '—')}")
    print(f"  ・最大許容ノイズ比率      : {ocr.get('noise_ratio_max', '—')}")

    schema = profile.get("schema", {})
    print(f"\n📋 スキーマ検証")
    print(f"  ・スキーマ不備の扱い      : {_fmt_level(schema.get('missing_keys_level', 'warning'))}")
    print(f"  ・answer-in-options必須   : {_fmt_bool(schema.get('answer_in_options_strict', True))}")

    hall = profile.get("hallucination", {})
    print(f"\n🧠 ハルシネーション検知")
    print(f"  ・キーワード照合必須      : {_fmt_bool(hall.get('keyword_match_required', False))}")
    print(f"  ・ソース追跡必須          : {_fmt_bool(hall.get('source_tracking_required', False))}")
    print()


def print_compare(config: dict) -> None:
    """3プリセットを横並びで比較表示する。"""
    profiles = config["profiles"]
    param_defs = config.get("parameter_definitions", {})
    presets = ["small", "medium", "large"]
    active = config.get("active_profile", "medium")

    header_names = {
        "small":  "ライト（S）",
        "medium": "標準（M）",
        "large":  "ストリクト（L）",
    }

    print(f"\n{'='*80}")
    print(f"  Basetract クオリティプロファイル 比較表")
    print(f"  ★ = 現在アクティブ")
    print(f"{'='*80}")
    print(f"  {'パラメータ':<35} {'ライト（S）':>14} {'標準（M）★' if active=='medium' else '標準（M）':>14} {'ストリクト（L）':>14}")
    print(f"  {'-'*35} {'-'*14} {'-'*14} {'-'*14}")

    for key_path, pdef in param_defs.items():
        label = pdef.get("label", key_path)
        # 省略して表示
        short_label = label[:33] + ".." if len(label) > 35 else label
        vals = []
        for p in presets:
            pdata = pdef.get("presets", {})
            v = pdata.get(p, "—")
            if isinstance(v, bool):
                v = "ON" if v else "OFF"
            marker = "★" if p == active else " "
            vals.append(f"{marker}{v}")
        print(f"  {short_label:<35} {vals[0]:>14} {vals[1]:>14} {vals[2]:>14}")

    print(f"\n  現在のアクティブプロファイル: [{active}] {profiles[active].get('name_ja', '')}")
    print()


def print_show(config: dict) -> None:
    """現在のアクティブプロファイルを表示する。"""
    active = config.get("active_profile", "medium")
    profiles = config.get("profiles", {})
    profile = profiles.get(active, {})
    print(f"\n現在のアクティブプロファイル: [{active}]")
    print_profile(profile, active)


def print_list(config: dict) -> None:
    """全プロファイルの一覧を表示する。"""
    active = config.get("active_profile", "medium")
    profiles = config.get("profiles", {})
    print(f"\n利用可能なプロファイル:")
    for name, prof in profiles.items():
        marker = "★ " if name == active else "  "
        print(f"  {marker}[{name}] {prof.get('name_ja', prof.get('name', ''))}")
    print(f"\n切り替えコマンド: python3 tools/quality_config.py --set <name>")


# ===== CLI エントリポイント =====

def main():
    parser = argparse.ArgumentParser(
        description="Basetract クオリティプロファイル管理ツール",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--show",    action="store_true", help="現在のプロファイルを表示")
    parser.add_argument("--list",    action="store_true", help="全プロファイルを一覧表示")
    parser.add_argument("--compare", action="store_true", help="3プリセットを横並び比較")
    parser.add_argument("--set",     metavar="PROFILE",   help="プロファイルを切り替え（small/medium/large/custom）")
    parser.add_argument("--custom",  nargs="+",           metavar="KEY=VALUE", help="カスタム値を設定（例: logic.critical_chars=60）")
    parser.add_argument("--export",  action="store_true", help="現在の設定をJSONで出力")

    args = parser.parse_args()

    # 引数なしの場合は --show と同等
    if not any([args.show, args.list, args.compare, args.set, args.custom, args.export]):
        args.show = True

    try:
        config = load_config()
    except FileNotFoundError as e:
        print(f"❌ エラー: {e}", file=sys.stderr)
        sys.exit(1)

    if args.set:
        try:
            set_active_profile(args.set)
        except ValueError as e:
            print(f"❌ エラー: {e}", file=sys.stderr)
            sys.exit(1)

    if args.custom:
        if config.get("active_profile") != "custom":
            print("ℹ️  カスタム値を設定するにはプロファイルを 'custom' に切り替えます...")
            set_active_profile("custom")
            config = load_config()
        for kv in args.custom:
            if "=" not in kv:
                print(f"❌ フォーマットエラー: '{kv}' は KEY=VALUE 形式で指定してください", file=sys.stderr)
                sys.exit(1)
            key, value = kv.split("=", 1)
            try:
                set_custom_value(key.strip(), value.strip())
            except (ValueError, KeyError) as e:
                print(f"❌ エラー: {e}", file=sys.stderr)
                sys.exit(1)
        config = load_config()

    if args.export:
        active = config.get("active_profile", "medium")
        profile = config["profiles"].get(active, {})
        print(json.dumps(profile, ensure_ascii=False, indent=2))
    elif args.compare:
        print_compare(config)
    elif args.list:
        print_list(config)
    elif args.show or args.set or args.custom:
        config = load_config()
        print_show(config)


if __name__ == "__main__":
    main()
