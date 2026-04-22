#!/usr/bin/env python3
"""Build phased EX reinforce pages from mock exam wrong answers."""
from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "dist" / "mock_exam_data.json").read_text(encoding="utf-8"))

PAGE_MAP = {
    "D5": ("EX1", "複数表の結合"),
    "D6": ("EX2", "サブクエリ・集合演算"),
    "D3": ("EX3", "単一行関数"),
    "D7": ("EX4", "DML・トランザクション"),
    "D8": ("EX5", "DDL・オブジェクト管理"),
    "D4": ("EX6", "グループ関数・集計"),
    "D1": ("EX7", "SQLとRDBの基礎"),
    "D2": ("EX8", "データの絞り込みとソート"),
}

PHASE_LABELS = {
    1: "Phase 1 最優先再構築",
    2: "Phase 2 中位弱点の補修",
    3: "Phase 3 基礎の取りこぼし回収",
}

PRIORITY_COLOR = {"high": "#c0392b", "mid": "#e67e22", "low": "#f1c40f", "ok": "#2ecc71"}
PRIORITY_LABEL = {"high": "最優先", "mid": "優先", "low": "要復習", "ok": "維持"}

CONCEPT_META = {
    "corr_subquery": {
        "title": "相関サブクエリの実行順",
        "why": "相関サブクエリは、外側問い合わせの行を1行ずつ評価し、その行ごとに内側問い合わせを再実行する。非相関サブクエリのように内側が先に1回だけ動くわけではない。",
        "pitfall": "非相関サブクエリの実行順と混同すると、内側先行や内外逆転の選択肢を選びやすい。",
        "rebuild": [
            "外側列を内側が参照していたら、まず相関サブクエリと判断する。",
            "相関=外側1行ごとに内側を再実行、という1文で固定する。",
            "比較演算子が = のまま複数行を返しそうなら、IN や ANY/ALL を疑う。",
        ],
    },
    "union_order": {
        "title": "集合演算と ORDER BY",
        "why": "UNION、INTERSECT、MINUS を使った文では、ORDER BY は最後に1回だけ書ける。列名は先頭 SELECT の列名、または位置番号で指定する。",
        "pitfall": "各 SELECT ごとに ORDER BY が書ける、または任意の列番号を指定できると誤認しやすい。",
        "rebuild": [
            "集合演算の ORDER BY は文末に1回だけと覚える。",
            "位置番号は最終結果の列数の範囲内だけ使える。",
            "ORDER BY の列名は先頭 SELECT 基準で決まる。",
        ],
    },
    "union_vs_unionall": {
        "title": "UNION と UNION ALL の違い",
        "why": "UNION は列数と型をそろえたうえで重複行を削除する。UNION ALL は重複を残し、重複排除のソート処理も行わない。",
        "pitfall": "列名まで完全一致が必要と思い込んだり、UNION ALL でも重複排除やソートが起きると誤解しやすい。",
        "rebuild": [
            "必要なのは列数と対応する型であり、列名一致は必須ではない。",
            "UNION=重複削除あり、UNION ALL=重複削除なしで分けて覚える。",
            "性能面では通常 UNION ALL の方が軽い。",
        ],
    },
    "set_operator_general": {
        "title": "INTERSECT を含む集合演算の基本",
        "why": "複合問合せでは、各 SELECT の列数と対応するデータ型をそろえる必要がある。INTERSECT は両方の結果に共通する行を返し、NULL を含む行も比較対象になる。",
        "pitfall": "列名まで一致必須と思い込んだり、列数・型の一致条件と、INTERSECT が返す行の意味を切り分けられずに失点しやすい。",
        "rebuild": [
            "集合演算はまず『列数一致』『対応型一致』を確認する。",
            "UNION は和、INTERSECT は共通、MINUS は差集合と役割を分ける。",
            "列名は先頭 SELECT 基準で決まり、完全一致は必須ではない。",
        ],
    },
    "minus_set": {
        "title": "MINUS による差集合",
        "why": "片方にはあり、もう片方にはない行を取りたいときは MINUS を使う。一度も取引がない商品や、存在しない組合せの抽出で使う典型論点である。",
        "pitfall": "共通部分を返す INTERSECT や、単なる連結である UNION を差集合と混同しやすい。",
        "rebuild": [
            "A にあって B にない = A MINUS B で固定する。",
            "共通部分は INTERSECT、両方連結は UNION/UNION ALL と切り分ける。",
            "存在確認の代替として NOT EXISTS でも書けるが、差集合を聞かれたら MINUS を優先する。",
        ],
    },
    "scalar_subquery": {
        "title": "スカラサブクエリの制約",
        "why": "スカラサブクエリは1行1列だけを返すサブクエリであり、0行なら NULL、2行以上ならエラーになる。使える句と使えない場所を区別する必要がある。",
        "pitfall": "0行時に 0 を返す、複数列でも使える、どの句でも自由に置けると誤認しやすい。",
        "rebuild": [
            "スカラ=1行1列だけ、と定義から覚える。",
            "0行時は NULL、複数行時はエラーをセットで覚える。",
            "INSERT VALUES や SELECT 句など、式を書ける位置で使う意識を持つ。",
        ],
    },
    "subquery_comparison": {
        "title": "ANY・ALL・平均比較",
        "why": "サブクエリ結果が複数行になるときは、IN、ANY、ALL を使って比較する。部門別平均より高い給与のような問題では、相関サブクエリか集約結果との結合で表現する。",
        "pitfall": "複数行サブクエリに対して = や > をそのまま使ったり、ANY と ALL の意味を逆に覚えやすい。",
        "rebuild": [
            "複数行が返るなら IN/ANY/ALL を考える。",
            "部門別平均より高い、は相関サブクエリか集約結果 JOIN で書く。",
            "ANY はどれか1つ、ALL は全て、という日本語で確認する。",
        ],
    },
    "subquery_usage": {
        "title": "サブクエリが必要になる場面",
        "why": "外側の検索条件で『別の結果を先に求めてから比較する』必要があるとき、サブクエリが必要になる。平均値との比較や、他の検索結果を条件に使う問題が典型である。",
        "pitfall": "単純な集計や結合だけで済む処理までサブクエリ必須だと思い込み、逆に比較対象を先に求める必要がある場面を見落としやすい。",
        "rebuild": [
            "先に別結果を求めて、その値で外側を絞るならサブクエリを疑う。",
            "単なる GROUP BY 集計だけで済む処理と切り分ける。",
            "結合で済むのか、比較用の値生成が必要なのかを日本語で判定する。",
        ],
    },
    "exists_notexists": {
        "title": "EXISTS と NOT IN / NOT EXISTS",
        "why": "EXISTS は行の存在だけを見る。NOT IN はサブクエリ結果に NULL が混ざると全体が不明になりやすいため、存在否定は NOT EXISTS の方が安全である。",
        "pitfall": "EXISTS が列値そのものを返すように感じたり、NOT IN の NULL 罠を見落としやすい。",
        "rebuild": [
            "EXISTS は真偽判定だけなので SELECT 1 で十分と覚える。",
            "除外条件で NULL の可能性があるなら NOT EXISTS を優先する。",
            "存在確認と値比較を別物として扱う。",
        ],
    },
    "multiple_row_subquery": {
        "title": "複数行サブクエリの性質",
        "why": "複数行サブクエリは、複数行を返し得る副問合せであり、WHERE、HAVING、GROUP BY を内部に持つこともできる。比較では IN、ANY、ALL など複数行対応の演算子を使う必要がある。",
        "pitfall": "複数行サブクエリなのに 2 行以上が必須だと思い込んだり、WHERE や GROUP BY を書けないと誤認しやすい。",
        "rebuild": [
            "複数行サブクエリは『複数行になり得る』のであって、常に複数行とは限らない。",
            "内部では WHERE、GROUP BY、HAVING も通常どおり使える。",
            "外側との比較演算子が複数行対応かを必ず確認する。",
        ],
    },
    "self_join_vs_subquery": {
        "title": "自己結合と副問合せの使い分け",
        "why": "同一表内の重複や対応関係を確認するときは、同じ表を別名で比較する自己結合でも、集約や存在確認を使う副問合せでも表現できる。要件に対して成立する手法を見分けるのが論点である。",
        "pitfall": "JOIN の種類に引っ張られて不要な外部結合を選んだり、自己結合で十分な場面を特殊な結合に広げてしまいやすい。",
        "rebuild": [
            "同一表の比較なら、まず自己結合で書けるかを考える。",
            "重複確認や存在確認は副問合せでも書けることを押さえる。",
            "FULL OUTER や LEFT/RIGHT OUTER が本当に必要かを要件から判断する。",
        ],
    },
    "like_case_functions": {
        "title": "LIKE と大文字小文字関数",
        "why": "LIKE の判定では、ワイルドカードの位置と UPPER/LOWER/INITCAP の変換結果を正しく合わせる必要がある。'T' と 'T%' は意味が全く異なる。",
        "pitfall": "LIKE パターンの末尾 % を落としたり、関数適用後の比較文字列まで揃えずに失点しやすい。",
        "rebuild": [
            "前方一致なら 'X%'、部分一致なら '%X%' を機械的に使い分ける。",
            "UPPER(col) を使ったら比較側も UPPER でそろえる。",
            "LIKE と BETWEEN は置き換え不能なことを意識する。",
        ],
    },
    "date_arithmetic": {
        "title": "日付演算と月数計算",
        "why": "DATE 型の差は日数で返る。月単位なら MONTHS_BETWEEN、月加算なら ADD_MONTHS を使う。年数を 365 日換算で書くと境界条件を外しやすい。",
        "pitfall": "日付差と月差を同じように扱ったり、MONTHS_BETWEEN の引数順を逆に覚えやすい。",
        "rebuild": [
            "日数差は date1 - date2、月差は MONTHS_BETWEEN(date1, date2)。",
            "nか月後・前は ADD_MONTHS(date, n) で書く。",
            "条件式では『過去16か月以内』のような日本語を数式に言い換えてから書く。",
        ],
    },
    "conversion_format": {
        "title": "TO_CHAR・TO_NUMBER・TO_DATE の書式変換",
        "why": "文字列として保持された数値や日付を演算するには、まず TO_NUMBER や TO_DATE で型変換し、その後に TO_CHAR で表示形式を整える。書式モデルが一致しなければ失敗する。",
        "pitfall": "変換の向きを逆にしたり、表示書式と内部型の処理順を取り違えやすい。",
        "rebuild": [
            "演算前に元の型へ戻し、表示直前に TO_CHAR で整形する。",
            "書式モデルの桁数、カンマ、小数点位置まで確認する。",
            "TO_CHAR は表示、TO_NUMBER/TO_DATE は演算準備と役割分担で覚える。",
        ],
    },
    "null_case": {
        "title": "NULL 関数と条件式",
        "why": "NVL、NVL2、NULLIF、COALESCE、CASE、DECODE は、NULL や条件分岐を表すための関数群であり、引数順と戻り値の型整合が重要である。",
        "pitfall": "NVL と NVL2 の引数順、CASE と DECODE の使い分け、NULLIF の意味を混同しやすい。",
        "rebuild": [
            "NVL(a,b)=a が NULL なら b、NVL2(a,b,c)=a が NULL でなければ b。",
            "範囲条件や IS NULL は CASE、単純一致だけなら DECODE でもよい。",
            "NULLIF(a,b)=等しければ NULL と声に出して覚える。",
        ],
    },
    "string_extract": {
        "title": "SUBSTR・INSTR・TRIM・REPLACE の使い分け",
        "why": "文字列の一部抽出では、位置取得に INSTR、切り出しに SUBSTR、不要部分の削除に TRIM、置換に REPLACE を使い分ける。空白位置の +1 を忘れると全体がずれる。",
        "pitfall": "位置の起点や切り出し長を誤り、ほぼ正しそうな SQL を選んでしまいやすい。",
        "rebuild": [
            "まず INSTR で位置を求め、その位置を SUBSTR に渡す。",
            "先頭や末尾を削るなら TRIM、途中の語句置換なら REPLACE を使う。",
            "1始まりのインデックスであることを常に意識する。",
        ],
    },
    "numeric_functions": {
        "title": "ROUND・TRUNC・FLOOR などの数値関数",
        "why": "ROUND は四捨五入、TRUNC は切り捨て、FLOOR は指定値以下の最大整数、CEIL は指定値以上の最小整数を返す。関数ごとの戻り値を正確に区別する必要がある。",
        "pitfall": "丸める関数と切り捨てる関数を曖昧に覚えて、似た選択肢を取り違えやすい。",
        "rebuild": [
            "ROUND=四捨五入、TRUNC=切り落とし、FLOOR/CEIL=整数方向と覚える。",
            "小数点桁数指定があるときは第何位を見るのかを書き出す。",
            "日付に対する ROUND/TRUNC も使えることを別で覚える。",
        ],
    },
    "single_row_function_basics": {
        "title": "単一行関数の基本性質",
        "why": "単一行関数は入力 1 行ごとに 1 つの結果を返し、ネストもできる。引数には列、リテラル、式が使え、戻り値の型は引数と異なる場合もある。",
        "pitfall": "引数は 1 つだけ、SELECT 句でしか使えない、戻り値型は同じ、といった表面的な思い込みで落としやすい。",
        "rebuild": [
            "単一行関数は『各行ごとに 1 結果』であって『表全体で 1 行』ではない。",
            "ネスト可、句も SELECT 限定ではないと整理する。",
            "引数型と戻り値型が一致しない関数も多いと覚える。",
        ],
    },
    "default_and_add_column": {
        "title": "DEFAULT と列追加・挿入",
        "why": "DEFAULT は値を省略したときに補われる。既存行がある表へ NOT NULL 列を追加するなら、DEFAULT と NOT NULL をセットで与えないと既存行を満たせない。",
        "pitfall": "DEFAULT 句だけで NOT NULL まで満たせると考えたり、列指定と VALUES 個数の対応を外しやすい。",
        "rebuild": [
            "既存データあり + NOT NULL 列追加 = DEFAULT 必須、と覚える。",
            "INSERT は列リストと VALUES の数を必ず対応させる。",
            "DEFAULT を使うのは『省略時の補完』であり、明示列に勝手には入らない。",
        ],
    },
    "merge_object": {
        "title": "MERGE の文法と使える対象",
        "why": "MERGE は 1 つの対象表に対し、ON 条件で一致時は UPDATE、非一致時は INSERT を行う。USING には表、ビュー、サブクエリを使える。",
        "pitfall": "WHEN MATCHED で INSERT、WHEN NOT MATCHED で UPDATE のように逆向きに書いてしまいがちで、複数表更新もできると誤認しやすい。",
        "rebuild": [
            "MATCHED=UPDATE、NOT MATCHED=INSERT を固定する。",
            "更新対象は 1 表だけ、USING 側は比較用データと覚える。",
            "MERGE でも WHERE 条件付き UPDATE/DELETE やビュー利用可否を確認する。",
        ],
    },
    "ddl_rules": {
        "title": "DDL と DML/TCL の切り分け",
        "why": "CREATE、ALTER、DROP、TRUNCATE などは DDL、INSERT/UPDATE/DELETE/MERGE は DML、COMMIT/ROLLBACK/SAVEPOINT は TCL である。DDL は暗黙コミットを伴う。",
        "pitfall": "TRUNCATE を DML と勘違いしたり、DDL でロールバックできると思い込みやすい。",
        "rebuild": [
            "DDL=定義変更、DML=データ操作、TCL=トランザクション制御で分ける。",
            "TRUNCATE は DDL、DELETE は DML とセットで覚える。",
            "DDL 実行後は暗黙コミットされる点を必ず思い出す。",
        ],
    },
    "constraints": {
        "title": "制約定義と有効化・無効化",
        "why": "主キー、外部キー、CHECK、NOT NULL などの制約は、型や参照整合性を守るための定義である。ENABLE/DISABLE、CASCADE、SYSDATE 使用可否など細部の制約規則が問われる。",
        "pitfall": "CHECK 制約で使える式、主キー無効化時の外部キーへの影響、NULL 許容の違いを曖昧にしやすい。",
        "rebuild": [
            "PK=NOT NULL + UNIQUE、FK は NULL 可、UK も NULL 可を再確認する。",
            "CHECK では SYSDATE や他列参照など使えない式があると覚える。",
            "ENABLE/DISABLE と CASCADE の影響範囲を図で整理する。",
        ],
    },
    "view_rules": {
        "title": "ビューの性質と更新可否",
        "why": "ビューはスキーマオブジェクトであり、基表に依存している。更新可否や WITH CHECK OPTION、READ ONLY、別スキーマ参照可否などが典型論点になる。",
        "pitfall": "ビュー作成時に索引も複製される、基表が消えても常に有効、CHECK OPTION が常時必須、といった誤解が起きやすい。",
        "rebuild": [
            "ビューは定義保存であり、データ本体を持たないことを前提に考える。",
            "更新可否は関数、集合演算、GROUP BY などの有無で判断する。",
            "WITH CHECK OPTION は『ビュー条件を破る更新禁止』のための追加指定と覚える。",
        ],
    },
    "sequence_synonym_index": {
        "title": "シーケンス・シノニム・索引",
        "why": "シーケンスは連番供給、シノニムは別名、索引は検索高速化のためのオブジェクトである。INVISIBLE INDEX、NEXTVAL/CURRVAL、PUBLIC SYNONYM など固有ルールが問われる。",
        "pitfall": "CURRVAL の利用条件、INVISIBLE INDEX の更新有無、シノニムの対象範囲を曖昧にしやすい。",
        "rebuild": [
            "NEXTVAL を使った後でなければ CURRVAL は使えないことを覚える。",
            "INVISIBLE INDEX でも索引自体は更新されると覚える。",
            "シノニムは表だけでなく、ビューやシーケンスなどにも張れる。",
        ],
    },
    "privileges_roles": {
        "title": "権限付与とロール",
        "why": "オブジェクト権限は WITH GRANT OPTION、システム権限は WITH ADMIN OPTION と付与方法が異なる。列単位 UPDATE やロールの扱いも頻出である。",
        "pitfall": "GRANT OPTION と ADMIN OPTION を混同し、列単位権限の構文を取り違えやすい。",
        "rebuild": [
            "表や列への権限は WITH GRANT OPTION と覚える。",
            "列単位 UPDATE は UPDATE (col1, col2) ON table の形で書く。",
            "ロールは権限の束であり、オブジェクト権限そのものとは別だと整理する。",
        ],
    },
    "datetime_types": {
        "title": "DATE・TIMESTAMP・TIME ZONE",
        "why": "DATE は秒まで、TIMESTAMP は小数秒まで、TIMESTAMP WITH TIME ZONE はタイムゾーン情報付き、LOCAL TIME ZONE は DB タイムゾーンで正規化される。CURRENT_TIMESTAMP と SYSTIMESTAMP も基準が異なる。",
        "pitfall": "DATE が小数秒まで持つと勘違いしたり、CURRENT_TIMESTAMP と SYSTIMESTAMP の基準を混同しやすい。",
        "rebuild": [
            "DATE と TIMESTAMP の保持精度をまず分ける。",
            "WITH LOCAL TIME ZONE は保存時に DB タイムゾーンへ正規化される。",
            "CURRENT_TIMESTAMP はセッション、SYSTIMESTAMP はサーバ側で覚える。",
        ],
    },
    "transaction_control": {
        "title": "COMMIT・ROLLBACK・SAVEPOINT",
        "why": "COMMIT は変更確定とロック解放、ROLLBACK TO SAVEPOINT は指定地点以降の変更だけを戻す。SAVEPOINT 自体や以前の SAVEPOINT は残るが、COMMIT 後は全て消える。",
        "pitfall": "ROLLBACK TO SAVEPOINT でロックまで解放される、COMMIT 後も SAVEPOINT が残る、と誤認しやすい。",
        "rebuild": [
            "COMMIT=確定+ロック解放+SAVEPOINT消去。",
            "ROLLBACK TO SAVEPOINT=変更だけ戻す、SAVEPOINTは残る。",
            "完全な ROLLBACK と TO SAVEPOINT を別物として覚える。",
        ],
    },
    "truncate_delete": {
        "title": "TRUNCATE と DELETE の違い",
        "why": "DELETE は DML なので WHERE 条件と ROLLBACK が使える。TRUNCATE は DDL なので高速だが WHERE 句は使えず、ROLLBACK もできない。",
        "pitfall": "TRUNCATE でも一部行を消せる、または ROLLBACK で戻せると考えやすい。",
        "rebuild": [
            "行単位削除と復旧が必要なら DELETE を選ぶ。",
            "表全体の高速初期化なら TRUNCATE を選ぶ。",
            "TRUNCATE は DDL なので暗黙コミットを伴う。",
        ],
    },
    "update_subquery": {
        "title": "UPDATE とサブクエリ",
        "why": "UPDATE の SET 句で相関サブクエリを使うと、更新対象行ごとにサブクエリが評価される。サブクエリが複数行を返せばエラーになる。",
        "pitfall": "サブクエリが先に1回だけ実行されると思い込み、相関性や複数行エラーを見落としやすい。",
        "rebuild": [
            "SET 句内で外側表の列を参照していたら相関サブクエリ。",
            "1行ごとに評価されることを前提に読む。",
            "単一行が保証できないなら結合 UPDATE など別案を考える。",
        ],
    },
    "multitable_insert": {
        "title": "INSERT ALL / FIRST",
        "why": "INSERT ALL は条件に合う全ての INTO に挿入し、INSERT FIRST は最初に一致した INTO だけに挿入する。ELSE 句や条件付き挿入の位置も重要である。",
        "pitfall": "ALL と FIRST の挙動差を曖昧にし、ELSE の有無や条件評価順で失点しやすい。",
        "rebuild": [
            "ALL=全部、FIRST=最初だけ、と1語で覚える。",
            "WHEN 条件と INTO の対応を上から順に追う。",
            "マルチテーブル挿入も DML なので COMMIT が必要。",
        ],
    },
    "merge_dml": {
        "title": "DML としての MERGE",
        "why": "MERGE は DML であり、対象表1つに対して一致/非一致の分岐を行う。UPDATE 対象列、INSERT 条件、DELETE 条件の位置を正しく読む必要がある。",
        "pitfall": "MERGE を DDL と感じたり、ON 条件や WHEN 節の向きを取り違えやすい。",
        "rebuild": [
            "MERGE INTO 対象表 / USING 比較元の構文を固定する。",
            "一致時と非一致時で何が許されるかを整理する。",
            "UPDATE 対象に主キー列を書けるかなど、細部の制約を確認する。",
        ],
    },
    "update_syntax": {
        "title": "UPDATE 文の基本構文",
        "why": "UPDATE は `UPDATE 表名 SET 列1=値1, 列2=値2 WHERE 条件` の形で書く。SET は 1 回だけ書き、列代入はカンマで並べる。",
        "pitfall": "SET を重ねたり、代入列の途中に AND を入れたりして、意味ではなく文法エラーを起こしやすい。",
        "rebuild": [
            "UPDATE の骨格を丸ごと暗記する。",
            "複数列更新は `,` でつなぎ、条件は WHERE に分離する。",
            "日付リテラルや NULL 代入は文法上そのまま書けると確認する。",
        ],
    },
    "self_join": {
        "title": "自己結合",
        "why": "自己結合は同じ表を別名で2回参照する結合であり、表別名が必須である。INNER JOIN にもでき、OUTER JOIN に限定されない。",
        "pitfall": "自己結合だから特殊な JOIN 種類が必須だと思い込み、表別名の必須性を軽視しやすい。",
        "rebuild": [
            "自己結合=同じ表を2回使うので別名必須。",
            "結合条件は ON で素直に書く。",
            "INNER/LEFT/RIGHT などの種類は要件で決める。",
        ],
    },
    "full_outer": {
        "title": "FULL OUTER JOIN",
        "why": "FULL OUTER JOIN は左右両方の表の全行を返し、一致しない側は NULL で埋める。デカルト積ではなく、Oracle 独自の (+) 構文では表現できない。",
        "pitfall": "両表の全行という言葉から全組合せを連想して、デカルト積と混同しやすい。",
        "rebuild": [
            "FULL OUTER = 左全件 + 右全件、ではあるが全組合せではない。",
            "Oracle 独自結合構文 (+) では FULL は書けない。",
            "一致しない側が NULL で埋まる点を必ず確認する。",
        ],
    },
    "join_syntax": {
        "title": "USING・ON・NATURAL の構文差",
        "why": "USING は同名列だけ、ON は任意条件、NATURAL は同名列自動判定で使う。相互に併用できない組合せがある。",
        "pitfall": "USING で表別名付き列を参照したり、NATURAL JOIN に ON を足せると誤認しやすい。",
        "rebuild": [
            "USING と ON は排他、NATURAL も別系統として覚える。",
            "USING 列は SELECT で表別名を付けられない点を確認する。",
            "JOIN 種類と結合条件の書き方を分けて読む。",
        ],
    },
    "having_where": {
        "title": "WHERE と HAVING",
        "why": "WHERE は集計前の行条件、HAVING は集計後のグループ条件である。集計関数を WHERE に直接書くとエラーになる。",
        "pitfall": "COUNT や AVG 条件を WHERE に置いてしまい、GROUP BY 後の条件だと気付けないことが多い。",
        "rebuild": [
            "行条件は WHERE、集計結果条件は HAVING と固定する。",
            "SELECT の論理処理順を FROM→WHERE→GROUP BY→HAVING で覚える。",
            "HAVING が必要かどうかは『集計後に絞るか』で判断する。",
        ],
    },
    "count_avg": {
        "title": "COUNT・AVG と NULL",
        "why": "COUNT(*) は行数、COUNT(col) は NULL を除く列数、AVG(col) は NULL を平均計算から除外する。集計関数ごとに NULL の扱いが異なる。",
        "pitfall": "COUNT(*) と COUNT(col) を同一視し、AVG の分母に NULL 行まで含めて考えやすい。",
        "rebuild": [
            "COUNT(*) は全行、COUNT(col) は NULL 除外を声に出して確認する。",
            "AVG(col)=SUM(col)/COUNT(col) に近い考え方で整理する。",
            "NULL を含む列の集計問題は分母を必ず確認する。",
        ],
    },
    "groupby_error": {
        "title": "GROUP BY の文法",
        "why": "集計関数以外の列を SELECT に出すなら、その列は GROUP BY に含める必要がある。構文順序や句の役割を崩すとエラーになる。",
        "pitfall": "SELECT 列と GROUP BY 列の整合を取らずに、ほぼ正しい SQL を選びやすい。",
        "rebuild": [
            "非集計列は全部 GROUP BY に入るかチェックする。",
            "WHERE、GROUP BY、HAVING、ORDER BY の順序を固定する。",
            "エラー問題では『どの句に何を書いているか』から逆算する。",
        ],
    },
    "keys_null": {
        "title": "主キー・外部キー・一意キーと NULL",
        "why": "主キーは NOT NULL かつ一意、外部キーは NULL 可、一意キーも NULL を許せる。キー制約ごとの NULL 許容差が基本である。",
        "pitfall": "主キーと一意キーを同じ扱いで覚えたり、外部キーが必ず値を持つと考えやすい。",
        "rebuild": [
            "PK は NULL 不可、UK と FK は NULL 可で分ける。",
            "NULL は『未定』であって参照違反ではないことを理解する。",
            "キー問題では制約の目的を日本語で言い換える。",
        ],
    },
    "sql_categories": {
        "title": "SQL 分類の基礎",
        "why": "DDL は定義変更、DML はデータ操作、DCL は権限制御、TCL はトランザクション制御である。各文をどこへ分類するかが基礎力になる。",
        "pitfall": "TRUNCATE や COMMIT の分類が曖昧で、設問を読む前に迷いが生じやすい。",
        "rebuild": [
            "CREATE/ALTER/DROP/TRUNCATE は DDL。",
            "INSERT/UPDATE/DELETE/MERGE は DML。",
            "COMMIT/ROLLBACK/SAVEPOINT は TCL、GRANT/REVOKE は DCL。",
        ],
    },
    "dual_foundation": {
        "title": "DUAL と Oracle 基礎",
        "why": "DUAL は 1 行 1 列の疑似表で、式や関数の確認に使う。所有者や構造を含め、Oracle 固有の基礎知識として出題される。",
        "pitfall": "列名や所有者を誤記しやすく、通常の業務表と同じ感覚で読んでしまいやすい。",
        "rebuild": [
            "DUAL は 1 行 1 列で関数確認用と覚える。",
            "DUMMY 列を持つこと、SYS 所有であることを確認する。",
            "式だけ返す SELECT のときは DUAL を思い出す。",
        ],
    },
    "data_model": {
        "title": "ERD と正規化",
        "why": "N:N 関係は中間表で分解する、正規化は重複や従属を整理する、というモデリングの基本が問われる。SQL 文法ではなく設計の前提知識である。",
        "pitfall": "属性名とキー属性を混同し、関係の多重度を言語化できないまま選ぶと外しやすい。",
        "rebuild": [
            "N:N は中間表、1:N は外部キーで表す。",
            "主キーにする列と単なる属性列を分けて考える。",
            "正規化は重複削減と更新異常防止のためだと理解する。",
        ],
    },
    "null_filter": {
        "title": "NULL 判定と WHERE 条件",
        "why": "NULL 判定は = NULL ではなく IS NULL / IS NOT NULL を使う。複数列の NULL 条件は列ごとに明示する必要がある。",
        "pitfall": "NULL を通常の値のように比較したり、複数列をまとめて IS NOT NULL にできると誤認しやすい。",
        "rebuild": [
            "NULL 比較は必ず IS NULL / IS NOT NULL。",
            "複数列条件は AND で列ごとに書く。",
            "COUNT や算術演算で NULL がどう扱われるかも合わせて確認する。",
        ],
    },
    "operator_precedence": {
        "title": "演算子優先順位",
        "why": "AND は OR より先、算術演算は比較より先など、優先順位を知らないと WHERE 条件の意味が変わる。必要なら括弧で明示する。",
        "pitfall": "自然言語の読み順で解釈してしまい、SQL の実際の評価順とずれやすい。",
        "rebuild": [
            "迷ったら括弧で意味を固定する。",
            "AND が OR より強いことをまず確認する。",
            "IN、BETWEEN、LIKE は比較条件として塊で読む。",
        ],
    },
    "order_row_limit": {
        "title": "ORDER BY・ROWNUM・FETCH",
        "why": "ROWNUM は ORDER BY より前に振られるため、並べ替えてから上位 n 件を取りたいなら副問合せや FETCH FIRST を使う。ORDER BY の列別名や位置番号も正しく使う必要がある。",
        "pitfall": "ROWNUM と ORDER BY の評価順を逆に読んだり、FETCH/ORDER BY の構文順を崩しやすい。",
        "rebuild": [
            "先に並べ替えたいなら副問合せか FETCH FIRST を使う。",
            "ORDER BY の位置番号は SELECT 列順に対応する。",
            "FETCH / OFFSET は ORDER BY の後に続ける。",
        ],
    },
    "substitution_vars": {
        "title": "置換変数と VERIFY",
        "why": "SQL*Plus 系の置換変数では & は毎回入力、&& は再利用される。DEFINE 済みかどうか、VERIFY の役割も含めて読む必要がある。",
        "pitfall": "DEFINE の有無を見ずにプロンプト発生を判断したり、VERIFY を変数定義と混同しやすい。",
        "rebuild": [
            "& は都度入力、&& は定義保持と覚える。",
            "DEFINE 済みならプロンプトが出ない可能性を確認する。",
            "VERIFY は置換前後の表示であり、変数作成ではない。",
        ],
    },
    "like_pattern": {
        "title": "LIKE とワイルドカード",
        "why": "_ は1文字、% は0文字以上を表す。先頭一致・末尾一致・部分一致のパターンを正確に書き分けるのが基本である。",
        "pitfall": "_ と % の意味を逆に覚えたり、前方一致と部分一致を混同しやすい。",
        "rebuild": [
            "'A%' は前方一致、'%A' は後方一致、'%A%' は部分一致。",
            "_ はちょうど1文字なので桁数条件も含む。",
            "大文字小文字区別が必要なら UPPER/LOWER と組み合わせる。",
        ],
    },
    "generic_subquery": {
        "title": "サブクエリ総合",
        "why": "サブクエリは返す行数と比較演算子の組合せで意味が決まる。まず単一行か複数行か、相関か非相関かを切り分ける必要がある。",
        "pitfall": "行数判定を飛ばして記号だけで選ぶと、正しそうな選択肢に流れやすい。",
        "rebuild": [
            "1行か複数行かを先に判定する。",
            "相関か非相関かを次に判定する。",
            "最後に比較演算子が合っているかを確認する。",
        ],
    },
    "generic_functions": {
        "title": "単一行関数総合",
        "why": "単一行関数は文字列、数値、日付、NULL、条件分岐で役割が分かれている。まず何を変換したいかを見て関数の系統を選ぶ。",
        "pitfall": "関数名の見た目で選んでしまい、入力型と戻り型の確認を飛ばしやすい。",
        "rebuild": [
            "文字列か数値か日付かを最初に決める。",
            "戻り値をどの型で欲しいのかを確認する。",
            "式全体の型が合っているかまで見る。",
        ],
    },
    "generic_object": {
        "title": "オブジェクト管理総合",
        "why": "DDL 系問題では、表定義、制約、権限、ビュー、索引など複数のオブジェクト特性を切り分ける必要がある。何のオブジェクトを操作しているかを起点に読む。",
        "pitfall": "SQL の表面だけで判断し、対象オブジェクトの性質を思い出せずに失点しやすい。",
        "rebuild": [
            "まず表・ビュー・索引・権限のどれを操作しているか決める。",
            "そのオブジェクト固有の制約を思い出す。",
            "DDL か DML かも同時に確認する。",
        ],
    },
    "generic_dml": {
        "title": "DML 総合",
        "why": "DML 問題では、対象行の決まり方、更新タイミング、トランザクション制御を順番に読む必要がある。1文の中で何が確定し、何が取り消せるかが核心になる。",
        "pitfall": "構文だけを見て、実行後の状態変化まで追えずに失点しやすい。",
        "rebuild": [
            "対象行、変更内容、確定/取消の可否を3段階で確認する。",
            "DDL と混ざっていないかを見る。",
            "副問合せがある場合は相関性と返却行数を先に確認する。",
        ],
    },
    "generic_filter": {
        "title": "検索条件総合",
        "why": "WHERE 条件問題では、NULL、ワイルドカード、優先順位、行制限など論点が混ざる。条件を日本語へ戻してから式へ落とすのが最も安全である。",
        "pitfall": "SQL 断片の雰囲気で選び、日本語条件との対応を確認しないまま誤答しやすい。",
        "rebuild": [
            "まず条件文を日本語で言い換える。",
            "次に各条件を AND/OR へ分解する。",
            "最後に NULL や行制限の例外規則を確認する。",
        ],
    },
}


