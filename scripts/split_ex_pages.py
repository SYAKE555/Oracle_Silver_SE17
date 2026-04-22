#!/usr/bin/env python3
"""Build mock exam review pages from recorded exam results."""
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


def summarize_requirement(parsed: dict) -> str:
    stem = re.sub(r"\s+", " ", (parsed.get("stem") or "").strip())
    return short_text(stem or "設問条件の読み取り", 120)


def concept_teaching_pack(domain: str, concept_id: str) -> dict[str, object]:
    if domain == "D6":
        if concept_id in {"set_operator_general", "union_order", "union_vs_unionall", "minus_set"}:
            return {
                "definition": "集合演算は、複数の SELECT 文の結果を 1 つの結果集合として扱う構文である。各 SELECT で列数を一致させ、対応する列のデータ型も互換にする必要がある。",
                "syntax": (
                    "SELECT col1, col2\n"
                    "FROM   table_a\n"
                    "UNION | UNION ALL | INTERSECT | MINUS\n"
                    "SELECT col1, col2\n"
                    "FROM   table_b\n"
                    "ORDER BY 1;"
                ),
                "principles": [
                    "ORDER BY は複合問合せ全体の末尾に 1 回だけ書く。",
                    "列名は先頭の SELECT 側を基準に解釈される。",
                    "UNION は重複除去、UNION ALL は重複保持、INTERSECT は共通部分、MINUS は左辺から右辺を除いた差集合を返す。",
                ],
                "procedure": [
                    "まず各 SELECT の列数と型の対応を確認する。",
                    "次に設問が求める集合関係が和集合・共通部分・差集合のどれかを判定する。",
                    "最後に ORDER BY の位置と列指定が複合問合せ全体の文法に合っているか確認する。",
                ],
            }
        if concept_id == "exists_notexists":
            return {
                "definition": "EXISTS は副問合せが 1 行でも返れば真となる存在判定であり、返す列値そのものではなく行の存在だけを評価する。",
                "syntax": (
                    "SELECT outer_col\n"
                    "FROM   outer_table o\n"
                    "WHERE  EXISTS (\n"
                    "         SELECT 1\n"
                    "         FROM   inner_table i\n"
                    "         WHERE  i.key = o.key\n"
                    "       );"
                ),
                "principles": [
                    "EXISTS では SELECT 句の値は本質ではなく、通常は SELECT 1 でよい。",
                    "存在否定は NOT EXISTS を使うと、NOT IN の NULL 問題を避けやすい。",
                    "外側の列を内側で参照していれば相関サブクエリである。",
                ],
                "procedure": [
                    "設問が値比較ではなく存在確認を求めているかを読む。",
                    "NULL を含む可能性がある除外条件なら NOT IN より NOT EXISTS を優先する。",
                    "外側表と内側表の結び付き条件が副問合せ内にあるかを確認する。",
                ],
            }
        if concept_id == "scalar_subquery":
            return {
                "definition": "スカラサブクエリは 1 行 1 列だけを返す副問合せであり、式が書ける場所に埋め込める。0 行なら NULL、2 行以上なら ORA-01427 エラーとなる。",
                "syntax": (
                    "SELECT col,\n"
                    "       (SELECT MAX(inner_col)\n"
                    "        FROM   inner_table\n"
                    "        WHERE  key = outer_table.key) AS max_val\n"
                    "FROM   outer_table;"
                ),
                "principles": [
                    "戻り値は常に 1 列でなければならない。",
                    "SELECT 句、WHERE 句、VALUES 句など式の位置で利用できる。",
                    "複数行が返る可能性があるなら IN、ANY、ALL などへ切り替える。",
                ],
                "procedure": [
                    "副問合せが 1 値に収束する集約または主キー条件になっているか確認する。",
                    "0 行時の戻り値が NULL であることを前提に式全体を読む。",
                    "複数行の可能性があるならスカラサブクエリとして不成立と判断する。",
                ],
            }
        if concept_id in {"corr_subquery", "subquery_usage", "subquery_comparison", "multiple_row_subquery", "generic_subquery", "self_join_vs_subquery"}:
            return {
                "definition": "副問合せは、外側の検索条件や出力列で利用する値集合を別の SELECT 文で求める構文である。単一行・複数行・相関の区別が先に必要になる。",
                "syntax": (
                    "SELECT o.col\n"
                    "FROM   outer_table o\n"
                    "WHERE  o.value > (\n"
                    "         SELECT AVG(i.value)\n"
                    "         FROM   inner_table i\n"
                    "         WHERE  i.group_id = o.group_id\n"
                    "       );"
                ),
                "principles": [
                    "外側列を内側が参照していれば相関サブクエリであり、外側行ごとに評価される。",
                    "副問合せの返却行数に応じて =、IN、ANY、ALL、EXISTS を使い分ける。",
                    "比較用の値を先に作るのか、存在だけを見るのかを日本語で判定すると構文を選びやすい。",
                ],
                "procedure": [
                    "副問合せが 1 行か複数行かを最初に判定する。",
                    "次に相関の有無を見て、評価回数と結び付き条件を確認する。",
                    "最後に比較演算子が返却行数と整合しているかを確認する。",
                ],
            }
    if domain == "D3":
        if concept_id in {"like_case_functions", "string_extract"}:
            return {
                "definition": "文字列関数は 1 行ずつ入力を受け取り、変換後の文字列または位置情報を返す。大文字小文字の正規化、部分抽出、位置探索は役割を分けて扱う。",
                "syntax": (
                    "SELECT UPPER(item_name),\n"
                    "       SUBSTR(item_name, 1, 3),\n"
                    "       INSTR(item_name, ' ') \n"
                    "FROM   item\n"
                    "WHERE  UPPER(item_name) LIKE 'S%';"
                ),
                "principles": [
                    "LIKE のワイルドカードは % が 0 文字以上、_ が 1 文字である。",
                    "INSTR は位置、SUBSTR は切り出し、TRIM は前後除去、REPLACE は置換に使う。",
                    "UPPER や LOWER を使うなら比較側の文字列も同じ規則でそろえる。",
                ],
                "procedure": [
                    "まず要求が前方一致・部分一致・文字抽出のどれかを判定する。",
                    "次に正規化関数を列側と比較値側の両方へ必要か確認する。",
                    "位置を使う処理なら INSTR、切り出しなら SUBSTR と機能を分ける。",
                ],
            }
        if concept_id == "conversion_format":
            return {
                "definition": "型変換関数は、内部計算のために元の型へ戻す処理と、表示形式へ整える処理を分けて書く。数値演算の前に TO_NUMBER、日付演算の前に TO_DATE、表示の直前に TO_CHAR を使う。",
                "syntax": (
                    "SELECT TO_CHAR(\n"
                    "         TO_NUMBER(shohin_kakaku, '999,999.99') * 0.30,\n"
                    "         '999,999.00'\n"
                    "       ) AS discount_price\n"
                    "FROM   shohin;"
                ),
                "principles": [
                    "文字列として保存された数値へ直接乗算や加算を行う前に、TO_NUMBER で数値へ変換する。",
                    "表示形式を指定する最終段階では TO_CHAR を使い、TO_NUMBER を外側に置かない。",
                    "書式モデルは元データまたは出力形式と桁数・小数点位置が一致していなければならない。",
                ],
                "procedure": [
                    "まず元データの型が文字列か数値か日付かを確認する。",
                    "次に演算前の型変換と表示直前の書式変換を分離して読む。",
                    "最後に書式モデルが入力側・出力側のどちらへ掛かっているかを確認する。",
                ],
            }
        if concept_id == "date_arithmetic":
            return {
                "definition": "DATE 型の減算結果は日数であり、月単位の計算には MONTHS_BETWEEN や ADD_MONTHS を用いる。表示形式の整形は TO_CHAR、演算前の型変換は TO_DATE や TO_NUMBER が担当する。",
                "syntax": (
                    "SELECT ADD_MONTHS(made_date, 24) AS two_years_later,\n"
                    "       MONTHS_BETWEEN(SYSDATE, made_date) AS elapsed_months,\n"
                    "       TO_CHAR(made_date, 'YYYY-MM-DD') AS made_ymd\n"
                    "FROM   item;"
                ),
                "principles": [
                    "DATE の差は日数、月差は MONTHS_BETWEEN(date1, date2) を使う。",
                    "2 年以上経過のような条件は、日本語を `SYSDATE - 730 >= made_date` などへ書き換えて判定する。",
                    "型変換は演算前、書式変換は表示直前に行う。",
                ],
                "procedure": [
                    "まず設問が日数計算か月数計算かを分ける。",
                    "次に不等号の向きを『いつより古いか』という日本語で確認する。",
                    "文字列との比較や表示整形がある場合は変換順序を確認する。",
                ],
            }
        if concept_id in {"null_case", "single_row_function_basics", "numeric_functions", "generic_functions"}:
            return {
                "definition": "単一行関数は各行に対して 1 つの結果を返し、文字列・数値・日付・NULL・条件分岐の各カテゴリで役割が分かれる。",
                "syntax": (
                    "SELECT ROUND(price, 2),\n"
                    "       NVL(discount, 0),\n"
                    "       CASE WHEN quantity IS NULL THEN 0 ELSE quantity END\n"
                    "FROM   item;"
                ),
                "principles": [
                    "ROUND は四捨五入、TRUNC は切り捨てであり、結果が変わる境界値を意識する。",
                    "NVL と NVL2 は引数の意味が異なり、CASE は一般的な条件分岐に使える。",
                    "単一行関数は SELECT 句だけでなく WHERE 句や ORDER BY でも利用できる。",
                ],
                "procedure": [
                    "何を変換したいのかを文字列・数値・日付・NULL 処理に分ける。",
                    "入力型と戻り値型が式全体で整合しているか確認する。",
                    "境界値が変わる関数では、丸め・切り捨て・NULL 代替の効果を具体的に追う。",
                ],
            }
    if domain == "D8":
        if concept_id in {"default_and_add_column", "constraints", "ddl_rules", "generic_object"}:
            return {
                "definition": "DDL は表定義や制約を変更する文であり、列定義・制約定義・既存データへの影響を同時に読む必要がある。DEFAULT は値省略時に補完されるが、列指定や VALUES 個数との対応は別に守られる。",
                "syntax": (
                    "ALTER TABLE item\n"
                    "ADD status VARCHAR2(10) DEFAULT 'NEW' NOT NULL;\n\n"
                    "INSERT INTO item (item_id, item_name)\n"
                    "VALUES ('1001', 'ITEM1');"
                ),
                "principles": [
                    "既存行がある表へ NOT NULL 列を追加する場合、DEFAULT を伴わないと成立しない。",
                    "INSERT 文で DEFAULT を使うなら、列リストと VALUES の対応を厳密に守る。",
                    "DDL は暗黙 COMMIT を伴うため、DML や TCL と切り分けて理解する。",
                ],
                "procedure": [
                    "対象が表定義変更かデータ操作かを最初に分類する。",
                    "次に既存行の有無、NULL 許容、DEFAULT 補完の関係を確認する。",
                    "最後に列数・列順・制約条件が SQL 文法どおりかを確認する。",
                ],
            }
        if concept_id == "merge_object":
            return {
                "definition": "MERGE は一致時 UPDATE、非一致時 INSERT を 1 文で行う DML である。更新対象は 1 表だけで、USING には比較元の表や副問合せを置く。",
                "syntax": (
                    "MERGE INTO target t\n"
                    "USING source s\n"
                    "ON (t.id = s.id)\n"
                    "WHEN MATCHED THEN\n"
                    "  UPDATE SET t.name = s.name\n"
                    "WHEN NOT MATCHED THEN\n"
                    "  INSERT (id, name) VALUES (s.id, s.name);"
                ),
                "principles": [
                    "MATCHED 側は UPDATE、NOT MATCHED 側は INSERT が基本形である。",
                    "比較条件は ON 句で指定し、更新対象表は MERGE INTO 側に 1 つだけ書く。",
                    "USING には表、ビュー、副問合せを置ける。",
                ],
                "procedure": [
                    "対象表と比較元の役割を切り分ける。",
                    "ON 句で一致条件を読んだ後、MATCHED/NOT MATCHED の処理内容を確認する。",
                    "複数表更新のように見える選択肢は MERGE の文法外として除外する。",
                ],
            }
        if concept_id in {"view_rules", "sequence_synonym_index", "privileges_roles", "datetime_types"}:
            return {
                "definition": "Oracle のオブジェクト管理問題では、ビュー、索引、シーケンス、シノニム、権限、日時型のそれぞれに固有の成立条件がある。",
                "syntax": (
                    "CREATE VIEW v_item AS\n"
                    "SELECT item_id, item_name FROM item;\n\n"
                    "CREATE SEQUENCE seq_item START WITH 1;\n"
                    "GRANT SELECT ON item TO user_name;"
                ),
                "principles": [
                    "ビューは定義を保持するオブジェクトであり、基表そのものを複製するわけではない。",
                    "シーケンスの CURRVAL は同一セッションで NEXTVAL 実行後にのみ参照できる。",
                    "オブジェクト権限とシステム権限では付与オプションが異なる。",
                ],
                "procedure": [
                    "何のオブジェクトを操作している文かを最初に確定する。",
                    "そのオブジェクト固有の使用条件や制約を確認する。",
                    "権限・時刻・索引のような副作用の有無を最後に判定する。",
                ],
            }
    if domain == "D7":
        if concept_id in {"transaction_control", "truncate_delete", "generic_dml"}:
            return {
                "definition": "トランザクションは COMMIT または ROLLBACK で区切られる 1 まとまりの処理である。DML は未確定状態を持てるが、DDL 実行時には暗黙 COMMIT が発生する。",
                "syntax": (
                    "SAVEPOINT before_update;\n"
                    "UPDATE invoices\n"
                    "SET    status = 'PAID'\n"
                    "WHERE  invoice_id = 10;\n"
                    "ROLLBACK TO before_update;\n"
                    "COMMIT;"
                ),
                "principles": [
                    "COMMIT は変更確定とロック解放、SAVEPOINT 消去を行う。",
                    "ROLLBACK TO SAVEPOINT は指定地点以降の変更だけを戻す。",
                    "TRUNCATE や ALTER などの DDL はトランザクション境界を強制する。",
                ],
                "procedure": [
                    "まず文が DML か DDL かを分類する。",
                    "次に変更が未確定で残るか、即時確定されるかを判断する。",
                    "SAVEPOINT がある場合は、どこまで戻せるかを時系列で追う。",
                ],
            }
        if concept_id in {"update_syntax", "update_subquery", "multitable_insert", "merge_dml"}:
            return {
                "definition": "DML 文は、対象行の決定、変更内容の記述、確定/取消の可否を文法どおりに記述する必要がある。UPDATE や INSERT ALL/FIRST、MERGE は句の位置が崩れると不成立になる。",
                "syntax": (
                    "UPDATE invoices i\n"
                    "SET    amount = (\n"
                    "         SELECT SUM(l.amount)\n"
                    "         FROM   invoice_lines l\n"
                    "         WHERE  l.invoice_id = i.invoice_id\n"
                    "       )\n"
                    "WHERE  i.status = 'OPEN';"
                ),
                "principles": [
                    "UPDATE の SET は 1 回だけ書き、複数列代入はカンマで並べる。",
                    "相関サブクエリを使う場合は更新行ごとに副問合せが評価される。",
                    "INSERT ALL は一致したすべて、INSERT FIRST は最初に一致した INTO のみへ挿入する。",
                ],
                "procedure": [
                    "まず対象行を決める WHERE や ON 句を確認する。",
                    "次に SET、VALUES、WHEN 節が Oracle の文法順に並んでいるかを見る。",
                    "副問合せがある場合は単一行保証または条件分岐の位置を確認する。",
                ],
            }
    if domain == "D5":
        return {
            "definition": "結合問題では、どの表の行を残すか、同名列をどう結び付けるか、自己結合か外部結合かを区別して読む必要がある。",
            "syntax": (
                "SELECT e.employee_id, m.employee_id AS manager_id\n"
                "FROM   employees e\n"
                "JOIN   employees m\n"
                "ON     e.manager_id = m.employee_id;"
            ),
            "principles": [
                "INNER JOIN は一致行のみ、LEFT/RIGHT OUTER JOIN は片側全件、FULL OUTER JOIN は両側全件を返す。",
                "自己結合では同じ表を別名で複数回参照するため、表別名が必須である。",
                "USING は同名列だけ、ON は任意条件、NATURAL は同名列自動判定である。",
            ],
            "procedure": [
                "どの表の行を必ず残したいかを先に判断する。",
                "同一表の比較なら自己結合として表別名の有無を確認する。",
                "JOIN 種類と条件記述方式 USING/ON/NATURAL を分けて判定する。",
            ],
        }
    if domain == "D4":
        return {
            "definition": "集計問題では、行条件は WHERE、グループ条件は HAVING、集計関数以外の列は GROUP BY に含める、という基本規則を守る必要がある。",
            "syntax": (
                "SELECT department_id, COUNT(*)\n"
                "FROM   employees\n"
                "WHERE  salary IS NOT NULL\n"
                "GROUP  BY department_id\n"
                "HAVING COUNT(*) >= 2;"
            ),
            "principles": [
                "WHERE は集計前、HAVING は集計後に適用される。",
                "COUNT(*) は全行、COUNT(col) は NULL を除く行数を返す。",
                "SELECT に出す非集計列は GROUP BY にすべて含める。",
            ],
            "procedure": [
                "条件が行単位かグループ単位かを最初に判定する。",
                "次に SELECT 列と GROUP BY 列の整合を確認する。",
                "NULL を含む列では COUNT(*) と COUNT(col) の違いを明示的に追う。",
            ],
        }
    if domain == "D1":
        return {
            "definition": "SQL と RDB の基礎問題では、制約、キー、ER 図、SQL 分類など、文法以前のデータベース原則を正確に押さえる必要がある。",
            "syntax": (
                "CREATE TABLE child (\n"
                "  child_id NUMBER PRIMARY KEY,\n"
                "  parent_id NUMBER REFERENCES parent(parent_id)\n"
                ");"
            ),
            "principles": [
                "主キーは NOT NULL かつ一意、外部キーは NULL を許容できる。",
                "N:N 関係は中間表へ分解し、1:N 関係は外部キーで表す。",
                "DDL、DML、DCL、TCL は役割ごとに分類して理解する。",
            ],
            "procedure": [
                "まず設問が制約・ERD・SQL 分類のどれを問うているかを判定する。",
                "次にキーの性質や関係の多重度を日本語で言い換える。",
                "最後に Oracle 固有の基礎知識である DUAL や SQL 分類へ当てはめる。",
            ],
        }
    return {
        "definition": "検索条件問題では、LIKE、NULL 判定、AND/OR の優先順位、ORDER BY、行制限の評価順をそれぞれ分けて読む必要がある。",
        "syntax": (
            "SELECT item_name, item_price\n"
            "FROM   item\n"
            "WHERE  item_name IS NOT NULL\n"
            "AND    item_price IS NOT NULL\n"
            "AND    item_name LIKE 'T%'\n"
            "ORDER  BY item_price\n"
            "FETCH FIRST 10 ROWS ONLY;"
        ),
        "principles": [
            "LIKE 'T%' は T で始まる文字列、IS NULL / IS NOT NULL は NULL 判定専用である。",
            "AND は OR より先に評価されるため、必要なら括弧で意味を固定する。",
            "ROWNUM は ORDER BY より前、FETCH FIRST は ORDER BY 後に書く。",
        ],
        "procedure": [
            "問題文を行条件へ分解して、各条件を SQL 断片へ置き換える。",
            "NULL 条件は各列ごとに明示し、通常比較と混在させない。",
            "行制限がある場合は ORDER BY との評価順まで確認する。",
        ],
    }


