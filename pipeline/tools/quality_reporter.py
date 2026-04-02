#!/usr/bin/env python3
# ← 互換性修正: dict[str, list] の Python 3.9+ 構文を 3.8 以前でも動作させる
from __future__ import annotations
"""
Basetract Quality Reporter — Fixed Version
修正点:
  - from quality_guard import QualityGuard がカレントディレクトリ依存だったバグを修正
    → sys.path に自身のディレクトリを追加することで、どこから実行しても動作する
  - generate_report() のレポート出力先をスクリプト引数または実行元ディレクトリに変更
  - タイムスタンプを report に追加
  - 警告と致命的エラーを分けて集計する
"""
import os
import sys
import json
import logging
from datetime import datetime

# 同一ディレクトリ内の quality_guard を確実にimportできるようパスを追加
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quality_guard import QualityGuard

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# 中央化インポートマネージャーを使用
from import_manager import import_profile_loader
profile_loader = import_profile_loader()
from profile_loader import load_quality_profile

_PROFILE = load_quality_profile()


class QualityReporter:
    """Basetract プロジェクト全体の品質を集計・レポートするツール。"""

    def __init__(self, data_dir: str = "app/data", report_dir: str = "."):
        self.data_dir = data_dir
        self.report_dir = report_dir
        self.total_segments = 0
        self.passed_segments = 0
        self.critical_errors: dict[str, list] = {}   # 致命的エラー（スキーマ違反等）
        self.advisory_errors: dict[str, list] = {}   # 品質勧告（logic密度等）

    def run_aggregate_audit(self) -> None:
        logger.info(f"Initiating global health scan: {self.data_dir}")
        if not os.path.exists(self.data_dir):
            logger.error(f"Data directory not found: {self.data_dir}")
            return

        # プロファイルから閾値を取得
        logic_cfg = _PROFILE.get("logic", {})
        schema_cfg = _PROFILE.get("schema", {})
        critical_chars = logic_cfg.get("critical_chars", 40)
        recommended_chars = logic_cfg.get("recommended_chars", 100)
        tech_fact_min = logic_cfg.get("tech_fact_min_count", 3)
        schema_level = schema_cfg.get("missing_keys_level", "error")

        for root, _, files in os.walk(self.data_dir):
            for file in sorted(files):
                # sample.js と analytics_schema.sql は対象外
                if not file.endswith(('.js', '.json')):
                    continue
                if file in ('sample.js', 'analytics_schema.sql'):
                    continue

                path = os.path.join(root, file)
                guard = QualityGuard(path)
                if not guard.validate_structure():
                    self.critical_errors[file] = guard.errors
                    continue

                if not (isinstance(guard.data, list) and guard.data and isinstance(guard.data[0], dict)):
                    continue

                guard.validate_granularity()
                self.total_segments += len(guard.data)

                # プロファイルベースのエラー分類
                critical = []
                advisory = []
                
                for error in guard.errors:
                    error_lower = error.lower()
                    
                    # スキーマエラーはプロファイル設定に従って分類
                    if 'missing' in error_lower or 'schema' in error_lower:
                        if schema_level == "error":
                            critical.append(error)
                        else:
                            advisory.append(error)
                    # CRITICAL閾値違反は致命的エラー
                    elif f"{critical_chars} chars minimum" in error or f"{tech_fact_min} technical facts required" in error:
                        critical.append(error)
                    # それ以外は品質勧告
                    else:
                        advisory.append(error)

                if critical:
                    self.critical_errors[file] = critical
                if advisory:
                    self.advisory_errors[file] = advisory

                if not guard.errors:
                    self.passed_segments += len(guard.data)

        self.generate_report()

    def generate_report(self) -> None:
        os.makedirs(self.report_dir, exist_ok=True)
        report_path = os.path.join(self.report_dir, "PROJECT_HEALTH.md")
        health = (self.passed_segments / self.total_segments * 100) if self.total_segments > 0 else 0.0
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# Basetract Health Report\n\n")
            f.write(f"**Generated**: {timestamp}\n\n")
            f.write(f"## Overall Stats\n\n")
            f.write(f"- **Total Segments**: {self.total_segments}\n")
            f.write(f"- **Passed Segments**: {self.passed_segments}\n")
            f.write(f"- **Health Index**: {health:.1f}%\n\n")

            if self.critical_errors:
                f.write(f"## Critical Defects ({sum(len(v) for v in self.critical_errors.values())} issues)\n\n")
                for fname, errors in self.critical_errors.items():
                    f.write(f"### `{fname}`\n")
                    for err in errors:
                        f.write(f"- [ ] **[CRITICAL]** {err}\n")
                    f.write("\n")
            else:
                f.write("## Critical Defects\n\nNone. All schemas validated.\n\n")

            if self.advisory_errors:
                f.write(f"## Quality Advisories ({sum(len(v) for v in self.advisory_errors.values())} items)\n\n")
                for fname, errors in self.advisory_errors.items():
                    f.write(f"### `{fname}`\n")
                    for err in errors:
                        f.write(f"- [ ] {err}\n")
                    f.write("\n")

            status = "PROTECTED" if not self.critical_errors else "DEGRADED"
            f.write(f"---\n**System Status**: {status}\n")

        logger.info(f"Report generated: {report_path} (Health: {health:.1f}%)")


if __name__ == "__main__":
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "app/data"
    report_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    reporter = QualityReporter(data_dir=data_dir, report_dir=report_dir)
    reporter.run_aggregate_audit()
