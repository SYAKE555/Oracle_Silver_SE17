# 技術仕様書（Basetract）

> **重要**: 本仕様書はBasetractシステムの絶対的な技術基準です。全ての開発活動はこの仕様書に準拠する必要があります。
> **AI Agent Team参照**: AI Agent Teamによる開発の場合、必ず`docs/ai_agent_framework.md`、`docs/ai_agent_base_prompt.md`、`docs/ai_agent_creation_procedure.md`を併せて参照してください。

## 0. 適用範囲と絶対参照

### 0.1 目的
本仕様書は、Basetractインフラ基盤におけるデータ構造、品質基準、開発プロセスを定義する絶対的な基準文書です。

### 0.2 適用範囲
- 全ての学習システムプロジェクト
- 全てのデータ生成・変換プロセス
- 全ての品質保証活動
- **AI Agent Teamによる全開発活動**

### 0.3 絶対参照ドキュメント
- `docs/ai_agent_framework.md` - AI Agent Team設計フレームワーク
- `docs/ai_agent_base_prompt.md` - 各エージェントの基本プロンプトテンプレート
- `docs/ai_agent_creation_procedure.md` - AI Agent Team作成テンプレート手順
- `docs/ai_agent_example.md` - 実装例と実行フロー
- `docs/ai_agent_framework_analysis.md` - 設計分析と改善提案

### 0.4 AI Agent Team適用時の追加要件
AI Agent Teamによる開発の場合、以下の追加要件を遵守してください：
- 協調開発プロセスの実施
- 反復品質保証サイクルの適用
- 紛争解決メカニズムの遵守
- 標準化されたコミュニケーションプロトコルの使用

---

## 1. データスキーマ

### 1.1 問題データ (Basetract Full-Spec Schema)
各データセグメントは、情報の欠落を防ぐため、以下の12キー構造（dataBufferプロトコル）を完全に遵守する必要があります：
```javascript
window.dataBuffer = [
  {
    "id": "UNIQUE-ID",
    "category": "[Official Category]",
    "text": "設問（事実に基づく具体的な問い）",
    "type": "choice | text",
    "answer": "A. 正解のラベルと内容",
    "options": ["A. 選択肢1", "B. 選択肢2", "C. 選択肢3", "D. 選択肢4"],
    "logic": "100文字以上の技術的な詳細解説。ハルシネーションを防ぐため、数値や規格名を必須とする。",
    "plan": "不正解時の具体的学習プラン。",
    "weight": 0.1,
    "textbook_ref": ["対応する教科書の章番号"],
    "tags": ["タグ1", "タグ2"],
    "difficulty": "Easy | Medium | Hard"
  }
];
```

## 2. ディレクトリ構造規約
Basetractプロジェクトは、以下の4カテゴリ構造を守ることで、AIおよび人間の可読性を最大化します：

- `core/`: 基幹プロトコル、AIスキル定義、システム設計書。
- `materials/`: 教科書テンプレート、UIコンポーネント、初期スキーマ。
- `materials/sources/`: スキャン画像、写真などのOCR一次資料（生データ）。
- `tools/`: 自動化スクリプト本体（Factory, Guard, Crawler, Generator）。
- `docs/`: 運用マニュアル、要件定義、本仕様書。

## 3. 品質保証（QA）基準

### 3.1 技術的密度 (Technical Density)
- `logic` フィールドは、文字数（目安100文字）だけでなく、技術的キーワードの密度を重視すること。
- 40文字未満の極端な短文は不可。
- 短文であっても、プロトコル名、数値、コマンド等の具体的な「事実」が3つ以上含まれていれば合格とする。

### 3.2 ハルシネーション検知ルール
1. **存在チェック**: `answer` で指定されたラベルが、`options` 内に完全に一致して存在すること。
2. **キーワード照合**: `logic` 内に `answer` の主要キーワードが含まれていること。
3. **ソース追跡**: 自動生成されたデータは、必ずソースとなったURLまたは一次資料のリファレンスを持つこと。

## 4. 視覚情報（OCR）品質基準

### 4.1 抽出信頼性 (Confidence Score)
- `ocr_engine.py` が算出する信頼スコアが 0.7 未満の場合、ソースとして採用せず「要再撮影」の警告を出すこと。
- 文字の欠損（ノイズ比率 10% 以上）が検知された場合、後続の生成ステップを停止すること。

### 4.2 自己補完プロトコル (Self-Correction)
- 信頼スコア 0.7〜0.9 のデータについては、既存の技術コンテキストに基づき、AIが文脈から「欠損文字」を推測・補完することを許可する。
- 補完された箇所には必ず `[AUDITED]` タグを付与し、人間による最終確認の対象とすること。

## 5. ツールチェーン リファレンス

### 5.1 ツール一覧（pipeline/tools/）

| ツール | 役割 |
|---|---|
| `content_generator.py` | raw JSON → Basetract 12キースキーマ問題セグメント生成 |
| `ocr_engine.py` | Tesseract OCR + OpenAI Vision API によるスキャン画像→テキスト変換 |
| `quality_guard.py` | JS/JSON データファイルのスキーマ検証・粒度チェック |
| `hallucination_detector.py` | 正解整合性・logic 密度・スキーマ完全性の多層検証 |
| `quality_reporter.py` | プロジェクト全体の健全性スコアを `PROJECT_HEALTH.md` にレポート |
| `research_crawler.py` | 公式ドキュメント URL から技術データを収集（SSRF 保護付き） |
| `formatter.py` | 技術キーワードへの callout ブロック注入 |
| `mobile_patch.py` | 既存 HTML ファイルに Nuclear CSS を後付けでパッチ適用 |
| `factory.py` | テンプレートからプロジェクトを一括生成・同期するオーケストレーター |

### 5.2 推奨ワークフロー

```
materials/sources/ (スキャン画像)
    ↓ ocr_engine.py
pipeline/data_stage/ (raw JSON)
    ↓ research_crawler.py (URL取得時)
    ↓ content_generator.py
app/data/initial_state.js (12キースキーマ)
    ↓ quality_guard.py + hallucination_detector.py
    ↓ quality_reporter.py → PROJECT_HEALTH.md
app.py (Flask) → index.html / mobile.html
```

## 6. システムエンジン & UIロジック (Phase 24+)
Basetractは、静的なHTMLだけでなく、動的なバックエンド連携および高度なUI制御を備えています。

### 6.1 バックエンド・アーキテクチャ (Universal Engine)
- **構成**: Python/Flask + SQLite3。
- **配置**: `system/app.py`（展開後は各プロジェクトのルートに配置）。
- **責務**: API経由でのデータ提供、学習履歴の永続化、AIプロンプトの管理。
- **設定**: `system/config.json` により、ドメイン固有の情報（試験名、DB名、API制限）を一括管理する。

### 6.2 UI制御ロジック (Sidebar & Modal)
- **サイドバー管理**: `side-nav.collapsed` クラスによる動的な幅制御。PCでは作業スペースの確保、モバイルではオーバーフロー防止を目的とする。
- **インライン演習 (Mini-Quiz)**: `[data-quiz-id]` 属性を持つ要素をクリックすることで、`basetract_core.js` がオーバーレイModalを生成。教材を読みながら即座に知識をテスト可能。

## 7. セキュリティ・設定
- APIキー等の機密情報は `config/.env` で管理し、テンプレートやスクリプト内にはハードコードしないこと。