DOMAIN_CLAUSE_ORDER = {
    "D1": (
        '<span class="kw">CREATE TABLE</span> 表名 (\n'
        '  列名 データ型 [<span class="kw">DEFAULT</span> 既定値] [列制約 …],\n'
        '  …,\n'
        '  [<span class="kw">CONSTRAINT</span> 名称 <span class="kw">PRIMARY KEY</span> | <span class="kw">FOREIGN KEY</span> | <span class="kw">UNIQUE</span> | <span class="kw">CHECK</span> (条件)]\n'
        ');\n'
        '<span class="note">-- 主キーは NOT NULL かつ UNIQUE。外部キーは NULL を許容可。</span>\n'
        '<span class="note">-- DDL/DML/DCL/TCL は役割で分類する（CREATE=DDL、INSERT=DML、GRANT=DCL、COMMIT=TCL）。</span>'
    ),
    "D2": (
        '<span class="kw">SELECT</span>    列リスト / 式 / DISTINCT <span class="desc">-- 出力する列</span>\n'
        '<span class="kw">FROM</span>      表 [別名]                <span class="desc">-- 取得元</span>\n'
        '<span class="kw">WHERE</span>     行フィルタ条件            <span class="desc">-- 行を絞り込み（集約前）</span>\n'
        '<span class="kw">ORDER BY</span>  列 / 位置 / 式 [ASC|DESC] <span class="desc">-- 並べ替え</span>\n'
        '<span class="kw">FETCH FIRST</span> n <span class="kw">ROWS ONLY</span>   <span class="desc">-- 行制限（12c 以降）</span>\n'
        '<span class="note">-- NULL 判定は = NULL ではなく IS [NOT] NULL。AND は OR より優先。</span>\n'
        '<span class="note">-- ROWNUM は ORDER BY より先に振られるため、並び替え後の上位取得は副問合せか FETCH。</span>'
    ),
    "D3": (
        '<span class="kw">SELECT</span> 単一行関数(列)        <span class="desc">-- 値の変換・整形（列ごとに結果）</span>\n'
        '<span class="kw">FROM</span>   表\n'
        '<span class="kw">WHERE</span>  単一行関数(列) 比較演算子 値\n'
        '<span class="kw">ORDER BY</span> 単一行関数(列);\n'
        '<span class="note">-- 単一行関数は SELECT / WHERE / ORDER BY のどれにも書ける（GROUP BY 後の HAVING 内でも可）。</span>\n'
        '<span class="note">-- 変換順序: 演算前に TO_NUMBER / TO_DATE、表示直前に TO_CHAR。</span>\n'
        '<span class="note">-- NULL 処理: NVL(式, 代替) / NVL2(式, 非NULL, NULL) / COALESCE / CASE。</span>'
    ),
    "D4": (
        '<span class="kw">SELECT</span>   グループ列, 集計関数(列) <span class="desc">-- 集計結果</span>\n'
        '<span class="kw">FROM</span>     表\n'
        '<span class="kw">WHERE</span>    行条件                 <span class="desc">-- ← 集計“前”。集計関数は書けない</span>\n'
        '<span class="kw">GROUP BY</span> グループ化列          <span class="desc">-- SELECT の非集計列はすべてここに含める</span>\n'
        '<span class="kw">HAVING</span>   集計条件               <span class="desc">-- ← 集計“後”。COUNT(*) 等はここに書く</span>\n'
        '<span class="kw">ORDER BY</span> 集計列 / 位置番号\n'
        '<span class="note">-- COUNT(*) は全行、COUNT(列) は NULL を除く。SUM/AVG/MIN/MAX は NULL を無視。</span>'
    ),
    "D5": (
        '<span class="kw">SELECT</span> e.col, d.col\n'
        '<span class="kw">FROM</span>   employees e\n'
        '<span class="kw">[INNER | LEFT | RIGHT | FULL] OUTER JOIN</span> departments d\n'
        '<span class="kw">ON</span>     e.dept_id = d.dept_id     <span class="desc">-- ON は任意の結合条件</span>\n'
        '   -- または --\n'
        '<span class="kw">JOIN</span>   departments <span class="kw">USING</span> (dept_id) <span class="desc">-- USING は同名列限定、別名不可</span>\n'
        '<span class="kw">NATURAL JOIN</span> departments             <span class="desc">-- 同名列を自動結合（ON/USING 不可）</span>\n'
        '<span class="kw">WHERE</span>  … <span class="kw">ORDER BY</span> …;\n'
        '<span class="note">-- 自己結合は同じ表を別名 2 回で FROM に書く。JOIN 種類は INNER でも外部でも可。</span>\n'
        '<span class="note">-- Oracle 独自 (+) は FULL OUTER JOIN と NATURAL JOIN をサポートしない。</span>'
    ),
    "D6": (
        '<span class="kw">SELECT</span> 列, (<span class="kw">SELECT</span> … <span class="kw">FROM</span> …) <span class="desc">-- スカラサブクエリ（SELECT句：1行1列必須）</span>\n'
        '<span class="kw">FROM</span>   (<span class="kw">SELECT</span> … <span class="kw">FROM</span> …) v <span class="desc">-- インラインビュー（FROM句）</span>\n'
        '<span class="kw">WHERE</span>  列 = (<span class="kw">SELECT</span> … )      <span class="desc">-- 単一行サブクエリ：=, &lt;, &gt;</span>\n'
        '  <span class="kw">OR</span> 列 <span class="kw">IN</span>  (<span class="kw">SELECT</span> …)       <span class="desc">-- 複数行サブクエリ：IN / ANY / ALL</span>\n'
        '  <span class="kw">OR EXISTS</span> (<span class="kw">SELECT</span> 1 <span class="kw">FROM</span> … <span class="kw">WHERE</span> o.k = i.k) <span class="desc">-- 相関・存在判定</span>\n'
        '<span class="kw">UNION</span> [<span class="kw">ALL</span>] | <span class="kw">INTERSECT</span> | <span class="kw">MINUS</span>\n'
        '<span class="kw">SELECT</span> …\n'
        '<span class="kw">ORDER BY</span> 1;                   <span class="desc">-- ORDER BY は最後に 1 回だけ</span>\n'
        '<span class="note">-- 相関：外側列を内側が参照 → 行ごとに再実行。非相関：内側が 1 回だけ実行。</span>\n'
        '<span class="note">-- 集合演算は各 SELECT の列数・型が一致。列名は先頭 SELECT 基準。</span>'
    ),
    "D7": (
        '<span class="kw">INSERT INTO</span> 表 [(列リスト)] <span class="kw">VALUES</span> (値リスト);   <span class="desc">-- 列数と順序を一致</span>\n'
        '<span class="kw">UPDATE</span> 表 <span class="kw">SET</span> 列 = 値 [, …] [<span class="kw">WHERE</span> 条件];        <span class="desc">-- WHERE 省略で全行更新</span>\n'
        '<span class="kw">DELETE FROM</span> 表 [<span class="kw">WHERE</span> 条件];                       <span class="desc">-- DML：ロールバック可能</span>\n'
        '<span class="kw">MERGE INTO</span> 対象 t <span class="kw">USING</span> 比較元 s <span class="kw">ON</span> (条件)\n'
        '  <span class="kw">WHEN MATCHED THEN UPDATE SET</span> … \n'
        '  <span class="kw">WHEN NOT MATCHED THEN INSERT</span> (…) <span class="kw">VALUES</span> (…);\n'
        '-- TCL --\n'
        '<span class="kw">SAVEPOINT</span> 名称; … <span class="kw">ROLLBACK TO</span> 名称; <span class="kw">COMMIT</span>;\n'
        '<span class="note">-- DDL (CREATE/ALTER/DROP/TRUNCATE) は暗黙 COMMIT。TRUNCATE はロールバック不可。</span>\n'
        '<span class="note">-- COMMIT でロック解放・SAVEPOINT 消去。ROLLBACK TO は指定地点以降のみ取消。</span>'
    ),
    "D8": (
        '<span class="kw">CREATE TABLE</span> 表 (\n'
        '  列 型 [<span class="kw">DEFAULT</span> 値] [<span class="kw">NOT NULL</span>] [<span class="kw">CONSTRAINT</span> 名 <span class="kw">PRIMARY KEY</span> | …]\n'
        ');\n'
        '<span class="kw">ALTER TABLE</span> 表 <span class="kw">ADD</span>      (列 型 [DEFAULT …] [NOT NULL]);  <span class="desc">-- 既存行ありでNOT NULLなら DEFAULT 必須</span>\n'
        '<span class="kw">ALTER TABLE</span> 表 <span class="kw">MODIFY</span>   (列 型 | DEFAULT | NOT NULL);\n'
        '<span class="kw">ALTER TABLE</span> 表 <span class="kw">DROP COLUMN</span> 列;\n'
        '<span class="kw">CREATE VIEW</span> v <span class="kw">AS SELECT</span> …;              <span class="desc">-- 定義保持。基表複製ではない</span>\n'
        '<span class="kw">CREATE SEQUENCE</span> s <span class="kw">START WITH</span> 1 <span class="kw">INCREMENT BY</span> 1;  <span class="desc">-- CURRVAL は NEXTVAL 実行後のみ有効</span>\n'
        '<span class="kw">CREATE INDEX</span> idx <span class="kw">ON</span> 表(列);\n'
        '<span class="kw">GRANT</span> 権限 <span class="kw">ON</span> 表 <span class="kw">TO</span> ユーザ [<span class="kw">WITH GRANT OPTION</span>];\n'
        '<span class="note">-- DDL はすべて暗黙 COMMIT を伴う。DEFAULT は値省略時 / VALUES(DEFAULT) で補完。</span>'
    ),
}


