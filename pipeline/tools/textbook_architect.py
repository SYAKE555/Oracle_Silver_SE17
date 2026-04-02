#!/usr/bin/env python3
"""
Basetract Textbook Architect v3 -- Oracle Database SQL (1Z0-071)
Oracle SQL 教科書を生成する。

設計原則:
1. 前提知識ゼロで読める
2. 概念説明 -> コード例 -> 問題演習 の流れ
3. 試験頻出ポイントを明示
4. Oracle 1Z0-071 公式8ドメイン構造に準拠
"""

import json, re, os, logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# ============================================================
# 教科書の教育コンテンツ（ドメイン x セクション x 学習内容）
# ============================================================
TEXTBOOK_CONTENT = {
    "D1": {
        "title": "SQLとリレーショナルデータベースの基礎",
        "intro": "リレーショナルデータベースの基本概念とSQLの基本構文を学びます。データベースがどのように機能するか、SELECT文でどのようにデータを取得するかを理解しましょう。",
        "sections": [
            {
                "name": "リレーショナルデータベースとSQL概要",
                "topics": ["リレーショナルデータベース", "テーブル", "行", "列", "主キー"],
                "content": (
                    "<h3>リレーショナルデータベースとは</h3>"
                    "<p>リレーショナルデータベース（RDB）は、データを<strong>テーブル（表）</strong>の形式で管理するデータベースです。"
                    "テーブルは行（レコード）と列（カラム）で構成されます。</p>"
                    "<table class='summary-table'>"
                    "<tr><th>用語</th><th>説明</th><th>例</th></tr>"
                    "<tr><td>テーブル（表）</td><td>データを格納する2次元の表</td><td>EMPLOYEES テーブル</td></tr>"
                    "<tr><td>行（レコード）</td><td>テーブルの1件分のデータ</td><td>従業員1人分の情報</td></tr>"
                    "<tr><td>列（カラム）</td><td>データの属性（項目）</td><td>EMPLOYEE_ID, LAST_NAME 等</td></tr>"
                    "<tr><td>主キー（PK）</td><td>行を一意に識別する列</td><td>EMPLOYEE_ID</td></tr>"
                    "<tr><td>外部キー（FK）</td><td>他テーブルの主キーを参照する列</td><td>DEPARTMENT_ID</td></tr>"
                    "</table>"
                    "<h3>SQL とは</h3>"
                    "<p>SQL（Structured Query Language）はリレーショナルデータベースを操作するための標準言語です。"
                    "以下の4種類の操作があります。</p>"
                    "<table class='summary-table'>"
                    "<tr><th>分類</th><th>コマンド</th><th>説明</th></tr>"
                    "<tr><td>DQL（データ照会）</td><td>SELECT</td><td>データの検索・取得</td></tr>"
                    "<tr><td>DML（データ操作）</td><td>INSERT, UPDATE, DELETE</td><td>データの追加・変更・削除</td></tr>"
                    "<tr><td>DDL（データ定義）</td><td>CREATE, ALTER, DROP</td><td>テーブル等の構造定義</td></tr>"
                    "<tr><td>TCL（トランザクション制御）</td><td>COMMIT, ROLLBACK, SAVEPOINT</td><td>トランザクション管理</td></tr>"
                    "</table>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> Oracle では SELECT も DML に含める場合がありますが、"
                    "試験では DML = INSERT/UPDATE/DELETE として扱うことが多いです。"
                    "</div>"
                )
            },
            {
                "name": "SELECT文の基本構文",
                "topics": ["SELECT", "FROM", "列別名", "AS", "DISTINCT", "DUAL"],
                "content": (
                    "<h3>SELECT 文の基本</h3>"
                    "<p>SELECT 文はデータベースからデータを取得する最も基本的な命令です。</p>"
                    "<pre><code>-- 基本構文\n"
                    "SELECT 列名1, 列名2, ...\n"
                    "FROM   テーブル名;\n\n"
                    "-- 全列を取得する場合\n"
                    "SELECT *\n"
                    "FROM   EMPLOYEES;\n\n"
                    "-- 特定の列を取得する場合\n"
                    "SELECT EMPLOYEE_ID, LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<h3>列別名（AS）</h3>"
                    "<p>列に別名（エイリアス）を付けることができます。スペースや特殊文字を含む場合はダブルクォートで囲みます。</p>"
                    "<pre><code>SELECT LAST_NAME AS 名前,\n"
                    "       SALARY AS 給与,\n"
                    "       SALARY * 12 AS \"年間給与\"\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<h3>DISTINCT で重複排除</h3>"
                    "<pre><code>-- 重複を排除して部署IDを取得\n"
                    "SELECT DISTINCT DEPARTMENT_ID\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<h3>DUAL テーブル</h3>"
                    "<p>DUAL は Oracle が提供する特殊な1行1列のダミーテーブルです。"
                    "関数の確認や計算式のテストに使います。</p>"
                    "<pre><code>-- 現在日時の確認\n"
                    "SELECT SYSDATE FROM DUAL;\n\n"
                    "-- 計算式のテスト\n"
                    "SELECT 2 + 3 FROM DUAL;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "列別名にダブルクォートを使うと大文字小文字が区別されます。"
                    "AS は省略可能ですが、試験では AS を明示するパターンが多く出題されます。"
                    "DISTINCT は SELECT の直後に1つだけ記述可能です。"
                    "</div>"
                )
            },
            {
                "name": "NULL の基礎",
                "topics": ["NULL", "IS NULL", "IS NOT NULL", "算術演算", "連結演算子"],
                "content": (
                    "<h3>NULL とは</h3>"
                    "<p>NULL は「値が存在しない」「不明」を表す特殊な値です。"
                    "0（ゼロ）や空文字とは異なります。</p>"
                    "<h3>NULL を含む算術演算</h3>"
                    "<p>NULL を含む算術演算の結果は必ず NULL になります。</p>"
                    "<pre><code>-- COMMISSION_PCT が NULL の場合、結果も NULL\n"
                    "SELECT LAST_NAME,\n"
                    "       SALARY * COMMISSION_PCT AS コミッション\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<h3>IS NULL / IS NOT NULL</h3>"
                    "<p>NULL の比較には = や != は使えません。IS NULL / IS NOT NULL を使います。</p>"
                    "<pre><code>-- コミッションがない（NULL）従業員\n"
                    "SELECT LAST_NAME\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  COMMISSION_PCT IS NULL;\n\n"
                    "-- コミッションがある（NULL でない）従業員\n"
                    "SELECT LAST_NAME\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  COMMISSION_PCT IS NOT NULL;</code></pre>"
                    "<h3>文字列連結演算子（||）</h3>"
                    "<pre><code>-- || で文字列を連結\n"
                    "SELECT FIRST_NAME || ' ' || LAST_NAME AS 氏名\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "NULL = NULL は FALSE（NULL を比較演算子で比較できない）。"
                    "NULL を含む列の ORDER BY は、デフォルトで昇順の場合 NULLS LAST、"
                    "降順の場合 NULLS FIRST の動作となります。"
                    "</div>"
                )
            }
        ]
    },

    "D2": {
        "title": "データの絞り込みとソート",
        "intro": "WHERE 句を使ったデータの絞り込みと、ORDER BY を使ったデータのソート方法を学びます。",
        "sections": [
            {
                "name": "WHERE句と比較演算子",
                "topics": ["WHERE", "BETWEEN", "IN", "比較演算子", "AND", "OR", "NOT"],
                "content": (
                    "<h3>WHERE 句の基本</h3>"
                    "<p>WHERE 句を使うと条件に合う行だけを取得できます。</p>"
                    "<pre><code>SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  SALARY >= 10000;</code></pre>"
                    "<h3>比較演算子一覧</h3>"
                    "<table class='summary-table'>"
                    "<tr><th>演算子</th><th>意味</th><th>例</th></tr>"
                    "<tr><td>=</td><td>等しい</td><td>SALARY = 5000</td></tr>"
                    "<tr><td>&lt;&gt; または !=</td><td>等しくない</td><td>SALARY &lt;&gt; 5000</td></tr>"
                    "<tr><td>&gt;</td><td>より大きい</td><td>SALARY &gt; 5000</td></tr>"
                    "<tr><td>&lt;</td><td>より小さい</td><td>SALARY &lt; 5000</td></tr>"
                    "<tr><td>&gt;=</td><td>以上</td><td>SALARY &gt;= 5000</td></tr>"
                    "<tr><td>&lt;=</td><td>以下</td><td>SALARY &lt;= 5000</td></tr>"
                    "</table>"
                    "<h3>BETWEEN ... AND</h3>"
                    "<pre><code>-- 5000 以上 10000 以下の給与（両端含む）\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  SALARY BETWEEN 5000 AND 10000;</code></pre>"
                    "<h3>IN 演算子</h3>"
                    "<pre><code>-- 部署 10, 20, 30 のいずれか\n"
                    "SELECT LAST_NAME, DEPARTMENT_ID\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  DEPARTMENT_ID IN (10, 20, 30);</code></pre>"
                    "<h3>AND / OR / NOT</h3>"
                    "<pre><code>-- AND: 両方の条件を満たす\n"
                    "SELECT LAST_NAME, SALARY, DEPARTMENT_ID\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  SALARY > 5000\n"
                    "AND    DEPARTMENT_ID = 50;\n\n"
                    "-- OR: どちらかの条件を満たす\n"
                    "SELECT LAST_NAME, SALARY, DEPARTMENT_ID\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  SALARY > 10000\n"
                    "OR     DEPARTMENT_ID = 10;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "BETWEEN の値は「小さい値 AND 大きい値」の順で指定します。"
                    "NOT IN に NULL が含まれる場合、全件が返りません（NULL との比較が不定のため）。"
                    "AND は OR より優先度が高いため、OR を使う場合は括弧で明示的にグループ化を推奨。"
                    "</div>"
                )
            },
            {
                "name": "LIKE演算子とワイルドカード",
                "topics": ["LIKE", "ワイルドカード", "アンダースコア", "パーセント", "ESCAPE"],
                "content": (
                    "<h3>LIKE 演算子</h3>"
                    "<p>LIKE は文字列のパターンマッチングに使います。2種類のワイルドカードがあります。</p>"
                    "<table class='summary-table'>"
                    "<tr><th>ワイルドカード</th><th>意味</th><th>例</th></tr>"
                    "<tr><td>%（パーセント）</td><td>0文字以上の任意の文字列</td><td>'A%' → A で始まる</td></tr>"
                    "<tr><td>_（アンダースコア）</td><td>任意の1文字</td><td>'_a%' → 2文字目が a</td></tr>"
                    "</table>"
                    "<pre><code>-- 'S' で始まる名前\n"
                    "SELECT LAST_NAME\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  LAST_NAME LIKE 'S%';\n\n"
                    "-- 2文字目が 'a' の名前\n"
                    "SELECT LAST_NAME\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  LAST_NAME LIKE '_a%';\n\n"
                    "-- 名前に 'an' を含む\n"
                    "SELECT LAST_NAME\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  LAST_NAME LIKE '%an%';</code></pre>"
                    "<h3>ESCAPE オプション</h3>"
                    "<p>% や _ を文字として検索したい場合は ESCAPE を使います。</p>"
                    "<pre><code>-- JOB_ID に 'SA_' を含む（_ をリテラルとして扱う）\n"
                    "SELECT JOB_ID\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  JOB_ID LIKE '%SA$_%' ESCAPE '$';</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "LIKE の比較は大文字小文字を区別します（Oracle のデフォルト）。"
                    "ESCAPE に使う文字は任意の1文字で、慣例的に \\ や $ が使われます。"
                    "</div>"
                )
            },
            {
                "name": "ORDER BY句",
                "topics": ["ORDER BY", "ASC", "DESC", "NULLS FIRST", "NULLS LAST"],
                "content": (
                    "<h3>ORDER BY の基本</h3>"
                    "<p>ORDER BY 句で検索結果をソートします。デフォルトは昇順（ASC）です。</p>"
                    "<pre><code>-- 給与の昇順（デフォルト）\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY SALARY;\n\n"
                    "-- 給与の降順\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY SALARY DESC;\n\n"
                    "-- 複数列でのソート（部署昇順、給与降順）\n"
                    "SELECT LAST_NAME, DEPARTMENT_ID, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY DEPARTMENT_ID ASC, SALARY DESC;</code></pre>"
                    "<h3>NULLS FIRST / NULLS LAST</h3>"
                    "<pre><code>-- NULL を最初に表示\n"
                    "SELECT LAST_NAME, COMMISSION_PCT\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY COMMISSION_PCT NULLS FIRST;\n\n"
                    "-- NULL を最後に表示\n"
                    "SELECT LAST_NAME, COMMISSION_PCT\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY COMMISSION_PCT NULLS LAST;</code></pre>"
                    "<h3>列位置や別名でのソート</h3>"
                    "<pre><code>-- SELECT の列番号でソート（2列目 = SALARY）\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY 2 DESC;\n\n"
                    "-- 列別名でソート\n"
                    "SELECT LAST_NAME, SALARY * 12 AS annual_sal\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY annual_sal DESC;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "NULL は昇順ソートではデフォルトで最後（NULLS LAST）、"
                    "降順ソートではデフォルトで最初（NULLS FIRST）に表示されます。"
                    "ORDER BY は SELECT リストにない列でもソートできます（DISTINCT 使用時を除く）。"
                    "</div>"
                )
            },
            {
                "name": "行制限と置換変数",
                "topics": ["OFFSET", "FETCH", "ROWNUM", "置換変数", "DEFINE", "VERIFY"],
                "content": (
                    "<h3>OFFSET / FETCH（行制限）</h3>"
                    "<p>ORDER BY と組み合わせて、先頭から何行スキップし、何行取得するかを指定します。</p>"
                    "<pre><code>-- 給与の高い順に、上位5件を取得\n"
                    "SELECT EMPLOYEE_ID, LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY SALARY DESC\n"
                    "FETCH FIRST 5 ROWS ONLY;\n\n"
                    "-- 6〜10位を取得（5行スキップして5行取得）\n"
                    "SELECT EMPLOYEE_ID, LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "ORDER BY SALARY DESC\n"
                    "OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;</code></pre>"
                    "<h3>ROWNUM（疑似列）</h3>"
                    "<pre><code>-- 先頭10行（取得順）\n"
                    "SELECT *\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  ROWNUM &lt;= 10;</code></pre>"
                    "<h3>置換変数（SQL*Plus系）</h3>"
                    "<p>実行時に値を入力させる変数です。学習・検証で使われます。</p>"
                    "<pre><code>-- &amp; で単発置換\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  DEPARTMENT_ID = &amp;dept_id;\n\n"
                    "-- DEFINE で固定\n"
                    "DEFINE dept_id = 50\n"
                    "SELECT LAST_NAME FROM EMPLOYEES WHERE DEPARTMENT_ID = &amp;dept_id;\n\n"
                    "-- VERIFY ON/OFF（置換前後の表示）\n"
                    "SET VERIFY ON</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "行制限は ORDER BY とセットで使わないと結果の順序が不定になります。"
                    "ROWNUM は ORDER BY より前に付与されるため、上位N件抽出で誤用しやすいです。"
                    "置換変数（DEFINE/VERIFY）は SQL*Plus 系の操作問題で問われることがあります。"
                    "</div>"
                )
            }
        ]
    },

    "D3": {
        "title": "単一行関数",
        "intro": "1行ずつ処理する単一行関数を学びます。文字列関数、数値関数、日付関数、NULL関数と条件式を扱います。",
        "sections": [
            {
                "name": "文字列関数",
                "topics": ["UPPER", "LOWER", "SUBSTR", "LENGTH", "INSTR", "REPLACE", "TRIM", "LPAD", "RPAD"],
                "content": (
                    "<h3>主要な文字列関数</h3>"
                    "<table class='summary-table'>"
                    "<tr><th>関数</th><th>構文</th><th>説明</th></tr>"
                    "<tr><td>UPPER</td><td>UPPER(str)</td><td>大文字に変換</td></tr>"
                    "<tr><td>LOWER</td><td>LOWER(str)</td><td>小文字に変換</td></tr>"
                    "<tr><td>INITCAP</td><td>INITCAP(str)</td><td>先頭を大文字、残りを小文字</td></tr>"
                    "<tr><td>LENGTH</td><td>LENGTH(str)</td><td>文字数を返す</td></tr>"
                    "<tr><td>SUBSTR</td><td>SUBSTR(str, start [,len])</td><td>部分文字列を取り出す</td></tr>"
                    "<tr><td>INSTR</td><td>INSTR(str, search)</td><td>文字列の位置を返す</td></tr>"
                    "<tr><td>REPLACE</td><td>REPLACE(str, from, to)</td><td>文字を置換する</td></tr>"
                    "<tr><td>TRIM</td><td>TRIM(str)</td><td>前後の空白（または指定文字）を除去</td></tr>"
                    "<tr><td>LPAD</td><td>LPAD(str, len, pad)</td><td>左側を指定文字で埋める</td></tr>"
                    "<tr><td>RPAD</td><td>RPAD(str, len, pad)</td><td>右側を指定文字で埋める</td></tr>"
                    "</table>"
                    "<pre><code>SELECT UPPER('hello'),        -- HELLO\n"
                    "       LOWER('WORLD'),        -- world\n"
                    "       LENGTH('Oracle'),      -- 6\n"
                    "       SUBSTR('Oracle', 2, 3),-- rac\n"
                    "       INSTR('Oracle', 'a'),  -- 3\n"
                    "       REPLACE('abc', 'b', 'B'), -- aBc\n"
                    "       LPAD('42', 5, '0'),    -- 00042\n"
                    "       TRIM('  hello  ')      -- hello\n"
                    "FROM DUAL;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "SUBSTR の開始位置は 1 から始まります（0 を指定すると 1 と同じ動作）。"
                    "負の値を指定すると末尾からカウントします。"
                    "INSTR は見つからない場合 0 を返します（NULL ではない）。"
                    "</div>"
                )
            },
            {
                "name": "数値関数",
                "topics": ["ROUND", "TRUNC", "MOD", "CEIL", "FLOOR"],
                "content": (
                    "<h3>主要な数値関数</h3>"
                    "<table class='summary-table'>"
                    "<tr><th>関数</th><th>構文</th><th>説明</th></tr>"
                    "<tr><td>ROUND</td><td>ROUND(n [,d])</td><td>四捨五入。d は小数点以下の桁数</td></tr>"
                    "<tr><td>TRUNC</td><td>TRUNC(n [,d])</td><td>切り捨て。d は小数点以下の桁数</td></tr>"
                    "<tr><td>MOD</td><td>MOD(m, n)</td><td>m を n で割った余り</td></tr>"
                    "<tr><td>CEIL</td><td>CEIL(n)</td><td>n 以上の最小整数（切り上げ）</td></tr>"
                    "<tr><td>FLOOR</td><td>FLOOR(n)</td><td>n 以下の最大整数（切り下げ）</td></tr>"
                    "</table>"
                    "<pre><code>SELECT ROUND(45.926, 2),   -- 45.93\n"
                    "       ROUND(45.926, 0),   -- 46\n"
                    "       ROUND(45.926, -1),  -- 50\n"
                    "       TRUNC(45.926, 2),   -- 45.92\n"
                    "       TRUNC(45.926, -1),  -- 40\n"
                    "       MOD(1600, 300),     -- 100\n"
                    "       CEIL(2.3),          -- 3\n"
                    "       FLOOR(2.7)          -- 2\n"
                    "FROM DUAL;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "ROUND と TRUNC の第2引数（桁数）は省略すると 0（整数）として扱われます。"
                    "負の値（例: -1）を指定すると十の位で丸めます。"
                    "MOD(m, n) は m が負の場合も使えます（結果の符号は m に依存）。"
                    "</div>"
                )
            },
            {
                "name": "日付関数",
                "topics": ["SYSDATE", "ADD_MONTHS", "MONTHS_BETWEEN", "TO_DATE", "TO_CHAR", "LAST_DAY"],
                "content": (
                    "<h3>日付の基本</h3>"
                    "<p>Oracle では日付型は DATE 型で、日付と時刻の両方を保持します。</p>"
                    "<pre><code>-- 現在日時\n"
                    "SELECT SYSDATE FROM DUAL;\n\n"
                    "-- 日付の加減算（1日単位）\n"
                    "SELECT SYSDATE + 7 AS 1週間後,\n"
                    "       SYSDATE - 1 AS 昨日\n"
                    "FROM DUAL;</code></pre>"
                    "<h3>主要な日付関数</h3>"
                    "<table class='summary-table'>"
                    "<tr><th>関数</th><th>説明</th><th>例</th></tr>"
                    "<tr><td>ADD_MONTHS(d, n)</td><td>日付に n ヶ月加算</td><td>ADD_MONTHS(SYSDATE, 3)</td></tr>"
                    "<tr><td>MONTHS_BETWEEN(d1, d2)</td><td>2日付間の月数</td><td>MONTHS_BETWEEN(d1, d2)</td></tr>"
                    "<tr><td>LAST_DAY(d)</td><td>月の末日を返す</td><td>LAST_DAY(SYSDATE)</td></tr>"
                    "<tr><td>NEXT_DAY(d, day)</td><td>次の指定曜日の日付</td><td>NEXT_DAY(SYSDATE, 'MONDAY')</td></tr>"
                    "<tr><td>ROUND(d, fmt)</td><td>日付の四捨五入</td><td>ROUND(SYSDATE, 'MONTH')</td></tr>"
                    "<tr><td>TRUNC(d, fmt)</td><td>日付の切り捨て</td><td>TRUNC(SYSDATE, 'YEAR')</td></tr>"
                    "</table>"
                    "<h3>TO_CHAR / TO_DATE（変換関数）</h3>"
                    "<pre><code>-- 日付を文字列に変換\n"
                    "SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM DUAL;\n\n"
                    "-- 文字列を日付に変換\n"
                    "SELECT TO_DATE('2024-01-15', 'YYYY-MM-DD') FROM DUAL;\n\n"
                    "-- 数値を文字列に変換\n"
                    "SELECT TO_CHAR(12345.67, '999,999.99') FROM DUAL;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "日付同士の減算は日数（小数）を返します。"
                    "MONTHS_BETWEEN の結果は小数になることがあります（整数にするなら TRUNC や FLOOR を使用）。"
                    "TO_CHAR のフォーマット: YYYY=4桁年, MM=月, DD=日, HH24=24時間形式, MI=分, SS=秒。"
                    "</div>"
                )
            },
            {
                "name": "NULL関数と条件式",
                "topics": ["NVL", "NVL2", "COALESCE", "NULLIF", "DECODE", "CASE"],
                "content": (
                    "<h3>NULL を扱う関数</h3>"
                    "<table class='summary-table'>"
                    "<tr><th>関数</th><th>構文</th><th>説明</th></tr>"
                    "<tr><td>NVL</td><td>NVL(expr, alt)</td><td>NULL なら alt を返す</td></tr>"
                    "<tr><td>NVL2</td><td>NVL2(expr, notnull, null)</td><td>NULL なら null_val、そうでなければ notnull_val を返す</td></tr>"
                    "<tr><td>COALESCE</td><td>COALESCE(e1, e2, ...)</td><td>NULL でない最初の値を返す</td></tr>"
                    "<tr><td>NULLIF</td><td>NULLIF(e1, e2)</td><td>e1 = e2 なら NULL、異なれば e1 を返す</td></tr>"
                    "</table>"
                    "<pre><code>-- NVL: コミッションが NULL なら 0 を使う\n"
                    "SELECT LAST_NAME,\n"
                    "       SALARY * (1 + NVL(COMMISSION_PCT, 0)) AS 合計給与\n"
                    "FROM   EMPLOYEES;\n\n"
                    "-- COALESCE: 最初の非 NULL 値\n"
                    "SELECT COALESCE(NULL, NULL, 'Hello', 'World') FROM DUAL; -- Hello</code></pre>"
                    "<h3>条件式（CASE / DECODE）</h3>"
                    "<pre><code>-- CASE 式（標準 SQL）\n"
                    "SELECT LAST_NAME,\n"
                    "       CASE JOB_ID\n"
                    "           WHEN 'IT_PROG' THEN 'IT部門'\n"
                    "           WHEN 'SA_REP'  THEN '営業部門'\n"
                    "           ELSE 'その他'\n"
                    "       END AS 部門名\n"
                    "FROM   EMPLOYEES;\n\n"
                    "-- DECODE（Oracle 独自）\n"
                    "SELECT LAST_NAME,\n"
                    "       DECODE(JOB_ID,\n"
                    "              'IT_PROG', 'IT部門',\n"
                    "              'SA_REP',  '営業部門',\n"
                    "              'その他') AS 部門名\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "NVL と NVL2 は引数のデータ型が一致している必要があります。"
                    "COALESCE は標準 SQL で移植性が高いです。"
                    "DECODE は Oracle 独自です。CASE 式の方が標準 SQL に準拠しています。"
                    "CASE 式には「単純 CASE（WHEN 値）」と「検索 CASE（WHEN 条件）」の2種類があります。"
                    "</div>"
                )
            }
        ]
    },

    "D4": {
        "title": "グループ関数と集計",
        "intro": "複数行をまとめて集計するグループ関数と、GROUP BY / HAVING を使ったグループ集計を学びます。",
        "sections": [
            {
                "name": "グループ関数",
                "topics": ["COUNT", "SUM", "AVG", "MAX", "MIN", "グループ関数", "NULL"],
                "content": (
                    "<h3>グループ関数とは</h3>"
                    "<p>グループ関数（集計関数）は複数の行をまとめて1つの結果を返す関数です。</p>"
                    "<table class='summary-table'>"
                    "<tr><th>関数</th><th>説明</th><th>NULL の扱い</th></tr>"
                    "<tr><td>COUNT(*)</td><td>行数を返す</td><td>NULL 行も含めてカウント</td></tr>"
                    "<tr><td>COUNT(列)</td><td>指定列の非 NULL 件数</td><td>NULL を無視</td></tr>"
                    "<tr><td>SUM(列)</td><td>合計値</td><td>NULL を無視</td></tr>"
                    "<tr><td>AVG(列)</td><td>平均値</td><td>NULL を無視（分母も減る）</td></tr>"
                    "<tr><td>MAX(列)</td><td>最大値</td><td>NULL を無視</td></tr>"
                    "<tr><td>MIN(列)</td><td>最小値</td><td>NULL を無視</td></tr>"
                    "</table>"
                    "<pre><code>SELECT COUNT(*) AS 総件数,\n"
                    "       COUNT(COMMISSION_PCT) AS コミッションあり件数,\n"
                    "       SUM(SALARY) AS 給与合計,\n"
                    "       AVG(SALARY) AS 給与平均,\n"
                    "       MAX(SALARY) AS 最高給与,\n"
                    "       MIN(SALARY) AS 最低給与\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<h3>DISTINCT との組み合わせ</h3>"
                    "<pre><code>-- 重複を除いた件数\n"
                    "SELECT COUNT(DISTINCT DEPARTMENT_ID) AS 部署数\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "AVG(COMMISSION_PCT) は NULL を除いた平均です。全員での平均を求めるなら "
                    "AVG(NVL(COMMISSION_PCT, 0)) を使います。"
                    "COUNT(*) と COUNT(列) の違いは頻出です。"
                    "</div>"
                )
            },
            {
                "name": "GROUP BY と HAVING",
                "topics": ["GROUP BY", "HAVING", "SQL実行順序", "ORA-00979"],
                "content": (
                    "<h3>GROUP BY の基本</h3>"
                    "<p>GROUP BY でグループに分けてから集計します。</p>"
                    "<pre><code>-- 部署ごとの給与合計\n"
                    "SELECT DEPARTMENT_ID,\n"
                    "       SUM(SALARY) AS 給与合計,\n"
                    "       COUNT(*) AS 人数\n"
                    "FROM   EMPLOYEES\n"
                    "GROUP BY DEPARTMENT_ID;</code></pre>"
                    "<h3>HAVING 句</h3>"
                    "<p>HAVING はグループに対する条件を指定します（WHERE はグループ前の行への条件）。</p>"
                    "<pre><code>-- 平均給与が 8000 以上の部署\n"
                    "SELECT DEPARTMENT_ID,\n"
                    "       AVG(SALARY) AS 平均給与\n"
                    "FROM   EMPLOYEES\n"
                    "GROUP BY DEPARTMENT_ID\n"
                    "HAVING AVG(SALARY) >= 8000;</code></pre>"
                    "<h3>SQL の実行順序</h3>"
                    "<table class='summary-table'>"
                    "<tr><th>順序</th><th>句</th><th>説明</th></tr>"
                    "<tr><td>1</td><td>FROM</td><td>テーブルの取得</td></tr>"
                    "<tr><td>2</td><td>WHERE</td><td>行の絞り込み</td></tr>"
                    "<tr><td>3</td><td>GROUP BY</td><td>グループ化</td></tr>"
                    "<tr><td>4</td><td>HAVING</td><td>グループの絞り込み</td></tr>"
                    "<tr><td>5</td><td>SELECT</td><td>列の選択</td></tr>"
                    "<tr><td>6</td><td>ORDER BY</td><td>ソート</td></tr>"
                    "</table>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント（ORA-00979）：</strong> "
                    "SELECT に記述した列は GROUP BY にも含める必要があります。"
                    "グループ関数以外の列が SELECT にあり、GROUP BY に含まれていない場合は ORA-00979 エラーになります。"
                    "WHERE にはグループ関数を使えません（HAVING を使う）。"
                    "</div>"
                )
            }
        ]
    },

    "D5": {
        "title": "複数表の結合",
        "intro": "複数のテーブルを結合してデータを取得する JOIN 構文を学びます。内部結合、外部結合、自己結合など様々な結合方法を習得します。",
        "sections": [
            {
                "name": "INNER JOIN",
                "topics": ["INNER JOIN", "JOIN", "ON", "USING", "NATURAL JOIN", "等結合"],
                "content": (
                    "<h3>INNER JOIN の基本</h3>"
                    "<p>INNER JOIN は両方のテーブルで条件が一致する行だけを返します。</p>"
                    "<pre><code>-- ON 句を使った結合\n"
                    "SELECT e.LAST_NAME, e.DEPARTMENT_ID, d.DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES e\n"
                    "INNER JOIN DEPARTMENTS d\n"
                    "ON     e.DEPARTMENT_ID = d.DEPARTMENT_ID;\n\n"
                    "-- USING 句（同名の列で結合する場合）\n"
                    "SELECT LAST_NAME, DEPARTMENT_ID, DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES\n"
                    "JOIN   DEPARTMENTS\n"
                    "USING  (DEPARTMENT_ID);\n\n"
                    "-- NATURAL JOIN（同名列を自動で等結合）\n"
                    "SELECT LAST_NAME, DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES\n"
                    "NATURAL JOIN DEPARTMENTS;</code></pre>"
                    "<h3>旧来の等結合（Oracle 独自）</h3>"
                    "<pre><code>-- WHERE 句による等結合（非 ANSI 形式）\n"
                    "SELECT e.LAST_NAME, d.DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES e, DEPARTMENTS d\n"
                    "WHERE  e.DEPARTMENT_ID = d.DEPARTMENT_ID;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "USING 句を使う場合、結合に使った列にはテーブル名（またはエイリアス）を付けてはいけません。"
                    "NATURAL JOIN は結合列を明示しないため、予期しない結合が起きる危険があります。"
                    "INNER は省略可能（JOIN のみでも内部結合になる）。"
                    "</div>"
                )
            },
            {
                "name": "OUTER JOIN",
                "topics": ["LEFT OUTER JOIN", "RIGHT OUTER JOIN", "FULL OUTER JOIN", "外部結合"],
                "content": (
                    "<h3>外部結合（OUTER JOIN）</h3>"
                    "<p>一方のテーブルに一致する行がなくても、NULL として結果に含めます。</p>"
                    "<table class='summary-table'>"
                    "<tr><th>種類</th><th>説明</th></tr>"
                    "<tr><td>LEFT OUTER JOIN</td><td>左テーブルの全行を返す。右に一致なければ NULL</td></tr>"
                    "<tr><td>RIGHT OUTER JOIN</td><td>右テーブルの全行を返す。左に一致なければ NULL</td></tr>"
                    "<tr><td>FULL OUTER JOIN</td><td>両テーブルの全行を返す。一致なければ NULL</td></tr>"
                    "</table>"
                    "<pre><code>-- 部署なし従業員も含めて表示（LEFT OUTER JOIN）\n"
                    "SELECT e.LAST_NAME, d.DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES e\n"
                    "LEFT OUTER JOIN DEPARTMENTS d\n"
                    "ON     e.DEPARTMENT_ID = d.DEPARTMENT_ID;\n\n"
                    "-- 従業員のいない部署も含めて表示（RIGHT OUTER JOIN）\n"
                    "SELECT e.LAST_NAME, d.DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES e\n"
                    "RIGHT OUTER JOIN DEPARTMENTS d\n"
                    "ON     e.DEPARTMENT_ID = d.DEPARTMENT_ID;\n\n"
                    "-- Oracle 独自の外部結合記法（(+) 記号）\n"
                    "SELECT e.LAST_NAME, d.DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES e, DEPARTMENTS d\n"
                    "WHERE  e.DEPARTMENT_ID = d.DEPARTMENT_ID(+);</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "Oracle 独自の (+) 記法では、NULL を補完したい側（右テーブル相当）に (+) を付けます。"
                    "FULL OUTER JOIN は (+) 記法では表現できません。"
                    "OUTER は省略可能（LEFT JOIN でも外部結合になる）。"
                    "</div>"
                )
            },
            {
                "name": "自己結合とクロス結合",
                "topics": ["自己結合", "SELF JOIN", "CROSS JOIN", "クロス結合", "エイリアス"],
                "content": (
                    "<h3>自己結合（SELF JOIN）</h3>"
                    "<p>同じテーブルを異なるエイリアスで2回参照して結合します。階層データ（上司-部下など）の取得に使います。</p>"
                    "<pre><code>-- 従業員とその上司の名前を表示\n"
                    "SELECT e.LAST_NAME AS 従業員,\n"
                    "       m.LAST_NAME AS 上司\n"
                    "FROM   EMPLOYEES e\n"
                    "LEFT JOIN EMPLOYEES m\n"
                    "ON     e.MANAGER_ID = m.EMPLOYEE_ID;</code></pre>"
                    "<h3>クロス結合（CROSS JOIN）</h3>"
                    "<p>CROSS JOIN は全行の組み合わせを返します（直積）。結果行数 = テーブル1の行数 x テーブル2の行数。</p>"
                    "<pre><code>-- CROSS JOIN（ANSI 形式）\n"
                    "SELECT e.LAST_NAME, d.DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES e\n"
                    "CROSS JOIN DEPARTMENTS d;\n\n"
                    "-- 旧来の表記（WHERE 句なし）\n"
                    "SELECT e.LAST_NAME, d.DEPARTMENT_NAME\n"
                    "FROM   EMPLOYEES e, DEPARTMENTS d;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "自己結合では必ずテーブルエイリアスが必要です。"
                    "クロス結合は意図せず WHERE を省略した場合にも発生するため注意が必要です。"
                    "上司が存在しない場合（社長など）は MANAGER_ID が NULL になるため、"
                    "INNER JOIN ではなく LEFT JOIN を使うと全員が表示されます。"
                    "</div>"
                )
            }
        ]
    },

    "D6": {
        "title": "サブクエリ",
        "intro": "SELECT 文の中に別の SELECT 文を入れ子にするサブクエリの書き方と使いどころを学びます。",
        "sections": [
            {
                "name": "単一行サブクエリ",
                "topics": ["サブクエリ", "単一行サブクエリ", "スカラーサブクエリ"],
                "content": (
                    "<h3>サブクエリとは</h3>"
                    "<p>サブクエリは SELECT 文の中に入れ子にした別の SELECT 文です。"
                    "内側のクエリ（サブクエリ）が先に実行され、その結果を外側のクエリが使います。</p>"
                    "<h3>単一行サブクエリ</h3>"
                    "<p>1行1列だけを返すサブクエリ。= や &gt; などの比較演算子と組み合わせます。</p>"
                    "<pre><code>-- Abel と同じ部署の従業員\n"
                    "SELECT LAST_NAME, DEPARTMENT_ID\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  DEPARTMENT_ID = (\n"
                    "    SELECT DEPARTMENT_ID\n"
                    "    FROM   EMPLOYEES\n"
                    "    WHERE  LAST_NAME = 'Abel'\n"
                    ");\n\n"
                    "-- 最低給与よりも多く稼ぐ従業員\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  SALARY > (\n"
                    "    SELECT MIN(SALARY)\n"
                    "    FROM   EMPLOYEES\n"
                    ");</code></pre>"
                    "<h3>スカラーサブクエリ</h3>"
                    "<p>SELECT リストや WHERE 句で1値を返すサブクエリです。</p>"
                    "<pre><code>SELECT LAST_NAME,\n"
                    "       SALARY,\n"
                    "       (SELECT AVG(SALARY) FROM EMPLOYEES) AS 全体平均\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "単一行サブクエリが複数行を返すと ORA-01427 エラーになります。"
                    "スカラーサブクエリが0行を返す場合は NULL が返ります。"
                    "</div>"
                )
            },
            {
                "name": "複数行サブクエリ",
                "topics": ["複数行サブクエリ", "IN", "ANY", "ALL", "NOT IN"],
                "content": (
                    "<h3>複数行サブクエリ</h3>"
                    "<p>複数行を返すサブクエリには IN, ANY, ALL などの演算子を使います。</p>"
                    "<table class='summary-table'>"
                    "<tr><th>演算子</th><th>説明</th></tr>"
                    "<tr><td>IN</td><td>リストのどれかと等しい</td></tr>"
                    "<tr><td>NOT IN</td><td>リストのどれとも等しくない</td></tr>"
                    "<tr><td>ANY (SOME)</td><td>リストの少なくとも1つと比較条件を満たす</td></tr>"
                    "<tr><td>ALL</td><td>リストのすべての値と比較条件を満たす</td></tr>"
                    "</table>"
                    "<pre><code>-- 部署 20 または 50 のジョブ ID のいずれかに一致する従業員\n"
                    "SELECT LAST_NAME, JOB_ID\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  JOB_ID IN (\n"
                    "    SELECT JOB_ID\n"
                    "    FROM   EMPLOYEES\n"
                    "    WHERE  DEPARTMENT_ID IN (20, 50)\n"
                    ");\n\n"
                    "-- ANY: 部署 50 の誰かより給与が多い\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  SALARY > ANY (\n"
                    "    SELECT SALARY\n"
                    "    FROM   EMPLOYEES\n"
                    "    WHERE  DEPARTMENT_ID = 50\n"
                    ");\n\n"
                    "-- ALL: 部署 50 の全員より給与が多い\n"
                    "SELECT LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  SALARY > ALL (\n"
                    "    SELECT SALARY\n"
                    "    FROM   EMPLOYEES\n"
                    "    WHERE  DEPARTMENT_ID = 50\n"
                    ");</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "NOT IN のリストに NULL が含まれると、結果は0行になります（NULL との比較が不定のため）。"
                    "&gt; ANY は「最小値より大きい」、&gt; ALL は「最大値より大きい」と覚えましょう。"
                    "</div>"
                )
            },
            {
                "name": "集合演算子（UNION / INTERSECT / MINUS）",
                "topics": ["UNION", "UNION ALL", "INTERSECT", "MINUS", "集合演算子"],
                "content": (
                    "<h3>集合演算子の基本</h3>"
                    "<p>複数の SELECT 結果を集合として結合・比較します。SELECT の列数とデータ型互換が必要です。</p>"
                    "<table class='summary-table'>"
                    "<tr><th>演算子</th><th>説明</th></tr>"
                    "<tr><td>UNION</td><td>重複を除去して結合</td></tr>"
                    "<tr><td>UNION ALL</td><td>重複を保持して結合</td></tr>"
                    "<tr><td>INTERSECT</td><td>共通部分のみ抽出</td></tr>"
                    "<tr><td>MINUS</td><td>左にあり右にない行を抽出</td></tr>"
                    "</table>"
                    "<pre><code>-- 部署10と20の従業員IDを統合（重複除去）\n"
                    "SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 10\n"
                    "UNION\n"
                    "SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 20;\n\n"
                    "-- 重複を保持して統合\n"
                    "SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 10\n"
                    "UNION ALL\n"
                    "SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 20;\n\n"
                    "-- 共通する JOB_ID\n"
                    "SELECT JOB_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 10\n"
                    "INTERSECT\n"
                    "SELECT JOB_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 20;\n\n"
                    "-- 部署10にいて部署20にはいない従業員\n"
                    "SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 10\n"
                    "MINUS\n"
                    "SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = 20;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "重複排除が不要なら UNION ALL が高速です。"
                    "ORDER BY は原則として最後の SELECT 全体に対して1回だけ指定します。"
                    "</div>"
                )
            },
            {
                "name": "相関サブクエリとEXISTS",
                "topics": ["EXISTS", "NOT EXISTS", "相関サブクエリ", "相関"],
                "content": (
                    "<h3>相関サブクエリ</h3>"
                    "<p>外側のクエリの列を参照するサブクエリです。外側の行ごとに繰り返し実行されます。</p>"
                    "<pre><code>-- 自分の部署の平均給与より高い従業員\n"
                    "SELECT o.LAST_NAME, o.SALARY, o.DEPARTMENT_ID\n"
                    "FROM   EMPLOYEES o\n"
                    "WHERE  o.SALARY > (\n"
                    "    SELECT AVG(i.SALARY)\n"
                    "    FROM   EMPLOYEES i\n"
                    "    WHERE  i.DEPARTMENT_ID = o.DEPARTMENT_ID\n"
                    ");</code></pre>"
                    "<h3>EXISTS / NOT EXISTS</h3>"
                    "<p>EXISTS はサブクエリが1行以上返す場合に真になります。IN より効率的な場合があります。</p>"
                    "<pre><code>-- 部下が存在する従業員（管理職）\n"
                    "SELECT e.LAST_NAME, e.EMPLOYEE_ID\n"
                    "FROM   EMPLOYEES e\n"
                    "WHERE  EXISTS (\n"
                    "    SELECT 1\n"
                    "    FROM   EMPLOYEES sub\n"
                    "    WHERE  sub.MANAGER_ID = e.EMPLOYEE_ID\n"
                    ");\n\n"
                    "-- 部下がいない従業員\n"
                    "SELECT e.LAST_NAME, e.EMPLOYEE_ID\n"
                    "FROM   EMPLOYEES e\n"
                    "WHERE  NOT EXISTS (\n"
                    "    SELECT 1\n"
                    "    FROM   EMPLOYEES sub\n"
                    "    WHERE  sub.MANAGER_ID = e.EMPLOYEE_ID\n"
                    ");</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "EXISTS はサブクエリが行を返すかどうかだけを確認するため、SELECT リストは SELECT 1 や SELECT * でも問題ありません。"
                    "NOT IN と NOT EXISTS は NULL の扱いが異なります。NOT IN は NULL が含まれると0行ですが、"
                    "NOT EXISTS は NULL の影響を受けません。"
                    "</div>"
                )
            }
        ]
    },

    "D7": {
        "title": "DML（データ操作言語）",
        "intro": "INSERT, UPDATE, DELETE でデータを変更する方法と、COMMIT/ROLLBACK によるトランザクション管理を学びます。",
        "sections": [
            {
                "name": "INSERT と UPDATE",
                "topics": ["INSERT", "UPDATE", "SET", "VALUES", "INSERT INTO SELECT"],
                "content": (
                    "<h3>INSERT 文</h3>"
                    "<p>テーブルに新しい行を追加します。</p>"
                    "<pre><code>-- 全列に値を挿入（列リストを省略）\n"
                    "INSERT INTO DEPARTMENTS\n"
                    "VALUES (280, 'New Dept', 100, 1700);\n\n"
                    "-- 指定した列のみ挿入\n"
                    "INSERT INTO DEPARTMENTS (DEPARTMENT_ID, DEPARTMENT_NAME)\n"
                    "VALUES (290, 'Another Dept');\n\n"
                    "-- サブクエリを使った一括挿入\n"
                    "INSERT INTO SALES_REPS (EMP_ID, NAME, SALARY)\n"
                    "SELECT EMPLOYEE_ID, LAST_NAME, SALARY\n"
                    "FROM   EMPLOYEES\n"
                    "WHERE  JOB_ID = 'SA_REP';</code></pre>"
                    "<h3>UPDATE 文</h3>"
                    "<p>既存の行のデータを変更します。WHERE がないと全行が更新されます。</p>"
                    "<pre><code>-- 特定の行を更新\n"
                    "UPDATE EMPLOYEES\n"
                    "SET    SALARY = SALARY * 1.1,\n"
                    "       COMMISSION_PCT = 0.05\n"
                    "WHERE  DEPARTMENT_ID = 50;\n\n"
                    "-- サブクエリを使った更新\n"
                    "UPDATE EMPLOYEES\n"
                    "SET    DEPARTMENT_ID = (\n"
                    "           SELECT DEPARTMENT_ID\n"
                    "           FROM   DEPARTMENTS\n"
                    "           WHERE  DEPARTMENT_NAME = 'Sales'\n"
                    "       )\n"
                    "WHERE  EMPLOYEE_ID = 100;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "INSERT の列リストを省略する場合は、テーブル定義の列順に全列分の値を指定する必要があります。"
                    "UPDATE で WHERE を省略すると全行が更新されます（意図しない全件更新に注意）。"
                    "</div>"
                )
            },
            {
                "name": "DELETE・TRUNCATE とトランザクション",
                "topics": ["DELETE", "TRUNCATE", "COMMIT", "ROLLBACK", "SAVEPOINT", "トランザクション"],
                "content": (
                    "<h3>DELETE 文</h3>"
                    "<pre><code>-- 条件に合う行を削除\n"
                    "DELETE FROM DEPARTMENTS\n"
                    "WHERE  DEPARTMENT_ID = 290;\n\n"
                    "-- 全行削除（ROLLBACK 可能）\n"
                    "DELETE FROM COPY_EMPLOYEES;</code></pre>"
                    "<h3>TRUNCATE 文</h3>"
                    "<pre><code>-- テーブルの全データを高速削除（DDL、ROLLBACK 不可）\n"
                    "TRUNCATE TABLE COPY_EMPLOYEES;</code></pre>"
                    "<table class='summary-table'>"
                    "<tr><th>比較</th><th>DELETE</th><th>TRUNCATE</th></tr>"
                    "<tr><td>分類</td><td>DML</td><td>DDL</td></tr>"
                    "<tr><td>ROLLBACK</td><td>可能</td><td>不可</td></tr>"
                    "<tr><td>WHERE 句</td><td>使用可能</td><td>使用不可（全件削除のみ）</td></tr>"
                    "<tr><td>処理速度</td><td>低速（ログ記録あり）</td><td>高速（ログ記録なし）</td></tr>"
                    "<tr><td>AUTOCOMMIT</td><td>なし</td><td>あり（暗黙的COMMIT）</td></tr>"
                    "</table>"
                    "<h3>トランザクション制御</h3>"
                    "<pre><code>-- データ変更\n"
                    "UPDATE EMPLOYEES SET SALARY = 5000 WHERE EMPLOYEE_ID = 100;\n\n"
                    "-- セーブポイント設定\n"
                    "SAVEPOINT update_done;\n\n"
                    "-- 追加の変更\n"
                    "DELETE FROM EMPLOYEES WHERE EMPLOYEE_ID = 200;\n\n"
                    "-- セーブポイントまで戻す\n"
                    "ROLLBACK TO update_done;\n\n"
                    "-- 確定\n"
                    "COMMIT;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "TRUNCATE は DDL なので暗黙的 COMMIT が行われます。ROLLBACK できません。"
                    "DDL 文（CREATE, ALTER, DROP 等）を実行すると、直前の未コミットの DML が自動的に COMMIT されます。"
                    "SAVEPOINT はトランザクション内の特定の時点に戻すためのマーカーです。"
                    "</div>"
                )
            },
            {
                "name": "MERGE とマルチテーブル挿入",
                "topics": ["MERGE", "WHEN MATCHED", "WHEN NOT MATCHED", "マルチテーブルINSERT"],
                "content": (
                    "<h3>MERGE 文（UPSERT）</h3>"
                    "<p>一致すれば UPDATE、なければ INSERT を1文で実行します。</p>"
                    "<pre><code>MERGE INTO SALES_TARGET t\n"
                    "USING (SELECT 10 AS DEPT_ID, 1200000 AS TARGET_AMT FROM DUAL) s\n"
                    "ON (t.DEPT_ID = s.DEPT_ID)\n"
                    "WHEN MATCHED THEN\n"
                    "  UPDATE SET t.TARGET_AMT = s.TARGET_AMT\n"
                    "WHEN NOT MATCHED THEN\n"
                    "  INSERT (DEPT_ID, TARGET_AMT)\n"
                    "  VALUES (s.DEPT_ID, s.TARGET_AMT);</code></pre>"
                    "<h3>マルチテーブル INSERT</h3>"
                    "<p>1つのソース結果を条件で複数テーブルへ振り分けます。</p>"
                    "<pre><code>INSERT ALL\n"
                    "  WHEN SALARY &gt;= 10000 THEN\n"
                    "    INTO HIGH_SAL (EMP_ID, SALARY) VALUES (EMPLOYEE_ID, SALARY)\n"
                    "  WHEN SALARY &lt; 10000 THEN\n"
                    "    INTO LOW_SAL (EMP_ID, SALARY) VALUES (EMPLOYEE_ID, SALARY)\n"
                    "SELECT EMPLOYEE_ID, SALARY\n"
                    "FROM   EMPLOYEES;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "MERGE は ON 条件で一致判定し、WHEN MATCHED / WHEN NOT MATCHED を使い分けます。"
                    "大量同期処理で UPDATE+INSERT を分けるより保守しやすいケースが多いです。"
                    "</div>"
                )
            }
        ]
    },

    "D8": {
        "title": "DDL・オブジェクト管理",
        "intro": "テーブルやオブジェクトの作成・変更・削除など、データ定義言語（DDL）とデータベースオブジェクトの管理を学びます。",
        "sections": [
            {
                "name": "CREATE TABLE と制約",
                "topics": ["CREATE TABLE", "ALTER TABLE", "DROP TABLE", "PRIMARY KEY", "FOREIGN KEY", "NOT NULL", "UNIQUE", "CHECK", "DEFAULT"],
                "content": (
                    "<h3>CREATE TABLE の基本</h3>"
                    "<pre><code>CREATE TABLE EMPLOYEES (\n"
                    "    EMPLOYEE_ID   NUMBER(6)     CONSTRAINT emp_pk PRIMARY KEY,\n"
                    "    FIRST_NAME    VARCHAR2(20),\n"
                    "    LAST_NAME     VARCHAR2(25)  CONSTRAINT emp_lname_nn NOT NULL,\n"
                    "    EMAIL         VARCHAR2(25)  CONSTRAINT emp_email_uk UNIQUE,\n"
                    "    HIRE_DATE     DATE          DEFAULT SYSDATE,\n"
                    "    SALARY        NUMBER(8,2)   CONSTRAINT emp_salary_ck CHECK (SALARY > 0),\n"
                    "    DEPARTMENT_ID NUMBER(4)     CONSTRAINT emp_dept_fk\n"
                    "                               REFERENCES DEPARTMENTS(DEPARTMENT_ID)\n"
                    ");</code></pre>"
                    "<h3>制約の種類</h3>"
                    "<table class='summary-table'>"
                    "<tr><th>制約</th><th>説明</th></tr>"
                    "<tr><td>PRIMARY KEY</td><td>行を一意に識別。NOT NULL + UNIQUE の組み合わせ</td></tr>"
                    "<tr><td>FOREIGN KEY</td><td>別テーブルの主キーを参照。参照整合性を保証</td></tr>"
                    "<tr><td>UNIQUE</td><td>列の値を一意に保つ（NULL は複数可）</td></tr>"
                    "<tr><td>NOT NULL</td><td>NULL 値を禁止する</td></tr>"
                    "<tr><td>CHECK</td><td>列の値が条件を満たすことを保証</td></tr>"
                    "<tr><td>DEFAULT</td><td>値が指定されない場合のデフォルト値（制約ではなく列オプション）</td></tr>"
                    "</table>"
                    "<h3>ALTER TABLE / DROP TABLE</h3>"
                    "<pre><code>-- 列の追加\n"
                    "ALTER TABLE EMPLOYEES ADD (NOTES VARCHAR2(100));\n\n"
                    "-- 列の変更\n"
                    "ALTER TABLE EMPLOYEES MODIFY (FIRST_NAME VARCHAR2(30));\n\n"
                    "-- 列の削除\n"
                    "ALTER TABLE EMPLOYEES DROP COLUMN NOTES;\n\n"
                    "-- テーブルの削除（データも削除）\n"
                    "DROP TABLE COPY_EMPLOYEES;\n\n"
                    "-- テーブルの削除（PURGE: ごみ箱に入れない）\n"
                    "DROP TABLE COPY_EMPLOYEES PURGE;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "PRIMARY KEY は1テーブルに1つだけ設定可能です。UNIQUE は複数可。"
                    "FOREIGN KEY の参照先テーブルを削除するには ON DELETE CASCADE または先に子テーブルを削除する必要があります。"
                    "DROP TABLE はデフォルトでごみ箱（RECYCLEBIN）に入り、FLASHBACK TABLE で復元可能です。"
                    "</div>"
                )
            },
            {
                "name": "VIEW・SEQUENCE・INDEX",
                "topics": ["VIEW", "CREATE VIEW", "SEQUENCE", "NEXTVAL", "CURRVAL", "INDEX", "SYNONYM"],
                "content": (
                    "<h3>VIEW（ビュー）</h3>"
                    "<p>ビューは保存された SELECT 文です。テーブルのようにアクセスできます。</p>"
                    "<pre><code>-- ビューの作成\n"
                    "CREATE VIEW emp_dept_vu AS\n"
                    "    SELECT e.EMPLOYEE_ID, e.LAST_NAME, e.DEPARTMENT_ID,\n"
                    "           d.DEPARTMENT_NAME\n"
                    "    FROM   EMPLOYEES e\n"
                    "    JOIN   DEPARTMENTS d\n"
                    "    ON     e.DEPARTMENT_ID = d.DEPARTMENT_ID;\n\n"
                    "-- ビューの使用\n"
                    "SELECT * FROM emp_dept_vu WHERE DEPARTMENT_NAME = 'Sales';\n\n"
                    "-- ビューの削除\n"
                    "DROP VIEW emp_dept_vu;</code></pre>"
                    "<h3>SEQUENCE（シーケンス）</h3>"
                    "<p>シーケンスは連番を生成するオブジェクトです。主キーの自動採番に使います。</p>"
                    "<pre><code>-- シーケンスの作成\n"
                    "CREATE SEQUENCE emp_seq\n"
                    "    START WITH 1\n"
                    "    INCREMENT BY 1\n"
                    "    MAXVALUE 99999\n"
                    "    NOCACHE\n"
                    "    NOCYCLE;\n\n"
                    "-- 次の値を取得（NEXTVAL）\n"
                    "INSERT INTO EMPLOYEES (EMPLOYEE_ID, LAST_NAME)\n"
                    "VALUES (emp_seq.NEXTVAL, 'Smith');\n\n"
                    "-- 現在の値を確認（CURRVAL: NEXTVAL を1度呼んだ後のみ使用可）\n"
                    "SELECT emp_seq.CURRVAL FROM DUAL;</code></pre>"
                    "<h3>INDEX（インデックス）</h3>"
                    "<pre><code>-- インデックスの作成\n"
                    "CREATE INDEX emp_lname_idx\n"
                    "ON EMPLOYEES (LAST_NAME);\n\n"
                    "-- インデックスの削除\n"
                    "DROP INDEX emp_lname_idx;</code></pre>"
                    "<h3>SYNONYM（シノニム）</h3>"
                    "<pre><code>-- パブリックシノニムの作成（DBA 権限が必要）\n"
                    "CREATE PUBLIC SYNONYM emp FOR EMPLOYEES;\n\n"
                    "-- プライベートシノニム\n"
                    "CREATE SYNONYM emp FOR EMPLOYEES;\n\n"
                    "-- シノニムの削除\n"
                    "DROP SYNONYM emp;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "CURRVAL は NEXTVAL を同じセッションで1回以上呼び出してから使用できます。"
                    "シーケンスに CACHE を設定するとシステム障害時に番号が欠番になることがあります。"
                    "INDEX は検索を高速化しますが、INSERT/UPDATE/DELETE は遅くなります。"
                    "PRIMARY KEY と UNIQUE 制約を作成すると、自動的にインデックスが作成されます。"
                    "</div>"
                )
            },
            {
                "name": "権限・ロール・辞書ビュー・タイムゾーン",
                "topics": ["GRANT", "REVOKE", "ROLE", "USER_TABLES", "ALL_TAB_COLUMNS", "CURRENT_TIMESTAMP", "AT TIME ZONE", "INTERVAL"],
                "content": (
                    "<h3>権限とロール</h3>"
                    "<pre><code>-- 権限付与\n"
                    "GRANT SELECT, INSERT ON EMPLOYEES TO app_user;\n\n"
                    "-- ロール作成と付与\n"
                    "CREATE ROLE report_reader;\n"
                    "GRANT SELECT ON EMPLOYEES TO report_reader;\n"
                    "GRANT report_reader TO app_user;\n\n"
                    "-- 権限の剥奪\n"
                    "REVOKE INSERT ON EMPLOYEES FROM app_user;</code></pre>"
                    "<h3>データ・ディクショナリ・ビュー</h3>"
                    "<pre><code>-- 自スキーマの表一覧\n"
                    "SELECT TABLE_NAME FROM USER_TABLES ORDER BY TABLE_NAME;\n\n"
                    "-- 参照可能な列定義\n"
                    "SELECT OWNER, TABLE_NAME, COLUMN_NAME, DATA_TYPE\n"
                    "FROM   ALL_TAB_COLUMNS\n"
                    "WHERE  TABLE_NAME = 'EMPLOYEES';</code></pre>"
                    "<h3>日時・タイムゾーン</h3>"
                    "<pre><code>-- 現在日時（セッションタイムゾーン）\n"
                    "SELECT CURRENT_DATE, CURRENT_TIMESTAMP FROM DUAL;\n\n"
                    "-- タイムゾーン変換\n"
                    "SELECT CURRENT_TIMESTAMP AT TIME ZONE '+00:00' AS UTC_TIME\n"
                    "FROM   DUAL;\n\n"
                    "-- INTERVAL の利用例\n"
                    "SELECT CURRENT_TIMESTAMP + INTERVAL '2' HOUR AS PLUS_2H\n"
                    "FROM   DUAL;</code></pre>"
                    "<div class='tip-box'>"
                    "<strong>試験のポイント：</strong> "
                    "権限は最小権限で付与し、役割単位ではロールを使います。"
                    "辞書ビュー（USER_/ALL_/DBA_）は参照範囲が異なります。"
                    "CURRENT_TIMESTAMP はタイムゾーンを保持し、AT TIME ZONE で変換できます。"
                    "</div>"
                )
            }
        ]
    }
}


