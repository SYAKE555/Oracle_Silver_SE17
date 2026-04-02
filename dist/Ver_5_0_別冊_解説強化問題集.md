# Oracle DBA Silver SQL 2019 別冊 解説強化問題集

## 使い方
- 各問題は「誤答しやすい観点」を先に明示しています。
- まず自力で回答し、次に「解説（なぜそうなるか）」を読んでください。
- 最後に「実務での確認SQL」を手元で実行して定着させてください。

## 問題1（SELECT / 列別名）
- 問題:
  - `EMPLOYEES(employee_id, employee_name, salary)` から、見出しを `社員ID`, `社員名`, `月給` で表示するSQLを作成せよ。見出しの日本語を正しく表示できる形にすること。
- 解説:
  - 列別名に日本語や空白・記号を使う場合は二重引用符が必要。`AS` は省略可能だが、可読性のため付ける方が安全。
  - 試験では「文字列リテラル」と「列別名の二重引用符」の混同を狙う問題が多い。
- 例:
```sql
SELECT employee_id AS "社員ID",
       employee_name AS "社員名",
       salary AS "月給"
FROM employees;
```

## 問題2（WHERE / NULL判定）
- 問題:
  - `manager_id` が未設定の従業員を抽出するSQLを書け。
- 解説:
  - `= NULL` は比較不能。`IS NULL` / `IS NOT NULL` を使う。
  - 誤答しやすいのは `WHERE manager_id = NULL`。
- 例:
```sql
SELECT employee_id, employee_name
FROM employees
WHERE manager_id IS NULL;
```

## 問題3（GROUP BY / HAVING）
- 問題:
  - 部署ごと平均給与を求め、平均給与が 5000 以上の部署だけ表示せよ。
- 解説:
  - 集約前の行条件は `WHERE`、集約後のグループ条件は `HAVING`。
  - `HAVING AVG(salary) >= 5000` の位置関係を問う問題が頻出。
- 例:
```sql
SELECT department_id, AVG(salary) AS avg_sal
FROM employees
GROUP BY department_id
HAVING AVG(salary) >= 5000;
```

## 問題4（JOIN）
- 問題:
  - `employees` と `departments` を結合し、従業員名と部署名を表示せよ。部署未所属の従業員も落とさないこと。
- 解説:
  - これは左外部結合。`LEFT OUTER JOIN` で employees 側を保持する。
  - 旧式外部結合記法との混同が出やすい。
- 例:
```sql
SELECT e.employee_name, d.department_name
FROM employees e
LEFT OUTER JOIN departments d
  ON e.department_id = d.department_id;
```

## 問題5（副問合せ）
- 問題:
  - 平均給与より高い従業員を抽出せよ。
- 解説:
  - 単一行副問合せの典型。副問合せが単一値を返す前提。
  - 試験では「複数行を返してエラーになるケース」との対比が重要。
- 例:
```sql
SELECT employee_id, employee_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

## 問題6（集合演算子）
- 問題:
  - `sales_2024` と `sales_2025` の顧客ID集合を重複排除して統合せよ。
- 解説:
  - 重複排除は `UNION`。重複保持なら `UNION ALL`。
  - 列数・型整合が取れていないとエラー。
- 例:
```sql
SELECT customer_id FROM sales_2024
UNION
SELECT customer_id FROM sales_2025;
```

## 問題7（DML / UPDATE安全実行）
- 問題:
  - 部署50の給与を3%上げる更新を、安全確認付きで実行する手順を書け。
- 解説:
  - 先に同条件SELECTで件数確認、必要ならSAVEPOINT、更新後再確認、最後にCOMMIT。
  - 試験ではWHERE漏れの影響が頻出。
- 例:
```sql
SELECT COUNT(*) FROM employees WHERE department_id = 50;
SAVEPOINT before_raise;
UPDATE employees
SET salary = salary * 1.03
WHERE department_id = 50;
SELECT COUNT(*) FROM employees WHERE department_id = 50;
COMMIT;
```

## 問題8（DDL / 制約）
- 問題:
  - `status` 列を `NEW/DOING/DONE` のみ許可する制約付きで表を作成せよ。
- 解説:
  - 値域制御は `CHECK` 制約。アプリ側のみで制御しない。
  - 制約名を付けると障害時解析が速い。
- 例:
```sql
CREATE TABLE tasks (
  task_id NUMBER PRIMARY KEY,
  status  VARCHAR2(10) CONSTRAINT ck_tasks_status
          CHECK (status IN ('NEW','DOING','DONE'))
);
```

## 問題9（VIEW）
- 問題:
  - 部署50のみを扱うビューを作成し、条件外への更新を禁止せよ。
- 解説:
  - `WITH CHECK OPTION` により、更新後もビュー条件を満たすことを強制できる。
```sql
CREATE OR REPLACE VIEW v_dept50 AS
SELECT employee_id, department_id, salary
FROM employees
WHERE department_id = 50
WITH CHECK OPTION;
```

## 問題10（INDEX）
- 問題:
  - `orders(order_date, customer_id)` に対して、日付検索を主目的とした複合索引を作成せよ。
- 解説:
  - 複合索引は先頭列が重要。利用クエリに合わせて列順を決める。
```sql
CREATE INDEX idx_orders_date_cust
ON orders(order_date, customer_id);
```

## 問題11（権限 / ロール）
- 問題:
  - レポート閲覧専用ロールを作成し、`sales.monthly_report` への `SELECT` のみ付与せよ。
- 解説:
  - 個別GRANT乱発を避け、ロールで管理するのが運用上安全。
```sql
CREATE ROLE role_report_viewer;
GRANT SELECT ON sales.monthly_report TO role_report_viewer;
GRANT role_report_viewer TO report_user;
```

## 問題12（タイムゾーン）
- 問題:
  - 現在時刻を UTC と Asia/Tokyo の両方で表示せよ。
- 解説:
  - 同じ瞬間でも表示時刻はタイムゾーンで変わる。比較前に基準統一が必要。
```sql
SELECT SYSTIMESTAMP AT TIME ZONE 'UTC'        AS utc_now,
       SYSTIMESTAMP AT TIME ZONE 'Asia/Tokyo' AS tokyo_now
FROM dual;
```
