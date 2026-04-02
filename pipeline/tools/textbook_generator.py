#!/usr/bin/env python3
"""
Basetract Textbook Generator for Oracle Silver SE 17
教材データ（initial_state.js）からドメイン別のスタティックHTML教科書を生成する。
"""

import json
import re
import logging
import os
from pathlib import Path
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


class TextbookGenerator:
    """教材データからHTML教科書を生成する。"""

    def __init__(self, data_path: str, output_dir: str = "textbooks"):
        self.data_path = data_path
        self.output_dir = output_dir
        self.questions = []
        self.domain_map = defaultdict(list)
        os.makedirs(output_dir, exist_ok=True)

    def load_data(self) -> bool:
        """initial_state.js（またはJSON）から教材データを読み込む。"""
        logger.info(f"Loading data from: {self.data_path}")
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # window.dataBuffer = [...]; 形式のJSファイルとJSONファイルに対応
            if self.data_path.endswith('.js'):
                match = re.search(r'window\.dataBuffer\s*=\s*(\[.*\])\s*;', content, re.DOTALL)
                if not match:
                    match = re.search(r'^\s*(\[.*\])\s*$', content, re.DOTALL)
                if not match:
                    logger.error("Could not locate window.dataBuffer or JSON array in JS file.")
                    return False
                data = json.loads(match.group(1))
            else:
                data = json.loads(content)

            if not isinstance(data, list):
                logger.error("Data must be a list of questions.")
                return False

            self.questions = data
            # ドメイン別に分類
            for q in self.questions:
                domain = q.get('category', 'Uncategorized')
                self.domain_map[domain].append(q)

            logger.info(f"Loaded {len(self.questions)} questions from {len(self.domain_map)} domains.")
            return True
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            return False

    def generate_domain_textbook(self, domain: str, questions: list) -> str:
        """ドメイン別教科書HTMLを生成する。"""
        domain_name = domain.replace("D", "").split("-")[0] if domain.startswith("D") else domain

        html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{domain} — Oracle Java Silver SE 17 教科書</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Noto Sans JP', 'Segoe UI', sans-serif;
            line-height: 1.8;
            color: #2c3e50;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
        }}
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        .meta {{
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        .meta-item {{
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
        }}
        .content {{
            padding: 40px;
        }}
        .toc {{
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin-bottom: 40px;
            border-radius: 4px;
        }}
        .toc h2 {{
            margin-bottom: 15px;
            color: #667eea;
        }}
        .toc ol {{
            margin-left: 20px;
        }}
        .toc li {{
            margin-bottom: 8px;
        }}
        .toc a {{
            color: #667eea;
            text-decoration: none;
            border-bottom: 1px dashed #667eea;
        }}
        .toc a:hover {{ color: #764ba2; }}

        .question-block {{
            margin-bottom: 50px;
            padding: 25px;
            border: 1px solid #e0e6ed;
            border-radius: 8px;
            background: #fafbfc;
            page-break-inside: avoid;
        }}
        .question-block h3 {{
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.3em;
        }}
        .question-meta {{
            display: flex;
            gap: 15px;
            margin-bottom: 15px;
            flex-wrap: wrap;
            font-size: 0.9em;
        }}
        .badge {{
            background: #667eea;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 600;
        }}
        .badge.easy {{ background: #27ae60; }}
        .badge.medium {{ background: #f39c12; }}
        .badge.hard {{ background: #e74c3c; }}

        .question-text {{
            background: white;
            padding: 15px;
            border-left: 4px solid #667eea;
            margin-bottom: 15px;
            border-radius: 4px;
            font-weight: 500;
        }}
        .question-text pre {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 12px;
            border-radius: 4px;
            overflow-x: auto;
            margin: 10px 0;
            font-size: 0.9em;
        }}

        .options {{
            margin-bottom: 15px;
        }}
        .options h4 {{
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1em;
        }}
        .option {{
            background: white;
            padding: 12px;
            margin-bottom: 8px;
            border-radius: 4px;
            border-left: 3px solid #bdc3c7;
        }}
        .option.correct {{
            border-left-color: #27ae60;
            background: #f0fdf4;
        }}
        .option.correct::before {{
            content: "✓ ";
            color: #27ae60;
            font-weight: bold;
        }}

        .answer {{
            background: #f0fdf4;
            border-left: 4px solid #27ae60;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 15px;
        }}
        .answer h4 {{
            color: #27ae60;
            margin-bottom: 8px;
        }}

        .logic {{
            background: #f3f4f6;
            border-left: 4px solid #8b5cf6;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 15px;
            line-height: 1.7;
        }}
        .logic h4 {{
            color: #8b5cf6;
            margin-bottom: 8px;
            font-size: 0.95em;
        }}

        .plan {{
            background: #eff6ff;
            border-left: 4px solid #3b82f6;
            padding: 15px;
            border-radius: 4px;
        }}
        .plan h4 {{
            color: #3b82f6;
            margin-bottom: 8px;
            font-size: 0.95em;
        }}

        .tags {{
            margin-top: 15px;
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .tag {{
            background: #e8eaf6;
            color: #3f51b5;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.85em;
        }}

        footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }}

        @media (max-width: 768px) {{
            header {{ padding: 40px 20px; }}
            header h1 {{ font-size: 1.8em; }}
            .content {{ padding: 20px; }}
            .question-block {{ padding: 15px; }}
        }}

        @media print {{
            body {{ background: white; }}
            .container {{ box-shadow: none; }}
            header {{ page-break-after: avoid; }}
            .question-block {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{domain}</h1>
            <p>Oracle Certified Java Programmer, Silver SE 17 (1Z0-825)</p>
            <div class="meta">
                <div class="meta-item">問題数: {len(questions)}</div>
                <div class="meta-item">難易度: 混合</div>
                <div class="meta-item">バージョン: v2.0.0</div>
            </div>
        </header>

        <div class="content">
            <div class="toc">
                <h2>目次</h2>
                <ol>
"""

        # 目次生成
        for i, q in enumerate(questions, 1):
            question_title = q.get('text', 'No title').split('\n')[0][:60]
            html += f'                    <li><a href="#q{i}">{question_title}...</a></li>\n'

        html += """                </ol>
            </div>
"""

        # 問題生成
        for i, q in enumerate(questions, 1):
            html += self._generate_question_html(q, i)

        html += """        </div>

        <footer>
            <p>© 2026 Basetract Oracle Silver Learning Platform</p>
            <p>本教科書はOracle認定試験（1Z0-825）対策用の学習教材です。</p>
        </footer>
    </div>
</body>
</html>
"""
        return html

    def _generate_question_html(self, question: dict, number: int) -> str:
        """1つの問題をHTML形式で生成する。"""
        difficulty = question.get('difficulty', 'Medium').lower()
        badge_class = f"badge {difficulty}"

        html = f"""            <div class="question-block" id="q{number}">
                <h3>問{number}: {question.get('id', 'Unknown')}</h3>

                <div class="question-meta">
                    <span class="{badge_class}">{difficulty.upper()}</span>
                    <span class="badge">カテゴリ: {question.get('category', 'N/A')}</span>
                </div>

                <div class="question-text">
"""

        # 問題文（コードがある場合は整形）
        text = question.get('text', '')
        if '```' in text:
            parts = text.split('```')
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    html += f"<p>{part.strip()}</p>\n"
                else:
                    html += f"<pre>{part.strip()}</pre>\n"
        else:
            html += f"<p>{text}</p>\n"

        html += """                </div>

                <div class="options">
                    <h4>選択肢</h4>
"""

        # 選択肢
        answer = question.get('answer', '')
        for option in question.get('options', []):
            is_correct = option == answer
            correct_class = "correct" if is_correct else ""
            html += f'                    <div class="option {correct_class}">{option}</div>\n'

        html += """                </div>

                <div class="answer">
                    <h4>正解</h4>
"""
        html += f"                    <p>{answer}</p>\n"
        html += """                </div>

                <div class="logic">
                    <h4>解説（技術的根拠）</h4>
"""
        logic = question.get('logic', '')
        html += f"                    <p>{logic}</p>\n"
        html += """                </div>

                <div class="plan">
                    <h4>不正解の場合の学習プラン</h4>
"""
        plan = question.get('plan', '')
        html += f"                    <p>{plan}</p>\n"
        html += """                </div>

                <div class="tags">
"""

        # タグ
        for tag in question.get('tags', []):
            html += f'                    <span class="tag">{tag}</span>\n'

        html += """                </div>
            </div>
"""
        return html

    def generate_all(self) -> bool:
        """全ドメインのHTML教科書を生成する。"""
        if not self.load_data():
            return False

        logger.info(f"Generating textbooks for {len(self.domain_map)} domains...")

        for domain, questions in sorted(self.domain_map.items()):
            domain_code = domain.split('-')[0] if '-' in domain else domain
            filename = f"{domain_code}_textbook.html"
            filepath = os.path.join(self.output_dir, filename)

            html_content = self.generate_domain_textbook(domain, questions)

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                logger.info(f"Generated: {filepath} ({len(questions)} questions)")
            except Exception as e:
                logger.error(f"Failed to write {filepath}: {e}")
                return False

        # インデックスHTMLも生成
        self._generate_index()

        logger.info(f"Textbooks generated in: {self.output_dir}")
        return True

    def _generate_index(self) -> str:
        """全教科書へのインデックスHTMLを生成する。"""
        index_html = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oracle Java Silver SE 17 教科書 — インデックス</title>
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
            margin-bottom: 60px;
        }
        header h1 { font-size: 2.5em; margin-bottom: 10px; }
        header p { font-size: 1.1em; opacity: 0.9; }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-decoration: none;
            color: inherit;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }
        .card h2 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.5em;
        }
        .card .count {
            font-size: 2em;
            color: #764ba2;
            font-weight: bold;
            margin: 15px 0;
        }
        .card .label {
            color: #666;
            font-size: 0.95em;
        }
        .card:hover h2 { color: #764ba2; }

        footer {
            text-align: center;
            color: white;
            margin-top: 60px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Oracle Java Silver SE 17</h1>
            <p>1Z0-825 認定試験対策 教科書</p>
        </header>

        <div class="grid">
"""

        for domain in sorted(self.domain_map.keys()):
            domain_code = domain.split('-')[0] if '-' in domain else domain
            domain_name = domain.split(' - ')[-1] if ' - ' in domain else domain
            question_count = len(self.domain_map[domain])
            filename = f"{domain_code}_textbook.html"

            index_html += f"""            <a href="{filename}" class="card">
                <h2>{domain_code}</h2>
                <div class="count">{question_count}</div>
                <div class="label">問題</div>
                <p>{domain_name}</p>
            </a>
"""

        index_html += """        </div>

        <footer>
            <p>© 2026 Basetract Oracle Silver Learning Platform</p>
            <p>本教科書はOracle認定試験（1Z0-825）対策用の学習教材です。</p>
        </footer>
    </div>
</body>
</html>
"""

        index_path = os.path.join(self.output_dir, "index.html")
        try:
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_html)
            logger.info(f"Generated index: {index_path}")
        except Exception as e:
            logger.error(f"Failed to write index: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 textbook_generator.py <data_file> [output_dir]")
        print("Example: python3 textbook_generator.py app/data/initial_state.js textbooks")
        sys.exit(1)

    data_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "textbooks"

    generator = TextbookGenerator(data_file, output_dir)
    success = generator.generate_all()
    sys.exit(0 if success else 1)