def priority_code(rank: int, accuracy: float) -> str:
    if rank < 2:
        return "high"
    if rank < 5:
        return "mid"
    if accuracy < 75:
        return "low"
    return "ok"


def split_answer(ans: str | None) -> list[str]:
    if not ans:
        return []
    compact = re.sub(r"\s+", "", ans).upper()
    if "." in compact:
        return [part for part in compact.split(".") if part]
    if re.fullmatch(r"[A-Z]+", compact) and len(compact) > 1:
        return list(compact)
    if re.fullmatch(r"\d+", compact) and len(compact) > 1:
        return list(compact)
    return [compact]


def normalize_line(line: str) -> str:
    return line.replace("\u3000", " ").rstrip()


def strip_noise(lines: list[str]) -> list[str]:
    return [normalize_line(line) for line in lines if line.strip() and line.strip() != "拡大する"]


def parse_standard_options(lines: list[str]) -> tuple[str, list[dict]]:
    stem_lines: list[str] = []
    options: list[dict] = []
    current = None
    started = False
    pattern = re.compile(r"^\((\d+)\)\s*([A-Z])\.\s*(.*)$")
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            started = True
            if current:
                options.append(current)
            current = {"key": match.group(2), "ordinal": match.group(1), "text": match.group(3)}
            continue
        if started:
            if current:
                current["text"] += ("\n" if current["text"] else "") + line
        else:
            stem_lines.append(line)
    if current:
        options.append(current)
    return "\n".join(stem_lines).strip(), options


