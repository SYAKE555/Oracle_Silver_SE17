# Oracle DBA Silver SQL 教科書 変更履歴

## Ver 3.0（2026-04-01）

### 実施概要
- 既存版の欠点分析を先行し、是正方針に基づいて全面再構築。
- 単一HTML・CSS内包・JavaScript非依存の条件を維持。
- 16章すべてを「定義 / 役割 / 動作原理 / 制限事項 / 試験・実務の急所」で統一。

### ファイル管理
- 退避: `textbooks/old/Ver_2_0_Oracle_DBA_Silver_SQL_Textbook.html`
- 新規: `textbooks/Ver_3_0_Oracle_DBA_Silver_SQL_Textbook.html`
- 欠点レポート: `docs/Ver_3_0_Oracle_DBA_Silver_SQL_Defect_Report.md`

### 改修ポイント
1. 情報密度の強化
- 章内サブトピックを全網羅し、各トピックに品質5項目を固定配置。
- 章内に誤り例、チェックリスト、代表SQLを追加。

2. 初学者導線
- 章ごとに用語注釈（NULL、暗黙変換、最小権限など）を配置。
- 学習順と到達基準を導入部に明示。

3. UI/UX
- 左サイド固定目次（追従）で長文移動を改善。
- 章末トップ復帰リンクを標準装備。
- 目に優しいブルー/グレー基調、ライトコードテーマへ統一。

4. 図解
- 処理順フロー図、JOIN比較図、更新手順図、権限モデル図をHTML/CSSで実装。

5. ノイズ排除
- 学習者に不要な運用メタ情報を本文から除去。

### 関連リンク更新
- `textbooks/index.html` を Ver 3.0 へ更新
- `SETUP_GUIDE.md` / `docs/location_map.md` を Ver 3.0 参照へ更新

### 参照情報
- `01-02_ORACLE MASTER Silver SQL 2019_テキスト_unlocked.pdf`（ローカル参照）
- Oracle SQL Language Reference 19c/21c（構文確認）
