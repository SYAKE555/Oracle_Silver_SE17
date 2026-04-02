window.dataBuffer = [
  {
    "id": "OSLV-D1-001",
    "category": "D1-SQLとリレーショナルデータベースの基礎",
    "text": "以下のSELECT文の出力として正しいものはどれか。\n```sql\nSELECT last_name || ', ' || first_name AS full_name\nFROM employees\nWHERE employee_id = 100;\n```\nlast_name='King', first_name='Steven' のとき。",
    "type": "choice",
    "answer": "B. King, Steven",
    "options": [
      "A. King Steven",
      "B. King, Steven",
      "C. 'King', 'Steven'",
      "D. KingSteven"
    ],
    "logic": "正解は「King, Steven」である。Oracle SQLの連結演算子||は文字列を結合する。'King' || ', ' || 'Steven' の結果は 'King, Steven' となる。AS full_name は列の別名を定義するが出力値には影響しない。選択肢Aはカンマとスペースがない。選択肢Cはシングルクォートが余分に含まれている。選択肢Dは区切りなしの結合となっている。Oracle SQL Reference §連結演算子参照。",
    "plan": "連結演算子||の動作を確認し、文字列リテラル（シングルクォート）と列名の違いを整理すること。AS句による列別名の書き方（スペースや特殊文字を含む場合はダブルクォートが必要）も確認すること。",
    "weight": 0.3,
    "textbook_ref": ["D1-SELECT基本"],
    "tags": ["連結演算子", "SELECT", "列別名", "AS"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D1-002",
    "category": "D1-SQLとリレーショナルデータベースの基礎",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT DISTINCT department_id\nFROM employees;\n```\nemployeesテーブルに department_id が 10,10,20,20,30,NULL,NULL の7行が存在する場合。",
    "type": "choice",
    "answer": "C. 10, 20, 30, NULL の4行",
    "options": [
      "A. 10, 20, 30 の3行（NULLは除外）",
      "B. 10, 10, 20, 20, 30 の5行",
      "C. 10, 20, 30, NULL の4行",
      "D. エラーになる"
    ],
    "logic": "正解は「10, 20, 30, NULL の4行」である。DISTINCTは重複行を除去するが、NULLも1つの値として扱われるため、NULLが複数あっても1行のNULLとして返される。したがって結果は 10, 20, 30, NULL の4行となる。選択肢AはNULLを除外しているため誤り。Oracle SQL Reference §SELECT文のDISTINCT句参照。",
    "plan": "DISTINCTキーワードの動作、特にNULLの扱いを確認すること。DISTINCTは複数列に適用した場合に列の組合せで重複判定することも押さえること。",
    "weight": 0.4,
    "textbook_ref": ["D1-SELECT基本"],
    "tags": ["DISTINCT", "NULL", "SELECT", "重複排除"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D1-003",
    "category": "D1-SQLとリレーショナルデータベースの基礎",
    "text": "NULLに関する説明として正しいものはどれか。",
    "type": "choice",
    "answer": "A. NULL + 100 の結果はNULLになる",
    "options": [
      "A. NULL + 100 の結果はNULLになる",
      "B. NULL = NULL はTRUEになる",
      "C. NULL は 0 と等しい",
      "D. NULLの列をORDER BYでソートすると常に先頭になる"
    ],
    "logic": "正解は「NULL + 100 の結果はNULLになる」である。NULLは「不明な値」であり、NULLを含む算術演算の結果は常にNULLになる。NULL = NULLはTRUEではなくUNKNOWNになるため、NULLの比較にはIS NULLまたはIS NOT NULLを使う必要がある。NULLは0でも空文字でもない。ORDER BYでのNULLの順序はデフォルトでは昇順（ASC）のとき最後、降順（DESC）のとき最初になる（NULLS FIRST/NULLS LASTで制御可能）。",
    "plan": "NULLの性質（未知の値）と算術演算・比較演算・論理演算でのNULLの伝播ルールを整理すること。IS NULL / IS NOT NULL の使い方、NVL・COALESCEでのNULL置換も合わせて学ぶこと。",
    "weight": 0.5,
    "textbook_ref": ["D1-NULL基礎"],
    "tags": ["NULL", "算術演算", "比較演算", "IS NULL"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D2-001",
    "category": "D2-データの絞り込みとソート",
    "text": "以下のSQL文で返される行を正しく説明しているものはどれか。\n```sql\nSELECT employee_id, salary\nFROM employees\nWHERE salary BETWEEN 5000 AND 10000;\n```",
    "type": "choice",
    "answer": "B. salary が 5000 以上かつ 10000 以下の行",
    "options": [
      "A. salary が 5000 より大きく 10000 より小さい行",
      "B. salary が 5000 以上かつ 10000 以下の行",
      "C. salary が 5000 未満または 10000 超の行",
      "D. salary が 5000 または 10000 の行のみ"
    ],
    "logic": "正解は「salary が 5000 以上かつ 10000 以下の行」である。BETWEEN x AND y は x <= 値 <= y の範囲を意味し、両端の値を含む（inclusive）。したがって salary = 5000 および salary = 10000 の行も結果に含まれる。選択肢Aは両端を含まない（exclusive）の説明であり誤り。BETWEENはNOT BETWEENで否定でき、数値・日付・文字列のいずれにも使用可能。Oracle SQL Reference §BETWEEN条件参照。",
    "plan": "BETWEENの両端包含（inclusive）を確実に覚えること。NOT BETWEENの動作、および日付型でのBETWEEN使用例（WHERE hire_date BETWEEN DATE'2020-01-01' AND DATE'2020-12-31'）も確認すること。",
    "weight": 0.4,
    "textbook_ref": ["D2-WHERE条件"],
    "tags": ["BETWEEN", "WHERE", "範囲条件", "inclusive"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D2-002",
    "category": "D2-データの絞り込みとソート",
    "text": "以下のSQL文の結果として正しいものはどれか。\n```sql\nSELECT last_name\nFROM employees\nWHERE last_name LIKE '_a%';\n```",
    "type": "choice",
    "answer": "C. 2文字目が 'a' の last_name を持つ全行",
    "options": [
      "A. 'a' を含む全ての last_name",
      "B. 'a' で始まる last_name",
      "C. 2文字目が 'a' の last_name を持つ全行",
      "D. 'a' で終わる last_name"
    ],
    "logic": "正解は「2文字目が 'a' の last_name を持つ全行」である。LIKEパターンの_（アンダースコア）は任意の1文字に一致し、%（パーセント）は0文字以上の任意の文字列に一致する。'_a%' は「1文字（何でもよい）」+「a」+「0文字以上（何でもよい）」のパターンであるため、2文字目が 'a' である文字列に一致する。例: 'James', 'Mary', 'Barry' 等。Oracle SQL Reference §LIKE条件参照。",
    "plan": "LIKEのワイルドカード文字_（1文字）と%（0文字以上）の違いを確認すること。ESCAPE句を使ったワイルドカード文字自体の検索（例: WHERE name LIKE '100\\%' ESCAPE '\\'）も押さえること。",
    "weight": 0.5,
    "textbook_ref": ["D2-LIKE条件"],
    "tags": ["LIKE", "ワイルドカード", "アンダースコア", "WHERE"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D2-003",
    "category": "D2-データの絞り込みとソート",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT last_name, salary\nFROM employees\nWHERE commission_pct IS NULL\nORDER BY salary DESC NULLS LAST;\n```\ncommission_pctがNULLの行には salary = 8000, 5000, NULL の3行があるとする。",
    "type": "choice",
    "answer": "B. salary: 8000 → 5000 → NULL の順で3行",
    "options": [
      "A. salary: NULL → 8000 → 5000 の順で3行",
      "B. salary: 8000 → 5000 → NULL の順で3行",
      "C. salary: 5000 → 8000 → NULL の順で3行",
      "D. エラーになる（NULLをORDER BYに使えない）"
    ],
    "logic": "正解は「salary: 8000 → 5000 → NULL の順で3行」である。ORDER BY salary DESC はsalaryを降順にソートする。NULLS LAST を指定すると、NULLの値を持つ行はソート結果の末尾に配置される。IS NULLはNULL値を持つ行を選択する正しい構文（= NULLは使えない）。ORDER BYのデフォルトNULL順序は昇順（ASC）ではNULLS LAST、降順（DESC）ではNULLS FIRSTとなる。NULLS FIRST/NULLS LASTで明示的に制御できる。",
    "plan": "ORDER BYにおけるNULLの扱いを整理すること。ASC/DESCとNULLS FIRST/NULLS LASTの組み合わせ4パターンを確認すること。IS NULLとIS NOT NULLの使い方を覚えること。",
    "weight": 0.5,
    "textbook_ref": ["D2-ORDER BY"],
    "tags": ["ORDER BY", "DESC", "NULLS LAST", "IS NULL"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D2-004",
    "category": "D2-データの絞り込みとソート",
    "text": "以下のSQL文と同じ結果を返すものはどれか。\n```sql\nSELECT employee_id FROM employees\nWHERE department_id IN (10, 20, 30);\n```",
    "type": "choice",
    "answer": "A. WHERE department_id = 10 OR department_id = 20 OR department_id = 30",
    "options": [
      "A. WHERE department_id = 10 OR department_id = 20 OR department_id = 30",
      "B. WHERE department_id = 10 AND department_id = 20 AND department_id = 30",
      "C. WHERE department_id BETWEEN 10 AND 30",
      "D. WHERE department_id >= 10 AND department_id <= 30"
    ],
    "logic": "正解は「WHERE department_id = 10 OR department_id = 20 OR department_id = 30」である。IN (x, y, z) は各値とのOR条件と等価であり、リストに含まれるいずれかの値に一致する行を返す。選択肢BはAND条件のため、1つの列が同時に10・20・30になることはなく結果は0行。選択肢CのBETWEEN 10 AND 30は10〜30の連続した範囲（15や25も含む）なので異なる。選択肢Dも同様に範囲条件で異なる。",
    "plan": "IN句とOR条件の等価性を理解すること。NOT INの動作、特にリストにNULLが含まれる場合（NOT IN (10, NULL)は常に結果0行になる）の挙動を確認すること。",
    "weight": 0.4,
    "textbook_ref": ["D2-IN条件"],
    "tags": ["IN", "OR", "WHERE", "比較条件"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D3-001",
    "category": "D3-単一行関数",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT ROUND(45.926, 2), TRUNC(45.926, 2)\nFROM DUAL;\n```",
    "type": "choice",
    "answer": "B. 45.93 と 45.92",
    "options": [
      "A. 45.92 と 45.93",
      "B. 45.93 と 45.92",
      "C. 46 と 45",
      "D. 45.926 と 45.926"
    ],
    "logic": "正解は「45.93 と 45.92」である。ROUND(45.926, 2)は小数点第2位で四捨五入する。第3位が6（5以上）なので第2位が繰り上がり 45.93 となる。TRUNC(45.926, 2)は小数点第2位以下を切り捨てる（四捨五入しない）。したがって 45.92 となる。DUALは計算結果など値を返すためだけに使うOracleの仮想表。選択肢Cは第0位での操作の結果であり誤り。Oracle SQL Reference §ROUND, TRUNC参照。",
    "plan": "ROUND(数値, 桁数)とTRUNC(数値, 桁数)の違い（四捨五入 vs 切り捨て）を確認すること。桁数が負の場合（例: ROUND(456, -2) = 500）の動作も押さえること。DUALテーブルの用途も覚えること。",
    "weight": 0.5,
    "textbook_ref": ["D3-数値関数"],
    "tags": ["ROUND", "TRUNC", "数値関数", "DUAL"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D3-002",
    "category": "D3-単一行関数",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT NVL2(commission_pct, salary * commission_pct, 0)\nFROM employees\nWHERE employee_id = 100;\n```\nemployee_id=100 は commission_pct = NULL, salary = 24000 とする。",
    "type": "choice",
    "answer": "C. 0",
    "options": [
      "A. 24000",
      "B. NULL",
      "C. 0",
      "D. エラーになる"
    ],
    "logic": "正解は「0」である。NVL2(expr1, expr2, expr3)は expr1 がNULLでなければ expr2 を返し、NULLであれば expr3 を返す。commission_pctがNULLのため、expr3である0が返される。NVL(expr1, expr2)との違いは、NVLはNULLのとき代替値を返すだけだが、NVL2はNULLでない場合の式も指定できる点。この例はNULLでない場合は歩合給計算、NULLの場合は0を返す典型的な使い方。Oracle SQL Reference §NVL2参照。",
    "plan": "NULL関数を整理すること: NVL(expr1, expr2)はNULLなら expr2、NVL2(expr1, expr2, expr3)はNULLでなければ expr2・NULLなら expr3、COALESCE(a,b,c...)は左から最初のNULL以外の値、NULLIF(a,b)はaとbが等しければNULL・異なればaを返す。",
    "weight": 0.6,
    "textbook_ref": ["D3-NULL関数"],
    "tags": ["NVL2", "NULL関数", "NVL", "COALESCE"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D3-003",
    "category": "D3-単一行関数",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT SUBSTR('ABCDEFG', 3, 4) FROM DUAL;\n```",
    "type": "choice",
    "answer": "B. CDEF",
    "options": [
      "A. BCD",
      "B. CDEF",
      "C. ABCD",
      "D. BCDE"
    ],
    "logic": "正解は「CDEF」である。SUBSTR(string, start, length)はstringのstart位置からlength文字を取り出す。Oracleの文字列インデックスは1始まりである。'ABCDEFG'の3番目の文字は'C'であり、そこから4文字（C, D, E, F）を取り出すと'CDEF'となる。選択肢AはSUBSTR('ABCDEFG', 2, 3)の結果。選択肢DはSUBSTR('ABCDEFG', 2, 4)の結果。Oracle SQL Reference §SUBSTR参照。",
    "plan": "SUBSTR(str, start, length)の引数を確認すること。startが負の場合（末尾からカウント）の動作も押さえること。関連関数のINSTR（文字列の位置を返す）、LENGTH（文字列長）とあわせて整理すること。",
    "weight": 0.5,
    "textbook_ref": ["D3-文字列関数"],
    "tags": ["SUBSTR", "文字列関数", "インデックス"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D3-004",
    "category": "D3-単一行関数",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT\n  CASE job_id\n    WHEN 'IT_PROG' THEN '開発'\n    WHEN 'SA_MAN'  THEN '営業'\n    ELSE 'その他'\n  END AS job_type\nFROM employees\nWHERE employee_id = 200;\n```\nemployee_id=200 の job_id = 'HR_REP' とする。",
    "type": "choice",
    "answer": "D. その他",
    "options": [
      "A. 開発",
      "B. 営業",
      "C. NULL",
      "D. その他"
    ],
    "logic": "正解は「その他」である。CASE式の単純CASE形式はWHEN節で指定した値と一致するかを順番に比較する。job_id = 'HR_REP'は'IT_PROG'にも'SA_MAN'にも一致しないため、ELSEの'その他'が返される。ELSE句がない場合、どのWHEN条件にも一致しないときNULLが返される。CASE式はSELECT句・WHERE句・ORDER BY句などで使用できる。Oracle SQL Reference §CASE式参照。",
    "plan": "単純CASE式と検索CASE式（WHEN 条件式 THEN...）の2種類を区別して覚えること。ELSEなしのCASEでは不一致時にNULLが返ることも押さえること。DECODE関数（Oracle固有）との違いも確認すること。",
    "weight": 0.5,
    "textbook_ref": ["D3-CASE式"],
    "tags": ["CASE", "WHEN", "ELSE", "DECODE"],
    "difficulty": "Easy"
  },
  {
    "id": "OSLV-D4-001",
    "category": "D4-グループ関数と集計",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT COUNT(*), COUNT(commission_pct), AVG(commission_pct)\nFROM employees;\n```\n全107行のうち commission_pct が NULL でない行が35行、NULLの行が72行あるとする。",
    "type": "choice",
    "answer": "B. 107, 35, NULL以外の35行の平均値",
    "options": [
      "A. 107, 107, 全107行の平均値",
      "B. 107, 35, NULL以外の35行の平均値",
      "C. 35, 35, NULL以外の35行の平均値",
      "D. 107, 35, 0"
    ],
    "logic": "正解は「107, 35, NULL以外の35行の平均値」である。COUNT(*)はNULLを含む全行数を数えるので107。COUNT(列名)はNULL以外の行数を数えるので35。AVG(列名)もNULLを無視して計算するため、NULL以外の35行の合計÷35となる。グループ関数（COUNT, SUM, AVG, MAX, MIN）はCOUNT(*)以外すべてNULLを無視する。ただしCOUNT(*)のみNULLを含む全行を数える特別な動作をする。Oracle SQL Reference §グループ関数参照。",
    "plan": "グループ関数とNULLの関係を整理すること。COUNT(*)は全行、COUNT(列)はNULL以外の行を数える違いを確実に覚えること。SUM・AVG・MAX・MINもNULLを無視することを確認すること。",
    "weight": 0.6,
    "textbook_ref": ["D4-グループ関数"],
    "tags": ["COUNT", "AVG", "NULL", "グループ関数"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D4-002",
    "category": "D4-グループ関数と集計",
    "text": "以下のSQL文はエラーになる。その理由として正しいものはどれか。\n```sql\nSELECT department_id, last_name, AVG(salary)\nFROM employees\nGROUP BY department_id;\n```",
    "type": "choice",
    "answer": "B. last_nameがGROUP BY句にもグループ関数にも含まれていないため",
    "options": [
      "A. AVG関数はGROUP BYと一緒に使えないため",
      "B. last_nameがGROUP BY句にもグループ関数にも含まれていないため",
      "C. department_idとlast_nameを同時にSELECTできないため",
      "D. エラーにはならない"
    ],
    "logic": "正解は「last_nameがGROUP BY句にもグループ関数にも含まれていないため」である。GROUP BYを使う場合、SELECT句に書ける列は（1）GROUP BY句に含まれている列、または（2）グループ関数（AVG, COUNT等）で集計した列のみである。last_nameはGROUP BY department_idに含まれておらず、グループ関数でも囲まれていないため、ORA-00979エラーが発生する。department_idとAVG(salary)はルールを満たしているので問題ない。",
    "plan": "GROUP BY使用時のSELECT句のルール（グループ化列とグループ関数のみ）を確実に覚えること。WHERE句とHAVING句の違い（WHEREはグループ化前の絞り込み、HAVINGはグループ化後の絞り込み）も整理すること。",
    "weight": 0.7,
    "textbook_ref": ["D4-GROUP BY"],
    "tags": ["GROUP BY", "ORA-00979", "SELECT制約", "グループ関数"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D4-003",
    "category": "D4-グループ関数と集計",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nSELECT department_id, AVG(salary)\nFROM employees\nGROUP BY department_id\nHAVING AVG(salary) > 8000\nORDER BY AVG(salary) DESC;\n```",
    "type": "choice",
    "answer": "C. 部署ごとの平均給与を計算し、平均が8000超の部署のみを降順で表示する",
    "options": [
      "A. 全社員の中から給与が8000超の社員を部署ごとに集計して降順表示",
      "B. HAVING句はWHERE句の代わりなのでWHERE AVG(salary) > 8000 と同じ",
      "C. 部署ごとの平均給与を計算し、平均が8000超の部署のみを降順で表示する",
      "D. エラーになる（HAVING句にはグループ関数を使えない）"
    ],
    "logic": "正解は「部署ごとの平均給与を計算し、平均が8000超の部署のみを降順で表示する」である。SQL実行順序はFROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY。HAVING句はGROUP BYでグループ化された後の結果を絞り込む。選択肢AはHAVINGではなくWHEREを使った場合の説明で、個々の行を絞り込むもの。選択肢BはWHERE句にはグループ関数は書けないので誤り。HAVINGにはグループ関数の条件を書くことができる。",
    "plan": "SQL句の実行順序（FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY）を覚えること。WHEREは個別行の絞り込み（グループ関数使用不可）、HAVINGはグループの絞り込み（グループ関数使用可）の違いを確認すること。",
    "weight": 0.7,
    "textbook_ref": ["D4-HAVING"],
    "tags": ["HAVING", "GROUP BY", "AVG", "SQL実行順序"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D5-001",
    "category": "D5-複数表の結合",
    "text": "以下のSQL文の結果として正しいものはどれか。\n```sql\nSELECT e.last_name, d.department_name\nFROM employees e\nJOIN departments d ON e.department_id = d.department_id;\n```\nemployeesに department_id = NULL の社員が2名いるとする。",
    "type": "choice",
    "answer": "B. department_idがNULLの社員2名は結果に含まれない",
    "options": [
      "A. department_idがNULLの社員2名もNULLとして結果に含まれる",
      "B. department_idがNULLの社員2名は結果に含まれない",
      "C. エラーになる（NULLを持つ列はJOINに使えない）",
      "D. NULLとNULLが一致するとみなされdepartmentsのNULL行と結合される"
    ],
    "logic": "正解は「department_idがNULLの社員2名は結果に含まれない」である。INNER JOIN（JOINとだけ書いた場合もINNER JOIN）は結合条件に一致する行のみを返す。NULLは何とも等しくないため（NULL = NULLはUNKNOWN）、ON e.department_id = d.department_idはNULLの場合に一致しない。NULLの社員も含めたい場合はLEFT OUTER JOINを使う。選択肢DはNULL同士を等しいとみなすことはないため誤り。",
    "plan": "INNER JOINとOUTER JOINの違いを理解すること。LEFT/RIGHT/FULL OUTER JOINの動作をベン図で確認すること。NULLを含む結合条件の動作（NULLは一致しない）を確認すること。",
    "weight": 0.6,
    "textbook_ref": ["D5-INNER JOIN"],
    "tags": ["INNER JOIN", "NULL", "結合条件", "ON"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D5-002",
    "category": "D5-複数表の結合",
    "text": "以下のSQL文の実行結果の行数として正しいものはどれか。\n```sql\nSELECT e.last_name, d.department_name\nFROM employees e\nLEFT OUTER JOIN departments d\nON e.department_id = d.department_id;\n```\nemployees: 107行（うち department_id = NULL が2行）、departments: 27行",
    "type": "choice",
    "answer": "A. 107行（NULLの社員2名はdepartment_nameがNULLで表示）",
    "options": [
      "A. 107行（NULLの社員2名はdepartment_nameがNULLで表示）",
      "B. 105行（NULLの社員は除外）",
      "C. 27行（departmentsの行数に合わせる）",
      "D. 134行（107 + 27）"
    ],
    "logic": "正解は「107行（NULLの社員2名はdepartment_nameがNULLで表示）」である。LEFT OUTER JOINは左表（employees）の全行を必ず結果に含める。右表（departments）で対応する行がない場合（NULLの社員の場合）、右表の列はNULLとして表示される。したがって employees の全107行が返され、department_id = NULLの2名はdepartment_nameがNULLとなる。INNER JOINなら105行、RIGHT OUTER JOINなら右表基準。",
    "plan": "LEFT/RIGHT/FULL OUTER JOINの返行数を理解すること。LEFT JOIN: 左表全行＋右表一致行（不一致はNULL）。RIGHT JOIN: 右表全行＋左表一致行（不一致はNULL）。FULL JOIN: 両表全行（不一致はNULL）。",
    "weight": 0.7,
    "textbook_ref": ["D5-OUTER JOIN"],
    "tags": ["LEFT OUTER JOIN", "OUTER JOIN", "NULL", "行数"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D5-003",
    "category": "D5-複数表の結合",
    "text": "以下のSQL文（自己結合）の目的として正しいものはどれか。\n```sql\nSELECT e.last_name AS 社員名,\n       m.last_name AS 上司名\nFROM employees e\nJOIN employees m ON e.manager_id = m.employee_id;\n```",
    "type": "choice",
    "answer": "C. 社員とその上司の名前を同じテーブルから取得する",
    "options": [
      "A. 全社員の部下一覧を表示する",
      "B. manager_idがNULLの社員のみを表示する",
      "C. 社員とその上司の名前を同じテーブルから取得する",
      "D. エラーになる（同じテーブルをJOINできない）"
    ],
    "logic": "正解は「社員とその上司の名前を同じテーブルから取得する」である。自己結合（SELF JOIN）は同一テーブルに対して別名（エイリアス）を2つ付けてJOINする手法。ここではemployeesテーブルをe（社員側）とm（上司側）として結合し、e.manager_id = m.employee_idで社員の上司IDと上司のemployee_idを一致させる。manager_idがNULLの社員（最上位管理者）はINNER JOINなので結果に含まれない。LEFT JOINにすれば全社員＋上司名NULLの行が含まれる。",
    "plan": "自己結合の用途（同一テーブル内の親子関係、階層構造の表現）を理解すること。別名（エイリアス）が必須であることを覚えること。INNER JOINとLEFT JOINの選択が結果に影響することを確認すること。",
    "weight": 0.6,
    "textbook_ref": ["D5-自己結合"],
    "tags": ["自己結合", "SELF JOIN", "エイリアス", "階層"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D6-001",
    "category": "D6-サブクエリ",
    "text": "以下のSQL文の動作として正しいものはどれか。\n```sql\nSELECT last_name, salary\nFROM employees\nWHERE salary > (SELECT AVG(salary) FROM employees);\n```",
    "type": "choice",
    "answer": "A. 全社員の平均給与より高い給与を受け取る社員の名前と給与を返す",
    "options": [
      "A. 全社員の平均給与より高い給与を受け取る社員の名前と給与を返す",
      "B. 部署ごとの平均給与より高い給与を受け取る社員を返す",
      "C. エラーになる（WHERE句にサブクエリは使えない）",
      "D. サブクエリが複数行返す場合にエラーになる"
    ],
    "logic": "正解は「全社員の平均給与より高い給与を受け取る社員の名前と給与を返す」である。このサブクエリは単一行サブクエリ（AVGは1つの値を返す）であり、=, >, <, >=, <=などの単一行比較演算子と使用できる。外側のクエリはサブクエリが返した平均値と各行のsalaryを比較する。WHERE句にサブクエリは使用可能。サブクエリが複数行を返す可能性がある場合はIN, ANY, ALLなどの複数行演算子を使う必要がある。",
    "plan": "単一行サブクエリ（1値を返す）と複数行サブクエリ（複数行を返す）の違いを理解すること。単一行演算子（=, >, <等）は単一行サブクエリにのみ使用可能。複数行にはIN/ANY/ALLが必要。サブクエリが0行を返した場合の動作も確認すること。",
    "weight": 0.6,
    "textbook_ref": ["D6-単一行サブクエリ"],
    "tags": ["サブクエリ", "単一行サブクエリ", "AVG", "WHERE"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D6-002",
    "category": "D6-サブクエリ",
    "text": "以下のSQL文の動作として正しいものはどれか。\n```sql\nSELECT last_name, salary\nFROM employees\nWHERE salary = ANY (\n  SELECT MIN(salary)\n  FROM employees\n  GROUP BY department_id\n);\n```",
    "type": "choice",
    "answer": "B. いずれかの部署の最低給与と一致する給与を持つ社員を返す",
    "options": [
      "A. 全部署の最低給与と一致する給与を持つ社員のみを返す",
      "B. いずれかの部署の最低給与と一致する給与を持つ社員を返す",
      "C. 最低給与が最も低い部署の社員のみを返す",
      "D. エラーになる（= ANY は不正な構文）"
    ],
    "logic": "正解は「いずれかの部署の最低給与と一致する給与を持つ社員を返す」である。= ANY は複数行サブクエリで使用し、「いずれかの値と等しい」という意味になる（INと同等の動作）。サブクエリは部署ごとの最低給与をリストで返す。外側のクエリはそのリスト内のいずれかの値とsalaryが一致する社員を返す。= ALLは「すべての値と等しい」、> ANYは「いずれかの値より大きい（最小値より大きい）」、> ALLは「すべての値より大きい（最大値より大きい）」を意味する。",
    "plan": "複数行演算子 IN, = ANY, > ANY, > ALL, < ANY, < ALL の意味を整理すること。= ANYはINと同等。> ANYは最小値より大きい。> ALLは最大値より大きい。NOT INと != ALLの等価性も確認すること。",
    "weight": 0.7,
    "textbook_ref": ["D6-複数行サブクエリ"],
    "tags": ["ANY", "複数行サブクエリ", "MIN", "IN"],
    "difficulty": "Hard"
  },
  {
    "id": "OSLV-D6-003",
    "category": "D6-サブクエリ",
    "text": "以下のSQL文で EXISTS を使う効果として正しいものはどれか。\n```sql\nSELECT department_id, department_name\nFROM departments d\nWHERE EXISTS (\n  SELECT 1 FROM employees e\n  WHERE e.department_id = d.department_id\n);\n```",
    "type": "choice",
    "answer": "C. 少なくとも1名の社員が所属する部署のみを返す",
    "options": [
      "A. 全部署の社員数を返す",
      "B. 社員が1名もいない部署のみを返す",
      "C. 少なくとも1名の社員が所属する部署のみを返す",
      "D. エラーになる（相関サブクエリのSELECTは * のみ使用可能）"
    ],
    "logic": "正解は「少なくとも1名の社員が所属する部署のみを返す（選択肢C）」である。EXISTSは相関サブクエリが1行以上の結果を返せばTRUE、0行ならFALSEとなる。SELECT 1（またはSELECT *）は実際の値ではなくEXISTSの存在チェックに使うため、列の内容は何でもよい。外側クエリのdをサブクエリ内で参照している（d.department_id）のが相関の部分。NOT EXISTSにすると社員が1名もいない部署を返す。",
    "plan": "EXISTS / NOT EXISTS の動作（行が存在するか否か）を理解すること。相関サブクエリ（外側クエリの値をサブクエリ内で参照）の実行メカニズムを理解すること。EXISTSとINの違い（NULLの扱い、パフォーマンス）を確認すること。",
    "weight": 0.8,
    "textbook_ref": ["D6-EXISTS"],
    "tags": ["EXISTS", "相関サブクエリ", "NOT EXISTS"],
    "difficulty": "Hard"
  },
  {
    "id": "OSLV-D7-001",
    "category": "D7-DML（データ操作言語）",
    "text": "以下のSQL操作を実行した後の状態として正しいものはどれか。\n```sql\nINSERT INTO departments VALUES (280, 'Training', NULL, NULL);\nSAVEPOINT sp1;\nUPDATE departments SET department_name = 'Education' WHERE department_id = 280;\nROLLBACK TO sp1;\n```",
    "type": "choice",
    "answer": "B. department_id=280 のdepartment_nameは 'Training' になる（UPDATEがロールバックされた）",
    "options": [
      "A. department_id=280 の行は存在しない（ROLLBACKで全て取り消された）",
      "B. department_id=280 のdepartment_nameは 'Training' になる（UPDATEがロールバックされた）",
      "C. department_id=280 のdepartment_nameは 'Education' のままになる",
      "D. エラーになる（SAVEPOINTとROLLBACKは同一トランザクションで使えない）"
    ],
    "logic": "正解は「department_id=280 のdepartment_nameは 'Training' になる（UPDATEがロールバックされた）」である。SAVEPOINT sp1はsp1という中間保存点をトランザクション内に設定する。ROLLBACK TO sp1はsp1以降の変更（UPDATEのみ）を取り消し、sp1設定時点（INSERTの後）の状態に戻す。したがってINSERTは残り、UPDATEは取り消される。ROLLBACK（TO なし）は全変更を取り消す。COMMIT後はROLLBACKできない。Oracle SQL Reference §SAVEPOINT, ROLLBACK参照。",
    "plan": "トランザクション制御文（TCL）を整理すること: COMMIT（変更を確定）、ROLLBACK（全変更取り消し）、ROLLBACK TO セーブポイント名（セーブポイント以降の変更のみ取り消し）、SAVEPOINT（中間保存点の設定）。",
    "weight": 0.7,
    "textbook_ref": ["D7-トランザクション"],
    "tags": ["SAVEPOINT", "ROLLBACK", "トランザクション", "DML"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D7-002",
    "category": "D7-DML（データ操作言語）",
    "text": "DELETEとTRUNCATEの違いとして正しいものはどれか。",
    "type": "choice",
    "answer": "B. TRUNCATEはDDL文でありROLLBACKできない。DELETEはDML文でROLLBACK可能",
    "options": [
      "A. TRUNCATEはWHERE句で削除する行を指定できる",
      "B. TRUNCATEはDDL文でありROLLBACKできない。DELETEはDML文でROLLBACK可能",
      "C. DELETEはテーブル定義ごと削除するがTRUNCATEはデータのみ削除する",
      "D. TRUNCATEもDELETEも同じくROLLBACKできる"
    ],
    "logic": "正解は「TRUNCATEはDDL文でありROLLBACKできない。DELETEはDML文でROLLBACK可能」である。TRUNCATE TABLEはDDL（データ定義言語）であり、実行時に暗黙的COMMITが行われるためROLLBACKできない。また全行を高速に削除するがWHERE句は使えない。DELETE FROMはDML（データ操作言語）であり、WHERE句で対象行を指定でき、COMMIT前ならROLLBACKで取り消せる。テーブル定義を削除するのはDROP TABLE。",
    "plan": "DELETE vs TRUNCATE の比較を整理すること: WHERE句の有無、ROLLBACK可否、ログ記録の有無、速度の違い。DROP TABLE（テーブル構造ごと削除）も合わせて3つを比較すること。",
    "weight": 0.6,
    "textbook_ref": ["D7-DELETE-TRUNCATE"],
    "tags": ["DELETE", "TRUNCATE", "DDL", "DML", "ROLLBACK"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D7-003",
    "category": "D7-DML（データ操作言語）",
    "text": "以下のUPDATE文の実行結果として正しいものはどれか。\n```sql\nUPDATE employees\nSET salary = salary * 1.1,\n    commission_pct = NVL(commission_pct, 0) + 0.05\nWHERE department_id = 80;\n```\ndepartment_id=80 の社員5名のうち commission_pctがNULLの社員が2名いるとする。",
    "type": "choice",
    "answer": "C. 5名全員のsalaryが10%増加し、NULLの社員のcommission_pctは0.05になる",
    "options": [
      "A. commission_pctがNULLの社員はUPDATE対象外になる",
      "B. NVLはUPDATE文では使えないためエラーになる",
      "C. 5名全員のsalaryが10%増加し、NULLの社員のcommission_pctは0.05になる",
      "D. commission_pctがNULLの社員のsalaryはNULLになる"
    ],
    "logic": "正解は「5名全員のsalaryが10%増加し、NULLの社員のcommission_pctは0.05になる」である。SET句では単一行関数（NVLなど）を使用できる。NVL(commission_pct, 0)はcommission_pctがNULLの場合0を返すので、0 + 0.05 = 0.05 が設定される。NULL以外の社員は既存値 + 0.05 となる。salary = salary * 1.1 も全行に適用される。WHERE句はdepartment_id = 80 の絞り込みのみ。",
    "plan": "UPDATE文のSET句では単一行関数・演算式が使用可能なことを確認すること。複数列を1つのUPDATE文で更新できることを覚えること（カンマ区切り）。サブクエリをSETに使う方法（UPDATE ... SET col = (SELECT ...)）も学ぶこと。",
    "weight": 0.6,
    "textbook_ref": ["D7-UPDATE"],
    "tags": ["UPDATE", "NVL", "SET", "DML"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D8-001",
    "category": "D8-DDL・オブジェクト管理",
    "text": "以下のCREATE TABLE文で定義された制約の説明として正しいものはどれか。\n```sql\nCREATE TABLE orders (\n  order_id    NUMBER(6)    CONSTRAINT pk_orders PRIMARY KEY,\n  customer_id NUMBER(6)    NOT NULL,\n  order_date  DATE         DEFAULT SYSDATE,\n  status      VARCHAR2(10) CONSTRAINT chk_status\n                           CHECK (status IN ('PENDING','SHIPPED','DONE'))\n);\n```",
    "type": "choice",
    "answer": "B. order_idは重複不可かつNOT NULL。order_dateは省略するとSYSDATEが入る。statusは3種の値のみ許可",
    "options": [
      "A. order_idは重複可能だがNOT NULL。statusはNULLも許可される",
      "B. order_idは重複不可かつNOT NULL。order_dateは省略するとSYSDATEが入る。statusは3種の値のみ許可",
      "C. customer_idはNULLを許可する。order_dateは省略するとNULLになる",
      "D. PRIMARY KEY制約はNULLを許可するUNIQUE制約と同じ"
    ],
    "logic": "正解は「order_idは重複不可かつNOT NULL。order_dateは省略するとSYSDATEが入る。statusは3種の値のみ許可」である。PRIMARY KEY = UNIQUE + NOT NULL の制約。customer_idはNOT NULL制約があるのでNULL不可。order_dateのDEFAULT SYSDATEはINSERT時に値を省略した場合に現在日時が自動設定される。CHECK制約はstatusが'PENDING','SHIPPED','DONE'の3値のみ許可（NULLはCHECKをパスするためNOT NULLと組み合わせが推奨）。",
    "plan": "各制約の特徴を整理すること: PRIMARY KEY（一意+NOT NULL）、UNIQUE（一意、NULL可）、NOT NULL、CHECK（条件式）、FOREIGN KEY（参照整合性）。DEFAULT句は制約ではなくデフォルト値設定。CHECK制約はNULLを通過することも覚えること。",
    "weight": 0.6,
    "textbook_ref": ["D8-制約"],
    "tags": ["PRIMARY KEY", "CHECK", "DEFAULT", "NOT NULL", "制約"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D8-002",
    "category": "D8-DDL・オブジェクト管理",
    "text": "以下のビュー(VIEW)に関する説明として正しいものはどれか。\n```sql\nCREATE OR REPLACE VIEW emp_view AS\nSELECT employee_id, last_name, salary\nFROM employees\nWHERE salary > 10000;\n```",
    "type": "choice",
    "answer": "C. ビューは実データを持たない仮想表。ベーステーブルが更新されると自動的に最新データを反映する",
    "options": [
      "A. ビューはデータを物理的にコピーして保存するため、ベーステーブル変更後も古いデータを返す",
      "B. このビューからはINSERT/UPDATEができない（ビューは常に読み取り専用）",
      "C. ビューは実データを持たない仮想表。ベーステーブルが更新されると自動的に最新データを反映する",
      "D. OR REPLACEを使うと既存のビューを削除して新規作成するためエラーが発生する"
    ],
    "logic": "正解は「ビューは実データを持たない仮想表。ベーステーブルが更新されると自動的に最新データを反映する」である。ビューはSELECT定義を保存するだけで実データは持たない。参照時にSQLを実行するためベーステーブルの変更をリアルタイムに反映する。OR REPLACEは既存ビューがあっても削除せずに置き換える（エラーにならない）。単純ビュー（グループ関数・DISTINCT・JOIN・演算列などがない）はDML操作も可能。",
    "plan": "ビューの特徴（仮想表、実データなし）を理解すること。CREATE VIEW vs CREATE OR REPLACE VIEW の違いを覚えること。DML操作可能な単純ビューと不可な複雑ビューの条件も確認すること。",
    "weight": 0.6,
    "textbook_ref": ["D8-VIEW"],
    "tags": ["VIEW", "CREATE OR REPLACE", "仮想表", "DML"],
    "difficulty": "Medium"
  },
  {
    "id": "OSLV-D8-003",
    "category": "D8-DDL・オブジェクト管理",
    "text": "以下のSQL文の実行結果として正しいものはどれか。\n```sql\nCREATE SEQUENCE emp_seq\n  START WITH 100\n  INCREMENT BY 10\n  MAXVALUE 200\n  NOCYCLE;\n\nSELECT emp_seq.NEXTVAL FROM DUAL;\nSELECT emp_seq.NEXTVAL FROM DUAL;\nSELECT emp_seq.CURRVAL FROM DUAL;\n```",
    "type": "choice",
    "answer": "B. 100, 110, 110",
    "options": [
      "A. 100, 110, 100",
      "B. 100, 110, 110",
      "C. 100, 100, 100",
      "D. 110, 120, 120"
    ],
    "logic": "正解は「100, 110, 110」である。NEXTVALは呼び出すたびにシーケンスをINCREMENT BY分進めて現在値を返す。最初のNEXTVAL: START WITH 100 なので 100。2回目のNEXTVAL: 100 + 10 = 110。CURRVALは現在のシーケンス値を返す（進めない）ため 110。NOCYCLEはMAXVALUEに達した後さらに呼ぶとエラーになる設定（CYCLEならSTART WITHから再開）。CURRVALはNEXTVALを一度も呼んでいないセッションでは使用できない点に注意。",
    "plan": "シーケンスのNEXTVAL（次の値を取得し進める）とCURRVAL（現在値を返す・進めない）の違いを覚えること。CYCLE/NOCYCLEの動作、SYNONYMの用途（別名定義）も合わせて学ぶこと。",
    "weight": 0.7,
    "textbook_ref": ["D8-SEQUENCE"],
    "tags": ["SEQUENCE", "NEXTVAL", "CURRVAL", "INCREMENT"],
    "difficulty": "Medium"
  }
];
