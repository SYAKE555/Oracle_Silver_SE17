#!/usr/bin/env python3
import json
import os
import argparse
from datetime import datetime
from pathlib import Path

# centralized import manager を使用
from import_manager import import_profile_loader
profile_loader = import_profile_loader()

class HistoryManager:
    def __init__(self, json_path: str):
        self.json_path = Path(json_path)
        self.history = self._load()

    def _load(self):
        if self.json_path.exists():
            with open(self.json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def _save(self):
        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def check_content(self, text: str):
        """禁止語彙が含まれていないかチェックする"""
        forbidden = profile_loader.get_profile_value("logic", "forbidden_words", [])
        found = [word for word in forbidden if word in text]
        if found:
            raise ValueError(f"禁止語彙が検出されました: {found}")

    def add_entry(self, version, title, category, author, changes, verification=None):
        # バリデーション
        self.check_content(title)
        for change in changes:
            self.check_content(change.get("description", ""))
            self.check_content(change.get("detail", ""))
        
        entry = {
            "version": version,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "title": title,
            "author": author,
            "category": category,
            "changes": changes,
            "verification": verification
        }
        self.history.insert(0, entry)  # 最新を先頭に
        self._save()
        print(f"Added entry for {version}")

    def generate_markdown(self, md_path):
        """JSONからMarkdownを生成する"""
        lines = ["# Basetract 変更・修正履歴\n", "> **注意**: このファイルは CHANGELOG.json から自動生成されています。\n\n"]
        
        for entry in self.history:
            lines.append(f"## [{entry['version']}] — {entry['date']} — {entry['title']}\n")
            lines.append(f"**実施者**: {entry.get('author', 'Unknown')}\n")
            lines.append(f"**種別**: {entry.get('category', 'General')}\n\n")
            
            lines.append("### 変更内容\n")
            for change in entry.get("changes", []):
                lines.append(f"- **{change['component']}**: {change['description']}\n")
                if change.get('detail'):
                    lines.append(f"  - {change['detail']}\n")
            
            if entry.get("verification"):
                lines.append(f"\n**検証結果**: {entry['verification']}\n")
            
            lines.append("\n---\n\n")

        with open(md_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Generated Markdown: {md_path}")

def main():
    parser = argparse.ArgumentParser(description="Basetract History Manager")
    parser.add_argument("--json", default="CHANGELOG.json", help="Path to CHANGELOG.json")
    parser.add_argument("--generate-md", help="Output path for Markdown (e.g. CHANGELOG.md)")
    
    args = parser.parse_args()
    manager = HistoryManager(args.json)

    if args.generate_md:
        manager.generate_markdown(args.generate_md)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