def parse_numbered_options(lines: list[str]) -> tuple[str, list[dict]]:
    stem_lines: list[str] = []
    options: list[dict] = []
    current = None
    started = False
    pattern = re.compile(r"^\((\d+)\)\s*(.+)$")
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            started = True
            if current:
                options.append(current)
            current = {"key": match.group(1), "ordinal": match.group(1), "text": match.group(2)}
            continue
        if started:
            if current:
                current["text"] += ("\n" if current["text"] else "") + line
        else:
            stem_lines.append(line)
    if current:
        options.append(current)
    return "\n".join(stem_lines).strip(), options


def parse_letter_block_options(lines: list[str]) -> tuple[str, list[dict]]:
    map_pattern = re.compile(r"^\((\d+)\)\s*([A-Z])\s*$")
    label_pattern = re.compile(r"^([A-Z])\.\s*(.*)$")
    mappings = {}
    mapping_start = None
    for idx in range(len(lines) - 1, -1, -1):
        match = map_pattern.match(lines[idx].strip())
        if not match:
            if mappings:
                break
            continue
        mapping_start = idx
        mappings[match.group(2)] = match.group(1)
    if not mappings:
        return "", []

    content_lines = lines[:mapping_start]
    stem_lines: list[str] = []
    options: list[dict] = []
    current = None
    started = False
    for line in content_lines:
        match = label_pattern.match(line.strip())
        if match and match.group(1) in mappings:
            started = True
            if current:
                options.append(current)
            current = {"key": match.group(1), "ordinal": mappings[match.group(1)], "text": match.group(2)}
            continue
        if started:
            if current:
                current["text"] += ("\n" if current["text"] else "") + line
        else:
            stem_lines.append(line)
    if current:
        options.append(current)
    return "\n".join(stem_lines).strip(), options


