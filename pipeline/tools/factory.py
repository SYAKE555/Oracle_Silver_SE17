#!/usr/bin/env python3
"""
Basetract Project Factory
"""
import os
import shutil
import logging
import argparse
import sys
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# プロジェクトレジストリのパス（テンプレートルートの config/ に配置）
REGISTRY_FILENAME = "project_registry.json"


class Factory:
    """Project environment orchestration engine."""

    def __init__(self, template_dir: str, project_name: str, sync_mode: bool = False):
        self.template_dir = template_dir
        self.project_name = project_name
        self.sync_mode = sync_mode
        self.output_dir = os.path.join(os.getcwd(), project_name)

    def verify_templates(self) -> bool:
        """テンプレートの整合性チェック"""
        logger.info("Checking template integrity...")
        required = [
            "materials/unified_engine_template.html",
            "materials/basetract_core.js",
            "materials/loader.js",
            "launcher/web_launcher.py",
            "tools/quality_reporter.py",
            "pipeline/bootstrap.py",
            "system/app.py",
            "tools/quality_guard.py",
            "tools/ocr_engine.py",
            "tools/content_generator.py",
            "tools/history_manager.py",
        ]
        missing = [r for r in required if not os.path.exists(os.path.join(self.template_dir, r))]
        if missing:
            logger.error(f"Integrity failure: Missing files {missing}")
            return False
        logger.info("Template integrity check complete.")
        return True

    def initialize_project(self) -> bool:
        if not self.sync_mode:
            logger.info(f"Initializing new project environment: {self.project_name}")
            if not self.verify_templates():
                return False
            if os.path.exists(self.output_dir):
                logger.error(f"Directory already exists: {self.output_dir}")
                return False
            os.makedirs(self.output_dir)
        else:
            logger.info(f"Synchronizing infrastructure for: {self.project_name}")
            if not os.path.exists(self.output_dir):
                logger.error(f"Project directory missing: {self.output_dir}")
                return False
            if not self.verify_templates():
                return False

        # 1. ディレクトリ構造の生成
        subdirs = [
            "app/data", "pipeline/logs", "pipeline/tools",
            "docs", "config/skills", "materials/sources",
            "system", "launcher"
        ]
        for sd in subdirs:
            os.makedirs(os.path.join(self.output_dir, sd), exist_ok=True)

        # 2. ファイルマッピング（改善版ファイルを使用）
        mappings = [
            ("core/system_architecture.md",        "README.md"),
            ("materials/unified_engine_template.html", "index.html"),
            ("materials/mobile_engine_template.html",  "mobile.html"),
            ("materials/basetract_core.js",         "app/basetract_core.js"),
            ("materials/loader.js",                 "app/loader.js"),
            ("materials/ui_design_tokens.css",      "app/theme.css"),
            ("materials/sample_data.js",            "app/data/initial_state.js"),
            ("materials/lab_definition_template.json", "app/labs.json"),
            ("materials/analytics_schema.sql",      "app/data/analytics_schema.sql"),
            ("core/ai_skill_template.md",           "config/skills/maintainer/skill.md"),
            ("core/prompt.md",                      "docs/creation_prompt.md"),
            # Launchers（Flask対応版）
            ("launcher/web_launcher.py",            "launch_web.py"),
            ("launcher/desktop_launcher.py",        "launch_app.py"),
            # Backend（セキュリティ強化版に変更）
            ("system/app.py",              "app.py"),
            ("system/config.template.json",   "config.json"),
            # Docs & Pipeline（バージョン固定版・修正版に変更）
            ("docs/requirements.md",                "docs/requirements.md"),
            ("docs/specification.md",               "docs/technical_spec.md"),
            ("docs/substitution_guide.md",          "docs/substitution_guide.md"),
            ("docs/setup.md",                       "docs/setup.md"),
            ("pipeline/requirements_pinned.txt",    "pipeline/requirements.txt"),
            ("pipeline/bootstrap.py",         "pipeline/bootstrap.py"),
            # .env テンプレート
            ("config/secrets.template.env",         "config/secrets.template.env"),
        ]

        # 同期時にユーザーデータを保護するファイルリスト
        PROTECTED_ON_SYNC = {"app/data/initial_state.js"}

        for src, dst in mappings:
            src_path = os.path.join(self.template_dir, src)
            dst_path = os.path.join(self.output_dir, dst)

            if self.sync_mode and dst in PROTECTED_ON_SYNC and os.path.exists(dst_path):
                logger.info(f"Skipping protected file: {dst}")
                continue

            if os.path.exists(src_path):
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy2(src_path, dst_path)
                logger.info(f"Deployed: {dst}")
            else:
                logger.warning(f"Source missing (skipped): {src}")

        # 3. ツールチェーンの同期（改善版・統合版を使用）
        # 自動検知: tools/ 以下の全 .py ファイルを同期対象とする（fragility排除）
        tools_src_dir = os.path.join(self.template_dir, "tools")
        if os.path.exists(tools_src_dir):
            for tool_file in os.listdir(tools_src_dir):
                if tool_file.endswith(".py"):
                    src_path = os.path.join(tools_src_dir, tool_file)
                    dst_path = os.path.join(self.output_dir, "pipeline/tools", tool_file)
                    shutil.copy2(src_path, dst_path)
                    logger.info(f"Synchronized tool: {tool_file}")
        else:
            logger.warning("Tools directory missing in template, synchronization skipped.")

        # 4. テストスイートの同期
        test_files = [
            "tests/test_comprehensive.py",
            "tests/run_tests.py",
            "tests/requirements.txt"
        ]
        for test_file in test_files:
            src_path = os.path.join(self.template_dir, test_file)
            dst_path = os.path.join(self.output_dir, test_file)
            if os.path.exists(src_path):
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy2(src_path, dst_path)
                logger.info(f"Synchronized test: {test_file}")

        # 5. 監視システムの同期
        monitoring_files = [
            "tools/monitoring.py"
        ]
        for monitoring_file in monitoring_files:
            src_path = os.path.join(self.template_dir, monitoring_file)
            dst_path = os.path.join(self.output_dir, "pipeline/tools", monitoring_file.split('/')[-1])
            if os.path.exists(src_path):
                shutil.copy2(src_path, dst_path)
                logger.info(f"Synchronized monitoring: {monitoring_file}")

        # 6. プロジェクトレジストリを更新
        self._update_registry()

        logger.info(f"Orchestration complete: {self.output_dir}")
        return True

    def _update_registry(self) -> None:
        """全プロジェクトのメタ情報を project_registry.json に記録する。"""
        registry_dir = os.path.join(self.template_dir, "config")
        os.makedirs(registry_dir, exist_ok=True)
        registry_path = os.path.join(registry_dir, REGISTRY_FILENAME)

        try:
            if os.path.exists(registry_path):
                with open(registry_path, "r", encoding="utf-8") as f:
                    registry = json.load(f)
            else:
                registry = {"registry": []}
            
            if not isinstance(registry, dict):
                registry = {"registry": []}

            now = datetime.now().isoformat()
            projects = registry.get("registry", [])
            existing = next((p for p in projects if p.get("name") == self.project_name), None)

            if existing:
                existing["last_updated"] = now
                existing["status"] = "active"
            else:
                # 簡易的な問題数カウント（実査数値の反映）
                data_path = os.path.join(self.output_dir, "app/data/initial_state.js")
                if os.path.exists(data_path):
                    try:
                        import re
                        with open(data_path, 'r', encoding='utf-8') as df:
                            content = df.read()
                            # IDパターンを正規表現でカウント
                            q_count = len(re.findall(r'"id":\s*"[^"]+"', content))
                    except Exception as e:
                        logger.warning(f"Question count error: {e}")

                projects.append({
                    "name": self.project_name,
                    "path": self.output_dir,
                    "created_at": now,
                    "last_updated": now,
                    "status": "active",
                    "question_count": q_count,
                })
            registry["registry"] = projects

            with open(registry_path, "w", encoding="utf-8") as f:
                json.dump(registry, f, ensure_ascii=False, indent=2)
            logger.info(f"Registry updated: {registry_path}")
        except Exception as e:
            logger.warning(f"Registry update skipped: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basetract Project Factory")
    parser.add_argument("name", help="Project name")
    parser.add_argument("--sync", action="store_true", help="Sync infra without overwriting user data")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_root = os.path.abspath(os.path.join(script_dir, ".."))

    engine = Factory(template_root, args.name, sync_mode=args.sync)
    engine.initialize_project()