def render_concept_guide(domain: str, concept_id: str, color: str) -> str:
    meta = CONCEPT_META[concept_id]
    pack = concept_teaching_pack(domain, concept_id)
    syntax_html = html.escape(str(pack["syntax"]))
    principles = "".join(f"<li>{html.escape(item)}</li>" for item in pack["principles"])
    procedure = "".join(f"<li>{html.escape(item)}</li>" for item in pack["procedure"])
    clause_order = DOMAIN_CLAUSE_ORDER.get(domain, "")
    clause_html = (
        f'<div class="guide-block"><div class="guide-title">句の並び順（Oracle 正式構文）</div>'
        f'<div class="clause-order">{clause_order}</div></div>'
        if clause_order else ""
    )
    return f"""
    <div class="concept-guide" style="border-top-color:{color}">
      <div class="guide-block">
        <div class="guide-title">論点の定義</div>
        <p>{html.escape(str(pack["definition"]))}</p>
      </div>
      {clause_html}
      <div class="guide-block">
        <div class="guide-title">この論点の基本形</div>
        <pre>{syntax_html}</pre>
      </div>
      <div class="guide-grid">
        <div class="guide-block">
          <div class="guide-title">成立条件</div>
          <ul class="guide-list">{principles}</ul>
        </div>
        <div class="guide-block">
          <div class="guide-title">判定手順</div>
          <ol class="guide-list ordered">{procedure}</ol>
        </div>
      </div>
      <div class="guide-note">失点しやすい点: {html.escape(meta["pitfall"])}</div>
    </div>
    """


