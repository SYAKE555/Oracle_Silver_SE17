#!/usr/bin/env python3
"""
Basetract Textbook Builder — Oracle Silver SE 17
問題DBの「logic」と「plan」を逆算して、0からJavaを学べる教科書を生成する。

設計原理：
1. 各問題の「logic」→ その概念の「説明」
2. 各問題の「plan」→ その概念の「学習手順」
3. 問題を解くだけで自動的に理解できる体系
4. バカでもわかるシンプルさ
"""

import json
import re
import os
import logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


class TextbookBuilder:
    """品質検証ロジックから教科書を生成する。"""

    def __init__(self, data_path: str, output_dir: str = "textbooks"):
        self.data_path = data_path
        self.output_dir = output_dir
        self.questions = []
        self.concepts = defaultdict(list)  # 概念ごとに問題をグループ化
        os.makedirs(output_dir, exist_ok=True)

    def load_data(self) -> bool:
        """教材データを読み込む。"""
        logger.info(f"Loading: {self.data_path}")
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if self.data_path.endswith('.js'):
                match = re.search(r'window\.dataBuffer\s*=\s*(\[.*\])\s*;', content, re.DOTALL)
                if not match:
                    match = re.search(r'^\s*(\[.*\])\s*$', content, re.DOTALL)
                if not match:
                    logger.error("Could not locate data buffer.")
                    return False
                data = json.loads(match.group(1))
            else:
                data = json.loads(content)

            self.questions = data
            # タグで概念をグループ化
            for q in self.questions:
                for tag in q.get('tags', []):
                    self.concepts[tag].append(q)

            logger.info(f"Loaded {len(self.questions)} questions, {len(self.concepts)} concepts")
            return True
        except Exception as e:
            logger.error(f"Failed to load: {e}")
            return False

    def extract_concept_from_logic(self, logic: str) -> str:
        """logicテキストから概念の要約を抽出する。"""
        # 最初の100文字以内の重要表現を拾う
        lines = logic.split('。')
        if lines:
            return lines[0].strip()
        return logic[:80]

    def generate_chapter(self, chapter_name: str, questions: list) -> str:
        """章単位のHTML生成。"""
        html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter_name} — Oracle Java Silver 教科書</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Noto Sans JP', 'Segoe UI', sans-serif;
            line-height: 1.8;
            color: #333;
            background: #f5f7fa;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 40px;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 30px;
            font-size: 2em;
        }}
        h2 {{
            color: #34495e;
            margin-top: 40px;
            margin-bottom: 15px;
            font-size: 1.4em;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}
        h3 {{
            color: #2c3e50;
            margin-top: 25px;
            margin-bottom: 10px;
            font-size: 1.1em;
        }}

        .concept {{
            background: #ecf0f1;
            border-left: 4px solid #3498db;
            padding: 20px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .concept strong {{
            color: #2980b9;
            font-size: 1.1em;
        }}

        .explanation {{
            background: #f9f9f9;
            border-left: 4px solid #27ae60;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
            line-height: 1.7;
        }}
        .explanation p {{
            margin-bottom: 10px;
        }}

        .learning-steps {{
            background: #e8f8f5;
            border: 1px solid #27ae60;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }}
        .learning-steps h4 {{
            color: #27ae60;
            margin-bottom: 10px;
        }}
        .learning-steps ol {{
            margin-left: 20px;
        }}
        .learning-steps li {{
            margin-bottom: 8px;
            line-height: 1.6;
        }}

        .example {{
            background: #fff3cd;
            border: 1px dashed #ffc107;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
            font-size: 0.95em;
        }}
        .example strong {{
            color: #856404;
        }}

        .key-point {{
            background: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 12px 15px;
            margin: 15px 0;
            border-radius: 4px;
            font-weight: 500;
            color: #721c24;
        }}

        code {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}

        pre {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            margin: 15px 0;
            font-size: 0.85em;
            line-height: 1.5;
        }}

        .reference {{
            background: #e7f3ff;
            border: 1px solid #0066cc;
            padding: 10px 15px;
            margin: 15px 0;
            border-radius: 4px;
            font-size: 0.9em;
        }}
        .reference strong {{
            color: #0066cc;
        }}

        footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: #999;
            font-size: 0.9em;
        }}

        @media (max-width: 768px) {{
            .container {{ padding: 20px; }}
            h1 {{ font-size: 1.5em; }}
            h2 {{ font-size: 1.2em; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{chapter_name}</h1>
        <p style="color: #666; margin-bottom: 30px; font-size: 1.05em;">
            この教科書は、問題を解くだけで理解できるように設計されています。<br>
            各セクションの学習ステップに沿って、順番に読んでください。
        </p>
"""

        # 概念ごとのセクション生成
        concepts_set = set()
        for q in questions:
            for tag in q.get('tags', []):
                concepts_set.add(tag)

        for concept in sorted(concepts_set):
            concept_questions = [q for q in questions if concept in q.get('tags', [])]
            html += self._generate_concept_section(concept, concept_questions)

        html += """        <footer>
            <p>© 2026 Basetract Oracle Silver Learning Platform</p>
            <p>本教科書は Oracle Certified Java Programmer, Silver SE 17 (1Z0-825) 試験対策用です。</p>
        </footer>
    </div>
</body>
</html>
"""
        return html

    def _generate_concept_section(self, concept: str, questions: list) -> str:
        """概念ごとのセクション生成。"""
        html = f"""        <h2>{concept}</h2>
"""

        # 概念の説明（最初の問題のlogicから抽出）
        if questions:
            first_logic = questions[0].get('logic', '')
            summary = self.extract_concept_from_logic(first_logic)

            html += f"""        <div class="concept">
            <strong>概念:</strong> {concept}
        </div>

        <div class="explanation">
            <p><strong>説明:</strong></p>
            <p>{summary}</p>
        </div>
"""

        # 各問題ごとのセクション
        for q in questions:
            html += self._generate_problem_explanation(q)

        return html

    def _generate_problem_explanation(self, q: dict) -> str:
        """問題ごとの説明セクション。"""
        text = q.get('text', '')
        logic = q.get('logic', '')
        plan = q.get('plan', '')
        answer = q.get('answer', '')
        problem_id = q.get('id', '')

        # 問題文の整形
        text_short = text.split('\n')[0][:80]

        html = f"""        <h3>{problem_id}: {text_short}...</h3>

        <div class="explanation">
            <p><strong>重要なポイント:</strong></p>
            <p>{logic}</p>
        </div>

        <div class="learning-steps">
            <h4>📚 学習プラン</h4>
            <ol>
                <li>{plan}</li>
            </ol>
        </div>

        <div class="key-point">
            ✓ 正解: {answer}
        </div>

"""
        return html

    def generate_all(self) -> bool:
        """全ドメイン別教科書を生成。"""
        if not self.load_data():
            return False

        # ドメインごとにグループ化
        domains = defaultdict(list)
        for q in self.questions:
            domain = q.get('category', 'Other')
            domain_code = domain.split('-')[0] if '-' in domain else domain
            domains[domain_code].append(q)

        logger.info(f"Generating {len(domains)} domain textbooks...")

        for domain_code in sorted(domains.keys()):
            questions = domains[domain_code]
            domain_full = questions[0].get('category', domain_code) if questions else domain_code

            filename = f"{domain_code}_tutorial.html"
            filepath = os.path.join(self.output_dir, filename)

            html_content = self.generate_chapter(domain_full, questions)

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                logger.info(f"Generated: {filepath} ({len(questions)} problems)")
            except Exception as e:
                logger.error(f"Failed to write {filepath}: {e}")
                return False

        self._generate_master_index(domains)
        logger.info(f"Textbooks generated in: {self.output_dir}")
        return True

    def _generate_master_index(self, domains: dict) -> None:
        """マスターインデックスHTML生成。"""
        index_html = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oracle Java Silver SE 17 学習ガイド</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Noto Sans JP', 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        header {
            text-align: center;
            color: white;
            margin-bottom: 50px;
        }
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.05em;
            opacity: 0.95;
        }

        .intro-box {
            background: white;
            border-radius: 8px;
            padding: 30px;
            margin-bottom: 40px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .intro-box h2 {
            color: #667eea;
            margin-bottom: 15px;
        }
        .intro-box p {
            color: #555;
            line-height: 1.8;
            margin-bottom: 10px;
        }

        .chapters {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .chapter-card {
            background: white;
            border-radius: 8px;
            padding: 25px;
            text-decoration: none;
            color: inherit;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border-top: 4px solid #667eea;
        }
        .chapter-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            border-top-color: #764ba2;
        }
        .chapter-card h3 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.3em;
        }
        .chapter-card .count {
            color: #999;
            font-size: 0.9em;
        }
        .chapter-card p {
            color: #666;
            font-size: 0.95em;
            margin-top: 10px;
        }

        footer {
            text-align: center;
            color: white;
            font-size: 0.9em;
            margin-top: 60px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Oracle Java Silver SE 17</h1>
            <p>1Z0-825 認定試験対策 学習ガイド</p>
        </header>

        <div class="intro-box">
            <h2>このガイドについて</h2>
            <p>
                このガイドは、<strong>0からJavaを学べる</strong>ように設計されています。
            </p>
            <p>
                各章は、実際の試験問題の「正解根拠」と「学習プラン」から構成されています。
                つまり、<strong>問題を解くだけで自動的に理解できる</strong>仕組みになっています。
            </p>
            <p>
                <strong>推奨学習順序:</strong>
            </p>
            <ol style="margin: 15px 0 0 20px; color: #555;">
                <li><strong>D1</strong> → Javaプログラムの基本構造</li>
                <li><strong>D2</strong> → データ型と文字列操作</li>
                <li><strong>D3</strong> → 演算子と制御構造</li>
                <li><strong>D4</strong> → クラスとオブジェクト指向</li>
                <li><strong>D5</strong> → 継承とインタフェース</li>
                <li><strong>D6</strong> → 例外処理</li>
            </ol>
        </div>

        <div class="chapters">
"""

        for domain_code in sorted(domains.keys()):
            questions = domains[domain_code]
            domain_full = questions[0].get('category', domain_code) if questions else domain_code
            domain_name = domain_full.split('-')[-1].strip() if '-' in domain_full else domain_full
            filename = f"{domain_code}_tutorial.html"

            index_html += f"""            <a href="{filename}" class="chapter-card">
                <h3>{domain_code}</h3>
                <p>{domain_name}</p>
                <div class="count">{len(questions)}個の学習ポイント</div>
            </a>
"""

        index_html += """        </div>

        <footer>
            <p>© 2026 Basetract Oracle Silver Learning Platform</p>
            <p>このガイドは Oracle Certified Java Programmer, Silver SE 17 (1Z0-825) 試験対策用です。</p>
        </footer>
    </div>
</body>
</html>
"""

        index_path = os.path.join(self.output_dir, "index.html")
        try:
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_html)
            logger.info(f"Generated master index: {index_path}")
        except Exception as e:
            logger.error(f"Failed to write index: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 textbook_builder.py <data_file> [output_dir]")
        print("Example: python3 textbook_builder.py app/data/initial_state.js textbooks_tutorials")
        sys.exit(1)

    data_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "textbooks_tutorials"

    builder = TextbookBuilder(data_file, output_dir)
    success = builder.generate_all()
    sys.exit(0 if success else 1)