def parse_question_block(text: str) -> dict:
    lines = strip_noise(text.splitlines())
    stem, options = parse_standard_options(lines)
    if options:
        return {"stem": stem, "options": options, "raw": text}
    stem, options = parse_letter_block_options(lines)
    if options:
        return {"stem": stem, "options": options, "raw": text}
    stem, options = parse_numbered_options(lines)
    if options:
        return {"stem": stem, "options": options, "raw": text}
    return {"stem": text, "options": [], "raw": text}


def short_text(text: str, limit: int = 88) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1] + "…"


def html_pre(text: str) -> str:
    return f"<pre>{html.escape(text.strip())}</pre>"


def detect_concept(domain: str, text: str) -> str:
    rules = {
        "D6": [
            ("corr_subquery", r"相関|外側の文|内側の文|各部門の平均給与"),
            ("set_operator_general", r"INTERSECT|複合問合せ"),
            ("union_order", r"ORDER BY.*UNION|UNION.*ORDER BY|集合演算.*ORDER BY"),
            ("union_vs_unionall", r"UNION ALL|UNION演算子とUNION ALL"),
            ("minus_set", r"一度も取引が無い|MINUS"),
            ("scalar_subquery", r"スカラサブクエリ|エラーにならないもの"),
            ("self_join_vs_subquery", r"自己結合|同じ商品名"),
            ("subquery_usage", r"サブクエリが必要なケース|平均価格より高い"),
            ("exists_notexists", r"EXISTS|NOT EXISTS|NOT IN"),
            ("multiple_row_subquery", r"複数行の副問合せ|複数行のサブクエリ"),
            ("subquery_comparison", r"ANY| ALL |平均給与|AVG\(salary\)|GROUP BY dept_id"),
        ],
        "D3": [
            ("single_row_function_basics", r"シングル行関数|単一行関数について"),
            ("conversion_format", r"TO_CHAR|TO_NUMBER|TO_DATE|形式|書式"),
            ("date_arithmetic", r"MONTHS_BETWEEN|ADD_MONTHS|LAST_DAY|NEXT_DAY|SYSDATE|DATE型|過去16か月|CURRENT_DATE"),
            ("null_case", r"NVL|NVL2|NULLIF|COALESCE|CASE|DECODE"),
            ("string_extract", r"SUBSTR|INSTR|TRIM|REPLACE|CONCAT|LENGTH|LPAD|RPAD"),
            ("numeric_functions", r"ROUND|TRUNC|FLOOR|CEIL|MOD"),
            ("like_case_functions", r"LIKE|UPPER|LOWER|INITCAP"),
        ],
        "D8": [
            ("default_and_add_column", r"DEFAULT|列を追加|正常に挿入|DEFAULT 0"),
            ("merge_object", r"MERGE"),
            ("view_rules", r"ビュー|VIEW"),
            ("sequence_synonym_index", r"シノニム|SYNONYM|シーケンス|SEQUENCE|索引|INDEX|INVISIBLE"),
            ("privileges_roles", r"GRANT|REVOKE|権限|ロール|WITH GRANT OPTION|WITH ADMIN OPTION|LISA"),
            ("datetime_types", r"TIMESTAMP|TIME ZONE|INTERVAL|CURRENT_TIMESTAMP|SYSTIMESTAMP"),
            ("constraints", r"ENABLE CONSTRAINT|DISABLE CONSTRAINT|PRIMARY KEY|FOREIGN KEY|CHECK|NOT NULL|UNIQUE|制約"),
            ("ddl_rules", r"DDL|DML|TRUNCATE|DELETE|CREATE TABLE|ALTER TABLE"),
        ],
        "D7": [
            ("transaction_control", r"SAVEPOINT|COMMIT|ROLLBACK"),
            ("truncate_delete", r"TRUNCATE|DELETE"),
            ("merge_dml", r"MERGE"),
            ("multitable_insert", r"INSERT ALL|INSERT FIRST|マルチテーブル"),
            ("update_syntax", r"有効なSQL|UPDATE .* SET "),
            ("update_subquery", r"UPDATE .*SELECT|UPDATE invoices|相関サブクエリ"),
        ],
        "D5": [
            ("full_outer", r"FULL OUTER"),
            ("self_join", r"自己結合"),
            ("join_syntax", r"JOIN|USING|NATURAL|ON句"),
        ],
        "D4": [
            ("having_where", r"HAVING|WHERE"),
            ("count_avg", r"COUNT|AVG|SUM|MAX|MIN|NULL"),
            ("groupby_error", r"GROUP BY"),
        ],
        "D1": [
            ("keys_null", r"主キー|外部キー|一意キー|NULL"),
            ("sql_categories", r"DML|DDL|DCL|TCL|トランザクション制御言語|構造化問合せ言語"),
            ("dual_foundation", r"DUAL"),
            ("data_model", r"ERD|正規化|チーム|エンティティ"),
        ],
        "D2": [
            ("substitution_vars", r"置換変数|VERIFY|DEFINE|&"),
            ("order_row_limit", r"ORDER BY|ROWNUM|FETCH|OFFSET"),
            ("null_filter", r"NULL|IS NOT NULL|IS NULL"),
            ("operator_precedence", r"優先順位|AND|OR|BETWEEN| IN "),
            ("like_pattern", r"LIKE|ワイルドカード"),
        ],
    }
    for concept_id, pattern in rules.get(domain, []):
        if re.search(pattern, text, flags=re.I | re.S):
            return concept_id
    fallbacks = {
        "D6": "generic_subquery",
        "D3": "generic_functions",
        "D8": "generic_object",
        "D7": "generic_dml",
        "D5": "join_syntax",
        "D4": "groupby_error",
        "D1": "sql_categories",
        "D2": "generic_filter",
    }
    return fallbacks[domain]