def option_observations(domain: str, concept_id: str, option_text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", option_text.strip())
    upper = compact.upper()
    observations: list[str] = []

    if "PRIMARY KEY" in upper and "NULL" in compact:
        observations.append("主キーは NOT NULL 制約を含むため、NULL を許容しません。")
    if "FOREIGN KEY" in upper and "NULL" in compact:
        observations.append("外部キーは参照先が未定の状態を表す NULL を保持できます。")
    if ("UNIQUE" in upper or "一意キー" in compact) and "NULL" in compact:
        observations.append("一意キーは主キーと異なり、NULL を保持できます。")
    if "LIKE 'T'" in upper and "LIKE 'T%'" not in upper:
        observations.append("`LIKE 'T'` は T 一文字との一致であり、T で始まる文字列全体は対象にできません。")
    if "LIKE '%T%'" in upper:
        observations.append("`LIKE '%T%'` は前方一致ではなく、途中または末尾に T を含む行まで対象にします。")
    if "LIKE '%T'" in upper and "LIKE '%T%'" not in upper:
        observations.append("`LIKE '%T'` は末尾が T の文字列を対象にします。")
    if "= 'T%'" in upper:
        observations.append("`= 'T%'` はワイルドカード解釈ではなく、文字列 `T%` そのものとの比較です。")
    if "ROUND(" in upper and "ITEM_PRICE" in upper:
        observations.append("ROUND による四捨五入は、価格条件の境界値を変えるため、問題文が単純比較を求める場合は不要または不適切です。")
    if "TRUNC(" in upper and "ITEM_PRICE" in upper:
        observations.append("TRUNC は小数点以下を切り捨てるため、価格列の扱いを整数化したうえで比較する文になります。")
    if "TO_CHAR" in upper and "TO_NUMBER" in upper and "* .30" in upper:
        observations.append("文字列価格を TO_NUMBER で数値へ直してから乗算し、最後に TO_CHAR で書式整形しているなら、型変換の順序として適切です。")
    if "TO_CHAR" in upper and "* .30" in upper and "TO_NUMBER" not in upper:
        observations.append("文字列列へ直接乗算しているなら、演算前の数値変換が不足しています。")
    if upper.startswith("SELECT TO_NUMBER(TO_NUMBER("):
        observations.append("最終出力の書式整形段階では TO_NUMBER ではなく TO_CHAR を使う必要があります。")
    if "AVG(MADE_DATE)" in upper:
        observations.append("AVG 集計は DATE 型へ適用できないため、この式はエラーになります。")
    if "MIN(SYSDATE - MADE_DATE)" in upper or "MAX(MADE_DATE)" in upper:
        observations.append("DATE の減算結果は数値であり、MIN/MAX はその型へ適用できます。")
    if "TO_CHAR(SYSDATE - MADE_DATE)" in upper:
        observations.append("`SYSDATE - MADE_DATE` は日数を表す数値であり、TO_CHAR による文字列化自体は成立します。")
    if "BETWEEN" in upper and "%" in upper:
        observations.append("BETWEEN は大小比較であり、LIKE のワイルドカード判定を代替できません。")
    if "SYSDATE - 2*365" in upper:
        observations.append("`SYSDATE - 2*365 >= made_date` の形なら、2 年以上前に製造された行を抽出できます。")
    if "MADE_DATE >= SYSDATE - 2*365" in upper:
        observations.append("この不等号の向きでは、古い商品ではなく直近 2 年以内の商品を残してしまいます。")
    if "UNION ALL" in upper:
        observations.append("UNION ALL は重複行を残したまま結果集合を連結します。")
    elif "UNION" in upper:
        observations.append("UNION は重複を除去して結果集合を結合します。")
    if "INTERSECT" in upper:
        observations.append("INTERSECT は左右両方に存在する行だけを返します。")
    if "MINUS" in upper:
        observations.append("MINUS は左側にあり右側にはない行だけを返します。")
    if "EXISTS" in upper:
        observations.append("EXISTS は返却列ではなく、副問合せが 1 行でも存在するかどうかだけを判定します。")
    if "NOT IN" in upper:
        observations.append("NOT IN は副問合せ結果に NULL が含まれると判定不能になりやすいため、NOT EXISTS より危険です。")
    if "LEFT OUTER JOIN" in upper:
        observations.append("LEFT OUTER JOIN は左側表の全行を保持し、右側に一致しない行は NULL で埋めます。")
    if "RIGHT OUTER JOIN" in upper:
        observations.append("RIGHT OUTER JOIN は右側表の全行を保持します。表の並びと保持側を取り違えると要件から外れます。")
    if "FULL OUTER JOIN" in upper:
        observations.append("FULL OUTER JOIN は左右両方の全行を返し、デカルト積ではありません。")
    if "INNER JOIN" in upper:
        observations.append("INNER JOIN は結合条件に一致した行だけを返します。")
    if "USING" in upper:
        observations.append("USING 句は同名列に対してだけ使え、列参照では表別名を付けられません。")
    if "NATURAL JOIN" in upper:
        observations.append("NATURAL JOIN は同名列を自動で結合に使うため、ON 句や USING 句とは併用しません。")
    if "HAVING" in upper:
        observations.append("HAVING は集計後のグループに対して条件を適用します。")
    if "WHERE" in upper and re.search(r"WHERE .*COUNT\(", upper):
        observations.append("集計関数を WHERE に直接書くことはできず、集計後条件なら HAVING が必要です。")
    if "COUNT(*)" in upper:
        observations.append("COUNT(*) は NULL の有無に関係なく行数全体を数えます。")
    if "COUNT(" in upper and "COUNT(*)" not in upper:
        observations.append("COUNT(列) はその列が NULL の行を数えません。")
    if "IS NOT NULL" in upper or "IS NULL" in upper:
        observations.append("NULL 判定は `= NULL` ではなく `IS NULL` / `IS NOT NULL` を使います。")
    if "ROWNUM" in upper:
        observations.append("ROWNUM は ORDER BY より前に振られるため、並べ替え後の上位抽出には副問合せや FETCH FIRST が必要です。")
    if "FETCH FIRST" in upper or "OFFSET" in upper:
        observations.append("FETCH / OFFSET は ORDER BY の後に続く行制限構文です。")
    if "DEFAULT" in upper:
        observations.append("DEFAULT は列値を省略したとき、または VALUES 句で DEFAULT を明示したときに補完されます。")
    if "INSERT INTO" in upper and "VALUES" in upper:
        observations.append("INSERT 文では、列リストと VALUES 内の値の個数・順序が一致していなければなりません。")
    if "MERGE INTO" in upper:
        observations.append("MERGE は `MERGE INTO 対象表 USING 比較元 ON 条件` の順に書き、一致時 UPDATE、非一致時 INSERT を分岐します。")
    if "SAVEPOINT" in upper:
        observations.append("SAVEPOINT はロールバック復帰点であり、COMMIT すると消去されます。")
    if "COMMIT" in upper:
        observations.append("COMMIT は変更を確定し、ロックを解放してトランザクションを終了させます。")
    if "ROLLBACK" in upper:
        observations.append("ROLLBACK は未確定変更を取り消します。SAVEPOINT 指定ならその地点以降だけを戻します。")
    if "DDL" in upper or any(word in upper for word in ["ALTER ", "CREATE ", "DROP ", "TRUNCATE "]):
        observations.append("DDL は定義変更であり、Oracle では暗黙 COMMIT を伴います。")
    if "CURRENT_TIMESTAMP" in upper or "SYSTIMESTAMP" in upper:
        observations.append("CURRENT_TIMESTAMP はセッションタイムゾーン、SYSTIMESTAMP はサーバ側タイムスタンプを返します。")
    if "DUAL" in upper:
        observations.append("DUAL は Oracle 固有の 1 行 1 列の疑似表で、式や関数結果の確認に使います。")
    if not observations and domain == "D6" and ("SELECT" in upper or "WHERE" in upper):
        observations.append("副問合せでは返却行数、相関の有無、比較演算子の整合が成立条件になります。")
    if not observations and domain == "D3":
        observations.append("単一行関数では、入力型・戻り値型・境界値への影響を同時に確認する必要があります。")
    if not observations and domain == "D8":
        observations.append("オブジェクト管理問題では、対象オブジェクトの性質と文法要件が一致しているかを確認する必要があります。")
    if not observations and domain == "D7":
        observations.append("DML/TCL 問題では、対象行、変更内容、確定/取消の可否を順番に確認する必要があります。")
    if not observations and domain == "D5":
        observations.append("結合問題では、保持側の表と結合条件の書き方が要件と一致しているかが判定基準になります。")
    if not observations and domain == "D4":
        observations.append("集計問題では、WHERE・GROUP BY・HAVING の役割分担を崩していないかが判定基準です。")
    if not observations and domain == "D1":
        observations.append("基礎問題では、キー制約や SQL 分類の正式定義に合致しているかを確認します。")
    if not observations and domain == "D2":
        observations.append("検索条件問題では、NULL 判定、ワイルドカード、優先順位、行制限の評価順が成立条件です。")
    return observations


def build_option_review(question: dict, parsed: dict, concept_id: str) -> str:
    if not parsed["options"]:
        return ""

    correct_keys = split_answer(question["ans"])
    self_keys = split_answer(question.get("self_ans"))
    requirement = summarize_requirement(parsed)
    items = []
    for option in parsed["options"]:
        is_correct = option["key"] in correct_keys
        selected = option["key"] in self_keys
        classes = ["option-review", "correct" if is_correct else "wrong"]
        labels = ["正答肢" if is_correct else "非正答肢"]
        if selected:
            labels.append("自己回答")
        badge_html = "".join(f"<span>{html.escape(label)}</span>" for label in labels)
        option_text_html = html.escape(option["text"]).replace("\n", "<br>")
        observations = option_observations(question["domain"], concept_id, option["text"])
        if observations:
            reason = " ".join(observations)
        elif is_correct:
            reason = f"この選択肢は「{requirement}」という設問条件に対して、{CONCEPT_META[concept_id]['title']} の成立条件を満たしています。"
        else:
            reason = f"この選択肢は「{requirement}」という設問条件に対して、{CONCEPT_META[concept_id]['title']} の成立条件または文法要件を満たしていません。"
        items.append(
            f"""
            <div class="{' '.join(classes)}">
              <div class="option-review-head">
                <div class="option-review-key">{html.escape(option['key'])}</div>
                <div class="option-review-badges">{badge_html}</div>
              </div>
              <div class="option-review-text">{option_text_html}</div>
              <div class="option-review-reason">{'正しい。' if is_correct else '誤り。'} {html.escape(reason)}</div>
            </div>
            """
        )
    return f'<div class="option-review-grid">{"".join(items)}</div>'


def build_question_commentary(question: dict, parsed: dict, concept_id: str) -> tuple[str, str, list[str]]:
    meta = CONCEPT_META[concept_id]
    pack = concept_teaching_pack(question["domain"], concept_id)
    correct_keys = split_answer(question["ans"])
    self_keys = split_answer(question.get("self_ans"))
    wrong_selected = [key for key in self_keys if key not in correct_keys]
    hit_selected = [key for key in self_keys if key in correct_keys]
    requirement = summarize_requirement(parsed)

    correct_ref = render_option_refs(parsed, correct_keys) if correct_keys else html.escape(question["ans"] or "正答未記録")
    explain = (
        f"この設問で確定させる論点は「{meta['title']}」です。"
        f"問題文は「{requirement}」を満たす記述または SQL を求めています。"
        f"{meta['why']} そのため、成立条件を満たす正答は {correct_ref} です。"
    )

    if self_keys:
        if wrong_selected and hit_selected:
            mistake = (
                f"自己回答は {render_option_refs(parsed, self_keys)} でした。"
                f"一部は論点を捉えていますが、{render_option_refs(parsed, wrong_selected)} を混在させたことで正答条件を外しています。"
                f"失点要因は {meta['pitfall']}"
            )
        elif wrong_selected:
            mistake = (
                f"自己回答は {render_option_refs(parsed, self_keys)} でした。"
                f"失点要因は {meta['pitfall']} "
                f"正答との差は、条件の向き、句の位置、返却行数、またはオブジェクトの性質を正式定義のレベルで確認し切れていない点にあります。"
            )
        else:
            mistake = "自己回答の記録はありますが、誤選択肢の差分が残っていないため、ここでは成立条件の固定に集中します。"
    else:
        mistake = "自己回答の記録がないため、ここでは正答が成立する条件と、誤りになりやすい境界を固定します。"

    return explain, mistake, list(pack["procedure"])


def build_correct_question_commentary(question: dict, parsed: dict, concept_id: str) -> tuple[str, str, list[str]]:
    meta = CONCEPT_META[concept_id]
    pack = concept_teaching_pack(question["domain"], concept_id)
    correct_keys = split_answer(question["ans"])
    self_keys = split_answer(question.get("self_ans"))
    requirement = summarize_requirement(parsed)
    correct_ref = render_option_refs(parsed, correct_keys) if correct_keys else html.escape(question["ans"] or "正答未記録")

    explain = (
        f"この設問の論点は「{meta['title']}」です。"
        f"問題文は「{requirement}」という条件を満たす説明または SQL を求めています。"
        f"{meta['why']} この設問では正答 {correct_ref} を選べており、成立条件を正しく読めています。"
    )

    if self_keys:
        maintain = (
            f"自己回答は {render_option_refs(parsed, self_keys)} で、正答と一致しています。"
            f"得点できた理由は、条件の向き、句の位置、返却行数、オブジェクトの性質を正式定義どおりに読めていた点にあります。"
        )
    else:
        maintain = "自己回答の記録はありませんが、正答が成立する条件を言語化して、次回も同じ論点を再現できる状態にします。"

    return explain, maintain, list(pack["procedure"])


def review_filename(ex_id: str, review_mode: str) -> str:
    if review_mode == "wrong":
        return f"{ex_id}_reinforce.html"
    return f"{ex_id}_correct.html"


def review_hub_filename(review_mode: str) -> str:
    return "mock_exam_reinforce.html" if review_mode == "wrong" else "mock_exam_correct.html"


def collect_domain_questions(domain: str, review_mode: str) -> list[dict]:
    want_correct = review_mode == "correct"
    items = []
    for exam in DATA["exams"]:
        for question in exam["questions"]:
            if question["domain"] != domain or question["correct"] != want_correct:
                continue
            parsed = parse_question_block(question["text"])
            concept_id = detect_concept(domain, question["text"])
            question_copy = dict(question)
            question_copy["exam_title"] = exam["title"]
            question_copy["parsed"] = parsed
            question_copy["concept_id"] = concept_id
            items.append(question_copy)
    return items


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


def build_domain_page(domain_info: dict, review_mode: str = "wrong") -> str:
    domain = domain_info["domain"]
    ex_id = domain_info["ex_id"]
    label = domain_info["label"]
    priority = domain_info.get("priority", "ok")
    phase_no = domain_info.get("phase")
    color = PRIORITY_COLOR.get(priority, "#2ecc71")

    review_questions = collect_domain_questions(domain, review_mode)

    grouped: dict[str, list[dict]] = defaultdict(list)
    for question in review_questions:
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
        concept_guide = render_concept_guide(domain, concept_id, color)
        questions_html = []
        for question in sorted(grouped[concept_id], key=lambda item: (item["exam"], item["q"])):
            if review_mode == "wrong":
                explain, secondary_copy, study_steps = build_question_commentary(question, question["parsed"], concept_id)
                secondary_title = "今回の失点要因"
            else:
                explain, secondary_copy, study_steps = build_correct_question_commentary(question, question["parsed"], concept_id)
                secondary_title = "得点できた理由"
            option_review = build_option_review(question, question["parsed"], concept_id)
            questions_html.append(
                f"""
                <article class="question-card">
                  <div class="question-meta">{html.escape(question['exam_title'])} / 問{question['q']} / 正答 {html.escape(question['ans'] or '-')} / 自己回答 {html.escape(question.get('self_ans') or '-')}</div>
                  <div class="block-title">問題文</div>
                  {html_pre(question['text'])}
                  <div class="analysis-block">
                    <div class="block-title">設問の読み解き</div>
                    <p>{explain}</p>
                    <div class="block-title">{secondary_title}</div>
                    <p>{secondary_copy}</p>
                    <div class="block-title">選択肢ごとの判定</div>
                    {option_review}
                    <div class="block-title">解く順序</div>
                    <ul class="study-step-list">
                      {''.join(f'<li>{html.escape(item)}</li>' for item in study_steps)}
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
              {concept_guide}
              {''.join(questions_html)}
            </section>
            """
        )

    page_title = "全誤答徹底解説" if review_mode == "wrong" else "正答済み総点検"
    subtitle = (
        f"{label} / {PHASE_LABELS[phase_no]} / 演習を省き、失点した設問だけを叩き直すページ"
        if review_mode == "wrong"
        else f"{label} / 正答した設問をカテゴリ別に再確認し、得点源を維持するページ"
    )
    summary_copy = (
        "このページは、実際に間違えた設問をカテゴリ別に並べ、記録された問題全文を正本として、正答理由・誤答理由・叩き直しポイントまで一気に確認するための再構築教材です。"
        if review_mode == "wrong"
        else "このページは、正答できた設問をカテゴリ別に並べ、記録された問題全文を正本として、なぜ取れたのかと維持ポイントを再確認するための定着教材です。"
    )
    hub_href = review_hub_filename(review_mode)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{ex_id} {label} - {page_title}</title>
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
  .concept-guide {{ border-top: 5px solid {color}; background: #f8fafc; border-radius: 16px; padding: 16px; margin-bottom: 18px; }}
  .guide-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; }}
  .guide-block {{ margin-bottom: 12px; }}
  .guide-title {{ font-size: .82rem; font-weight: 900; color: {color}; margin-bottom: 6px; }}
  .guide-block p {{ color: #334155; font-size: .9rem; }}
  .guide-list {{ padding-left: 20px; color: #334155; font-size: .9rem; }}
  .guide-list li {{ margin-bottom: 5px; }}
  .guide-note {{ background: #fff7ed; border-left: 4px solid {color}; border-radius: 10px; padding: 10px 12px; color: #7c2d12; font-size: .88rem; margin-top: 6px; }}
  .question-card {{ border: 1px solid #dbe4ef; border-radius: 16px; padding: 16px; margin-bottom: 14px; background: #fcfdff; }}
  .question-meta {{ font-size: .8rem; color: #64748b; margin-bottom: 10px; font-weight: 700; }}
  .block-title {{ font-size: .85rem; font-weight: 800; color: {color}; margin: 10px 0 6px; }}
  pre {{ white-space: pre-wrap; word-break: break-word; background: #0f172a; color: #e2e8f0; border-radius: 12px; padding: 14px; font-size: .84rem; overflow-x: auto; }}
  .analysis-block p {{ color: #334155; font-size: .9rem; margin-bottom: 8px; }}
  .option-review-grid {{ display: flex; flex-direction: column; gap: 12px; margin-bottom: 8px; }}
  .option-review {{ border-radius: 14px; padding: 16px 18px; border: 1px solid #dbe4ef; background: white; }}
  .option-review.correct {{ border-left: 6px solid #16a34a; background: #f6fdf8; }}
  .option-review.wrong {{ border-left: 6px solid #c0392b; background: #fffafa; }}
  .option-review-head {{ display: flex; justify-content: flex-start; gap: 12px; align-items: center; margin-bottom: 10px; }}
  .option-review-key {{ font-size: 1.05rem; font-weight: 900; color: #0f172a; min-width: 1.8em; }}
  .option-review-badges span {{ display: inline-block; background: #eef2f7; color: #334155; font-size: .74rem; font-weight: 800; border-radius: 999px; padding: 3px 10px; margin-left: 4px; }}
  .option-review-text {{ color: #1f2937; font-size: .98rem; line-height: 1.65; margin-bottom: 10px; font-weight: 600; }}
  .option-review-reason {{ color: #334155; font-size: .92rem; line-height: 1.75; }}
  .clause-order {{ background: #0f172a; color: #e2e8f0; border-radius: 12px; padding: 14px 16px; font-family: 'SFMono-Regular', Menlo, Consolas, monospace; font-size: .86rem; line-height: 1.8; white-space: pre; overflow-x: auto; }}
  .clause-order .kw {{ color: #fbbf24; font-weight: 800; }}
  .clause-order .desc {{ color: #93c5fd; }}
  .clause-order .note {{ color: #86efac; font-style: italic; }}
  .study-step-list {{ padding-left: 20px; color: #334155; font-size: .9rem; }}
  .study-step-list li {{ margin-bottom: 5px; }}
  @media (max-width: 720px) {{
    .page-header h1 {{ font-size: 1.55rem; }}
    .container {{ padding: 18px; }}
    .concept-section h3 {{ flex-direction: column; align-items: flex-start; }}
    .option-review-head {{ flex-direction: column; align-items: flex-start; }}
  }}
</style>
</head>
<body>
<div class="page-header">
  <h1>{ex_id} {page_title}</h1>
  <div class="subtitle">{subtitle}</div>
</div>
<div class="container">
  <a class="nav-back" href="mock_exam_dashboard.html">模擬試験ダッシュボード</a>
  <a class="nav-back" href="mock_exam_report.html">結果レポート</a>
  <a class="nav-back" href="{hub_href}">模擬試験レビュー</a>
  {'<a class="nav-back" href="phase' + str(phase_no) + '_reinforce.html">このフェーズへ戻る</a>' if review_mode == "wrong" and phase_no else ''}
  <a class="nav-back" href="index.html">教科書トップ</a>

  <div class="hero-card">
    <div style="font-size:.9rem;color:#64748b;font-weight:700">{domain} / {PRIORITY_LABEL[priority]}</div>
    <div style="font-size:1.4rem;font-weight:900;margin-top:4px">{label}</div>
    <p style="margin-top:8px;color:#334155">{summary_copy}</p>
    <div class="hero-grid">
      <div class="metric"><div class="label">レビュー種別</div><div class="value">{'誤答' if review_mode == 'wrong' else '正答'}</div></div>
      <div class="metric"><div class="label">進捗率</div><div class="value">{domain_info['accuracy']:.1f}%</div></div>
      <div class="metric"><div class="label">{'誤答数' if review_mode == 'wrong' else '正答数'}</div><div class="value">{len(review_questions)}問</div></div>
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


def build_correct_hub_page(items: list[dict]) -> str:
    cards = []
    for item in sorted(items, key=lambda row: (-row["accuracy"], row["domain"])):
        correct_count = DATA["summary"]["combined"][item["domain"]]["correct"]
        color = PRIORITY_COLOR["ok"] if item["accuracy"] >= 75 else ("#f1c40f" if item["accuracy"] >= 50 else "#e67e22")
        cards.append(
            f"""
            <a class="phase-card" href="{review_filename(item['ex_id'], 'correct')}" style="border-left:6px solid {color}">
              <div class="phase-tag" style="background:{color}">{item['ex_id']}</div>
              <div class="phase-body">
                <div class="phase-title">{item['label']}</div>
                <div class="phase-meta">元ドメイン {item['domain']} / 進捗 {item['accuracy']:.1f}% / 正答 {correct_count}問 / 取れている論点の維持確認</div>
              </div>
            </a>
            """
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>正答済み総点検ハブ - Oracle Silver SQL</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Noto Sans JP', 'Hiragino Sans', sans-serif; background: #eef2f7; color: #1f2937; line-height: 1.7; }}
  .page-header {{ background: linear-gradient(135deg,#0f766e 0%,#115e59 55%,#16a34a 100%); color: white; padding: 42px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 1.9rem; margin-bottom: 8px; }}
  .container {{ max-width: 1080px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 999px; text-decoration: none; color: #1f2937; box-shadow: 0 4px 14px rgba(15,23,42,.08); font-size: .9rem; margin: 0 8px 16px 0; }}
  .intro, .phase-card {{ background: white; border-radius: 18px; box-shadow: 0 10px 26px rgba(15,23,42,.08); }}
  .intro {{ padding: 20px 22px; margin-bottom: 18px; border-top: 6px solid #16a34a; }}
  .phase-grid {{ display: grid; gap: 14px; }}
  .phase-card {{ display: grid; grid-template-columns: 84px 1fr; gap: 14px; align-items: center; padding: 16px 18px; text-decoration: none; color: inherit; }}
  .phase-tag {{ color: white; font-weight: 900; text-align: center; padding: 10px 0; border-radius: 12px; font-size: 1rem; }}
  .phase-title {{ font-size: 1rem; font-weight: 800; }}
  .phase-meta {{ font-size: .86rem; color: #475569; margin-top: 4px; }}
</style>
</head>
<body>
<div class="page-header">
  <h1>正答済み総点検ハブ</h1>
  <div>本番で取れた問題をカテゴリ別に再確認し、得点源を維持するための導線ページ</div>
</div>
<div class="container">
  <a class="nav-back" href="mock_exam_dashboard.html">模擬試験ダッシュボード</a>
  <a class="nav-back" href="mock_exam_report.html">結果レポート</a>
  <a class="nav-back" href="index.html">教科書トップ</a>
  <div class="intro">
    <div style="font-size:.95rem;color:#64748b;font-weight:700">方針</div>
    <div style="font-size:1.35rem;font-weight:900;margin-top:4px">正答した論点も、落とさない形で再固定する</div>
    <p style="margin-top:8px;color:#334155">弱点補強だけだと、たまたま取れた領域が次回で崩れます。ここでは正答済みの設問をカテゴリ別に並べ、なぜ取れたのかと維持ポイントを確認します。</p>
  </div>
  <div class="phase-grid">
    {''.join(cards)}
  </div>
</div>
</body>
</html>
"""


def build_center_page(ranked: list[dict]) -> str:
    weakest = sorted(ranked, key=lambda item: (item["accuracy"], -item["wrong_count"], item["domain"]))[:3]
    strongest = sorted(ranked, key=lambda item: (-item["accuracy"], item["domain"]))[:3]
    exam_cards = []
    for exam in DATA["exams"]:
        exam_cards.append(
            f"""
            <div class="stat-card">
              <div class="stat-label">{html.escape(exam['title'])}</div>
              <div class="stat-value">{exam['final_score']}%</div>
              <div class="stat-copy">設問正答率 {exam['accuracy']:.0f}%</div>
            </div>
            """
        )

    weak_links = "".join(
        f'<a class="mini-link weak" href="{review_filename(item["ex_id"], "wrong")}">{item["ex_id"]} {item["label"]} <span>{item["accuracy"]:.0f}%</span></a>'
        for item in weakest
    )
    strong_links = "".join(
        f'<a class="mini-link strong" href="{review_filename(item["ex_id"], "correct")}">{item["ex_id"]} {item["label"]} <span>{item["accuracy"]:.0f}%</span></a>'
        for item in strongest
    )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>模擬試験ダッシュボード</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Noto Sans JP', 'Hiragino Sans', sans-serif; background: #eef2f7; color: #1f2937; line-height: 1.7; }}
  a {{ color: inherit; }}
  .page-header {{ background: linear-gradient(135deg,#10243f 0%,#1f3d63 55%,#c0392b 100%); color: white; padding: 42px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 1.95rem; margin-bottom: 8px; }}
  .container {{ max-width: 1120px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 999px; text-decoration: none; color: #1f2937; box-shadow: 0 4px 14px rgba(15,23,42,.08); font-size: .9rem; margin: 0 8px 16px 0; }}
  .hero, .panel, .entry-card {{ background: white; border-radius: 18px; box-shadow: 0 10px 26px rgba(15,23,42,.08); }}
  .hero {{ padding: 22px 24px; margin-bottom: 18px; border-top: 6px solid #c0392b; }}
  .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 16px; }}
  .stat-card {{ background: #f8fafc; border-radius: 14px; padding: 14px; }}
  .stat-label {{ color: #64748b; font-size: .82rem; }}
  .stat-value {{ font-size: 1.35rem; font-weight: 900; color: #0f172a; margin-top: 4px; }}
  .stat-copy {{ font-size: .84rem; color: #475569; margin-top: 4px; }}
  .entry-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 18px; }}
  .entry-card {{ padding: 18px 20px; text-decoration: none; border-top: 6px solid #1f3d63; }}
  .entry-card.review {{ border-top-color: #2c3e50; }}
  .entry-card.wrong {{ border-top-color: #c0392b; }}
  .entry-card.correct {{ border-top-color: #16a34a; }}
  .entry-title {{ font-size: 1rem; font-weight: 900; color: #0f172a; }}
  .entry-copy {{ margin-top: 8px; color: #475569; font-size: .9rem; }}
  .panel {{ padding: 20px 22px; margin-bottom: 18px; }}
  .panel h2 {{ font-size: 1rem; color: #10243f; margin-bottom: 12px; }}
  .link-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px; }}
  .mini-link {{ display: flex; justify-content: space-between; gap: 12px; align-items: center; text-decoration: none; padding: 12px 14px; border-radius: 12px; background: #f8fafc; }}
  .mini-link.weak {{ border-left: 4px solid #c0392b; }}
  .mini-link.strong {{ border-left: 4px solid #16a34a; }}
  .mini-link span {{ font-weight: 800; color: #334155; }}
</style>
</head>
<body>
<div class="page-header">
  <h1>模擬試験ダッシュボード</h1>
  <div>結果分析は次の画面へ寄せ、ここでは模擬試験関連の入口だけを compact にまとめる</div>
</div>
<div class="container">
  <a class="nav-back" href="index.html">教科書トップ</a>
  <div class="hero">
    <div style="font-size:.95rem;color:#64748b;font-weight:700">Overview</div>
    <div style="font-size:1.45rem;font-weight:900;margin-top:4px">結果分析、誤答補強、正答維持をここで統合</div>
    <p style="margin-top:8px;color:#334155">模擬試験の詳細分析はこの先のレポートにまとめ、トップ導線は 1 箇所に集約しています。まずは誤答か正答かで入り口を分け、必要なら結果分析へ進みます。</p>
    <div class="stats">
      {''.join(exam_cards)}
    </div>
  </div>

  <div class="entry-grid">
    <a class="entry-card review" href="mock_exam_report.html">
      <div class="entry-title">結果分析へ進む</div>
      <div class="entry-copy">総合スコア、失点比率、項目別進捗、試験別詳細を確認するページ。</div>
    </a>
    <a class="entry-card wrong" href="mock_exam_reinforce.html">
      <div class="entry-title">誤答の徹底解説</div>
      <div class="entry-copy">落とした問題だけをカテゴリ別にまとめた補強導線。弱点回収を優先する。</div>
    </a>
    <a class="entry-card correct" href="mock_exam_correct.html">
      <div class="entry-title">正答の総点検</div>
      <div class="entry-copy">正答できた問題もカテゴリ別に再確認し、得点源を維持する導線。</div>
    </a>
  </div>

  <div class="panel">
    <h2>弱点から入る</h2>
    <div class="link-grid">{weak_links}</div>
  </div>

  <div class="panel">
    <h2>得点源を維持する</h2>
    <div class="link-grid">{strong_links}</div>
  </div>
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
  <a class="nav-back" href="mock_exam_dashboard.html">模擬試験ダッシュボード</a>
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
  <a class="nav-back" href="mock_exam_dashboard.html">模擬試験ダッシュボード</a>
  <a class="nav-back" href="mock_exam_report.html">結果レポート</a>
  <a class="nav-back" href="index.html">教科書トップ</a>
  <div class="intro">
    <div style="font-size:.95rem;color:#64748b;font-weight:700">方針</div>
    <div style="font-size:1.4rem;font-weight:900;margin-top:4px">フェーズ単位で、全誤答を徹底解説ページへ分割</div>
    <p style="margin-top:8px;color:#334155">Phase 1 から順に進み、各 EX ページで実際に間違えた問題だけを確認します。各設問では記録された問題全文を正本として、正答理由・誤答理由・叩き直しポイントを整理しています。</p>
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
        html_text = build_domain_page(item, review_mode="wrong")
        for outdir in ["dist", "textbooks"]:
            out = ROOT / outdir / review_filename(item["ex_id"], "wrong")
            out.write_text(html_text, encoding="utf-8")
            print(f"wrote {out}")

    for item in ranked:
        html_text = build_domain_page(item, review_mode="correct")
        for outdir in ["dist", "textbooks"]:
            out = ROOT / outdir / review_filename(item["ex_id"], "correct")
            out.write_text(html_text, encoding="utf-8")
            print(f"wrote {out}")

    hub = build_hub_page(phases)
    for outdir in ["dist", "textbooks"]:
        out = ROOT / outdir / review_hub_filename("wrong")
        out.write_text(hub, encoding="utf-8")
        print(f"wrote {out}")

    correct_hub = build_correct_hub_page(ranked)
    for outdir in ["dist", "textbooks"]:
        out = ROOT / outdir / review_hub_filename("correct")
        out.write_text(correct_hub, encoding="utf-8")
        print(f"wrote {out}")

    center = build_center_page(ranked)
    for outdir in ["dist", "textbooks"]:
        out = ROOT / outdir / "mock_exam_dashboard.html"
        out.write_text(center, encoding="utf-8")
        print(f"wrote {out}")

    for phase in phases:
        phase_html = build_phase_page(phase)
        for outdir in ["dist", "textbooks"]:
            out = ROOT / outdir / f"phase{phase['phase']}_reinforce.html"
            out.write_text(phase_html, encoding="utf-8")
            print(f"wrote {out}")


if __name__ == "__main__":
    main()
