# Oracle DBA Silver SQL 学習用HTML 改修レポート

## Ver 1.1（2026-04-01）

### 1. Ver 1.0 の欠点（ユーザー指摘）
- テーマカラーが強すぎて長時間学習に不向き
- ライト背景とダークコードのコントラスト差が大きく視覚疲労が強い
- 見出しが `div` のみで、文書構造がセマンティックでない
- 長文ページに対して移動導線が弱い（トップ復帰・クイック移動不足）
- 実務ケースが末尾集中で、章本文との学習往復がしづらい
- 後半章の実務文脈が薄い

### 2. Ver 1.1 で実施した改修
- 配色を学習向けブルー系へ再設計（視認性・疲労軽減）
- SQLコード背景をライト化し、本文との輝度差を縮小
- 章見出しを `h2`、小見出しを `h3` に変更（構造化）
- 先頭に固定式クイック移動ナビを追加
- 全セクション末尾に `▲ 目次へ戻る` を追加
- 目次を3部構成（基礎 / 集計結合 / 更新運用）へ階層化
- 各章（1〜16）へ「実務ミニケース」を本文内埋め込み
- 公式仕様ベース補強章（19c/21c）を新設
- 「インポート済み教材参照」文言を削除し、独立教材として明記

### 3. 内容を深くしたポイント（抜粋）
- MERGE の決定性（1文内同一行複数更新不可）と投入前重複排除
- 集合演算子の列数/型整合ルール、括弧明示の実務運用
- DDL暗黙COMMITを前提にした手順分離
- SEQUENCE欠番の仕様理解とID設計分離
- USER_/ALL_/DBA_ ビューの使い分けと障害初動テンプレ化
- TZ付き型の保存・表示責務分離

### 4. 対象ファイル
- `/Users/onosekiamane/Downloads/ベースアクセス/Oracle_Silver_SE17/textbooks/Oracle_DBA_Silver_SQL_Textbook.html`

### 5. 参照した公式情報（Oracle）
- Oracle Database SQL Language Reference 19c  
  https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/
- Oracle Database SQL Language Reference 21c: GRANT  
  https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/GRANT.html
- Oracle Database SQL Language Reference 21c: REVOKE  
  https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/REVOKE.html
- Oracle Database SQL Language Reference 21c: Data Types  
  https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html
- Oracle Database Reference 21c: ALL_TAB_COLUMNS  
  https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_COLUMNS.html

### 6. 次版（Ver 1.2）での強化予定
- 章ごとに図を1枚以上追加（ER風・処理順・権限フロー）
- DBA観点（CDB/PDB、RMAN、REDO/UNDO、障害復旧手順）の補講章を追加
- 章末確認問題を「基礎/応用/実務判断」3段階に再編
