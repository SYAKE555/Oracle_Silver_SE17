# コンポーネント代用・変更手順書 (Substitution Guide)

Basetractは「中立的な基盤」であるため、特定の技術に依存せず、ニーズに応じて構成部品を交換することが可能です。以下に主要な代用手段と変更手順を記載します。

## 1. 自動化エンジン (Python) の代用
Python以外で自動化ロジックを再構築する場合。

- **代用候補**: Node.js (TypeScript), Rust, Go
- **変更手順**:
    1. `tools/` 配下のスクリプトを入出力仕様（Specification.md）に合わせて他言語で再実装。
    2. 生成されるデータ形式（window.dataBuffer）さえ維持すれば、フロントエンド（HTML/JS）の変更は不要です。

## 2. AIレビュー / 生成エンジンの代用
高コストなAPIを避けたい、またはオフライン環境で使用したい場合。

- **代用候補**:
    - **Local LLMs**: Llama-3, Mistral, Gemma 2 (LM Studio や Ollama 経由)
    - **別API**: OpenAI ↔ Anthropic ↔ Google Gemini (互換プロンプトを使用)
- **変更手順**:
    1. `config/.env` のエンドポイント情報を書き換え。
    2. `tools/` 内の通信用関数（requests等）を各モデルのSDKに変更。

## 3. ストレージ層の代用
JSON/JSファイル形式から、より大規模な管理へ移行する場合。

- **代用候補**: SQLite, PostgreSQL, MongoDB
- **変更手順**:
    1. `materials/loader.js` を Fetch API ベースに変更し、DB API エンドポイントを叩くよう修正。
    2. `tools/unified_generator.py` の出力をファイル書き出しから SQL `INSERT` 文に変更（旧: `segment_generator.py` は `unified_generator.py` に統合済み）。

## 4. フロントエンド・ライブラリの代用
Mermaid.js以外の図解ツールを使用したい場合や、別のCSSフレームワーク（Tailwind等）を導入したい場合。

- **代用候補**: PlantUML, D3.js, Tailwind CSS, Bootstrap
- **変更手順**:
    1. `materials/unified_engine_template.html` の `<script>` や `<link>` タグで新しいライブラリをロード。
    2. 新規スタイルを適用。

## 5. 監視・オーディット機能の拡張
Basetractの品質監視（Quality Reporter）を拡張または他システムと連携させる場合。

- **代用候補**: Prometheus, Grafana, カスタムダッシュボード
- **変更手順**:
    1. `tools/quality_reporter.py` の JSON 出力を拡張。
    2. 他の監視基盤（例: OPENClaw等）から `PROJECT_HEALTH.md` をクロール・監視対象に追加。
    3. `launch_web.py` / `launch_app.py` のエントリーポイントを変更し、監視ダッシュボードを初期画面に設定。

---
> [!IMPORTANT]
> **変更の黄金律**: どのコンポーネントを交換しても、システム全体の整合性は以下の２点が守られている限り維持されます。
> 1. `core/specification.md` で定義された「12キー・データ構造」と「品質基準」を破壊しないこと。
> 2. **Mobile Responsive Layout（スマホでの横幅強制100%制御 / `!important` 指定の Nuclear CSS）の削除・上書き禁止。** いかなるUI拡張を行っても、モバイル環境でのレイアウト崩壊はBasetractの根幹仕様への違反となります。
