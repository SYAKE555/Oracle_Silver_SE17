# Oracle DBA Silver SQL 学習環境 — セットアップガイド

## プロジェクト構成

```
Oracle_Silver_SE17/
├── index.html                           # PC版UI
├── mobile.html                          # モバイル版UI
├── config.json                          # Oracle Database SQL設定（1Z0-071）
├── app.py                               # Flask APIサーバー
├── launch_web.py                        # ブラウザ起動スクリプト
├── launch_app.py                        # デスクトップアプリ起動
├── app/
│   ├── data/
│   │   ├── initial_state.js             # 教材データ（12キースキーマ）
│   │   └── analytics_schema.sql         # 学習履歴DB
│   ├── basetract_core.js                # UIエンジン
│   ├── loader.js                        # 動的ローダー
│   └── theme.css                        # レスポンシブスタイル
├── docs/
│   ├── learning_flow.md                 # SQL向け学習フロー
│   ├── technical_spec.md                # 技術仕様
│   └── setup.md                         # セットアップ
└── textbooks/
    ├── index.html                       # 教科書一覧
    └── Ver_4_0_Oracle_DBA_Silver_SQL_Textbook.html
```

## クイックスタート

### 1. 環境セットアップ
```bash
cd Oracle_Silver_SE17
python3 pipeline/bootstrap.py --yes
```

### 2. サーバー起動
```bash
# オプションA: ブラウザ自動起動
python3 launch_web.py

# オプションB: デスクトップアプリ
python3 launch_app.py
```

### 3. アクセス
- Web: `http://localhost:5000`
- 教科書: `textbooks/index.html`

## 教材の特徴

### 出題ドメイン（SQL 8分野）
| ドメイン | 主要トピック |
|---|---|
| D1 | SQL基礎、SELECT、NULL |
| D2 | WHERE、LIKE、ORDER BY |
| D3 | 単一行関数、CASE、変換関数 |
| D4 | 集計、GROUP BY、HAVING |
| D5 | 結合（INNER/OUTER/SELF/CROSS） |
| D6 | サブクエリ（単一行/複数行/相関） |
| D7 | DML、トランザクション制御 |
| D8 | DDL、制約、ビュー、索引、シーケンス |

### 品質検証済み補完領域
- 集合演算子（UNION/INTERSECT/MINUS）
- 権限管理（GRANT/REVOKE/ROLE）
- データ辞書ビュー（USER_/ALL_/DBA_）
- 日時とタイムゾーン型

## 企業ネットワーク公開の注意点

- 公開URLは **HTTPSのみ** を使用する（`https://...`）。
- 外部スクリプト依存を減らし、静的HTML単体でも本文閲覧可能な状態で公開する。
- 不要なブランドロゴ・商標表記・宣伝文言は含めない。
- 社用端末からのアクセスを想定し、教材ページに追跡スクリプトを埋め込まない。

## 公式参考資料（HTTPS）

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/F19136_01/sqlrf/index.html)
- [試験情報 1Z0-071](https://education.oracle.com/ja/oracle-database-sql/pexam_1Z0-071)

---

Version: v2.1.0-oracle-dba-silver-sql  
Last Updated: 2026-04-01  
Status: Production Ready
