# Oracle DBA Silver SQL 教科書 改修レポート

## Ver 2.0（2026-04-01）

### 実施したファイル管理
- 旧版を退避:
  - `textbooks/old/Ver_1_0_Oracle_DBA_Silver_SQL_Textbook.html`
- 新版を作成:
  - `textbooks/Ver_2_0_Oracle_DBA_Silver_SQL_Textbook.html`

### Ver 1.0 の欠点に対する対応
1. はじめに不足
- 導入セクションを追加し、目的・学習到達基準・使い方を明示。

2. 目次ジャンプ不可
- 章ID（`#ch1`〜`#ch16`）と目次アンカーリンクを実装。
- 各章末に「▲ 目次へ戻る」を追加。

3. 学習を阻害するメタ情報
- 教材本文から不要なメタ説明（インポート参照表現等）を排除。

4. 解説の薄さ
- 全16章を「役割 / 動作原理 / 制限事項 / 試験急所 / 実務ケース / 例題SQL」で統一。

5. 図解不足
- 処理順フロー図（SELECT処理順）
- JOIN差分表（INNER/LEFT）
- 更新手順フロー（件数確認→SAVEPOINT→更新→差分確認→確定/取消）

6. 試験対策不足
- 各章にひっかけポイントを明示（NULL比較、演算子優先順位、暗黙変換など）。

7. 可読性
- ブルー/グレー基調へ配色変更。
- コード背景をライト化し、スマホ屋外でも判読性を改善。
- 表は `overflow-x:auto` で横スクロール可能化。

### 仕様適合
- 単一HTML（CSS内包）
- PC/スマホ対応
- JavaScript非依存（`<script>`未使用）

### 反映済み関連リンク
- `textbooks/index.html` を Ver 2.0 へ更新
- `SETUP_GUIDE.md` / `docs/location_map.md` の参照を Ver 2.0 に更新

### 参照した公式情報（Oracle）
- Oracle Database SQL Language Reference 19c
  - https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/
- Oracle Database SQL Language Reference 21c: GRANT
  - https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/GRANT.html
- Oracle Database SQL Language Reference 21c: REVOKE
  - https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/REVOKE.html
- Oracle Database SQL Language Reference 21c: Data Types
  - https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html
- Oracle Database Reference 21c: ALL_TAB_COLUMNS
  - https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_COLUMNS.html
