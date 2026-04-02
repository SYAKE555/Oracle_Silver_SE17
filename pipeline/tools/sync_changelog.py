#!/usr/bin/env python3
"""
Basetract Changelog Synchronizer
Generates CHANGELOG.md from CHANGELOG.json to maintain a single source of truth.
"""
import json
import os

def sync():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(root_dir, 'CHANGELOG.json')
    md_path = os.path.join(root_dir, 'CHANGELOG.md')

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    md_content = "# Basetract 変更・修正履歴\n"
    md_content += "> **注意**: このファイルは CHANGELOG.json から自動生成されています。\n\n"

    for entry in data:
        version = entry.get('version', 'Unknown')
        date = entry.get('date', 'Unknown')
        title = entry.get('title', entry.get('description', 'Untitled'))
        
        md_content += f"## [{version}] — {date} — {title}\n"
        
        author = entry.get('author')
        if author:
            md_content += f"**実施者**: {author}\n"
            
        category = entry.get('category')
        if category:
            md_content += f"**種別**: {category}\n"
            
        md_content += "\n### 変更内容\n"
        
        changes = entry.get('changes', [])
        for change in changes:
            if isinstance(change, dict):
                comp = change.get('component', 'general')
                desc = change.get('description', '')
                detail = change.get('detail')
                md_content += f"- **{comp}**: {desc}\n"
                if detail:
                    md_content += f"  - {detail}\n"
            else:
                md_content += f"- {change}\n"
        
        verification = entry.get('verification')
        if verification:
            md_content += f"\n**検証結果**: {verification}\n"
            
        md_content += "\n---\n\n"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Successfully synchronized {md_path}")

if __name__ == "__main__":
    sync()