class TextbookArchitect:
    def __init__(self, data_file: str, output_dir: str):
        self.data_file = data_file
        self.output_dir = output_dir
        self.problems = self._load_problems()
        os.makedirs(output_dir, exist_ok=True)

    def _load_problems(self):
        """initial_state.js から問題データを読み込む"""
        try:
            with open(self.data_file, encoding="utf-8") as f:
                raw = f.read()
            # window.dataBuffer = [...] の形式をパース
            match = re.search(r'window\.dataBuffer\s*=\s*(\[.*?\]);', raw, re.DOTALL)
            if match:
                data = json.loads(match.group(1))
                logger.info(f"問題データ {len(data)} 件を読み込みました")
                return data
        except Exception as e:
            logger.warning(f"問題データの読み込みに失敗しました: {e}")
        return []

    def find_problems_for_section(self, domain_code: str, section_topics: list) -> list:
        """ドメインとトピックに関連する問題を検索する"""
        if not self.problems:
            return []
        matched = []
        seen_ids = set()
        for p in self.problems:
            # ドメインフィルタ（例: D1 の問題のみ D1 セクションに表示）
            cat = p.get("category", "")
            if not cat.startswith(domain_code):
                continue
            pid = p.get("id", "")
            if pid in seen_ids:
                continue
            combined = " ".join([
                p.get("text", ""),
                p.get("logic", ""),
                " ".join(p.get("tags", []))
            ]).lower()
            for topic in section_topics:
                if topic.lower() in combined:
                    matched.append(p)
                    seen_ids.add(pid)
                    break
        return matched[:3]  # 最大3問

    def _render_problem_card(self, problem: dict, idx: int) -> str:
        """問題カードのHTMLを生成する"""
        qid = problem.get("id", f"Q{idx+1}")
        question = problem.get("text", "").replace("\n", "<br>")
        choices = problem.get("options", [])
        answer = problem.get("answer", "")
        explanation = problem.get("logic", "")

        choices_html = ""
        for c in choices:
            choices_html += f"<li>{c}</li>"

        return (
            f'<div class="problem-card" id="prob-{qid}">'
            f'<div class="problem-header">問題 {idx+1} <span class="qid">#{qid}</span></div>'
            f'<p class="problem-text">{question}</p>'
            f'<ul class="choices">{choices_html}</ul>'
            f'<details class="answer-details">'
            f'<summary>解答・解説を見る</summary>'
            f'<div class="answer-content">'
            f'<p><strong>正解:</strong> {answer}</p>'
            f'<p>{explanation}</p>'
            f'</div>'
            f'</details>'
            f'</div>'
        )

    def _get_css(self) -> str:
        return """
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f5f7fa; color: #2d3748; line-height: 1.7; }
        .page-header {
            background: linear-gradient(135deg, #c0392b 0%, #e74c3c 50%, #e67e22 100%);
            color: white; padding: 40px 24px; text-align: center;
        }
        .page-header h1 { font-size: 2rem; margin-bottom: 8px; }
        .page-header .subtitle { opacity: 0.9; font-size: 1rem; }
        .container { max-width: 960px; margin: 0 auto; padding: 24px; }
        .section-card {
            background: white; border-radius: 12px; padding: 28px;
            margin-bottom: 32px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .section-title {
            font-size: 1.3rem; font-weight: 700; color: #c0392b;
            margin-bottom: 16px; padding-bottom: 8px;
            border-bottom: 3px solid #e74c3c;
        }
        .topic-chips { margin-bottom: 16px; display: flex; flex-wrap: wrap; gap: 6px; }
        .chip {
            background: #fdf2f8; color: #c0392b; border: 1px solid #f0a0a0;
            padding: 2px 10px; border-radius: 20px; font-size: 0.8rem;
        }
        pre { background: #1e293b; color: #e2e8f0; padding: 16px; border-radius: 8px; overflow-x: auto; margin: 12px 0; }
        code { font-family: 'Consolas', 'Monaco', monospace; font-size: 0.88rem; }
        p code { background: #f0f4f8; color: #c0392b; padding: 1px 5px; border-radius: 4px; }
        .tip-box {
            background: #fffde7; border-left: 4px solid #f9a825;
            padding: 12px 16px; border-radius: 0 8px 8px 0; margin: 12px 0;
        }
        .warning-box {
            background: #fce4ec; border-left: 4px solid #e91e63;
            padding: 12px 16px; border-radius: 0 8px 8px 0; margin: 12px 0;
        }
        .summary-table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 0.9rem; }
        .summary-table th {
            background: #c0392b; color: white; padding: 8px 12px; text-align: left;
        }
        .summary-table td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; }
        .summary-table tr:nth-child(even) td { background: #f9fafb; }
        h3 { font-size: 1.05rem; color: #2d3748; margin: 16px 0 8px; }
        .problem-section-title {
            font-size: 1.1rem; font-weight: 700; color: #2d3748;
            margin: 28px 0 12px; padding-bottom: 6px;
            border-bottom: 2px solid #e2e8f0;
        }
        .problem-card {
            background: #f9fafb; border: 1px solid #e2e8f0;
            border-radius: 8px; padding: 16px; margin-bottom: 16px;
        }
        .problem-header { font-weight: 700; color: #c0392b; margin-bottom: 8px; }
        .qid { font-size: 0.8rem; color: #718096; font-weight: 400; margin-left: 8px; }
        .problem-text { margin-bottom: 10px; }
        .choices { padding-left: 20px; margin-bottom: 10px; }
        .choices li { margin: 4px 0; }
        .answer-details summary {
            cursor: pointer; color: #c0392b; font-weight: 600;
            padding: 6px 0; user-select: none;
        }
        .answer-content { background: white; padding: 12px; border-radius: 6px; margin-top: 8px; }
        .breadcrumb { padding: 12px 24px; background: white; border-bottom: 1px solid #e2e8f0; font-size: 0.85rem; }
        .breadcrumb a { color: #c0392b; text-decoration: none; }
        .intro-box { background: #fff8f8; border: 1px solid #f0a0a0; border-radius: 8px; padding: 16px; margin-bottom: 24px; }
        """

    def _generate_domain_html(self, domain_id: str) -> str:
        data = TEXTBOOK_CONTENT[domain_id]
        title = data["title"]
        intro = data["intro"]
        sections = data["sections"]

        sections_html = ""
        for sec in sections:
            topics = sec["topics"]
            problems = self.find_problems_for_section(domain_id, topics)

            chips = "".join(f'<span class="chip">{t}</span>' for t in topics)

            problems_html = ""
            if problems:
                probs_inner = "".join(self._render_problem_card(p, i) for i, p in enumerate(problems))
                problems_html = (
                    f'<div class="problem-section-title">練習問題</div>'
                    f'{probs_inner}'
                )

            sections_html += (
                f'<div class="section-card">'
                f'<div class="section-title">{sec["name"]}</div>'
                f'<div class="topic-chips">{chips}</div>'
                f'<div class="section-content">{sec["content"]}</div>'
                f'{problems_html}'
                f'</div>'
            )

        css = self._get_css()
        return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{domain_id}: {title} | Oracle SQL 教科書</title>
