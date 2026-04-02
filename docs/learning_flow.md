# Oracle DBA Silver SQL (1Z0-071) 学習フロー

> 本文書の目的: SQL資格試験（1Z0-071相当）の出題構造に合わせて、学習順序を最適化する。

## 1. 試験構造（SQL 8ドメイン）

| ドメイン | 学習テーマ | 優先度 |
|---|---|---|
| D1 | SQL基礎、SELECT、NULL | 高 |
| D2 | 条件式、ソート、行制限 | 高 |
| D3 | 単一行関数、型変換、条件式 | 高 |
| D4 | 集計、GROUP BY、HAVING | 高 |
| D5 | 結合 | 高 |
| D6 | サブクエリ | 高 |
| D7 | DML、トランザクション | 中 |
| D8 | DDL、制約、ビュー、索引 | 中 |

## 2. 推奨学習順

1. D1-D2: 取得系の土台
2. D3-D4: 関数と集計
3. D5-D6: 複数表・サブクエリ
4. D7-D8: 更新系とオブジェクト管理
5. 総合演習: 45分セット演習を反復

## 3. 補完学習（教科書の不足を補う）

- 集合演算子: `UNION`, `UNION ALL`, `INTERSECT`, `MINUS`
- 権限管理: `GRANT`, `REVOKE`, ロール設計
- データ辞書: `USER_TABLES`, `ALL_TAB_COLUMNS` など
- 日時/タイムゾーン: `TIMESTAMP WITH TIME ZONE`

## 4. 実務と結びつける学習ポイント

- SELECTは「帳票・画面・APIレスポンス」の土台。
- JOINは「業務エンティティの関連付け」（例: 受注と顧客）。
- トランザクションは「失敗時に戻せる更新単位」。
- 権限設計は「本番事故を防ぐ最小権限」の実践。

## 5. 公式参照（HTTPS）

- <https://docs.oracle.com/cd/F19136_01/sqlrf/index.html>
- <https://education.oracle.com/ja/oracle-database-sql/pexam_1Z0-071>