def option_lookup(parsed: dict) -> dict[str, dict]:
    return {option["key"]: option for option in parsed["options"]}


def render_options(parsed: dict, correct_keys: list[str], self_keys: list[str]) -> str:
    if not parsed["options"]:
        return ""

    rendered = []
    for option in parsed["options"]:
        classes = ["option-card"]
        if option["key"] in correct_keys:
            classes.append("correct")
        if option["key"] in self_keys:
            classes.append("selected")
        option_text = html.escape(option["text"]).replace("\n", "<br>")
        rendered.append(
            f"""
            <div class="{' '.join(classes)}">
              <div class="option-key">{html.escape(option['key'])}</div>
              <div class="option-text">{option_text}</div>
            </div>
            """
        )
    return f'<div class="options-grid">{"".join(rendered)}</div>'


def render_option_refs(parsed: dict, keys: list[str]) -> str:
    lookup = option_lookup(parsed)
    labels = []
    for key in keys:
        option = lookup.get(key)
        if option:
            labels.append(f"{key}「{html.escape(short_text(option['text'], 56))}」")
        else:
            labels.append(key)
    return " / ".join(labels)


def build_question_commentary(question: dict, parsed: dict, concept_id: str) -> tuple[str, str, list[str]]:
    meta = CONCEPT_META[concept_id]
    correct_keys = split_answer(question["ans"])
    self_keys = split_answer(question.get("self_ans"))
    wrong_selected = [key for key in self_keys if key not in correct_keys]
    hit_selected = [key for key in self_keys if key in correct_keys]

    correct_ref = render_option_refs(parsed, correct_keys) if correct_keys else html.escape(question["ans"] or "正答未記録")
    explain = (
        f"この問題の論点は「{meta['title']}」です。{meta['why']} "
        f"したがって正答は {correct_ref} になります。"
    )

    if self_keys:
        if wrong_selected and hit_selected:
            mistake = (
                f"自己回答は {render_option_refs(parsed, self_keys)} でした。"
                f"一部は当たっていますが、{render_option_refs(parsed, wrong_selected)} に引っ張られて取りこぼしています。"
                f"{meta['pitfall']}"
            )
        elif wrong_selected:
            mistake = (
                f"自己回答は {render_option_refs(parsed, self_keys)} でした。"
                f"{meta['pitfall']} 正答との差は、条件の向き、句の置き場所、またはオブジェクトの性質を正確に読み切れていない点にあります。"
            )
        else:
            mistake = "自己回答の記録はありますが、誤選択肢情報の不足により差分説明は省略します。"
    else:
        mistake = "自己回答の記録がないため、正答根拠だけを固定し直します。"

    return explain, mistake, meta["rebuild"]