<style>{css}</style>
</head>
<body>
<div class="breadcrumb">
  <a href="index.html">Oracle SQL 教科書</a> &gt; {domain_id}: {title}
</div>
<div class="page-header">
  <h1>{domain_id}: {title}</h1>
  <div class="subtitle">Oracle Database SQL (1Z0-071) 対策</div>
</div>
<div class="container">
  <div class="intro-box">{intro}</div>
  {sections_html}
</div>
</body>
</html>"""

    def _generate_index_html(self) -> str:
        cards_html = (
            '<div class="index-card">'
            '<a href="Oracle_DBA_Silver_SQL_Textbook.html">'
            '<div class="card-domain">FULL</div>'
            '<div class="card-title">Oracle DBA Silver SQL 総合教科書</div>'
            '<div class="card-sections">目次1〜16章対応 / 実務例つき / JS無効閲覧対応 / HTTPS公開方針</div>'
            '</a>'
            '</div>'
        )
        for domain_id, data in TEXTBOOK_CONTENT.items():
            section_names = " / ".join(s["name"] for s in data["sections"])
            cards_html += (
                f'<div class="index-card">'
                f'<a href="{domain_id}_textbook.html">'
                f'<div class="card-domain">{domain_id}</div>'
                f'<div class="card-title">{data["title"]}</div>'
                f'<div class="card-sections">{section_names}</div>'
                f'</a>'
                f'</div>'
            )

        css = self._get_css()
        extra_css = """
        .index-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; padding: 24px; max-width: 1100px; margin: 0 auto; }
        .index-card { background: white; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow: hidden; transition: transform 0.2s, box-shadow 0.2s; }
        .index-card:hover { transform: translateY(-4px); box-shadow: 0 6px 16px rgba(0,0,0,0.14); }
        .index-card a { display: block; padding: 20px; text-decoration: none; color: inherit; }
        .card-domain { font-size: 1.5rem; font-weight: 900; color: #c0392b; margin-bottom: 6px; }
        .card-title { font-size: 1rem; font-weight: 700; color: #2d3748; margin-bottom: 8px; }
        .card-sections { font-size: 0.78rem; color: #718096; line-height: 1.5; }
        .index-intro { text-align: center; padding: 20px 24px 0; color: #4a5568; font-size: 0.95rem; }
        """
        return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Oracle Database SQL (1Z0-071) 教科書</title>
<style>{css}{extra_css}</style>
</head>
<body>
<div class="page-header">
  <h1>Oracle Database SQL 教科書</h1>
  <div class="subtitle">Oracle Database SQL (1Z0-071) 完全対策</div>
</div>
<p class="index-intro">8つのドメインを体系的に学習できます。各カードをクリックして学習を開始してください。</p>
<div class="index-grid">
  {cards_html}
</div>
</body>
</html>"""

    def generate_all(self):
        """D1〜D8 の HTML と index.html を生成する"""
        generated = []
        for domain_id in TEXTBOOK_CONTENT:
            html = self._generate_domain_html(domain_id)
            filename = f"{domain_id}_textbook.html"
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            logger.info(f"生成: {filepath}")
            generated.append(filepath)

        index_html = self._generate_index_html()
        index_path = os.path.join(self.output_dir, "index.html")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_html)
        logger.info(f"生成: {index_path}")
        generated.append(index_path)

        logger.info(f"完了: {len(generated)} ファイルを生成しました")
        return generated


# ============================================================
# エントリーポイント
# ============================================================
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("使い方: python3 textbook_architect.py <data_file> <output_dir>")
        sys.exit(1)

    data_file = sys.argv[1]
    output_dir = sys.argv[2]

    architect = TextbookArchitect(data_file, output_dir)
    files = architect.generate_all()
    print(f"\n{len(files)} ファイルを生成しました:")
    for f in files:
        print(f"  {f}")