def priority_data() -> list[dict]:
    domains = sorted(
        PAGE_MAP,
        key=lambda dom: (
            DATA["summary"]["combined"][dom]["accuracy"],
            -len(DATA["summary"]["combined"][dom]["wrong"]),
            dom,
        ),
    )
    ranked = []
    for rank, domain in enumerate(domains):
        accuracy = DATA["summary"]["combined"][domain]["accuracy"]
        ex_id, label = PAGE_MAP[domain]
        ranked.append(
            {
                "domain": domain,
                "ex_id": ex_id,
                "label": label,
                "accuracy": accuracy,
                "wrong_count": len(DATA["summary"]["combined"][domain]["wrong"]),
                "priority": priority_code(rank, accuracy),
            }
        )
    return ranked


def assign_phases(ranked: list[dict]) -> list[dict]:
    phase_sizes = [3, 3, len(ranked) - 6]
    cursor = 0
    phase_defs = []
    for phase_no, size in enumerate(phase_sizes, start=1):
        items = ranked[cursor : cursor + size]
        cursor += size
        for item in items:
            item["phase"] = phase_no
        phase_defs.append({"phase": phase_no, "title": PHASE_LABELS[phase_no], "items": items})
    return phase_defs


def build_domain_page(domain_info: dict) -> str:
    domain = domain_info["domain"]
    ex_id = domain_info["ex_id"]
    label = domain_info["label"]
    priority = domain_info["priority"]
    phase_no = domain_info["phase"]
    color = PRIORITY_COLOR[priority]

    wrong_questions = []
    for exam in DATA["exams"]:
        for question in exam["questions"]:
            if question["domain"] == domain and not question["correct"]:
                parsed = parse_question_block(question["text"])
                concept_id = detect_concept(domain, question["text"])
                question_copy = dict(question)
                question_copy["exam_title"] = exam["title"]
                question_copy["parsed"] = parsed
                question_copy["concept_id"] = concept_id
                wrong_questions.append(question_copy)

    grouped: dict[str, list[dict]] = defaultdict(list)
    for question in wrong_questions:
        grouped[question["concept_id"]].append(question)

    sorted_concepts = sorted(
        grouped,
        key=lambda concept_id: (-len(grouped[concept_id]), CONCEPT_META[concept_id]["title"]),
    )

    toc_items = []
    sections = []
    for concept_index, concept_id in enumerate(sorted_concepts, start=1):
        anchor = f"{domain.lower()}-{concept_index}"
        meta = CONCEPT_META[concept_id]
        questions_html = []
        for question in sorted(grouped[concept_id], key=lambda item: (item["exam"], item["q"])):
            correct_keys = split_answer(question["ans"])
            self_keys = split_answer(question.get("self_ans"))
            explain, mistake, rebuild = build_question_commentary(question, question["parsed"], concept_id)
            questions_html.append(
                f"""
                <article class="question-card">
                  <div class="question-meta">{html.escape(question['exam_title'])} / 問{question['q']} / 正答 {html.escape(question['ans'] or '-')} / 自己回答 {html.escape(question.get('self_ans') or '-')}</div>
                  <div class="block-title">問題文</div>
                  {html_pre(question['parsed']['stem'] or question['text'])}
                  <div class="block-title">選択肢</div>
                  {render_options(question['parsed'], correct_keys, self_keys)}
                  <div class="analysis-block">
                    <div class="block-title">なぜそうなるか</div>
                    <p>{explain}</p>
                    <div class="block-title">今回の誤り</div>
                    <p>{mistake}</p>
                    <div class="block-title">叩き直しポイント</div>
                    <ul class="rebuild-list">
                      {''.join(f'<li>{html.escape(item)}</li>' for item in rebuild)}
                    </ul>
                  </div>
                </article>
                """
            )

        toc_items.append(
            f'<a href="#{anchor}" class="{priority}">{html.escape(meta["title"])} <span>{len(grouped[concept_id])}問</span></a>'
        )
        sections.append(
            f"""
            <section class="concept-section" id="{anchor}">
              <h3>{html.escape(meta['title'])}<span>{len(grouped[concept_id])}問</span></h3>
              <p class="concept-copy">{html.escape(meta['why'])}</p>
              {''.join(questions_html)}
            </section>
            """
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{ex_id} {label} - 全誤答徹底解説</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Noto Sans JP', 'Hiragino Sans', sans-serif; background: #eef2f7; color: #1f2937; line-height: 1.7; }}
  a {{ color: inherit; }}
  .page-header {{ background: linear-gradient(135deg,#10243f 0%,#1f3d63 55%,{color} 100%); color: white; padding: 42px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 1.9rem; margin-bottom: 8px; }}
  .page-header .subtitle {{ opacity: 0.92; font-size: 0.95rem; }}
  .container {{ max-width: 1180px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 999px; text-decoration: none; color: #1f2937; box-shadow: 0 4px 14px rgba(15,23,42,.08); font-size: .9rem; margin: 0 8px 16px 0; }}
  .hero-card, .toc, .concept-section {{ background: white; border-radius: 18px; box-shadow: 0 10px 26px rgba(15,23,42,.08); }}
  .hero-card {{ padding: 20px 22px; margin-bottom: 18px; border-top: 6px solid {color}; }}
  .hero-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 14px; }}
  .metric {{ background: #f8fafc; border-radius: 14px; padding: 14px; }}
  .metric .label {{ color: #64748b; font-size: .82rem; }}
  .metric .value {{ font-size: 1.35rem; font-weight: 900; color: #0f172a; margin-top: 4px; }}
  .toc {{ padding: 18px 22px; margin-bottom: 22px; }}
  .toc h2 {{ font-size: 1rem; color: {color}; margin-bottom: 10px; }}
  .toc-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; }}
  .toc a {{ display: flex; justify-content: space-between; gap: 10px; align-items: center; text-decoration: none; padding: 10px 12px; border-radius: 12px; background: #f8fafc; border-left: 4px solid {color}; font-size: .88rem; }}
  .toc a:hover {{ background: #eef2f7; }}
  .concept-section {{ padding: 22px; margin-bottom: 24px; }}
  .concept-section h3 {{ display: flex; justify-content: space-between; gap: 12px; align-items: center; font-size: 1.15rem; margin-bottom: 8px; color: #0f172a; }}
  .concept-section h3 span {{ font-size: .82rem; padding: 5px 10px; border-radius: 999px; background: {color}; color: white; }}
  .concept-copy {{ color: #475569; font-size: .92rem; margin-bottom: 16px; }}
  .question-card {{ border: 1px solid #dbe4ef; border-radius: 16px; padding: 16px; margin-bottom: 14px; background: #fcfdff; }}
  .question-meta {{ font-size: .8rem; color: #64748b; margin-bottom: 10px; font-weight: 700; }}
  .block-title {{ font-size: .85rem; font-weight: 800; color: {color}; margin: 10px 0 6px; }}
  pre {{ white-space: pre-wrap; word-break: break-word; background: #0f172a; color: #e2e8f0; border-radius: 12px; padding: 14px; font-size: .84rem; overflow-x: auto; }}
  .options-grid {{ display: grid; gap: 8px; }}
  .option-card {{ display: grid; grid-template-columns: 32px 1fr; gap: 10px; align-items: start; border: 1px solid #dbe4ef; border-radius: 12px; padding: 10px 12px; background: white; }}
  .option-card.correct {{ border-color: #22c55e; box-shadow: inset 0 0 0 1px #22c55e; }}
  .option-card.selected {{ background: #fff7ed; }}
  .option-card.correct.selected {{ background: #f0fdf4; }}
  .option-key {{ display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 999px; font-size: .82rem; font-weight: 900; background: #e2e8f0; color: #0f172a; }}
  .option-card.correct .option-key {{ background: #dcfce7; color: #166534; }}
  .option-card.selected .option-key {{ background: #ffedd5; color: #9a3412; }}
  .option-card.correct.selected .option-key {{ background: linear-gradient(90deg,#dcfce7,#ffedd5); color: #166534; }}
  .option-text {{ font-size: .88rem; color: #1f2937; line-height: 1.6; padding-top: 3px; word-break: break-word; }}
  .analysis-block p {{ color: #334155; font-size: .9rem; margin-bottom: 8px; }}
  .rebuild-list {{ padding-left: 20px; color: #334155; font-size: .9rem; }}
  .rebuild-list li {{ margin-bottom: 5px; }}
  @media (max-width: 720px) {{
    .page-header h1 {{ font-size: 1.55rem; }}
    .container {{ padding: 18px; }}
    .concept-section h3 {{ flex-direction: column; align-items: flex-start; }}
  }}
</style>
</head>
<body>
<div class="page-header">
  <h1>{ex_id} 全誤答徹底解説</h1>
  <div class="subtitle">{label} / {PHASE_LABELS[phase_no]} / 演習を省き、失点した設問だけを叩き直すページ</div>
</div>
<div class="container">
  <a class="nav-back" href="mock_exam_report.html">結果レポート</a>
  <a class="nav-back" href="mock_exam_reinforce.html">EX ハブ</a>
  <a class="nav-back" href="phase{phase_no}_reinforce.html">このフェーズへ戻る</a>
  <a class="nav-back" href="index.html">教科書トップ</a>

  <div class="hero-card">
    <div style="font-size:.9rem;color:#64748b;font-weight:700">{domain} / {PRIORITY_LABEL[priority]}</div>
    <div style="font-size:1.4rem;font-weight:900;margin-top:4px">{label}</div>
    <p style="margin-top:8px;color:#334155">このページは、実際に間違えた設問をカテゴリ別に並べ、問題文・選択肢・正答理由・誤答理由・叩き直しポイントまで一気に確認するための再構築教材です。</p>
    <div class="hero-grid">
      <div class="metric"><div class="label">フェーズ</div><div class="value">Phase {phase_no}</div></div>
      <div class="metric"><div class="label">進捗率</div><div class="value">{domain_info['accuracy']:.1f}%</div></div>
      <div class="metric"><div class="label">誤答数</div><div class="value">{domain_info['wrong_count']}問</div></div>
      <div class="metric"><div class="label">カテゴリ数</div><div class="value">{len(sorted_concepts)}</div></div>
    </div>
  </div>

  <div class="toc">
    <h2>カテゴリ別目次</h2>
    <div class="toc-grid">
      {''.join(toc_items)}
    </div>
  </div>

  {''.join(sections)}
</div>
</body>
</html>
"""


def phase_card(item: dict) -> str:
    color = PRIORITY_COLOR[item["priority"]]
    return f"""
    <a class="phase-card" href="{item['ex_id']}_reinforce.html" style="border-left:6px solid {color}">
      <div class="phase-tag" style="background:{color}">{item['ex_id']}</div>
      <div class="phase-body">
        <div class="phase-title">{item['label']}</div>
        <div class="phase-meta">元ドメイン {item['domain']} / 優先度 {PRIORITY_LABEL[item['priority']]} / 進捗 {item['accuracy']:.1f}% / 誤答 {item['wrong_count']}問</div>
      </div>
    </a>
    """


def build_phase_page(phase_info: dict) -> str:
    phase_no = phase_info["phase"]
    total_wrong = sum(item["wrong_count"] for item in phase_info["items"])
    avg_accuracy = sum(item["accuracy"] for item in phase_info["items"]) / len(phase_info["items"])
    first_color = PRIORITY_COLOR[phase_info["items"][0]["priority"]]
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{phase_info['title']} - EX 強化学習</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Noto Sans JP', 'Hiragino Sans', sans-serif; background: #eef2f7; color: #1f2937; line-height: 1.7; }}
  .page-header {{ background: linear-gradient(135deg,#10243f 0%,#1f3d63 55%,{first_color} 100%); color: white; padding: 42px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 1.8rem; margin-bottom: 8px; }}
  .container {{ max-width: 980px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 999px; text-decoration: none; color: #1f2937; box-shadow: 0 4px 14px rgba(15,23,42,.08); font-size: .9rem; margin: 0 8px 16px 0; }}
  .intro, .phase-card {{ background: white; border-radius: 18px; box-shadow: 0 10px 26px rgba(15,23,42,.08); }}
  .intro {{ padding: 20px 22px; margin-bottom: 18px; border-top: 6px solid {first_color}; }}
  .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 14px; }}
  .stat {{ background: #f8fafc; border-radius: 14px; padding: 14px; }}
  .stat .label {{ color: #64748b; font-size: .82rem; }}
  .stat .value {{ font-size: 1.32rem; font-weight: 900; color: #0f172a; margin-top: 4px; }}
  .phase-grid {{ display: grid; gap: 14px; }}
  .phase-card {{ display: grid; grid-template-columns: 84px 1fr; gap: 14px; align-items: center; padding: 16px 18px; text-decoration: none; color: inherit; }}
  .phase-tag {{ color: white; font-weight: 900; text-align: center; padding: 10px 0; border-radius: 12px; font-size: 1rem; }}
  .phase-title {{ font-size: 1rem; font-weight: 800; }}
  .phase-meta {{ font-size: .86rem; color: #475569; margin-top: 4px; }}
</style>
</head>
<body>
<div class="page-header">
  <h1>{phase_info['title']}</h1>
  <div>このフェーズで扱う EX を先に潰し、次のフェーズへ進むための導線ページ</div>
</div>
<div class="container">
  <a class="nav-back" href="mock_exam_reinforce.html">EX ハブ</a>
  <a class="nav-back" href="mock_exam_report.html">結果レポート</a>
  <a class="nav-back" href="index.html">教科書トップ</a>
  <div class="intro">
    <div style="font-size:.95rem;color:#64748b;font-weight:700">Phase {phase_no}</div>
    <div style="font-size:1.35rem;font-weight:900;margin-top:4px">{phase_info['title']}</div>
    <p style="margin-top:8px;color:#334155">このフェーズでは、進捗が特に低い領域を先に潰します。各 EX ページは、模擬試験で落とした全設問をカテゴリ別に再解説しています。</p>
    <div class="stats">
      <div class="stat"><div class="label">対象 EX 数</div><div class="value">{len(phase_info['items'])}</div></div>
      <div class="stat"><div class="label">合計誤答数</div><div class="value">{total_wrong}</div></div>
      <div class="stat"><div class="label">平均進捗率</div><div class="value">{avg_accuracy:.1f}%</div></div>
    </div>
  </div>
  <div class="phase-grid">
    {''.join(phase_card(item) for item in phase_info['items'])}
  </div>
</div>
</body>
</html>
"""


def build_hub_page(phases: list[dict]) -> str:
    phase_sections = []
    for phase in phases:
        total_wrong = sum(item["wrong_count"] for item in phase["items"])
        phase_sections.append(
            f"""
            <section class="phase-section">
              <h2>{phase['title']}</h2>
              <p class="phase-copy">対象 {len(phase['items'])} EX / 合計誤答 {total_wrong} 問。リンク先では、該当ドメインの全誤答をカテゴリ別に叩き直します。</p>
              <div class="phase-grid">
                {''.join(phase_card(item) for item in phase['items'])}
              </div>
              <a class="phase-link" href="phase{phase['phase']}_reinforce.html">このフェーズの導線ページを見る</a>
            </section>
            """
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EX 強化学習ハブ - Oracle Silver SQL</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Noto Sans JP', 'Hiragino Sans', sans-serif; background: #eef2f7; color: #1f2937; line-height: 1.7; }}
  .page-header {{ background: linear-gradient(135deg,#10243f 0%,#1f3d63 55%,#c0392b 100%); color: white; padding: 42px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 1.9rem; margin-bottom: 8px; }}
  .container {{ max-width: 1080px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 999px; text-decoration: none; color: #1f2937; box-shadow: 0 4px 14px rgba(15,23,42,.08); font-size: .9rem; margin: 0 8px 16px 0; }}
  .intro, .phase-section, .phase-card {{ background: white; border-radius: 18px; box-shadow: 0 10px 26px rgba(15,23,42,.08); }}
  .intro {{ padding: 22px; margin-bottom: 20px; border-top: 6px solid #c0392b; }}
  .phase-section {{ padding: 22px; margin-bottom: 22px; }}
  .phase-section h2 {{ font-size: 1.2rem; margin-bottom: 8px; color: #10243f; }}
  .phase-copy {{ color: #475569; font-size: .92rem; margin-bottom: 14px; }}
  .phase-grid {{ display: grid; gap: 14px; }}
  .phase-card {{ display: grid; grid-template-columns: 84px 1fr; gap: 14px; align-items: center; padding: 16px 18px; text-decoration: none; color: inherit; }}
  .phase-tag {{ color: white; font-weight: 900; text-align: center; padding: 10px 0; border-radius: 12px; font-size: 1rem; }}
  .phase-title {{ font-size: 1rem; font-weight: 800; }}
  .phase-meta {{ font-size: .86rem; color: #475569; margin-top: 4px; }}
  .phase-link {{ display: inline-block; margin-top: 14px; text-decoration: none; font-weight: 800; color: #c0392b; }}
</style>
</head>
<body>
<div class="page-header">
  <h1>EX 強化学習ハブ</h1>
  <div>演習ではなく、模擬試験で落とした全設問をカテゴリ別に叩き直すための再構築ハブ</div>
</div>
<div class="container">
  <a class="nav-back" href="mock_exam_report.html">結果レポート</a>
  <a class="nav-back" href="index.html">教科書トップ</a>
  <div class="intro">
    <div style="font-size:.95rem;color:#64748b;font-weight:700">方針</div>
    <div style="font-size:1.4rem;font-weight:900;margin-top:4px">フェーズ単位で、全誤答を徹底解説ページへ分割</div>
    <p style="margin-top:8px;color:#334155">Phase 1 から順に進み、各 EX ページで実際に間違えた問題だけを確認します。各設問には問題文・選択肢・正答理由・誤答理由・叩き直しポイントを載せています。</p>
  </div>
  {''.join(phase_sections)}
</div>
</body>
</html>
"""


def main() -> None:
    ranked = priority_data()
    phases = assign_phases(ranked)

    for item in ranked:
        html_text = build_domain_page(item)
        for outdir in ["dist", "textbooks"]:
            out = ROOT / outdir / f"{item['ex_id']}_reinforce.html"
            out.write_text(html_text, encoding="utf-8")
            print(f"wrote {out}")

    hub = build_hub_page(phases)
    for outdir in ["dist", "textbooks"]:
        out = ROOT / outdir / "mock_exam_reinforce.html"
        out.write_text(hub, encoding="utf-8")
        print(f"wrote {out}")

    for phase in phases:
        phase_html = build_phase_page(phase)
        for outdir in ["dist", "textbooks"]:
            out = ROOT / outdir / f"phase{phase['phase']}_reinforce.html"
            out.write_text(phase_html, encoding="utf-8")
            print(f"wrote {out}")


if __name__ == "__main__":
    main()
