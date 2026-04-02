# Ping-t Oracle Master Silver SQL 2019 参考資料バインダー

- 作成日時: 2026-04-03 07:16:24 JST
- 取得対象: `https://mondai.ping-t.com/question_subjects/61`
- 取得問題数: **586**
- 取得参考URL数: **806**

## 分野別傾向サマリ

| 分野 | 問題数 | 参考URL数 | 傾向キーワード |
|---|---:|---:|---|
| DDL文 | 70 | 117 | SELECT, WHERE, GROUP BY, ORDER BY, JOIN, 副問合せ, INSERT, DELETE, CREATE, ALTER |
| DML文 | 53 | 65 | SELECT, WHERE, JOIN, 副問合せ, INSERT, UPDATE, DELETE, MERGE, CREATE, DROP |
| 変換関数および条件式 | 52 | 85 | SELECT, WHERE, ALTER, TIMESTAMP |
| データの制限およびソート | 50 | 50 | SELECT, WHERE, ORDER BY |
| 単一行関数 | 47 | 68 | SELECT, WHERE, HAVING, ORDER BY, ALTER |
| 副問合せ | 46 | 57 | SELECT, WHERE, GROUP BY, HAVING, ORDER BY, JOIN, 副問合せ, INSERT, UPDATE, DELETE |
| 索引、シノニムおよびシーケンス | 41 | 42 | SELECT, WHERE, GROUP BY, HAVING, ORDER BY, 副問合せ, UNION, INSERT, UPDATE, DELETE |
| 複数の表のデータ | 40 | 62 | SELECT, WHERE, ORDER BY, JOIN |
| グループ関数 | 36 | 45 | SELECT, WHERE, GROUP BY, HAVING, ORDER BY |
| ビュー | 31 | 35 | SELECT, WHERE, GROUP BY, JOIN, 副問合せ, INSERT, UPDATE, DELETE, CREATE, ALTER |
| Select文 | 29 | 39 | SELECT, WHERE, GROUP BY, HAVING, ORDER BY, CREATE |
| 集合演算子 | 25 | 46 | SELECT, WHERE, GROUP BY, ORDER BY, JOIN, 副問合せ, UNION |
| 異なるタイム・ゾーンでのデータ管理 | 23 | 32 | SELECT, WHERE, INSERT, UPDATE, CREATE, ALTER, TIMESTAMP, INTERVAL |
| ユーザ・アクセスの制御 | 23 | 30 | SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, TRUNCATE, VIEW, INDEX |
| リレーショナル・データベース | 12 | 20 |  |
| データ・ディクショナリ・ビュー | 8 | 13 | SELECT, WHERE, ORDER BY, INDEX |

## 問題別データ

### 問題ID 26420 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26420?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表のデータを以下の形式で表示させるためには、どの問い合わせを実行しますか(該当するものをすべて選択してください)。 従業員名's salary is 月給
- 解説要約: 文字リテラルの一部に一重引用符(')を使用する場合は、代替引用符q演算子を使用するか、一重引用符を2つ続けて記述します。 q演算子の引用符デリミタに使用できる文字は、 ・任意の文字(大文字と小文字は区別されます) ・[],<>,(),{}の組合せ となります。 以上より、 ・SELECT employee_name || q'{'s salary is }' || salary FROM employees; ・SELECT employee_name || '''s salary is ' || salary FROM employees; が正解となります。 その他の選択肢については以下のとおりです。 ・SELECT employee_name || "'s salary is " || salary FROM employees; 文字リテラルは二重引用符(")ではなく、一重引用符(')で囲みます。このSQL文はエラーとなります。 列の別名を指定する場合は、列別名を二重引用符(")で囲みますので混同しないようにしましょう。 ・SELECT employee_name || ''s...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#i42617

### 問題ID 26421 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26421?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表の構造を確認してください。 EMPLOYEES表の検索結果を以下の形式で表示させるためには、どの問い合わせを実行しますか(該当するものをすべて選択してください)。
- 解説要約: SQL文の実行結果に表示される列見出しを変更したい場合は、SELECT句に列別名を指定します。 列別名は項目名と列別名をスペースで区切るか、明示的にASキーワードで指定します。 列別名はオブジェクトのネーミング規則に従って命名されますが、大文字と小文字を区別したり、ネーミング規則に反する列別名(スペースを使用するなど)を使用する場合は、列別名を二重引用符(")で囲まなければなりません。 設問の問合せ結果の列見出しのうち、「社員No」では大文字と小文字が使用されており、「給与(年収)」では記号が使用されていますので、この2つの列見出しは列別名を"(二重引用符)で囲んで指定したことがわかります。 以上より、 ・SELECT employee_id "社員No", employee_name 社員名, salary "給与(月給)" FROM employees; ・SELECT employee_id AS "社員No", employee_name AS "社員名", salary AS "給与(月給)" FROM employees; が正解となります。 正解のSQL文の実行結果は次の...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55280
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements008.htm#i27570
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/ap_keywd001.htm#BABCJAEB

### 問題ID 26422 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26422?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 
- 解説要約: SELECT文の検索結果から重複した行を排除するには、SELECTキーワードの直後に1度だけDISTINCTキーワードを指定します。 DISTINCTキーワードに続けて複数の項目を指定した場合は、指定した項目の組合せで重複を排除した行が表示されます。 以上より、 ・SELECT DISTINCT prod_id, cust_id FROM sales; が正解となります。 正解のSELECT文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT prod_id, cust_id FROM sales; SELECT句にDISTINCTキーワードを指定しない場合は、検索結果として全ての行が出力されます。 ・SELECT DISTINCT prod_id, DISTINCT cust_id FROM sales; DISTINCTキーワードはSELECTキーワードの直後に1つだけ指定します。このSQL文はエラーとなります。 ・SELECT DISTINCT * FROM sales; DISTINCTキーワードを指定していますが、列を全て（*）として...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55272

### 問題ID 26423 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26423?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 算術演算子の優先順位として正しい記述はどれですか(該当するものを全て選択してください)。
- 解説要約: SQL文で使用できる算術演算子は次の通りです。 また、演算子の優先順位は次の通りです。 同じ優先順位の演算子が複数使われている場合は、左側の計算から順番に行われます。 以上より、 ・減算よりも乗算や除算のほうが優先順位が高い ・同じ優先順位の演算子がある場合は、左側から計算を行う が正解となります。 その他の選択肢については以下のとおりです。 ・優先順位が一番高いのは加算である 加算よりも乗算、除算の優先順位が高いので誤りです。 ・除算の優先順位が一番低い 除算よりも加算、減算の優先順位が低いので誤りです。 ・除算よりも乗算のほうが優先順位が高い 除算と乗算の優先順位は同じです。同じ優先順位の演算子が複数使われている場合は、左側の計算から順番に行われます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators002.htm#SQLRF51156

### 問題ID 26424 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26424?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: DEPARTMENTS表の構造を確認してください。 全ての列の値を表示するためには、どの問い合わせを実行しますか(該当するものをすべて選択してください)。
- 解説要約: 表から全ての列の値を表示するにはSELECT句に*(アスタリスク)を指定するか、全ての列名を列挙します。 以上より、 ・SELECT * FROM departments; ・SELECT department_id, department_name, manager_id FROM departments; が正解となります。 正解のSELECT文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT ALL FROM departments; ALLは検索結果の重複行を排除せずに表示するためのキーワードです。ALLキーワードのあとには表示する項目を記述する必要があります。 例) SELECT ALL employee_name FROM EMPLOYEES; ・SELECT DISTINCT FROM departments; DISTINCTは検索結果から重複した行を排除するためのキーワードです。DISTINCTキーワードのあとには表示する項目を記述する必要があります。 例) SELECT DISTINCT employee_name FRO...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#i2065646

### 問題ID 26425 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26425?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表の構造を確認してください。 hiredate, employee_id, employee_name の順番で検索結果を表示するためには、どの問い合わせを実行しますか。
- 解説要約: SELECT文の検索結果はSELECT句で指定した項目の順番通りに表示されます。 以上より、 ・SELECT hiredate, employee_id, employee_name FROM employees; が正解となります。 正解のSELECT文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT * FROM employeess; SELECT句の項目に*(アスタリスク)を指定すると、検索対象の表の全ての列を表示します。 ・SELECT employee_id, employee_name, hiredate FROM employees; SELECT句に指定された項目が表示順ではありません。このSQL文では、employee_id, employee_name, hiredate の順で検索結果が表示されます。 ・SELECT ALL FROM employees; ALLは検索結果の重複行を排除せずに表示するためのキーワードです。ALLキーワードのあとには表示する項目を記述する必要があります。 例) SELECT ALL em...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#i2065646

### 問題ID 26426 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26426?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: SQL*Plusのコマンドで、表の構造を表示するためのコマンドはどれですか(2つ選択してください)。
- 解説要約: 表構造を表示するためのSQL*PlusのコマンドはDESCRIBEコマンドです。 以上より、 ・DESCRIBE ・DESC が正解となります。 DESCRIBEコマンドは以下のように使用します。DESCと省略することもできます。 DESCRIBE 表名; または DESC 表名; 指定した表の「列の名前」「列でNULL値が許可されるかどうか」「列のデータ型・精度」の情報が表示されます。 その他の選択肢については以下のとおりです。 ・DECODE SQL文で分岐処理を行うためのOracle Database固有の関数です。 ・DISTINCT SELECT文で重複した検索結果を排除するためのキーワードです。 ・DEFAULT 表作成時に列の初期値を設定するためのオプションです。
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQPUG/GUID-2E7032A1-67E9-4E13-96B6-D8F7B138ECAA.htm

### 問題ID 26427 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26427?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表のSALARY列がNULL値だった場合、次のSELECT文の実行結果として正しい記述はどれですか。 SELECT '私の月給は' || salary || 'です。' FROM employees;
- 解説要約: 連結演算子||で文字列とNULL値を連結した結果は文字列となります。 設問ではSALARY列の値がNULL値なので、SALARY列を除いた文字列が連結されます。 以上より、 ・私の月給はです。 が正解となります。 設問のSQL文の実行結果は次のようになります。 SELECT '私の月給は' || salary || 'です。' FROM employees;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators003.htm#i997789

### 問題ID 26428 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26428?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 次の表示形式で検索結果を表示させるためには、どの問い合わせを実行しますか。
- 解説要約: SELECT句において、一重引用符(')で囲まれた文字と、表示する列の値を、||を使用して繋ぐことで、表示形式を書式化することができます。 以上より、 ・SELECT '従業員番号 : ' || employee_id || ' 従業員氏名 : ' || employee_name FROM employees; が正解となります。 正解のSELECT文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT "従業員番号 : " || employee_id || " 従業員氏名: " || employee_name FROM employees; 文字リテラルは二重引用符(")ではなく、一重引用符(')で囲みます。このSQL文はエラーとなります。 ・SELECT '従業員番号 : ' + employee_id + ' 従業員氏名: ' + employee_name FROM employees; 列の値と文字リテラルを連結するには連結演算子 || を使用します。このSQL文はエラーとなります。 ・SELECT 従業員番号 : || empl...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators003.htm#i997789
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#i42617

### 問題ID 26429 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26429?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次の2つのSQL文を実行した時のパフォーマンスについての記述として正しいものはどれですか。 1) SELECT employee_id, employee_name, department_id FROM employees WHERE department_id = 1 OR department_id = 2 OR department_id = 3; 2) SELECT employee_id, employee_name, department_id FROM employees WHERE department_id IN (1, 2, 3);
- 解説要約: IN演算子は、SQL文の実行時に内部的にOR演算子による条件のセットとして処理されるので、実行時のパフォーマンスに違いはありません。 以上より、 ・2つのSQL文のパフォーマンスに違いはない が正解となります。 設問のSQLの文の実行結果はそれぞれ次のようになります。 SQLを表示 SELECT employee_id, employee_name, department_id FROM employees WHERE department_id = 1 OR department_id = 2 OR department_id = 3; SQLを表示 SELECT employee_id, employee_name, department_id FROM employees WHERE department_id IN (1, 2, 3); 参考： IN演算子を使用すると、リストに指定した複数の値のいずれかと一致する行を検索できます。 IN演算子の指定方法は次のとおりです。 WHERE 項目名 IN (値1[, 値2, ...]) OR演算子で複数の条件を指定している場合には、IN...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions013.htm#i1050801

### 問題ID 26430 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26430?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文を実行した結果の説明として正しい記述はどれですか。 SELECT employee_id, employee_name, manager_id FROM employees WHERE manager_id = NULL;
- 解説要約: 列がNULL値であるかを判定するには、IS NULL演算子を使用します。IS NULL演算子では、列の値がNULL値である場合に条件が成立します。 NULL値は特殊な値ですので、列の値がNULL値かどうかの判定はIS NULL演算子以外の比較演算子ではできません。 設問のSQL文では、MANAGER_ID列がNULLである行を検索していますが、IS NULL演算子を使用していません。NULL値に対して=(等号)などの比較演算子を使用した場合、条件の判定がNULL値となり検索結果は1行も表示されません。（エラーにはなりません） 以上より、 ・検索結果が1件も表示されない が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, manager_id FROM employees WHERE manager_id = NULL; その他の選択肢については以下のとおりです。 ・EMPLOYEES表のMANAGER_ID列がNULL値のデータだけが表示される NULL値かどうかを判定するにはIS NU...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements005.htm#SQLRF51095

### 問題ID 26431 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26431?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文の実行結果として表示される列の組合せとして、正しいものはどれですか(該当するものを全て選択してください)。 SELECT department_id, employee_id, employee_name, salary, commission, hiredate FROM employees WHERE (department_id = 3 OR salary > 400000) AND commission <= 1200000 OR hiredate > '2008-04-01';
- 解説要約: WHERE句に条件が複数指定されている場合は、論理演算子の優先順位に従って条件が評価されます。 AND演算子とOR演算子ではAND演算子のほうが先に評価されますが、()括弧がある場合は、括弧内の演算子を優先して評価します。 WHERE (department_id = 3 OR salary > 400000) AND commission <= 1200000 OR hiredate > '2008-04-01'; 設問では「(department_id = 3 OR salary > 400000)」の部分が先に評価され、次にANDですので、「DEPARTMENT_ID列が3かSALARY列が400000より大きく、かつCOMMISSION列が1200000以下である」列（E）、または、「HIREDATE列が2008年4月1日より大きい（新しい）」列（B,C）が検索されます。 以上より、 ・E ・B ・C が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions004.htm#i1052219

### 問題ID 26432 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26432?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文の実行結果と同じ結果となるSQL文はどれですか。 SELECT department_id, department_name FROM departments WHERE department_id IN (1, 2, 5);
- 解説要約: IN演算子を使用して記述した条件は、OR演算子を使用して置き換えられます。 設問のSQL文で指定された条件は、DEPARTMENT_ID列の値が1か2か5であればよいので、OR演算子を使用して、 department_id = 1 OR deoartment_id = 2 OR department_id = 5 と置き換えることができます。 以上より、 ・SELECT department_id, department_name FROM departments WHERE department_id = 1 OR department_id = 2 OR department_id = 5; が正解となります。 設問のSQL文と正解のSQL文の実行結果はそれぞれ次のようになります。 SQLを表示 SELECT department_id, department_name FROM departments WHERE department_id IN (1, 2, 5); SQLを表示 SELECT department_id, department_name FROM depart...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions013.htm#i1050801

### 問題ID 26433 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26433?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: CUSTOMERS表の構造を確認して下さい。 CUSTOMERS表から、住所に「横浜市」という文字列を含む顧客を検索するには、どの問い合わせを実行しますか。
- 解説要約: LIKE演算子を使用すると、指定した文字パターンに一致した行を検索できます。 文字パターンには、任意の1文字と一致する「_」や、0文字以上の任意の文字列と一致する「%」といった、ワイルドカードを利用できます。 設問では「横浜市」を含む行を検索するので、文字パターンは'%横浜市%'となります。 以上より、 ・SELECT customer_id, cust_last_name || cust_first_name, cust_address FROM customers WHERE cust_address LIKE '%横浜市%'; が正解となります。 正解のSELECT文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT customer_id, cust_last_name || cust_first_name, cust_address FROM customers WHERE cust_address = '%横浜市%'; 文字パターンを指定するにはLIKE演算子を使用します。この条件では住所が「%横浜市%」という行を検索してしまいます...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions007.htm#i1034153

### 問題ID 26434 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26434?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のSALARY列の値が300,000以上600,000以下の行を表示するためには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。
- 解説要約: BETWEEN演算子で、指定した範囲の値を検索することができます。 また、「SALARY列の値が300,000以上」、「SALARY列の値が600,000以下」という2つの条件をAND演算子で指定しても同じ結果となります。 以上より、 ・SELECT employee_name, salary FROM employees WHERE salary BETWEEN 300000 AND 600000; ・SELECT employee_name, salary FROM employees WHERE salary >= 300000 AND salary <= 600000; が正解となります。 正解のSELECT文の実行結果は次のようになります。 SQLを表示 SELECT employee_name, salary FROM employees WHERE salary BETWEEN 300000 AND 600000; SQLを表示 SELECT employee_name, salary FROM employees WHERE salary >= 300000 AND s...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions011.htm#CJAGAIDD

### 問題ID 26435 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26435?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のDEPARTMENT_IDには1~5の値が登録されています。 EMPLOYEES表のDEPARTMENT_IDが1,2,3の従業員がヒットする条件として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: IN演算子を使用すると、リストに指定した複数の値のいずれかと一致する行を検索することができます。 設問ではDEPARTMENT_ID列の値が1,2,3のいずれかである行を検索するので、IN演算子を使用してDEPARTMENT_ID IN(1, 2, 3)のように条件を記述することができます。 また、IN演算子とNOT演算子を組み合わせると、リストに指定した値以外という条件を作ることができます。 なお、IN演算子はOR演算子を使用して置き換えが可能ですので、department_id IN (1, 2, 3)とdepartment_id = 1 OR department_id = 2 OR department_id = 3は等価です。 以上より、 ・WHERE department_id NOT IN (4, 5) ・WHERE department_id IN (1, 2, 3) ・WHERE department_id = 1 OR department_id = 2 OR department_id = 3 が正解となります。 設問の検索条件でEMPLOYEES表を検索すると次...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions013.htm#i1050801

### 問題ID 26436 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26436?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表に登録されている従業員のうち、2007年4月1日以降に入社した従業員を検索するのには、どの問い合わせを実行しますか。 ただし、日付書式は「RR-MM-DD」とします。
- 解説要約: WHERE句の条件に文字リテラルや日付リテラルを使用する場合は、一重引用符(')で囲まなければなりません。 また、日付リテラルの場合は、日付書式が区別されるため、環境にあった日付書式で日付リテラルを記述する必要があります。 設問では、日付書式は「RR-MM-DD(年-月-日)」ですので、2007年4月1日は、'07-04-01'のように記述します。 以上より、 ・SELECT employee_id, employee_name, hiredate FROM employees WHERE hiredate >= '07-04-01'; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT employee_id, employee_name, hiredate FROM employees WHERE hiredate >= 07-04-01; ・SELECT employee_id, employee_name, hiredate FROM employees WHERE hiredate >= "07-04...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#i2134734

### 問題ID 26437 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26437?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: WHERE句の説明として正しい記述はどれですか。
- 解説要約: 特定の条件に合致した行を検索したい場合は、SELECT文にWHERE句で条件を指定します。 以上より、 ・検索データの絞り込みを行える が正解となります。 その他の選択肢については以下のとおりです。 ・列別名を指定できる WHERE句では列別名を指定できません。 ・必ずSELECT句の直後に記述する WHERE句は必ずFROM句の後に記述します。 ・WHERE句には条件を1つだけ記述できる WHERE句には複数の条件を記述できます。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#i2134734

### 問題ID 26438 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26438?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 次のSELECT文で使われている機能として正しい記述はどれですか(該当するものをすべて選択してください)。 SELECT employee_id, employee_name, salary FROM employees WHERE salary >= 400000;
- 解説要約: SELECT文では「射影(投影)」、「選択」、「結合」の3つの機能を使用して表からデータを取得します。 射影(投影)：表から特定の列を取得します。 選択：表から特定の行を取得します 結合：複数の表のデータを関連付けて取得します 設問のSELECT文では、EMPLOYEES表のEMPLOYEE_ID,EMPLOYEE_NAME,SALARY列を取得し(射影)、WHERE句によってSALARY列の値が400,000以上の行を取得しています(選択)。 以上より、 ・射影(投影) ・選択 が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56306/sqllangu.htm#CNCPT88902

### 問題ID 26439 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26439?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: SELECT文に関する説明として正しい記述はどれですか(該当するものを2つ選択してください)。
- 解説要約: SELECT文で全ての列を検索する場合は、*(アスタリスク)を指定するか、全ての列名を,(カンマ)で区切って列挙します。 また、文字リテラルと日付リテラルは一重引用符(')で囲むのに対し、数値リテラルは囲む必要はありません。数値リテラルを一重引用符(')で囲むと文字リテラルとして扱われます。 以上より、 ・すべての列を検索する場合は*を指定する ・文字リテラルと日付リテラルは一重引用符(')で囲むが、数値リテラルは囲まない が正解となります。 その他の選択肢については以下のとおりです。 ・SELECT文に算術式を指定することはできない SQL文のFROM句以外の句で算術式を指定することができます。 ・SELECT文で検索した結果は最初の項目の昇順で表示される SELECT文で検索した結果はソートされません。検索結果をソートするにはORDER BY句を指定します。 ・列別名は一重引用符(')で囲む 列別名は二重引用符(")で囲むので誤りです。一重引用符で囲むのは文字リテラルや日付リテラルです。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#i2065646

### 問題ID 26440 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26440?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表の構造を確認してください。 次のSELECT文を実行したところ、年収に何も表示されない従業員がいました。原因として正しい記述はどれですか。 SELECT employee_name, salary * 12 FROM employees;
- 解説要約: 算術式の中にNULL値が含まれている場合、その演算結果はNULLとなります。 0は通常の演算の通り計算できますので、NULL値と0での演算結果の違いに注意しましょう。 以上より、 ・SALARY列の値が「NULL」の従業員がいるため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_name, salary * 12 FROM employees; その他の選択肢については以下のとおりです。 ・エラーが発生したため NULL値と数値の演算結果はNULLとなります。エラーとはなりません。 ・SALARY列の値が「0」の従業員がいるため 通常の数値の演算ですので、0 * 12 = 0 となります。 ・SALARY列の値が「スペース」の従業員がいるため EMPLOYEES表のSALARY列はNUMBER（数値）型ですので、スペースが登録されることはありません。 また、文字列で算術演算を行うとエラーとなります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements005.htm#i59110

### 問題ID 26441 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26441?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 重複行を排除した検索結果を表示させるためには、どの問い合わせを実行しますか。
- 解説要約: SELECT文の検索結果から重複した行を排除するには、SELECTキーワードの直後に1度だけDISTINCTキーワードを指定します。 以上より、 ・SELECT DISTINCT prod_id, cust_id FROM sales; が正解となります。 SALES表には次のデータが登録されています。 SQLを表示 SELECT * FROM sales; 正解のSQL文を実行すると、SELECT句に指定された項目の組合せが一意となる行だけが表示されます。 SQLを表示 SELECT DISTINCT prod_id, cust_id FROM sales; その他の選択肢については以下のとおりです。 ・SELECT DISTINCT(*) FROM sales; ・SELECT DISTINCT (prod_id, cust_id) FROM sales; DISTINCTキーワードの後の項目を()括弧で囲むとエラーになります。 ・SELECT DISTINCT prod_id, DISTINCT cust_id FROM sales; ・SELECT prod_id, cust_...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55272

### 問題ID 26442 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26442?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表の構造を確認してください。 次の実行結果となるようSELECT文を作成しましたが、期待通りの結果となりませんでした。 原因として正しい記述はどれですか(該当するものを全て選択してください)。 期待する実行結果： 作成したSELECT文： SELECT DISTINCT employee_id AS EMPLOYEEID, employee_name || q'['s Salary is ]' || salary yen FROM employees;
- 解説要約: 設問では、EMPLOYEE_NAME列とSALARY列を連結して、 EMPLOYEE_NAME's Salary is SALARYyen と表示させようとしています。 このうち、「's Salary is 」の部分と「yen」の部分は文字リテラルですので、列と連結演算子||で連結しなければなりません。 ですので、「yen」の部分は連結演算子で結合し、さらに文字リテラルですので以下のように一重引用符(')で囲む必要があります。 SELECT DISTINCT employee_id AS EMPLOYEEID, employee_name || q'['s Salary is ]' || salary || 'yen' FROM employees; 以上より、 ・「yen」を連結演算子で連結する必要がある ・「yen」はリテラルなので一重引用符(')で囲まなければならない が正解となります。 設問に記載されている誤ったSQL文と実行結果は次のとおりです。 SQLを表示 SELECT DISTINCT employee_id AS EMPLOYEEID, employee_name |...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators003.htm#i997789
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#i42617

### 問題ID 26443 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26443?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: ORDER BY句の説明として正しい記述はどれですか(該当するものを全て選択して下さい)。
- 解説要約: ORDER BY句には、ソートする項目として、列名、列別名、算術式、SELECT句に指定されている順番（数値）を指定できます。また、一度に複数の項目を指定することもできます。 以上より、 ・ORDER BY句に列別名を指定することができる ・ORDER BY句では、同時に複数の列を指定することができる が正解となります。 その他の選択肢については以下のとおりです。 ・ORDER BY句はFROM句の直後に記述しなければならない ORDER BY句はSELECT文の最後に記述します ・1つのSELECT文中にWHERE句とORDER BY句を同時に指定することはできない ORDER BY句はSELECT文の他の句と同時に指定することができます ・ORDER BY句では項目の昇順にしかソートできない DESCキーワードを記述すると降順にソートされます 参考： SELECT文の検索結果はどのような順番で表示されるか保証されていません。そのため、何らかの値によってソートされた検索結果が必要な場合はORDER BY句を指定します。 ORDER BY句はWHERE句など他の句と同時に指定できますが...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#i2053998

### 問題ID 26444 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26444?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: ORDER BY句によるソートの説明として間違っているものはどれですか。
- 解説要約: SELECT文の検索結果は行の表示順序が決まっていませんが、ORDER BY句を指定することで検索結果をソートして表示できます。 ソートの順序はソートする項目のデータ型によって次のようになります。 このようにNULL値は最も大きな値として扱われますので、昇順であれば最後、降順であれば先頭に表示されます。 以上より、 ・ソート項目にNULL値が混在していた場合のソート結果は不定である が間違った記述であり、この設問の正解となります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees ORDER BY salary DESC; その他の選択肢については以下のとおりです。 ・文字型のソートでは、大文字と小文字は区別される 文字型の場合は文字コード順にソートされるため、大文字小文字が区別されます。例えば、昇順の場合は大文字、小文字の順に表示されます。 SQLを表示 SELECT prod_id, prod_name FROM products ORDER BY prod_name; ・日付型の降順では新しい日付から順...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#i2053998

### 問題ID 26445 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26445?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表に登録されている従業員を年収の多い順に表示するには、どの問い合わせを実行しますか。 ただし、年収は SALARY列 の12倍に COMMISSION列 を加算して求めることとします。
- 解説要約: ORDER BY句では、ソートする項目として、算術式を指定する事ができます。 設問より、年収はSALARY列の12倍にCOMMISSION列を加算すればよいので、ORDER BY句にはこの計算式を指定すればよいことになります。また、年収の多い順に表示するとは降順に表示するということなので、DESCキーワードの記述が必要です。 以上より、 ・SELECT employee_id, employee_name, salary * 12 + commission FROM employees ORDER BY salary * 12 + commission DESC; が正解となります。 正解のSELECT文の実行結果は次のようになります。 ※先頭に(salary*12+commission)の値がNULLの行が表示されていますが、これはSALARY列またはCOMMISSION列がNULLである行があり、算術式の結果もNULLとなったためです。ソート時にはNULLは最も大きい値として扱われるため、降順の場合はNULLが先頭に表示されます。 その他の選択肢については以下のとおりです。 ・SE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#i2053998

### 問題ID 26446 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26446?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表に登録されている従業員を月収(SALARY列)の多い順に表示するためには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。
- 解説要約: ORDER BY句では、ソートする項目として、列別名やSELECT句に指定されている順番（数値）を指定できます。 大文字と小文字を区別するためなどに二重引用符(")で囲んだ列別名を使用している場合は、ORDER BY句でも同様に列別名を二重引用符(")で囲む必要があります。 SALARY列はSELECT句で左から3番目に指定されていますので、「ORDER BY 3」とすれば SALARY列でソートされます。 また、月収の多い順に表示するには、降順でソートする為のDESCキーワードが必要です。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees ORDER BY 3 DESC; ・SELECT employee_id ID, employee_name NAME, salary sal FROM employees ORDER BY sal DESC; ・SELECT employee_id, employee_name, salary "sal" FROM employees ORDER BY "sal" DE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#i2053998

### 問題ID 26447 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26447?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表に登録されている従業員を月収(SALARY列)の多い順に表示しようとしたところ、SALARY列がNULLの従業員が先頭に表示されました。 月収の多い順かつSALARY列がNULLである従業員のみ最後に表示するためには、どの問い合わせを実行しますか。
- 解説要約: NULL値はデフォルトで最も大きい値として扱われます。そのため、降順でソートを行うとソート項目がNULL値である行が必ず先頭に表示されることになります。 ORDER BY句では、昇順、降順にかかわらず、NULL値が含まれる行を先頭に表示するか最後に表示するかを指定することができます。 ・NULLS FIRST：NULL値が含まれる行を先頭に表示 ・NULLS LAST ：NULL値が含まれる行を最後に表示 ですので、DESCを指定してSALARY列を降順に表示し、NULLS LASTを指定してSALARY列がNULL値である行を最後に表示させます。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees ORDER BY salary DESC NULLS LAST; が正解となります。 正解のSELECT文の実行結果は次のようになります その他の選択肢については以下のとおりです。 ・SELECT employee_id, employee_name, salary FROM employees ORDER BY ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#i2053998

### 問題ID 26448 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26448?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表に登録されている従業員を、DEPARTMENT_ID列の昇順でソートし、さらにSALARY列の降順でソートした結果を表示するためには、どの問い合わせを実行しますか。
- 解説要約: ORDER BY句では、1度に複数の項目を指定してソートすることもできます。その場合、ORDER BY句に指定された順番でソート処理が行われます。 昇順（ASC 省略可）でソートするか降順（DESC）でソートするかは、項目ごとに指定することができます。 以上より、 ・SELECT department_id, employee_id, employee_name, salary FROM employees ORDER BY department_id, salary DESC; が正解となります。 正解のSELECT文の実行結果は次のようになります。まずDEPARTMENT_ID列で昇順（小さい順に）ソートし、DEPARTMENT_ID列の値が同じ行では、SALARY列で降順（大きい順に）ソートしています。 ※先頭にSALARY列の値がNULLの行が表示されています。ソート時にはNULLは最も大きい値として扱われるため、降順の場合はNULLが先頭に表示されます。 なお、DEPARTMENT_ID列とSALARY列で同じ値の行が複数登録されている場合、それらの行が表示される順番は保証さ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#i2053998

### 問題ID 26449 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26449?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表の従業員ID（employee_id）と従業員名（employee_name）を表示するためには、どの問い合わせを実行しますか。 ただし、表示するのは月収(SALARY列)が300,000以上でDEPARTMENT_IDの昇順に表示するものとします。
- 解説要約: ORDER BY句はWHERE句と同時に指定することができます。ORDER BY句とWHERE句を同時に指定すると、WHERE句によって絞り込まれた検索結果がORDER BY句でソートされ表示されます。 ただし、ORDER BY句はSELECT文の最後に指定しなければならないので、ORDER BY句よりも先にWHERE句を指定しなければなりません。 また、ORDER BY句には、設問のようにSELECT句で指定されていない項目を指定することもできます。ただし、SELECT句に指定していない項目でソートを行うと、ソートの基準となる項目が表示されないため、ソートされたデータであるかが分かりにくくなります。 以上より、 ・SELECT employee_id, employee_name FROM employees WHERE salary >= 300000 ORDER BY department_id ASC; が正解となります。 正解のSELECT文の実行結果は次のようになります。 ソートの基準となるDEPARTMENT_ID列が表示されていない為、実際にソートされているのか、この結...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#i2053998

### 問題ID 26450 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26450?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 置換変数に関する説明として、正しいものを全て選択して下さい。
- 解説要約: SQL*PlusやSQL Developerなどのツールでは、置換変数を利用できます。 置換変数を利用すると、WHERE句の条件などに指定する値を、SQL文の中に直接記述するのではなく、実行時に値を指定できるようになります。 置換変数には「&置換変数」と「&&置換変数」の2種類があり、「&置換変数」はSQL文実行後に変数の値が破棄されますが、「&&置換変数」はセッションを切断するまで値が保持されます。 なお、置換変数はWHERE句だけではなく、SQL文の全ての箇所で使用できます。 以上より、 ・実行時に条件などの値を指定することができる ・変数値を再利用する場合は「&&置換変数」を利用する ・「&置換変数」と「&&置換変数」の2種類がある が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQPUG/GUID-68AC9FF2-B92A-48D1-9699-133D47F8DDC1.htm

### 問題ID 26451 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26451?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: SQL関数に関する説明として誤っているものはどれですか。
- 解説要約: SQL関数とはOracleに予め用意されている関数のことです。 多くの関数が引数を必要としますが、SYSDATE関数など引数を必要としない関数もあります。 以上より、 ・SQL関数には常に引数が必要である が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions001.htm#CJAHCIID

### 問題ID 26452 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26452?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 「123456」を百の位で四捨五入します。正しい結果が得られるのはどれですか。
- 解説要約: ROUND関数は引数で与えられた数値を四捨五入して返します。 1番目の引数で与えられた数値が、小数点以下で2番目の引数の桁に丸められますが、2番目の引数に負の値が指定された場合は、整数値に丸められます。 例えば2番目の引数が-1の時は一の位、-2の時は十の位、-3の時は百の位で四捨五入します。 以上より、 ・ROUND(123456,-3) が正解となります。 選択肢の関数の、それぞれの実行結果は次のようになります。 SQLを表示 SELECT ROUND(123456,-2), ROUND(123456,3), ROUND(123456,100), ROUND(123456,-3) FROM dual; その他の選択肢については以下のとおりです。 ・ROUND(123456,3) ・ROUND(123456,100) 2番目の引数が正の値の場合には、小数点以下の該当する桁で四捨五入を行いますが、1番目の引数で与えられた数値が整数値（小数点以下が無い）のため、引数の値のまま返されます。 ・ROUND(123456,-2) 2番目の引数が-2ですので十の位で四捨五入が行われます。 参考：...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions155.htm#SQLRF00698

### 問題ID 26453 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26453?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL関数の実行結果として正しいものはどれですか。 TRUNC(10000 / 3, 2)
- 解説要約: TRUNC関数は、1番目の引数で与えられた数値が、小数点以下で2番目の引数の桁に切り捨てられます。 設問では、式10000÷3の結果（3333.333333・・・）を小数点以下2桁に切り捨てます。 以上より、 ・3333.33 が正解となります。 設問のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT TRUNC(10000 / 3, 2) FROM dual; 参考： ・ROUND関数は引数で与えられた数値を四捨五入します。 使用法は以下の通りです。 ROUND(数値 [, n]) 数値：四捨五入をする数値 n：小数点以下n桁に丸める 例) n=1 小数点2桁目で四捨五入され、小数点以下1桁に丸められる n=2 小数点3桁目で四捨五入され、小数点以下2桁に丸められる 2番目の引数は省略可能です。省略された場合は整数値に丸められます。 また、2番目の引数には負の値を指定することもできます。負の値が指定された場合は次のようになります。 例) n=-1 一の位で四捨五入される n=-2 十の位で四捨五入される n=-3 百の位で四捨五入される 例) ROUND関数の使...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions221.htm#i79729

### 問題ID 26454 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26454?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL関数の実行結果として正しいものはどれですか。 MOD(128, 30)
- 解説要約: MOD関数は引数で与えられた数値の除算の余りを返します。 以上より、 ・8 が正解となります。 商（割り算の結果）では無く、余りを返すので注意しましょう。商は算術演算子の「/」で求めます。 設問のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT MOD(128, 30) FROM dual; 参考： ・ROUND関数は引数で与えられた数値を四捨五入します。 使用法は以下の通りです。 ROUND(数値 [, n]) 数値：四捨五入をする数値 n：小数点以下n桁に丸める 例) n=1 小数点2桁目で四捨五入され、小数点以下1桁に丸められる n=2 小数点3桁目で四捨五入され、小数点以下2桁に丸められる 2番目の引数は省略可能です。省略された場合は整数値に丸められます。 また、2番目の引数には負の値を指定することもできます。負の値が指定された場合は次のようになります。 例) n=-1 一の位で四捨五入される n=-2 十の位で四捨五入される n=-3 百の位で四捨五入される 例) ROUND関数の使用例 SQLを表示 SELECT ROUND(12345.6789), ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions101.htm#i77996

### 問題ID 26455 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26455?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: SQL関数の結果として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 選択肢のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT ROUND(1234.56789,-3), ROUND(9876.54321,-3) FROM dual; SQLを表示 SELECT TRUNC(1234.56789,3), TRUNC(9876.54321,2) FROM dual; SQLを表示 SELECT MOD(18, 5), MOD(25, 8) FROM dual; 以上より、 ・ROUND(9876.54321, -3)の結果は10000である ・TRUNC(1234.56789, 3)の結果は1234.567である ・MOD(25, 8)の結果は1である が正解となります。 参考： ・ROUND関数は引数で与えられた数値を四捨五入します。 使用法は以下の通りです。 ROUND(数値 [, n]) 数値：四捨五入をする数値 n：小数点以下n桁に丸める 例) n=1 小数点2桁目で四捨五入され、小数点以下1桁に丸められる n=2 小数点3桁目で四捨五入され、小数点以下2桁に丸められる 2番目の引数は省略可能です。省略された場合は整数値に丸め...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions155.htm#i78633
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions221.htm#i79729
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions101.htm#i77996

### 問題ID 26456 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26456?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次の問い合わせを確認して下さい。 SELECT TRUNC(123.456789, MOD(102, ROUND(23.456, -1))) FROM dual; 結果はどうなりますか。
- 解説要約: 単一行関数のネストレベルには制限ありません。関数がネストしている場合は、一番内側の関数から実行されます。 設問では、まず四捨五入のROUND(23.456, -1)が実施され、結果は20になります。次に余りを求めるMOD(102, 20)が実施され、結果は2になります。最後に切り捨てのTRUNC(123.456789, 2)が実施され、結果は123.45になります。 以上より、 ・123.45 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TRUNC(123.456789, MOD(102, ROUND(23.456, -1))) FROM dual; 参考： ・ROUND関数は引数で与えられた数値を四捨五入します。 使用法は以下の通りです。 ROUND(数値 [, n]) 数値：四捨五入をする数値 n：小数点以下n桁に丸める 例) n=1 小数点2桁目で四捨五入され、小数点以下1桁に丸められる n=2 小数点3桁目で四捨五入され、小数点以下2桁に丸められる 2番目の引数は省略可能です。省略された場合は整数値に丸められます。 また、2番...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions155.htm#i78633
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions221.htm#i79729
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions101.htm#i77996

### 問題ID 26457 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26457?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 「mp3player」という商品名の商品を検索したいのですが、商品名が大文字/小文字のどちらでテーブルに格納されているか分かりません。 WHERE句に指定する条件として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: UPPER関数は引数で渡された文字列を大文字に変換して返し、LOWER関数は小文字に変換して返します。 ですので、UPPER関数、LOWER関数をWHERE句条件で使用する場合は、 ・UPPER関数 = 大文字の文字列 ・LOWER関数 = 小文字の文字列 のように指定しなければ行が検索されません。 以上より、 ・WHERE UPPER(prod_name) = 'MP3PLAYER' ・WHERE LOWER(prod_name) = 'mp3player' が正解となります。 参考： UPPER関数とLOWER関数は、単一行関数のうちの文字関数に分類されます。 ・UPPER関数は引数で渡された文字列を大文字に変換して返します。 UPPER(文字列) ・LOWER関数は引数で渡された文字列を小文字に変換して返します。 LOWER(文字列) 例) UPPER関数とLOWER関数の使用例 SQLを表示 SELECT UPPER('mp3player'), LOWER('MP3PLAYER') FROM dual; その他、主な文字関数には次のものがあります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions226.htm#i90176
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions094.htm#i104382

### 問題ID 26458 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26458?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: SQL関数の結果として正しいものはどれですか。 INITCAP('merry x''mas')
- 解説要約: INITCAP関数は、引数で指定された文字列中の単語の先頭文字を大文字、それ以外を小文字で返す関数です。 文字列「merry x'mas」はスペースと「'」が単語の区切りとして認識されるので、「Merry X'Mas」が返されます。 以上より、 ・Merry X'Mas が正解となります。 設問のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT INITCAP('merry x''mas') FROM dual; 参考： INITCAP関数は、単一行関数のうちの文字関数に分類されます。 引数で指定された文字列中の単語の先頭文字を大文字、それ以外を小文字で返します。 使用法は以下の通りです。 INITCAP(文字列) 文字列中の単語の区切りはスペースの他 ,(カンマ)や -(ハイフン)などの記号も単語の区切りとして認識されます。 その他、主な文字関数には次のものがあります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions074.htm#i77574

### 問題ID 26459 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26459?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL文の結果と同じ結果となるSQL文はどれですか。 SELECT 'My name is ' || employee_name FROM employees;
- 解説要約: 文字列を連結する場合、連結演算子||で連結する方法のほか、CONCAT関数で連結することもできます。 以上より、 ・SELECT CONCAT('My name is ', employee_name) FROM employees; が正解となります。 設問と正解のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT 'My name is ' || employee_name FROM employees; SQLを表示 SELECT CONCAT('My name is ', employee_name) FROM employees; なお「CONNECT」「CONTACT」という関数はありません。 参考： CONCAT関数は、単一行関数のうちの文字関数に分類されます。 引数で指定された2つの文字列を連結して返します。 使用法は以下の通りです。 CONCAT(文字列1, 文字列2) CONCAT関数は連結演算子||で文字列を連結した場合と同じ結果を返します。 その他、主な文字関数には次のものがあります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions033.htm#i77004
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/operators003.htm#i997789

### 問題ID 26460 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26460?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL関数の実行結果として正しいものを1つ選択して下さい。 LENGTH('Oracle Web問題集')
- 解説要約: LENGTH関数は引数で指定された文字列の長さを返す関数です。 "Oracle Web問題集"のように文字列に全角文字やスペースが含まれている場合、全角文字やスペースも1文字としてカウントされます。 以上より、 ・13 が正解となります。 設問のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT LENGTH('Oracle Web問題集') FROM dual; 参考： LENGTH関数は、単一行関数のうちの文字関数に分類されます。 引数で指定された文字列の長さを返します。 使用法は以下の通りです。 LENGTH(文字列) LENGTH関数では、全角文字やスペース、記号も1文字としてカウントしますので注意しましょう。 その他、主な文字関数には次のものがあります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions088.htm#i77725

### 問題ID 26461 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26461?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 文字列の先頭にあるスペースだけを削除するにはどのSQL関数を使用しますか。
- 解説要約: TRIM関数は、引数で指定された文字列の前後にある削除文字を取り除いた文字列を返す関数です。 設問では先頭のスペースを削除するので、削除位置に"LEADING"を指定します。また、スペースを削除する場合は削除文字の指定は必要としません。 以上より、 ・TRIM(LEADING FROM ' Oracle Master Web問題集 ') が正解となります。 正解のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT TRIM(LEADING FROM ' Oracle Master Web問題集 ') FROM dual; その他の選択肢については以下のとおりです。 ・TRIM(' Oracle Master Web問題集 ') SQLを表示 SELECT TRIM(' Oracle Master Web問題集 ') FROM dual; ・TRIM(BOTH FROM ' Oracle Master Web問題集 ') SQLを表示 SELECT TRIM(BOTH FROM ' Oracle Master Web問題集 ') FROM dual; ・TRIM(TR...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions219.htm#i79689

### 問題ID 26462 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26462?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL関数の実行結果として正しいものを1つ選択して下さい。 REPLACE('Oracle Master', 'Master', 'Database')
- 解説要約: REPLACE関数は、一つ目の引数で指定された文字列の中から、二つ目の引数の「変更前文字列」を検索し、それを三つ目の引数の「変更後文字列」に置換した文字列を返す関数です。 設問では、文字列"Oracle Master"のうち、"Master"を"Database"に変更するので、"Oracle Database"が返されます。 以上より、 ・Oracle Database が正解となります。 設問のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT REPLACE('Oracle Master', 'Master', 'Database') FROM dual; 参考： REPLACE関数は、単一行関数のうちの文字関数に分類されます。 一つ目の引数で指定された文字列の中から、二つ目の引数の「変更前文字列」を検索し、それを三つ目の引数の「変更後文字列」に置換した文字列を返す関数です。 使用法は以下の通りです。 REPLACE(文字列, 変更前文字列[, 変更後文字列]) 変更後文字列が省略された場合は、文字列から変更前文字列を削除した文字列が返されます。 その他、主な...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions153.htm#i78608

### 問題ID 26463 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26463?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 実行結果に"Oracle"が表示されるのはどの問い合わせですか(該当するものを全て選択して下さい)。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT SUBSTR('Oracle Master', 1, 6) FROM dual; SUBSTR関数で文字列"Oracle Master"の1文字目から6文字分の文字列を返すので、実行結果は"Oracle"となります。 ・SELECT TRIM(REPLACE('Oracle Master', 'Master')) FROM dual; REPLACE関数で文字列"Oracle Master"から"Master"が削除され"Oracle "となります。その後、TRIM関数で前後のスペースが取り除かれるので、実行結果は"Oracle"となります。 ・SELECT INITCAP('oracle') FROM dual; INITCAP関数は単語の1文字目を大文字、2文字目以降を小文字で出力するので、実行結果は"Oracle"となります。 ・SELECT TRIM(RPAD('Oracle Master', 7, ' ')) FROM dual; RPAD関数で長さが7文字の文字列が返されるので"Oracle "となります。その後、TRI...
- 参考URL: なし

### 問題ID 26464 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26464?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 苗字が「佐藤」で始まる従業員を検索するには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。
- 解説要約: SUBSTR関数は引数で指定された文字列の部分文字列を返す関数、INSTR関数は引数で指定した文字列中から検索文字列を検索し、その位置を数値で返す関数です。 苗字が「佐藤」で始まる従業員を検索するには、EMPLOYEE_NAME列の最初の2文字が「佐藤」であればよいので、SUBSTR関数で最初の2文字を取り出して比較するか、INSTR関数で1文字目から「佐藤」が出現するかを確認します。 以上より、 ・SELECT employee_id, employee_name FROM employees WHERE SUBSTR(employee_name, 1, 2) = '佐藤'; ・SELECT employee_id, employee_name FROM employees WHERE INSTR(employee_name, '佐藤') = 1; が正解となります。 なお、INSTR関数は検索文字列が文字列中に見つからなかった場合は0（ゼロ）を返します。 ですので、例えば「藤」という文字が含まれていない名前を検索したい場合は、以下のようにします。 WHERE INSTR(emplo...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions181.htm#i87066
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions080.htm#i77598

### 問題ID 26465 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26465?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: PROD表の構造を確認して下さい。 NAME列の値を右詰めで表示するには、どの問い合わせを実行しますか。
- 解説要約: LPAD関数は引数で指定された文字列が指定した長さの文字列になるように、左側に指定された埋め込み文字を付加した文字列を返す関数です。 設問では、従業員名を右詰めで表示したいので、従業員名の左側にスペースを埋め込み文字列の長さを統一することで、右詰めで表示することができます。 以上より、 ・SELECT LPAD(name, 20, ' ') FROM prod; が正解となります。 正解のSQL文の実行結果は次のようになります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions095.htm
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions159.htm

### 問題ID 26466 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26466?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 日付値の特徴として誤っている記述はどれですか(該当するものを全て選択して下さい)。
- 解説要約: 日付値には以下のような特徴があります。 ・日付値は世紀,年,月,日,時,分,秒を表す内部的な数値形式で格納されています。 ・日付値のデフォルトの表示書式は言語環境により異なりますが、変更することができます。 ・日付値に対して数値（日数）の加算,減算を行えます。また日付値-日付値で2つの日付値間の日数を求める事もできます。ただし、日付値+日付値の演算はできません。 以上より、 ・内部的には文字列で格納されている ・日付値の表示形式は言語環境により決まっており、変更することはできない が正解となります。 参考： 日付値には以下のような特徴があります。 ・日付値は世紀,年,月,日,時,分,秒を表す内部的な数値形式で格納されています。 ・日付値のデフォルトの表示書式は言語環境により異なりますが、変更することができます。 英語環境の場合のデフォルト値："DD-MON-RR"(日-月-年) 日本語環境の場合のデフォルト値："RR-MM-DD"(年-月-日) SQLを表示 SELECT SYSDATE FROM dual; ALTER SESSION SET nls_date_language = ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00202
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#BABGIGCJ
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i48042

### 問題ID 26467 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26467?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 現在の日時は1999年12月31日13時50分です。 次のSQL関数の実行結果として正しいものはどれですか。 ただし、日付の表示書式はRR-MM-DDとします。 ROUND(SYSDATE, 'DD')
- 解説要約: ROUND関数は、引数で指定された日付値を丸めて返します。 設問のROUND関数では書式に「DD」が指定されています。「DD」は指定した日付が正午より前なら当日の午前0時を、正午以降なら翌日の午前0字を返します。 以上より、 ・00-01-01 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions154.htm#i78665

### 問題ID 26468 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26468?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 日本からシンガポールのデータベースに接続しています。 次のSQL関数の実行結果として正しいものはどれですか。 SYSDATE
- 解説要約: SYSDATE関数は接続しているデータベースサーバーの現在の日時を返す関数です。 設問ではシンガポールのデータベースサーバーに接続しているので、SYSDATE関数の実行結果はシンガポールの現在の日時となります。 以上より、 ・現在のシンガポールの日時を表示する が正解となります。 参考： SYSDATE関数は、単一行関数のうちの日付関数に分類されます。 接続しているデータベースサーバーの現在の日時を返します。 使用法は以下の通りです。 SYSDATE SQLを表示 SELECT SYSDATE FROM dual; SYSDATE関数には引数はありません。 なお、接続先の現在時刻ではなく、ローカルマシンの現在時刻を表示したい場合には、CURRENT_DATE関数を使用します。 CURRENT_DATE SQLを表示 SELECT CURRENT_DATE FROM dual; 主な日付関数は次のとおりです。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions191.htm#i79216
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions044.htm#i999792

### 問題ID 26469 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26469?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次の関数の結果として正しいものを1つ選択して下さい。 ただし、日付書式はRR-MM-DDとします。 MONTHS_BETWEEN('12-02-29', '12-05-31')
- 解説要約: MONTHS_BETWEEN関数は、引数で指定された2つの日付間の月数を返す関数です。 MONTHS_BETWEEN(日付1, 日付2) 日付1が日付2よりも過去の日付の場合は、負の値を返します。 1ヶ月未満の値は小数で返されますが、日付1と日付2が、月の同じ日または月の最終日の場合、結果は常に整数になります。 設問では'12-02-29'のほうが過去の日付ですので、負の値が返されます。 また、'12-02-29'は2月の最終日(2012年はうるう年です)、'12-05-31'は5月の最終日ですので、整数が返されます。 以上より、 ・-3 が正解となります。 設問のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT MONTHS_BETWEEN('12-02-29', '12-05-31') FROM dual;
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions102.htm#i78039

### 問題ID 26470 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26470?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次の関数の結果として正しいものを1つ選択して下さい。 ただし、日付書式はRR-MM-DDとします。 ADD_MONTHS('11-04-30', -3)
- 解説要約: ADD_MONTHS関数は、引数で指定された日付のnヶ月後の日付を返す関数です。2番目の引数に負が指定された場合はnヶ月前の値を返します。 また、1番目の引数に月の最終日が指定された場合はnヶ月後(またはnヶ月前)の最終日が返されます。 以上より、 ・11-01-31 が正解となります。 設問では1番目の引数に"11-04-30"が指定されていますが、ADD_MONTHS関数の結果は"11-01-30"にはなりません。 1番目の引数に月の最終日が指定された場合は、nヶ月後(またはnヶ月前)の最終日が返されますので注意しましょう。 設問のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT ADD_MONTHS('11-04-30', -3) FROM dual; 参考： ADD_MONTHS関数は、単一行関数のうちの日付関数に分類されます。 引数で指定された日付のnヶ月後の日付を返します。 使用法は以下の通りです。 ADD_MONTHS(日付, n) nが正の値の場合は、nヶ月後の日付を、nが負の値の場合はnヶ月前の値を返します。 SQLを表示 SELECT ADD_...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions011.htm#i76717

### 問題ID 26471 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26471?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 明日以降で最初の月曜日を表示するSQL文として正しいものはどれですか(2つ選択してください)。 ただし、データベースの実行環境は日本語環境とし、日付の表示書式はRR-MM-DDとします。
- 解説要約: NEXT_DAY関数は引数で指定した日付の翌日以降に、指定した曜日になる最初の日付を返す関数です。 曜日の指定は言語環境で異なります。日本語環境の場合は、'月曜日'や省略形の'月'のように指定します。 また、曜日に1から7の数字を指定することも可能です。データベースのNLS_TERRITORYパラメータが「AMERICA」や「JAPAN」などの多くの地域では以下の対応になります。 1：日曜日、2：月曜日、3：火曜日、4：水曜日、5：木曜日、6：金曜日、7：土曜日 以上より、 ・SELECT NEXT_DAY(SYSDATE, '月曜日') FROM dual; ・SELECT NEXT_DAY(SYSDATE, 2) FROM dual; が正解です。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT NEXT_DAY(SYSDATE, 'MON') FROM dual; ・SELECT NEXT_DAY(SYSDATE, 'MONDAY') FROM dual; 英語環境での曜日指定なので、誤りです。 ・SELECT NEXT...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions106.htm#i78154
  - https://www.shift-the-oracle.com/sql/functions/next_day.html

### 問題ID 26472 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26472?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 現在の日時は2010年12月24日13時50分です。 次の関数の実行結果として、正しいものを1つ選択して下さい。 ただし、データベースの実行環境は英語環境とし、日付の表示書式はデフォルトとします。 LAST_DAY('14-FEB-12')
- 解説要約: LAST_DAY関数は、引数で指定された日付を含む月の最終日を返す関数です。 設問ではLAST_DAY関数の引数に「14-FEB-12」が指定されていますので、2012年2月29日を返します。 英語環境で、日付の表示書式のデフォルトは「DD-MON-RR」になりますので、「29-FEB-12」が返されます。 以上より、 ・29-FEB-12 が正解となります。 関数の引数に日付リテラルを指定する場合は、データベースの実行環境にあった日付の表示書式で記述しなければなりません。 デフォルトの表示書式は言語環境により異なります。 ・英語環境の場合のデフォルト値：DD-MON-RR(日-月-年) ・日本語環境の場合のデフォルト値：RR-MM-DD(年-月-日) 設問のLAST_DAY関数の実行結果は次のようになります。 ※日本語環境の場合は、事前に以下のSQL文を実行してセッションを英語環境に変更して下さい。 ALTER SESSION SET NLS_DATE_LANGUAGE = 'AMERICAN'; ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MON...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions084.htm#i83733

### 問題ID 26473 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26473?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 現在の日時は2010年12月25日14時40分です。 TRUNC関数の結果として正しいものはどれですか(該当するものを全て選択して下さい)。 ただし、日付の表示書式はRR-MM-DDとします。
- 解説要約: TRUNC関数は、引数で指定された日付値を切り捨てて返す関数です。 どの単位で切り捨てるのかは書式で指定します。指定できる主な書式は次のとおりです。 以上より、 ・TRUNC(SYSDATE, 'YEAR')の結果は"10-01-01"である ・TRUNC(SYSDATE, 'MONTH')の結果は"10-12-01"である ・TRUNC(SYSDATE, 'DD')の結果は"10-12-25"である が正解となります。 正解のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT TRUNC(SYSDATE, 'YEAR'), TRUNC(SYSDATE, 'MONTH'), TRUNC(SYSDATE, 'DD') FROM dual; その他の選択肢については以下のとおりです。 ・TRUNC(SYSDATE) TRUNC(SYSDATE, 'DD')と同義ですので、結果は"10-12-25"となります。 参考： 日付値を引数に指定するTRUNC関数は、単一行関数のうちの日付関数に分類されます。 引数で指定された日付値を切り捨てて返します。 使用法は以下の通りです。...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions220.htm#i79761

### 問題ID 26474 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26474?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: データ型の変換に関して正しい記述はどれですか(該当するものを全て選択して下さい)。
- 解説要約: データ型の変換には、暗黙的なデータ変換と明示的なデータ変換があります。 暗黙的なデータ変換はOracle Databaseが自動で行うデータ変換であるのに対し、明示的なデータ変換は変換関数を使用して行う変換です。 変換関数には主に次のものがありますが、数値を日付値に変換したり、日付値を数値に変換する関数はありません。 ・TO_CHAR：数値や日付値を文字列に変換する ・TO_DATE：文字列を日付値に変換する ・TO_NUMBER：文字列を数値に変換する 以上より、 ・TO_CHAR関数は数値または日付値を文字列に変換する ・日付値を数値に変換する関数はない が正解となります。 その他の選択肢については以下のとおりです。 ・TO_DATE関数は数値を日付値に変換する TO_DATE関数は文字列を日付値に変換するので、誤った記述です。 ・TO_NUMBER関数は文字列または日付値を数値に変換する TO_NUMBER関数は文字列を数値に変換するので、誤った記述です ・データ型を変換する場合は必ず変換関数で変換しなければならない 暗黙的なデータ変換によりデータ型が変換される場合もあるので、誤...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements002.htm#SQLRF00214

### 問題ID 26475 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26475?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMLOYEES表の構造を確認して下さい。 COMMISSION列を次の形式で表示するには、どの問い合わせを実行しますか。 例) ¥800,000 ただし、実行環境は日本語環境とします。
- 解説要約: TO_CHAR関数は数値を書式化した文字列に変換します。 COMMISSION列は最大7桁の数値ですが、設問の例が¥800,000となっていますので、数値が7桁未満の場合に先頭を0で埋めていないということがわかります。 また、¥記号を表示する場合は、ローカル通貨記号の"L"を指定します。 以上より、 ・SELECT employee_name, TO_CHAR(commission, 'L9,999,999') FROM employees; が正解となります。 正解のSQL文の実行すると次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT employee_name, TO_NUMBER(commission, 'L9,999,999') FROM employees; TO_NUMBER関数は文字列を数値に変換する関数ですので、エラーとなります。 ・SELECT employee_name, TO_CHAR(commission, 'L0,000,000') FROM employees; 数値書式の先頭に'0'を使用すると、数値の桁数が数値書式の桁数に...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions201.htm#i79330
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34570

### 問題ID 26476 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26476?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 HIREDATE列を次の形式で表示するには、どの問い合わせを実行しますか。 例) 2012年04月01日
- 解説要約: 通常、DATE型の値を表示させると、「2012-04-01」のように表示されますので、任意のフォーマットに従って表示させるにはTO_CHAR関数を使用します。 TO_CHAR関数の日付書式には日時書式要素の他、文字も含めることができますが、半角記号以外の文字は二重引用符(")で囲まなければなりません。 以上より、 ・SELECT employee_name, TO_CHAR(hiredate, 'YYYY"年"MM"月"DD"日"') FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT employee_name, TO_CHAR(hiredate, 'YYYY-MM-DD') FROM employees; "2012-04-01"の形式で表示されます。 ・SELECT employee_name, TO_CHAR(hiredate, 'YYYY年MM月DD日') FROM employees; ・日付書式の中に文字を埋め込むことはできないので、エラーとなる 日付書式中に文字を...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions200.htm#i1009324
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924

### 問題ID 26477 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26477?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: TO_DATE関数で文字列を日付値に変換します。 日付書式の指定方法として誤っているものはどれですか。
- 解説要約: TO_DATE関数の日付書式には日時書式要素の他、文字も含めることができますが、半角記号以外の文字は二重引用符(")で囲まなければなりません。 二重引用符(")で囲まれていない場合は、エラーとなります。 以上より、 TO_DATE('2012年5月21日', 'YYYY年MM月DD日') が正解となります。 正解のTO_DATE関数の実行結果は次のようになります。 SQLを表示 SELECT TO_DATE('2012年5月21日', 'YYYY年MM月DD日') FROM dual; その他の選択肢については次のとおりです。 ・TO_DATE('2012年5月21日', 'YYYY"年"MM"月"DD"日"') SQLを表示 SELECT TO_DATE('2012年5月21日', 'YYYY"年"MM"月"DD"日"') FROM dual; ・TO_DATE('2012年5月21日', 'YY"年"MM"月"DD"日"') SQLを表示 SELECT TO_DATE('2012年5月21日', 'YY"年"MM"月"DD"日"') FROM dual; ・TO_DATE('201...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions203.htm#SQLRF06132
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924

### 問題ID 26478 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26478?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: TO_NUMBER関数で文字列を数値に変換します。正しく変換されるものはどれですか。 ただし、実行環境は日本語環境とします。
- 解説要約: TO_NUMBER関数は文字列を数値へ変換します。 変換する文字列には日本語環境でデフォルトの通貨記号である「¥」が含まれているため、数値書式にはローカル通貨記号の"L"を指定します。 また、3桁目と4桁目の間にカンマ(,)がありますので、数値書式にもカンマ(,)を指定しなければなりません。 以上より、 ・TO_NUMBER('¥500,000', 'L999,999') が正解となります。 正解のTO_NUMBER関数の実行結果は次のようになります。 SQLを表示 SELECT TO_NUMBER('¥500,000', 'L999,999') FROM dual; その他の選択肢については次のとおりです。 ・TO_NUMBER('$500,000', 'L999,999') 文字列の通貨記号と数値書式の通貨記号が異なるため、エラーとなります。 SQLを表示 SELECT TO_NUMBER('$500,000', 'L999,999') FROM dual; ・TO_NUMBER('¥500,000', '999,999') 文字列には通貨記号が含まれていますが、数値書式に通貨記号...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions211.htm#SQLRF06140
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34570

### 問題ID 26479 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26479?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文でエラーとなるのはどれですか。
- 解説要約: NVL関数の第2引数には、第1引数と同じデータ型の値を指定しなければなりません。異なるデータ型の値を指定するとエラーとなります。 選択肢のSQL文のうち、 ・SELECT NVL(manager_id, 'none') FROM employees; は、MANAGER_ID列の値がNULLだった場合に文字列「none」に変換しようとしていますが、MANAGER_ID列はNUMBER型の列であるためエラーとなります。 以上より、 ・SELECT NVL(manager_id, 'none') FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT NVL(salary, 0) FROM employees; ・SELECT employee_name, NVL(yomi, 'none') FROM employees; NVL関数の第1引数と第2引数で同じデータ型の値が指定されているため、エラーになりません。 ・SELECT employee_name, NVL(yomi, 0) FR...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL.html#GUID-3AB61E54-9201-4D6A-B48A-79F4C4A034B2

### 問題ID 26480 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26480?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: DEPARTMENTS表の構造とデータを確認して下さい。 次のSQLの文の実行し、各部署のNEW_MANAGERに表示される値の組合せとして、正しいものはどれですか。 SELECT department_name, DECODE(department_id, 1, 1013 , 2, 1014 , 3, 1015 , 4, 1016 , manager_id) new_manager FROM departments;
- 解説要約: DECODE関数は、SQL文の中で分岐処理を行うための関数です。 第1引数に指定された式の値と条件を比較し、最初に合致した条件に対応した値を返します。 設問のSQL文では、第1引数にDEPARTMENT_ID列が、条件には"1", "2", "3", "4"が指定されています。 DEPARTMENTS表はDEPARTMENT_IDの値が1~5の5行が登録されていますが、DECODE関数の条件に"5"は指定されていません。したがって、DEPARTMENT_ID列の値が"5"の場合は、デフォルト値として指定されているMANAGER_ID列の値を返します。 以上より、 ・C が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_name, DECODE(department_id, 1, 1013 , 2, 1014 , 3, 1015 , 4, 1016 , manager_id) new_manager FROM departments;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions049.htm#SQLRF00631

### 問題ID 26481 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26481?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 実行結果が"12-04-01"と表示されるのはどの問い合わせですか(該当するものを全て選択して下さい)。 ただし、データベースの実行環境は日本語環境とし、日付書式はRR-MM-DDとします。 ※ 2012年3月26日は月曜日です。
- 解説要約: TO_DATE関数は文字リテラルを日付値に変換します。引数に時刻が指定されていない場合は午前0時0分0秒に設定されます。 選択肢を1つずつ確認してみましょう。 ・SELECT ROUND(TO_DATE('12-04-10'), 'MONTH') FROM dual; ROUND関数の書式に"MONTH"が指定されているので、丸めて当月の1日が返されます。したがって実行結果は"12-04-01"となります。 ・SELECT LAST_DAY('12-03-01') + 1 FROM dual; LAST_DAY関数で当月の最終日を求めると"12-03-31"となります。その後で1日を加算しているので、翌日の"12-04-01"が返されます。 ・SELECT NEXT_DAY('12-03-26', '日') FROM dual; "12-03-26"は月曜日です。NEXT_DAY関数で翌日以降で最初の日曜日が返されます。したがって実行結果は"12-04-01"となります。 ・SELECT ROUND(TO_DATE('12-04-10'), 'DD') FROM dual; TO_DA...
- 参考URL: なし

### 問題ID 26482 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26482?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 日付値の演算について正しいものはどれですか(該当するものを全て選択して下さい)。 ただし、日付の表示書式はRR-MM-DDとします。
- 解説要約: 日付値に対し数値を加算したり減算した場合は、数値を日数として加算したり減算したりします。 以上より、 ・TO_DATE('10-09-27') + 3の結果は"10-09-30"である ・TO_DATE('11-01-01') - 3の結果は"10-12-29"である が正解となります。 なお、TO_DATE関数は文字リテラルを日付値に変換します。引数に時刻が指定されていない場合は午前0時0分0秒に設定されます。 正解の演算を実行すると次のようになります。 SQLを表示 SELECT TO_DATE('10-09-27') + 3 FROM dual; SQLを表示 SELECT TO_DATE('11-01-01') - 3 FROM dual; その他の選択肢については以下のとおりです。 ・TO_DATE('10-09-27') + 3の結果は"10-12-27"である 日数が加算されるので、'2010-09-30'となります。 ・TO_DATE('11-02-08') + 100の結果はエラーとなる ・TO_DATE('11-01-01') - 3の結果はエラーとなる 日付値に対...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i48042

### 問題ID 26483 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26483?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表に登録されている従業員のうち、2003年4月1日から2012年4月1日の間に入社した従業員を、入社日が新しい順で表示し、さらに入社日が同じ従業員同士は従業員番号が小さい順で表示するには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。 ただし、日付書式は「RR-MM-DD」とします。
- 解説要約: 日付の範囲を指定してデータを検索するには比較演算子の「>=（以上）」と「<=（以下）」で範囲を指定するか、BETWEEN演算子を使用します。 また、SELECT文の実行結果をソートして表示する場合は、ORDER BY句を指定します。ORDER BY句に複数の項目を指定した場合は、指定した順番でソート処理が行われます。また、項目ごとに昇順、降順どちらでソートするかを指定することができます。 ORDER BY句で指定できる項目は列名の他、SELECT句に指定されている項目の順番（数値）などがあります。 以上より、 ・SELECT employee_id, employee_name, hiredate FROM employees WHERE hiredate >= '03-04-01' AND hiredate <= '12-04-01' ORDER BY 3 DESC, 1; ・SELECT employee_id, employee_name, hiredate FROM employees WHERE hiredate BETWEEN '03-04-01' AND '12-04-0...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Sorting-Query-Results.html
  - https://docs.oracle.com/cd/F19136_01/sqlrf/BETWEEN-Condition.html

### 問題ID 26484 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26484?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次の文字列を数値に変換し12倍した値を、最初の文字列と同じ形式で表示するには、どのSQL文を実行しますか。 $1,234.56
- 解説要約: 文字列を数値に変換するにはTO_NUMBER関数を、数値を書式化した文字列に変換するにはTO_CHAR関数を使用します。 設問では値を12倍にしなければなりませんので、TO_NUMBER関数で文字列を数値に変換後、12倍にする演算を行います。 以上より、 ・SELECT TO_CHAR(TO_NUMBER('$1,234.56', '$9G999D99')*12, '$999G999D99') FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT TO_CHAR(TO_NUMBER('$1,234.56', '$9G999D99'), '$999G999D99')*12 FROM dual; TO_CHAR関数は文字列を返します。TO_CHAR関数の結果に対して*12の演算を行なっているためエラーとなります。 ・SELECT TO_NUMBER(TO_NUMBER('$1,234.56', '$9G999D99')*12, '$99G999D99') FROM dual; TO_NUMBER関...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions201.htm#SQLRF06130
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions203.htm#SQLRF06132

### 問題ID 26485 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26485?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: グループ関数に関する説明で正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: グループ関数は、複数行のデータをグループ化して、集計処理を行った結果をグループ毎に1つだけ返す関数で、SELECT句、HAVING句、ORDER BY句で指定することができます。 集計するデータにNULL値が含まれている場合は、COUNT(*)を除き集計時に無視されます。またグループ関数では2レベルまでネストが可能です。 DISTINCTオプションを指定すると、重複したデータは1度だけ処理されます。 以上より、 ・行のグループごとに1つの結果を返す ・グループ関数にDISTINCTをオプションとして指定することができる が正解となります。 その他の選択肢については以下のとおりです。 ・グループ関数はネストできない グループ関数は2レベルまでネストすることができます。 ・グループ関数はNULL値は0として集計する COUNT関数に*(アスタリスク)を指定した場合を除き、NULL値は集計時に無視されます。 ・グループ関数はSQL文の全ての句で指定することができる グループ関数はSELECT句、HAVING句、ORDER BY句で指定することができます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203

### 問題ID 26486 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26486?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: COUNT関数に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: COUNT関数は取り出されたデータの件数を返す関数です。 引数には列名や数値型、文字列型、日付型の値を返す式の他、*(アスタリスク)を指定できます。 また、重複した値がある場合の処理方法をDISTINCT/ALLオプションで指定できます。 以上より、 ・COUNT(DISTINCT salary)は重複した値やNULL値を除いたデータの件数を返す ・COUNT(*)はNULL値も含めた全てのデータ件数を返す ・引数に日付型の列を指定できる が正解となります。 その他の選択肢については以下のとおりです。 ・COUNT(ALL salary)はNULL値も含めた全てのデータの件数を返す COUNT関数の引数に列名や式を指定した場合、NULL値はカウントされません。 ・COUNT(DISTINCT *)とCOUNT(DISTINCT salary)の結果は同じである *(アスタリスク)にDISTINCTオプションを指定することはできません。 また、COUNT(*)はNULL値もカウントされるのに対し、COUNT(DISTINCT salary)はNULL値がカウントされませんので、異なる結果...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions039.htm#i82697

### 問題ID 26487 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26487?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 SALARY列がNULLである従業員の人数を表示するには、どのSQL文を実行しますか。
- 解説要約: COUNT関数でNULL値を含むデータ件数を返すのは、引数に*(アスタリスク)を指定した場合のみです。 したがって、COUNT(*)からNULL値を含まない件数であるCOUNT(salary)を減算すれば良いことになります。 以上より、 ・SELECT COUNT(*) - COUNT(salary) FROM employees; が正解となります。 これは以下のSQL文と同じ結果になります。 SELECT COUNT(*) FROM employees WHERE salary IS NULL; 選択肢のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT COUNT(*) FROM employees; NULL値を含む全てのデータ件数を返します。 ・SELECT COUNT(DISTINCT salary) FROM employees; ・SELECT COUNT(*) - COUNT(DISTINCT salary) FROM employees; COUNT(DISTINCT salary)は、NULL値と重複した値を除いた...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions039.htm#i82697

### 問題ID 26488 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26488?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 部署ごとに最も年収の多い従業員の年収を表示するSQL文として、正しいものはどれですか。 ただし、部署はDEPARTMENT_ID列の値とし、年収はSALARY列を12倍したものにCOMMISSION列を加算したものとします。
- 解説要約: SELECT文にGROUP BY句を指定すると、関連のある行をグループ化することができます。 部署ごとに最も多い年収を表示するには、同じ部署の行をGROUP BY句でグループ化し、MAX関数で年収の最大値を表示させます。 以上より、 ・SELECT MAX(salary * 12 + commission) total FROM employees GROUP BY department_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT MAX(salary * 12 + commission) FROM employees; GROUP BY句でグループ化されていないため、全従業員のなかで最も多い年収が表示されます。 ・SELECT MAX(salary * 12 + commission) FROM employees GROUP BY employee_id; EMPLOYEE_IDでグループ化しているため、部署ごとの表示にはなりません。 ・SELECT salary * 12 + commiss...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions098.htm#i89072

### 問題ID 26489 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26489?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 全社員の平均月収を求めるにはどのSQLの文を実行しますか(該当するものを全て選択して下さい)。 ただし、月収はSALARY列の値とし、SALARY列がNULL値である場合は月収を0として扱うこととします。
- 解説要約: 平均月収を求めるためにはAVG関数を使用しますが、グループ関数はNULL値を無視して集計してしまうので、AVG関数の引数にSALARY列をそのまま指定してしまうとNULL値以外の件数で割った平均が求められます。 全従業員の平均値を求めるには、 ・SALARY列のNULL値を0に変換してからAVG関数で集計する ・AVG関数を使用せずに、SALARY列の和を全従業員数で割る などの方法で求めなければなりません。 NULL値を0に変換するにはNVL関数などを使用します。 以上より、 ・SELECT SUM(salary) / COUNT(*) FROM employees; ・SELECT AVG(NVL(salary, 0)) FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT AVG(salary) FROM employees; AVG関数はNULL値を無視して集計するため、全従業員の平均にはなりません。 ・SELECT NVL(AVG(salary), 0) FROM empl...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions018.htm#i82074

### 問題ID 26490 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26490?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: SELECT文で指定する句の順番として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: SELECT文に指定する句の順序は、 1.SELECT句 2.FROM句 3.WHERE句 4.GROUP BY句 5.HAVING句 6.ORDER BY句 です。ただし、GROUP BY句とHAVING句は入れ替えができます。 以上より、 ・1.SELECT 2.FROM 3.WHERE 4.HAVING 5.GROUP BY 6.ORDER BY ・1.SELECT 2.FROM 3.WHERE 4.GROUP BY 5.HAVING 6.ORDER BY が正解となります。
- 参考URL: なし

### 問題ID 26491 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26491?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: GROUP BY句に関する説明として、正しいものはどれですか。
- 解説要約: SELECT文にGROUP BY句を指定すると、関連のある行をグループ化できますが、GROUP BY句を指定する場合にはいくつかの要件を満たす必要があります。 ・GROUP BY句には1つ以上の列を指定する ・GROUP BY句に列別名を指定することはできない ・GROUP BY句を指定したSELECT文のSELECT句には、GROUP BY句で指定した列、もしくはグループ関数のみ指定できる （select句に指定したグループ関数以外の列はすべてgroup by句で指定する必要がある） ・GROUP BY句とORDER BY句を併用する場合、ORDER BY句にはGROUP BY句で指定した列、もしくはグループ関数のみ指定できます （グループ化されている列の値を、グループ化されていない列の値を基準に並べ替える事はできない為） 以上より、 ・GROUP BY句を指定した場合、SELECT句にはGROUP BY句で指定した列とグループ関数のみ指定できる が正解となります。 これは、グループ化されている列の値と、グループ化されていない列の値を同時に表示する事はできない為です。 その他の選択肢...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038

### 問題ID 26492 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26492?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせを実行したところエラーとなりました。エラーの原因はどれですか。 SELECT MAX(MIN(AVG(salary))) "Sal" FROM employees GROUP BY department_id, job_id;
- 解説要約: 単一行関数が任意のレベルにネストできるのに対し、グループ関数は2レベルまでしかネストできません。しかも、GROUP BY句を指定した場合に限ります。 設問のSQL文ではGROUP BY句がありますが、MAX(MIN(AVG(salary)))と3レベルのネストとなっているためエラーとなります。 以上より、 ・グループ関数は2レベルまでしかネストできないため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT MAX(MIN(AVG(salary))) "Sal" FROM employees GROUP BY department_id, job_id; その他の選択肢については以下のとおりです。 ・GROUP BY句で指定した列が、SELECT句で指定されていないため SELECT文にGROUP BY句が指定されている場合は、SELECT句にはGROUP BY句で指定された列かグループ関数しか指定できませんが、必ず指定する必要はありません。 ・GROUP BY句に2つ以上の列を指定しているため GROUP BY句には1つ以上の任意の数の列を...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203

### 問題ID 26493 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26493?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせの実行結果について、正しい記述はどれですか。 SELECT department_id, job_id, COUNT(*), MIN(salary) FROM employees WHERE department_id IN (1, 2, 3, 4) GROUP BY department_id, job_id HAVING AVG(salary) >= 250000;
- 解説要約: SELECT文にWHERE句、GROUP BY句、HAVING句を同時に指定する場合は、WHERE句、GROUP BY句、HAVING句、またはWHERE句、HAVING句、GROUP BY句の順に指定します。 また、WHERE句、HAVING句には行を取り出す条件を指定しますが、WHERE句にグループ関数を指定できないのに対し、HAVING句ではグループ関数を指定することができます。 以上より、 ・正常に実行される が正解となります。 設問のSQL文の実行結果は次のようになります。 平均給与が250000以上のグループの情報を表示しています。 SQLを表示 SELECT department_id, job_id, COUNT(*), MIN(salary) FROM employees WHERE department_id IN (1, 2, 3, 4) GROUP BY department_id, job_id HAVING AVG(salary) >= 250000; その他の選択肢については次のとおりです。 ・1つのSELECT文でWHERE句とHAVING句は併用できな...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26494 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26494?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 部署ごとの従業員人数を表示するにはどのSQL文を実行しますか。 ただし、部署はDEPARTMENT_ID列の値とします。
- 解説要約: SELECT文にGROUP BY句を指定すると、関連のある行をグループ化することができます。 部署ごとの従業員人数を表示するには、同じ部署の行をGROUP BY句でグループ化し、COUNT関数で行の数をカウントします。 以上より、 ・SELECT department_id, COUNT(*) FROM employees GROUP BY department_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT COUNT(department_id) FROM employees; GROUP BY句でグループ化されていないため、全従業員数がカウントされます。 ・SELECT department_id, COUNT(*) FROM employees; DEPARTMENT_ID列がGROUP BY句で指定されていないため、エラーとなります。 ・SELECT department_id, COUNT(DISTINCT department_id) FROM employees GROUP BY de...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions039.htm#i82697

### 問題ID 26495 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26495?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 年収の最高額を表示するには、どのSQL文を実行しますか。 ただし、年収はSALARY列の値を12倍したものにCOMMISSION列の値を加算したものとします。 また、SALARY列またはCOMMISSION列のいずれかがNULL値である従業員については対象外とします。
- 解説要約: MAX関数は指定された列や式の値の最大値を返す関数です。 年収は(salary * 12 + commission)で求めることができるので、年収の最高額を求めるには、MAX関数の引数に(salary * 12 + commission)を指定します。 なお、SALARY列またはCOMMISSION列のいずれかがNULL値である場合は(salary * 12 + commission)の結果がNULL値となり、MAX関数の集計対象外となります。 以上より、 ・SELECT MAX(salary * 12 + commission) FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT MAX(salary) * 12 + MAX(commission) FROM employees; SALARY列の最大値 * 12 + COMMISSION列の最大値が返されます。 ・SELECT MIN(salary) FROM employees; MIN関数は最小値を求める関数です。SALAR...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions098.htm#i89072
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions100.htm#i1280029

### 問題ID 26496 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26496?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 表の結合について、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 表の結合を行う際に、表接頭辞として「表名」または「表別名」を指定すると、メモリの使用量が節約でき、パフォーマンスの向上につながります。ただし、同じ表の表接頭辞として「表名」と「表別名」を混在することはできません。 また、結合条件にBETWEEN句を指定して結合することができます(等号(=)以外の演算子を使用した結合を「非等価結合」といいます)。 以上より、 ・表接頭辞を使用するとパフォーマンスが向上する ・結合条件にBETWEEN演算子を使用することができる が正解となります。 その他の選択肢については次のとおりです。 ・3つ以上の表は結合できない 3つ以上の表も結合することができます。 ・必ず他の表と結合する 同じ表を2つの表に見立てて結合することもできます(自己結合といいます)。 ・1つのSQL文で、同一の表に対する表接頭辞として表名と表別名を混在して記述できる 表別名を定義した表に対し、元の表名を表接頭辞として指定することはできません。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#i2054012

### 問題ID 26497 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26497?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 自然結合の説明として正しいものはどれですか(該当するものを3つ選択して下さい)。
- 解説要約: 自然結合では、2つの表に共通して存在する同名で同じデータ型(または互換性のあるデータ型)の列に基づいて、表を結合します。 そのため、結合条件を指定する必要はありません。また、2つの表に同名で同じデータ型の列が複数ある場合はその組合せで結合します。 なお、自然結合の結合列には表接頭辞を使用することができません。表接頭辞を指定するとエラーとなります。 以上より、 ・2つの表に共通して存在する列に基づいて結合を行う ・同名かつ同じデータ型の列で結合する場合に使用する ・結合列に表接頭辞を使用することはできない が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/SELECT.html#GUID-CFA006CA-6FF1-4972-821E-6996142A51C6__BABHGCAE
  - https://atmarkit.itmedia.co.jp/ait/articles/1203/22/news164.html

### 問題ID 26498 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26498?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: USING句の説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: USING句を使用した結合は、等価結合の1つです。結合する表に共通する列が複数ある場合に、特定の列だけを結合列として指定することができます。 USING句を指定した結合では、結合列に表接頭辞を使用することはできません。また、1つの結合でNATURAL JOIN句と同時に指定することもできません。 なおUSING句は、1つのSQL文で2つの表を結合する場合だけではなく、3つ以上の表を結合する場合にも使用できます。このような複数の結合においては、USING句を使用した結合はNATURAL JOIN句など他の結合方法と混在することができます。 以上より、 ・1つの結合でNATURAL JOIN句と一緒に指定できない ・共通する列が複数ある場合に、特定の列だけを結合列に指定できる が正解となります。 その他の選択肢については次のとおりです。 ・結合列に表接頭辞を使用できる USINGを使用した結合では、結合列に表接頭辞を使用することはできません。 ・他の結合と組み合わせて3つ以上の表を結合できない 1つのSQL文内で、USING句を使用した結合と他の結合(USING句も含む)を組み合わせて、3...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26499 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26499?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: ON句の説明として誤っているものはどれですか。
- 解説要約: ON句を使用した結合では、自然結合やUSING句での結合とは異なり、列名が違っていても結合列として指定することができます。 以上より、 ・同じ名前の列のみを結合することができる が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26500 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26500?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: USING句とON句について正しいものはどれですか。
- 解説要約: USING句とON句の違いは次のとおりです。 ・USING句は等価結合にのみ、ON句は等価結合と非等価結合に使用できる ・USING句は同名の列のみ、ON句は異なる列名の列も結合列に使用できる ・USING句では結合列に表接頭辞を使用できないが、ON句では結合列に表接頭辞を必ず使用する 以上より、 ・ON句では列名の異なる列を結合列に使用することができる が正解となります。 その他の選択肢については次のとおりです。 ・どちらも等価結合、非等価結合のどちらにも使用できる ON句は等価結合、非等価結合の両方で使用できますが、USING句は等価結合の場合しか使用できません。 ・どちらも結合列には必ず表接頭辞を使用する USING句では結合列に表接頭辞を使用するとエラーとなります。ON句では結合列に表接頭辞を使用しないとエラーとなります。 ・USING句では列名の異なる列を結合列に使用することができる USING句では結合する2つの表で同じ列名の列を結合列に使用できます。異なる列名の列を結合列にする場合はON句で指定します。 参考： USING句を使用した結合とON句を使用した結合の違いを以下...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26501 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26501?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表、EMPLOYEES表の構造を確認して下さい。 次のSQL文を実行するとどうなりますか。 SELECT d.department_id, d.department_name, e.employee_id,e.employee_name FROM departments d, employees e WHERE d.department_id = e.department_id AND salary BETWEEN 200000 AND 450000;
- 解説要約: 設問のSQL文はOracle独自の結合構文を用いたSQL文です。 Oracle独自の結合構文のルールに従って記述されているので、JOINやON,USINGなどのキーワードがありませんが、正常に実行することができます。 以上より、 ・正常に実行される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT d.department_id, d.department_name, e.employee_id,e.employee_name FROM departments d, employees e WHERE d.department_id = e.department_id AND salary BETWEEN 200000 AND 450000; その他の選択肢については次のとおりです。 ・結合条件をWHERE句に記述しているためエラーとなる Oracle独自の結合構文では、結合する表名は,(カンマ)で区切ってFROM句に指定し、結合条件はWHERE句に指定します。 ・結合条件以外の条件を指定しているのでエラーとなる 1つのSQL文で結合条件と...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF30046
  - https://atmarkit.itmedia.co.jp/ait/articles/1204/23/news132.html

### 問題ID 26503 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26503?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表、EMPLOYEES表の構造を確認して下さい。 次の等価結合のうち、正しく実行されるものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 自然結合やUSING句を使用した結合では、結合列に表接頭辞を使用することはできませんが、ON句を使用した結合ではSELECT句やWHERE句に2つの表の共通列を指定する場合、表接頭辞で修飾しなければなりません。 以上より、 ・SELECT department_id, d.department_name, e.employee_name FROM departments d JOIN employees e USING (department_id); ・SELECT departments.department_id, departments.department_name, employees.employee_name FROM departments JOIN employees ON departments.department_id = employees.department_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, d.department_name, e.employee_na...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55325
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314

### 問題ID 26504 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26504?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表、EMPLOYEES表の構造を確認して下さい。 全従業員のうち、いずれかの部署に所属している従業員の従業員番号、従業員名、所属部署番号、所属部署名を表示するには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。
- 解説要約: DEPARTMENTS表とEMPLOYEES表から、全従業員のうち、いずれかの部署に所属している従業員の従業員番号、従業員名、所属部署番号、所属部署名を取り出すには、2つの表の共通列であるDEPARTMENT_ID列の値で等価結合を行います。 以上より、 ・SELECT e.employee_id, e.employee_name, d.department_id, d.department_name FROM departments d, employees e WHERE d.department_id = e.department_id; ・SELECT employee_id, employee_name, department_id, department_name FROM departments JOIN employees USING (department_id); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT e.employee_id, e.employee_name, d.department_id, d.dep...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Joins.html#SQLRF52350
  - https://atmarkit.itmedia.co.jp/ait/articles/1203/22/news164.html

### 問題ID 26505 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26505?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: EMPLOYEES表の構造とGRADE表の構造とデータを確認して下さい。 従業員の給与等級を表示するには、どの問い合わせを実行しますか。 なお、従業員の給与等級は、EMPLOYEES表のSALARY列の値と、GRADE表のLOW列からHIGH列の値の範囲で決定します。
- 解説要約: 結合条件に「値が同じであること」(結合条件に=(等号)を使用する)を指定するのではなく、「指定した範囲内に含まれること」を指定する結合などを不等価結合といいます。 非等価結合では、結合条件に<,>,<=,>=,BETWEEN等の演算子を使用します。 設問では、従業員の給与等級を表示するために、EMPLOYEES表のSALARY列の値がGRADE表のHIGH列とLOW列の値の範囲内である行を結合することで、従業員の給与等級を表示することができます。 以上より、 ・SELECT g.grade, e.employee_name FROM grade g JOIN employees e ON salary BETWEEN low AND high ORDER by 1; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT g.grade, e.employee_name FROM grade g JOIN employees e WHERE salary BETWEEN low AND high ORDER by g...
- 参考URL: なし

### 問題ID 26506 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26506?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 従業員名とその上司の氏名を表示するには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。
- 解説要約: 従業員の氏名はEMPLOYEES表から取り出せます。 しかし上司の氏名を取り出すには、EMPLOYEES表のMANAGER_ID列の値でEMPLOYEES表を検索し、EMPLOYEE_NAME列の値を取り出す必要があります。 このようなデータの取り出しを行うには、従業員の氏名を持つEMPLOYEES表と、MANAGER_IDを持つEMPLOYEES表があると見立てて、2つの表を結合します(自己結合といいます)。 自己結合はON句もしくはOracle独自の結合構文で行えます。 以上より、 ・SELECT emp.employee_name, mgr.employee_name FROM employees emp, employees mgr WHERE emp.manager_id = mgr.employee_id; ・SELECT emp.employee_name, mgr.employee_name FROM employees emp JOIN employees mgr ON emp.manager_id = mgr.employee_id; が正解となります。 正解のSQ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52351

### 問題ID 26507 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26507?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表のMANAGER_ID列には上司のEMPLOYEE_IDが登録されています。また、上司のいない従業員のMANAGER_ID列にはNULL値が登録されています。 従業員名とその上司の氏名を表示するには、どの問い合わせを実行しますか。 ただし、上司がいない従業員については、上司の氏名欄を空欄として表示して下さい。
- 解説要約: 従業員の氏名はEMPLOYEES表から取り出せます。 しかし上司の氏名を取り出すには、EMPLOYEES表のMANAGER_ID列の値でEMPLOYEES表を検索し、EMPLOYEE_NAME列の値を取り出す必要があります。 このようなデータの取り出しを行うには、従業員の氏名を持つEMPLOYEES表と、MANAGER_IDを持つEMPLOYEES表があると見立てて、2つの表を結合します(自己結合といいます)。 また、設問の「上司がいない従業員については、上司の氏名欄を空欄として下さい」より、上司のいない従業員のデータも取り出すということがわかります。これは結合条件に合致しないデータも取り出すということですので、外部結合を行います。 全ての選択肢において表別名empから従業員名を、mgrから上司名を取り出していますが、empから取り出す従業員名は結合条件に合致しないデータも取り出さなくてはなりません。 全ての選択肢において、列別名empはJOIN句の左側にありますので、LEFT OUTER JOINを使用します。 以上より、 ・SELECT emp.employee_name, mgr...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Joins.html#GUID-29A4584C-0741-4E6A-A89B-DCFAA222994A

### 問題ID 26508 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26508?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 2つの表を結合するSQL文としてエラーとなるものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 選択肢のSQL文を1つずつ確認してみましょう。 ・SELECT department_name, employee_name, salary FROM departments d JOIN employees e WHERE d.department_id = e.department_id; JOIN句で結合する場合、結合条件はON句、またはUSING句に記述します。このSQL文のように等号（=）を使用するならばON句が必要ですが、WHERE句に結合条件が指定されておりエラーとなります。 ・SELECT department_name, employee_name, salary FROM departments d LEFT OUTER JOIN employees e ON d.department_id = e.department_id; LEFT OUTER JOINによる左側外部結合です。結合条件にJOIN句の左側に指定された表のデータは、結合条件に合致しない場合でも表示します。正しいSQL文です。 ・SELECT d.department_name, e.employe...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#sthref2240

### 問題ID 26509 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26509?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 次の問い合わせの実行結果として、正しいものはどれですか。 SELECT d.department_name, e.employee_name FROM departments d CROSS JOIN employees e;
- 解説要約: CROSS JOINキーワードで表の結合を行うと、2つの表に登録されている行の全ての組合せ(デカルト積といいます)を返すクロス結合が行われます。 クロス結合では、2つの表に登録されている行の全ての組合せが返されるので、結合条件の指定はできません。 以上より、 ・2つの表に格納されているデータの全ての組合せが表示される が正解となります。 設問のDEPARTMENTS表とEMPLOYEES表のデータの登録件数はそれぞれ以下の通りです。 SQLを表示 SELECT COUNT(*) FROM departments; SQLを表示 SELECT COUNT(*) FROM employees; 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT d.department_name, e.employee_name FROM departments d CROSS JOIN employees e; その他の選択肢については次のとおりです。 ・結合条件を指定していないので、エラーとなる クロス結合では結合条件を指定できません。 ・2つの表に共通して存在する列に基づいて...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52352

### 問題ID 26510 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26510?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 副問合せに関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: Oracle DatabaseではSQL文の中に別のSQL文を入れ子にして実行することができ、入れ子の内側の問合せのことを副問合せといいます(副問合せに対し、外側の問合せを主問合せといいます)。副問合せは、SELECT文のSELECT句、FROM句、WHERE句、HAVING句の他、INSERT文やUPDATE文等のDML文でも使用することができます。 副問合せには、次のようにいろいろな使用方法があります。 ・SELECT文のSELECT句、FROM句、WHERE句、HAVING句、ORDER BY句や、INSERT文、UPDATE文等のDML文で使用できる ・主問合せと副問合せで異なる表にアクセスできる ・1つの主問合せに対し、複数の副問合せを指定できる ・副問合せをネストできる(WHERE句に指定した副問合せでは255レベルのネストが可能) ・副問合せの中でGROUP BY句やHAVIMG句、ORDER BY句を使用できる なお、副問合せには、1件のデータを返す単一行副問合せと複数行の結果を返す複数行副問合せがあります。 以上より、 ・主問合せと副問合せで異なる表にアクセスできる ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858
  - https://atmarkit.itmedia.co.jp/ait/articles/1208/06/news118.html

### 問題ID 26511 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26511?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せと同じ結果となる問合せはどれですか。 SELECT employee_id, employee_name FROM employees WHERE employee_id =ANY (SELECT manager_id FROM employees);
- 解説要約: =ANY(値のリスト)はリスト内のいずれかの値と等しい場合にTRUEとなります。IN(値のリスト)と等価です。 以上より、 ・SELECT employee_id, employee_name FROM employees WHERE employee_id IN (SELECT manager_id FROM employees); が正解となります。 設問のSQL文の実行結果と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name FROM employees WHERE employee_id =ANY (SELECT manager_id FROM employees); SQLを表示 SELECT employee_id, employee_name FROM employees WHERE employee_id IN (SELECT manager_id FROM employees); その他の選択肢については次のとおりです。 ・SELECT employee_id, employee_name ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26512 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26512?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せを実行すると、何件のデータが返されますか。 SELECT prodid, name, category FROM prod WHERE category IN (SELECT category FROM oldprod WHERE category IS NOT NULL);
- 解説要約: IN(値のリスト)はリスト内のいずれかの値と等しい場合にTRUEとなります。 設問のSQL文では、副問合せからOLDPROD表のNULL値以外のCATEGORY列の値である"10","40","60"が返されるので、主問合せでは、PROD表のCATEGORY列の値が"10","40"の行が取り出されます。 以上より、 ・2 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prodid, name, category FROM prod WHERE category IN (SELECT category FROM oldprod WHERE category IS NOT NULL); 参考： 複数行演算子には次のものがあります。 複数行演算子ANYとALLは必ず単一行演算子とセットで使用しなければなりません。 また、IN演算子はNOT演算子と組合せて使用することができます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26513 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26513?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 所属従業員の平均給与が、全社員の平均給与より多い部署に所属する従業員を表示するには、どの問い合わせを実行しますか。
- 解説要約: IN(値のリスト)はリスト内のいずれかの値と等しい場合にTRUEとなります。 選択肢のSQL文の副問合せでは、所属従業員の平均給与が、全社員の平均給与より多い部署のDEPARTMENT_IDを取り出していますので、主問合せでは、副問合せで取り出したDEPARTMENT_IDのいずれかの値と等しい行を取り出せば良いことになります。そのためにはIN演算子を使用します。 以上より、 ・SELECT department_id, employee_id, employee_name FROM employees WHERE department_id IN (SELECT department_id FROM employees HAVING AVG(salary) > (SELECT AVG(salary) FROM employees) GROUP BY department_id); が正解となります。 正解のSQL文の実行結果は次のようになります。 参考： 複数行演算子には次のものがあります。 複数行演算子ANYとALLは必ず単一行演算子とセットで使用しなければなりません。 また、IN...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26514 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26514?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せを実行したところ、データが1件も表示されませんでした。原因は何ですか。 なお、EMPLOYEES表にはHIREDATE列が'10-04-01'以降の従業員が10件登録されています。 SELECT employee_id, employee_name, salary FROM employees WHERE salary NOT IN (SELECT salary FROM employees WHERE hiredate >= '10-04-01');
- 解説要約: NOT IN演算子は、リスト内の全ての値と等しくない場合にTRUEを返します。 そのため、NOT IN演算子の値のリストにNULL値が含まれていると、NULL値と比較対象の値の比較結果がNULL値になるので、全ての値と等しくないという判定がなされず、主問合せではデータが1件も取り出されません。 設問の副問合せで返されるSALARY列の値にはNULL値が含まれているため、主問合せではデータが1件も取り出されません。 以上より、 ・副問合せの結果にNULL値が含まれているため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees WHERE salary NOT IN (SELECT salary FROM employees WHERE hiredate >= '10-04-01'); その他の選択肢については次のとおりです。 ・副問合せの結果がNULL値となるため 副問合せの結果にはNULL値以外の値も含まれます。 ・NOT IN演算子と複数行副...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions013.htm#CJAFFIIG

### 問題ID 26515 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26515?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次の問合せと同じ結果となる問合せはどれですか。 SELECT employee_id, employee_name FROM employees WHERE employee_id NOT IN (SELECT manager_id FROM departments);
- 解説要約: NOT IN(値のリスト)はリスト内の全ての値と等しくない場合にTRUEとなります。<>ALL(値のリスト)と等価です。 以上より、 ・SELECT employee_id, employee_name FROM employees WHERE employee_id <>ALL (SELECT manager_id FROM departments); が正解となります。 設問のSQL文の実行結果と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name FROM employees WHERE employee_id NOT IN (SELECT manager_id FROM departments); SQLを表示 SELECT employee_id, employee_name FROM employees WHERE employee_id <>ALL (SELECT manager_id FROM departments); その他の選択肢については次のとおりです。 ・SELECT employee...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26516 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26516?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せと同じ結果となる問合せはどれですか。 SELECT employee_id, employee_name, salary FROM employees WHERE salary >=ANY (SELECT AVG(salary) FROM employees GROUP BY department_id);
- 解説要約: ANY演算子はリスト内のいずれかの値が条件を満たす場合にTRUEを返しますので、>=ANY(値のリスト)は比較する値がリスト内のいずれかの値と等しいか、それよりも大きい場合にTRUEを返します。 ANY演算子はリスト内の値のうち1つでも条件を満す値があればTRUEとなるので、>=ANY(値のリスト)はリスト内の最小値以上の場合にTRUEを返すということになります。 したがって、>=ANY(値のリスト)は>=リスト内の最小値に置き換えることができます。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees WHERE salary >= (SELECT MIN(AVG(salary)) FROM employees GROUP BY department_id); が正解となります。 設問のSQL文の実行結果と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees WHERE salary >=A...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26517 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26517?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せを実行すると、何件のデータが返されますか。 SELECT prodid, name, category FROM prod WHERE category >ANY (SELECT category FROM oldprod WHERE category IS NOT NULL);
- 解説要約: ANY演算子はリスト内のいずれかの値が条件を満たす場合にTRUEを返しますので、>ANY(値のリスト)は比較する値がリスト内のいずれかの値よりも大きい場合にTRUEを返します。 ANY演算子はリスト内の値のうち1つでも条件を満す値があればTRUEとなるので、>ANY(値のリスト)はリスト内の最小値より大きい場合にTRUEとなるということです。 設問のSQL文では、副問合せからOLDPROD表のNULL値以外のCATEGORY列の値である"10","40","60"が返されるので、主問合せではCATEGORY列の値が"10","40","60"の最小値である"10"より大きい行がPROD表から取り出されます。 以上より、 ・4 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prodid, name, category FROM prod WHERE category >ANY (SELECT category FROM oldprod WHERE category IS NOT NULL); 参考： 複数行演算子には次のものがあります。 ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26518 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26518?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せと同じ結果となる問合せはどれですか。 SELECT employee_id, employee_name, salary FROM employees WHERE salary >ALL (SELECT AVG(salary) FROM employees GROUP BY department_id);
- 解説要約: ALL演算子はリスト内の全ての値が条件を満たす場合にTRUEを返しますので、>ALL(値のリスト)は比較する値がリスト内の全ての値よりも大きい場合にTRUEを返します。 ALL演算子はリスト内の全ての値が条件を満たさなければTRUEにならないため、>ALL(値のリスト)では、比較する値がリスト内の最大値よりも大きければTRUEを返すということになります。 したがって、>ALL(値のリスト)は>リスト内の最大値に置き換えることができます。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees WHERE salary > (SELECT MAX(AVG(salary)) FROM employees GROUP BY department_id); が正解となります。 設問のSQL文の実行結果と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees WHERE salary >ALL (SELEC...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26519 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26519?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せを実行すると、何件のデータが返されますか。 SELECT prodid, name, category FROM prod WHERE category <ALL (SELECT category FROM oldprod WHERE category > 10);
- 解説要約: ALL演算子はリスト内の全ての値が条件を満たす場合にTRUEをかえしますので、<ALL(値のリスト)は比較する値がリスト内の全ての値よりも小さい場合にTRUEを返します。 ALL演算子はリスト内の全ての値が条件を満たさなければTRUEにならないため、<ALL(値のリスト)はリスト内の最小値より小さい場合にTRUEになるということです。 設問のSQL文では、副問合せからOLDPROD表のCATEGORY列の値である"40","60"が返されるので、主問合せではCATEGORY列の値が"40","60"の最小値である"40"より小さい行がPROD表から取り出されます。 以上より、 ・3 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prodid, name, category FROM prod WHERE category 10); 参考： 複数行演算子には次のものがあります。 複数行演算子ANYとALLは必ず単一行演算子とセットで使用しなければなりません。 また、IN演算子はNOT演算子と組合せて使用することができます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#SQLRF52105

### 問題ID 26520 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26520?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 各部署の平均月収のうち、一番安い平均月収よりも安い月収の従業員を表示するには、どの問い合わせを実行しますか。
- 解説要約: ALL演算子はリスト内の全ての値が条件を満たす場合にTRUEをかえしますので、<ALL(値のリスト)は比較する値がリスト内の全ての値よりも小さい場合にTRUEを返します。 ALL演算子はリスト内の全ての値が条件を満たさなければTRUEにならないため、<ALL(値のリスト)はリスト内の最小値より小さい場合にTRUEになるということです。 設問の問合せを行うには、副問合せで各部署の平均月収を取り出し、<ALL演算子で各部署の平均月収の最小値よりも小さい月収の従業員を取り出します。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees WHERE salary <ALL (SELECT AVG(salary) from employees GROUP BY department_id); が正解となります。 正解のSQL文の実行結果は次のようになります。 参考： 複数行演算子には次のものがあります。 複数行演算子ANYとALLは必ず単一行演算子とセットで使用しなければなりません。 また、IN演算子はNOT演算子と組合せ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm

### 問題ID 26521 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26521?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: 複合問合せに関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 集合演算子を用いて複合問合せを行う場合、SELECT句に指定する列や式は次のガイドラインに従います。 ・複合問合せの列見出しは1つ目の問合せに指定された列名が使用される(それぞれの問合せで指定される列名が異なっていても良い) ・2つの問合せでSELECT句に指定する列や式の数を同数にしなければならない ・2つの問合せでSELECT句に指定する列や式のデータ型を同じ、もしくは同じデータ型グループにしなければならない(ただし、サイズは異なっていても良い) 以上より、 ・1つ目の問合せと2つ目の問合せで、SELECT句に指定する列や式を同じ数にしなければならない ・1つ目の問合せと2つ目の問合せで、SELECT句に指定する列のデータ型を同じデータ型（もしくは同じデータ型グループ）にしなければならない ・1つ目の問合せと2つ目の問合せで、SELECT句に指定した列のデータ型が同じであれば、列のサイズが異なっていても良い が正解となります。 なお、同じデータ型グループとは同じデータを扱うデータ型をグループ化したものです。 例えば、CHAR型とVARCHAR2型はどちらも文字列を扱いますので、同じ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Set-Operators.html
  - https://docs.oracle.com/cd/F19136_01/sqlrf/The-UNION-ALL-INTERSECT-MINUS-Operators.html

### 問題ID 26522 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26522?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: UNION演算子の説明として、正しいものはどれですか。
- 解説要約: UNION演算子を用いた複合問合せでは、2つの問合せの結果から重複行を排除して表示します。この時、NULL値が含まれる場合は重複したNULL値は排除され、NULL値が1つだけ表示されます。 UNION演算子を用いた複合問合せの結果は、SELECT句の1番目に指定されている列で昇順にソートされて表示されます。 以上より、 ・問合せの結果はソートされる が正解となります。 その他の選択肢については次のとおりです。 ・2つの問合せの結果から重複行もすべて表示する 重複行は排除されます。 ・NULL値は表示しない NULL値は表示されます。NULL値が重複した場合は、重複したNULL値は排除され、NULL値が1つだけ表示されます。 ・2つの問合せで、SELECT句には同じ列名を指定する 列数を同数にする必要がありますが、列名は異なっていても構いません。 参考： UNION演算子を用いた複合問合せでは、2つの問合せの結果から重複行を排除して表示します。 SQLを表示 SELECT job_id FROM jobs; SELECT DISTINCT job_id FROM employees; S...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26523 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26523?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: UNION ALL演算子に関する説明として、正しいものはどれですか。
- 解説要約: UNION ALL演算子を用いた複合問合せでは、2つの問合せの結果を重複行も含めて表示します。NULL値が含まれている場合は、重複したNULL値も全て表示します。 なお、問合せ結果は、UNION演算子を用いた複合問合せとは異なり、ソートされませんので注意しましょう。 以上より、 ・問合せの結果をソートしない が正解となります。 その他の選択肢については次のとおりです。 ・2つの問合せの結果から重複行を排除して表示する UNION演算子の説明です。 ・NULL値を無視して表示する 複合問合せではNULL値は無視されません。UNION ALL演算子を用いた複合問合せでは、重複したNULL値も全て表示されます。 ・2つの問合せの結果のうち共通する行を表示する INTERSECT演算子の説明です。 参考： UNION ALL演算子を用いた複合問合せでは、2つの問合せの結果を重複行も含めて表示します。 SQLを表示 SELECT job_id FROM jobs; SELECT job_id FROM employees; SQLを表示 SELECT job_id FROM jobs UNION...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26524 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26524?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: INTERSECT演算子の説明として、正しいものはどれですか。
- 解説要約: INTERSECT演算子を用いた複合問合せでは、2つの問合せの結果の共通する行を表示します。この時、NULL値が含まれる場合は重複したNULL値は排除され、NULL値が1つだけ表示されます。 INTERSECT演算子を用いた複合問合せの結果は、SELECT句の1番目に指定されている列で昇順にソートされて表示されます。 以上より、 ・問合せの結果にNULL値が含まれている場合は、NULL値を1つだけ表示する が正解となります。 その他の選択肢については次のとおりです。 ・問合せの結果がソートされない 問合せの結果はSELECT句の1番目に指定されている列で昇順にソートされます。 ・1つ目の問合せから2つ目の問合せと重複しない行を表示する MINUS演算子の説明です。 ・1つ目の問合せと2つ目の問合せの順番を入れ替えると結果が変わる 2つの問合せ結果の共通する行を表示するので、1つ目と2つ目の問合せの順番を入れ替えても結果は変わりません。 ・2つの問合せのSELECT句に指定する列の数は異なっていても良い 問合せの列名は異なっていても構いませんが、列数は同数にする必要があるので、誤りです。...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26525 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26525?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: MINUS演算子に関する説明として、誤っているものはどれですか。
- 解説要約: MINUS演算子を用いた複合問合せでは、1つ目の問合せ結果から2つ目の問合せ結果にない行を表示します。そのため、1つ目の問合せと2つ目の問合せの順序を入れ替えた問合せでは結果が異なります。 その他の集合演算子では、順番を入れ替えても取り出される行は同じです。 以上より、 ・1つ目の問合せと2つ目の問合せの順序を逆にしても結果は同じになる が正解となります。 次の複合問合せで、指定するSELECT文の順序を入れ替えると次のようになります。 SQLを表示 SELECT job_id FROM jobs MINUS SELECT job_id FROM employees; 順序を入れ替えた結果： SQLを表示 SELECT job_id FROM employees MINUS SELECT job_id FROM jobs; 参考： MINUS演算子を用いた複合問合せでは、1つ目の問合せ結果から2つ目の問合せ結果にない行を表示します。 SQLを表示 SELECT job_id FROM jobs; SELECT DISTINCT job_id FROM employees; SQLを表示...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26526 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26526?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せの実行結果はどうなりますか。 SELECT category FROM prod UNION SELECT category FROM oldprod;
- 解説要約: 設問のSQL文はUNION演算子を用いて複合問合せを行なっています。 UNION演算子を用いた複合問合せでは、2つの問合せの結果から重複行を排除して表示されます。したがって、問合せの結果は、2つの問合せの結果からPROD表とOLDPROD表で重複している"10, 40, NULL"の値を排除したものが表示されます。 以上より、 が正解となります。 参考： UNION演算子を用いた複合問合せでは、2つの問合せの結果から重複行を排除して表示します。 SQLを表示 SELECT job_id FROM jobs; SELECT DISTINCT job_id FROM employees; SQLを表示 SELECT job_id FROM JOBS UNION SELECT job_id FROM employees; UNION演算子による複合問合せでは、内部的に、問合せ結果をSELECT句の1番目に指定されている列の昇順にソートし(1番目に指定されている列に同値がある場合は、さらに2つ目に指定されている列の昇順にソートします)、重複行を排除して結果を表示します。 SQLを表示 SELE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26527 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26527?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せの実行結果はどうなりますか。 SELECT category FROM prod UNION ALL SELECT category FROM oldprod;
- 解説要約: 設問のSQL文はUNION ALL演算子を用いて複合問合せを行なっています。 UNION ALL演算子を用いた複合問合せでは、2つの問合せの結果を重複行も含めて表示します。したがって、問合せの結果は、PROD表の問合せ結果である"10, 20, 30, 40, 50, NULL"とOLDPROD表の問合せ結果である"10, 40, 60, NULL"が重複行も含めて表示されます。 以上より、 が正解となります。 参考： UNION ALL演算子を用いた複合問合せでは、2つの問合せの結果を重複行も含めて表示します。 SQLを表示 SELECT job_id FROM jobs; SELECT job_id FROM employees; SQLを表示 SELECT job_id FROM jobs UNION ALL SELECT job_id FROM employees; 複合問合せでは問合せの結果にNULL値が含まれていてもNULL値を無視しません。UNION ALL演算子を用いた複合問合せでは、重複したNULL値も全て表示されます。 SQLを表示 SELECT salary FR...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26528 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26528?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せの実行結果はどうなりますか。 SELECT category FROM prod MINUS SELECT category FROM oldprod;
- 解説要約: 設問のSQL文はMINUS演算子を用いて複合問合せを行なっています。 MINUS演算子を用いた複合問合せでは、1つ目の問合せ結果から2つ目の問合せ結果にない行を表示します。したがって、複合問合せの結果は、PROD表の問合せ結果である"10, 20, 30, 40, 50, NULL"からOLDPROD表の問合せ結果である"10, 40, 60, NULL"を除いた"20, 30, 50"が表示されます。 以上より、 が正解となります。 参考： MINUS演算子を用いた複合問合せでは、1つ目の問合せ結果から2つ目の問合せ結果にない行を表示します。 SQLを表示 SELECT job_id FROM jobs; SELECT DISTINCT job_id FROM employees; SQLを表示 SELECT job_id FROM jobs MINUS SELECT job_id FROM employees; MINUS演算子による複合問合せでは、内部的に、問合せ結果をSELECT句の1番目に指定されている列の昇順にソートし(1番目に指定されている列に同値がある場合は、さらに2つ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26529 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26529?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: トランザクションの説明として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: トランザクションは、前回処理を確定または取消した後に、COMMIT文やROLLBACK文を実行した時や、DDL文、DCL文を実行した時に終了します。 DML文は1つ以上の文のまとまりで1つのトランザクションになりますので、一連の処理の終了後、COMMIT文またはROLLBACK文を実行する等してトランザクションを終了します。 以上より、 ・トランザクションはDDL文により終了する ・トランザクションはDCL文により終了する ・トランザクションは前回コミットまたはロールバックしてから次回コミットまたはロールバックするまでの一連の処理のことである が正解となります。 その他の選択肢については次のとおりです。 ・DML文は常に1つの文で1つのトランザクションになる DML文は1つ以上の文のまとまりで1つのトランザクションになります。 ・トランザクションはSAVEPOINT文により終了する SAVEPOINT文はトランザクション内にマーカーを作成します。SAVEPOINT文ではトランザクションは終了しません。 ・トランザクションはDML文により終了する DML文は1つ以上の文のまとまりで1つの...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/transactions.html

### 問題ID 26530 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26530?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: TRUNCATE文の説明として誤っているものはどれですか。
- 解説要約: TRUNCATE文の特徴は以下のとおりです。 ・削除するデータを指定できず、表の全てのデータを削除する ・DDL文のため自動コミットが実行され、処理を取消できない ・DELETE文よりも処理が高速である 以上より、 ・TRUNCATE文では削除するデータを指定できる が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10007.htm#SQLRF01707

### 問題ID 26531 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26531?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 自動ロールバックされるイベントとして、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: Oracle Databaseでは次の場合に自動ロールバックされます。 ・システム障害が発生した場合 ・SQL *Plusを×ボタンで終了した時など異常終了した場合 以上より、 ・システム障害時 ・SQL *Plusの異常終了時 が正解となります。 その他の選択肢については次のとおりです。 ・EXIT文でSQL *Plus終了時 ・DDL文実行時 これらの場合は自動コミットされます。 ・SAVEPOINT文実行時 SAVEPOINT文ではトランザクション内にマーカーを作成しますが、トランザクションは終了しません。 参考： COMMIT文やROLLBACK文実行時以外でもトランザクションが終了する場合があります(暗黙的トランザクション処理)。 暗黙的トランザクション処理には、全ての処理を自動的に確定する自動コミットと、全ての処理を自動的に取消す自動ロールバックの2種類があります。 [自動コミット] SQLを表示 UPDATE dummy SET column2 = 'oracle' WHERE column1 = 1; CREATE TABLE dummy2 (column1 NUMBE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/transact.htm#g11401

### 問題ID 26532 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26532?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 自動コミットされるイベントとして、誤っているものはどれですか。
- 解説要約: Oracle Databaseでは次の場合に自動コミットされます。 ・DDL文を実行した場合 ・DCL文を実行した場合 ・SQL DeveloperやSQL *Plusを正常終了した場合 選択肢のTRANCATE文はDDL文に該当し、INSERT文はDML文に該当します。 DML文実行時は自動コミットされません。 以上より、 ・INSERT文実行時 が正解となります。 参考： COMMIT文やROLLBACK文実行時以外でもトランザクションが終了する場合があります(暗黙的トランザクション処理)。 暗黙的トランザクション処理には、全ての処理を自動的に確定する自動コミットと、全ての処理を自動的に取消す自動ロールバックの2種類があります。 [自動コミット] SQLを表示 UPDATE dummy SET column2 = 'oracle' WHERE column1 = 1; CREATE TABLE dummy2 (column1 NUMBER(2), column2 VARCHAR2(10)); ROLLBACK; SELECT * FROM dummy; [自動ロールバック] SQL...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/transact.htm#g11401

### 問題ID 26533 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26533?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(該当するものを全て選択して下さい)。 1. SQL> INSERT INTO prod VALUES (11, 'Debussy', 10, SYSDATE, NULL); 2. SQL> SAVEPOINT a; 3. SQL> UPDATE prod SET name = 'Chopin' WHERE prodid = 11; 4. SQL> SAVEPOINT b; 5. SQL> DELETE prod WHERE prodid = 11; 6. SQL> ROLLBACK TO S...
- 解説要約: 6.のROLLBACK文により、3.以降の処理が取消されます。そのため、PROD表のPRODID列の値が11である行のNAME列の値は"Debussy"となります。4.で作成したセーブポイントbも取消されます。 ただし、2.で作成したセーブポイントaは残っています。 以上より、 ・SAVEPOINT bは無効となる ・PRODID=11のNAME列の値は"Debussy"である が正解となります。 設問のSQL文を順に説明します。 1.INSERT文により、PROD表にデータが1件追加されます。ただし、INSERT文はDML文に該当し自動コミットされないため、データの追加は確定されていない状態です。 2.セーブポイントaを作成します。 3.PROD表のPRODID列の値が11である行のNAME列の値を"Chopin"に変更します。UPDATE文はDML文に該当し自動コミットされないため、データの変更は確定されていない状態です。 4.セーブポイントbを作成します。 5.DELETE文により、PROD表のPRODID列の値が11である行を削除します。DELETE文はDML文に該当し自動コミ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10001.htm#SQLRF01701
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9021.htm#SQLRF55217

### 問題ID 26534 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26534?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(該当するものを全て選択して下さい)。 1. SQL> INSERT INTO prod VALUES (11, 'Debussy', 10, SYSDATE, NULL); 2. SQL> COMMIT; 3. SQL> SAVEPOINT a; 4. SQL> UPDATE prod SET name = 'Chopin' WHERE prodid = 11; 5. SQL> ROLLBACK; 6. SQL> SAVEPOINT b; 7. SQL> DELETE prod WHERE ...
- 解説要約: 5.のROLLBACK文により、3.以降の処理が取消されます。そのため、SAVEPOINT aは無効となり、PROD表のPRODID列の値が11である行のNAME列の値は"Debussy"となります。 7.でPRODID列の値が11である行が削除されていますが、直後のROLLBACK文により、削除が取消されます。 以上より、 ・SAVEPOINT aは無効となる ・PRODID=11のNAME列の値は"Debussy"である が正解となります。 設問のSQL文を順に説明します。 1.INSERT文により、PROD表にデータが1件追加されます。ただし、INSERT文はDML文に該当し自動コミットされないため、データの追加は確定されていない状態です。 2.COMMIT文により、それまでの処理が確定されます。1.で追加したデータはこのCOMMIT文で確定されますので、取消すことはできません。 3.セーブポイントaを作成します。 4.PROD表のPRODID列の値が11である行のNAME列の値を"Chopin"に変更します。UPDATE文はDML文に該当し自動コミットされないため、データの変更...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10001.htm#SQLRF01701
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9021.htm#SQLRF55217

### 問題ID 26535 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26535?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(該当するものを全て選択して下さい)。 なお、それぞれのユーザは、Oracleへの接続には同一アカウント(pingt）を使用して同じデータにアクセスしているものとします。 ユーザーA： 1.SQL> INSERT INTO prod VALUES (11, 'Debussy', 10, SYSDATE, NULL); 2.SQL> COMMIT; 3.SQL> UPDATE prod SET name = 'Liszt' WHERE prodid = 11; 4.SQL> SELECT * F...
- 解説要約: ユーザーAがデータの変更を行なっているとき、ユーザーAが変更処理をコミットするまで、他のユーザーはユーザーAが変更後のデータを参照することはできません(ユーザーAは変更処理が確定されていなくても、変更後のデータを参照することができます)。ユーザーAが変更処理をコミットする前に他のユーザーがそのデータを参照した場合、他のユーザーへは変更前のデータが返されます。ユーザーAの変更が確定されるまで待機させられることはありません。 以上より、 ・ユーザーAが参照したデータのNAME列の値は"Liszt"である ・ユーザーBが参照したデータのNAME列の値は"Debussy"である ・ユーザーCが参照したデータのNAME列の値は"Liszt"である が正解となります。 設問のSQL文を順に説明します。 ユーザーA： 1.SQL> INSERT INTO prod VALUES (11, 'Debussy', 10, SYSDATE, NULL); 2.SQL> COMMIT; 3.SQL> UPDATE prod SET name = 'Liszt' WHERE prodid = 11; 4.SQ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/consist.htm

### 問題ID 26536 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26536?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 読取り一貫性に関する説明として、正しいものはどれですか(該当するものを3つ選択して下さい)。
- 解説要約: 読取り一貫性は、データの読取りを開始した時点で最新のコミット済みのデータを返すことを保証します。 データの変更処理がコミットされていない場合、変更したデータは変更したユーザーだけが参照でき、他のユーザーへはUNDOセグメントにある変更前のデータが返されます。 以上より、 ・他のユーザーが更新中のデータを参照した場合、Oracleサーバーは更新前にコミットされたデータを返す ・読み取り一貫性を実現するためにUNDOセグメントが使用される ・未確定のデータは、更新中のユーザーだけが参照できる が正解となります。 参考： 複数のユーザーが同時に同じデータに対して操作を行うと、データの不整合が発生する可能性があります。 例えば、あるデータに対して、同時に、読取りを行うユーザーAと書込みを行うユーザーBがいる場合、ユーザーAがデータの読取り中にユーザーBがデータの書込みを行ってしまうと、ユーザーAは一貫性のあるデータを取得することができません。 このような場合、Oracle Databaseは「読取り一貫性」という機能でそれぞれのユーザーに対して一貫性のあるデータを提供します。 読取り一貫性は、...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/consist.htm

### 問題ID 26537 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26537?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 排他ロックに関する説明として、正しいものはどれですか。
- 解説要約: Oracle Databaseは複数のユーザーが同時に同じ行に対して変更処理(INSERT,UPDATE,DELETE)を行った場合に、データの矛盾が生じないよう、行毎に排他ロックをかけて変更処理を行います。 排他ロックがかかっている行に対して変更処理を行おうとすると、排他ロックが解除されるまで待機させられます。排他ロックはトランザクションの終了時に解除されます。 以上より、 ・INSERT、UPDATE、DELETE文実行時、Oracleサーバーは排他ロックをかける が正解となります。 その他の選択肢については次のとおりです。 ・他のユーザーが更新中のデータを参照した場合、更新が完了するまで待機させられる 更新中のデータを他のユーザーが参照した場合、UNDOセグメントにコピーされた変更前のデータが返されます。 ・排他ロックでは表全体がロックされる 行毎にロックされます ・ロックがかかっている行に対して、DELETE文を実行すると待機せずに処理される ロックがかかっている行に対して変更処理(INSERT,UPDATE,DELETE)を行うとロックが解除されるまで待機させられます。 参考...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/consist.htm

### 問題ID 26538 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26538?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(該当するものを全て選択して下さい)。 なお、それぞれのユーザは、Oracleへの接続には同一アカウント(pingt)を使用して同じデータにアクセスしているものとします。 ユーザーA： 1.SQL> INSERT INTO prod VALUES (11, 'Debussy', 10, SYSDATE, NULL); 2.SQL> COMMIT; 3.SQL> SELECT name FROM prod WHERE prodid = 11; 4.SQL> UPDATE prod SET nam...
- 解説要約: ユーザーAが変更処理を行うと、変更対象となる行は排他ロックがかけられ、他のユーザーが変更処理を行おうとすると、ユーザーAの変更処理が確定されるまで待機しなければなりません。 また、変更処理中のデータを他のユーザーが参照すると、他のユーザーは変更処理が確定されるまで、変更後のデータを参照することはできません。 以上より、 ・ユーザーAが10.で参照したデータのNAME列の値は"Chopin"である ・ユーザーBの5.の操作は待機させられる が正解となります。 設問のSQL文を順に説明します。 ユーザーA： 1.SQL> INSERT INTO prod VALUES (11, 'Debussy', 10, SYSDATE, NULL); 2.SQL> COMMIT; 3.SQL> SELECT name FROM prod WHERE prodid = 11; 4.SQL> UPDATE prod SET name = 'Liszt' WHERE prodid = 11; ユーザーB： 5.SQL> UPDATE prod SET name = 'Chopin' WHERE prodid...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/consist.htm

### 問題ID 26539 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26539?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 次の問合せの説明として、正しいものはどれですか。 SELECT employee_id, employee_name, hiredate FROM employees WHERE department_id IN (1, 2, 3) FOR UPDATE NOWAIT;
- 解説要約: SELECT文にFOR UPDATE句を指定すると、SELECT文で取り出される行に排他ロックをかけることができます。この時、SELECT文で取り出される行が別のセッションで既にロックされていると、別のセッションのロックが解除されるまで、SELECT文は待機しますが、NOWAITオプションを指定すると、待機せずにすぐにエラーを返します。 設問のSELECT文では、FOR UPDATE句にNOWAITオプションが指定されているので、SELECT文で取り出される行が既に別のセッションで排他ロックをかけられている場合は、待機せずにエラーを返します。 以上より、 ・検索対象の行が他のユーザーにロックされている場合はエラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 ユーザーA： SELECT employee_id, employee_name, hiredate FROM employees FOR UPDATE; ユーザーB： SELECT employee_id, employee_name, hiredate FROM employees W...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55370

### 問題ID 26540 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26540?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表にデータを追加するSQL文として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 表にデータを追加するには、INSERT文を使用します。 INSERT文にはデータを追加する列名と値を1対1で指定します。列名を省略する場合は、表内の列の構成の順で値を指定します。 列名と対応する値のデータ型が異なると、エラーとなります。 以上より、 ・INSERT INTO prod(prodid, name, category, startdate, enddate) VALUES (20, 'SuperMan', 20, '2001-02-15', '2010-10-30'); ・INSERT INTO prod VALUES (20, 'SuperMan', 20, '2001-02-15', '2010-10-30'); ・INSERT INTO prod(startdate, enddate, prodid, name, category) VALUES ('2001-02-15', '2010-10-30', 20, 'SuperMan', 20); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 INSERT INTO prod(prod...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm#SQLRF01604

### 問題ID 26541 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26541?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表にデータを追加するSQL文として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 列にNULL値を登録するには、NULL値を登録する列に明示的にNULLまたは''(一重引用符を2つ)を指定するか、INSERT文で列の指定を省略します。 NULL値の指定時、'NULL'としてしまうと文字列として判断されてしまいますので、注意しましょう。 以上より、 ・INSERT INTO prod(prodid, name, category, startdate, enddate) VALUES (11, 'OnePiece', 30, '2011-02-15', NULL); ・INSERT INTO prod(prodid, name, category, startdate) VALUES (11, 'OnePiece', 30, '2011-02-15'); ・INSERT INTO prod VALUES (11, 'OnePiece', 30, '2011-02-15', ''); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 INSERT INTO prod(prodid, name, category, startdate, e...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm#SQLRF01604

### 問題ID 26542 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26542?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次のSQL文を実行したところ、エラーとなりました。エラーの原因は何ですか。 INSERT INTO prod(name, category, startdate, prodid) VALUES('Pokemon', 50, NULL, NULL);
- 解説要約: INSERT文でデータを追加する際に、表のNOT NULL制約が定義されている列の値にNULL値を登録することはできません。 INSERT文でデータ追加時、NOT NULL制約が定義されている列にNULLや''(一重引用符を2つ)を指定したり、列の指定を省略したりするとエラーとなります。 以上より、 ・PRODID列にNULL値が設定されているため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 INSERT INTO prod(name, category, startdate, prodid) VALUES('Pokemon', 50, NULL, NULL); その他の選択肢については次のとおりです。 ・ENDDATE列の値が省略されているため INSERT文でNOT NULL制約が定義されていない列を省略してもエラーとはなりません。省略した列にはNULL値が登録されます。 ・STARTDATE列にNULL値が設定されているため STARTDATE列にはNOT NULL制約が定義されていないため、NULL値を登録することができます。 ・INSER...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm#SQLRF01604

### 問題ID 26543 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26543?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 2つの表の特定の列の値が等しいデータだけを取り出す結合はどれですか。
- 解説要約: Oracle Databaseではいろいろな方法で表を結合することができます。主な結合方法は次の通りです。 以上より、 ・等価結合 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#sthref2240

### 問題ID 26544 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26544?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表のデータを更新するSQL文として、正しいもの（エラーとならないもの）はどれですか(該当するものを全て選択して下さい)。
- 解説要約: 表のデータを更新するには、UPDATE文を使用します。 UPDATE文では、SET句に更新する列名と値を=(イコール)でつなぎ指定します。複数の列の値を1つのUPDATE文で更新する場合は、列名と値のセットを,(カンマ)で区切って指定します。 なお、NOT NULL制約を定義された列をNULL値で更新することはできません。エラーとなります。 以上より、 ・UPDATE prod SET name = 'SuperMario', startdate = '09-04-28' WHERE prodid = 5; ・UPDATE prod SET startdate = '12-05-01'; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 UPDATE prod SET name = 'SuperMario', startdate = '09-04-28' WHERE prodid = 5; SELECT * FROM prod WHERE prodid = 5; SQLを表示 UPDATE prod SET startdate = '12-05-01';...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF01708

### 問題ID 26545 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26545?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PRODID列の値が3の行のNAME列の値を"Atom"に、STARTDATE列の値を登録されている値の3ヶ月後に変更するSQL文はどれですか。
- 解説要約: 現在の日付のnヶ月後を計算するには、ADD_MONTHS関数を使用します。 日付値に数値を加算すると日数として加算されますので、注意しましょう。 以上より、 ・UPDATE prod SET name = 'Atom', startdate = ADD_MONTHS(startdate, 3) WHERE prodid = 3; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT * FROM prod WHERE prodid = 3; UPDATE prod SET name = 'Atom', startdate = ADD_MONTHS(startdate, 3) WHERE prodid = 3; SELECT * FROM prod WHERE prodid = 3; その他の選択肢については次のとおりです。 ・UPDATE prod SET name = 'Atom', startdate = startdate + 3 WHERE prodid = 3; 日付値に数値を加算すると日数として加算します。そのためSTARTDATE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF01708
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions011.htm#SQLRF00603

### 問題ID 26546 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26546?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 UPDATE employees SET salary = (SELECT MAX(salary) FROM employees) WHERE employee_id IN (SELECT manager_id FROM departments WHERE department_id = 1);
- 解説要約: UPDATE文のSET句で副問合せを使用して、表のデータを更新することができます。SET句に副問合せを使用すると、別の表の値に基いてデータを更新することもできます。 以上より、 ・正常に実行され、値が変更される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees WHERE employee_id IN (SELECT manager_id FROM departments WHERE department_id = 1); UPDATE employees SET salary = (SELECT MAX(salary) FROM employees) WHERE employee_id IN (SELECT manager_id FROM departments WHERE department_id = 1); SELECT employee_id, employee_name, salary FROM employees WHERE e...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF01708

### 問題ID 26547 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26547?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 STARTDATE列の値が"2003年4月1日"以降である行を削除するSQL文はどれですか。
- 解説要約: 表のデータを削除するには、DELETE文を使用します。 ある条件に合致したデータだけを削除する場合は、DELETE文にWHERE句を指定して削除する行の条件を指定します。 設問では、PROD表のSTARTDATE列の値が"2003年4月1日"以降のデータを削除するので、DELETE文のWHERE句に条件を指定します。 なお、TRUNCATE文も表のデータを削除しますが、DELETE文のように条件を指定して表のデータを削除することはできません。 以上より、 ・DELETE FROM prod WHERE startdate >= '03-04-01'; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT * FROM prod; DELETE FROM prod WHERE startdate >= '03-04-01'; SELECT * FROM prod; その他の選択肢については次のとおりです。 ・DELETE prod; 削除する行の条件が指定されていないため、PROD表の全ての行が削除されてしまいます。 ・TRUNCATE TABL...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF01505

### 問題ID 26548 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26548?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 DELETE FROM employees WHERE employee_id IN (SELECT manager_id FROM departments WHERE department_id = 1);
- 解説要約: DELETE文のWHERE句には副問合せを使用した条件を指定することができます。 設問では、副問合せでDEPARTMENTS表のDEPARTMENT_ID列が1である部署のマネージャーIDを取得し、EMPLOYEES表から該当する従業員のデータを削除しています。 副問合せの結果が1行も返されなかった場合は、1行も削除されないだけでエラーにはなりません。 設問のSQL文は文法上の誤りもありませんので、正常に実行することができます。 以上より、 ・正常に実行され、行が削除される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 DELETE FROM employees WHERE employee_id IN (SELECT manager_id FROM departments WHERE department_id = 1); SELECT * FROM employees WHERE employee_id IN (SELECT manager_id FROM departments WHERE department_id = 1); 参考： 表に格...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF01505

### 問題ID 26549 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26549?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 DELETE (SELECT department_id, employee_id FROM employees) WHERE salary > 400000;
- 解説要約: DELETE文では、削除の対象となる表を指定する際、表名だけではなく副問合せによる指定をすることができます。 表名の代わりに副問合せを指定したDELETE文では、条件に副問合せで指定した列のみ使用することができます。 設問のSQL文は文では、副問合せにDEPARTMENT_ID列とEMPLOYEE_ID列が指定されていますが、WHERE句で副問合せに指定されていないSALARY列を使用しているため、エラーとなります。 以上より、 ・表名の代わりに指定した副問合せのSELECT句に指定された列しかWHERE句に指定できないため、エラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 DELETE (SELECT department_id, employee_id FROM employees) WHERE salary > 400000; 参考： 表に格納されているデータを削除するには、DELETE文を使用します。 DELETE [FROM] 表名 [WHERE 条件]; SQLを表示 SELECT * FROM prod; DELETE FRO...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF01505

### 問題ID 26550 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26550?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 マネージャーである従業員とEMPLOYEE_ID列の値が1001である従業員を削除するSQL文として、エラーとなる可能性のあるものはどれですか(2つ選択して下さい)。
- 解説要約: EMPLOYEES表からデータを削除する条件をまとめると、 ・マネージャーである従業員 もしくは ・EMPLOYEE_ID = 1001 となりますが、このうち、マネージャーである従業員は、EMPLOYEES表のMANAGER_IDの値を取得すればよいので、 ・EMPLOYEE_ID IN (SELECT DISTINCT manager_id FROM employees) のように記述できます。 MANAGER_IDの値を返す問合せは複数行のデータを返す可能性がありますので、IN演算子を使用します。複数行のデータが返された場合に比較演算子に=演算子を使用しているとエラーとなります。 また、「IN (値1, 値2, 副問合せ, ...)」のようにIN演算子の値のリスト中の値の1つとして副問合せを使用する場合も、複数行が返された場合はエラーとなります。副問合せが複数行のデータを返す可能性がある場合は、「IN (副問合せ)」のように副問合せを単独で値のリストに指定します。 以上より、 ・DELETE employees WHERE employee_id IN (1001, (SELEC...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF01505

### 問題ID 26551 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26551?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: スキーマ・オブジェクトはどれですか(該当するものを全て選択して下さい)。
- 解説要約: スキーマ・オブジェクトとはデータベースに格納する表やビュー、索引などの総称で特定のユーザーに所有されるものです。 記憶域やロール、ユーザー等システム全体で共有されるものはスキーマ・オブジェクトではありません。 以上より、 ・表 ・ビュー ・シノニム ・索引 が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56306/tablecls.htm#i22627
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements007.htm#SQLRF51127

### 問題ID 26552 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26552?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 表および全てのデータを完全に削除するのはどれですか。
- 解説要約: 表を完全に削除するには、DROP TABLE文にPURGEオプションを指定して実行します。PURGEオプションを指定しないと、表はごみ箱に移動され、後で復元することができます。 以上より、 ・DROP TABLE 表名 PURGE; が正解となります。 その他の選択肢については次のとおりです。 ・TRUNCATE TABLE 表名; ・DELETE FROM 表名; 表のデータだけを削除します。 ・DROP TABLE 表名; 表をごみ箱へ移動します。ごみ箱へ移動した表はFLASHBACK TABLE文で復元することができます。 参考： 表の削除はDROP ANY TABLE権限を持つユーザーによって行われます。 DROP TABLE 表名 [PURGE]; SQLを表示 DROP TABLE prod_table; 表を削除すると、表と表内のデータ、表に定義した制約、索引も同時に削除されます。その表を参照しているビューやシノニムは削除されませんが、無効になります。無効になったビューやシノニムにアクセスするとエラーになります。 SQLを表示 CREATE VIEW prod_view ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/ADMIN/tables.htm#GUID-C35B192C-1C8B-425F-A003-D36D0EABEB3A
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9003.htm#SQLRF01806

### 問題ID 26553 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26553?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 表の削除に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: DROP TABLE文で表をごみ箱に移動したり、完全に削除したりすることができます。ごみ箱に移動した表は復元することができます。 表を削除すると、表と表内のデータ、表に定義した制約、索引も同時に削除されます。その表を参照しているビューやシノニムは削除されませんが、無効になります。無効になったビューやシノニムにアクセスするとエラーになります。 以上より、 ・表を削除すると、表に定義されている制約や索引も同時に削除される ・ごみ箱に移動した表を復元することができる が正解となります。 その他の選択肢については次のとおりです。 ・表を削除できるのは、表の所有者だけである 表の削除はDROP ANY TABLE権限を持つ全てのユーザーが表を削除することができます。 ・DROP TABLE文では表をごみ箱に移動するだけで、完全に削除する方法はない 表を完全に削除するにはPURGEオプションを指定して削除します。 ・表を削除すると、関連するビューやシノニムも同時に削除される 制約や索引は同時に削除されますが、ビューやシノニムは削除されません。 参考： 表の削除はDROP ANY TABLE権限を持...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/ADMIN/tables.htm#GUID-C35B192C-1C8B-425F-A003-D36D0EABEB3A
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9003.htm#SQLRF01806

### 問題ID 26554 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26554?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 DROP TABLE prod_table;
- 解説要約: DROP TABLE文はDDL文に該当します。 DDL文では、1文で1つのトランザクションとなるため、DROP TABLE文実行後はトランザクションが終了します。 以上より、 ・PROD_TABLE表の構造とデータが削除され、トランザクションが終了する が正解となります。 その他の選択肢については次のとおりです。 ・PROD_TABLE表のデータは削除されるが、構造は削除されない DROP TABLE文では、表の構造、データの両方が削除されます。表のデータだけを削除したい場合はDELETE文を使用します。 ・PROD_TABLE表の構造とデータが完全に削除され、以後復元できない DROP TABLE文にPURGEオプションが指定されていない場合、表はごみ箱に移動するだけで、完全に削除されたわけではありません。FLASHBACK TABLE文でごみ箱に移動した表を復元することができます。 ・PROD_TABLE表の構造とPROD_TABLE表を参照するビューが削除される 表を削除してもビューは削除されません。 参考： 表の削除はDROP ANY TABLE権限を持つユーザーによって行われ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/ADMIN/tables.htm#GUID-C35B192C-1C8B-425F-A003-D36D0EABEB3A
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9003.htm#SQLRF01806
  - https://docs.oracle.com/cd/E16338_01/server.112/b56306/transact.htm#CNCPT88953

### 問題ID 26555 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26555?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 文字列を扱うデータ型の説明として、誤っているものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 文字列を扱うデータ型には、CHAR型、VARCHAR2型、LONG型、CLOB型等のデータ型があります。このうち、主に使用されるのがCHAR型とVARCHAR2型です。 CHAR型、VARCHAR2型の特徴は次の通りです。 以上より、 ・文字型の列を定義する場合は、必ずサイズを指定しなければならない ・VARCHAR2型とCHAR型に違いはない が正解となります。 その他の選択肢については次のとおりです。 ・LONG型の列はORDER BY句に指定することはできない LONG型の列はORDER BY句やGROUP BY句に指定することはできません。 ・LONG型よりもCLOB型のほうが大きなデータを扱うことができる LONG型が2GBまでなのに対し、CLOB型は4GBまで扱うことができます。 ・LONG型の列は1つの表に1つだけ定義することができる LONG型は1つの表に1つだけ定義することができます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF50973
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00201
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF20041

### 問題ID 26556 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26556?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: NUMBER型の説明として、誤っているものはどれですか。
- 解説要約: データ型がNUMBER(5,2)の列に12.345を入力すると、小数点第3位が四捨五入され、12.35が格納されます。 以下は実行結果です。 SQLを表示 CREATE TABLE temp1 (number1 NUMBER(5, 2) ); INSERT INTO temp1 VALUES(12.345); SELECT number1 FROM temp1; 誤りを選ぶ問題ですので、 ・データ型がNUMBER(5,2)の列に12.345を入力すると、12.34が格納される が正解となります。 実行結果のように、12.34ではなく12.35が格納されます。 その他の選択肢については、すべて正しい結果が記述されています。 参考： NUMBER型は数値データを格納するために使用するデータ型です。 次のように定義します。 列名 NUMBER[(最大精度[, 位取り])] 最大精度：格納する数値の全体の桁数(1~38桁) 位取り：小数点以下の桁数(-84~127)。負の値が指定された場合は、整数部の丸める桁数を指定したとこになる。 位取りを省略した場合は、NUMBER(最大桁数, 0)と同じ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/tablecls.htm#CBBFFHEB
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00222

### 問題ID 26557 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26557?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: バイナリデータを格納するデータ型として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: バイナリデータを扱う主なデータ型は次の通りです。 選択肢にあるLONG型は最大2GBの文字型です。また、BINARYというデータ型はありません。 以上より、 ・RAW ・BLOB ・BFILE ・LONG RAW が正解となります。 なお、LONG RAW型はLONG型と同様に以下の制限があります。 ・LONG RAW型の列は1つの表に1つだけ定義できる ・LONG RAW型の列には制約は定義できない ・LONG RAW型の列はGROUP BY句とORDER BY句に指定できない ・副問合せによる表の作成時、LONG RAW型の列はコピーできない
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF50993
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF50997
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF50996

### 問題ID 26558 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26558?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 制約の目的として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 制約とは、表に格納するデータに関するルールです。表に制約を定義することで、ルールに反するデータの追加や、ルールを満たさなくなるようなデータの更新、削除を行うことができなくなります。 以上より、 ・無効なデータの登録を防止する ・他の表との間に依存性のあるデータの誤削除を防止する が正解となります。 その他の選択肢については次のとおりです。 ・データ参照時のパフォーマンスを向上させる 制約のチェックのために時間が必要となるため、パフォーマンスは向上しません。但し、一部の制約には索引を自動作成するものがあり、索引はデータ参照時のパフォーマンスを向上させる効果があります。しかしそれは索引の効果であり、制約それ自体がパフォーマンスを向上させる訳ではありません。 ・表へのアクセス制限を行う 制約は表に格納するデータに関するルールです。表自体のアクセスを宣言するものではありません。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#g20134
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52180

### 問題ID 26559 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26559?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文のうち、エラーとなるものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: UNIQUE制約は列レベル、表レベルのどちらでも定義することができますが、複数の列の組合せに対してUNIQUE制約を定義する場合は、表レベルで定義しなければなりません。 また、表レベルで制約を定義する場合は、制約を定義する列を指定しなければなりません。 以上より、 ・CREATE TABLE temp ( id NUMBER(2) CONSTRAINT temp_uq UNIQUE (id, name), name VARCHAR2(10) CONSTRAINT name_nn NOT NULL, birth DATE ); ・CREATE TABLE temp ( id NUMBER(2) CONSTRAINT id_uq UNIQUE, name VARCHAR2(10) CONSTRAINT name_nn NOT NULL, birth DATE, CONSTRAINT temp_uq UNIQUE ); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE temp (id NUMBER(2) CONSTRAINT tem...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDCJAAE
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52195

### 問題ID 26560 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26560?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文でTEMP表を作成し、データを追加しました。 CREATE TABLE temp ( id NUMBER(2) NOT NULL, name VARCHAR2(10), birth DATE, CONSTRAINT temp_uq UNIQUE (id, name) ); INSERT INTO temp VALUES (1, 'tanaka', '88-05-21'); INSERT INTO temp VALUES (2, 'sasaki', '75-12-07'); INSERT INTO temp VALUES (3, 'yamada', '90-02-14'); TEMP...
- 解説要約: 設問ではTEMP表のID列とNAME列の組合せに対してUNIQUE制約を定義しています。そのため、TEMP表に追加するデータは、ID列とNAME列の組合せが一意にならなければなりません。 すでに3件のデータが登録されているので、既に登録されているデータのID列、NAME列の組合せと同じ組合せのデータはエラーとなります。 以上より、 ・INSERT INTO temp VALUES (1, 'tanaka', '69-10-05'); ・INSERT INTO temp VALUES (2, 'sasaki', '76-08-31'); が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE temp (id NUMBER(2) NOT NULL, name VARCHAR2(10), birth DATE, CONSTRAINT temp_uq UNIQUE (id, name) ); INSERT INTO temp VALUES (1, 'tanaka', '88-05-21'); INSERT INTO temp VALUES ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDCJAAE
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52195

### 問題ID 26561 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26561?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: PRIMARY KEY制約に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: PRIMARY KEY制約を定義すると、定義された列または列の組合せに重複したデータやNULL値を登録することができなくなります。 PRIMARY KEY制約は1つの表に1つしか定義することができません。ですが、必ず指定しなければならないわけではありません。 PRIMARY KEY制約は複数の列の組合せに対して定義することができます。その場合は表レベルで定義します。 なお、PRIMARY KEY制約を定義すると、自動的に制約と同じ名前の一意索引が作成されます。 以上より、 ・1つの表に1つしか定義することができない ・PRIMARY KEY制約を定義した列にはNULL値を格納できない ・PRIMARY KEY制約を定義すると、自動的に索引が作成される が正解となります。 参考： 列または列の組合せにPRIMARY KEY制約を定義すると、定義された列または列の組合せに重複したデータやNULL値を登録することができなくなります。 SQLを表示 CREATE TABLE temp (id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY, name VARCHA...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDDBJBB
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52197

### 問題ID 26562 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26562?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文のうち、エラーとなるものはどれですか。
- 解説要約: PRIMARY KEY制約は、1つの表に1つしか定義することができません。複数の列に個別にPRIMARY KEY制約を定義することはできません。 以上より、 ・CREATE TABLE temp ( id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT name_pk PRIMARY KEY, birth DATE ); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE temp (id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT name_pk PRIMARY KEY, birth DATE ); 参考： 列または列の組合せにPRIMARY KEY制約を定義すると、定義された列または列の組合せに重複したデータやNULL値を登録することができなくなります。 SQLを表示 CREATE TABLE temp (id NUMBER(2) CONSTRA...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDDBJBB
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52197

### 問題ID 26563 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26563?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: FOREIGN KEY制約の説明として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: FOREIGN KEY制約の親表に指定された表は、依存する行の有無にかかわらず削除することができません。 また、親表のデータを削除した場合の子表の振る舞いは、 ・ON DELETE CASCADEオプション ・ON DELETE SET NULLオプション を指定して設定できます。 ON DELETE CASCADEでは、親表の行が削除された場合、参照していた子表の行も同時に削除されます。 また、ON DELETE SET NULLでは、親表の行が削除された場合、参照していた子表の列にNULL値を設定します。 以上より、 ・ON DELETE CASCADEオプションを指定すると、親表の行を削除する際に、親表を参照している子表の行も自動的に削除する ・FOREIGN KEY制約を定義すると、依存する行の有無にかかわらず親表を削除できない が正解となります。 その他の選択肢については次のとおりです。 ・ON DELETE CASCADEオプションを指定すると、親表の行を削除する際に、親表を参照している子表の行にNULL値を設定する ON DELETE SET NULLの説明です。 ・ON...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDIIGBG
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52199

### 問題ID 26564 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26564?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文のうち、正常に実行できるSQL文はどれですか。
- 解説要約: CHECK制約の条件にはWHERE句に指定する条件と同等のものを指定できますが、次の指定はできません。 ・CURRVAL,NEXTVAL,LEVEL,ROWNUM疑似列 ・SYSDATE,UID,USER,USERENV関数 ・他の行を参照する問合せ また、複数の列を使用する条件は表レベルで定義しなければなりません。 以上より、 ・CREATE TABLE temp ( id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY, name VARCHAR2(10), salary NUMBER(8), commission NUMBER(8), CONSTRAINT salary_ck CHECK (salary < commission) ); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE temp (id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY, name VARCHAR2(10), salary NUMBER(8), commission NUMBER(8...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDGBFBJ
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52204

### 問題ID 26565 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26565?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次の3つのSQL文の文を実行したところ、エラーとなりました。エラーの原因は何ですか(該当するものを全て選択して下さい)。 CREATE TABLE customer_table ( customer_id NUMBER(2) CONSTRAINT custid_pk PRIMARY KEY, cust_name VARCHAR2(30), cust_address VARCHAR2(50) ); CREATE TABLE order_table (order_id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY, order_date DATE CONSTRAIN...
- 解説要約: 列の組合せに対してPRIMARY KEY制約を定義する場合は、表レベルで定義しなければなりません。 設問のORDER_ITEM_TABLE表では、列レベルでPRIMARY KEY制約を定義しているので、エラーとなります。 また、CHECK制約はWHERE句で指定できる条件と同様の指定ができますが、SYSDATE関数を使用できない等いくつかの制限があります。 以上より、 ・列の組合せに対してPRIMARY KEY制約を定義する場合は、表レベルで定義しなければならないため ・CHECK制約の条件にSYSDATE関数を使用できないため が正解となります。 その他の選択肢については次のとおりです。 ・CHECK制約ではBETWEEN演算子は使用できないため CHECK制約の条件にはWHERE句で指定できる条件と同様の指定ができます。BETWEEN演算子も使用することができます。 ・列の組合せに対してPRIMARY KEY制約を定義できないため 列の組合せに対してPRIMARY KEY制約を定義することができます。列の組合せに対してPRIMARY KEY制約を定義する場合は、表レベルで定義します...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#g20134
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52180

### 問題ID 26566 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26566?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文のうち、正常に実行されるものはどれですか。
- 解説要約: 制約は列レベル、表レベルで定義することができます。制約を定義する場合は、次の事項に注意します。 ・CONSTRAINT 制約名は省略することができる ・CONSTRAINT 制約名を省略した場合は、「SYS_Cn」という制約名となる（nには一意の番号が振られる） ・1つの列に複数の列レベル制約を定義する場合は、スペースで区切って定義する 例) 列名 データ型 [[CONSTRAINT 制約名1] 制約の種類] [[CONSTRAINT 制約名2] 制約の種類] ・1つの表に複数の表レベル制約を定義する場合は、カンマで区切って定義する ・列レベル制約と表レベル制約では機能に違いはない ・列レベル制約と表レベル制約は1つの表で同時に指定できる ・複数の列の組み合わせに対して制約を定義する場合は、表レベル制約でのみ定義できる ・NOT NULL制約は列レベルでのみ定義できる なお、PRIMARY KEY制約は1つの表に1つだけしか定義することはできません。また、CHECK制約の条件にはSYSDATE関数を使用することはできません。 以上より、 ・CREATE TABLE table1 ( c...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#g20134
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52180

### 問題ID 26567 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26567?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次の要件を満たす表を作成するには、どのSQL文を実行しますか。 ・IDはサイズ2の数値型で、NULL値を入力できない ・IDには重複した値を入力できない ・ORDER_DATEは日付型で、NULL値を入力できない ・ORDER_DATEのデフォルト値は当日の日付 ・QTYはサイズ3の数値型で、1以上125以下の値しか入力できない ・PAYMENTは文字型で、"Cash"か"Credit"のどちらかしか入力できない
- 解説要約: 設問の要件は以下の通りです。 ・IDはサイズ2の数値型で、NULL値を入力できない ・IDには重複した値を入力できない ・ORDER_DATEは日付型で、NULL値を入力できない ・ORDER_DATEのデフォルト値は当日の日付 ・QTYはサイズ3の数値型で、1以上125以下の値しか入力できない ・PAYMENTは文字型で、"Cash"か"Credit"のどちらかしか入力できない 要件を満たす列の定義は次の通りです。 ・ID : ID NUMBER(2) PRIMARY KEY または ID NUMBER(2) UNIQUE NOT NULL ・ORDER_DATE : ORDER_DATE DATE DEFALUT SYSDATE NOT NULL ・QTY : QTY NUMBER(3) CHECK (qty BETWEEN 1 AND 125) または QTY NUMBER(3) CHECK (qty >= 1 AND qty <= 125) ・PAYMENT : VARCHAR2(6) CHECK (payment IN ('Cash', 'Credit')) または VARC...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF01402

### 問題ID 26568 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26568?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE tmp ( id#9 NUMBER(2) NOT NULL, name$ VARCHAR2(20), birth_day DATE NOT NULL, age DATE DEFAULT SYSDATE - birth_day, image777 LONG );
- 解説要約: 表の作成時に、列にDEFAULTオプションを指定するとその列のデフォルト値を設定できます。 DEFAULTオプションには式や関数を指定できますが、他の列を参照する式は指定できません。 以上より、 ・DEFAULTオプションの指定に他の列を使用できないため、エラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE tmp (id#9 NUMBER(2) NOT NULL, name$ VARCHAR2(20), birth_day DATE NOT NULL, age DATE DEFAULT SYSDATE - birth_day, image777 LONG );
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF01402
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF54458

### 問題ID 26569 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26569?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表をコピーしてEMPLOYEES2表を作成するSQL文として誤っているものはどれですか。
- 解説要約: 副問合せによる表の作成では、副問合せのSELECT句に計算式や関数を指定する場合は、計算式や関数に列別名を指定するか、CREATE TABLE文で列名を指定しなければなりません。 計算式や関数に列別名が指定されておらず、かつCREATE TABLE文の列名も省略されているとエラーとなります。 以上より、 ・CREATE TABLE employees2 AS SELECT employee_id, employee_name, salary * 12 + commission FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE employees2 AS SELECT employee_id, employee_name, salary*12+commission FROM employees;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF54626

### 問題ID 26570 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26570?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE employees2 AS SELECT employee_id, employee_name, salary*12 sal FROM employees WHERE 1 = 2;
- 解説要約: 副問合せによる表の作成では、表作成時に、副問合せで取り出されたデータも一緒にコピーされますが、副問合せの結果取り出されるデータが1件もなかった場合は表の構造だけがコピーされます。 設問の副問合せのWHERE句に指定された条件は、1 = 2と絶対に成立しない条件ですので、副問合せによって取り出されるデータは0件です。したがって、設問のSQL文では表の構造だけがコピーされます。 以上より、 ・EMPLOYEES表の構造だけがコピーされる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE employees2 AS SELECT employee_id, employee_name, salary*12 sal FROM employees WHERE 1 = 2; DESC employees2; SELECT * FROM employees2;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF54626

### 問題ID 26571 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26571?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表のEMPLOYEE_ID列にはPRIMARY KEY制約だけが定義されています。 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE employees2 (id, name, hiredate DEFAULT SYSDATE, sal CHECK (sal > 100000)) AS SELECT employee_id, employee_name, hiredate, salary FROM employees;
- 解説要約: 副問合せによる表の作成時、データ型とNOT NULL制約は問合せた表から新たに作成する表へとコピーされますが、NOT NULL制約以外の制約やデフォルト値はコピーされません。 ただし、副問合せによる表の作成時にデフォルト値を設定したり、制約を定義することはできます。 設問のSQL文では、HIREDATE列にデフォルト値を、SAL列にCHECK制約を定義しています。 また、ID列は、EMPLOYEES表のPRIMARY KEYであるEMPLOYEE_ID列をコピーしていますが、PRIMARY KEY制約はコピーされないため、ID列にはPRIMARY KEY制約は定義されません。 以上より、 ・表が作成されるが、ID列にはPRIMARY KEY制約は定義されない が正解となります。 その他の選択肢については次のとおりです。 ・副問合せを使用した表の作成では、CREATE TABLE文でDEFAULT値を設定できないため、エラーとなる ・副問合せを使用した表の作成では、CREATE TABLE文で制約を定義できないため、エラーとなる 副問合せによる表の作成時、列のデフォルト値を設定したり、制...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF54626

### 問題ID 26572 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26572?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 副問合せによる表の作成時、新たに作成した表にコピーされるものはどれですか。
- 解説要約: 副問合せによる表の作成時、新たに作成する表の列にデータ型を指定することができません。列のデータ型は副問合せにより自動的に定義されます。 また、副問合せで問合せを行なっている表の列にNOT NULL制約が明示的に定義されている場合、新たに作成する表にもNOT NULL制約がコピーされますが、その他の制約はコピーされません。 以上より、 ・データ型 ・NOT NULL制約 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF54626

### 問題ID 26573 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26573?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: ALTER TABLE文で実行できる項目はどれですか。
- 解説要約: 既存の表の定義を変更するにはALTER TABLE文を使用します。 ALTER TABLE文では、次の操作を行うことができます。 ・新しい列の追加 ・既存の列のデータ型の変更 ・既存の列へのデフォルト値の設定 ・既存の列への制約の定義 ・既存の列の削除 ・既存の列名の変更 ・表のモード変更(読み取り/書き込みモード、読み取り専用モード) 以上より、 ・制約の追加 ・列の追加 ・データ型の変更 が正解となります。 その他の選択肢については次のとおりです。 ・表の削除 表の削除はDROP TABLE文で行います。 ・データの削除 データの削除はDELETE文またはTRUNCATE文で行います。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_3001.htm#SQLRF01001

### 問題ID 26574 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26574?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューに関する説明として、誤っているものはどれですか。
- 解説要約: ビューを利用する目的は次の通りです。 ・データへのアクセス制御 ・複雑なSQL文の簡素化 ・データの独立性を確保 ・同じデータを異なる視点で表示 以上より、 ・問合せのパフォーマンスが向上する が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56306/schemaob.htm#i20690

### 問題ID 26575 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26575?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 月収が450,000以下である従業員の従業員番号、氏名、部署、入社日を持つビューを作成するには、どのSQL文を実行しますか(該当するものを2つ選択して下さい)。
- 解説要約: ビューの作成はCREATE VIEW文で行います。 設問ではビューの条件として、 ・月収が450,000以下 ・列は従業員番号、氏名、部署、入社日を持つ の2つを挙げていますので、この条件を満たす問合せをCREATE VIEW文の副問合せに指定してビューを作成します。 なお、ビューに別名を指定する場合、副問合せのSELECT句に指定した列の数と別名の数を同数にしなければなりません。 以上より、 ・CREATE VIEW v_emp AS SELECT employee_id, employee_name, hiredate, department_id FROM employees WHERE salary <= 450000; ・CREATE VIEW v_emp (id, name, hiredate, dept) AS SELECT employee_id, employee_name, hiredate, department_id FROM employees WHERE salary <= 450000; が正解となります。 正解のSQL文の実行結果は次のようになります。 ...
- 参考URL:
  - https://docs.oracle.com/cd/F23071_01/aeutl/managing-views.html#GUID-80EA2657-998D-47AD-908E-14CA108F8070
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF01504

### 問題ID 26576 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26576?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューの削除に関する説明として、誤っているものはどれですか。
- 解説要約: ビューの削除は、ビューの所有者またはDROP ANY VIEW権限を持つユーザーによって行われます。 ビューを削除してもビューの定義に含まれる実表に影響はありません。しかし削除したビューを基にして作成したビュー、削除したビューのシノニムは無効となります。 以上より、 ・ビューを削除すると、実表は無効となる が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9009.htm#SQLRF01812

### 問題ID 26577 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26577?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューを通して実表のデータを削除できないのは、ビューの定義にどの要素が含まれている場合ですか(該当するものを全て選択して下さい)。
- 解説要約: ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 以上より、 ・GROUP BY句 ・グループ関数 ・ROWNUM擬似列 ・DISTINCTキーワード が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF54819

### 問題ID 26578 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26578?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: NEXTVAL擬似列、CURRVAL擬似列を指定できる箇所はどれですか(該当するものを全て選択して下さい)。
- 解説要約: NEXTVAL擬似列、CURRVAL擬似列は以下の箇所で参照することができます。 ・主問合せのSELECT句 ・INSERT文の副問合せのSELECT句 ・INSERT文のVALUES句 ・UPDATE文のSET句 ・CREATE TABLE文またはALTER TABLE文の列のDEFAULT値 よって正解は上記5つとなります。 また、NEXTVAL擬似列、CURRVAL擬似列は以下では使用することはできません。 ・SELECT文、UPDATE文、DELETE文内の副問合せ ・ビューのSELECT句 ・DISTINCTキーワードが指定されたSELECT文 ・GROUP BY句、ORDER BY句、HAVING句を持つSELECT文 ・集合演算子UNION、INTERSECT、MINUSによって別のSELECT文と結合されているSELECT文 ・SELECT文のWHERE句 ・CHECK制約の条件
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Sequence-Pseudocolumns.html#GUID-D438E28B-3E30-4B12-8D52-8DA5CFE2E0FF

### 問題ID 26579 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26579?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 順序値の欠番が発生する原因として、誤っているものはどれですか。
- 解説要約: 順序は指定された規則に従って一意な順序値を生成しますが、以下のような場合には欠番が生じることもあり、連番が保証されているわけではありません。 ・ロールバックが発生した時 ・システムがクラッシュした時 また、複数の表で同じ順序を使用している場合も、それら複数の表全体で一意な順序値が生成されるので、1つの表だけを見ると連番とならない場合があります。 以上より、 ・コミット が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314

### 問題ID 26580 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26580?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: DEPARTMENTS表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE departments5 AS SELECT * FROM departments WHERE 1 = 2; CREATE SEQUENCE seq_dept; INSERT INTO departments5 VALUES (seq_dept.currval, 'Sales', 1001); UPDATE departments5 SET department_id = seq_dept.nextval WHERE manager_id = 1001;
- 解説要約: 現在のセッションで一度も順序値が生成されていないときにCURRVAL擬似列を参照すると、エラーとなります。 設問のSQL文では、順序を生成した後、NEXTVAL擬似列を参照せずにCURRVAL擬似列を参照しているためエラーとなります。 以上より、 ・NEXTVAL擬似列を参照する前にCURRVAL擬似列を参照しているので、エラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE departments5 AS SELECT * FROM departments WHERE 1 = 2; CREATE SEQUENCE seq_dept; INSERT INTO departments5 VALUES (seq_dept.CURRVAL, 'Sales', 1001); その他の選択肢については次のとおりです。 ・順序の増分値が指定されていないため、CREATE SEQUENCE文で、エラーとなる 順序値の増分値が指定されていない場合は、デフォルトの増分値が適用されます。 ・正常に実行され、MANAGER_IDが1001の行...
- 参考URL: なし

### 問題ID 26581 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26581?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文の説明として、正しいものはどれですか。 CREATE SEQUENCE seq_id CACHE 25 NOCYCLE;
- 解説要約: 順序の生成時、キャッシュを利用していない場合は、順序値の生成のためにデータディクショナリ（オブジェクトの情報を格納する表）に毎回アクセスし順序値を生成します。これに対し、キャッシュを利用している場合は、メモリ上にいくつかの順序値を生成するときだけデータディクショナリにアクセスします。そのため、キャッシュを利用しない場合と比べて、キャッシュを利用している場合のほうが順序値を取得する処理が高速になります。 以上より、 ・キャッシュを利用するため、順序値を高速に取得できる が正解となります。 その他の選択肢については次のとおりです。 ・順序値が最大値に到達すると、初期値に戻って繰り返し順序を生成する 順序の生成時、NOCYCLEが指定されているので、順序が最大値に達すると、順序の生成を終了します。 ・キャッシュを利用するので、順序の欠番が発生しない キャッシュ利用中にシステムクラッシュが発生すると、メモリ上の順序値が失われるので、欠番が生じます。 ・キャッシュを利用する場合は、順序値の最大値の指定が必須なので、エラーとなる 順序値の最大値が明示的に指定されていない場合は、デフォルトの最大値が...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/admin/managing-views-sequences-and-synonyms.html#GUID-83FA2D7D-6119-4182-94EA-60554024A2CE

### 問題ID 26582 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26582?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 順序の変更に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 順序の変更では、START WITHオプション以外のオプションを変更することができます。 ただし、現在までに生成された順序値よりも小さな最大値を設定するなど、現在までに生成された値と矛盾するような定義の変更はできません。 なお、順序の定義を変更しても、現在までに生成された順序値に影響はありません。 以上より、 ・順序の定義を変更しても、既に生成された順序値に影響はない ・キャッシュ上に生成するキャッシュ値の個数を変更できる ・順序の定義の変更時、妥当性のチェックが行われる が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_2012.htm#SQLRF00817

### 問題ID 26583 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26583?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文で順序の変更したところエラーとなりました。エラーの原因は何ですか。 SQL> SELECT seq_id.currval FROM dual; CURRVAL ------- 250 SQL> ALTER SEQUENCE seq_id 2 INCREMENT BY 10 3 MAXVALUE 200 4 NOCYCLE 5 NOCACHE;
- 解説要約: 順序の変更では、START WITHオプション以外のオプションを変更することができます。 ただし、現在までに生成された順序値よりも小さな最大値を設定するなど、現在までに生成された値と矛盾するような定義の変更はできません。 設問のSQL文では現在の順序値が250であるのに対し、最大値を200に変更しようとしています。 現在までに生成された順序値の整合性が損なわれるため、この変更はエラーとなります。 以上より、 ・最大値に既に生成されている順序値よりも小さい値が指定されたため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT seq_id.CURRVAL FROM dual; ALTER SEQUENCE seq_id INCREMENT BY 10 MAXVALUE 200 NOCYCLE NOCACHE; その他の選択肢については次のとおりです。 ・キャッシュ値の変更はできないため ・サイクルの変更はできないため 順序の変更時、CACHE、CYCLEオプションの変更は可能です。変更できないオプションはSTART WITHオプションです。 ・...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_2012.htm#SQLRF00817

### 問題ID 26584 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26584?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文の実行結果として正しい記述はどれですか。 CREATE SEQUENCE seq_id MAXVALUE 100; CREATE TABLE emp ( id NUMBER(3) DEFAULT seq_id.NEXTVAL PRIMARY KEY, name VARCHAR2(10), hiredate DATE DEFAULT SYSDATE );
- 解説要約: Oracle 12cより、CREATE TABLE文やALTER TABLE文のデフォルト値にNEXTVAL疑似列とCURRVAL疑似列を指定できるようになりました。 ※Oracle 11gまでは、列のデフォルト値にNEXTVAL疑似列とCURRVAL疑似列を指定できませんでした。 NEXTVAL疑似列、CURRVAL疑似列は以下では使用できません。 ・SELECT文、UPDATE文、DELETE文内の副問合せ ・ビューのSELECT句 ・DISTINCTキーワードが指定されたSELECT文 ・GROUP BY句、ORDER BY句、HAVING句を持つSELECT文 ・集合演算子UNION、INTERSECT、MINUSによって別のSELECT文と結合されているSELECT文 ・SELECT文のWHERE句 ・CHECK制約の条件 以上より、 ・正常に表が作成される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE SEQUENCE seq_id MAXVALUE 100; CREATE TABLE emp ( id NUMBER(3) ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/NEWFT/chapter12101.htm#FEATURENO09966
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/pseudocolumns002.htm#sthref835

### 問題ID 26585 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26585?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 順序を削除するには、どのSQL文を実行しますか。
- 解説要約: 順序を削除するにはDROP SEQUENCE文を使用します。 以上より、 ・DROP SEQUENCE sqe_id; が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9001.htm

### 問題ID 26586 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26586?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 順序に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 順序はCREATE SEQUENCE文で作成し、ALTER SEQUENCE文で変更、DROP SEQUENCE文で削除します。 作成した順序から新しい順序値を取得したり、現在の順序値を確認するためには、NEXTVAL疑似列、CURRVAL疑似列を参照します。ただし、CURRVAL疑似列は、順序生成後に一度NEXTVAL疑似列を参照してから参照しなければなりません。 以上より、 ・順序を削除する場合は、DROP SEQUENCE文で削除する ・セッション開始後、CURRVAL疑似列を参照する前にNEXTVAL疑似列を参照しなければならない が正解となります。 その他の選択肢については次のとおりです。 ・順序は複数の表で共有できない 順序は表と関連付けられるものではないので、複数の表で1つの順序を使用できます。 ・キャッシュにある未使用の順序値は、クラッシュして再起動した後も使用できる 順序値がキャッシュされている状態の時にシステムがクラッシュすると、メモリ上にキャッシュされている順序値は失われてしまい、データベース再起動後も復帰はしません。そのため、順序値に欠番が生じることになります。...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/ADMIN/views.htm#i1106548
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/pseudocolumns002.htm#i1009336

### 問題ID 26587 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26587?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 索引の作成に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 索引には PRIMARY KEY制約やUNIQUE制約によってOracleが自動的に作成する一意索引と、ユーザが任意に作成する索引があります。 一意索引は、索引に指定した列または列の組合せに重複した値を持つ行がない場合に作成できる索引です。PRIMARY KEY制約やUNIQUE制約によって自動的に作成されるほか、CREATE UNIQUE INDEX文により作成することができます(ただし、索引に指定する列に重複した値が既に登録されていると、一意索引は作成できません)。 任意に索引を作成する場合、複数の列の組合せで索引を作成することもできます(「複合の索引」といいます)。また、PRIMARY KEY制約やUNIQUE制約が複数の列の組合せで指定された場合も、「複合の索引」となります。 以上より、 ・CREATE UNIQUE INDEX文で一意索引を作成できる ・CREATE INDEX文で複合の索引を作成できる ・PRIMARY KEY制約で一意索引を作成できる が正解となります。 その他の選択肢については以下の通りです。 ・UNIQUE制約で複合の索引を作成できない UNIQUE制...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_5012.htm#SQLRF01209

### 問題ID 26588 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26588?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 索引の削除に関する説明として、誤っているものはどれですか。
- 解説要約: PRIMARY KEY制約やUNIQUE制約によって自動的に作成された一意索引をDROP INDEX文で削除することはできません。PRIMARY KEY制約やUNIQUE制約を削除した時に自動的に削除されます。 以上より、 ・PRIMARY KEY制約で作成された索引をDROP INDEX文で削除できる が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8017.htm#SQLRF01510

### 問題ID 26589 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26589?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: SALES表の構造を確認して下さい。 SALES表のPROD_ID列、CUST_ID列、TIME_ID列の組み合わせに対してPRIMARY KEY制約が定義されています。 次のSQL文のうち、エラーとなるものはどれですか。
- 解説要約: SALES表のPROD_ID列、CUST_ID列、TIME_ID列の組み合わせに対してPRIMARY KEY制約が定義されているので、PROD_ID列、CUST_ID列、TIME_ID列の組み合わせに対して自動的に索引が作成されています。 既に索引が定義されている列や列の組合せに対して新しい索引を作成することはできません。 以上より、 ・CREATE INDEX ind1 ON sales (prod_id, cust_id, time_id); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE INDEX ind1 ON sales (prod_id, cust_id, time_id); なお、複数の列の組合せに対して索引が作成されている場合、列の組合せに対して新しい索引を作成することはできませんが、列の組合せの一部に新しい索引を作成することはできます。 SQLを表示 CREATE INDEX ind1 ON sales (prod_id, cust_id);
- 参考URL: なし

### 問題ID 26590 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26590?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: ユーザーAがCUSTOMERS表を所有しています。データベース管理者はユーザーBにユーザーAが所有するCUSTOMERS表のSELECT権限を付与しました。 ユーザーBが下記のようにCUSTOMERS表を参照できるようにシノニムを作成するための、実行者とSQL文の組合せとして正しいものはどれですか。 なお、ユーザーAにはCREATE SYNONYM権限が付与されています。 SELECT * FROM cust; 実行者： 1) データベース管理者 2) ユーザーA SQL文： a) CREATE SYNONYM cust FOR a.CUSTOMERS; b) CREATE PUBLIC SY...
- 解説要約: ユーザーが使用できるシノニムは、自身のスキーマに作成されたプライベートシノニムまたはパブリックシノニムのどちらかです。 設問では、ユーザーBがシノニムを使用した問合せを行うので、ユーザーBのプライベートシノニムまたはパブリックシノニムとしてCUSTシノニムが作成されなければなりません。 以上より、 ・実行者：1) SQL文：b) が正解となります その他の選択肢については次のとおりです。 ・実行者：1) SQL文：a) (データベース管理者が CREATE SYNONYM cust FOR a.CUSTOMERS; を実行) PUBLICの指定がないためデータベース管理者のプライベートシノニムが作成されます。そのためユーザーBがこのシノニムを利用することはできません。 ・実行者：2) SQL文：c) (ユーザーAが CREATE PUBLIC SYNONYM cust FOR CUSTOMERS; を実行) ユーザーAにCREATE PUBLIC SYNONYM権限は付与されていないため、パブリックシノニムを作成することはできません。 ・実行者：2) SQL文：d) (ユーザーAが C...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7001.htm#SQLRF01401

### 問題ID 26591 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26591?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: プライベートシノニムを削除するには、どのSQL文を実行しますか。
- 解説要約: プライベートシノニムを削除するにはDROP SYNONYM文を使用します。 DROP PUBLIC SYNONYM文はパブリックシノニムを削除します。 以上より、 ・DROP SYNONYM cust; が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9002.htm#SQLRF01805

### 問題ID 26592 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26592?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表に登録されている従業員のうち、最初に入社した従業員の入社日を表示するには、どの問合せを実行しますか。
- 解説要約: MAX関数やMIN関数の引数には、数値の他、文字列や日付値を指定することができます。 MAX関数の引数に日付値を指定すると、最も新しい(最近の)日付が、MIN関数の引数に日付値を指定すると、最も過去の日付が返されます。 設問では、最初に入社した従業員の入社日を求めるので、MIN関数でHIREDATE列の最も古い日付を取得します。 以上より、 ・SELECT MIN(hiredate) FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT MAX(hiredate) FROM employees; MAX(hiredate)は入社日の最大値を求めるので、最後に入社した従業員の入社日が表示されます。 ・SELECT SUM(hiredate) FROM employees; ・SELECT AVG(hiredate) FROM employees; SUM関数やAVG関数は引数に数値を指定します。文字列を指定することはできませんので、エラーとなります。 参考： MAX,MIN関数はそれぞ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions098.htm#i89072
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions100.htm#i1280029

### 問題ID 26593 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26593?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMP2表のSALARY列に、以下の3件のデータが格納されているとします。 100000, NULL, 500000 次のSQL文の実行結果として正しいものはどれですか。 SELECT AVG(salary) FROM emp2;
- 解説要約: グループ関数では、COUNT関数の引数に*(アスタリスク)が指定された場合を除き、NULL値を無視して集計処理を行います。 したがって、設問のAVG関数では、 (100000 + 500000) ÷ 2 の結果が返されます。 以上より、 ・300000が表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT salary FROM emp2; SELECT AVG(salary) FROM emp2; 参考： グループ関数では、COUNT関数に引数に*(アスタリスク)が指定された場合を除き、NULL値を無視して集計処理を行います。 SQLを表示 SELECT COUNT(*), COUNT(salary) FROM employees; AVG関数で平均を求める場合に集計するデータにNULL値が含まれていると、AVG関数はNULL値を除いたデータの平均値を返します。 SQLを表示 SELECT * FROM salary; SELECT AVG(sal) FROM salary; NULL値を含めた全件数で割った平均を求めたい場合は、...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203

### 問題ID 26594 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26594?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せの実行結果として、正しいものはどれですか。 SELECT prodid, name, category FROM prod WHERE category IN (SELECT category FROM oldprod);
- 解説要約: IN演算子はリスト内のいずれかの値と等しい場合にTRUEを返すため、IN演算子の値のリストにNULL値以外の値が含まれていて、その値と比較対象の値が等しければ、主問合せでデータが取り出されます。 設問のSQL文の副問合せでは"10","40","NULL"が返されますが、PROD表のCATEGORY列が"10","40"である行があるため、データが取り出されます。 なお、PROD表のCATEGORY列が"NULL"である行もありますが、NULL値同士を判定してもNULL値となり、値が等しいという判定ができないので、CATEGORY列が"NULL"である行は取り出されません。 以上より、 ・正常に実行され、PROD表のCATEGORY列の値が"10"と"40"の行が表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prodid, name, category FROM prod WHERE category IN (SELECT category FROM oldprod); 参考： WHERE句に指定された副問合せがNULL値を...
- 参考URL: なし

### 問題ID 26595 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26595?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: DEPARTMENTS表の構造を確認して下さい。 次のSQL文でDEPARTMENTS6表と順序を作成します。 [DEPARTMENTS6表] CREATE TABLE departments6 AS SELECT * FROM departments WHERE 1 = 0; [順序] CREATE SEQUENCE seq_dept; DEPARTMENTS6表にデータを追加するSQL文として、正しいものはどれですか。ただし、現在のセッションにおいて、作成した順序からまだ一度も順序値を取得していません。
- 解説要約: 順序から順序値を生成するにはNEXTVAL擬似列を参照します。また、最後に生成した順序値を参照するには、CURRVAL擬似列を参照します。 なお、CURRVAL擬似列は、現在のセッションで一度も順序値が生成されていない場合は参照することができません。NEXTVAL擬似列を参照して順序値を生成後、CURRVAL擬似列を参照します。 以上より、 ・INSERT INTO departments6 VALUES (seq_dept.NEXTVAL, 'Sales', 1001); が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・INSERT INTO departments6 VALUES (NEXTVAL, 'Sales', 1001); NEXTVAL擬似列は順序の名前で修飾し、seq_dept.NEXTVALのように参照しなければなりません。 ・INSERT INTO departments6 VALUES (seq_dept.CURRVAL, 'Sales', 1001); 現在のセッションでまだ一度も順序値を取得してい...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/pseudocolumns002.htm

### 問題ID 26596 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26596?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次の通りSQL文のうち、正常に実行されるものはどれですか。なお、PROD表のPRODID列にはPRIMARY KEY（重複値およびNULL値を許可しない）制約が定義されています。
- 解説要約: UPDATE文で列の値を更新する場合、更新する列に定義されている制約やデータ型を考慮する必要があります。 設問では、PRODID列にPRIMARY KEY制約が定義されているので、NULL値で更新したり複数の行で同じ値に更新することはできません。 また、制約が定義されていなくても、DATE型の列を数値や文字列で更新するなどデータ型が一致しない更新はできません。 以上より、 ・UPDATE prod SET startdate = NULL; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 UPDATE prod SET startdate = NULL; SELECT * FROM prod; その他の選択肢については次のとおりです。 ・UPDATE prod SET prodid = NULL WHERE prodid > 3; PRODID列にはPRIMARY KEY制約が定義されているため、NULL値で更新することはできません。 ・UPDATE prod SET startdate = 50 WHERE prodid = 3; STARTDATE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF01708

### 問題ID 26597 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26597?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 
- 解説要約: SELECT文の検索結果から重複した行を排除するには、SELECTキーワードの直後に1度だけDISTINCTキーワードを指定します。 以上より、 ・SELECT DISTINCT cust_id FROM sales; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT cust_id FROM sales; 重複を排除せずに、全ての行が取り出されます。 ・SELECT cust_id FROM DISTINCT sales; DISTINCTキーワードは表名の前ではなく、列名の前に指定します。このSQL文はエラーとなります。 ・SELECT cust_id DISTINCT FROM sales; DISTINCTキーワードは列名の後ろではなく、列名の前に指定します。このSQL文はエラーとなります。 参考： 重複した行を排除して検索結果を取り出すには、DISTINCTキーワードを使用します。 SELECT DISTINCT 項目1 [, 項目2, ... ] FROM 検索対象の表名; DISTINCTキーワー...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55272

### 問題ID 26598 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26598?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 
- 解説要約: データの件数を取得するには、COUNT関数を使用します。 COUNT関数でデータ件数の取得時、DISTINCTオプションを指定すると、重複した値は1度だけカウントされます。 設問では、商品を購入したことのある顧客の人数を求めるので、SALES表のCUST_ID列の値のうち、重複を排除した列の件数を求めれば良いことになります。 以上より、 ・SELECT COUNT(DISTINCT cust_id) FROM sales; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT DISTINCT COUNT(*) FROM sales; ・SELECT DISTINCT COUNT(cust_id) FROM sales; COUNT関数の結果に対してDISTINCTキーワードを指定しても、CUST_ID列の重複データを排除することはできません。 ・SELECT COUNT(DISTINCT *) FROM sales; *(アスタリスク)にDISTINCTオプションを指定することはできません。エラーとなります。 ・...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions039.htm#i82697

### 問題ID 26599 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26599?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表の全てのデータを削除するには、どのSQL文を実行しますか(該当するものをすべて選択してください)。
- 解説要約: 表の全てのデータを削除するには、DELETE文を削除する行の条件を指定せずに実行するか、TRUNCATE文を実行します。 DELETE文のFROMキーワードは省略が可能です。 以上より、 ・TRUNCATE TABLE prod; ・DELETE FROM prod; ・DELETE prod; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 TRUNCATE TABLE prod; SELECT * FROM prod; ROLLBACK; SELECT * FROM prod; SQLを表示 DELETE FROM prod; SELECT * FROM prod; ROLLBACK; SELECT * FROM prod; SQLを表示 DELETE prod; SELECT * FROM prod; その他の選択肢については次のとおりです。 ・TRUNCATE FROM prod; TRUNCATE文は、TRUNCATE TABLE 表名 のように記述します。 ・TRUNCATE TABLE prod WHERE prodid > 1; TRU...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF01505
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10007.htm#SQLRF01707

### 問題ID 26600 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26600?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 SELECT TO_NUMBER('-0.75', '0.99999') * 3 FROM dual;
- 解説要約: TO_NUMBER関数は文字列を数値へ変換し、数値データを返すため、返された数値を演算で使用することができます。 以上より、 ・正常に実行され、-2.25が表示される が正解となります。 設問のSQL文の実行結果は次のとおりです。 SQLを表示 SELECT TO_NUMBER('-0.75', '0.99999') * 3 FROM dual; その他の選択肢については次のとおりです。 ・TO_NUMBER関数の数値書式に-(マイナス)記号が指定されていないため、エラーとなる 数値書式で符号を指定する場合は「-」ではなく「S」を使用します。ただし、-(マイナス)記号は「S」の指定がなくても正常に動作します。 ・TO_NUMBER関数の結果を用いて演算を行うことはできないため、エラーとなる TO_NUMBER関数は数値を返すので、結果を演算で使用することができます。 ・正常に実行され、2.25が表示される TO_NUMBER関数は「-0.75」を返すので、演算結果は-2.25となります。 参考： TO_NUMBER関数は、文字列を指定された書式に従って数値に変換する関数です。 書式は以...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions211.htm#SQLRF06140
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34570

### 問題ID 26601 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26601?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のROUND関数の結果として、正しいものはどれですか。 ROUND(123.456789, 3)
- 解説要約: ROUND関数は引数で与えられた数値を四捨五入して返します。 2番めの引数に正の値が指定された場合、1番目の引数で与えられた数値が、小数点以下で2番目の引数の桁に丸められます。 設問では2番めの引数に3が指定されていますので、小数点4桁目が四捨五入され、小数点以下3桁に丸められます。 以上より、 ・123.457 が正解となります。 設問のROUND関数の実行結果は次のようになります。 SQLを表示 SELECT ROUND(123.456789, 3) FROM dual; 参考： ・ROUND関数は引数で与えられた数値を四捨五入します。 使用法は以下の通りです。 ROUND(数値 [, n]) 数値：四捨五入をする数値 n：小数点以下n桁に丸める 例) n=1 小数点2桁目で四捨五入され、小数点以下1桁に丸められる n=2 小数点3桁目で四捨五入され、小数点以下2桁に丸められる 2番目の引数は省略可能です。省略された場合は整数値に丸められます。 また、2番目の引数には負の値を指定することもできます。負の値が指定された場合は次のようになります。 例) n=-1 一の位で四捨五入される...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions155.htm#SQLRF00698

### 問題ID 26602 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26602?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認してください。 次の問い合わせのうち、エラーとならない問い合わせはどれですか(該当するものを全て選択して下さい)。
- 解説要約: SELECT文にGROUP BY句を指定しない場合、グループ関数を使用することはできますが、グループ関数をネストすることはできません。 また、GROUP BY句を指定しても、グループ関数は2レベルまでしかネストすることができません。 以上より、 ・SELECT MAX(salary), MIN(salary), AVG(salary) FROM employees; ・SELECT MAX(AVG(salary)) FROM employees GROUP BY department_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT AVG(MIN(salary)) FROM employees; グループ関数をネストする場合は、必ずGROUP BY句を指定しなければなりません。 ・SELECT AVG(MIN(MAX(salary))) FROM employees GROUP BY department_id, job_id; グループ関数はGROUP BY句を指定しても、2レベルまでしかネストでき...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203

### 問題ID 26603 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26603?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せを実行すると、何件のデータが返されますか。 SELECT prodid, name, category FROM prod WHERE category >=ALL (SELECT category FROM oldprod WHERE category < 50);
- 解説要約: ALL演算子はリスト内の全ての値が条件を満たす場合にTRUEをかえしますので、>=ALL(値のリスト)は比較する値がリスト内の全ての値と等しいか、大きい場合にTRUEを返します。 ALL演算子はリスト内の全ての値が条件を満たさなければTRUEにならないため、>=ALL(値のリスト)はリスト内の最大値以上場合にTRUEになるということです。 設問のSQL文では、副問合せからOLDPROD表のCATEGORY列の値である"10","40"が返されるので、主問合せではCATEGORY列の値が"10","40"の最大値である"40"以上の行がPROD表から取り出されます。 以上より、 ・2 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prodid, name, category FROM prod WHERE category >=ALL (SELECT category FROM oldprod WHERE category < 50); 参考： 複数行演算子には次のものがあります。 複数行演算子ANYとALLは必ず単一行演算子とセットで使...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#SQLRF52105

### 問題ID 26604 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26604?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せを実行すると、何件のデータが返されますか。 SELECT prodid, name, category FROM prod WHERE category <=ANY (SELECT category FROM oldprod WHERE category < 30);
- 解説要約: ANY演算子はリスト内のいずれかの値が条件を満たす場合にTRUEを返しますので、<=ANY(値のリスト)は比較する値がリスト内のいずれかの値と等しいか小さい場合にTRUEを返します。 ANY演算子はリスト内の値のうち1つでも条件を満す値があればTRUEとなるので、<=ANY(値のリスト)はリスト内の最大値以下の場合にTRUEとなるということです。 設問のSQL文では、副問合せからOLDPROD表のCATEGORY列の値が30以下である"10"が返されるので、主問合せではCATEGORY列の値が"10"であるデータのみが返されます。 以上より、 ・1 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prodid, name, category FROM prod WHERE category <=ANY (SELECT category FROM oldprod WHERE category < 30); 参考： 複数行演算子には次のものがあります。 複数行演算子ANYとALLは必ず単一行演算子とセットで使用しなければなりません。 また、I...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#SQLRF52105

### 問題ID 26605 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26605?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の図はPROD表とOLDPROD表を使用して複合問合せを行った結果です。 1) 2) 複合問合せに使用した演算子と結果の組合せとして正しいものはどれですか。 [演算子] a) UNION b) UNION ALL c) INTERSECT d) MINUS
- 解説要約: UNION ALL演算子による複合問合せの結果は、重複行もすべて表示されます。また、結果のソートは行われません。 UNION ALL演算子以外の演算子による複合問合せでは、結果に重複行が含まれる場合、重複行は排除され1つだけ表示されます。また、結果はSELECT句の一番目に指定した列の昇順にソートされます。 設問の図を見ると、 1) 結果に重複行が含まれるので、UNION ALL演算子による複合問合せ 2) 結果に重複行が含まれず、ソートされているので、UNION ALL演算子以外の演算子による複合問合せであることがわかります。PROD表、OLDPROD表のデータから、2つの表の問合せ結果から重複行を排除したものであることがわかるので、UNION演算子による問合せ であることがわかります。 以上より、 ・1) と b) ・2) と a) が正解となります。 それぞれの演算子を使用して複合問合せを行った結果は次の通りです。 a) SQLを表示 SELECT category FROM prod UNION SELECT category FROM oldprod; b) SQLを表示 S...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26606 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26606?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: NUMBER型の説明として、正しいものはどれですか。
- 解説要約: NUMBER型の値を定義する際、全体の桁数と位取りを指定します。 位取りは小数点以下の桁数のことで、全体の桁数のうち小数点以下の桁数がいくつであるかを指定します。 位取りに負の値が指定された場合は、整数部の丸める桁数を指定したとこになります。また、全体の桁数と位取りの両方が省略された場合は、最大精度の浮動小数点となります。 以上より、 ・データ型がNUMBER(3,-1)の列に123.45を入力すると、120が格納される ・データ型がNUMBERの列に12.345を入力すると、12.345が格納される が正解となります。 正解の選択肢の実行結果は次のようになります。 SQLを表示 CREATE TABLE temp2 (number1 NUMBER(3,-1), number2 NUMBER ); INSERT INTO temp2 VALUES (123.45, 12.345); SELECT * FROM temp2; その他の選択肢については次のとおりです。 ・データ型がNUMBER(5)の列に123.45を入力すると、123.45が格納される 位取りが省略されているので、少数点...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00222

### 問題ID 26607 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26607?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: SALES表の構造を確認して下さい。 SALES表をコピーしてSALES2表を作成するSQL文として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: 副問合せによる表の作成では、CREATE TABLE文に指定する列名の数と、副問合せのSELECT句に指定する列名(列別名)の数は同数にしなければなりません。CREATE TABLE文の列名を省略した場合は、副問合せのSELECT句に指定された列名または列別名と同名の列が定義されます。 また、副問合せのSELECT句に計算式や関数を指定する場合は、計算式や関数に列別名を指定するか、CREATE TABLE文で列名を指定しなければなりません。 計算式や関数に列別名が指定されておらず、かつCREATE TABLE文の列名も省略されているとエラーとなります。 以上より、 ・CREATE TABLE sales2 AS SELECT prod_id prod, cust_id cust, sysdate time FROM sales; ・CREATE TABLE sales2 AS SELECT * FROM sales WHERE 1 = 1; が正解となります。 2つ目の副問合せのWHERE句に指定された条件は 1 = 1 と必ず成立する条件ですので、条件無しの場合と同様に、全てのデータ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF54626

### 問題ID 26608 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26608?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: TIMESTAMP型の説明として正しいものはどれですか。
- 解説要約: TIMESTAMP型はDATE型を拡張したデータ型で、世紀、年、月、日、時、分、秒に加え秒の小数点以下の値を格納することができます。 TIMESTAMP型の列に値を格納するためには、日付リテラルを使用するか、文字列や数値をTO_TIMESTAMP関数でTIMESTAMP型の値に変換します。 以上より、 ・TIMESTAMP型は秒の小数点以下の値も格納できる が正解となります。 その他の選択肢については次のとおりです。 ・文字列からTIMESTAMP型への変換はできない TO_TIMESTAMP関数で文字列からTIMESTAMP型への変換ができます。 ・DATE型にTIMESTAMP型の値を格納できない 暗黙的データ変換により、TIMESTAMP型の値をDATE型の列へ格納することができます。 ・TIMESTAMP型には年、月、日の値は格納できない TIMESTAMP型には年、月、日のほか、時、分、秒、秒の小数点以下の値を格納することができます。 SQLを表示 CREATE TABLE timeTable (id NUMBER(2), date1 DATE, timestamp1 TIM...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00203

### 問題ID 26609 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26609?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のTO_NUMBER関数のうち、正常に実行できるものはどれですか。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・TO_NUMBER('123,456.789', '999D999D999') 数値書式「D」はピリオド(.)と同じく、指定された位置に小数点を返しますが、1つの書式の中で2つ以上指定することはできません。 設問の書式では「D」が2回指定されていますので、エラーとなります。 SQLを表示 SELECT TO_NUMBER('123,456.789', '999D999D999') FROM dual; ・TO_NUMBER('123.456789', '999D999G999') 数値書式「G」はカンマ(,)と同じく、指定された位置に桁区切り文字を返しますが、小数点よりも右側に指定することはできません。 設問の書式では、小数点を戻す「D」の右側に「G」が指定されていますので、エラーとなります。 SQLを表示 SELECT TO_NUMBER('123.456789', '999D999G999') FROM dual; ・TO_NUMBER('123.456789', '999.999') 数値書式「9」は数値の桁数の指定です。 設問の書式では、...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions211.htm#SQLRF06140
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34570

### 問題ID 26610 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26610?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 索引に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 索引は、作成後に変更することはできません。そのため、変更したい場合は、索引を削除後に再度作成しなければなりません。 なお、索引を作成した表自体を削除した場合、索引も一緒に削除されますが、索引を削除しても、対象の表は影響を受けません。 また、PRIMARY KEY制約やUNIQUE制約によって自動的に作成された一意索引をDROP INDEX文で削除することはできません。PRIMARY KEY制約やUNIQUE制約を削除した時に自動的に削除されます。 以上より、 ・索引の変更はできないので、内容を変更したい場合は索引をいったん削除してから再作成する必要がある ・表を削除すると、その表に設定された索引も削除される が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8017.htm#SQLRF01510

### 問題ID 26611 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26611?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: DEPARTMENTS表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE departments7 AS SELECT * FROM departments WHERE 1 = 0; CREATE SEQUENCE seq_dept START WITH 2; INSERT INTO departments7 VALUES (seq_dept.NEXTVAL, 'Sales', 1001); INSERT INTO departments7 VALUES (seq_dept.NEXTVAL, 'Sales', 1002); UPDATE...
- 解説要約: 順序から順序値を生成するにはNEXTVAL擬似列を参照します。また、最後に生成した順序値を参照するには、CURRVAL擬似列を参照します。 設問のSQL文ではsqe_deptという名前の順序を作成していますが、START WITHオプションを指定しているので、生成される順序の初期値は2となります。 最初のINSERT文では、MANAGER_ID列の値が1001である行を追加していますが、DEPARTMENT_IDの値に順序を使用しています。ここでは順序作成後、初めてNEXTVAL擬似列を参照しているので、DEPARTMENT_ID列の値は初期値の2をとなります。 次のINSERT文では、MANAGER_ID列の値が1002である行を追加していますが、ここでもDEPARTMENT_IDの値に順序を使用しています。NEXTVAL擬似列を参照しているので、次の順序値が返され、DEPARTMENT_ID列の値は3となります。 最後のUPDATE文では、MANAGER_ID列の値が1001である行のDEPARTMENT_ID列の値を次の順序値で更新しています。直前のINSERT文でNEXTVAL...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314
  - https://docs.oracle.com/cd/E96517_01/admin/managing-views-sequences-and-synonyms.html#GUID-50B77DCA-C44E-488C-B281-7478A01E842E

### 問題ID 26612 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26612?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: NEXTVAL擬似列、CURRVAL擬似列を参照することができない箇所はどれですか(該当するものを全て選択して下さい)。
- 解説要約: NEXTVAL擬似列、CURRVAL擬似列は以下の箇所で参照することができます。 ・主問合せのSELECT句 ・INSERT文の副問合せのSELECT句 ・INSERT文のVALUES句 ・UPDATE文のSET句 ・CREATE TABLE文またはALTER TABLE文の列のDEFAULT値 NEXTVAL擬似列、CURRVAL擬似列は以下では使用することはできません。 ・SELECT文、UPDATE文、DELETE文内の副問合せ ・ビューのSELECT句 ・DISTINCTキーワードが指定されたSELECT文 ・GROUP BY句、ORDER BY句、HAVING句を持つSELECT文 ・集合演算子UNION、INTERSECT、MINUSによって別のSELECT文と結合されているSELECT文 ・SELECT文のWHERE句 ・CHECK制約の条件 以上より、 ・ビューのSELECT句 ・SELECT文のWHERE句 ・GROUP BY句、ORDER BY句、HAVING句を持つSELECT文 ・DISTINCTキーワードが指定されたSELECT文 が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Sequence-Pseudocolumns.html#GUID-D438E28B-3E30-4B12-8D52-8DA5CFE2E0FF

### 問題ID 26613 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26613?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文で順序を生成します。 CREATE SEQUENCE s_dept INCREMENT BY 10 MAXVALUE 90 NOCYCLE; その後、次のSQL文を10回実行した結果として正しいものはどれですか。 SELECT s_dept.NEXTVAL FROM dual;
- 解説要約: CREATE SEQUENCE文のオプションは次の通りです。 設問のSQL文では、増分値が10、最大値が90、順序値が最大値に達した場合、順序値の生成を終了するというオプションが指定されています。 設問のSELECT文を10回繰り返すと、初期値が1(明示的に指定がない場合の初期値は1)で増分値が10ですので、順序値は91となり、オプションで指定した最大値より大きな値になってしまいます。順序値が最大値に達した場合、順序値の生成を終了するというオプションを指定しているので、順序値が最大値を超えた場合はエラーが発生します。 以上より、 ・エラーとなる が正解となります。 設問のSQL文の実行結果は次のとおりです。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314

### 問題ID 26614 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26614?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次の要件を満たす順序を作成するSQL文として、正しいものはどれですか。 ・初期値は1 ・増分は1 ・最大値は50 ・順序が最大または最小値に達した場合は、順序値の生成を終了する ・順序値をキャッシュする
- 解説要約: 順序を生成する際に指定可能なオプションは以下のとおりです。 オプションを明示的に指定しない場合の初期値は、 ・初期値は1 ・増分値は1 ・順序が最大または最小値に達した場合は、順序値の生成を終了する ・順序値をキャッシュする です。 設問の要件を満たすためには、最大値のみ指定すれば良いことになります。 以上より、 ・CREATE SEQUENCE s_dept MAXVALUE 50; が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314

### 問題ID 26615 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26615?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文の実行結果と同じ結果となるSQL文はどれですか。 SELECT department_id, department_name FROM departments WHERE department_id NOT IN (1, 3, 5);
- 解説要約: 設問のSQL文は、指定された条件により、DEPARTMENT_ID列の値が1，3，5以外の行が取り出されます。 これは、DEPARTMENT_ID列の値が1以外 かつ 3以外 かつ 5以外ということですので、AND演算子を使用して次のように置き換えることができます。 department_id NOT IN(1,3,5) → department_id != 1 AND department_id != 3 AND department_id != 5 以上より、 ・SELECT department_id, department_name FROM departments WHERE department_id != 1 AND department_id != 3 AND department_id != 5; が正解となります。 設問と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, department_name FROM departments WHERE department_id NOT IN (1, 3, 5); ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions013.htm#i1050801

### 問題ID 26616 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26616?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認してください。 以下の条件を全て満たすデータを検索します。どの問い合わせを使用しますか。 ただし、日付書式は「RR-MM-DD」とします。 1.名前(EMPLOYEE_NAME)に「田」と「藤」のどちらも含まれていないこと 2.入社日(HIREDATE)が2001年10月1日より前か、2007年4月1日以降であること 3.部署(DEPARTMENT_ID)が「総務(1)」と「開発(3)」以外であること
- 解説要約: まず、各条件の式を1つずつ確認してみましょう。 1.名前(EMPLOYEE_NAME)に「田」と「藤」のどちらも含まれていないこと 「a と b のどちらでもない」という条件は以下のように変換できます。 NOT(a OR b) = (NOT a) AND (NOT b) また、文字パターンに一致しない行を検索する場合は[NOT LIKE 文字]を使用できるので、 employee_name NOT LIKE '%田%' AND employee_name NOT LIKE '%藤%' と記述します。 2.入社日(HIREDATE)が2001年10月1日より前か、2007年4月1日以降であること [NOT BETWEEN 下限値 AND 上限値]を使用して、 hiredate NOT BETWEEN '01-10-01' AND '07-03-31' と記述します。 NOT BETWEEN演算子では下限値と上限値は含まれないため、2007年4月1日以降は、上限値に'07-03-31'と記述します。 3.部署(DEPARTMENT_ID)が「総務(1)」と「開発(3)」以外であること DE...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/About-SQL-Conditions.html#GUID-65B103FE-C00C-46A3-8173-A731DBF62C80

### 問題ID 26617 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26617?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: PROD表のデータを確認して下さい。 上記データから、次のような8桁のキャンペーンコードを生成するにはどのSQL文を使用しますか。
- 解説要約: キャンペーンコードを確認すると、NAME列の最初の2文字 + STARTDATE列から「-(ハイフン)」を取り除いた数字の組み合わせであることが分かります。以下の関数を使用できます。 SUBSTR(文字列, m[, n]) : 文字列のm番目からn文字分の文字列を返す REPLACE(文字列, 変更前文字列 [, 変更後文字列]) : 変更後文字列が省略された場合は、文字列から変更前文字列を削除した文字列を返す ただし、NAME列が「ELLE」の行は「El」と2文字目が小文字になっているため、INITCAP関数で先頭を大文字、2文字目以降を小文字に変換しなければなりません。 以上より、 ・SELECT SUBSTR(INITCAP(name), 1, 2) || REPLACE(startdate, '-') "Code" FROM prod WHERE name IS NOT NULL; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT SUBSTR(INITCAP(name), 1, 2) || REPLACE(startdate, '...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/operators003.htm#i997789
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions033.htm#i77004
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions074.htm#i77574

### 問題ID 26618 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26618?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PROMOTIONS表の構造を確認して下さい。 各プロモーションの期間(日数)を表示するレポートを作成します。 プロモーションの終了日(PROMO_END_DATE)がNULLだったら、「進行中」と表示します。 どのSQL文を使用しますか(該当するものを全て選択して下さい)。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT promo_name, NVL(promo_end_date - promo_begin_date, '進行中') status FROM promotions; NVL関数の第2引数には、第1引数と同じデータ型の値を指定しなければなりません。 promo_end_date - promo_begin_dateがNULLの場合に文字列「進行中」を表示しようとしていますが、promo_end_date - promo_begin_dateは数値のため、エラーとなります。 誤ったSQL文です。 SQLを表示 SELECT promo_name, NVL(promo_end_date - promo_begin_date, '進行中') status FROM promotions; ・SELECT promo_name, NVL2(promo_end_date - promo_begin_date, TO_CHAR(promo_end_date - promo_begin_date), '進行中') status FROM promot...
- 参考URL: なし

### 問題ID 26619 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26619?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PROMOTIONS表の構造とデータを確認して下さい。 各プロモーションの開始日(PROMO_BEGIN_DATE)と終了日(PROMO_END_DATE)が同じだったら、「同日終了」と表示します。 どの問合せを使用しますか(該当するものを全て選択して下さい)。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT promo_name, NVL(TO_CHAR(promo_end_date - promo_begin_date), '同日終了') status FROM promotions; TO_CHAR(promo_end_date - promo_begin_date)がNULL値の場合に、「同日終了」を表示します。演算の結果がNULL値になるのは、promo_end_dateまたはpromo_begin_dateがNULL値である場合です。したがって設問の条件とは違う結果が表示されます。 誤ったSQL文です。 SQLを表示 SELECT promo_name, NVL(TO_CHAR(promo_end_date - promo_begin_date), '同日終了') status FROM promotions; ・SELECT promo_name, NVL2(NULLIF(promo_begin_date, promo_end_date), NULL, '同日終了') status FROM promotions; NULL...
- 参考URL: なし

### 問題ID 26620 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26620?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 次の問合せに関して正しい記述はどれですか。 SELECT employee_name, salary FROM (SELECT * FROM employees ORDER BY salary DESC NULLS LAST) WHERE ROWNUM < 6;
- 解説要約: ROWNUM疑似列は、SQL問合せによって返される行について、Oracleが行を選択する順序を示す番号を返します。選択される最初の行のROWNUMは1、2番目の行のROWNUMは2、というように順番に番号が返されます。 例えば、次のようにWHERE句にROWNUM疑似列の条件を追加すると、問合せ結果を10行のみ表示するように行数を制限できます。 SELECT * FROM employees WHERE ROWNUM < 11; ORDER BY句を副問合せに組み込んでROWNUM条件を使用した場合、ORDER BY句で行をソートした後にROWNUM条件を適用でき、上位N番(Top N)のレポートを出力できます。 SELECT * FROM (SELECT * FROM employees ORDER BY employee_id) WHERE ROWNUM < 11; ※上位N番を問合せるには、インライン・ビュー(FROM句の副問合せ)とORDER BY句、ROWNUM疑似列が必要であることを覚えておきましょう。 なお、副問合せを使用せず通常のSELECT文でORDER BY句とRO...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/pseudocolumns009.htm

### 問題ID 26621 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26621?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: NEW_PRODUCTS表の構造とデータを確認して下さい。 以下の問合せと同じ結果になるSQL文はどれですか。 SELECT prod_name, prod_status FROM new_products MINUS SELECT prod_name, prod_status FROM new_products WHERE prod_status = '生産中止';
- 解説要約: MINUS演算子を用いた複合問合せでは、1つ目の問合せ結果から2つ目の問合せ結果にない行を表示します。 設問のSQL文では、2つ目の問合せで「PROD_STATUS列が'生産中止'である」という条件を指定しているので、1つ目の全件問合せからこの条件の行を排除した行、つまり「PROD_STATUS列が'生産中止'ではない」行が表示されます。 では選択肢を1つずつ確認してみましょう。 ・SELECT prod_name, prod_status FROM new_products UNION SELECT prod_name, prod_status FROM new_products WHERE prod_status = '生産中止'; UNION演算子を用いた複合問合せでは、2つの問合せの結果から重複行を排除して表示します。2つ目の問合せで「PROD_STATUS列が'生産中止'である」という条件を指定していますが、1つ目の全件問合せと重複した行を排除するだけなので、全ての行が表示されます。誤ったSQL文です。 ・SELECT prod_name, prod_status FROM ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26622 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26622?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PRODUCTS表とSALES表の構造を確認して下さい。 以下の問合せと同じ結果になるSQL文はどれですか。 SELECT prod_id FROM products INTERSECT SELECT prod_id FROM sales;
- 解説要約: INTERSECT演算子を用いた複合問合せでは、2つの問合せの結果の共通する行を表示します。また、重複した行は排除されます。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prod_id FROM products INTERSECT SELECT prod_id FROM sales; 選択肢を1つずつ確認してみましょう。 ・SELECT prod_id FROM products UNION SELECT prod_id FROM sales; UNION演算子を用いた複合問合せでは、2つの問合せの結果を連結し、重複行を排除して表示します。誤ったSQL文です。 ・SELECT prod_id FROM products MINUS SELECT prod_id FROM sales; MINUS演算子を用いた複合問合せでは、1つ目の問合せ結果から2つ目の問合せ結果にない行を表示します。誤ったSQL文です。 ・SELECT p.prod_id FROM products p JOIN sales s ON p.prod_id = s.prod_id; O...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55272

### 問題ID 26623 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26623?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: Oracle Databaseのデータ型の説明について、正しい組合せはどれですか(該当するものを全て選択して下さい)。
- 解説要約: Oracle Databaseには、多くの組込みデータ型が用意されています。 選択肢を1つずつ確認してみましょう。 ・BFILE型 : OS上のバイナリファイルのポインタ情報のみを格納する BFILE型は最大4GBまでのバイナリデータを格納できる、読み取り専用のデータ型です。データはOracleのデータファイル内ではなく、OS上にバイナリファイル(動画やイメージ)として格納され、ファイルに対するポインタ情報のみが格納されます。 正しい選択肢です。 ・CLOB型 : 2GBまでの文字データを格納できる CLOB型は最大4GBまでの文字データを格納できます。2GBまでの文字データを格納できるのはLONG型です。 誤った選択肢です。 ・INTERVAL YEAR TO MONTH型 : 期間を日、時、分、秒の単位で格納する INTERVAL YEAR TO MONTH型は、期間を年、月の単位で格納します。期間を日、時、分、秒の単位で格納するのはINTERVAL DAY TO SECOND型です。 誤った選択肢です。 ・NUMBER型 : 負の数も格納できる NUMBER型には正と負の数値を格...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i54330

### 問題ID 26624 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26624?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: ROWID型の説明として、正しいものはどれですか。
- 解説要約: ROWID型は、行の一意なアドレスであるROWID疑似列(実際には列として定義されていない列)から返される値を列に格納するために使用する、BASE64文字列のデータ型です。 以上より、 ・行の一意なアドレスを表すBASE64文字列 が正解となります。 表にはROWID列の定義はありませんが、SELECT句にROWID疑似列を指定すると、各行の一意なアドレスを確認できます。 SQLを表示 SELECT department_id, department_name, rowid FROM departments; その他の選択肢については次のとおりです。 ・行の一意なアドレスを表すバイナリデータ ROWID型は行の一意なアドレスを表すBASE64文字列です。 ・4GBまでのバイナリデータを格納できる BLOB型の説明です。 ・表の1つの列にしか定義できない LONG型の説明です。ROWID型を2つ以上指定した表を作成できます。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i54330

### 問題ID 26626 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26626?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: USER_CONS_COLUMNSビューの説明として、正しいものはどれですか。
- 解説要約: USER_CONS_COLUMNSビューは、ビューにアクセスするデータベースユーザーが所有していて、制約が定義されている列を表示するデータ・ディクショナリ・ビューです。 データ・ディクショナリ・ビューとは、データベース内のオブジェクトやユーザー、権限などに関する様々な情報が格納されているが直接アクセスできないデータ・ディクショナリ表を参照するためのものです。 以上より、 ・ユーザー所有の、制約が定義されている列を表示する が正解となります。 その他の選択肢については以下のとおりです。 ・ユーザーがアクセスできる、制約が定義されている全ての列を表示する ALL_CONS_COLUMNSビューの説明です。 ・ユーザー所有の表の制約を表示する USER_CONSTRAINTSビューの説明です。 ・ユーザーがアクセスできる表の制約を表示する ALL_CONSTRAINTSビューの説明です。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56311/statviews_5257.htm#sthref2843

### 問題ID 26627 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26627?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューに対して設定できるオブジェクト権限はどれですか(該当するものを全て選択して下さい)。
- 解説要約: 他のデータベースユーザーが所有しているオブジェクトに対して何ができるかを設定するのが、オブジェクト権限です。 オブジェクト権限をユーザーやロール(複数の権限をまとめたもの)に付与するには、次の構文を使用します。 GRANT オブジェクト権限名 ON オブジェクト名 TO ｛ユーザー名 | PUBLIC | ロール名｝ ビューには、以下のオブジェクト権限を設定できます。 SELECT :データを検索する権限 UPDATE :データを更新する権限 INSERT :データを挿入する権限 DELETE :データを削除する権限 REFERENCES :参照整合性制約を作成する権限 以上より、 ・SELECT ・UPDATE ・INSERT ・DELETE ・REFERENCES が正解となります。 ALTER(表や順序を変更する権限)もオブジェクト権限ですが、ビューには設定できません。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9013.htm#i2155015

### 問題ID 26628 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26628?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 給与の高い順に、上位15%の従業員の情報を表示します。SALARY列に値が入っていない従業員は表示しません。 どの問合せを使用しますか。
- 解説要約: Oracle 12cより、SELECT文の問合せ結果として返される行数を制限できる機能、row_limiting_clause(行制限の条件)が加わりました。これにより、例えば上位10番目から20番目のデータを簡単に取り出せます。 row_limiting_clauseのFETCH句は返される行数、または行の割合を指定して、SELECT文の結果として返される行数を制限します。 FETCH { FIRST | NEXT } { 返される行数 | 返される行の割合 PERCENT } { ROW | ROWS } { ONLY | WITH TIES } 設問では給与の高い順に15%という条件ですので、まずORDER BY句でSALARY列を降順(DESC)にソートしますが、その際NULL値の行が先頭に表示されないようにNULLS LAST句を記述します。 ソートした後、FETCH句で15%を指定します。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees ORDER BY salary DESC NULLS LA...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_10002.htm#BABHFGAA

### 問題ID 26629 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26629?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の書式でデータを出力するにはどのSQL文を使用しますか。
- 解説要約: Oracle Database 11gリリース2から使用可能なLISTAGG関数は、複数行の列の値を連結して1行で表示できる関数です。 LISTAGG(連結して表示する列名 [, 'デリミタ']) WITHIN GROUP(ORDER BY ソートする項目 [ASC | DESC]) 設問では、PROD_CATEGORYごとのPROD_NAME列の一覧を「, 」で区切って表示しています。 以上より、 ・SELECT prod_category, LISTAGG(prod_name, ', ') WITHIN GROUP (ORDER BY prod_category) products FROM new_products GROUP BY prod_category; が正解となります。 その他の選択肢については次のとおりです。 ・SELECT prod_category, LISTAGG(prod_name, ', ') products FROM new_products GROUP BY prod_category; WITHIN GROUPキーワードがないためエラーとなります。...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions101.htm

### 問題ID 26630 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26630?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: NEW_PRODUCTS表の構造を確認して下さい。 同じ価格の製品が複数ある場合、その製品名と価格を検索して表示します。 目的の結果を得るには、どの問合せを使用しますか(2つ選択して下さい)。
- 解説要約: 設問のような条件を1つのSQL文で問合せるには、自己結合もしくは副問合せを使用します。 選択肢を1つずつ確認してみましょう。 ・SELECT DISTINCT p1.prod_name, list_price FROM new_products p1 JOIN new_products p2 USING (list_price) WHERE p1.prod_name <> p2.prod_name ORDER BY 2; USING句を使用した自己結合で、同じ価格で且つ製品名が違う行を検索し、DISTINCT句で冗長な行を省いています。正しいSQL文です。 ・SELECT DISTINCT p1.prod_name, p2.list_price FROM new_products p1, new_products p2 WHERE p1.prod_name <> p2.prod_name ORDER BY 2; Oracle独自の結合構文による自己結合ですが、WHERE句に結合条件(p1.list_price = p2.list_price)を記述していないため、行の全ての組合せのデカ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries006.htm#sthref2428
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries007.htm#i2067858

### 問題ID 26631 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26631?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 1つのSQL文で実行するために、副問合せまたは結合を使用しなければならない問合せはどれですか(2つ選択して下さい)。
- 解説要約: 選択肢の問合せをSQL文にすると、それぞれ次のようになります。 ・部署が3の部署の最高給与を表示する SELECT MAX(salary) FROM employees WHERE department_id = 3; ・｢山口洋子｣と同じ部署の従業員を表示する SELECT department_id, employee_name FROM employees WHERE department_id = (SELECT department_id FROM employees WHERE employee_name = '山口洋子'); ・給与が40万円以上の従業員の平均給与を表示する SELECT AVG(salary) FROM employees WHERE salary >= 400000; ・従業員とその上司の名前を表示する SELECT e.employee_name, m.employee_name FROM employees e LEFT OUTER JOIN employees m ON e.manager_id = m.employee_id; ・入社日が200...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries006.htm
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries007.htm#i2067858

### 問題ID 26632 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26632?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表から、上司のいる従業員の名前を表示します。 どの問合せを使用しますか(2つ選択して下さい)。
- 解説要約: EXISTS演算子は、副問合せの結果が1行以上返される場合にTRUEとして評価される演算子です。 主問合せのWHERE句に列名と比較演算子を指定する代りに、EXISTS演算子を指定します。 WHERE EXISTS (副問合せ) EXISTS演算子で設問の結果を得るには、主問合せで取り出したEMPLOYEES表 e の各行に対して副問合せを実行し、EMPLOYEES表 m のEMPLOYEE_ID列にMANAGER_ID列と同じ値があればTRUEを返し、上司がいる従業員として主問合せの行を表示します。 このSQL文はIN演算子を使用したSQL文にも置き換えられます。 以上より、 ・SELECT e.employee_name FROM employees e WHERE EXISTS (SELECT * FROM employees m WHERE e.manager_id = m.employee_id); ・SELECT employee_name FROM employees WHERE manager_id IN (SELECT employee_id FROM employe...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/conditions013.htm#i1051145

### 問題ID 26633 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26633?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: Oracle Databaseが管理するデータベースモデルは何ですか。
- 解説要約: データベースには大きく分けて3つの種類があります。 ・階層型 ・ネットワーク型 ・リレーショナル型 Oracle Databaseはリレーショナル型データベースを管理するためのソフトウェアです。 リレーショナル・データベース管理システム(RDBMS)と呼ばれます。 以上より、 ・リレーショナル型データベース が正解となります。 その他の選択肢については以下のとおりです。 ・階層型データベース ・ネットワーク型データベース Oracle Databaseが管理するのはリレーショナル型データベースなので、誤りです。 ・サークル型データベース このようなデータベースモデルはありません。
- 参考URL:
  - https://www.oracle.com/jp/technical-resources/articles/introductory-database-seminar.html#p01d

### 問題ID 26635 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26635?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEE_IDが「1008」の従業員と上司が同じである従業員の名前と、上司のEMPLOYEE_IDを出力します。 どの問合せを使用しますか(2つ選択して下さい)。
- 解説要約: EMPLOYEE_IDが「1008」の従業員と上司が同じである従業員、つまり「1008」の同僚を求める問題です。1つのSQL文で問合せるには、自己結合と副問合せを使用します。 まず、自己結合の方ですが、EMPLOYEE_IDが「1008」の従業員データのEMPLOYEES表 e と、同僚データのEMPLOYEES表 m があると見立てます。上司が同じであるという条件ですので、ON句には「e.manager_id = m.manager_id」という結合条件を指定します。 ※自己結合の例は通常、従業員データのEMPLOYEES表 e と上司データのEMPLOYEES表 m を見立てることが多いため、結合条件を「e.manager_id = m.employee_id」と間違えないようご注意ください。 JOIN句については、上記の結合条件の表 e と m には片方の表にしかない行が存在しないため、LEFT OUTER JOINとRIGHT OUTER JOINのどちらの外部結合でも、また、内部結合のJOIN句でも結果は同じです。両表に共通の行だけ取り出します。 次に副問合せの方は、副問合せ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries006.htm#sthref2428
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries007.htm#i2067858

### 問題ID 26636 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26636?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: ERモデルの構成要素はどれですか(該当するものを3つ選択して下さい)。
- 解説要約: ERモデル(Entity-Relationship Model)は、管理対象を「エンティティ(実体)」、「アトリビュート(属性)」、「リレーションシップ(関連)」という3つの構成要素で表現した概念データモデルです。主に「データベースにどのような表を作成するか」といった、リレーショナル・データベースの設計において使用されています。 以上より、 ・エンティティ ・アトリビュート ・リレーションシップ が正解となります。 以下に、ERモデルの要素とリレーショナル・データベースの対応を示します。 ・エンティティ(実体): 表 ・アトリビュート(属性): 列、主キー列 ・リレーションシップ(関連): 外部キー その他の選択肢については以下のとおりです。 ・リレーショナル・データベース データを行と列からなる2次元の表形式で格納するデータベースです。ERモデルの構成要素ではないので、誤りです。 ・フィールド リレーショナル・データベースで行と列が交差する値を格納する部分です。ERモデルの構成要素ではないので、誤りです。
- 参考URL:
  - https://www.otsuka-shokai.co.jp/words/e-r-model.html

### 問題ID 26637 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26637?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: EXAM表の構造を確認して下さい。 1つのSQL文で複数の行をEXAM表に追加するにはどのSQL文を使用しますか。
- 解説要約: マルチテーブル・インサートは、1つのSQL文で複数の表にデータを追加できる機能です。 通常のINSERT文では1文につき1行ずつ挿入しますが、マルチテーブル・インサートでは副問合せで返される複数の行を1つ以上の表に挿入できます。無条件のマルチテーブル・インサートと、条件付きのマルチテーブル・インサートがあります。 ・無条件のマルチテーブル・インサート INSERT文では1文につき1行ずつ挿入しますが、INSERT ALL文では1文でまとめて複数の行を挿入できます。 INSERT ALL INTO 表名[(列名1 [, 列名2 ...])] VALUES (値1 [, 値2 ...]) INTO 表名[(列名1 [, 列名2 ...])] VALUES (値1 [, 値2 ...]) [INTO 表名[(列名1 [, 列名2 ...])] VALUES (値1 [, 値2 ...])] SELECT 列名1 [, 列名2...] FROM 表名2 [WHERE 条件]); 以上より、 ・INSERT ALL INTO exam VALUES (1, 75, 60, 82) INTO ex...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/INSERT.html#GUID-903F8043-0254-4EE9-ACC1-CB8AC0AF3423__GUID-A375FB35-7EE9-4FF3-98BD-E58087EA1C6E

### 問題ID 26638 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26638?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: STUDENTS表とNEW_STUDENTS表の構造とデータを確認して下さい。 次の問合せの実行結果はどうなりますか。 MERGE INTO students s USING new_students n ON (s.student_id = n.student_id) WHEN MATCHED THEN UPDATE SET s.name = n.name DELETE WHERE (n.name IS NULL) WHEN NOT MATCHED THEN INSERT VALUES (n.student_id, n.name);
- 解説要約: MERGE文は異なる表の行をマージできるDML文です。1つのMERGE文で、該当する行があればUPDATE、無ければINSERTというように、行の挿入と更新を同時に行えます。 例えば、同じ構造の2つの表のデータを同期する場合に使用できます。 MERGE文の書式は参考をご参照ください。 設問のSQL文について説明します。 MERGE INTO students s USING new_students n ON (s.student_id = n.student_id) WHEN MATCHED THEN UPDATE SET s.name = n.name DELETE WHERE (n.name IS NULL) WHEN NOT MATCHED THEN INSERT VALUES (n.student_id, n.name); ・WHEN MATCHED THEN STUDENTS表とNEW_STUDENTS表のSTUDENT_ID列が一致した場合（STUDENTS表に既にデータが存在する場合）に実行されます。 UPDATE文では、STUDENT_ID列が2つの表に共通する「1」...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/MERGE.html#GUID-5692CCB7-24D9-4C0E-81A7-A22436DC968F

### 問題ID 26639 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26639?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を順番に実行しました。 CREATE GLOBAL TEMPORARY TABLE temp ( temp_id NUMBER(2), temp_name VARCHAR2(20) ) ON COMMIT DELETE ROWS; INSERT INTO temp VALUES (1, 'tempA'); COMMIT; この後の説明として正しい記述はどれですか。
- 解説要約: 設問のGLOBAL TEMPORARY句ではグローバル一時表（セッション終了後も表の構造を保持する）を作成しています。一時表は、トランザクションを終了またはセッションを切断するまでの間のみデータを保持する表です。一時表に挿入したデータはそのセッション内でのみ参照できます。 ON COMMIT DELETE ROWS句はトランザクション終了時にデータを削除（TRUNCATE）します。 TEMP表を作成した後はINSERT文で1件のデータを登録していますが、その後のCOMMIT文でトランザクションは終了し、データは削除されます。 以上より、 ・TEMP表のデータは0件である が正解です。 以下はSQL文の実行例です。 SQLを表示 CREATE GLOBAL TEMPORARY TABLE temp (temp_id NUMBER(2), temp_name VARCHAR2(20)) ON COMMIT DELETE ROWS; INSERT INTO temp VALUES (1, 'tempA'); SELECT * FROM temp; COMMIT; SELECT * FROM ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/tables-and-table-clusters.html#GUID-096986C4-9AD7-401D-BA6D-EF6CD4B494FE
  - https://atmarkit.itmedia.co.jp/fdb/ref/ref_oracle/table.html

### 問題ID 26640 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26640?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 外部表の説明として正しい記述はどれですか。
- 解説要約: 外部表は、データベース外部のファイルに格納されたデータにアクセスするための仕組みです。データベースには外部表の情報を記述するメタデータのみ格納されます。 以上より、 ・データベース外部のファイルに格納されたデータにアクセスできる が正解です。 外部表は作成した時点でデータを問い合わせることができ、SQL*Loaderのように外部ファイルのデータを実表にロードする必要はありません。 以下は外部表の作成例です。 SQLを表示 CREATE TABLE ext1 ( id NUMBER(4), text VARCHAR2(10)) ORGANIZATION EXTERNAL ( TYPE ORACLE_LOADER DEFAULT DIRECTORY ext_data ACCESS PARAMETERS ( RECORDS DELIMITED BY NEWLINE FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ( id, text) ) LOCATION ('ext1.csv') ); SELECT * FROM ext1; その他の...
- 参考URL:
  - https://docs.oracle.com/cd/E82638_01/admin/managing-tables.html#GUID-F6948F0E-0557-4C42-9145-1897DE974CC3

### 問題ID 26641 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26641?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: オブジェクト権限に関する説明として、正しいものはどれですか(3つ選択して下さい)。
- 解説要約: オブジェクト権限は、特定のデータベース・オブジェクトへの操作を許可するための権限です。 主なオブジェクト権限は次のとおりです。 オブジェクト権限は管理者ユーザー、または、オブジェクトの所有者が付与します。 オブジェクト権限は対象となるオブジェクトによって、付与できる権限が異なります。 権限の付与時にWITH GRANT OPTION句を指定すると、オブジェクト権限を付与されたユーザーが他のユーザーに対してオブジェクト権限を付与できるようになります。 なお、オブジェクトの所有者はオブジェクト権限を明示的に付与しなくても自分のオブジェクトに対する操作を行えます。 以上より、 ・オブジェクトの種類によって付与できる権限が異なる ・WITH GRANT OPTION句で、付与された権限を他のユーザーに付与できる ・オブジェクトの所有者はオブジェクト権限が付与されていなくてもオブジェクトを参照できる が正解となります。 その他の選択肢については次のとおりです。 ・オブジェクト権限を付与できるのは管理者ユーザーだけである オブジェクト権限は管理者ユーザー、またはオブジェクトの所有者が付与できます。...
- 参考URL: なし

### 問題ID 26642 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26642?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: ロールに関する説明として、正しいものはどれですか(2つ選択して下さい)。
- 解説要約: ロールとは、複数の権限を1つにまとめて名前を付けたものです。 複数のユーザーに複数のシステム権限（特定のデータベース操作を許可するための権限）やオブジェクト権限（特定のデータベース・オブジェクトへの操作を許可するための権限）を1つ1つ付与するのは大変ですし、管理も煩雑になります。そこで、必要な権限をロールとしてまとめておき、ロールをユーザーに付与することで権限を容易に管理できます。ユーザーに付与したロールに対して権限を追加したり、ロールから権限を削除した場合、ロールを付与されている全てのユーザーにロールの変更が影響します。 ロールにはシステム権限、オブジェクト権限、他のロールを含めることができます。ロールを付与されたユーザには、ロールに含まれている全ての権限が付与されます。 以上より、 ・複数のユーザーの権限を管理できる ・ロールをユーザーおよびロールに付与できる が正解です。 その他の選択肢については以下のとおりです。 ・ロールにシステム権限を付与することはできない ・ロールにオブジェクト権限を付与することはできない ・ロールに他のロールを付与することはできない ロールにはシステム権...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html

### 問題ID 26643 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26643?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: データ・ディクショナリの説明として正しいものはどれですか。
- 解説要約: データ・ディクショナリはデータベースに関する様々な管理情報が格納された読取り専用の表の集合です。データベース・オブジェクトやユーザーの定義、権限などの情報が含まれており、DDL文の実行時にOracle Databaseによって更新されます。 以上より、 ・データベース・オブジェクトやユーザー、権限などの管理情報が格納されている が正解です。 その他の選択肢については以下のとおりです。 ・データベースの管理情報をSQL文で参照するためのビューである データ・ディクショナリ表のデータを参照するためのデータ・ディクショナリ・ビューの説明です。データ・ディクショナリは表なので、誤りです。 ・SYSユーザーが定期的に表のデータを更新する DDL文の実行時にOracle Databaseによって更新されるので、誤りです。 ・データ・ディクショナリの所有者はSYSTEMユーザーである データ・ディクショナリはSYSユーザーによって所有され、SYSTEM表領域（管理情報が格納されている論理的な記憶領域）に格納されているので、誤りです。 ・一般ユーザーがアクセスできる 一般ユーザーはアクセスできないので...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/data-dictionary-and-dynamic-performance-views.html#GUID-BDF5B748-EB43-4B48-938E-89099069C3BB

### 問題ID 26644 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26644?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: CREATE DATABASE時にTIME_ZONE句に指定したデータベースのタイム・ゾーンを返す関数はどれですか。
- 解説要約: タイム・ゾーンとは同じ標準時（基準時刻との差）を扱う地域のことで、データベースにおいてはシステム運用の標準時を設定する項目です。 以下はデータベースのタイム・ゾーンや日時を返す関数です。 DBTIMEZONEは、CREATE DATABASE時やALTER DATABASE時にTIME_ZONE句に指定したタイム・ゾーンです。デフォルト値は日本語環境でも「+00:00」になっています。 SQLを表示 SELECT DBTIMEZONE FROM dual; 以上より、 ・DBTIMEZONE が正解です。 タイム・ゾーンには「+09:00」のようなUTC（Coordinated Universal Time：協定世界時）との時間差（オフセット）か、「Asia/Tokyo」のようなタイム・ゾーン地域名を設定します。 その他の選択肢については上表をご確認ください。 なお、DB_TIMEZONEという関数はありません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/DBTIMEZONE.html#GUID-F2368F72-7065-462F-80B9-E115F5A48025

### 問題ID 26645 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26645?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表の構造を確認してください。 SALARY列に12を掛け年収を求めます。求めた年収を以下の形式で表示させるためには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。
- 解説要約: SQL文の実行結果に表示される列見出しを変更したい場合は、SELECT句に列別名を指定します。列別名は算術式にも指定できます。 列別名は項目名と列別名をスペースで区切るか、明示的にASキーワードで指定します。 列別名はオブジェクトのネーミング規則に従って命名されますが、大文字と小文字を区別したり、ネーミング規則に反する列別名(スペースを使用するなど)を使用する場合は、列別名を二重引用符(")で囲まなければなりません。 設問の問合せ結果の列見出しは、大文字と小文字が使用されており、さらにスペースも使用されているので、"(二重引用符)で列別名を囲んで指定したことがわかります。 以上より、 ・SELECT salary * 12 AS "Yearly Income" FROM employees; ・SELECT salary * 12 "Yearly Income" FROM employees; が正解となります。 設問のSELECT文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT salary * 12 AS Yearly Income F...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55280
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements008.htm#i27570
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/ap_keywd001.htm#BABCJAEB

### 問題ID 26646 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26646?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表SALARY列(月給)とCOMMISSION列(歩合給)から従業員の年収を求めるSQL文として、正しいものはどれですか(該当するものを全て選択してください)。 ただし、年収は月給の12ヶ月分に歩合給を足したものとします。
- 解説要約: 算術式で複数の演算子を用いた計算を行う場合は、演算子の優先順位に従って計算が行われます。 演算子の優先順位は次の通りです。 同じ優先順位の演算子が複数使われている場合は、左側の計算から順番に行われます。 また、()括弧を用いることで優先順位が高くなります。 設問ではSALARY列の12倍の値にCOMMISSION列を加算するということですので、salary*12が先に計算される算術式が正解となります。 以上より、 ・SELECT commission + salary * 12 FROM employees; ・SELECT commission + ( salary * 12 ) FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 この場合、乗算（*）の方が加算（+）より元から優先順位が高いので、()括弧の有無は計算結果に影響しません。 その他の選択肢中の算術式については以下のとおりです。 ・salary * ( 12 + commission ) ()括弧により 12 + commission が先に計算されるので期待通りの結果にはな...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/operators002.htm#i1028549

### 問題ID 26647 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26647?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 列別名を指定したSQL文のうち、エラーが無く実行されるのはどのSQL文ですか(該当するものをすべて選択してください)。
- 解説要約: SQL文の実行結果に表示される列見出しを変更したい場合は、SELECT句に列別名を指定します。列別名は算術式にも指定することができます。 列別名は項目名と列別名をスペースで区切るか、明示的にASキーワードで指定します。 列別名はオブジェクトのネーミング規則に従って命名されますが、大文字と小文字を区別したり、ネーミング規則に反する列別名(スペースを使用するなど)を使用する場合は、列別名を二重引用符(")で囲まなければなりません。 以上より、 ・SELECT employee_name 従業員名, salary 給与 FROM employees; ・SELECT employee_name "Employee Name", salary AS Salary FROM employees; ・SELECT employee_name, salary "Salary($)" FROM employees; が正解となります。 正解のSQL文の実行結果はそれぞれ次のようになります。 SQLを表示 SELECT employee_name 従業員名, salary 給与 FROM employe...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55280
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements008.htm#i27570
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/ap_keywd001.htm#BABCJAEB

### 問題ID 26648 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26648?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 製品名に文字列「LED_」が含まれている製品を検索する条件として正しいものはどれですか。
- 解説要約: LIKE演算子を使用すると、指定した文字パターンに一致した行を検索できます。 文字パターンには、任意の1文字と一致する「_」や、0文字以上の任意の文字列と一致する「%」といった、ワイルドカードを利用できます。 ワイルドカードをリテラルの一部として使用する場合は、ESCAPEオプションを指定してワイルドカードをリテラルとして扱えるようにしなければなりません。 設問では「LED_」が含まれている行を検索するので、文字パターンは'%LED_%'となりますが、文字パターンに「_」が含まれているので、ESCAPEオプションを指定して「_」をリテラルとして扱う必要があります。 以上より、 ・WHERE prod_name LIKE '%LED\_%' ESCAPE '\' が正解となります。 ここではエスケープ文字として「\」を指定しています。（日本語環境では「¥」と表示されます。） 設問の検索条件でPRODUCTS表を検索すると次のようになります。 SQLを表示 SELECT prod_name FROM products WHERE prod_name LIKE '%LED\_%' ESCAP...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions007.htm#i1034153

### 問題ID 26649 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26649?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次の条件式で検索できる商品名はどれですか(該当するものを全て選択して下さい)。 WHERE prod_name LIKE '_i%LEDW_%ライト%' ESCAPE 'W'
- 解説要約: LIKE演算子を使用すると、指定した文字パターンに一致した行を検索できます。 文字パターンには、任意の1文字と一致する「_」や、0文字以上の任意の文字列と一致する「%」といった、ワイルドカードを利用できます。 ワイルドカードをリテラルの一部として使用する場合は、ESCAPEオプションを指定してワイルドカードをリテラルとして扱えるようにしなければなりません。 設問では「W」がエスケープ文字として指定されています。ですので「W」の直後に来るワイルドカードは、通常のリテラルとして扱われます。 '_i%LEDW_%ライト%' 設問の文字パターンでは、2つ目の「_」がワイルドカードでは無く、文字のアンダーバーとして扱われます。 この文字パターンは、以下のような文字列を表します。 ・1文字目 任意の1文字 ・2文字目 「i」 ・任意の文字列（0文字でも可） ・「LED_」という文字列 ・任意の文字列（0文字でも可） ・「ライト」という文字列 ・任意の文字列（0文字でも可） 以上より、 ・Light_LED_ハンディライト(6球) ・HighPower_LED_ハンディライト2 ・Silver LE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions007.htm#i1034153

### 問題ID 26650 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26650?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: CUSTOMERS表の構造を確認して下さい。 CUSTOMERS表の顧客名を検索します。苗字（cust_last_name）の2文字目が「藤」である顧客を検索するには、どの問い合わせを実行しますか。
- 解説要約: LIKE演算子を使用すると、指定した文字パターンに一致した行を検索できます。 文字パターンには、任意の1文字と一致する「_」や、0文字以上の任意の文字列と一致する「%」といった、ワイルドカードを利用できます。 設問では2文字目が「藤」である行を検索するので、文字パターンはまず'_藤'となりますが、苗字は2文字とは限りませんので「藤」の後に0文字以上の任意の文字列を表す「%」を付加します。 以上より、 ・SELECT customer_id, cust_last_name || ' ' || cust_first_name FROM customers WHERE cust_last_name LIKE '_藤%'; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT customer_id, cust_last_name || ' ' || cust_first_name FROM customers WHERE cust_last_name = '_藤%'; 文字パターンを指定するにはLIKE演算子を使用しま...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions007.htm#i1034153

### 問題ID 26651 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26651?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: PRODUCTS表の製品名に「HITS_」と「's」が順番で含まれている行を検索する条件として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: LIKE演算子を使用すると、指定した文字パターンに一致した行を検索できます。 文字パターンには、任意の1文字と一致する「_」や、0文字以上の任意の文字列と一致する「%」といった、ワイルドカードを利用できます。 ワイルドカードをリテラルの一部として使用する場合は、ESCAPEオプションを指定してワイルドカードをリテラルとして扱えるようにしなければなりません。 設問では「HITS_」が含まれている行を検索するので、文字パターンは'%HITS_%'となりますが、文字パターンに"_"が含まれているので、ESCAPEオプションを指定して「_」をリテラルとして扱う必要があります。 さらに「'S」も含まれるようにしなければなりませんが、一重引用符(')が含まれているので、代替引用符q演算子を使用するか、一重引用符(')を2つ記述して一重引用符(')をリテラルとします。 以上より、 ・WHERE prod_name LIKE q'(%HITSW_%'s%)' ESCAPE 'W' ・WHERE prod_name LIKE '%HITSW_%''s%' ESCAPE 'W' が正解となります。 ここで...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions007.htm#i1034153

### 問題ID 26652 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26652?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文を実行した結果として表示されるデータの組合せで正しいものはどれですか(該当するものを全て選択して下さい)。 SELECT salary FROM employees WHERE salary NOT BETWEEN 300000 AND 500000;
- 解説要約: BETWEEN演算子とNOT演算子を組合せて使用する場合は、下限値よりも小さいまたは上限値よりも大きい値を検索します(下限値、上限値は検索結果に含まれませんので注意しましょう)。 設問の条件では、300000より小さいか、500000より大きい値を検索します。 以上より、 ・200000, 600000, 800000 ・250000, 550000, 600000 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions011.htm#CJAGAIDD

### 問題ID 26653 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26653?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文の実行結果として表示される製品名として正しいものはどれですか(該当するものを全て選択して下さい)。 SELECT prod_name FROM products WHERE prod_name BETWEEN 'E' AND 'N';
- 解説要約: BETWEEN演算子の下限値、上限値に文字リテラルが指定された場合は、指定された文字列の文字コードの範囲で検索が行われます。 文字コードの範囲ですので、設問の場合は、頭文字が「E」で始まる商品名から、「N」という1文字の商品名までが検索されます。 以上より、 ・LEDライト ・Lantern ・HighPower_LED_ハンディライト2 が正解となります。 設問のSELECT文の実行結果は次のようになります。 SQLを表示 SELECT prod_name FROM products WHERE prod_name BETWEEN 'E' AND 'N';
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions011.htm#CJAGAIDD

### 問題ID 26654 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26654?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: ORDERS表の構造を確認して下さい。 2010年4月1日から2011年3月31日までの注文状況をORDERS表から取得するには、どの問い合わせを実行しますか。
- 解説要約: BETWEEN演算子の下限値、上限値には文字リテラルや日付リテラルを指定することもできます。その場合は、一重引用符(')で囲まなければなりません。 設問では注文日が2010年4月1日から2011年3月31日までのデータを検索するので、BETWEEN演算子の下限値と上限値にそれぞれ'2010-04-01','2011-03-31'を指定します。 以上より、 ・SELECT order_id, order_date, order_total FROM ORDERS WHERE order_date BETWEEN '2010-04-01' AND '2011-03-31'; が正解となります。 正解のSELECT文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT order_id, order_date, order_total FROM ORDERS WHERE order_date BETWEEN 2010-04-01 AND 2011-03-31; ・SELECT order_id, order_date, order_total FROM...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions011.htm#CJAGAIDD

### 問題ID 26655 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26655?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のCOMMISSION列がNULL値でない従業員を検索する条件として、正しいものはどれですか。
- 解説要約: 列がNULL値であるかを判定するには、IS NULL演算子を使用します。IS NULL演算子では、列の値がNULL値である場合に条件が成立します。 NULL値は特殊な値ですので、列の値がNULL値かどうかの判定はIS NULL演算子以外の比較演算子ではできません。 設問のようにNULL値ではないことを判定するには、IS NULL演算子とNOT演算子を組合せた、IS NOT NULL演算子を使用して、commission IS NOT NULLのように記述します。 以上より、 ・WHERE commission IS NOT NULL が正解となります。 正解の検索条件でEMPLOYEES表を検索すると次のようになります。 SQLを表示 SELECT employee_id, employee_name, commission FROM employees WHERE commission IS NOT NULL; その他の選択肢については以下のとおりです。 ・WHERE commission <> NULL ・WHERE commission != NULL NULL値かどうかを判定す...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements005.htm#SQLRF51095

### 問題ID 26656 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26656?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次の問い合わせを確認してください。 SELECT customer_id, cust_last_name, cust_first_name FROM customers WHERE 1 = 5; この問い合わせの実行結果はどうなりますか。
- 解説要約: 特定の条件に合致した行を検索したい場合は、SELECT文にWHERE句で条件を指定します。 WHERE句を指定すると、WHERE句に指定した条件が成立する(条件が真である)行のみ検索結果として表示されます。 設問の条件1=5は常に成立しない(条件が偽である)ので、検索結果は1つも表示されません。 以上より、 ・データは1件も検索されない が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT customer_id, cust_last_name, cust_first_name FROM customers WHERE 1 = 5; また、条件を次のように変更すると、全ての行が検索されます。 条件1=1が常に成立する（条件が真である）ためです。 SQLを表示 SELECT customer_id, cust_last_name, cust_first_name FROM customers WHERE 1 = 1;
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#i2134734

### 問題ID 26657 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26657?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のSALARY列が300,000未満のデータを検索する条件として、正しいものはどれですか。
- 解説要約: 特定の条件に合致した行を検索したい場合は、SELECT文にWHERE句で条件を指定します。 設問のように「未満（より小さい）」を条件とする場合は、比較演算子の「<」を使用します。 よって ・WHERE salary < 300000 が正解となります。 設問の検索条件でEMPLOYEES表を検索すると次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees WHERE salary < 300000; その他の選択肢については以下のとおりです。 ・WHERE salary >= 300000 SALARY列が300,000以上の行を検索する条件です。 ・WHERE salary <= 300000 SALARY列が300,000以下の行を検索する条件です。 ・WHERE salary > 300000 SALARY列が300,000より大きい行を検索する条件です。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#CJAGAABC

### 問題ID 26658 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26658?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のDEPARTMENT_IDが1以外の従業員を検索する条件として、正しいものを全て選択して下さい。
- 解説要約: 特定の条件に合致した行を検索したい場合は、SELECT文にWHERE句で条件を指定します。 設問のように、DEPARTMENT_IDが1ではないという条件を記述するには、「等しくない」を意味する<>,!=,^=などの比較演算子を使用します。 以上より、 ・WHERE department_id <> 1 ・WHERE department_id != 1 ・WHERE department_id ^= 1 が正解となります。 検索条件をWHERE department_id != 1としてEMPLOYEES表を検索すると次のようになります。 SQLを表示 SELECT employee_id, employee_name, department_id FROM employees WHERE department_id != 1; その他の選択肢については以下のとおりです。 ・WHERE department_id = 1 「=」は「等しい」を意味する比較演算子ですので、この条件ではDEPARTMENT_ID列が「1」である行が検索されます。 ・WHERE department_id ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#CJAGAABC

### 問題ID 26659 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26659?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: PRODUCTS表の構造を確認してください。 PRODUCTS表から製品名が「Lantern」の行を検索する条件として正しいものはどれですか。
- 解説要約: 特定の条件に合致した行を検索したい場合は、SELECT文にWHERE句で条件を指定します。 設問では製品名が「Lantern」である行を検索するので、WHERE句に指定する条件は、等しいを意味する「=」比較演算子を使用します。 なお、「Lantern」は文字リテラルですので一重引用符(')で囲みます。 ここで注意しなければならないのは、データベースに登録されている文字データは大文字/小文字が区別されるということです。表名や列名は大文字/小文字は区別されませんので、混同しないようにしましょう。 以上より、 ・WHERE prod_name = 'Lantern' が正解となります。 設問の検索条件でPRODUCTS表を検索すると次のようになります。 SQLを表示 SELECT prod_id, prod_name FROM products WHERE prod_name = 'Lantern'; その他の選択肢については以下のとおりです。 ・WHERE prod_name = 'LANTERN' 製品名が全て大文字の「LANTERN」が検索されます。 ・WHERE prod_name ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#CJAGAABC

### 問題ID 26660 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26660?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: CUSTOMERS表のCUST_LAST_NAME列の値が「佐藤」であるデータを検索する条件として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: WHERE句の条件に指定した値と等しい行を検索するには、=演算子やIN演算子を使用します。 またLIKE演算子でワイルドカードを用いない場合も=演算子と同じです。 以上より、 ・WHERE cust_last_name = '佐藤' ・WHERE cust_last_name IN ('佐藤') ・WHERE cust_last_name LIKE '佐藤' が正解となります。 ただ通常は、IN演算子は複数の値を列挙する際に用い、LIKE演算子はワイルドカードを併用して文字パターンに合致する複数の文字列を検索する際に用います。 正解の検索条件でCUSTOMERS表を検索すると次のようになります。 SQLを表示 SELECT customer_id, cust_last_name, cust_first_name FROM customers WHERE cust_last_name = '佐藤'; SQLを表示 SELECT customer_id, cust_last_name, cust_first_name FROM customers WHERE cust_last_name ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#i2134734

### 問題ID 26661 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26661?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文を実行した時に表示される列の組合せとして正しいものはどれですか(該当するものを全て選択してください)。 SELECT employee_name, salary, commission FROM employees WHERE salary >= 200000 AND commission <= 1000000;
- 解説要約: SQL文では「AND」や「OR」,「NOT」などの論理演算子を使用できます。 設問で使用されているAND演算子は、前後の条件が両方共成立する行が検索結果として表示されます。 設問のSQL文を実行すると、「SALARY列の値が200,000以上」かつ「COMMISSION列の値が1,000,000以下」の2つの条件を満たす値の組合せが正解となります。 以上より、 ・A ・C が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions004.htm#i1052219

### 問題ID 26662 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26662?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文を実行した時に表示される列の組合せとして、正しいものはどれですか(該当するものを全て選択して下さい)。 SELECT employee_name, salary, commission FROM employees WHERE salary >= 200000 OR commission <= 1100000;
- 解説要約: SQL文では「AND」や「OR」,「NOT」などの論理演算子を使用できます。 設問で使用されているOR演算子は、前後の条件がどちらかでも成立する行が検索結果として表示されます。 設問のSQL文を実行すると、「SALARY列の値が200,000以上」もしくは「COMMISSION列の値が1,100,000以下」のどちらかの条件を満たす値が正解となります。 以上より、 ・A ・C ・D ・E が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions004.htm#i1052219

### 問題ID 26663 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26663?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のSALARY列が300000より大きい従業員を検索する条件として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 特定の条件に合致した行を検索したい場合は、SELECT文にWHERE句で条件を指定します。 設問のように「より大きい」を条件とする場合は、比較演算子の「>」を使用します。 または、条件の判定結果を反転させる「NOT演算子」を使用して、「NOT salary <= 300000」（salaryが300000以下で無ければ真）とすることもできます。 以上より、 ・WHERE NOT salary <= 300000 ・WHERE salary > 300000 が正解となります。 その他の選択肢については以下のとおりです。 ・WHERE NOT salary < 300000 「salaryが300000より小さく無ければ真」となります。 この場合、salaryが300000の場合も真となってしまいます。 ・WHERE salary < 300000 「salaryが300000より小さければ真」となります。 ・WHERE salary >= 300000 「salaryが300000以上なら真」となります。 この場合、salaryが300000の場合も真となってしまいます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions004.htm#i1052219

### 問題ID 26664 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26664?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文はエラーとなります。エラーの原因は何ですか。 SELECT employee_id ID, employee_name NAME, salary * 12 sal FROM employees WHERE sal >= 300000 AND department_id IN (1, 2, 3);
- 解説要約: SELECT文の中で列別名を使用できるのはORDER BY句だけです。 設問のSQL文ではsalary * 12という算術式にsalという列別名を指定していますが、WHERE句の条件でその列別名を使用しているためエラーが発生します。 以上より、 ・WHERE句に列別名は指定できないから が正解となります。 設問のSQL文を実行するとエラーとなります。 SQLを表示 SELECT employee_id ID, employee_name NAME, salary * 12 sal FROM employees WHERE sal >= 300000 AND department_id IN (1, 2, 3); エラーが発生しないようにするには、WHERE句の条件に使用している列別名を算術式で記述します。 SELECT employee_id ID, employee_name NAME, salary * 12 sal FROM employees WHERE salary * 12 >= 300000 AND department_id IN (1, 2, 3); その他の選択肢に...
- 参考URL: なし

### 問題ID 26665 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26665?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 次のSELECT文を実行するとエラーとなります。エラーの原因はいくつありますか。 SELECT employee_id ID, employee_name 20EMPNAME, hiredate DATE FROM employees;
- 解説要約: 列別名はオブジェクトのネーミング規則に従って命名しなければなりません。 設問の列別名のうち、「20EMPNAME」は先頭に数字が使用されているためエラーとなります。また、「DATE」はSQLの予約語ですのでこちらもエラーとなります。 以上より、 ・2つ が正解となります。 「20EMPNAME」や「DATE」を列別名として使用するには、二重引用符(")で囲まなければなりません。 SQLを表示 SELECT employee_id ID, employee_name "20EMPNAME", hiredate "DATE" FROM employees;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements008.htm#i27561
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/ap_keywd001.htm#BABCJAEB

### 問題ID 26666 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26666?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 算術式を指定できる句として正しいものはどれですか(該当するものを全て選択してください)。
- 解説要約: 算術式はSELECT句だけではなく、FROM句を除く任意の句で使用できます。 以上より、 ・SELECT句 ・WHERE句 ・GROUP BY句 ・HAVING句 ・ORDER BY句 が正解となります。 それぞれの句の機能は次の通りです。 ・SELECT句 : データベースから取り出すデータを選択します ・FROM句 : データベースのどの表からデータを取り出すかを決定します ・WHERE句 : 条件に従って取り出すデータを制限します ・GROUP BY句 : 取り出すデータをグループ化します ・HAVING句 : 条件に従って取り出すグループを制限します ・ORDER BY句 : 取り出したデータをソートします WHERE句からORDER BY句は、以降の分野で詳しく扱います。
- 参考URL: なし

### 問題ID 26667 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26667?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 単一行関数の説明として正しい記述はどれですか(該当するものを全て選択して下さい)。
- 解説要約: 単一行関数とは、行ごとに処理を行い、1行につき1件の結果を返す関数です。SELECT句、WHERE句、HAVING句、ORDER BY句などで使用することができます。 単一行関数のネストレベルには制限ありません。また、指定した引数と返される結果のデータ型は、必ずしも一致するとは限りません。 以上より、 ・ネストレベルに制限はない ・1行ごとに1つの結果を返す が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions002.htm#CJAJHBIA

### 問題ID 26668 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26668?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: EMPLOYEES表は次のとおりです。 入社日（hiredate）から現在までの年数を求めるにはどの問い合わせを実行しますか。 ただし端数は切り捨てて年数のみを求めることとします。
- 解説要約: 入社してから現在までの年数は、現在の日時から入社日を減算することで求めることができます。 現在の日時はSYSDATE関数で、入社日はEMPLOYEES表のHIREDATE列から取得することができます。 日付-日付の演算では、2つの日付値間の日数が数値で戻されます。 設問では端数を切り捨てた年数が問われているので、求めた日数を365で割り、かつTRUNC関数（数値関数）で小数点を切り捨てます。 以上より、 ・SELECT TRUNC((SYSDATE - hiredate) / 365) FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT SYSDATE - hiredate FROM employees; 入社日から現在までの日数が表示されます。 ・SELECT (TRUNC(SYSDATE, 'YEAR') - TRUNC(hiredate, 'YEAR')) / 365 FROM employees; ・SELECT (TRUNC(SYSDATE, 'MONTH') - TR...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i48042
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions221.htm#SQLRF06150

### 問題ID 26669 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26669?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表の構造を確認してください。 次の問い合わせを実行したところエラーが発生しました。 SELECT employee_name AS "Name", salary * 12 AS "Sal", Sal + commission AS "Total" FROM employees; エラーの原因はどれですか。
- 解説要約: SELECT句に指定された算術式に列別名を指定することはできますが、算術式の中で列別名を使用することはできません。 設問の「Sal + commission」の部分の「Sal」は、SELECT句の2つ目の項目に指定された列別名ですので使用することはできません。 以上より、 ・算術式の中で列別名を使うことはできない が正解となります。 その他の選択肢については以下のとおりです。 ・SELECT句に指定した項目が算術式の場合は、列別名を指定できない 算術式にも列別名を指定できます。 ・列別名は一重引用符(')で囲まなければならない 一重引用符(')は文字リテラルや日付リテラルを囲むときに使用します。 列別名の大文字と小文字を区別したい場合や、スペース等を使用したい場合は列別名を二重引用符(")で囲みますので、設問のSQL文で列別名は正しく指定されています。 ・Sal + commissionの「Sal」を二重引用符(")で囲まなければならない 二重引用符(")で囲んだとしても、列別名を算術式の中で使用することはできません。
- 参考URL: なし

### 問題ID 26670 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26670?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 SALARY列が400000以下か設定されておらず、HIREDATE列が2007年4月1日以降の従業員を検索するために、次の問い合わせを実行しました。 SELECT employee_id, employee_name, salary, hiredate FROM employees WHERE salary <= 400000 OR salary IS NULL AND hiredate >= '2007-04-01'; この問い合わせについて正しい記述はどれですか。
- 解説要約: 論理演算子を使用してWHERE句に複数の条件が指定されている場合、論理演算子の優先順位に従って条件が判定されます。 論理演算子の優先順位は次の通りです。 WHERE salary <= 400000 OR salary IS NULL AND hiredate >= '2007-04-01'; 設問のSQL文では、 salary IS NULL AND hiredate >= '2007-04-01' の部分が初めに判定されるため、「SALARY列が400000以下」、または、「SALARY列がNULLで、且つHIREDATE列が2007年4月1日以降」のデータが検索されます。 以上より、 ・正常に実行されるが目的の結果は検索できない が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary, hiredate FROM employees WHERE salary <= 400000 OR salary IS NULL AND hiredate >= '2007-04-01';...
- 参考URL: なし

### 問題ID 26671 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26671?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 2001年に入社し、給与(SALARY列)が350,000以上で、氏名の2文字目が「藤」である従業員を表示するために実行する問い合わせはどれですか。
- 解説要約: 検索ずる条件は、2001年に入社かつ給与(SALARY列)が350,000以上かつ氏名の2文字目が「藤」である従業員ですので、これらの条件をAND演算子で指定します。 以上より、 ・SELECT employee_id, employee_name, salary, hiredate FROM employees WHERE salary >= 350000 AND hiredate BETWEEN '2001-01-01' AND '2001-12-31' AND employee_name LIKE '_藤%'; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT employee_id, employee_name, salary, hiredate FROM employees WHERE salary >= 350000 AND hiredate >= '2001-01-01' OR hiredate <= '2001-12-31' AND employee_name LIKE '_藤%'; hire...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions011.htm#CJAGAIDD

### 問題ID 26672 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26672?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問い合わせでエラーとなるのはどれですか。
- 解説要約: Oracle Databaseでは、データ型の変換が意味を持つ場合に、自動的にデータ型の変換が行われます(暗黙的なデータ変換といいます)。そのため、関数の引数やWHERE句の条件等に期待されるデータ型以外の値を指定したとしても、エラーとならない場合があります。 選択肢のSQL文を1つずつ確認してみましょう。 ・SELECT employee_id, employee_name FROM employees WHERE department_id = '1'; DEPARTMENT_ID列は数値なので、department_id = 1と指定するべきですが、'1'の部分が暗黙的なデータ変換により数値に変換されるので、エラーにはなりません。 ・SELECT employee_id, CONCAT(employee_name, salary) FROM employees; CONCAT関数の引数には文字列データを指定するべきですが、salary(数値)が暗黙的なデータ変換により文字列に変換されるので、エラーにはなりません。 ・SELECT employee_id, employee_nam...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements002.htm#i46862

### 問題ID 26673 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26673?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文を確認して下さい。 SELECT employee_id, employee_name, hiredate FROM employees WHERE hiredate >= '30-APR-10'; このSQL文に関して正しい記述はどれですか。 ただし、データベースの実行環境は日本語環境とし、日付書式は"RR-MM-DD"とします。
- 解説要約: Oracle Databaseでは、データ型の変換が意味を持つ場合に、自動的にデータ型の変換が行われます(暗黙的なデータ変換といいます)が、次のような場合にはデータ変換は行われません。 ・数値が期待されている箇所に'abc'などの文字列を指定する ・日付書式にあっていない日付リテラルを指定する 設問では、日本語環境で日付書式が"RR-MM-DD"であるのに対し、"DD-MON-RR"の形式で日付リテラルが指定されていますので、暗黙的なデータ変換が行われません。 以上より、 ・エラーが発生する が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, hiredate FROM employees WHERE hiredate >= '30-APR-10';
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements002.htm#i46862

### 問題ID 26674 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26674?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: xとyの値は表の通りです。 次のSQL文の結果として誤っているものはどれですか。 SELECT x, y, NVL(x * 12 + y, -1) FROM dual;
- 解説要約: NVL関数は第1引数の値がNULL値の場合、第2引数の値を返します。第1引数の値がNULL値でなければ、そのまま第1引数の値を返します。 また、計算式にNULL値が含まれる場合、結果はNULL値となります。 設問の表のうち、AのyはNULL値であるのに結果が-1となっていないため誤りです。 以上より、 ・A が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT 20, NULL, NVL(20 * 12 + NULL, -1) FROM dual;
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL.html#GUID-3AB61E54-9201-4D6A-B48A-79F4C4A034B2

### 問題ID 26675 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26675?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文でエラーとなるのはどれですか。
- 解説要約: NVL2関数は値がNULL値か否かを調べ、NULL値以外の場合は第2引数、NULL値の場合は第3引数の値を返す関数です。 第2引数と第3引数は同じデータ型でなければなりません。異なるデータ型の値を指定するとエラーとなります。 選択肢のSQL文のうち、 ・SELECT NVL2(commission, commission, 'none') FROM employees; COMMISSION列の値がNULL値だった場合に文字列「none」に変換しようとしていますが、第2引数のCOMMISSION列はNUMBER型の列であるためエラーとなります。 以上より、 ・SELECT NVL2(commission, commission, 'none') FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL2.html#GUID-414D6E81-9627-4163-8AC2-BD24E57742AE

### 問題ID 26676 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26676?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: xとyの値は表の通りです。 次のSQL文の結果として誤っているものはどれですか。 SELECT x, y, NVL2(x * 12 + y, 1, -1) FROM dual;
- 解説要約: NVL2関数は値がNULL値か否かを調べ、NULL値以外の場合は第2引数、NULL値の場合は第3引数の値を返す関数です。 設問のSQL文の場合、計算式の結果がNULL値以外の場合は1を、NULL値の場合は-1を返します。 設問の表のうち、Dは計算の結果NULL値とならないため1が返されます。 以上より、 ・D が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT 15, 80, NVL2(15 * 12 + 80, 1, -1) FROM dual;
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL2.html#GUID-414D6E81-9627-4163-8AC2-BD24E57742AE

### 問題ID 26677 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26677?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: NULLIF関数の説明で正しいものはどれですか(該当するものをすべて選択してください)。
- 解説要約: NULLIF関数は第1引数と第2引数が等しい場合はNULL値を、等しくない場合は第1引数の値を返します。 なお、第1引数にはリテラルのNULL値以外の値を指定しなければなりませんが、第2引数はNULL値を指定できます。 以上より、 ・2つの値を比較して、等しい場合にNULLを返す ・1番目の引数にリテラルNULL値を指定できない ・2番目の引数にリテラルNULL値を指定できる が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions116.htm#SQLRF00681

### 問題ID 26678 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26678?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: COALESCE関数の説明として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: COALESCE関数は引数の値を判定し、最初に見つかったNULL値以外の値を返す関数です なお、COALESCE関数の引数は、すべて同じデータ型の値でなければなりません。異なるデータ型の値を指定するとエラーとなります(暗黙的なデータ変換は行われません)。 以上より、 ・引数の値を判定し、最初に見つかったNULL値以外の値を返す ・引数に指定するデータは、すべて同じデータ型でなければならない が正解となります。 その他の選択肢については次のとおりです。 ・引数のデータ型は、暗黙的なデータ変換が行われるので、引数に異なるデータ型を指定できる 暗黙的なデータ変換は行われません。引数に異なるデータ型の値を指定するとエラーとなります。 ・すべての引数がNULLだった場合は0を返す ・引数には1つ以上のNULL値以外のデータを指定しなければならない すべての引数がNULL値の場合、COALESCE関数はNULL値を返します。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions030.htm#SQLRF00617

### 問題ID 26679 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26679?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: xとyの値は表の通りです。 次のSQL文の結果として誤っているものはどれですか。 SELECT x, y, COALESCE(x * 12 + y, x, y) FROM dual;
- 解説要約: COALESCE関数は引数の値を判定し、最初に見つかったNULL値以外の値を返す関数です。 設問の表のうち、Cは第1引数の計算結果と第2引数がNULL値となりますが、第3引数はNULL値ではないので、第3引数の値が返されるため誤りです。 以上より、 ・C が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT COALESCE(NULL + 12 + 150, NULL, 150) FROM dual;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions030.htm#SQLRF00617

### 問題ID 26680 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26680?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: SQL関数の結果として正しいものはどれですか。
- 解説要約: NVL関数は、第1引数の値がNULL値以外の場合は第1引数の値を返し、NULL値の場合は第2引数の値を返します。 NVL2関数は、第1引数の値がNULL値以外の場合は第2引数の値を返し、NULL値の場合は第3引数の値を返します。 NULLIF関数は、第1引数と第2引数の値を比較して、等しい場合はNULL値を、等しくない場合は第1引数を返します。 COALESCE関数は、引数の値を判定し、最初に見つかったNULL値以外の値を返します。 以上より、 ・NVL('sato', NULL)の結果は"sato"である が正解となります。 正解のNVL関数の実行結果は次のようになります。 SQLを表示 SELECT NVL('sato', NULL) FROM dual; その他の選択肢については次のとおりです。 ・NVL2(NULL, 'sato', 'yamada')の結果は"sato"である NVL2関数は第1引数の値がNULL値の場合、第3引数の値を返します。 SQLを表示 SELECT NVL2(NULL, 'sato', 'yamada') FROM dual; ・NULLIF('sa...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL.html#GUID-3AB61E54-9201-4D6A-B48A-79F4C4A034B2
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL2.html#GUID-414D6E81-9627-4163-8AC2-BD24E57742AE
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions030.htm#SQLRF00617

### 問題ID 26681 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26681?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PROMOTIONS表の構造とデータを確認して下さい。 次のSQL文の実行結果として正しいものはどれですか。 SELECT promo_id, promo_begin_date, promo_end_date, NVL2(NULLIF(promo_begin_date, promo_end_date), NVL(promo_end_date - promo_begin_date, 0), 0) "期間" FROM promotions;
- 解説要約: NVL関数は、第1引数の値がNULL値の場合は第2引数の値を返し、第1引数の値がNULL値以外の場合はそのまま第1引数の値を返します。 NVL2関数は、第1引数の値がNULL値以外の場合は第2引数の値を返し、第1引数の値がNULL値の場合は第3引数の値を返します。 NULLIF関数は、第1引数と第2引数が等しい場合はNULL値を、等しくない場合は第1引数の値を返します。 設問のSQL文で、期間が 0 と表示されるのは、promo_begin_date と promo_end_date が等しい場合、またはpromo_end_date - promo_begin_date がNULL値となる場合、すなわち、promo_end_date または promo_begin_date がNULL値である場合(どちらかの値がNULL値であるとき、演算結果はNULL値となります)です。 以上より、 ・PROMO_END_DATE列の値がNULL値の場合、期間に0と表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT promo_id, promo...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL.html#GUID-3AB61E54-9201-4D6A-B48A-79F4C4A034B2
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL2.html#GUID-414D6E81-9627-4163-8AC2-BD24E57742AE
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions116.htm#SQLRF00681

### 問題ID 26682 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26682?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PROD表の構造を確認して下さい。 次の2つのSQL文の結果として正しいものはどれですか。 1) SELECT NVL(enddate, name) FROM prod; 2) SELECT NVL2(enddate, name, name) FROM prod;
- 解説要約: NVL関数は、第1引数の値がNULL値の場合は第2引数の値を返し、第1引数の値がNULL値以外の場合はそのまま第1引数の値を返します。 NVL2関数は、第1引数の値がNULL値以外の場合は第2引数の値を返し、第1引数の値がNULL値の場合は第3引数の値を返します。 また、NVL関数の第2引数に指定する式は、第1引数の式と同じデータ型でなければなりません。 NVL2関数の第3引数に指定する式は、第2引数の式と同じデータ型でなければなりませんが、第1引数とは異なるデータ型でも構いません。 設問の2つのSQLをみると、NVL2関数の第2引数と第3引数には同じ型の列が指定されていますが、NVL関数では第1引数と第2引数で異なるデータ型の列が指定されているので、NVL関数を実行するとエラーが発生します。 以上より、 ・1)はエラーが発生し、2)は正常に実行できる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT NVL(enddate, name) FROM prod; SQLを表示 SELECT NVL2(enddate, name, name) ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL.html#GUID-3AB61E54-9201-4D6A-B48A-79F4C4A034B2
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL2.html#GUID-414D6E81-9627-4163-8AC2-BD24E57742AE

### 問題ID 26683 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26683?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文のうち正常に実行されるものはどれですか(該当するものをすべて選択してください)。
- 解説要約: DECODE関数は、第1引数に指定された式の値と、第2引数以降に指定された条件を順に判定し、値が合致した条件に対応する戻り値を返します。 なお、DECODE関数の条件に、WHERE句の条件に指定するような比較演算子を使用した条件を記述することはできません。 また、条件が複数指定された場合の戻り値のデータ型は、第3引数で指定された戻り値のデータ型が採用されます。したがってそれぞれの戻り値は、第3引数の戻り値のデータ型と同じデータ型の値を指定するか、暗黙的なデータ変換で第3引数の戻り値のデータ型と同じデータ型となるような値を指定しなければなりません。 以上より、 ・SELECT employee_id, employee_name, DECODE(salary, NULL, 150000) sal FROM employees; ・SELECT employee_id, employee_name, DECODE(NULLIF(salary, 500000), NULL, '-', salary) sal FROM employees; が正解となります。 正解のSQL文の実行結果は次のよ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions049.htm#SQLRF00631

### 問題ID 26684 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26684?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文をCASE式を使用して置き換えるとどうなりますか。 SELECT department_id, department_name, DECODE(department_id, 1, 1013 , 2, 1014 , manager_id) new_manager FROM departments;
- 解説要約: DECODE関数を使用した分岐処理を単純CASE式を使用して書き換えることができます。 CASE式ではデフォルトの戻り値はELSE句に指定しますので注意しましょう。 以上より、 ・SELECT department_id, department_name, CASE department_id WHEN 1 THEN 1013 WHEN 2 THEN 1014 ELSE manager_id END new_manager FROM departments; が正解となります。 設問のSQL文と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, department_name, DECODE(department_id, 1, 1013 , 2, 1014 , manager_id) new_manager FROM departments; SQLを表示 SELECT department_id, department_name, CASE department_id WHEN 1 THEN 1013 WHEN 2 THEN 10...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions004.htm#SQLRF20037
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions049.htm#SQLRF00631

### 問題ID 26685 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26685?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 2009年12月31日以前に入社した従業員と2010年1月1日以降に入社した従業員の年収の合計をそれぞれ求めるために次のSQL文を実行しました。 実行結果として正しいものはどれですか。 ただし、従業員の年収はSALARY列の12倍にCOMMISSION列の値を加算したものとします。 SELECT SUM(CASE WHEN hiredate < TO_DATE('2010-01-01', 'YYYY-MM-DD') THEN salary * 12 + commission ELSE NULL END) sum1, SUM(CASE WHEN hi...
- 解説要約: CASE式には単純CASE式と検索CASE式の2種類がありますが、設問のSQL文で使用されているCASE式は検索CASE式です。 CASE式は関数の引数として記述することもできますし、デフォルトの戻り値にNULL値を指定することもできます。 以上より、 ・正常に実行でき、期待したデータが表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT SUM(CASE WHEN hiredate < TO_DATE('2010-01-01', 'YYYY-MM-DD') THEN salary * 12 + commission ELSE NULL END) sum1, SUM(CASE WHEN hiredate >= TO_DATE('2010-01-01', 'YYYY-MM-DD') THEN salary * 12 + commission ELSE NULL END) sum2 FROM employees;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions004.htm#SQLRF20037

### 問題ID 26686 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26686?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 日付値の演算について正しいものはどれですか。 ただし、日付の表示書式はRR-MM-DDとします。
- 解説要約: 日付値に対して、「数値/24」を加算したり減算した場合は、数値を「時間数」として加算したり減算したりします。 設問の「12/24」であれば、12時間として演算します。 また、TO_DATE関数は文字リテラルを日付値に変換します。引数に時刻が指定されていない場合は午前0時0分0秒に設定されます。 以上より、 ・TO_DATE('12-01-01') + 12/24の結果は"12-01-01の正午"である が正解となります。 正解の演算を実行すると次のようになります。 SQLを表示 SELECT TO_CHAR(TO_DATE('12-01-01') + 12/24, 'RR-MM-DD HH24:MI:SS') FROM dual; その他の選択肢については以下のとおりです。 ・TO_DATE('12-01-01') + 12/24の結果はエラーとなる 日付値に対し数値/24を加算したり減算してもエラーとななりません。 ・TO_DATE('12-01-01') - 12/24の結果は"12-01-01の正午"である 12時間減算するので、"11-12-31の正午"となります。 ・TO_D...
- 参考URL: なし

### 問題ID 26687 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26687?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 「2012-Apr-25」という文字列を以下の形式で表示するには、どの問い合わせを実行しますか。 ただし、実行環境は英語環境とします。 25TH of April, Two Thousand Twelve
- 解説要約: 日付を表す文字列を書式化して表示するには、文字列をTO_DATE関数で日付値に変換し、その後、TO_CHAR関数で日付書式にしたがって文字列に変換します。 設問の表示形式では、 ・「年」はスペル表記 ・「月」は名前表記 ・「日」は順序表記 ですので、「年」には「SP」要素を指定、「月」は「MM」ではなく「Month」を指定、「日」は「TH」要素を指定しなければなりません。 また、埋め込みモードが有効になっていると、「Month」を指定した時に末尾にスペースが表示されるので、「FM」要素を指定して埋め込みモードを無効にする必要があります。 以上より、 ・SELECT TO_CHAR(TO_DATE('2012-Apr-25','YYYY-Mon-DD'), 'DDTH "of" FMMonth, YyyySP') FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。 ※日本語環境の場合は、事前に以下のSQL文を実行してセッションを英語環境に変更して下さい。 ALTER SESSION SET NLS_DATE_LANGUAGE = 'AMERICAN'...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions200.htm#SQLRF06129
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions203.htm#SQLRF06132

### 問題ID 26688 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26688?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: グループ関数が使用できるのはどの句ですか(該当するものを全て選択して下さい)。
- 解説要約: グループ関数はSELECT句、HAVING句、ORDER BY句で使用することができます。 以上より、 ・SELECT句 ・HAVING句 ・ORDER BY句 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203

### 問題ID 26689 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26689?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせの実行結果として、正しいものはどれですか。 SELECT employee_id, employee_name, salary FROM employees WHERE AVG(salary) > 350000;
- 解説要約: グループ関数を使用できるのは、SELECT句、ORDER BY句、HAVING句のみです。WHERE句ではグループ関数を使用することはできません。 以上より、 ・エラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees WHERE AVG(salary) > 350000;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203

### 問題ID 26690 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26690?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問い合わせのうち、エラーとなる問い合わせはどれですか(該当するものを全て選択して下さい)。
- 解説要約: グループ関数はSELECT句、HAVING句、ORDER BY句で使用できますが、WHERE句では使用できません。 また、主なグループ関数であるCOUNT,MAX,MIN,SUM,AVG関数の引数には、次の値を指定します。 ・COUNT関数 ： 数値型、文字列型、日付型の値を返す式または列と*(アスタリスク) ・MAX/MIN関数 ： 数値型、文字列型、日付型の値を返す式または列 ・SUM/AVG関数 ： 数値型の値を返す式または列 MAX/MIN関数は引数に日付型の値を指定できますが、SUM/AVG関数は数値しか指定できません。 以上より、 ・SELECT AVG(hiredate) FROM employees; ・SELECT employee_name FROM employees WHERE salary > AVG(salary); が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions003.htm#i89203
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions018.htm#i82074

### 問題ID 26691 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26691?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 平均月収を部署と職種の組合せで表示するためには、どの問い合わせを実行しますか。 ただし、月収はSALARY列の値とし、部署、職種はそれぞれDEPARTMENT_ID列、JOB_ID列とします。
- 解説要約: GROUP BY句を指定すると、GROUP BY句に指定された列の組合せで行をグループ化できます。 設問のように部署と職種の組合せで表示するためには、GROUP BY句にdepartment_idとjob_idを指定して行をグループ化します。 以上より、 ・SELECT department_id, job_id, AVG(salary) FROM employees GROUP BY department_id, job_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 DEPARTMENT_IDとJOB_IDの値が同一の行を同じグループとして平均を求めています。 その他の選択肢については以下のとおりです。 ・SELECT department_id, job_id, salary FROM employees GROUP BY department_id, job_id; department_idとjob_idの組合せでグループ化されますが、平均月収が求められていません。 ・SELECT department_id, job_id, AVG(salary...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions018.htm#i82074

### 問題ID 26692 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26692?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせのうち、エラーとなる問い合わせはどれですか(該当するものを全て選択して下さい)。
- 解説要約: SELECT文にGROUP BY句を指定すると、関連のある行をグループ化できますが、GROUP BY句を指定する場合にはいくつかの要件を満たす必要があります。 ・GROUP BY句には1つ以上の列を指定する ・GROUP BY句に列別名を指定することはできない ・GROUP BY句を指定したSELECT文のSELECT句には、GROUP BY句で指定した列、もしくはグループ関数のみ指定できる （select句に指定したグループ関数以外の列はすべてgroup by句で指定する必要がある） ・GROUP BY句とORDER BY句を併用する場合、ORDER BY句にはGROUP BY句で指定した列、もしくはグループ関数のみ指定できます （グループ化されている列の値を、グループ化されていない列の値を基準に並べ替える事はできない為） また、グループ関数はSELECT句、HAVING句、ORDER BY句で使用できます。WHERE句では使用できない事に注意して下さい。 条件にグループ関数を使用したい場合は、HAVING句で指定します。 以上より、 ・SELECT department_id DE...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038

### 問題ID 26693 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26693?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 平均月収を部署と職種の組合せで表示するためには、どの問い合わせを実行しますか(該当するものを全て選択して下さい)。 ただし、平均月収は部署の昇順、職種の降順で表示します。また、月収はSALARY列の値とし、部署、職種はそれぞれDEPARTMENT_ID列、JOB_ID列とします。
- 解説要約: GROUP BY句とORDER BY句を併用する場合、ORDER BY句にはGROUP BY句で指定した列かグループ関数を指定しなければなりません。 以上より、 ・SELECT department_id DEPT, job_id JOB, AVG(salary) SAL FROM employees GROUP BY department_id, job_id ORDER BY DEPT, JOB DESC; ・SELECT department_id, job_id, AVG(salary) FROM employees GROUP BY department_id, job_id ORDER BY 1, 2 DESC; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT department_id, job_id, AVG(salary) FROM employees GROUP BY department_id, job_id ORDER BY department_id, job_id, salary...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038

### 問題ID 26694 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26694?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせのうち、有効な問い合わせはどれですか(該当するものを全て選択して下さい)。
- 解説要約: SELECT文にGROUP BY句を指定すると、関連のある行をグループ化できますが、GROUP BY句を指定する場合にはいくつかの要件を満たす必要があります。 ・GROUP BY句には1つ以上の列を指定する ・GROUP BY句に列別名を指定することはできない ・GROUP BY句を指定したSELECT文のSELECT句には、GROUP BY句で指定した列、もしくはグループ関数のみ指定できる （select句に指定したグループ関数以外の列はすべてgroup by句で指定する必要がある） ・GROUP BY句とORDER BY句を併用する場合、ORDER BY句にはGROUP BY句で指定した列、もしくはグループ関数のみ指定できます （グループ化されている列の値を、グループ化されていない列の値を基準に並べ替える事はできない為） また、GROUP BY句はWHERE句とORDER BY句の間に指定します。 以上より、 ・SELECT department_id, job_id, COUNT(*) FROM employees GROUP BY department_id, job_id O...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038

### 問題ID 26695 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26695?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせに関して、正しい記述はどれですか。 1) SELECT department_id, AVG(salary) FROM employees WHERE salary BETWEEN 400000 AND 500000 GROUP BY department_id; 2) SELECT department_id, AVG(salary) FROM employees HAVING AVG(salary) BETWEEN 400000 AND 500000 GROUP BY department_id;
- 解説要約: 2つのSQL文の違いは、取り出す行の条件の指定にWHERE句を使用しているかHAVING句を使用しているかです。 どちらも正しく条件が指定されているので、2つのSQL文は正常に実行されますが、実行結果は異なります。 SQLは以下の順序で評価されます。 （評価順） FROM句→WHERE句→GROUP BY句→HAVING句→SELECT句→ORDER BY句 1)のSQL文では、WHERE句の条件に従って、全体からSALARY列の値が400,000以上500,000以下の行を取り出し、取り出した行に対してGROUP BY句で部署(department_id)毎にグループ化しています。 2)のSQL文では、GROUP BY句で部署(department_id)毎にグループ化した後、HAVING句の条件に従って、グループ（この場合、部署）のSALARY列の平均値が400,000以上500,000以下の行を取り出しています。 「平均給与が400,000以上500,000以下である部署を取り出している」と言えるのは、こちらです。 以上より、 ・どちらも正常に実行されるが、異なる結果となる が正...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55327
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26696 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26696?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせのうち、エラーとなる問い合わせはどれですか。
- 解説要約: SELECT文にWHERE句、GROUP BY句、HAVING句を同時に指定する場合は、WHERE句、GROUP BY句、HAVING句またはWHERE句、HAVING句、GROUP BY句の順に指定します。 また、HAVING句にはグループ関数の他、列を指定することもできますが、指定できる列はGROUP BY句で指定された列のみとなります。 以上より、 ・SELECT department_id, job_id, MIN(salary) FROM employees GROUP BY department_id, job_id HAVING AVG(salary) BETWEEN 200000 AND 500000 WHERE hiredate >= '03-04-01'; ・SELECT department_id, job_id, MIN(salary) FROM employees WHERE hiredate >= '03-04-01' GROUP BY department_id, job_id HAVING salary BETWEEN 200000 AND 500000...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26697 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26697?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: ENPLOYEES表の構造を確認して下さい。 従業員の月給の合計が3,000,000以上の部署を表示するには、どの問い合わせを実行しますか。 ただし、月給はSALARY列の値とし、部署はDEPARTMENT_IDの値とします。
- 解説要約: 部署ごとの月収の合計を表示するので、GROUP BY句で部署ごとにグループ化します。 また、月収の合計はグループ関数SUMで求めることができます。 条件にグループ関数を使用する場合は、WHERE句ではなくHAVING句で指定します。 以上より、 ・SELECT department_id, SUM(salary) FROM employees GROUP BY department_id HAVING SUM(salary) >= 3000000; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT department_id, SUM(salary) FROM employees GROUP BY department_id WHERE SUM(salary) >= 3000000; WHERE句の条件にグループ関数を使用することはできません。 ・SELECT department_id, SUM(salary) FROM employees HAVING SUM(salary) >= 3000000; GRO...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26698 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26698?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: 次の問い合わせを実行したところエラーとなりました。エラーの原因はどの句にありますか。 SELECT department_id dept, job_id job, AVG(salary) sal FROM employees WHERE department_id IN (1, 2, 3, 4) GROUP BY department_id, job_id HAVING sal > 250000 ORDER BY dept, job;
- 解説要約: HAVING句にはグループ関数とGROUP BY句に指定されている列を指定することができます。列別名を指定することはできません。 以上より、 ・HAVING句 が正解となります。 列別名はORDER BY句でのみ指定できます。これはSQL文が以下の順序で評価される為、SELECT句で指定した列別名を認識できるのはORDER BY句のみだからです。 （評価順） FROM句→WHERE句→GROUP BY句→HAVING句→SELECT句→ORDER BY句 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id dept, job_id job, AVG(salary) sal FROM employees WHERE department_id IN (1, 2, 3, 4) GROUP BY department_id, job_id HAVING sal > 250000 ORDER BY dept, job; HAVING句の列別名をAVG(salary)に変更すると、正常に実行することができます。 SQLを表示 SELECT de...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26699 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26699?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 2003年から2010年に入社した従業員数を部署と職種の組合せで表示するためには、どの問い合わせを実行しますか。 ただし、従業員数は部署の昇順、職種の降順で表示します。また、入社日はHIREDATE列の値とし、部署、職種はそれぞれDEPARTMENT_ID列、JOB_ID列の値とします。
- 解説要約: SELECT文でWHERE句、GROUP BY句、ORDER BY句を併用する場合は、 ・WHERE句 ・GROUP BY句 ・ORDER BY句 の順番で指定しなければなりません。 以上より、 ・SELECT department_id, job_id, COUNT(*) FROM employees WHERE hiredate BETWEEN '2003-01-01' AND '2010-12-31' GROUP BY department_id, job_id ORDER BY department_id, job_id DESC; が正解となります。 正解のSQL文の実行結果は次のようになります。
- 参考URL: なし

### 問題ID 26700 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26700?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表、EMPLOYEES表、JOBS表の構造を確認して下さい。 次のSQL文を実行するとどうなりますか。 SELECT d.department_id, job_id, employee_id, e.employee_name FROM departments d NATURAL JOIN employees e NATURAL JOIN jobs j;
- 解説要約: 自然結合では、結合列に表接頭辞を使用することはできません。表接頭辞を指定するとエラーとなります。 設問のSQL文では、DEPARTMENTS表とEMPLOYEES表の共通列であるDEPARTMENT_ID列に表接頭辞が使用されているため、実行するとエラーとなります。 以上より、 ・結合列に表接頭辞を使用しているのでエラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT d.department_id, job_id, employee_id, e.employee_name FROM departments d NATURAL JOIN employees e NATURAL JOIN jobs j; DEPARTMENT_ID列に指定された表接頭辞を削除すると、設問のSQL文は正常に実行されます。 SQLを表示 SELECT department_id, job_id, employee_id, e.employee_name FROM departments d NATURAL JOIN employees e NATURAL ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55325
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26701 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26701?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表とCATEGORY表の構造とデータを確認して下さい。 次のSQL文の文を実行すると、何件のデータが表示されますか。 SELECT name, category FROM prod NATURAL JOIN category;
- 解説要約: 設問のSQL文ではPROD表とCATEGORY表を自然結合で結合しています。自然結合で結合する場合は、2つの表に共通して存在する同名で同じデータ型の列に基づいて、表を結合します。 PROD表とCATEGORY表では、CATEGORY列とNAME列が同名で同じデータ型の列になりますので、これらの列の値の組合せが一致する行が結合されます。 PROD表とCATEGORY表のデータを見ると、CATEGORY列とNAME列の値の組合せが一致する行は1つもないので、結合結果は1件も表示されません。 以上より、 ・0 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT name, category FROM prod NATURAL JOIN category;
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55325
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26702 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26702?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQL文のうち、正しく実行されるものはどれですか。
- 解説要約: USING句を指定した結合では、結合列に表接頭辞を使用できません。また、NATURAL JOIN句と同時に指定することもできません。 以上より、 ・SELECT department_name, employee_name FROM departments JOIN employees USING (department_id); が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT department_name, employee_name FROM departments NATURAL JOIN employees USING (department_id); USING句を指定した結合では、NATURAL JOIN句とUSING句を1つの結合で同時に指定することはできません。 ・SELECT department_name, employee_name FROM departments d JOIN employees e USING (d.department_id); ・SELECT d.depart...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26703 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26703?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: どのような場合にUSING句を使用しますか(該当するものを2つ選択して下さい)。
- 解説要約: USING句を使用した結合は、等価結合の1つで、結合列を明示的に指定することができるので、2つの表に同名の列が複数あり、その一部を結合列にしたい場合や、同名でデータ型の異なる列がある場合に、USING句で結合列に指定しないことで、エラーを回避できます(自然結合では、同名でデータ型が異なる列を結合してしまいエラーとなります)。 以上より、 ・結合する2つの表に同じ列名でデータ型の異なる列がある場合 ・結合する2つの表の一部の列を結合列として使用する場合 が正解となります。 その他の選択肢については次のとおりです。 ・非等価結合を行う場合 USING句を使用した結合は等価結合となります。 ・結合列の値が一方の表にしか存在しない場合 外部結合を行います。 ・デカルト積を戻す結合を行う場合 CROSS結合を行います。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26704 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26704?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表、EMPLOYEES表の構造を確認して下さい。 次のSQL文を実行したところエラーとなりました。エラーの原因はなんですか。 SELECT department_id, employee_id, employee_name, salary FROM departments JOIN employees ON departments.department_id = employees.department_id WHERE departments.department_id IN (1, 2, 3, 4);
- 解説要約: ON句を使用した結合では、結合する2つの表にある同じ名前の列をSELECT句やWHERE句に指定する場合は、必ず表接頭辞を使用して列を指定しなければなりません。 設問のSQL文では、2つの表のDEPARTMENT_ID列が結合列として使用されていますが、SELECT句で表接頭辞を使用せずにDEPARTMENT_ID列が指定されています。WHERE句と同じように表接頭辞を使用してDEPARTMENT_ID列を指定しなければなりません。 以上より、 ・SELECT句で表接頭辞を使用していないため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, employee_id, employee_name, salary FROM departments JOIN employees ON departments.department_id = employees.department_id WHERE departments.department_id IN (1, 2, 3, 4); SELECT department...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26705 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26705?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表とCATEGORY表の構造とデータを確認して下さい。 次のSQL文の文を実行すると、何件のデータが表示されますか。 SELECT p.name, c.name FROM prod p JOIN category c ON p.category = c.category;
- 解説要約: 設問のSQL文ではPROD表とCATEGORY表をON句に指定した条件で結合しています。 ON句に指定された条件より、PROD表とCATEGORY表のCATEGORY列が等しい列が結合されます。 PROD表とCATEGORY表のデータを見ると、2つの表のCATEGORY列が等しい行は5行ありますので、結合結果には5行表示されます。 以上より、 ・5 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT p.name, c.name FROM prod p JOIN category c ON p.category = c.category;
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26706 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26706?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 次の問い合わせのうち、エラーとなるものはどれですか。
- 解説要約: Oracle Databaseでは外部結合演算子(+)を使用して外部結合を行うこともできます。外部結合演算子(+)を用いた結合では、WHERE句に指定した条件の片側に外部結合演算子(+)を指定します。 なお、外部結合演算子(+)を用いた外部結合では、WHERE句の両側に外部結合演算子(+)を指定することはできません。両方に指定した場合はエラーとなります。 以上より、 ・SELECT emp.employee_name, mgr.employee_name FROM employees emp, employees mgr WHERE emp.manager_id(+) = mgr.employee_id(+); が正解となります。 正解のSQL文の実行結果は次のようになります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26707 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26707?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: EMPLOYEES表とJOBS表の構造を確認して下さい。 従業員氏名と職種を表示するには、どの問い合わせを実行しますか。 ただし、担当する従業員がいない職種も含めて職種情報を表示し、職種を持たない従業員の情報は表示しないものとします。
- 解説要約: 従業員名と職種を取り出すには、EMPLOYEES表とJOBS表を結合します。 また、設問の「担当する従業員がいない職種も含めて職種情報を表示」とは、結合条件に合致しないデータも取り出すということですので、外部結合を行います。 担当する従業員がいない職種のデータも取り出すには、JOBS表からは結合条件に合致しないデータも取り出さなくてななりません。 したがって、「... jobs j LEFT OUTER JOIN ...」か「... RIGHT OUTER JOIN jobs j ...」のように外部結合しているものが正解です。 以上より、 ・SELECT e.employee_name, j.job_name FROM employees e RIGHT OUTER JOIN jobs j ON e.job_id = j.job_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT e.employee_name, j.job_name FROM employees e LEFT OUTER JOIN j...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Joins.html#GUID-29A4584C-0741-4E6A-A89B-DCFAA222994A

### 問題ID 26708 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26708?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 次の問い合わせの実行結果として、正しいものはどれですか。 SELECT o.order_date, c.cust_last_name, c.cust_first_name FROM orders o RIGHT OUTER JOIN customers c ON c.customer_id = o.cust_id;
- 解説要約: 設問のSQL文では、RIGHT OUTER JOIN句で右側外部結合を行なっているので、JOIN句の右側の表からは結合条件を満たしていないデータも取り出されます。 JOIN句の右側にはCUSTOMERS表が指定されているため、顧客データは結合条件を満たしていないデータも含めて取り出されます。 以上より、 ・売上の有無にかかわらず、全ての顧客名が表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT o.order_date, c.cust_last_name, c.cust_first_name FROM orders o RIGHT OUTER JOIN customers c ON c.customer_id = o.cust_id;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26709 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26709?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表とCATEGORY表の構造とデータを確認して下さい。 次のSQL文の実行結果として正しいものはどれですか。 SELECT c.name, p.name FROM category c LEFT OUTER JOIN prod p ON c.category = p.category;
- 解説要約: 設問のSQL文では、CATEGORY表とPROD表を左側外部結合で結合しています。 左側外部結合では、LEFT OUTER JIONの左側に指定された表の全てのデータを取り出すので、CATEGORY表のデータは全て取り出し、PROD表からは条件を満たしているデータのみ取り出されます。 以上より、 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26710 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26710?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表,OLDPROD表,CATEGORY表の構造とデータを確認して下さい。 次のSQL文の実行結果として正しいものはどれですか。 SELECT c.category c_category, p.category p_category, c.name c_name, p.name p_name FROM category c JOIN prod p ON c.category = p.category JOIN oldprod o ON p.category = o.category;
- 解説要約: 3つ以上の表を結合する場合、Oracle Databaseは結合順序を自動的に決定します。 設問のSQL文のように、3つの表を結合する場合、Oracle Databaseは最初に結合する2つの表を選択し、その結合結果と残りの表を結合します。 設問のSQL文では、次のどちらかの順序で結合が行われます。 ・CATEGORY表とPROD表の等価結合を行い、その結果とOLDPROD表を等価結合する SQLを表示 SELECT c.category c_category, p.category p_category, c.name c_name, p.name p_name FROM category c JOIN prod p ON c.category = p.category; SELECT * FROM oldprod; ・CATEGORY表と、PROD表とOLDPROD表を等価結合した結果を等価結合する SQLを表示 SELECT * FROM category; SELECT p.category p_category, p.name p_name FROM prod p JOIN ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF30046
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26711 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26711?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表とCATEGORY表の構造とデータを確認して下さい。 次のSQL文の実行結果として正しいものはどれですか。 SELECT c.category, c.name category_name, p.name prod_name FROM category c FULL OUTER JOIN prod p ON c.category = p.category ORDER BY c.category;
- 解説要約: 設問のSQL文では、CATEGORY表とPROD表を完全外部結合で結合しています。 完全外部結合では、指定された2つの表の条件を満たしていないデータも全て取り出します。 以上より、 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26712 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26712?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次のSQL文を実行すると、何件のデータが返されますか。 SELECT p.category, p.prodid, p.name prod_name, o.prodid old_id, o.name old_name FROM prod p FULL OUTER JOIN oldprod o ON p.category = o.category;
- 解説要約: 設問のSQL文で結合条件を満たす行は、CATEGORY列の値が10と40の2行です。ですが、完全外部結合を行なっているため、条件を満たしていない行も全て表示されます。 PROD表の条件を満たしていないデータはCATEGORY列の値が20,30,50,NULLの4行、OLDPROD表の条件を満たしていないデータはCATEGORY列の値が60,NULLの2行ですので、これらを合計して、8件のデータが表示されます。 以上より、 ・8 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT p.category, p.prodid, p.name prod_name, o.prodid old_id, o.name old_name FROM prod p FULL OUTER JOIN oldprod o ON p.category = o.category;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26713 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26713?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 副問合せが使用できる句はどれですか(該当するものを全て選択して下さい)。
- 解説要約: 副問合せは、SELECT文のSELECT句、FROM句、WHERE句、HAVING句、ORDER BY句の他、INSERT文やUPDATE文等のDML文でも使用することができます。 以上より、 ・SELECT句 ・FROM句 ・WHERE句 ・HAVING句 ・ORDER BY句 が正解となります。 以下にSELECT文のそれぞれの句で副問合せを使用した例を紹介します。 [SELECT句] SQLを表示 SELECT employee_name, (SELECT department_name FROM departments WHERE department_id = 1) dept_name, salary FROM employees WHERE department_id = 1; [FROM句] ※FROM句の副問合せはインライン・ビューとも呼ばれます SQLを表示 SELECT emp.* FROM (SELECT employee_name, hiredate, salary FROM employees WHERE department_id = 5) emp; [WH...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858

### 問題ID 26714 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26714?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 副問合せに関する説明として、正しいものはどれですか(2つ選択して下さい)。
- 解説要約: Oracle DatabaseではSQL文の中に別のSQL文を入れ子にして実行することができ、入れ子の内側の問合せのことを副問合せといいます(副問合せに対し、外側の問合せを主問合せといいます)。 通常の副問合せを使用したSQL文ではまず副問合せが実行され、副問合せの実行結果をもとに主問合せが実行されます。 副問合せの部分は()括弧で囲みます。(INSERT文で副問合せを使用してデータの追加を行う場合は、()は必須ではありません。分野「DML文」のINSERT文の参考をご参照ください。) 上記では比較演算子の右辺に副問合せを記述していますが、副問合せを左辺に定義してもかまいません。 また、単一行副問合せの場合、比較演算子に複数行演算子を使用してもエラーにならず正常に実行されます。しかし、複数行副問合せに単一行演算子を使用するとエラーとなります。 以上より、 ・SELECT文で使用する副問合せは()括弧で囲む ・複数行副問合せの比較演算子に単一行演算子=を使用するとエラーとなる が正解となります。 その他の選択肢については以下のとおりです。 ・必ず主問合せが実行された後で副問合せが実行され...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858

### 問題ID 26715 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26715?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 副問合せに関する説明として、誤っているものはどれですか。
- 解説要約: =ALL(値のリスト)は値のリストの全ての値と一致した場合に条件がTRUEになりますが、IN(値のリスト)は値のリストのいずれかに一致した場合に条件がTRUEになりますので、この2つの演算は等価ではありません。 以上より、 ・=ALL(値のリスト)はIN(値のリスト)と等価である が正解となります。 その他の選択肢については次のとおりです。 ・NOT IN(値のリスト)は<>ALL(値のリスト)と等価である NOT IN(値のリスト)は値のリストのいずれにも一致しない場合に条件がTRUEになりますので、<>ALL(値のリスト)と等価です。 ・NOT IN(値のリスト)にNULL値が含まれている場合は、データは1件も返されない NOT IN(値のリスト)は値のリストと比較した結果が全てFALSEになる場合に条件がTRUEになります。 値のリストにNULL値が含まれている場合は、NULL値との比較結果がNULL値となり、全ての結果がFALSEとならないため、条件はFALSEとなります。条件がFALSEなので、主問合せの結果は0件となります。 ・=ANY(値のリスト)はIN(値のリスト)と等...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#SQLRF52105

### 問題ID 26716 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26716?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 副問合せに関する説明として、正しいものはどれですか。
- 解説要約: 副問合せには、次のようにいろいろな使用方法があります。 ・SELECT文のSELECT句、FROM句、WHERE句、HAVING句、ORDER BY句や、INSERT文、UPDATE文等のDML文で使用できる ・主問合せと副問合せで異なる表にアクセスできる ・1つの主問合せに対し、複数の副問合せを指定できる ・副問合せをネストできる(WHERE句に指定した副問合せでは255レベルのネストが可能) ・副問合せの中でGROUP BY句やHAVIMG句、ORDER BY句を使用できる なお、副問合せの実行結果が0件となる場合、主問合せにはNULL値が返されるため、主問合せの実行結果は0件となります。 以上より、 ・副問合せがデータを1件も返さない場合は、主問合わせにNULLを返す が正解となります。 その他の選択肢については次のとおりです。 ・SELECT文でのみ使用できる 副問合せはINSERT文やUPDATE文などのDML文でも使用することができます。 ・副問合せのネストレベルに制限はない WHERE句で副問合せを使用した場合のネストレベルは255レベルです。 ・1つの問合せに指定できる...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858

### 問題ID 26717 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26717?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 副問合せを条件の一部として使用する場合の演算子の説明として、正しいものはどれですか。
- 解説要約: 副問合せがWHERE句などに指定する条件の一部として使用される場合、単一行副問合せでは単一行演算子を、複数行副問合せでは複数行演算子を使用して条件の判定を行います。 単一行副問合せ、複数行副問合せで使用する演算子はそれぞれ次の通りです。 複数行演算子INはNOT演算子と組合せて、NOT INとして使用することもできます。 以上より、 ・複数行演算子INはNOT演算子と組合せて使用できる が正解となります。 NOT INはリスト内の全ての値と等しくない場合にTRUEとなります。例えば次のSQL文では、マネージャーで無い従業員を表示しています。 SQLを表示 SELECT employee_name, hiredate, salary FROM employees WHERE employee_id NOT IN (SELECT manager_id FROM departments); その他の選択肢については次のとおりです。 ・>ANYと>ALLは同義である >ANYと>ALLは同義ではありません。>ANYは「副問合せの結果のうち、最小値よりも大きい」の意味ですが、>ALLは「副問合せ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#SQLRF52105

### 問題ID 26718 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26718?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 単一行副問合せに関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 単一行副問合せは主問合せに1件のデータを返す副問合せです。 副問合せがWHERE句などに指定する条件の一部として使用される場合、単一行副問合せでは単一行演算子を使用して条件を記述します。 ただし、ANY演算子などの複数行演算子と単一行副問合せを組み合せて使用してもエラーとはならず正常に実行されます。 以上より、 ・単一行副問合せとANY演算子を組み合せて使用できる ・単一行副問合せとIN演算子を組み合せて使用できる が正解となります。 以下のように、複数行演算子と単一行副問合せを組み合せて使用してもエラーになりません。 SQLを表示 SELECT AVG(salary) FROM employees; SELECT employee_name, hiredate, salary FROM employees WHERE salary >ANY (SELECT AVG(salary) FROM employees); その他の選択肢については次のとおりです。 ・単一行副問合せの結果が0件の場合は、主問合せに0を返す 副問合せの結果が0件の場合、主問合せにはNULL値が返されます。 ・単一...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions013.htm#i1033549

### 問題ID 26719 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26719?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せを実行すると、どうなりますか。 SELECT employee_id, employee_name, salary FROM employees WHERE commission >= (SELECT AVG(commission) FROM employees GROUP BY department_id);
- 解説要約: 条件の比較演算子に単一行演算子が使用されている場合、副問合せが戻すデータの件数は1件でなければなりません。複数件のデータが戻されるとエラーとなります。 以上より、 ・副問合せが複数行を返した場合、エラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, salary FROM employees WHERE commission >= (SELECT AVG(commission) FROM employees GROUP BY department_id); その他の選択肢については次のとおりです。 ・副問合せが複数行を返した場合、正常に実行される 比較演算子に単一行演算子が使用されているので、複数の行が返された場合はエラーとなります。 ・副問合せがNULL値を返した場合、エラーとなる 副問合せがNULL値を返した場合はエラーとなならず、主問合せでデータが1件も表示されません。 ・副問合せが1行を返した場合、エラーとなる 副問合せが1行を返した場合は、正常に実行されます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions013.htm#i1033549

### 問題ID 26720 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26720?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せのうち、正常に実行されるものはどれですか。 なお、EMPLOYEES表には以下の件数のデータが登録されています。
- 解説要約: 副問合せがWHERE句などに指定する条件の一部として使用される場合、単一行副問合せでは単一行演算子を、複数行副問合せでは複数行演算子を使用して条件の判定を行います。 比較演算子に単一行演算子を使用している場合、副問合せから複数件のデータが返されるとエラーとなります。また、1件のデータでも比較演算子の左辺と右辺で列数が異なる場合はエラーとなります。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees WHERE salary >= (SELECT AVG(salary) FROM employees); ・SELECT department_id, AVG(salary) FROM employees WHERE salary > (SELECT MIN(salary) FROM employees) GROUP BY department_id; が正解となります。 その他の選択肢については次のとおりです。 ・SELECT employee_id, employee_name, salary FROM empl...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions013.htm#i1033549

### 問題ID 26721 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26721?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せを実行すると、どうなりますか。 SELECT employee_id, employee_name FROM employees WHERE department_id IN (SELECT department_id FROM employees HAVING SUM(salary) = (SELECT MAX(SUM(salary)) FROM employees GROUP BY department_id) GROUP BY department_id);
- 解説要約: 副問合せはネストすることができます。WHERE句に指定する副問合せでは最大255レベルまでのネストが可能です。ネストした問合せでは、内側の問合せから実施されます。 設問のSQL文では、最初に内側の副問合せである SELECT MAX(SUM(salary)) FROM employees GROUP BY department_id が実施されます。この問合せでは、DEPARTMENT_ID毎の給与の合計額を計算し、一番多い給与の合計額を1件返します。 次に、 SELECT department_id FROM employees HAVING SUM(salary) = (内側の副問合せの結果) GROUP BY department_id が実施されます。この問合せでは、DEPARTMENT_ID毎の給与の合計額が一番多い部署のDEPARTMENT_IDの値を返します。 したがって、主問合せでは、給与の合計額が一番多い部署の全従業員番号と従業員名が取り出されます。 以上より、 ・所属する従業員の給与の合計が一番多い部署の全従業員番号と従業員名が表示される が正解となります。 設問の...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858

### 問題ID 26722 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26722?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次の問合せを実行したところエラーとなりました。エラーの原因は何ですか。 ただし、MANAGER_IDはDEPARTMENT_ID毎に異なる値が登録されているものとします。 SELECT employee_id, employee_name FROM employees WHERE department_id = (SELECT department_id FROM departments WHERE manager_id = (SELECT employee_id FROM employees WHERE salary =...
- 解説要約: 副問合せはネストすることができます。WHERE句に指定する副問合せでは最大255レベルまでのネストが可能です。ネストした問合せでは、内側の問合せから実施されます。 設問のSQL文では、最初に一番内側の副問合せである、 SELECT MAX(salary) FROM employees が実施されます。この問合せでは、全従業員のなかで一番給与額の多い従業員の給与額を1件返します。 次に、 SELECT employee_id FROM employees WHERE salary = (内側の問合せの結果) が実施されます。この問合せでは、一番給与額の多い従業員の従業員番号を返します。ここで、一番給与額の多い従業員が複数人いた場合、複数件のデータを返します。 次に、 SELECT department_id FROM departments WHERE manager_id = (内側の問合せの結果) が実施されます。この問合せでは、マネージャー番号が一番給与額の多い従業員と一致する部署の部署番号を返します。もしも内側の問合せから複数件のデータが返された場合は、単一行演算子を使用している...
- 参考URL: なし

### 問題ID 26723 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26723?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造とデータを確認して下さい。 次の問合せの実行結果として、正しいものはどれですか。 SELECT employee_id, employee_name, hiredate FROM employees WHERE department_id > (SELECT department_id FROM departments WHERE department_id NOT BETWEEN 1 AND 5);
- 解説要約: DEPARTMENTS表には、DEPARTMENT_ID列の値が1~5のデータが登録されています。 設問のSQL文の副問合せではDEPARTMENTS表のDEPARTMENT_ID列の値が1~5以外のデータを取り出そうとしていますが、DEPARTMENT_ID列の値が1~5以外のデータはないのでデータは1件も取り出されません。 副問合せでデータが1件も取り出されない場合、主問合せにはNULL値が返され、主問合せでの問い合わせ結果も0件となります。 以上より、 ・正常に実行されるが、データが1件も表示されない が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_id, employee_name, hiredate FROM employees WHERE department_id > (SELECT department_id FROM departments WHERE department_id NOT BETWEEN 1 AND 5); その他の選択肢については次のとおりです。 ・エラーとなる 副問合せから返されるデ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858

### 問題ID 26724 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26724?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 複数行副問合せに関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 複数行副問合せとは、複数件のデータを返す副問合せです。単一行副問合せと同じようにGROUP BY句を指定したり、副問合せをネストしたりすることができます。 また、複数列のデータを返すこともできます。 以上より、 ・複数行副問合せは複数件のデータも返す ・複数行副問合せをネストすることができる ・複数の列を返すこともできる が正解となります。 その他の選択肢については次のとおりです。 ・複数行副問合せは1件のデータを返す 1件のデータを返す副問合せは単一行副問合せといいます。複数行副問合せは複数件のデータを返します。 ・複数行副問合せではGROUP BY句を指定することはできない ・複数行副問合せではグループ関数を使用することができない 副問合せでは、グループ関数を使用したりGROUP BY句を指定することができます。
- 参考URL:
  - https://xtech.nikkei.com/it/article/COLUMN/20070914/281985/

### 問題ID 26725 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26725?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の作業のうち副問合せが必要な作業はどれですか(該当するものを全て選択して下さい)。
- 解説要約: 選択肢の作業をSQL文にすると、それぞれ次のようになります。 ・全社員の平均給与を表示する SELECT AVG(salary) FROM employees; ・全社員の平均給与より給与が多い従業員を表示する SELECT employee_name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees); ・部署ごとの平均給与を表示する SELECT AVG(salary) FROM employees GROUP BY department_id; ・所属従業員の給与の合計が一番多い部署の給与の合計を表示する SELECT MAX(SUM(salary)) FROM employees GROUP BY department_id; ・全社員の平均給与より給与が少ない従業員を表示する SELECT employee_name FROM employees WHERE salary < (SELECT AVG(salary) FROM employees); 以上より、 ・全社員の平均給与より給与が多い従業...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858
  - http://www.atmarkit.co.jp/ait/articles/1208/06/news118.html

### 問題ID 26726 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26726?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: 集合演算子に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 集合演算子には優先順位はありません。1つのSQL文に複数の集合演算子が使用されている場合は、SQL文の先頭から順番に複合問合せが行われます。 優先順位を明示的に指定したい場合は、()括弧を用いて優先順位を指定します。 以上より、 ・集合演算子に優先順位はない ・()括弧を用いて集合演算子の優先順位を変更できる が正解となります。 その他の選択肢については次のとおりです。 ・集合演算子UNIONは他の集合演算子よりも優先順位が高い ・集合演算子はUNION,UNION ALL,INTERSECT,MINUSの順で評価される 集合演算子には優先順位がありませんので、誤った記述です。 ・()括弧を使用しない場合、集合演算子は後ろに指定したものから評価される ()括弧を使用しない場合、後ろではなく、前に指定したものから評価されます。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381
  - https://www.shift-the-oracle.com/sql/set-operators-rule.html

### 問題ID 26727 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26727?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: 集合演算子の説明として、正しいものはどれですか。
- 解説要約: 複合問合せで使用する集合演算子は次の通りです。 以上より、 ・INTERSECTは2つの問合せの結果の共通する行を表示する が正解となります。 その他の選択肢については次のとおりです。 ・UNIONは2つの問合せの結果を重複行も含めて表示する UNION ALL演算子の説明です。 ・UNION ALLは2つの問合せの結果から重複行を排除して表示する UNION演算子の説明です。 ・MINUSは2つ目の問合せ結果から1つ目の問合せ結果にない行を表示する MINUSは1つ目の問合せ結果から2つ目の問合せ結果にない行を表示します
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26728 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26728?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次の問合せのうち、正しく実行されるものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 集合演算子を用いて複合問合せを行う際にORDER BY句を指定する場合は、次のガイドラインに従います。 ・ORDER BY句は複合問合せの最後の問合せに指定する ・ORDER BY句には最初の問合せに指定されている列名や列別名を指定する したがって、これらのガイドラインに従ってORDER BY句が指定されたSQL文が正解となります。 以上より、 ・SELECT department_id FROM departments UNION SELECT employee_id FROM employees ORDER BY department_id; ・SELECT department_id dept FROM departments UNION SELECT employee_id emp FROM employees ORDER BY dept; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id FROM departments UNION SELECT employee_id FROM employees O...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#SQLRF52348

### 問題ID 26729 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26729?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: 次の問合せに有効なORDER BY句はどれですか(該当するものを全て選択して下さい)。 SELECT department_id dept, manager_id mgr FROM departments INTERSECT SELECT department_id dept, employee_id emp FROM employees;
- 解説要約: 集合演算子を用いて複合問合せを行う際にORDER BY句を指定する場合は、次のガイドラインに従います。 ・ORDER BY句は複合問合せの最後の問合せに指定する ・ORDER BY句には最初の問合せに指定されている列名や列別名を指定する したがって、設問のSQL文でORDER BY句に指定できるのは、最初の問合せのSELECT句に指定されている列別名DEPTとMGRの2つということになります。なお、ORDER BY句にはSELECT句に指定した列の位置を指定することもできます。 以上より、 ・ORDER BY 1,2 ・ORDER BY dept,2 ・ORDER BY mgr DESC ・ORDER BY dept DESC が正解となります。 選択肢のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id dept, manager_id mgr FROM departments INTERSECT SELECT department_id dept, employee_id emp FROM employees ORDER BY 1, 2...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries005.htm#sthref2234

### 問題ID 26730 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26730?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せを実行したところ、エラーとなりました。修正後の問合せとして正しいものはどれですか。 SELECT employee_id id, employee_name name, salary, hiredate FROM employees WHERE department_id IN (1, 2, 3) UNION SELECT employee_id, employee_name, salary, TO_CHAR(NULL) FROM employees WHERE hiredate > '03-04-01' ORDER BY id;
- 解説要約: 集合演算子を用いた複合問合せでは、2つの問合せでSELECT句に指定する列や式の数を同数にしなければなりません。また、2つの問合せでSELECT句に指定する列や式のデータ型も同じ、もしくは同じデータ型グループにしなければなりません。ただし、データサイズは異なっていてもエラーとはなりません。 設問のSQL文は、SELECT句の最後に指定されたHIREDATE列とTO_CHAR(NULL)のデータ型がそれぞれDATE型とVARCHAR2型で異なっているためエラーとなります。したがって、データ型を同じにする必要があります。 以上より、 ・SELECT employee_id id, employee_name name, salary, hiredate FROM employees WHERE department_id IN (1, 2, 3) UNION SELECT employee_id, employee_name, salary, TO_DATE(NULL) FROM employees WHERE hiredate > '03-04-01' ORDER BY id; が正解と...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26731 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26731?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せの実行結果はどうなりますか。 SELECT category FROM prod INTERSECT SELECT category FROM oldprod;
- 解説要約: 設問のSQL文はINTERSECT演算子を用いて複合問合せを行なっています。 INTERSECT演算子を用いた複合問合せでは、2つの問合せの結果の共通する行を表示します。したがって、複合問合せの結果は、PROD表の問合せ結果である"10, 20, 30, 40, 50, NULL"とOLDPROD表の問合せ結果である"10, 40, 60, NULL"の共通する行である"10, 40, NULL"が表示されます。 以上より、 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26732 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26732?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せの実行結果はどうなりますか。 SELECT category FROM oldprod UNION (SELECT category FROM oldprod INTERSECT SELECT category FROM prod);
- 解説要約: 集合演算子には優先順位はありませんので、1つのSQL文に複数の集合演算子が使用されている場合は、SQL文の先頭から順番に複合問合せが行われます。 ですが、SQL文に()括弧が使用されている場合は、()括弧で囲まれた部分から問合せを実施します。 設問のSQL文では、()括弧で囲まれたINTERSECT演算子による複合問合せから行われます。 INTERSECT演算子による複合問合せでは、OLDPROD表の問合せ結果である"10, 40, 60, NULL"とPROD表の問合せ結果である"10, 20, 30, 40, 50, NULL"の共通する行である"10, 40, NULL"が返されます。 次に、UNION演算子による複合問合せで、OLDPROD表の問合せ結果である"10, 40, 60, NULL"とINTERSECT演算子による複合問合せ結果の"10, 40, NULL"の重複を除いた値である"10, 40, 60, NULL"が表示されます。 以上より、 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26733 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26733?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次の問合せの実行結果はどうなりますか。 SELECT department_id dept, employee_id emp FROM employees WHERE department_id IN (SELECT department_id FROM departments INTERSECT SELECT department_id FROM employees WHERE salary >= 700000) ORDER BY dept;
- 解説要約: 集合演算子は副問合せでも主問合せと同じように使用することができます。 設問のSQL文は集合演算子を使用する際のガイドラインに従って記述されているので、正常に実行できます。 以上より、 ・正常に実行される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id dept, employee_id emp FROM employees WHERE department_id IN (SELECT department_id FROM departments INTERSECT SELECT department_id FROM employees WHERE salary >= 700000) ORDER BY dept; その他の選択肢については次のとおりです。 ・副問合せでは集合演算子を使用できないため、エラーとなる 副問合せで集合演算子を使用することができるため、誤った記述です。 ・ORDER BY句に列別名が指定されているので、エラーとなる ORDER BY句では列別名を使用することができるため、誤った記述です。 ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26734 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26734?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PROD表とOLDPROD表の構造とデータを確認して下さい。 次の問合せの実行結果はどうなりますか。 SELECT category FROM oldprod UNION SELECT category FROM oldprod INTERSECT SELECT category FROM prod;
- 解説要約: 集合演算子には優先順位はありませんので、1つのSQL文に複数の集合演算子が使用されている場合は、SQL文の先頭から順番に複合問合せが実施されます。 設問のSQL文では、UNION演算子による複合問合せから行われます。 UNION演算子による複合問合せでは、OLDPROD表の問合せ結果をUNION演算子で1つにまとめるので、"10, 40, 60, NULL"が返されます。（OLDPROD表の元のデータのままですので、実際にはこの部分に意味はありません。） 次に、INTERSECT演算子による複合問合せで、UNION演算子による問合せ結果である"10, 40, 60, NULL"とPROD表の問合せ結果である"10, 20, 30, 40, 50, NULL"の共通する行である"10, 40, NULL"が返されます。 以上より、 が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26735 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26735?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: SALES表とCUSTOMERS表の構造を確認して下さい。 次の問合せの結果として、正しいものはどれですか。 SELECT cust_id FROM sales GROUP BY cust_id INTERSECT SELECT customer_id FROM customers WHERE cust_address LIKE '東京都%' MINUS SELECT cust_id FROM sales WHERE prod_id = 1002 ORDER BY 1;
- 解説要約: 複合問合せにおいて、WHERE句、GROUP BY句、ORDER BY句等の使用は禁止されていません。ただし、ORDER BY句を使用する場合には、以下のガイドラインに従います。 ・ORDER BY句は複合問合せの最後の問合せに指定する ・ORDER BY句には最初の問合せに指定されている列名や列別名を指定する 設問のSQL文では、まずINTERSECT演算子による複合問合せが実行され、その結果と3つ目の問合せをMINUS演算子を用いて複合問合せします。最後にORDER BY句により、問合せ結果がソートされます。 以上より、 ・正常に実行される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT cust_id FROM sales GROUP BY cust_id INTERSECT SELECT customer_id FROM customers WHERE cust_address LIKE '東京都%' MINUS SELECT cust_id FROM sales WHERE prod_id = 1002 ORDER BY 1;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26736 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26736?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: PRODUCTS表の構造を確認して下さい。 製品カテゴリが"CD"以外の製品を表示する問合せとして、正しいものはどれですか。
- 解説要約: 選択肢の複合問合せでは、1つ目の問合せではPRODUCTS表から全ての行が、2つ目の問合せではCATEGORY列が"CD"である行が返されます。 この2つの結果をまとめCATEGORY列が"CD"以外の行を返すには、1つ目の問合せから2つ目の問合せの結果にない行を表示すればよいので、MINUS演算子で複合問合せを行えば良いことになります。 以上より、 ・SELECT prod_id, prod_name, prod_category FROM products MINUS SELECT prod_id, prod_name, prod_category FROM products WHERE prod_category = 'CD'; が正解となります。 正解のSQL文の実行結果は次のようになります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators005.htm#i1035612
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries004.htm#i2054381

### 問題ID 26737 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26737?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 実行するとトランザクションが終了する文はどれですか(3つ選択して下さい)。
- 解説要約: トランザクションはCOMMIT文やROLLBACK文実行時やDDL文、DCL文実行時に終了します。 選択肢のうち、CREATE文はDDL文に該当しますが、SELECT文、UPDATE文はDML文です。またSAVEPOINT文ではトランザクション内にマーカーを作成しますが、トランザクションは終了しません。 以上より、 ・ROLLBACK ・COMMIT ・CREATE が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/transact.htm#g11401

### 問題ID 26738 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26738?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 次のSQL文の説明として正しいものはどれですか(該当するものを全て選択して下さい)。 TRUNCATE TABLE employees;
- 解説要約: TRUNCATE文は表の全てのデータを削除します。削除するデータを指定することはできません。 また、TRUNCATE文では処理の取消しができず、ロールバック用のデータを生成する必要がないため、DELETE文よりも高速にデータを削除できます。 TRUNCATE文によって、削除された表が使用していた領域の割り当ては解除されます。 以上より、 ・表のデータが全て削除される ・表が使用していた領域が解放される が正解となります。 その他の選択肢については次のとおりです。 ・削除トリガーが実行される 削除トリガーはDELETE文でデータを削除した時に実行されるプログラムです。TRUNCATE文でデータを削除した場合は実行されません。 ・ロールバック情報が生成される TRUNCATE文は処理の取消しができないため、ロールバック情報は生成されません。 ・表に作成されている索引や制約、トリガーが削除される TRUNCATE文では表のデータを削除しますが、索引や制約、トリガーは削除されず残ります。 ・FLASHBACK TABLE文でごみ箱から復元できる 「DROP TABLE 表名;」で表を削除した場...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10007.htm#SQLRF01707

### 問題ID 26739 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26739?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: トランザクション制御文とその説明の組合せとして、正しいものはどれですか。 トランザクション制御文： 1.COMMIT 2.ROLLBACK 3.SAVEPOINT 4.ROLLBACK TO SAVEPOINT 説明文： a. トランザクション内にマーカーを作成する b. 処理を確定しトランザクションを終了する c. 処理を取消しトランザクションを終了する d. マーカー以降の処理を取消す
- 解説要約: トランザクションは次のトランザクション制御文を使用して明示的に制御することができます。 以上より、 ・4 と d が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/transact.htm#CNCPT1118

### 問題ID 26740 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26740?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 次のSQL文を実行した時の説明として、正しいものはどれですか。 SQL> INSERT INTO prod VALUES(10, 'Bach', 10, SYSDATE, NULL); … ① SQL> COMMIT; … ② SQL> SELECT * FROM prod; … ③ SQL> ROLLBACK; … ④ SQL> SELECT * FROM prod; … ⑤
- 解説要約: ①で追加したデータは②のCOMMIT文で確定され取消すことができません。ですので、④でROLLBACK文を実行しても、⑤の問合せ時には①で追加したデータも表示されます。 以上より、 ・②を実行すると、処理が確定され、①のデータ追加処理を取り消すことができない ・③を実行すると、①で追加したデータも表示される が正解となります。 設問のSQL文を順に説明します。 ①：INSERT文により、PROD表にデータが1件追加されます。ただし、INSERT文はDML文に該当し自動コミットされないため、データの追加は確定されていない状態です。 ②：COMMIT文により、それまでの処理が確定されます。①で追加したデータはこのCOMMIT文で確定されますので、取消すことはできません。 ③：SELECT文による問い合わせの結果、PROD表の全てのデータが表示されます。①で追加したデータも表示されます。 ④：ROLLBACK文により、②のCOMMIT文より後で実行した処理が取消されます。ただし②のCOMMITの後に実施した処理は③の問合せのみですので、PROD表のデータは③から変更がありません。 ⑤：SEL...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_4010.htm#SQLRF01110
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9021.htm#SQLRF01610

### 問題ID 26741 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26741?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次のSQL文を実行した時に、CATEGORY列の値が"60"と表示されるSELECT文はどれですか(該当するものを全て選択して下さい)。 1. SQL> INSERT INTO prod VALUES(10, 'Bach', 10, SYSDATE, NULL); 2. SQL> UPDATE prod SET category = 60 WHERE prodid = 10; 3. SQL> SELECT * FROM prod WHERE prodid = 10; … ① 4. SQL> COMMIT; 5. SQL> SELECT * FROM prod...
- 解説要約: 設問のSQL文を順に説明します。 1. SQL> INSERT INTO prod VALUES(10, 'Bach', 10, SYSDATE, NULL); 2. SQL> UPDATE prod SET category = 60 WHERE prodid = 10; 3. SQL> SELECT * FROM prod WHERE prodid = 10; … ① 4. SQL> COMMIT; 5. SQL> SELECT * FROM prod WHERE prodid = 10; … ② 6. SQL> UPDATE prod SET category = 70 WHERE prodid = 10; 7. SQL> COMMIT; 8. SQL> SELECT * FROM prod WHERE prodid = 10; … ③ 9. SQL> UPDATE prod SET category = 60 WHERE prodid = 10; 10. SQL> ROLLBACK; 11.SQL> COMMIT; 12.SQL> SELECT * FROM prod WHER...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_4010.htm#SQLRF01110
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9021.htm#SQLRF01610

### 問題ID 26742 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26742?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: トランザクション終了後の説明として、正しいものはどれですか(該当するものを3つ選択してください)。
- 解説要約: トランザクションの終了時、トランザクション内のすべてのセーブポイントが破棄され、書込み処理時の排他ロックが解除されます。また、確定したデータの変更は取り消しすることはできません。 以上より、 ・全てのセーブポイントは破棄される ・すべての処理が確定または破棄され、取消すことはできない ・書込み処理をした行はロックが解除され、他のユーザーは変更したデータを参照できる が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/transact.htm#CNCPT1118

### 問題ID 26743 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26743?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(該当するものを全て選択して下さい)。 なお、それぞれのユーザは、Oracleへの接続には同一アカウント(pingt）を使用して同じデータにアクセスしているものとします。 ユーザーA： SQL> SELECT prodid, name, category FROM prod WHERE prodid = 2 2 FOR UPDATE WAIT 10; … ① ユーザーB： SQL> SELECT * FROM prod WHERE prodid = 2 2 FOR UPDATE NOWAIT; … ② SQL> UPDATE p...
- 解説要約: 設問のSQL文を1つずつ確認してみましょう。 ユーザーA： SQL> SELECT prodid, name, category FROM prod WHERE prodid = 2 2 FOR UPDATE WAIT 10; … ① ユーザーB： SQL> SELECT * FROM prod WHERE prodid = 2 2 FOR UPDATE NOWAIT; … ② SQL> UPDATE prod SET name = 'Chopin' WHERE prodid = 2; … ③ ユーザーA： SQL> COMMIT; ユーザーB： SQL> COMMIT; ①：SELECT文にFOR UPDATE句が指定されているので、SELECT文で取り出される行に排他ロックがかけられます。 ②：①でユーザーAが排他ロックをかけているため、ユーザーBはSELECT文にFOR UPDATE句を指定しても排他ロックをかけることはできません。さらにNOWAITオプションを指定しているので、SELECT文実行後、直ちにエラーとなります。 ③：①でユーザーAが排他ロックをかけているため、ユーザ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55370

### 問題ID 26744 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26744?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(該当するものを全て選択して下さい)。 なお、それぞれのユーザは、Oracleへの接続には同一アカウント(pingt）を使用して同じデータにアクセスしているものとします。 ユーザーA： SQL> SELECT d.department_name, e.employee_name 2 FROM departments d JOIN employees e USING (department_id) 3 FOR UPDATE OF e.employee_name NOWAIT; … ① ユーザーB： SQL> SELECT empl...
- 解説要約: 設問のSQL文を1つずつ確認してみましょう。 ユーザーA： SQL> SELECT d.department_name, e.employee_name 2 FROM departments d JOIN employees e USING (department_id) 3 FOR UPDATE OF e.employee_name NOWAIT; … ① ユーザーB： SQL> SELECT employee_id, employee_name FROM employees 2 FOR UPDATE NOWAIT; … ② SQL> SELECT department_id, department_name FROM departments 2 FOR UPDATE NOWAIT; … ③ ユーザーA： SQL> UPDATE employees SET salary = 350000 WHERE employee_id = 1020; SQL> COMMIT; ①：SELECT文のFOR UPDATE句に OF 表名.列名 オプションが指定されています。EMPLOYEES表のEM...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55370

### 問題ID 26745 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26745?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表にデータを追加するSQL文として、誤っているものはどれですか。
- 解説要約: INSERT文のVALUES句では、関数を使用することもできます。関数を使用する場合は、列のデータ型と関数が返す値の型が一致しなければなりません。 選択肢のSQL文では、SYSDATE、TO_DATE、TO_NUMBERなどの関数を使用してデータを追加しています。 そのうち、TO_DATE関数の結果をCATEGORY列に登録するSQL文がありますが、CATEGORY列はNUMBER型の列であるため、DATE型の値を登録できません。そのためエラーとなります。 以上より、 ・INSERT INTO prod(prodid, name, category, startdate) VALUES (30, 'Pokemon', TO_DATE('05-03-25', 'RR-MM-DD'), SYSDATE); が正解となります。 正解のSQL文の実行結果は次のようになります。 ちなみに、次のSQL文ではVARCHAR2型のNAME列にTO_NUMBER関数の結果(NUMBER型)を登録していますが、暗黙的データ変換により、NUMBER型がVARCHAR2型に変換されて登録されるため、エラーとは...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm#SQLRF01604

### 問題ID 26746 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26746?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表と同じ構造をもつPROD2表を作成し、PROD表のデータをコピーします。 正常に実行されるSQL文はどれですか(該当するものを全て選択して下さい)。
- 解説要約: 副問合せを使用してデータの追加を行うこともできます。 その場合、次のように記述します。 INSERT INTO 表名1 [(列名 [, 列名...])] (SELECT 列名 [, 列名...] FROM 表名2 [WHERE 条件]); なお、副問合せの部分を囲む()は必須ではありません。 副問合せを使用したINSERT文では、VALUES句は使用できません。 INSERT句に指定する列のリストと、副問合せのSELECT句に指定する列のリストは同数かつ同じ順番で指定します。 また、INSERT句の列のリストは省略可能ですが、省略する場合、副問合せのSELECT句の列のリストには、データを追加する表のすべての列を表の列構成の順番で指定しなければなりません 以上より、 ・INSERT INTO prod2 SELECT * FROM prod; ・INSERT INTO prod2(prodid, name, category) (SELECT prodid, name, category FROM prod); が正解となります。 正解のSQL文の実行結果は次のようになります。 注意)...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm

### 問題ID 26747 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26747?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表とOLDPROD表の構造を確認して下さい。 次のSQL文の実行結果と等しい結果となるものはどれですか。 SELECT p.category, p.name, o.name FROM prod p CROSS JOIN oldprod o;
- 解説要約: CROSS JOINキーワードで表の結合を行うと、2つの表に登録されている行の全ての組合せ(デカルト積といいます)を返すクロス結合が行われます。 クロス結合では、2つの表に登録されている行の全ての組合せを返す結合ですので、結合条件を指定せずに表を結合した場合の結果と等しくなります。 以上より、 ・SELECT p.category, p.name, o.name FROM prod p, oldprod o; が正解となります。 設問のPROD表とOLDPROD表のデータの登録件数はそれぞれ以下の通りです。 SQLを表示 SELECT COUNT(*) FROM prod; SQLを表示 SELECT COUNT(*) FROM oldprod; 設問のSQL文と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT p.category, p.name, o.name FROM prod p CROSS JOIN oldprod o; SQLを表示 SELECT p.category, p.name, o.name FROM prod p, oldprod o; ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52352
  - https://gihyo.jp/dev/serial/01/sql_academy2/001001

### 問題ID 26748 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26748?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROD表とCATEGORY表の構造を確認して下さい。 次のSQL文を実行したところ、エラーとなりました。エラーの原因は何ですか。 SELECT category, name FROM category JOIN prod ON category.category = prod.category;
- 解説要約: ON句を使用した表の結合において、結合する2つの表の両方に同名の列がある場合、同名の列をSELECT句やWHERE句に指定する場合には表接頭辞を付加して指定しなければなりません。 設問のSQL文のSELECT句にCATEGORY列、NAME列が指定されていますが、これらの列はCATEGORY表にもPROD表にも存在するため、表接頭辞を付加して指定しないとエラーとなります。 以上より、 ・SELECT句に指定した列に表接頭辞を付加していないため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT category, name FROM category JOIN prod ON category.category = prod.category; その他の選択肢については次のとおりです。 ・結合条件に同名の列を指定する場合は自然結合で結合しなければならないため ・結合条件に同名の列を指定する場合はUSING句で指定しなければならないため このような制限はありません。 ・WHERE句を指定していないため WHERE句の指定は必須ではありませんので...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#i2054012

### 問題ID 26749 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26749?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 UPDATE (SELECT department_id, employee_id FROM employees) SET salary = (SELECT MIN(salary) FROM employees) WHERE department_id IN (SELECT department_id FROM departments);
- 解説要約: UPDATE文では、更新の対象となる表を指定する際、表名ではなく副問合せを指定することができます。 表名の代わりに副問合せを指定したUPDATE文では、副問合せで取り出された列しかSET句に指定することができません。 設問のSQL文では、UPDATE句の副問合せでEMPLOYEES表のDEPARTMENT_ID列とEMPLOYEE_ID列が取り出されるので、SET句にはこの2つの列しか指定することができませんが、SET句にSALARY列を指定しているためエラーとなります。 以上より、 ・UPDATE句の副問合せのSELECT句に指定された列しか変更できないため、エラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 UPDATE (SELECT department_id, employee_id FROM employees) SET salary = (SELECT MIN(salary) FROM employees) WHERE department_id IN (SELECT department_id FROM departments...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm

### 問題ID 26750 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26750?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 次のSQL文と同じ結果となるSQL文はどれですか。 UPDATE employees SET (salary, commission) = (SELECT salary * 1.2, commission + 200000 FROM employees WHERE employee_id = 1010) WHERE department_id = 5;
- 解説要約: 設問のSQL文では、複数の列を返す副問合せを使用してデータの更新を行なっています。 このようなSQL文は、更新する列ごとに副問合せを指定するSQL文に置き換えることができます。 以上より、 ・UPDATE employees SET salary = (SELECT salary * 1.2 FROM employees WHERE employee_id = 1010), commission = (SELECT commission + 200000 FROM employees WHERE employee_id = 1010) WHERE department_id = 5; が正解となります。 設問と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT salary, commission FROM employees WHERE department_id = 5; SQLを表示 UPDATE employees SET (salary, commission) = (SELECT salary * 1.2, commission + 200000 F...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF01708

### 問題ID 26751 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26751?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEE_ID列の値が1015である従業員のSALARY列とCOMMISSION列の値を変更します。 SALARY列はEMPLOYEE_ID列が1008の従業員の1.1倍に、COMMISSION列はEMPLOYEE_ID列が1011の従業員と同じ値に変更するには、どのSQL文を実行しますか。
- 解説要約: 他のデータに基いて表の値を更新する場合は、副問合せを使用してデータを更新します。 SALARY列、COMMISSION列はそれぞれ異なるデータに基いて更新するため、SALARY列の更新に使用する副問合せとCOMMISSION列の更新に使用する副問合せを用意しなければなりません。 以上より、 ・UPDATE employees SET salary = (SELECT salary * 1.1 FROM employees WHERE employee_id = 1008), commission = (SELECT commission FROM employees WHERE employee_id = 1011) WHERE employee_id = 1015; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT salary, commission FROM employees WHERE employee_id = 1015; UPDATE employees SET salary = (SELECT salary * 1.1 FR...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF01708

### 問題ID 26752 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26752?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表からデータを削除するSQL文として、エラーが発生するものはどれですか。
- 解説要約: DELETE文ではWHERE句に削除するデータの条件を指定して実行することができますが、TRUNCATE文は削除するデータの条件を指定することができません。WHERE句を指定するとエラーとなります。 以上より、 ・TRUNCATE TABLE prod WHERE category = 30; が正解となります。 正解のSQLの実行結果は次のようになります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10007.htm#SQLRF01707
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF01505

### 問題ID 26753 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26753?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: スキーマに関する説明として、正しいものはどれですか。
- 解説要約: 表やビュー等のスキーマ・オブジェクトは必ずいずれかのユーザーに所有されています。スキーマとは、オブジェクトの所有者を表す論理的な概念です。 自分以外のユーザーが所有しているオブジェクトを参照する場合は、オブジェクト名に接頭辞としてスキーマ名をつけて「スキーマ名.オブジェクト名」のように参照しなければなりません。 以上より、 ・他のユーザーが所有する表を参照するときには、スキーマ名を接頭辞として参照する が正解となります。 その他の選択肢については次のとおりです。 ・オブジェクトを格納する領域である オブジェクトを格納する領域を記憶域といいます。記憶域はスキーマ・オブジェクトではありません。 ・スキーマが異なっていても、同じ表名は使用できない 表名はスキーマ内で一意でなければなりませんが、異なるスキーマでは同じ表名を使用することができます。 ・SELECT文で問合せを行う際に、スキーマを指定しない場合はSYSTEMユーザーの表を参照する スキーマ名を指定しない場合は、ログインしているユーザーが所有している表を参照します。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/tablecls.htm#i22627
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements007.htm#SQLRF51127

### 問題ID 26754 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26754?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: オブジェクト作成時に、オブジェクト名として使用できるものはどれですか(該当するものを全て選択して下さい)。 ただし、オブジェクト名は二重引用符(") で囲まない場合とします。
- 解説要約: オブジェクト名は以下の命名規則に従う必要があります。 ・オブジェクト名は30バイト以下（12c R2以降は128バイト以下） ・使用できる文字は、0~9,A~Z,a~z(日本語環境の場合は漢字,ひらがな,カタカナも使用可) ・使用できる記号は、_,$,#のみ ・オブジェクト名の先頭の文字は、数字,記号以外の文字 ・Oracleの予約語は使用できない この他、同一スキーマ内では重複するオブジェクト名は使用できません。また、アルファベットの大文字と小文字は区別されません。 大文字と小文字を区別したり、スペースを含めるなどネーミング規則に反する列別名を使用する場合は、オブジェクト名を 二重引用符(") で囲まなければなりません。 以上より、 ・EMP_ ・Dept が正解となります。 その他の選択肢については次のとおりです。 ・2012DEPT ・[employees] オブジェクト名の先頭の文字に数字や記号は使用できません。また、"[]"はオブジェクト名に使用できません。 SQLを表示 CREATE TABLE 2012DEPT (id NUMBER(2), name VARCHAR2(1...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements008.htm#SQLRF51129

### 問題ID 26755 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26755?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: オブジェクト名に関する説明として、正しいものはどれですか。
- 解説要約: オブジェクト名はスキーマ内で一意である必要があります。そのため、スキーマ内の表やビューに同じ名前を使用することはできません。ですが、異なるスキーマ同士では同じオブジェクト名を使用することができます。 ※例外として、索引や制約などは種類の異なるオブジェクトであれば、スキーマ内で同じオブジェクト名を使用することが可能です(同一スキーマ内で表と索引に同じオブジェクト名を使用することができます)。 以上より、 ・オブジェクト名はスキーマ内で一意でなければならない が正解となります。 その他の選択肢については次のとおりです。 ・スキーマ内で表とビューに同じ名前を使用することができる 同一スキーマ内で表とビューに同じ名前を使用することはできません。 ・スキーマが異なっていても、同じオブジェクト名は使用できない 異なるスキーマ同士では同じオブジェクト名を使用することができます。 ・表名と同じ列名は使用できない 列名はスキーマ・オブジェクトでは無い為、表名と同じ名前を使用することができます。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Database-Object-Names-and-Qualifiers.html#SQLRF51129

### 問題ID 26756 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26756?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: CHAR型とVARCHAR2型について、正しいものはどれですか。
- 解説要約: CHAR型、VARCHAR2型の特徴は次の通りです。 以上より、 ・VARCHAR2型は可変長のデータ型であるのに対し、CHAR型は固定長のデータ型である が正解となります。 その他の選択肢については次のとおりです。 ・指定できる値の最大サイズはどちらも4,000バイトである CHAR型の最大サイズは2,000バイトです。 ・VARCHAR2型のデフォルトのサイズは1である VARCHAR2型は定義時にサイズを省略することができないため、デフォルトのサイズはありません。 デフォルトのサイズが"1"なのはCHAR型です。 ・CHAR型はサイズを省略することはできない CAHR型は定義時にサイズを省略することができます。省略した場合のデータサイズは"1"となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/tablecls.htm#CBBEICCJ
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF50973

### 問題ID 26757 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26757?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 SELECT INTERVAL '200' MONTH, INTERVAL '50-11' YEAR TO MONTH, INTERVAL '4 12:30:10.1234567' DAY TO SECOND FROM dual;
- 解説要約: 期間を表す値を記述するには、期間リテラルの書式に基いて記述します。 設問のINTERVAL '200' MONTHは200ヶ月間の意味なので、16年8ヶ月を表すINTERVAL ’16-8’ YEAR TO MONTHと同義です。 なお、期間データ型には書式モデルはありません。SELECT文で期間データ型を表示させると、 INTERVAL ’16-8’ YEAR TO MONTH は +16-8 INTERVAL '50-11' YEAR TO MONTH は +50-11 INTERVAL '4 12:30:10.1234567' DAY TO SECOND は +04 12:30:10.123457 ※SECOND(秒フィールド)の精度はデフォルトで秒の小数点以下6桁のため、秒の小数点以下に「1234567」(7桁)を指定すると「123457」(6桁)に切り上げられます。 のように表示されます。 以上より、 ・+16-08 +50-11 +04 12:30:10.123457 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT INTER...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00206
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00207
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#SQLRF00221

### 問題ID 26758 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26758?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: データ型に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: CHAR型は最大2,000バイトまでの文字データを格納できる固定長のデータ型です。CHAR(5)に「abc」が格納されると、データの末尾に空白を追加し、長さが5バイトの「abc 」を格納します。 また、LONG型は最大2GBまでの文字データを格納できる可変長のデータ型ですが、次のような制約があります。 ・LONG型の列は1つの表に1つだけ定義できる ・LONG型の列には制約は定義できない(NULLおよびNOT NULL制約を除く) ・LONG型の列はGROUP BY句とORDER BY句に指定できない ・副問合せによる表の作成時、LONG型の列はコピーできない 以上より、 ・CHAR(5)に「abc」を入力すると、スペースを加え「abc 」が格納される ・LONG型の列には、NULLおよびNOT NULL以外の制約を定義できない が正解となります。 その他の選択肢については次のとおりです。 ・BFILE型は4GBまでにバイナリデータを格納でき、値を自由に変更することができる BFILE型は4GBまでにバイナリデータを格納できますが、読取り専用のデータ型ですので、値の変更はできません。 ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/tablecls.htm#CBBCFGEJ
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i54330

### 問題ID 26759 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26759?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 次のようなデータを格納するために適切なデータ型はどれですか。 ・図書の分類ごとに貸出可能期間を格納する ・図書の貸出日(DATE型)に関数を使用せずに貸出可能期間を加算でき、返却日を求めることができる ・最長の貸出期間は20日である
- 解説要約: 期間を格納するデータ型には、 ・INTERVAL YEAR TO MONTH：期間を年、月の単位で格納する ・INTERVAL DAY TO SECOND：期間を日、時、分、秒の単位で格納する があります。 期間を表すデータ型はDATE型との演算が可能です。例えば、「〇年△ヶ月」の期間を表すデータ型を使って現在の日時に加算することで、わかりやすく「〇年△ヶ月」経過後の日時を取得することができます。減算した場合は過去の日時となります。 設問で最長の貸出可能期間は20日ということですので、日の単位で期間を格納できるINTERVAL DAY TO SECOND型の変数を定義すれば良いことがわかります。 以上より、 ・INTERVAL DAY TO SECOND が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00206
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00207

### 問題ID 26760 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26760?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 制約とその説明の組合せとして、正しいものはどれですか(該当するものを全て選択して下さい)。 [制約] 1. NOT NULL 2. UNIQUE 3. PRIMARY KEY 4. FOREIGN KEY 5. CHECK [説明] a. NULL値を許可しない b. 重複値およびNULL値を許可しない c. 参照先の列に登録されている値またはNULL値のみ許可する d. 指定した条件に合う値のみ許可する e. 重複値は許可しないがNULL値は許可する
- 解説要約: Oracle Databaseでは、次の制約を定義することができます。 以上より、 ・1 と a ・4 と c が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#g20134
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52180

### 問題ID 26761 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26761?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 制約に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: Oracle Databaseでは、制約を列レベル、表レベルで定義することができます。 また、1つの列に1つまたは複数の制約を定義することができます。 複数の列の組み合わせに対して制約を定義することもできますが、その場合は、表レベルで定義しなければなりません。 なお、NOT NULL制約は列レベルでしか定義できません。 以上より、 ・1つの列に複数の制約を定義できる ・NOT NULL制約は列レベルでのみ定義できる ・複数の列の組合せに対して制約を定義できる が正解となります。 その他の選択肢については次のとおりです。 ・複数の列の組み合わせに対しての制約は列レベルで定義できる 複数の列の組み合わせに対しての制約は、表レベルでのみ定義することができます。 ・制約は表の作成時しか定義できない 制約は表作成時だけではなく、表の作成後も定義できます。その場合は既に登録されているデータが制約のルールを満たしていなければなりません。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#g20134
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52180

### 問題ID 26762 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26762?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を実行したところ、エラーとなりました。エラーの原因は何ですか。 CREATE TABLE temp ( column1 NUMBER(2), column2 VARCHAR2(10), NOT NULL (column1, coloumn2) );
- 解説要約: NOT NULL制約は列レベルでしか定義することができません。 設問のSQL文では、表レベルでNOT NULL制約を定義しているため、エラーとなります。 以上より、 ・表レベルでNOT NULL制約を定義しているため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE temp (column1 NUMBER(2), column2 VARCHAR2(10), NOT NULL (column1, coloumn2) ); その他の選択肢については次のとおりです。 ・制約名を定義していないため 制約名は省略することができます。制約名を省略した場合は、「SYS_Cn」という制約名となります。 ・PRIMARY KEY制約を定義した列が1つもないため 表にPRIMARY KEY制約は必ずしも定義する必要はありません。 ・VARCHAR2型が含まれる表にNOT NULL制約を定義しているため NOT NULL制約が定義できる列のデータ型に制限はありません。表レベルでのNOT NULL制約は定義できませんが、VARCHAR2型の列にNOT...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDJDDGH
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF30038

### 問題ID 26763 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26763?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文でPARENT表を作成しました。 CREATE TABLE parent ( id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); PARENT表を参照するCHILD表を作成するSQL文のうち、エラーとなるものはどれですか。
- 解説要約: FOREIGN KEY制約で参照できる親表の列は、PRIMARY KEY制約またはUNIQUE制約が定義されている列だけです。FOREIGN KEY制約の参照先にPRIMARY KEY制約またはUNIQUE制約が定義されていない列を指定するとエラーとなります。 以上より、 ・CREATE TABLE child ( id NUMBER(2), name VARCHAR2(10), deptid NUMBER(2), deptname VARCHAR2(10), CONSTRAINT dept_fk FOREIGN KEY (deptid, deptname) REFERENCES parent (id, dept_name) ); が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE parent (id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); CREATE TABLE child (id NUMBER(2), name VARCHAR2(...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDIIGBG
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52199

### 問題ID 26764 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26764?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文でPARENT表とCHILD表を作成しました。 CREATE TABLE parent ( id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); CREATE TABLE child ( id NUMBER(2) CONSTRAINT cid_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT cname_uq UNIQUE, deptid NUMBER(2) CONSTRAINT dept_fk REFERENCES parent (id) ON DELET...
- 解説要約: FOREIGN KEY制約の親表として指定された表は、参照されている行がない場合でも削除できなくなります。親表を削除する場合は、参照している子表を先に削除しなければなりません。 設問では、CHILD表がPARENT表を参照しているので、PARENT表を削除する前にCHILD表を削除しなければなりません。PARENT表を先に削除するとエラーとなります。 以上より、 ・エラーとなり、表もデータも削除されない が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#CHDIIGBG
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52199

### 問題ID 26765 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26765?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 制約に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: Oracle Databaseでは、次の制約を定義することができます。 PRIMARY KEY制約では、NULL値を格納できないのに対し、UNIQUE制約やFOREIGN KEY制約では制約を定義した列にNULL値を格納することができます。 以上より、 ・UNIQUE制約が定義されている列にNULL値を格納できる ・FOREIGN KEY制約が定義されている列にNULL値を格納できる が正解となります。 その他の選択肢については次のとおりです。 ・CHECK制約にCURRVALなどの疑似列を指定することができる CHECK制約に指定できる条件にはいくつかの制限があります。CURRVAL,NEXTVAL,LEVEL,ROWNUM疑似列の参照はできません。 ・表の作成時、PRIMARY KEY制約は必ず定義しなければならない PRIMARY KEY制約は必ず指定する必要はありません。 ・NOT NULL制約は表レベルで定義できる NOT NULL制約は列レベルでしか定義することができません。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56306/datainte.htm#g20134
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52180

### 問題ID 26766 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26766?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文のうち、正常に実行されるものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: オブジェクト名は以下の命名規則に従う必要があります。 ・オブジェクト名は30バイト以下（12c R2以降は128バイト以下） ・使用できる文字は、0~9,A~Z,a~z(日本語環境の場合は漢字,ひらがな,カタカナも使用可) ・使用できる記号は、_,$,#のみ ・オブジェクト名の先頭の文字は、数字,記号以外の文字 ・Oracleの予約語は使用できない この他、同一スキーマ内では重複するオブジェクト名は使用できません。また、アルファベットの大文字と小文字は区別されません。 大文字と小文字を区別したり、スペースを含めるなどネーミング規則に反する列別名を使用する場合は、オブジェクト名を 二重引用符(") で囲まなければなりません。 以上より、 ・CREATE TABLE temp#123 (id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY); ・CREATE TABLE temp_123 (temp_123 NUMBER(2) CONSTRAINT id_pk PRIMARY KEY); が正解となります。 選択肢の、 CREATE TABLE temp_12...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements008.htm#SQLRF51129

### 問題ID 26767 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26767?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: EMP表の構造を確認して下さい。 CREATE TABLE emp ( id NUMBER(2) PRIMARY KEY, name VARCHAR2(10), birth DATE, salary NUMBER(8), note LONG ); EMP表に関する説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: LONG型の列には以下の制限があります。 ・LONG型の列は1つの表に1つだけ定義できる ・LONG型の列には制約は定義できない(NULLおよびNOT NULL制約を除く) ・LONG型の列はGROUP BY句とORDER BY句に指定できない ・副問合せによる表の作成時、LONG型の列はコピーできない 以上より、 ・ORDER BY句にNOTE列を指定できない ・NOTE列にUNIQUE制約を指定できない が正解となります。 その他の選択肢については次のとおりです。 ・EMP表に新たにLONG型の列を追加できる EMP表には既にLONG型の列が定義されているので、新たにLONG型の列を追加することはできません。 ・GROUP BY句にNOTE列を追加できる NOTE列はLONG型の列なので、GROUP BY句に指定することはできません。 ・NOTE列にUNIQUE制約を指定できる NOTE列はLONG型の列なので、制約を定義することはできません。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00201

### 問題ID 26768 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26768?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 以下のSQL文でEMPLOYEES2表を作成し、データを登録します。 CREATE TABLE employees2 ( emp_id NUMBER(2) NOT NULL, name VARCHAR2(10) NOT NULL, birth DATE ); INSERT INTO employees2 VALUES(1, 'Tanaka', '1995-05-18'); INSERT INTO employees2 VALUES(2, 'Tanaka', '1979-12-10'); INSERT INTO employees2 VALUES(1, 'Yamada', '1999-01-31...
- 解説要約: EMPLOYEES2表のEMP_ID列には重複した値のデータが登録されています。 PRIMARY KEY制約が定義された列には重複したデータやNULL値は格納できませんので、EMP_ID列にはPRIMARY KEY制約を定義することはできません。 以上より、 ・既存のデータがPRIMARY KEY制約を満たしていないため、エラーとなる が正解となります。 既にデータが登録されている表に後から制約を追加する事はできますが、登録されているデータが追加する制約の条件を満たしている必要がありますので注意して下さい。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE employees2 (emp_id NUMBER(2) NOT NULL, name VARCHAR2(10) NOT NULL, birth DATE ); INSERT INTO employees2 VALUES(1, 'Tanaka', '1995-05-18'); INSERT INTO employees2 VALUES(2, 'Tanaka', '1979-12-10'); IN...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_3001.htm#SQLRF01001

### 問題ID 26769 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26769?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文実行後、EMPLOYEES2表に実施できる行為はどれですか。 ALTER TABLE employees2 READ ONLY;
- 解説要約: 設問のSQL文を実行すると、EMPLOYEES2表は読取り専用モードに変更されます。 読取り専用モードの表では、データの追加、更新、削除はできませんが、表の削除は行うことができます。 以上より、 ・表の削除 が正解となります。 以下は実行例です。 設問のSQL文を実行後、表にデータを追加することはできませんが、表の削除は行えます。 SQLを表示 ALTER TABLE employees2 READ ONLY; INSERT INTO employees2 VALUES (3, 'Yamada', '1999-01-31');
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_3001.htm#SQLRF53333

### 問題ID 26770 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26770?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: 単一ビューに関する説明として、正しいものはどれですか。
- 解説要約: 単一ビューとは、1つの実表から作成され、GROUP BY句や関数を使用していないビューのことです。 例外もありますが、単一ビューを通して実表のデータの追加や更新、削除を行うことができます。 以上より、 ・ビューを通じて実表のデータを操作できる が正解となります。 その他の選択肢については次のとおりです。 ・GROUP BY句を使用している ・2つ以上の表から作成している ・関数を使用している これらは複合ビューの説明です。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/admin/managing-views-sequences-and-synonyms.html#GUID-D925865C-D627-43D0-A71A-C690DA2FCD42

### 問題ID 26771 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26771?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: 複合ビューに分類されるビューの説明として、正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 複合ビューとは、単一ビュー以外のビューのことで、2つ以上の実表を基にして作成したビューや、1つ以上の実表を基にしGROUP BY句や関数を使用して作成したビューのことです。 複合ビューでは、ビューを通じての実表のデータの追加や更新、削除は、特定の条件を満たしている場合のみ可能です。 以上より、 ・GROUP BY句を使用している ・関数を使用している が正解となります。 その他の選択肢については次のとおりです。 ・必ず2つ以上の実表を基にして作成される 1つの実表を基にして作成した場合でも、GROUP BY句や関数を使用して作成したビューは複合ビューと言います。 ・常にビューを通じて実表のデータを操作できる 複合ビューでは、特定の条件を満たした場合のみ、ビューを通じて実表のデータの編集や削除を行うことができます。
- 参考URL: なし

### 問題ID 26772 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26772?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文のうち、正常に実行されるものはどれですか。
- 解説要約: CREATE VIEW文でビューを作成する場合は、次の点に注意が必要です。 ・副問合せのSELECT句に計算式や関数を指定する場合は、CREATE VIEW文で別名を指定するか、SELECT句の計算式や関数に列別名を指定する ・ビューの列名を定義する場合は、副問合せのSELECT句に指定する列の数と同数の列名を定義する 以上より、 ・CREATE VIEW v_emp AS SELECT employee_id, employee_name, salary*12 sal, hiredate FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・CREATE VIEW v_emp (id, name, sal, hireadte) AS SELECT * FROM employees WHERE salary >= 500000; 指定したビューの列名と、副問合せのSELECT句に指定した列名の個数が異なるため、エラーとなります。 ・CREATE VIEW v_emp AS SELECT emplo...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/admin/managing-views-sequences-and-synonyms.html#GUID-183AFB09-7E0B-4E50-A23A-A9FD469B1796
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF01504

### 問題ID 26773 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26773?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 部署名、従業員番号、従業員名、月収を表示するビューを作成するには、どのSQL文を実行しますか。
- 解説要約: 設問の要件を満たすビューを作成するには、DEPARTMENTS表から部署名を、EMPLOYEES表から従業員番号、従業員名、月収を取得しなければならないため、2つの表を基にした複合ビューを作成します。 2つの表を基に複合ビューを作成するには、2つの表を結合した問合せをCREATE VIEW文の副問合せに指定します。 以上より、 ・CREATE VIEW v_emp (dept, id, name, salary) AS SELECT d.department_name, e.employee_id, e.employee_name, e.salary FROM departments d JOIN employees e ON d.department_id = e.department_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE VIEW v_emp (dept, id, name, salary) AS SELECT d.department_name, e.employee_id, e.employee_name, e....
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/admin/managing-views-sequences-and-synonyms.html#GUID-183AFB09-7E0B-4E50-A23A-A9FD469B1796
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF01504

### 問題ID 26774 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26774?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: 次の2つのSQL文をSQL1),SQL2)の順で実行しました。 実行結果として正しいものはどれですか。 SQL1) CREATE OR REPLACE VIEW v_emp AS SELECT department_id, AVG(salary) avg_sal FROM employees GROUP BY department_id; SQL2) CREATE OR REPLACE VIEW v_emp AS SELECT employee_name, salary, hiredate FROM employees WHERE hiredate >= '2008-04-01';
- 解説要約: ビューの作成時、OR REPLACEオプションを指定すると、既に同名のビューが存在する場合でもエラーとならず、ビューの定義を新しい定義で置き換えることができます。 同名のビューが存在しない場合は、新しいビューを作成します。 設問のSQL文では、SQL1)でOR REPLACEオプション付きでV_EMPビューを作成しています。もしもV_EMPビューが既に存在していたとしても、V_EMPビューはSQL1)の定義で置き換えられます。 次にSQL2)ですが、こちらのCREATE VIEW文もOR REPLACEオプション付きでV_EMPビューを作成していますので、SQL1)で作成したV_EMPビューをSQL2)の定義で置き換えます。 以上より、 ・どちらも正常に実行され、SQL2)の内容でV_EMPビューが作成される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE OR REPLACE VIEW v_emp AS SELECT department_id, AVG(salary) avg_sal FROM employees GROUP BY d...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54760

### 問題ID 26775 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26775?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文でEMPLOYEES表を実表とするV_EMPビューを作成しました。 CREATE OR REPLACE VIEW v_emp AS SELECT department_id, employee_id, employee_name, salary FROM employees WHERE salary > 250000 AND salary < 800000 AND department_id = 1 WITH CHECK OPTION; V_EMPビューに対して、エラーとならずに実行できるSQL文はどれですか(該当するものを全て選択して...
- 解説要約: ビューの作成時、WITH CHECK OPTIONオプションを指定すると、ビューを通じて実表のデータを操作する場合に、ビューの定義時に指定したWHERE句の条件を満たしていないデータの追加や更新ができなくなります。 V_EMPビューは、 ・SALARY列の値が250,000より大きく800,000より小さい ・DEPARTMENT_ID列の値が1 という条件が指定されているので、この条件を満たすデータの追加、更新のみ行うことができます。 以上より、 ・INSERT INTO v_emp VALUES (1, 10, 'Tanaka', 600000); ・UPDATE v_emp SET salary = 500000 WHERE department_id = 3; が正解となります。 後者のSQL文は、WHERE句でdepartment_id = 3という条件が指定されていますが、更新する値(salary = 500000)自体はビューで定義された条件を満たしているためエラーとはなりませんので注意しましょう。 ただし、V_EMPビューではDEPARTMENT_ID列が1のデータにし...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54786

### 問題ID 26776 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26776?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表を実表とするビューを作成する場合、ビューのいずれの列に対しても、データの追加、更新、削除の全ての操作を行うことができるビューはどれですか。ただし、INSTEAD OFトリガーは定義していないものとします。
- 解説要約: 作成したビューを通じて実表のデータを操作することができます。 ただし、表に直接アクセスする場合とは異なり、ビューを通じての実表のデータの操作には、ビューの定義によっていろいろな制限があります。 ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 したがって、ビューを通じて実表へのデータの追加、更新、削除の全ての操作を行うためには、ビューの定義に次の要素が含まれていないことが条件になります。 ・GROUP BY句 ・グループ関数 ・ROWNUM擬似列 ・DISTINCTキーワード ・式によって定義された列 ・ビューに含まれない実表の列に定義されたNOT NULL制約 以上より、 ・CREATE OR REPLACE VIEW v_emp AS SELECT * FROM employees WHERE department_id = 5 WITH CHECK OPTION; ・CREATE OR REPLACE VIEW v_emp AS SELECT * FROM employees WHERE salary * 12 + commission > 1000...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782

### 問題ID 26777 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26777?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文でEMPLOYEES表を実表とするビューを作成しました。 CREATE OR REPLACE VIEW v_emp AS SELECT employee_name, hiredate, salary FROM employees WHERE department_id = 1 WITH CHECK OPTION; V_EMPビューに関する説明として、正しいものはどれですか。
- 解説要約: ビューの作成時、WITH CHECK OPTIONオプションを指定すると、ビューを通じて実表のデータを操作する場合に、ビューの定義時に指定したWHERE句の条件を満たしていないデータの追加や更新ができなくなります。 V_EMPビューは、 ・DEPARTMENT_ID列の値が1 という条件が指定されいるので、この条件を満たすデータの追加、更新のみ行うことができます。 以上より、 ・DEPARTMENT_IDが1である部署の従業員データを更新できる が正解となります。 その他の選択肢については次のとおりです。 ・データの追加ができる ・データの削除ができない NOT NULL制約が定義されているEMPLOYEE_ID列がビューに含まれていないため、設問のビューを通じてEMPLOYEES表にデータを追加することはできません。データの更新と削除は行うことができますが、WITH CHECK OPTIONが指定されているので、それもDEPARTMENT_IDが1であるデータに限られます。 ・DEPARTMENT_IDが5である部署の従業員データを更新できる ビューの定義により、DEPARTMENT...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54786

### 問題ID 26778 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26778?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文でEMPLOYEES表を実表とするビューを作成しました。ただし、INSTEAD OFトリガーは定義していないものとします。 CREATE OR REPLACE VIEW v_emp AS SELECT d.department_id, AVG(e.salary) sal FROM departments d JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_id; V_EMPビューに関する説明として、正しいものはどれですか。
- 解説要約: ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 設問のSQL文ではビューの定義にGROUP BY句が使用されているため、ビューを通じて実表のデータを操作することができません。 以上より、 ・ビューは作成されるが、ビューを通じて実表へのデータの追加、更新、削除はできない が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE OR REPLACE VIEW v_emp AS SELECT d.department_id, AVG(e.salary) sal FROM departments d JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_id; INSERT INTO v_emp VALUES (5, 500000); UPDATE v_emp SET sal = 100000; DELETE v_emp WHERE sal > 500000; その他の選択肢については次のとおりです。 ・ビューの作成時、副問合...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782

### 問題ID 26779 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26779?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューを通して実表のデータを更新できないのは、ビューの定義にどの要素が含まれている場合ですか(該当するものを全て選択して下さい)。
- 解説要約: ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 以上より、 ・GROUP BY句 ・グループ関数 ・ROWNUM擬似列 ・DISTINCTキーワード が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF55455

### 問題ID 26780 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26780?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューを通して実表へデータを追加する場合に、ビューの定義に含まれていても良い要素はどれですか。
- 解説要約: ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 以上より、 ・WHERE句 が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm#SQLRF55069

### 問題ID 26781 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26781?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: 実表より先にビューを作成する場合、どのSQL文を実行しますか。
- 解説要約: CREATE VIEW文でビューを作成する際に、FORCEオプションを指定すると、実表の有無にかかわらずビューを作成することができます。 メンテナンスや検証時に、一時的に実表が存在しないがビューを作成しておきたい場合などに利用します。 以上より、 ・CREATE FORCE VIEW view1 AS SELECT employee_id, employee_name, salary FROM emp3; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT * FROM emp3; CREATE FORCE VIEW view1 AS SELECT employee_id, employee_name, salary FROM emp3;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54761

### 問題ID 26782 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26782?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: 次のSQL文に関する説明として、正しいものはどれですか。 CREATE OR REPLACE VIEW v_emp AS SELECT employee_id, employee_name, salary FROM employees WITH READ ONLY;
- 解説要約: ビューの作成時、WITH READ ONLYオプションを指定すると、作成したビューが読取り専用のビューとなります。 読取り専用のビューでは、ビューを通じて実表のデータの操作を行うことができません。ただし、基にした実表に直接アクセスした場合は、実表へデータの追加や更新、削除を行うことができます。 以上より、 ・読み取り専用のビューとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE OR REPLACE VIEW v_emp AS SELECT employee_id, employee_name, salary FROM employees WITH READ ONLY; INSERT INTO v_emp VALUES (2000, 'Sato', 400000); その他の選択肢については次のとおりです。 ・ビューを通して実表のデータの追加/更新/削除ができる WITH READ ONLYオプションを指定すると、ビューを通して実表のデータの操作は行うことができません。 ・EMPLOYEES表へのデータの追加ができなくなる ・EMPL...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54785

### 問題ID 26783 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26783?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 順序に関する説明として、正しいものはどれですか(3つ選択して下さい)。
- 解説要約: 順序は複数のユーザーで共有可能なため、複数のユーザーが同じ順序で順序値を生成した場合、常に全体を通して一意な値(※)を生成します。 ※ただし、順序の作成時にCYCLEオプション(順序値が最大値または最小値に達した場合、初期値に戻り繰り返し順序を生成する)を指定した場合は、重複した順序値が生成されることもあります。 また、順序は表と関連付けられるものではないので、複数の表で1つの順序を使用することもできます。 なお、順序は連番が保証されているわけではなく、ロールバックが発生した場合などに欠番が生じることもあります。 以上より、 ・欠番が発生する場合もある ・複数のユーザーで共有可能である ・1つの順序を複数の表で使用できる が正解となります。 その他の選択肢については次のとおりです。 ・順序値が重複することはない 順序の作成時にCYCLEオプションを指定した場合は、重複した順序値が生成されることもあるので、誤りです。 ・ユーザー毎に一意な番号を生成する 順序は複数のユーザーで共有可能なため、複数のユーザーが同じ順序で順序値を生成した場合、ユーザー毎ではなくデータベース全体を通して一意な番...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314

### 問題ID 26784 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26784?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 順序に関する説明として、正しいものはどれですか(該当するものを2つ選択して下さい)。
- 解説要約: 順序を生成する際に指定可能なオプションは以下のとおりです。 以上より、 ・増分値を指定することができる ・初期値のデフォルト値は1である が正解となります。 その他の選択肢については次のとおりです。 ・順序の値が最大値に達した後は必ず順序値の生成を終了する 順序値が最大値に達した場合、初期値に戻って順序値を生成するか、順序値の生成を終了するかをCYCLE/NOCYCLEオプションで指定することができます。 ・順序を参照するたびに順序値が生成される CURRVAL疑似列を参照すると、最後に生成された順序値が返されます。その際に順序値は生成されません。 ・順序の増分値に負の値を指定できない 順序の増分値に負の値を指定することもできます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314

### 問題ID 26785 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26785?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次の要件を満たす順序を作成するSQL文として、正しいものはどれですか。 ・初期値は1 ・増分は2 ・最大値は150 ・順序が最大または最小値に達した場合は、初期値に戻って繰り返し順序値を生成する ・順序値をキャッシュする
- 解説要約: 順序を生成する際に指定可能なオプションは以下のとおりです。 CACHE/NOCACHEオプションの両方が省略された場合は、20個の順序値がキャッシュされます。 以上より、 ・CREATE SEQUENCE s_dept INCREMENT BY 2 MAXVALUE 150 CYCLE; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE SEQUENCE s_dept INCREMENT BY 2 MAXVALUE 150 CYCLE; SELECT s_dept.NEXTVAL FROM dual; SELECT s_dept.NEXTVAL FROM dual;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314

### 問題ID 26786 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26786?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: DEPARTMENTS表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE departments4 AS SELECT * FROM departments WHERE 1 = 0; CREATE SEQUENCE seq_dept; INSERT INTO departments4 VALUES (seq_dept.nextval, 'Sales', 1001); UPDATE departments4 SET department_id = seq_dept.currval WHERE manager_id = 1001;
- 解説要約: 順序から順序値を生成するにはNEXTVAL擬似列を参照します。また、最後に生成した順序値を参照するには、CURRVAL擬似列を参照します。 設問のSQL文ではsqe_deptという名前の順序を作成していますが、オプションを指定せずに順序を作成しているので、初期値や増分値などはデフォルト値（それぞれ1）を使用して順序が作成されます。 INSERT文では順序を使用してデータを追加しています。ここでNEXTVAL擬似列は1を返します。 次のUPDATE文ではCURRVAL擬似列を参照していますが、ここでCURRVAL擬似列は最後に生成した1を返します。したがって、MANAGER_ID列の値が1001である行のDEPARTMENT_ID列の値を1に変更するということになります。（つまりUPDATE文による変化はありません。） 以上より、 ・正常に実行され、MANAGER_IDが1001の行のDEPARTMENT_IDの値が1となる が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE departments4 AS SELECT * FRO...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Sequence-Pseudocolumns.html#GUID-693B576A-191D-45F5-B7CB-88D0EA821B44

### 問題ID 26787 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26787?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 索引に関する説明として、正しいものはどれですか(該当するものを3つ選択して下さい)。
- 解説要約: 索引はデータの検索を高速化するスキーマ・オブジェクトです。 表の列に索引が設定されると、索引が設定された列の値と、その物理的な格納場所（ROWID）を登録します。 索引が設定されていない表でデータを検索する場合、問合せの条件に従って、表の先頭のデータから1行ずつ検索していきますので、データが大量にある場合には相当の時間がかかります。しかし索引を設定している表では、ROWIDを使用してデータを検索するため、大量のデータの中からでも高速に目的のデータを探すことができます。 また、表に対してDML文を実行する度に、表に設定された索引はメンテナンス（必要であれば更新）されます。 以上より、 ・表のデータへのアクセスを高速化する ・索引を設定している表ではROWIDを使用して検索する ・DML文実行時、索引がメンテナンスされる が正解となります。 その他の選択肢については次のとおりです。 ・表を削除しても、その表に作成された索引は削除されない 索引を設定している表を削除すると、設定されている索引は自動で削除されます。 ・列の組合せに対して索引を作成することはできない 列の組合せに索引を作成するこ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CREATE-INDEX.html

### 問題ID 26788 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26788?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 索引はどのような列に作成しますか。
- 解説要約: 次の条件に該当する列に索引を作成すると、検索時のパフォーマンス向上につながります。 ・WHERE句の条件や結合条件としてよく使用される列 ・列にNULL値が多く含まれており、NULL値以外の値を指定して検索する列 ・表の規模が大きく、多くの問合せで15%未満の行を検索する列 以上より、 ・表の規模か大きく、多くの問合せで15%未満の行を検索する列 が正解となります。
- 参考URL: なし

### 問題ID 26789 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26789?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: シノニムに関する説明として、誤っているものはどれですか。
- 解説要約: シノニムはオブジェクトの別名を表すスキーマ・オブジェクトです。表やビューなどと同様に、一意に識別できるオブジェクトIDを持ちます。 シノニムには、作成したユーザーだけが使用できるプライベートシノニムと、全てのユーザーが使用できるパブリックシノニムの2種類があります。 プライベートシノニムとパブリックシノニムで同じ名前のシノニムを作成することができますが、プライベートシノニムとパブリックシノニムで同名のシノニムがある場合は、プライベートシノニムが優先されます。 以上より、 ・パブリックシノニムとプライベートシノニムではパブリックシノニムが優先される が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7001.htm#SQLRF01401

### 問題ID 26790 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26790?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文の説明として、正しいものはどれですか。 ただし、次のSQL文を実行するユーザーはPINGTユーザーのEMPLOYEES表を参照する権限が与えられているものとします。 CREATE SYNONYM emp FOR pingt.employees;
- 解説要約: PUBLICを指定せずに作成したシノニムはプライベートシノニムです。プライベートシノニムが作成されたスキーマでのみ使用することができます。 設問のSQL文では、PUBLICを指定していないのでプライベートシノニムが作成されます。また、シノニムを作成するスキーマを明示的に指定せずにシノニムを作成しているので、SQL文を実行したユーザーのスキーマにシノニムが作成されます。 したがって、そのシノニムは、SQL文を実行しシノニムを作成したユーザーだけが使用できます。 以上より、 ・SQL文を実行したユーザーがPINGTが所有するEMPLOYEES表をEMPで参照できる が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7001.htm#SQLRF01401

### 問題ID 26791 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26791?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: シノニムに関する説明として、正しいものはどれですか。
- 解説要約: シノニムを削除した場合、シノニムが参照していた表自体に影響はありません。 また、シノニムが作成されている表を削除しても、シノニムは削除されません。 以上より、 ・表に定義されたシノニムを削除しても、表に影響はない が正解となります。 その他の選択肢については次のとおりです。 ・シノニムは表にだけ定義できる シノニムやビューなど、他のオブジェクトに対してもシノニムを作成できます。 ・表にパブリックシノニムを定義すると、全てのユーザーがパブリックシノニムを用いて表からデータを取り出せる パブリックシノニムを作成しても、その表に対する参照権限がなければ表からデータを取り出せません。 ・自分が所有する表にシノニムを定義できない 自身が所有する表に対してもシノニムを作成できます。 ・パブリックシノニムは誰でも作成できる パブリックシノニムを作成するにはCREATE PUBLIC SYNONYM権限が必要になります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7001.htm#SQLRF01401
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9002.htm#SQLRF01805

### 問題ID 26792 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26792?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造とデータを確認して下さい。 次のSQL文のうち、エラーとなるものはどれですか。
- 解説要約: 副問合せから戻されるデータの件数が複数件の場合に、比較演算子に単一行演算子を使用するとエラーとなります。 選択肢のSQL文において、副問合せが返すデータの件数と比較演算子に注目すると、下記の副問合せは3件のデータを返しますが、 SELECT department_id FROM departments WHERE department_id BETWEEN 1 AND 3 比較演算子に"="が使用されているため、エラーが発生します。 以上より、 ・SELECT employee_id, employee_name, salary FROM employees WHERE department_id = (SELECT department_id FROM departments WHERE department_id BETWEEN 1 AND 3); が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT employee_id, employee_name, salary FROM employees WHERE...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm
  - http://www.atmarkit.co.jp/ait/articles/1208/06/news118.html

### 問題ID 26793 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26793?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューに関する説明として、正しいものはどれですか。ただし、INSTEAD OFトリガーは定義していないものとします。
- 解説要約: ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 選択肢を1つずつ確認してみましょう。 ・NOT NULL制約が定義された実表を基にしてビューを作成することはできない 実表の列にNOT NULL制約が定義されていても、ビューを作成することはできるので誤りです。 ・ビューの作成時、副問合せにグループ関数を使用することはできない ビューの作成時、副問合せにグループ関数を使用できるので誤りです。 ・ビューの作成時、副問合せにDISTINCTキーワードが含まれていると、ビューを通じて実表のデータを削除できない ビューの作成時、副問合せにDISTINCTキーワードが含まれている場合は、ビューを通じて実表のデータを削除できませんので、正しいです。 ・ビューの定義にROWNUM擬似列が含まれていても、ビューを通じて実表のデータの削除ができる ビューの定義にROWNUM擬似列が含まれている場合は、ビューを通じて実表へのデータの追加、更新、削除ができませんので誤りです。 以上より、 ・ビューの作成時、副問合せにDISTINCTキーワードが含まれていると、ビューを通じて実表の...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782

### 問題ID 26794 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26794?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 EMPLOYEES表を基に次の3つのビューを作成しました。ただし、INSTEAD OFトリガーは定義していないものとします。 ビューと実行可能な操作の組合せとして正しいものはどれですか(該当するものを2つ選択してください)。 ビュー1) CREATE OR REPLACE VIEW v_emp1 AS SELECT employee_id, employee_name, salary * 12 sal FROM employees; ビュー2) CREATE VIEW v_emp2 AS SELECT department_id, AVG(sala...
- 解説要約: 作成したビューを通じて実表のデータを操作することができます。 ただし、表に直接アクセスする場合とは異なり、ビューを通じての実表のデータの操作には、ビューの定義によっていろいろな制限があります。 ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 設問のビュー1はビューの定義に式によって定義された列が含まれています。データの削除を行うことができます。 ビュー2はビューの定義にGROUP BY句とグループ関数が使用されているため、データの追加、更新、削除の全てを行うことができません。 ビュー3はNOT NULL制約が定義されているEMPLOYEE_ID列がビューの定義に含まれていません。データの更新を行うことができます。 以上より、 ・ビュー1を通じて、EMPLOYEES表のデータの削除ができる ・ビュー3を通じて、EMPLOYEES表のデータの更新ができる が正解となります。 設問のSQL文の実行結果は次のようになります。 [ビュー1] SQLを表示 CREATE OR REPLACE VIEW v_emp1 AS SELECT employee_id, em...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782

### 問題ID 26795 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26795?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: DEPARTMENTS表の構造を確認して下さい。 DEPARTMENT_ID列とDEPARTMENT_NAME列の組合せに対して一意索引を作成するには、どのSQL文を実行しますか。
- 解説要約: 2つ以上の列の組合せに対して索引を作成する場合は、CREATE INDEX文のON句に索引を作成する全ての列名を指定します。 また、一意索引を作成するには、CREATE INDEX文にUNIQUEオプションを指定します。 以上より、 ・CREATE UNIQUE INDEX ind ON departments (department_id, department_name); が正解となります。 その他の選択肢については次のとおりです。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE UNIQUE INDEX ind ON departments (department_id, department_name); ・CREATE INDEX ind ON department_id, department_name; 一意索引を作成するにはUNIQUEオプションを指定します。また、ON句で索引を作成する表名が記述されていませんのでエラーとなります。 ・CREATE INDEX ind ON departments (department_id, depar...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_5012.htm

### 問題ID 26796 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26796?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: データベース管理者が次のSQL文でシノニムを作成しました。 CREATE PUBLIC SYNONYM emp FOR pingt.employees; ユーザーAがこのシノニムを使用して次の問合せを実行したところエラーとなりました。エラーの原因は何ですか。 SELECT * FROM emp;
- 解説要約: シノニムを使用するには、シノニムの基となるオブジェクトに対する適切な権限が必要です。シノニムを使用して問合せを行う場合は、シノニムの基になる表に対する参照権限が必要です。 以上より、 ・ユーザーAにEMPLOYEES表を参照する権限がないため が正解となります。 その他の選択肢については次のとおりです。 ・ユーザーAにempシノニムを使用する権限がないため シノニムを使用するための権限はありません。 ・パブリックシノニムはシノニムを作成したユーザーだけしか使用できないため パブリックシノニムは全てのユーザーが使用できるシノニムです。 ・プライベートシノニムはシノニムを作成したユーザーだけしか使用できないため プライベートシノニムはシノニムが作成されたスキーマでのみ使用できるシノニムです。ですが、設問のではPUBLICを指定してシノニムを作成しているので、パブリックシノニムが作成されます。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7001.htm

### 問題ID 26797 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26797?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 現在の日時は2012年5月10日12時38分0秒です。 10日後に入社する従業員のデータを登録するために、以下のSQL文を実行しました。実行結果として正しいものはどれですか。 INSERT INTO employees (employee_id, employee_name, hiredate) VALUES (2000, '江口佳代', SYSDATE + 10);
- 解説要約: SYSDATE関数は現在の日時を表すDATE型の値を返します。またDATE型の値に数値を加算すると、日数として加算されます。 設問のSQL文では、SYSDATE関数が返すDATE型の値に10を加算していますので、現在日時の2012年5月10日12時38分0秒に10日を加算した2012年5月20日12時38分0秒がHIREDATE列に登録されます。 以上より、 ・入社日に2012年5月20日12時38分0秒が登録される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 INSERT INTO employees (employee_id, employee_name, hiredate) VALUES (2000, '江口佳代', SYSDATE + 10); SELECT employee_id, employee_name, TO_CHAR(hiredate, 'YYYY-MM-DD HH24:MI:SS') FROM employees WHERE employee_id = 2000;
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions191.htm#SQLRF06124

### 問題ID 26798 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26798?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: SALES表とCUSTOMERS表の構造を確認して下さい。 SALES表とCUSTOMERS表から、商品を購入したことのある顧客の顧客番号と顧客氏名を表示するには、どのSQLを実行しますか。 ただし、1人の顧客につき1度だけ表示することとします。
- 解説要約: 商品の購入情報はSALES表に、顧客情報はCUSTOMERS表に登録されているので、顧客IDの値でSALES表とCUSTOMERS表を結合します。 SALES表とCUSTOMERS表の顧客ID列の列名を見ると、それぞれCUST_ID,CUSTOMER_IDと異なる名称であるため、NATURAL JOIN句やUSING句での結合はできません。ON句を使用して2つの表を結合します。 また、設問では、1人の顧客につき1度だけ表示するとのことですので、SELECT句にDISTINCTキーワードを指定して重複を排除した結果を取り出します。 以上より、 ・SELECT DISTINCT s.cust_id 顧客ID, c.cust_last_name || c.cust_first_name FROM sales s JOIN customers c ON s.cust_id = c.customer_id; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT DISTINCT s.cust_id 顧客ID, c.cust_...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55272
  - http://www.atmarkit.co.jp/fdb/rensai/oraclesql/07/01.html

### 問題ID 26799 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26799?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文の実行結果として表示される列の組合せとして、正しいものはどれですか(該当するものを全て選択してください)。 ただし、日付書式は"RR-MM-DD"とします。 SELECT department_id, employee_id, employee_name, salary, commission, hiredate FROM employees WHERE department_id = 3 OR salary > 400000 AND commission <= 1200000 OR hiredate > '08-04-01';
- 解説要約: WHERE句に条件が複数指定されている場合は、論理演算子の優先順位に従って条件が評価されます。 AND演算子とOR演算子ではAND演算子のほうが先に評価されます。 WHERE department_id = 3 OR salary > 400000 AND commission <= 1200000 OR hiredate > '08-04-01'; よって設問の条件は以下のように検索されます。 「SALARY列が400000より大きく且つCOMMISSION列が1200000以下」（無し）、または、「DEPARTMENT_ID列が3」（D,E）、または、「HIREDATE列が2008年4月1日より大きい（新しい）」（B,C） 以上より、 ・D ・E ・B ・C が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Logical-Conditions.html

### 問題ID 26800 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26800?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 次の順番でSQL文を実行しました。 1. SQL> INSERT INTO prod VALUES (11, 'Debussy', 10, SYSDATE, NULL); 2. SQL> SAVEPOINT a; 3. SQL> UPDATE prod SET name = 'Chopin' WHERE prodid = 11; 4. SQL> ROLLBACK TO SAVEPOINT a; 5. SQL> DELETE prod WHERE prodid = 11; 6. SQL> COMMIT; その後、次のSQL文を実行すると、どのようになりますか。...
- 解説要約: 6.のCOMMIT文により、トランザクション内の処理が確定され、作成したセーブポイントはすべて破棄されます。 したがって、7.でROLLBACK TO SAVEPOINT文を実行した時にはセーブポイントaは破棄されているのでエラーとなります。 以上より、 ・エラーとなる が正解となります。 設問のSQL文を順に説明します。 1.INSERT文により、PROD表にデータが1件追加します。ただし、INSERT文はDML文に該当し自動コミットされないため、データの追加は確定されていない状態です。 2.セーブポイントaを作成します。 3.UPDATE文により、PROD表のPRODIDが11であるデータのNAME列の値を'Chopin'に変更します。ただし、UPDATE文はDML文に該当し自動コミットされないため、データの変更は確定されていない状態です。 4.セーブポイントaより後に実行した処理を取消します。この場合、3.のUPDATE文が取消されます。 5.DELETE文により、PROD表のPRODIDが11であるデータを削除します。これは1.で追加したデータです。 6.COMMIT文により、...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10001.htm#SQLRF01701
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9021.htm#SQLRF55217
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_4010.htm#SQLRF01110

### 問題ID 26801 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26801?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文を実行すると、どのようになりますか。 SELECT TO_CHAR(-1.99, '9.990') FROM dual;
- 解説要約: TO_CHAR関数の第2引数に指定された数値書式により、小数部分は3桁で表示し、桁数が足りない場合は0で埋めます。整数部分は1桁で、桁数が足りない場合は0で埋めません。 第1引数に指定された数値の小数部分は2桁ですので小数点以下3桁目を0で埋めて「990」、整数部分は1桁ですので「1」となります。 また、第1引数に指定された数値は負の値ですので、数値書式に従って変換された文字列に-符号が適用されます。 以上より、 -1.990 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TO_CHAR(-1.99, '9.990') FROM dual;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions201.htm#i79330
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34570

### 問題ID 26802 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26802?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文を実行すると日付しか表示されません。 SELECT SYSDATE FROM dual; 時間も表示するためには、どのSQL文を実行しますか。
- 解説要約: 通常、DATE型の値を表示させると、「2012-04-01」のように表示されますので、任意のフォーマットに従って表示させるにはTO_CHAR関数を使用します。 以上より、 ・SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT TO_DATE(SYSDATE) FROM dual; TO_DATEに日付書式が指定されていないので、日付のみ表示されます。 ・SELECT TO_CHAR(SYSDATE, 'YYYY年MM月DD日 HH時MI分SS秒') FROM dual; 日付書式中に「年」などの文字を埋め込みたい場合は、二重引用符(")で文字を囲まなければなりません。二重引用符(")で囲んでいない場合はエラーとなります。 ・SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD') FROM dual; 日付書式に日付部分しか指定していないため、このSQL文では時間は表示されませ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions200.htm#i1009324
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924

### 問題ID 26803 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26803?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文を実行した結果として、正しいものはどれですか。 ただし、実行環境は日本語環境とします。 SELECT TO_CHAR(SYSDATE, 'YYYY/MON/DD(DAY) HH24:MI:SS', 'nls_date_language=AMERICAN') FROM dual;
- 解説要約: 日付書式要素の「DAY」,「DY」,「MONTH」,「MON」などを日本語環境で表示させると、「月曜日」,「月」,「6月」,「6月」のように表示されます。 設問のSQL文では、TO_CHAR関数の第3引数にNLSパラメータが指定されており、言語が英語環境に指定されているので、「DAY」,「DY」,「MONTH」,「MON」などの日付書式要素は、それぞれ「MONDAY」,「MON」,「JUNE」,「JUN」のように英語表示となります。 なお、設問のSQL文の日付書式では、 ・YYYY：4桁の年。2012年の場合は「2012」 ・MON：月の名前の省略形。6月の場合は「JUN」 ・DD：月における日。17日の場合は「17」 ・DAY：省略形ではない曜日。日曜日の場合は「SUNDAY」 のように表示されます。 以上より、 ・2012/JUN/17(SUNDAY ) 10:35:27 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TO_CHAR(SYSDATE, 'YYYY/MON/DD(DAY) HH24:MI:SS', 'nls_date_...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions200.htm#i1009324
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924

### 問題ID 26804 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26804?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 日付値を次の表示形式で表示するSQL文として、正しいものはどれですか。 ただし、実行環境は英語環境とします。 Eighteenth of June , 2012
- 解説要約: 設問の表示では、日の表示がスペル表記かつ順序表記、月の表示が省略形ではない月の名前、年の表示が数値表記で、「日 of 月, 年」というように表示されています。 日をスペル表記かつ順序表記にするためには、日付書式要素「Dd」にスペル表記を表す接尾辞「sp」と順序表記を表す「th」を指定します。 月は省略形ではない月の名前で表示されていますので、「Month」を指定し、年は4桁ですので、「YYYY」を指定します。 また、書式中に文字列を含める場合は、含める文字列を二重引用符(")で囲んで指定します。 以上より、 ・SELECT TO_CHAR(SYSDATE, 'Ddspth "of" Month, YYYY') FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。 ※日本語環境の場合は、事前に以下のSQL文を実行してセッションを英語環境に変更して下さい。 ALTER SESSION SET NLS_DATE_LANGUAGE = 'AMERICAN'; ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MON-RR'; S...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/TO_CHAR-datetime.html#GUID-0C3EEFD1-AE3D-452D-BF23-2FC95664E78F
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Format-Models.html#GUID-49B32A81-0904-433E-B7FE-51606672183A

### 問題ID 26805 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26805?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 日付値を次の表示形式で表示するSQL文として、正しいものはどれですか。
- 解説要約: 日付書式はデフォルトで埋め込みモードが有効となっています。埋め込みモードが有効の場合、数値が1桁の場合に先頭に0付きで表示されたり、文字の前後にスペース付きで表示されます。 埋め込みモードを無効にするには、日付書式に「FM」を指定します。 設問では、「01st」ではなく「1st」、また「June」の後ろにスペースがないことから、埋め込みモードを無効にして問合せを実行したことがわかります。 以上より、 ・SELECT TO_CHAR(SYSDATE, 'fmDdth "of" Month, YYYY') FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT TO_CHAR(SYSDATE, 'fmDdth "of" fmMonth, fmYYYY') FROM dual; 「FM」が指定される度に埋め込みモードの有効/無効が切り替わるため、2つ目の「FM」の指定で埋め込みモードが有効となり、「MONTH」が埋め込みモードで表示されます。 ・SELECT TO_CHAR(SYSDATE, 'Ddt...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions200.htm#i1009324
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924

### 問題ID 26806 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26806?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 ただし、実行環境は日本語環境とします。 SELECT TO_DATE('2012-05-21') FROM dual;
- 解説要約: TO_DATE関数の日付書式やNLSパラメータは省略可能です、省略された場合はセッションのデフォルト値が適用されます。 日本語環境で日付書式のデフォルト値は「RR-MM-DD」ですので、設問のSQL文は正常に実行され、「12-05-21」が表示されます。 以上より、 ・正常に実行され、「12-05-21」が表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TO_DATE('2012-05-21') FROM dual; 引数を「21-05-2012」に変更すると、デフォルトの日付書式と異なるフォーマットになるため、エラーとなります。 SQLを表示 SELECT TO_DATE('21-05-2012') FROM dual; その他の選択肢については次のとおりです。 ・日付書式が指定されていないため、エラーとなる ・NLSパラメータが指定されていないため、エラーとなる TO_DATE関数の日付書式やNLSパラメータは省略可能です、省略された場合はセッションのデフォルト値が適用されます。 ・正常に実行され、「12/05/21」が表...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/TO_DATE.html
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Format-Models.html#GUID-49B32A81-0904-433E-B7FE-51606672183A

### 問題ID 26807 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26807?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 現在の日時は2012年6月12日15時35分48秒です。 次のSQL文の実行結果として、正しいものはどれですか。 SELECT TO_CHAR(TO_DATE('95/12/31', 'RR/MM/DD'), 'YYYY/MM/DD') RR, TO_CHAR(TO_DATE('95/12/31', 'YY/MM/DD'), 'YYYY/MM/DD') YY FROM dual;
- 解説要約: 日付書式の要素である「YY」と「RR」はどちらも年の下2桁を表しますが、世紀の取扱に違いがあります。 「YY」は引数で指定された値を常に現在の世紀の値として扱うので、設問では2095年に変換されます。「RR」は現在の世紀が世紀の前半であるか後半であるか、指定された値が世紀の前半であるか後半であるかで世紀が決定されます。設問の「RR」は、1995年に変換されます。 以上より、 ・1995/12/31 2095/12/31 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TO_CHAR(TO_DATE('95/12/31', 'RR/MM/DD'), 'YYYY/MM/DD') RR, TO_CHAR(TO_DATE('95/12/31', 'YY/MM/DD'), 'YYYY/MM/DD') YY FROM dual;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions203.htm#SQLRF06132
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924

### 問題ID 26808 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26808?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 現在の日付は2012年06月23日です。 1999年4月1日から現在までの日数を求めるには、どのSQL文を実行しますか(該当するものをすべて選択してください)。 ただし、実行環境は英語環境とし、デフォルトの日付の表示形式は「RR-MM-DD」とします。
- 解説要約: 日付値から日付値を減算すると、2つの日付間の日数を求めることができます。 設問では「1999年4月1日」から現在までに経過した日数を求めるので、2つの日付の日付値を取得し、減算を行います。 現在の日付の日付値はSYSDATE関数で取得することができ、「1999年4月1日」の日付値はTO_DATE関数を使用して日付値を取得します。 以上より、 ・SELECT SYSDATE - TO_DATE('99-04-01', 'RR-MM-DD') FROM dual; ・SELECT SYSDATE - TO_DATE('1999-Apr-01', 'YYYY-Mon-DD') FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。 ※日本語環境の場合は事前に以下のSQL文を実行して、セッションを英語環境で日付の表示形式を「RR-MM-DD」に変更して下さい。 ALTER SESSION SET NLS_DATE_LANGUAGE = 'AMERICAN'; ALTER SESSION SET NLS_DATE_FORMAT = 'RR-MM-DD'; SQL...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions203.htm#SQLRF06132
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00208

### 問題ID 26809 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26809?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文のうち、エラーとなるものはどれですか。
- 解説要約: COALESCE関数は引数の値を判定し、最初に見つかったNULL値以外の値を返す関数です。 引数はすべて同じデータ型の値でなければなりません。異なるデータ型の値を指定するとエラーとなります(暗黙的なデータ変換は行われません)。 選択肢のSQL文のうち、 ・SELECT COALESCE(employee_id, employee_name, hiredate) FROM employees; は、EMPLOYEE_ID列、EMPLOYEE_NAME列、HIREDATE列のデータ型がそれぞれNUMBER型、VARCHAR2型、DATE型であるためエラーとなります。 以上より、 ・SELECT COALESCE(employee_id, employee_name, hiredate) FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions030.htm#SQLRF00617

### 問題ID 26810 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26810?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次の問合せ結果と等しい結果となるSQL文はどれですか(該当するものをすべて選択して下さい)。 SELECT TRIM(' Oracle Web問題集 ') FROM dual;
- 解説要約: TRIM関数は、引数で指定された文字列の前後にある削除文字を取り除いた文字列を返す関数です。 設問の問合せのように、TRIM関数の引数に削除位置と削除文字を指定しない場合は、文字列の前後のスペースが削除されます。 したがって、設問の問合せの結果は、前後のスペースが削除され「Oracle Web問題集」となります。 これと同じ結果が得られる問合せは、前後のスペースを取り除く SELECT TRIM(BOTH FROM ' Oracle Web問題集 ') FROM dual; と、前後の「#」記号を取り除く SELECT TRIM(BOTH '#' FROM '#Oracle Web問題集#') FROM dual; の2つの問合せです。 以上より、 ・SELECT TRIM(BOTH FROM ' Oracle Web問題集 ') FROM dual; ・SELECT TRIM(BOTH '#' FROM '#Oracle Web問題集#') FROM dual; が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TRIM(' Oracle...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions219.htm#SQLRF06149

### 問題ID 26811 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26811?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次の問合せの結果として、正しいものはどれですか。 SELECT TRIM(TRAILING '?' FROM '?Oracle Web問題集?') FROM dual;
- 解説要約: TRIM関数は、引数で指定された文字列の前後にある削除文字を取り除いた文字列を返す関数です。 設問ではTRIM関数の削除位置に「TRAILING」、削除文字に「?」を指定しています。「TRAILING」が指定されると、指定された文字列の末尾から削除文字を削除します。 以上より、 ・?Oracle Web問題集 が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TRIM(TRAILING '?' FROM '?Oracle Web問題集?') FROM dual;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions219.htm#i79689

### 問題ID 26812 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26812?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: PROD表の構造を確認して下さい。 次の問合せ結果となるSQL文として、正しいものはどれですか。
- 解説要約: RPAD関数は引数で指定された文字列が指定した長さの文字列になるように、右側に指定された埋め込み文字を付加した文字列を返す関数です。 設問の問合せ結果では、取得したNAME列の値が長さが20の文字列になるように、右側に「*」を埋め込んでいますので、RPAD関数を使用します。 なお、長さの指定は1バイト文字が何文字分かを指定しますので、2バイト文字が指定された場合は1文字を長さ2として考えなければなりません。 以上より、 ・SELECT RPAD(name, 20, '*') FROM prod; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT LPAD(name, 20, '*') FROM prod; LPAD関数は引数で指定された文字列が指定した長さの文字列になるように、左側に指定された埋め込み文字を付加した文字列を返します。 ・SELECT RPAD(name, 7, '*') FROM prod; ・SELECT LPAD(name, 7, '*') FROM prod; RPAD関数やLPAD関数の...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions095.htm#SQLRF00663
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions159.htm#SQLRF06103

### 問題ID 26813 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26813?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 現在の日時は2010年12月25日14時40分です。 ROUND関数の結果として正しいものはどれですか(該当するものを全て選択して下さい)。 ただし、日付の表示書式はRR-MM-DDとします。
- 解説要約: ROUND関数は、引数で指定された日付値を丸めて返します。 どの単位で丸めるかは書式で指定します。指定できる主な書式は次の通りです。 書式が省略された場合は"DD"が指定されたものとして処理されます。 以上より、 ・ROUND(SYSDATE, 'YEAR')の結果は"11-01-01"である ・ROUND(SYSDATE)の結果は"10-12-26"である ・ROUND(SYSDATE, 'MONTH')の結果は"11-01-01"である が正解となります。 正解のSQL関数の実行結果は次のようになります。 SQLを表示 SELECT ROUND(SYSDATE, 'YEAR'), ROUND(SYSDATE, 'MONTH'), ROUND(SYSDATE) FROM dual;
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions154.htm#SQLRF00699

### 問題ID 26814 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26814?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文のうち、エラーとなるものはどれですか。
- 解説要約: 関数がネストしている場合は、内側の関数から実行されます。内側の関数の結果が外側関数の引数として妥当な値であるか注意が必要です。 では、選択肢のSQL文を1つずつ確認してみましょう。 ・SELECT NVL2(ADD_MONTHS(hiredate, 6), TO_CHAR(hiredate), SYSDATE) FROM employees; まずADD_MONTHS関数が実行され日付値を返します。この値がNVL2関数の第1引数になります。NVL2関数の第2引数にはTO_CHAR関数が指定されていますので、文字列を指定したことになります。NVL2関数の第3引数は第2引数と同じデータ型でなければなりませんので、文字列型の値を指定しなければなりませんが、日付値を指定しても暗黙的なデータ変換によって文字列に変換されるので、このSQL文は正常に実行されます。 ・SELECT MONTHS_BETWEEN(SYSDATE, NVL(hiredate, SYSDATE)) FROM employees; まずNVL関数が実行され日付値を返します。そしてMONTHS_BETWEEN関数で現在日時とN...
- 参考URL: なし

### 問題ID 26815 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26815?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 従業員の給与を次の形式で表示するSQL文として、正しいものはどれですか。 なお、EMPLOYEES表に登録されている従業員の中には、SALARY列がNULL値である従業員が含まれます。SALARY列がNULL値の場合は「undecided」と表示して下さい。 実行環境は日本語環境とします。 ￥500,000
- 解説要約: SALARY列の値がNULL値の場合に、「undecided」を表示するためにNVL関数を使用することができます。 また、SALARY列の値を￥記号付きのカンマ(,)区切りで表示するには、TO_CHAR関数で書式化します。 以上より、 ・SELECT NVL(TO_CHAR(salary, 'L9,999,999'), 'undecided') FROM employees; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については次のとおりです。 ・SELECT NVL(salary, 'undecided') FROM employees; ・SELECT TO_CHAR(NVL(salary, 'undecided'), 'L9,999,999') FROM employees; NVL関数に指定された2つの引数のデータ型が異なるため、エラーとなります。 ・SELECT NVL(TO_CHAR(salary), 'undecided') FROM employees; エラーとはなりませんが、SALARY列の値が書式化されずに表示されます。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL.html#GUID-3AB61E54-9201-4D6A-B48A-79F4C4A034B2
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions201.htm#SQLRF06130

### 問題ID 26816 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26816?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PROD表と同じ構造をもつPROD2表を作成し、次のSQL文を実行したところ、エラーとなりました。エラーの原因として考えられるものを2つ選択して下さい。 INSERT INTO PROD2 SELECT name, category, prodid, startdate, enddate FROM prod WHERE prodid < 50;
- 解説要約: INSERT句の列のリストを省略する場合、副問合せのSELECT句の列のリストには、データを追加する表のすべての列を表の列構成の順番で指定しなければなりません。設問のSQL文では、PROD2表の列構成と副問合せの列のリストが異なるためエラーとなります。 また、INSERT句の列のリストを省略せずに、副問合せのSELECT句に指定する列のリストと同数かつ同じ順番で指定すれば正常に実行できます。設問のSQL文では、INSERT句に列のリストが副問合せと同じ順番で指定されていないこともエラーの原因と言えます。 以上より、 ・副問合せの列のリストがPROD2表の列構成の順番と異なるため ・INSERT句に列のリストが副問合せの順番で指定されていないため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 INSERT INTO PROD2 SELECT name, category, prodid, startdate, enddate FROM prod WHERE prodid < 50; 正解のエラーの原因はそれぞれ以下のように解消できます。 SQLを表示 ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm#SQLRF01604

### 問題ID 26817 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26817?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 次のSQL文を実行するとどうなりますか。 ただし、現在、コミットしていないトランザクションはないものとします。 DELETE FROM employees;
- 解説要約: DELETE文は表のデータを削除しますが、表の構造は削除しません。 また、DELETE文はDML文ですので、COMMIT文で操作が確定されるまではROLLBACK文で操作の取消しが可能です。 以上より、 ・表のデータが削除されるが、ロールバックすることができる が正解となります。 設問の一連の処理は次の通りです。 SQLを表示 COMMIT; DELETE FROM prod; SELECT * FROM prod; ROLLBACK; SELECT * FROM prod;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8005.htm#SQLRF01505
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_4010.htm#SQLRF01110
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9021.htm#SQLRF01610

### 問題ID 26818 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26818?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQLと同じ結果となるSQL文はどれですか(該当するものを全て選択して下さい)。 SELECT department_id, department_name, employee_name, hiredate FROM departments NATURAL JOIN employees ORDER BY department_id, employee_id, hiredate;
- 解説要約: 設問のSQL文のようなNATURAL JOIN句による表の結合を自然結合といいます。自然結合では、2つの表に共通して存在する同名で同じデータ型(または互換性のあるデータ型)の列に基づいて、2つの表を結合します。 設問のDEPARTMENTS表とEMPLOYEES表では、同名で同じデータ型の列はDEPARTMENT_ID列とMANAGER_ID列になりますので、設問のSQL文の結果は、これらの2つの列が等しいという結合条件で2つの表を結合した結果と等しくなります。 2つの表の特定の列の値が等しいデータを結合することを等価結合といいますが、等価結合を行うには自然結合のほか、USING句による結合とON句による結合、Oracle独自の結合構文による結合があります。 設問の選択肢では、USING句による結合とON句による結合があります。 USING句による結合では、2つの表に共通するある同名の列で、結合に使用する列をUSING句に指定すればよいので、USING句にDEPARTMENT_ID列とMANAGER_ID列を指定します。 また、ON句による結合では、結合条件をON句に指定しますので、O...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55325
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314

### 問題ID 26819 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26819?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQL文と同じ実行結果となるSQL文はどれですか(該当するものを全て選択して下さい)。 SELECT e.employee_id, d.department_name, e.employee_name FROM departments d JOIN employees e ON d.department_id = e.department_id WHERE e.hiredate >= '2005-10-01';
- 解説要約: 表の結合時、結合した表から取り出したい行を指定してSQL文を実行することができます。 ON句による結合では、ON句の後にWHERE句またはAND句で選択条件を指定します。 また、USING句による結合では、USING句の後にWHERE句で選択条件を指定します。 以上より、 ・SELECT e.employee_id, d.department_name, e.employee_name FROM departments d JOIN employees e ON d.department_id = e.department_id AND e.hiredate >= '2005-10-01'; ・SELECT e.employee_id, d.department_name, e.employee_name FROM departments d JOIN employees e USING(department_id) WHERE e.hiredate >= '2005-10-01'; が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT e.e...
- 参考URL: なし

### 問題ID 26820 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26820?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 2008年4月1日以降に入社した従業員のMANAGER_ID列の値を1005に変更するSQL文として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: 表名の代わりに副問合せを指定したUPDATE文では、副問合せのSELECT句に指定した列しか更新することができません。また、表名の代わりに副問合せを指定したUPDATE文にWHERE句を指定する場合も、副問合せのSELECT句に指定した列に関する条件しか指定できませんので注意しましょう。 では、選択肢のSQL文を1つずつ確認してみましょう。 ・UPDATE (SELECT manager_id, hiredate FROM employees) SET manager_id = 1005 WHERE hiredate >= '08-04-01'; 表名の代わりに副問合せを指定したUPDATE文です。更新する列、WHERE句の条件に指定した列ともに副問合せのSELECT句に指定されている列ですので、エラーにはならず、期待通りに更新されます。 ・UPDATE (SELECT manager_id FROM employees) SET manager_id = 1005 WHERE hiredate >= '08-04-01'; 表名の代わりに副問合せを指定したUPDATE文です。WHER...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10008.htm#SQLRF01708

### 問題ID 26821 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26821?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: EMP表の構造を確認して下さい。 CREATE TABLE emp ( id NUMBER(2) PRIMARY KEY, name VARCHAR2(10), birth DATE, salary NUMBER(8), note LONG ); 次のSQL文のうち、正常に実行されるものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: LONG型には以下の制限があります。 ・LONG型の列は1つの表に1つだけ定義できる ・LONG型の列には制約は定義できない(NULLおよびNOT NULL制約を除く) ・LONG型の列はGROUP BY句とORDER BY句に指定できない ・副問合せによる表の作成時、LONG型の列はコピーできない したがって、EMP表のNOTE列をGROUP BY句やORDER BY句に指定することはできません。 また、EMP表をコピーして新しい表を作成する際に、副問合せのSELECT句にNOTE列が含まれているとエラーとなります。 以上より、 ・SELECT id, name, birth FROM emp ORDER BY birth; ・CREATE TABLE emp2 AS SELECT id, salary FROM emp; が正解となります。 その他の選択肢については次のとおりです。 ・SELECT id, name, birth FROM emp ORDER BY note; ORDER BY句にNOTE列が指定されているのでエラーとなります。 ・SELECT AVG(salary...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00201

### 問題ID 26822 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26822?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE tmp ( id#9 NUMBER(2) NOT NULL, name$ VARCHAR2(20), birth_day DATE DEFAULT SYSDATE NOT NULL, age NUMBER(3), image777 LONG );
- 解説要約: CREATE TABLE文で表を作成する際、DEFAULTオプションに他の列を指定することはできませんが、関数やDEFAULTオプションを指定した列を指定することはできます。 また、LONG型の列に関しては1つの表に1つだけ定義することができます。 なお、列名は以下の命名規則にしたがって命名します。 ・オブジェクト名は30バイト以下 ・使用できる文字は、0~9,A~Z,a~z(日本語環境の場合は漢字,ひらがな,カタカナも使用可) ・使用できる記号は、_,$,#のみ ・オブジェクト名の先頭の文字は、数字,記号以外の文字 ・Oracleの予約語は使用できない 以上より、 ・正常に実行される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE tmp (id#9 NUMBER(2) NOT NULL, name$ VARCHAR2(20), birth_day DATE DEFAULT SYSDATE NOT NULL, age NUMBER(3), image777 LONG ); その他の選択肢については次のとおりです。 ・LONG...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF01402

### 問題ID 26823 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26823?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE tmp ( id NUMBER PRIMARY KEY, name VARCHAR2, birth_day DATE DEFAULT SYSDATE NOT NULL, age NUMBER, image777 LONG );
- 解説要約: VARCHAR2型の列データを定義する場合、データ長を必ず定義しなければなりません。 なお、NUMBER型ではデータ長の指定を省略することができます。 以上より、 ・VARCHAR2型にデータ長が指定されていないためエラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE TABLE tmp (id NUMBER PRIMARY KEY, name VARCHAR2, birth_day DATE DEFAULT SYSDATE NOT NULL, age NUMBER, image777 LONG ); その他の選択肢については次のとおりです。 ・正常に実行される VARCHAR2型のデータ長が省略されているためエラーとなります。 ・NUMBER型にデータ長が指定されていないためエラーとなる VARCHAR2型はデータ長を省略することはできませんが、NUMBER型では、データ長を省略することができます。省略された場合、最大精度の浮動小数点となります。 ・デフォルト値の指定に関数は使用できないためエラーとなる DEFAULTオプション...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i45694
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00222
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7002.htm#SQLRF01402

### 問題ID 26824 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26824?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PROD表の構造を確認して下さい。 次のSQL文のうち、正常に実行されるものはどれですか(該当するものを全て選択して下さい)。 ただし、日付書式は"RR-MM-DD"とします。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT startdate + '12-01-01' FROM prod; DATE型のSTARTDATE列の値に日付リテラルを加算しようとしていますが、DATE型同士の加算はできないため、Oracle Databaseは日付リテラルを数値へと暗黙的データ変換しようとします。ですが、'12-01-01'を数値へ変換できないためエラーとなります。 ・SELECT startdate + '10' FROM prod; DATE型のSTARTDATE列の値に文字リテラルを加算しようとしています。DATE型と文字型の加算はできませんが、'10'は暗黙的データ変換で数値の10に変換されるため、STARTDATE列の値に10日を加算した値が返されます。 ・SELECT 'name:' + name FROM prod; 文字リテラルと文字型の値を連結する場合は、連結演算子(||)を使用します。"+"では連結できませんのでエラーとなります。 SQLを表示 SELECT 'name:' + name FROM prod; SELECT 'name:' |...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements002.htm#SQLRF00214

### 問題ID 26825 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26825?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 数値書式のうち、負の値に関する書式とその説明として、正しいものはどれですか。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・TO_CHAR(-123456, '999999S') は -123456 と表示される 数値書式「S」は + または - 記号を表示します。「S」が数値書式の最初に指定された場合は値の前に、「S」が数値書式の最後に指定された場合は値の後に+ または - 記号を表示します。 この選択肢ではTO_CHAR関数の第一引数の値が負の値であり、「S」が数値書式の最後に指定されていますので、123456-と表示されます。 SQLを表示 SELECT TO_CHAR(-123456, '999999S') FROM dual; ・TO_CHAR(-123456, '999999') は 123456 と表示される 数値書式「9」は指定された桁数の値を表示します。値が負の値の場合は値の前に-記号を表示します。 この選択肢ではTO_CHAR関数の第一引数の値が負の値ですので、-123456と表示されます。 SQLを表示 SELECT TO_CHAR(-123456, '999999') FROM dual; ・TO_CHAR(-123456, '999999MI...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions201.htm#i79330
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34570

### 問題ID 26826 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26826?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 現在の日時は2012年12月12日午後10時28分35秒です。 現在時刻を次の形式で表示するには、どのSQL文を実行しますか。 ただし、実行環境は日本語環境とします。 2012年12月12日(水) 午後 10時28分35秒
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT TO_CHAR(SYSDATE, 'YYY"年"MM"月"DD"日 ("DY")" PM HH24"時"MI"分"SS"秒"') FROM dual; 年に「YYY」が指定されているため、「012年」のように3桁で表示されます。 また、時刻に「HH24」が指定されているため、「22時」と表示されます。 ・SELECT TO_CHAR(SYSDATE, 'RRRR"年"MM"月"DD"日 ("DY")" PM HH"時"MI"分"SS"秒"') FROM dual; このSQL文では設問の書式通りに表示されます。 ・SELECT TO_CHAR(SYSDATE, 'YYYY"年"MM"月"DD"日 ("DAY")" P.M. HH12"時"MI"分"SS"秒"') FROM dual; 曜日に「DAY」が指定されているため、「水曜日」と表示されます。 ・SELECT TO_CHAR(SYSDATE, 'RRR"年"MM"月"DD"日 ("DY")" HH12"時"MI"分"SS"秒"') FROM dual; 年を「RRR」と指定して...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions200.htm#i1009324
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34924

### 問題ID 26827 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26827?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: 次の2つのSQL文をSQL1),SQL2)の順で実行しました。 実行結果として正しいものはどれですか。 SQL1) CREATE OR REPLACE VIEW v_emp AS SELECT department_id, AVG(salary) avg_sal FROM employees GROUP BY department_id; SQL2) CREATE VIEW v_emp AS SELECT employee_name, salary, hiredate FROM employees WHERE hiredate >= '2008-04-01';
- 解説要約: ビューの作成時、OR REPLACEオプションを指定すると、既に同名のビューが存在する場合でもエラーとならず、ビューの定義を新しい定義で置き換えることができます。 同名のビューが存在しない場合は、新しいビューを作成します。 設問のSQL文では、SQL1)でOR REPLACEオプション付きでV_EMPビューを作成しています。もしもV_EMPビューが既に存在していたとしても、V_EMPビューはSQL1)の定義で置き換えられます。 次にSQL2)ですが、こちらのCREATE VIEW文ではOR REPLACEオプションを付けないでV_EMPビューを作成しています。この場合、SQL1)で作成したV_EMPビューはSQL2)で置き換えられません。同一スキーマに同名のビューを作成することはできませんのでSQL2)はエラーとなります。 以上より、 ・SQL1)が正常に実行され、SQL2)実行時にすでにv_empというビューが存在するので、SQL2)実行時にエラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 CREATE OR REPLACE VIEW v...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54760

### 問題ID 26828 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26828?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 索引を作成するのに適した列はどれですか(2つ選択して下さい)。
- 解説要約: 次の条件に該当する列に索引を作成すると、検索時のパフォーマンス向上につながります。 ・WHERE句の条件や結合条件としてよく使用される列 ・列にNULL値が多く含まれており、NULL値以外の値を指定して検索する列 ・表の規模が大きく、多くの問合せで15%未満の行を検索する列 以上より、 ・WHERE句の条件や結合条件としてよく使用される列 ・列にNULL値が多く含まれており、NULL値以外の値を指定して検索する列 が正解となります。
- 参考URL: なし

### 問題ID 26829 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26829?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: パブリックシノニムを削除する場合に必要な権限とSQL文の組合せとして、正しいものはどれですか。 ユーザー： 1) DROP ANY SYNONYM権限を持つユーザー 2) DROP PUBLIC SYNONIM権限を持つユーザー 3) データベース管理者 SQL文： a) DROP SYNONYM cust; b) DELETE PUBLIC SYNONYM cust; c) DROP PUBLIC SYNONYM cust; d) DELETE SYNONYM cust;
- 解説要約: パブリックシノニムの削除はDROP PUBLIC SYNONYM権限を持つユーザーによって行われます。 パブリックシノニムの削除は、DROP PUBLIC SYNONYM文で行います。 以上より、 ・権限：2) SQL文：c) が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9002.htm#SQLRF01805

### 問題ID 26830 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26830?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: パブリックシノニムを作成するSQL文として、正しいものはどれですか。
- 解説要約: パブリックシノニムはCREATE PUBLIC SYNONYM権限を持つユーザーによって作成されます。 パブリックシノニムは、CREATE PUBLIC SYNONYM文によって作成されます。 以上より、 ・CREATE PUBLIC SYNONYM dept FOR departments; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CONNECT GRANT CREATE PUBLIC SYNONYM to pingt; PINGTユーザーでログイン後、パブリックシノニムを作成します。 SQLを表示 CREATE PUBLIC SYNONYM dept FOR departments; その他の選択肢については次のとおりです。 ・CREATE SYNONYM dept FOR departments; パブリックシノニムを作成する場合は、CREATE SYNONYM文にPUBLICオプションを指定します。 ・CREATE PUBLIC SYNONYM dept ON departments; オブジェクト名はON句ではなくFOR句に指定します...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7001.htm#SQLRF01401

### 問題ID 26831 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26831?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: プライベートシノニムを作成するSQL文として、正しいものはどれですか。
- 解説要約: プライベートシノニムはCREATE SYNONYM権限を持つユーザーによって作成されます。 プライベートシノニムは、CREATE SYNONYM文によって作成されます。 以上より、 ・CREATE SYNONYM dept FOR departments; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 CREATE SYNONYM dept FOR departments; その他の選択肢については次のとおりです。 ・CREATE PRIVATE SYNONYM dept FOR departments; CREATE SYNONYM文にPRIVATEオプションはありません。 ・CREATE SYNONYM dept FROM departments; オブジェクト名はFROM句ではなくFOR句に指定します。 ・CREATE PUBLIC SYNONYM dept FOR departments; CREATE SYNONYM文にPUBLICオプションを指定すると、パブリックシノニムが作成されます。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_7001.htm#SQLRF01401

### 問題ID 26833 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26833?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: DEPARTMENTS表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか。 CREATE TABLE departments6 AS SELECT * FROM departments WHERE 1 = 0; CREATE SEQUENCE seq_dept; INSERT INTO departments6 VALUES (seq_dept.nextval, 'Sales', 1001); COMMIT; INSERT INTO departments6 VALUES (seq_dept.nextval, 'Dev', 1002); ROLLBACK; INS...
- 解説要約: 順序で値を生成したINSERT文がロールバックされると、表の状態はロールバックされますが、生成した順序値はロールバックされないので、欠番が生じる場合があります。 設問のSQL文では、2つ目のINSERT文でNEXTVAL擬似列は2を返します。ですが、直後のROLLBACK文で2つ目のINSERT文での処理は取消されてしまいます。その後のINSERT文でNEXTVAL擬似列は3を返すため、MANAGER_IDの値が1002である行のDEPARTMENT_IDの値は3となり、順序値2は欠番となります。 以上より、 ・MANAGER_IDの値が1002である行のDEPARTMENT_IDの値は3である が正解となります。 設問のSQL文の実行結果は次のとおりです。 SQLを表示 CREATE TABLE departments6 AS SELECT * FROM departments WHERE 1 = 0; CREATE SEQUENCE seq_dept; INSERT INTO departments6 VALUES (seq_dept.nextval, 'Sales', 1001)...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_6015.htm#SQLRF01314

### 問題ID 26834 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26834?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: INSTEAD OFトリガーを定義していないビューを通じてデータの追加、更新、削除を行う場合の説明として、正しいものはどれですか。
- 解説要約: ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 選択肢を1つずつ確認してみましょう。 ・ビューに含まれない実表の列にNOT NULL制約が定義されている場合は、NOT NULL制約が定義されている列にデフォルト値が設定されていれば、ビューを通じてデータを追加することができる ビューに含まれない実表の列にNOT NULL制約が定義されている場合、通常はデータの追加を行うことはできませんが、NOT NULL制約が定義されている列に、デフォルト値が設定されていれば、ビューを通じてデータを追加することができます。 SQLを表示 CREATE TABLE table1 (id NUMBER(2), name VARCHAR2(10), birth DATE NOT NULL ); CREATE VIEW view1 AS SELECT id, name FROM table1; INSERT INTO view1 VALUES (1, 'Tanaka'); SQLを表示 CREATE TABLE table2 (id NUMBER(2), name VARCHAR...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782

### 問題ID 26835 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26835?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: INSTEAD OFトリガーを定義していないビューを通じてデータの追加、更新、削除を行う場合の説明として、正しいものはどれですか。
- 解説要約: ビューを通じて実表のデータを操作することができる基本的なルールは次の通りです。 ビューの定義に式を含む列が定義されている場合、対象列を含むデータの追加、対象列のデータの更新を行うことはできません。 ですが、対象列以外はデータの追加、更新を行うことができます。 SQLを表示 DESC employees; CREATE VIEW v_emp AS SELECT employee_id, employee_name, salary * 12 salary FROM employees; INSERT INTO v_emp VALUES (1000, 'Tanaka', 8000000); INSERT INTO v_emp (employee_id, employee_name) VALUES (1000, 'Tanaka'); UPDATE v_emp SET salary = 0; UPDATE v_emp SET employee_name = 'Yamada' WHERE employee_id = 1000; 以上より、 ・ビューの定義に式を含む列が定義されていても、対象列以外は...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_8004.htm#SQLRF54782

### 問題ID 26836 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26836?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次の実行結果となるSQL文として正しいものはどれですか。 ただし、実行環境は日本語環境とします。 ¥500,000.0
- 解説要約: TO_CHAR関数は数値を書式化した文字列に変換します。 設問では、数値を3桁ごとにカンマ(,)で区切り、小数点以下1桁を表示しています。カンマ(,)や小数点(.)は数値書式の中でそのまま用いることができますが、カンマは「G」、小数点は「D」で指定することもできます。なお、数値書式において、カンマを小数点の右側に指定することはできません。 また、¥記号を表示する場合は、ローカル通貨記号の「L」を指定します。 以上より、 ・SELECT TO_CHAR(500000, 'L999G999D0') FROM dual; ・SELECT TO_CHAR(500000.0, 'L999G999D0') FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については、以下のとおりです。 ・SELECT TO_NUMBER('¥500,000.0', 'L999G999D0') FROM dual; TO_NUMBER関数は、文字列を指定された書式にしたがって数値に変換します。変換された数値は¥やカンマを含むことは出来ないため、誤りです。 ・SE...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions201.htm#i79330
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements004.htm#i34570

### 問題ID 26837 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26837?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 次のSQL文の実行結果と同じ実行結果となるSQL文として、正しいものはどれですか(該当するものを全て選択して下さい)。 SELECT q'(It's Monday today.)' FROM dual;
- 解説要約: 設問のSQL文では、代替引用符q演算子を使用していますので、一重引用符(')を含む文字リテラル 「It's Monday today.」 と表示されます。 これと同じように出力するためには代替引用符q演算子を使用するか、文字リテラル中の一重引用符(')を2つ続けて記述しなければなりません。 なお、q演算子は大文字、小文字のどちらで記述してもかまいません。 以上より、 ・SELECT 'It''s Monday today.' FROM dual; ・SELECT Q'$It's Monday today.$' FROM dual; が正解となります。 設問と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT q'(It's Monday today.)' FROM dual; SQLを表示 SELECT 'It''s Monday today.' FROM dual; SQLを表示 SELECT Q'$It's Monday today.$' FROM dual; その他の選択肢については次のとおりです。 ・SELECT 'It's Monday today.'...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#i42617

### 問題ID 26838 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26838?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 次のSQL文のうち、エラーとなるものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 代替引用符q演算子の引用符デリミタとして、[],<>,(),{}の記号を使用する場合は、括弧開き/括弧閉じの組合せで使用します。 また、引用符デリミタとして英文字を使用する場合、大文字と小文字は区別されるため、どちらか1つに統一しなければなりません。 以上より、 ・SELECT Q'[I'm fine.[' FROM dual; ・SELECT q'XI'm fine.x' FROM dual; が正解となります。 正解のSQL文の実行結果は次のようになります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#i42617

### 問題ID 26839 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26839?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL関数の実行結果として正しいものを1つ選択して下さい。 SELECT SUBSTR('Oracle Web問題集', -6, 3) FROM dual;
- 解説要約: SUBSTR関数は引数で指定された文字列の部分文字列を返す関数です。 SUBSTR関数は、1つ目の引数で指定された文字列のm文字目からn文字分の文字列を返しますが、2つ目の引数に負の値が指定された場合は、文字列の末尾から数えてm文字目からn文字分の文字列を返します。 設問のSQL文では、2つ目の引数に-6が指定されていますので、文字列の末尾から数えて6文字目である「W」から3文字分の文字列を返します。 以上より、 ・「Web」と表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT SUBSTR('Oracle Web問題集', -6, 3) FROM dual;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions181.htm#i87066

### 問題ID 26840 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26840?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL関数の実行結果として正しいものを1つ選択して下さい。 SELECT INSTR('Oracle Web問題集', 'WEB') FROM dual;
- 解説要約: INSTR関数は引数で指定した文字列中から検索文字列を検索し、その位置を返す関数です。 文字列が見つからない場合は「0」を返します。 設問のSQL分では、検索文字列に「WEB」が指定されています。INSTR関数では英文字の大文字と小文字は区別されますので、「Oracle Web問題集」から「WEB」を見つけることはできません。したがって、「0」を返します。 以上より、 ・「0」と表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT INSTR('Oracle Web問題集', 'WEB') FROM dual; 検索文字列を「Web」とした場合の実行結果は次のとおりです。 SQLを表示 SELECT INSTR('Oracle Web問題集', 'Web') FROM dual;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions080.htm#i77598

### 問題ID 26841 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26841?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 次のSQL文と同じ結果となるSQL文として、正しいものはどれですか。 SELECT emp.employee_name, mgr.employee_name FROM employees emp, employees mgr WHERE emp.manager_id(+) = mgr.employee_id;
- 解説要約: Oracle独自の結合構文で外部結合を行う場合、外部結合演算子(+)を使用します。条件の左側に(+)をつけると右側外部結合、右側につけると左側外部結合の結果と等しくなります。 設問のSQL文では、WHERE句に指定された条件の左側に(+)が付けられているので、右側外部結合の結果と等価になります。 以上より、 ・SELECT emp.employee_name, mgr.employee_name FROM employees emp RIGHT OUTER JOIN employees mgr ON emp.manager_id= mgr.employee_id; が正解となります。 設問と正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT emp.employee_name, mgr.employee_name FROM employees emp, employees mgr WHERE emp.manager_id(+) = mgr.employee_id; SQLを表示 SELECT emp.employee_name, mgr.employee_nam...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26842 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26842?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: SELECT文の機能について、正しい組合せはどれですか。
- 解説要約: SELECT文では「射影(投影)」、「選択」、「結合」の3つの機能を使用して表からデータを取得します。 射影(投影)：表から特定の列を取得します 選択：表から特定の行を取得します 結合：複数の表のデータを関連付けて取得します 以上より、 ・結合:複数の表のデータを関連付けて取得する が正解となります。 その他の選択肢については次のとおりです。 ・射影(投影):表から特定の行を取得する 射影(投影)は、表から特定の列を取得します。 ・参照:他の表のデータを取得する SELECT文の機能ではありません。 ・選択:表から特定の列を取得する 選択は、表から特定の行を取得します。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56306/sqllangu.htm#CNCPT88902

### 問題ID 26843 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26843?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のYOMI列に値が入ってない行を検索しようと以下のSQL文を実行しましたが、検索結果は1件も表示されませんでした。 該当のデータは3件あります。 SELECT employee_name, yomi FROM employees WHERE yomi = ''; WHERE句をどのように書き換えれば、希望のデータが検索されるでしょうか。
- 解説要約: フィールドに値が格納されていない状態をNULL値といい、列がNULL値であるかを判定するには、IS NULL演算子を使用します。IS NULL演算子では、列の値がNULL値である場合に条件が成立します。 NULL値は特殊な値ですので、列の値がNULL値かどうかの判定はIS NULL演算子以外の比較演算子ではできません。 設問のSQL文のようにNULL値に対して=(等号)などの比較演算子を使用した場合、条件の判定がNULL値となり検索結果は1行も表示されません。（エラーにはなりません） 以上より、 ・WHERE yomi IS NULL; が正解となります。 その他の選択肢については以下のとおりです。 ・WHERE yomi = ""; 文字リテラルを二重引用符(")で囲むとエラーとなります。 ・WHERE yomi IS NOT NULL; IS NOT NULL演算子は、NULL値でない場合に条件が成立します。 ・WHERE employee_name IS NULL; YOMI列ではなくEMPLOYEE_NAME列の値を判定しているので、希望のデータは検索されません。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements005.htm#SQLRF51095

### 問題ID 26844 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26844?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文を実行して表示される製品名として正しいものはどれですか(該当するものを全て選択して下さい)。 SELECT prod_name FROM products WHERE UPPER(prod_name) BETWEEN 'H' AND 'LE';
- 解説要約: BETWEEN演算子の下限値、上限値に文字リテラルが指定された場合は、指定された文字列の文字コードの範囲で検索が行われます。 設問の場合は、UPPER(prod_name)で全て大文字に変換された商品名の頭文字が「H」で始まるものから、「LE」という2文字の文字コードの範囲までが検索されます。 以上より、 ・HighPower_LED_ハンディライト2 ・Lantern が正解となります。 設問のSELECT文の実行結果は次のようになります。 SQLを表示 SELECT prod_name FROM products WHERE UPPER(prod_name) BETWEEN 'H' AND 'LE'; ちなみに、このSQL文でUPPER関数を使わないと、商品名「Lantern」はヒットしません。2文字目の小文字の「a」は大文字の全アルファベットより文字コードが大きいからです。 SQLを表示 SELECT prod_name FROM products WHERE prod_name BETWEEN 'H' AND 'LE'; UPPER関数で大文字「LANTERN」にした場合は、最...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions011.htm#CJAGAIDD

### 問題ID 26845 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26845?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文を実行し、置換変数の入力を促されたら1に「prod」を、2に「Mozart」を入力して、PROD表の結果が出力されました。 SELECT * FROM &&1 WHERE name = '&2'; 続けて2回目にこのSQL文を実行するとどうなりますか。
- 解説要約: 置換変数には「&置換変数」と「&&置換変数」の2種類があり、「&置換変数」はSQL文実行後に変数の値が破棄されますが、「&&置換変数」はセッションを切断もしくはUNDEFINEコマンドで破棄するまで値が保持されます。 以上より、 ・2のみに値を入力するよう促される が正解となります。 以下は設問のSQL文を2回実行した結果です。
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQPUG/GUID-68AC9FF2-B92A-48D1-9699-133D47F8DDC1.htm

### 問題ID 26846 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26846?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: Oracle Databaseで使用できる単一行関数とその説明として正しい組合せはどれですか。
- 解説要約: Oracle Databaseに予め用意されているSQL関数には、単一行関数とグループ関数の2種類があります。 選択肢を1つずつ確認します。 ・MOD:除算の余りを返す 正解です。MOD関数は引数で指定された数値の除算の余りを返します。 MOD(n, m) n：割られる数 m：割る数 ・TRIM:数値、日付値を切り捨てて返す TRUNC関数の説明なので、誤った記述です。 TRIM関数は引数で指定された文字列の前後にある削除文字を取り除いて文字列を返します。 TRIM([LEADING | TRAILING | BOTH] [削除文字] FROM 文字列) または TRIM(文字列) ・LAST_DAY:月の最終日の日付を返す 正解です。LAST_DAY関数は引数で指定された日付を含む月の最終日を返します。 LAST_DAY(日付) ・INITCAP:文字列を小文字に変換する LOWER関数の説明なので、誤った記述です。 INITCAP関数は引数で指定された文字列中の単語の先頭文字を大文字、それ以外を小文字で返します。 INITCAP(文字列) ・SUBSTR:指定した文字列が現れる位置...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions001.htm#CJAHCIID

### 問題ID 26847 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26847?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: SQL関数である単一行関数のタイプとして正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 単一行関数は、その処理内容等によって次のように分類されます。 以上より、 ・変換関数 ・日付関数 ・汎用関数 が正解となります。 その他の選択肢については次のとおりです。 ・論理関数 ・データ関数 このような関数はありません。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions002.htm#CJAJHBIA

### 問題ID 26848 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26848?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: PRODUCTS表の構造を確認して下さい。 次のSQL文の実行結果と同じ結果となるSQL文はどれですか。 SELECT prod_name FROM products WHERE prod_name LIKE '%i%' AND SUBSTR(prod_name, LENGTH(prod_name)-2, 1) = 'ラ';
- 解説要約: まず、設問のSQL文の検索条件を確認しましょう。 SELECT prod_name FROM products WHERE prod_name LIKE '%i%' AND SUBSTR(prod_name, LENGTH(prod_name)-2, 1) = 'ラ'; ・prod_name LIKE '%i%' PROD_NAME列が「i」を含む行を検索します。 ・SUBSTR(prod_name, LENGTH(prod_name)-2, 1) = 'ラ'; LENGTH(prod_name) : PROD_NAME列の文字列の長さを返します。 SUBSTR(prod_name, LENGTH(prod_name)-2, 1) : PROD_NAME列の[PROD_NAME列の長さ - 2]文字目から、1文字分の文字列を返します。 すなわち、PROD_NAMEの末尾から3文字目が「ラ」である行を検索します。 まとめると、PROD_NAME列が「i」という文字を含み、かつ、末尾から3文字目が「ラ」である行を問合せるSQL文です。 上記と同じ条件を記述した正解のSQL文は以下です。 ・...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions181.htm#i87066
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions080.htm#i77598

### 問題ID 26849 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26849?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: PRODUCTS表の構造を確認して下さい。 製品名にスペースが入っており、スペースの後の1つ目の単語が大文字の「L」もしくは小文字の「l」で始まる製品を検索します。 どのSQL文を使用しますか(該当するものを全て選択して下さい)。
- 解説要約: 検索条件を1つずつ確認しましょう。 ・製品名にスペースが入っている INSTR関数でPROD_NAMEのスペースの位置を検索し、結果が0でない(スペースの位置を返す)行というように記述できます。 INSTR(prod_name,' ') <> 0 ※不等号は「!=」「^=」も使えます。 ・スペースの後の1つ目の単語が大文字の「L」もしくは小文字の「l」で始まる SUBSTR関数でPROD_NAMEのスペースの後の文字を抽出します。 SUBSTR(prod_name, INSTR(prod_name,' ')+1) : スペースの後から末尾までの文字列を返す SUBSTR(prod_name, INSTR(prod_name,' ')+1, 1) : スペースの後の1文字を返す また、文字列が大文字か小文字を問わない場合は、UPPER関数かLOWER関数で大文字、小文字のいずれかに変換した上で条件と比較します。 以上より、 ・SELECT prod_name FROM products WHERE INSTR(prod_name,' ') ^= 0 AND UPPER(SUBSTR(pr...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions181.htm#i87066
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions080.htm#i77598

### 問題ID 26850 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26850?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: CUSTOMERS表の構造を確認して下さい。 顧客名と、郵便番号の「-(ハイフン)」より後ろの数字を「*」に置き換えて表示します。 どのSQL文を使用しますか。 顧客名 郵便番号 ------ ---------- 田中浩二 142-**** 佐々木二郎 146-**** 山口真弓 142-****
- 解説要約: 選択肢のSQL文を1つずつ確認してみましょう。 ・SELECT cust_last_name || cust_first_name "顧客名", RPAD(SUBSTR(cust_postal_code, 1, INSTR(cust_postal_code, '-')), LENGTH(cust_postal_code), '*') "郵便番号" FROM customers; INSTR(cust_postal_code, '-')でCUST_POSTAL_CODEの「-(ハイフン)」の位置を抽出し、 SUBSTR(cust_postal_code, 1, INSTR(cust_postal_code, '-')でCUST_POSTAL_CODEの先頭から「-(ハイフン)」までの文字列を抽出します。 抽出した文字列に、RPAD関数でLENGTH(cust_postal_code) = CUST_POSTAL_CODEの文字数分になるように右側に「*」を埋め込みます。 このSQL文が正解です。 SQLを表示 SELECT cust_last_name || cust_first_nam...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions159.htm#SQLRF06103

### 問題ID 26851 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26851?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL文を実行して表示される製品名として正しいものはどれですか。 SELECT prod_name FROM products WHERE INSTR(prod_name, ' ', 1, 2) <> 0;
- 解説要約: INSTR関数は、引数で指定された文字列のm文字目以降からn回目に出現した検索文字列の先頭の位置を返します。検索文字列が見つからなかった場合は0（ゼロ）を返します。 INSTR(文字列, 検索文字列[, m][, n]) 設問のSQL文では、PROD_NAME列の1文字目から「 」(スペース)を検索し、2回目に一致した位置を返し、<> 0でINSTR関数の結果が0でない、すなわち2回目のスペースが含まれている行を検索します。 以上より、 ・BEST HITS_80's DANCE が正解となります。 その他の選択肢はスペースが1つしか含まれていないため、検索でヒットしません。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions080.htm#i77598

### 問題ID 26852 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26852?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 勤続10年を超えた社員は、勤続年数 × 1万円の勤続手当がもらえることになりました。 社員名、勤続手当の額と、該当しない社員には「勤続手当なし」と出力するSQL文を作成しました。 このSQL文に関して正しい記述はどれですか。 SELECT employee_name "社員名", CASE WHEN (SYSDATE - hiredate)/ 365 > 10 THEN TO_CHAR(TRUNC((SYSDATE - hiredate)/ 365) * 10000) ELSE '勤続手当なし' END "勤続手当" FROM employees;
- 解説要約: 検索CASE式は、条件を条件1から順番に判定し、条件が真の場合に条件に対応する戻り値を返します。真となる条件が1つも存在しない場合は、ELSE句に指定されたデフォルトの戻り値が返されますが、ELSE句が指定されていない場合はNULL値を返します。 CASE WHEN 条件1 THEN 戻り値1 [WHEN 条件2 THEN 戻り値2 ...] [ELSE デフォルトの戻り値] END 設問のSQL文では、(SYSDATE - hiredate)/ 365で入社日から現在までの勤続年数を求め、10年を超える場合は、TRUNCで小数点以下を切り捨てた勤続年数 × 10000で手当の額を算出しています。この条件に該当しない場合は、「勤続手当なし」と表示します。 正しい結果を返すSQL文です。 CASE式では、WHEN句で比較条件やINやLIKEなどの演算子が使用できますが、DECODE関数では使用できません。設問のような条件はDECODE関数では記述できません。 選択肢のDECODE関数のSQL文はエラーになります。 以上より、 ・DECODE関数には置き換えられない が正解となります。 設...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions004.htm#SQLRF20037
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions049.htm#SQLRF00631

### 問題ID 26853 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26853?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PROMOTIONS表の構造を確認して下さい。 プロモーションの開始日(PROMO_BEGIN_DATE)が週末だったら「週末」を、平日だったら「平日」と表示します。 正しい結果を得られないSQL文はどれですか。 ただし、データベースの実行環境は日本語環境とします。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT promo_name, promo_begin_date, CASE TO_CHAR(promo_begin_date, 'DAY') WHEN '土曜日' THEN '週末' WHEN '日曜日' THEN '週末' ELSE '平日' END "開始日" FROM promotions; 単純CASE式です。TO_CHAR(promo_begin_date, 'DAY')で、PROMO_BEGIN_DATEの曜日を文字列として抜き出して、値が「土曜日」か「日曜日」の順に判定を行い、いずれにも該当しない場合は「平日」を返します。 正しいSQL文です。 SQLを表示 SELECT promo_name, promo_begin_date, CASE TO_CHAR(promo_begin_date, 'DAY') WHEN '土曜日' THEN '週末' WHEN '日曜日' THEN '週末' ELSE '平日' END "開始日" FROM promotions; ・SELECT promo_name, promo_begin_...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions004.htm#SQLRF20037
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions049.htm#SQLRF00631

### 問題ID 26854 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26854?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: WHERE句とHAVING句について、正しい記述はどれですか(該当するものを全て選択して下さい)。
- 解説要約: HAVING句を指定することで、SELECT文で取り出すグループを制限できます。 以下の手順でグループが制限されます。 1. WHERE句がある場合は、グループ化する前にWHERE句の条件で行を制限する 2. GROUP BY句に従ってグループ化する 3. グループ関数を適用する 4. HAVING句の条件で取り出すグループを制限する WHERE句にはグループ関数を使用できませんが、HAVING句にはグループ関数を条件に使用できます。 以上より、 ・WHERE句でグループ関数は使用できない ・WHERE句で行を制限した後に、GROUP BY句でグループ化する ・HAVING句でグループを制限する が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55327
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26855 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26855?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: ORDERS表の構造を確認して下さい。 年ごとのオーダー数を集計するために以下のSQL文を実行しましたが、エラーとなりました。 エラーの原因として正しいものはどれですか。 SELECT TO_CHAR(order_date, 'YYYY'), SUM(order_total) FROM orders GROUP BY TO_CHAR(order_date, 'RR');
- 解説要約: GROUP BY句を指定したSELECT文のSELECT句には、GROUP BY句で指定した列、もしくはグループ関数のみを指定できます。 設問のSQL文ではSELECT句ではTO_CHAR(order_date, 'YYYY')と、日付をYYYY書式の文字列に変換していますが、GROUP BY句ではRR書式に変換しています。このようにSELECT句とGROUP BY句のデータ型の変換が異なると、エラーになります。 以上より、 ・SELECT句のデータ型変換がGROUP BY句と異なるため が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT TO_CHAR(order_date, 'YYYY'), SUM(order_total) FROM orders GROUP BY TO_CHAR(order_date, 'RR'); SELECT句とGROUP BY句の書式を合わせると、正常に実行できます。 SQLを表示 SELECT TO_CHAR(order_date, 'YYYY'), SUM(order_total) FROM orders G...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038

### 問題ID 26856 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26856?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: EMPLOYEES表、JOBS表の構造を確認して下さい。 全社員の氏名とその上司の氏名と職種を表示するSQL文を作成しました。 空欄に入るJOIN句の組み合わせとして正しいものはどれですか。 SELECT e.employee_name, m.employee_name manager_name, j.job_name FROM employees e ___________ employees m ON e.manager_id = m.employee_id __________ jobs j ON e.job_id = j.job_id;
- 解説要約: 全社員の氏名はEMPLOYEES表から取り出せます。 社員の上司の氏名を取り出すには、EMPLOYEES表のMANAGER_ID列の値でEMPLOYEES表を検索し、EMPLOYEE_NAME列の値を取り出す必要があります。 このようなデータの取り出しを行うには、従業員の氏名を持つEMPLOYEES表と、MANAGER_IDを持つEMPLOYEES表があると見立てて、2つの表を結合します(自己結合といいます)。 また、職種を取り出すには、EMPLOYEES表とJOBS表をJOB_ID列で結合しJOB_NAME列の値を取り出します。 従業員の氏名を持つEMPLOYEES表、MANAGER_IDを持つEMPLOYEES表、JOBS表の3つの表を結合します。 全社員の氏名を表示するということは「上司のいない(MANAGER_IDがNULLの)社員も表示」するので、EMPLOYEES表の自己結合では、JOIN句の左側に指定された従業員の氏名を持つEMPLOYEES表のデータを全て取り出す左側外部結合を行います。また、EMPLOYEE_ID列とMANAGER_ID列を結合するため、異なる列名を結...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52353

### 問題ID 26857 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26857?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: Oracle Databaseに用意されているSQL関数で行える演算はどれですか(該当するものを全て選択して下さい)。
- 解説要約: SQL関数とはOracleに予め用意されている関数のことです。 主に以下のような関数があります。 [単一行関数] MOD(m, n) :mをnで割った余りを返す POWER(m, n) :mをn乗したべき乗を返す ROUND(m [,n]) :mを小数点以下n桁に四捨五入した値を返す [グループ関数] COUNT([DISTINCT | ALL] {列名 | 列名を含む式}) :データの件数を返す MAX([DISTINCT | ALL] {列名 | 列名を含む式}) :最大値を返す MIN([DISTINCT | ALL] {列名 | 列名を含む式}) :最小値を返す AVG([DISTINCT | ALL] {列名 | 列名を含む式}) :平均値を返す SUM([DISTINCT | ALL] {列名 | 列名を含む式}) :合計値を返す 以上より、 ・最大値を求める ・合計値を求める ・べき乗を求める が正解となります。 以下の、その他の選択肢の演算を行えるSQL関数はありません。 ・減算 ・除算の商を求める
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions001.htm#CJAHCIID

### 問題ID 26858 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26858?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せを実行したところエラーとなりました。 正常に実行するためにはどこを修正すればよいでしょうか。 SELECT MIN(AVG(salary)) FROM employees GROUP BY department_id HAVING MIN(AVG(salary)) > 400000;
- 解説要約: 設問のSQL文では、HAVING句で取り出すグループを制限していますが、HAVING句ではグループ関数をネストできません。 SELECT句ではグループ関数を2つまでネストできます。 以上より、 ・HAVING句のグループ関数 が正解となります。 では、SQL文の実行結果を見てみましょう。 部署(DEPARTMENT_ID)毎の給与(SALARY)の平均値が400000を超えるもので一番最小値を出力します。 正常に実行するために、HAVING句のグループ関数をMIN(AVG(salary))から(AVG(salary)に修正しています。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26859 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26859?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次の問合せを実行しました。実行結果について正しいものはどれですか。 SELECT employee_id, AVG(salary) FROM employees HAVING AVG(salary) >= MIN(salary) * 1.5 GROUP BY department_id;
- 解説要約: GROUP BY句を指定したSELECT文のSELECT句には、GROUP BY句で指定した列、もしくはグループ関数のみ指定できます（SELECT句に指定したグループ関数以外の列はすべてGROUP BY句で指定する必要がある）。 設問のSQL文では、SELECT句にGROUP BY句で指定していないemployee_idがあるので、エラーとなります。 以上より、 ・SELECT句にGROUP BY句で指定していない列があるのでエラーとなる が正解となります。 正しく実行するためには、SELECT句にdepartment_idを指定します。 SQLを表示 SELECT employee_id, AVG(salary) FROM employees HAVING AVG(salary) >= MIN(salary) * 1.5 GROUP BY department_id; SQLを表示 SELECT department_id, AVG(salary) FROM employees HAVING AVG(salary) >= MIN(salary) * 1.5 GROUP BY depa...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20038
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF20040

### 問題ID 26860 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26860?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQL文を実行するとエラーになりました。正しく実行するにはどのように修正しますか。 SELECT d.department_id, d.department_name, e.employee_name FROM employees e JOIN departments d USING (department_id) WHERE d.department_id IN (1, 5) ORDER BY department_name, employee_name;
- 解説要約: USING句を使用した表の結合では結合列に表接頭辞を使用できません。 設問のSQL文ではdepartment_idが結合列ですが、SELECT句とWHERE句でdepartment_idに表接頭辞を使用しているため、エラーとなります。 以上より、 ・全てのdepartment_idから表接頭辞を削除する が正解となります。 設問のSQL文と、それを修正した結果は次のようになります。 SQLを表示 SELECT d.department_id, d.department_name, e.employee_name FROM employees e JOIN departments d USING (department_id) WHERE d.department_id IN (1, 5) ORDER BY department_name, employee_name; SQLを表示 SELECT department_id, d.department_name, e.employee_name FROM employees e JOIN departments d USING (dep...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55315
  - https://atmarkit.itmedia.co.jp/ait/articles/1203/22/news164.html

### 問題ID 26861 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26861?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 外部結合の説明として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: 結合条件を満たしたデータのみを取り出すのではなく、検索条件を満たしていないデータも一緒に取り出す方法を外部結合といいます。 Oracle独自の結合構文では外部結合演算子(+)を使用して外部結合を行えますが、完全外部結合は行えません。 以上より、 ・結合条件を満たす行と満たさない行の両方を取り出す ・Oracle独自の結合構文には完全外部結合はない が正解となります。 その他の選択肢については以下のとおりです。 ・結合条件を満たす行のみを取り出す 結合条件を満たす行のみを取り出す結合を内部結合といいます。 ・結合条件を満たさない行のみを取り出す 外部結合では、結合条件を満たす行と満たさない行の両方を取り出します。 ・NULL値を持たない列のみ結合できる NULL値を持つ列を結合でき、結合条件を満たさない行も取り出せます。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26862 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26862?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 平均給与が400000を超える部署に所属する従業員を検索するために、次の問合せを実行しました。 SELECT employee_name, salary, department_id FROM employees WHERE department_id IN (SELECT department_id, AVG(salary) FROM employees GROUP BY department_id HAVING AVG(salary) > 400000); この問合せについて正しい記述はどれですか。
- 解説要約: 設問のSQL文では、副問合せで部署毎の平均給与が400000を超える部署と平均給与を検索しており、複数の列を返す複数列副問合せになっています。これ自体は正しいSQL文です。 しかし、主問合せのWHERE句でDEPARTMENT_ID列と副問合せの結果を比較していますが、副問合せのSELECT句の列数が多いためエラーとなります。 以上より、 ・副問合せのSELECT句が正しくないためエラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_name, salary, department_id FROM employees WHERE department_id IN (SELECT department_id, AVG(salary) FROM employees GROUP BY department_id HAVING AVG(salary) > 400000); SQLを表示 SELECT employee_name, salary, department_id FROM employees WHERE dep...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858

### 問題ID 26863 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26863?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: FROM句の副問合せのことを何と呼びますか。
- 解説要約: 副問合せは、SELECT文のSELECT句、FROM句、WHERE句、HAVING句の他、INSERT文やUPDATE文等のDML文でも使用できます。 FROM句の副問合せはインライン・ビューとも呼ばれます。 SQLを表示 SELECT emp.* FROM (SELECT employee_name, hiredate, salary FROM employees WHERE department_id = 5) emp; 以上より、 ・インライン・ビュー が正解となります。 その他の選択肢については以下のとおりです。 ・ネスト 関数の引数に別の関数を指定することを「関数のネスト」といいます ・内部結合 内部結合は、表の結合において結合条件を満たすデータのみを取り出す方法です。 ・複数行副問合せ 複数行副問合せは、複数件のデータを返す副問合せのことです。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858
  - https://atmarkit.itmedia.co.jp/ait/articles/1209/14/news146.html

### 問題ID 26864 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26864?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造とGRADE表の構造とデータを確認して下さい。 最高給与の従業員名と給与、給与等級を表示する以下のSQL文を作成しました。 従業員の給与等級は、EMPLOYEES表のSALARY列の値と、GRADE表のLOW列からHIGH列の値の範囲で決定します。 SELECT employee_name, salary, grade FROM employees, grade WHERE salary = (SELECT MAX(salary) FROM employees) AND salary BETWEEN low AND high ORDER BY 3, 2 DESC, 1...
- 解説要約: 設問のSQL文は、Oracle独自の結合構文による非等価結合です。 Oracle独自の結合構文ではWHERE句に結合条件を指定します。 非等価結合は、結合条件に=(等号演算子)以外の演算子を用いて、条件を満たすデータを取り出す結合です。非等価結合では、結合条件に<,>,<=,>=,BETWEEN等の演算子を使用します。 設問では、WHERE句の2番目の条件「salary BETWEEN low AND high」でEMPLOYEES表のSALARY列の値がGRADE表のHIGH列とLOW列の値の範囲内である行を結合し、従業員の給与等級を表示しています。 また、WHERE句の1番目の副問合せでEMPLOYEES表の最高給与を検索しています。 以下の2つのSQL文が設問と同じ条件を満たし、正解となります。 ・SELECT employee_name, salary, grade FROM employees, grade WHERE salary IN (SELECT MAX(salary) FROM employees) AND salary BETWEEN low AND high O...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF30046
  - https://atmarkit.itmedia.co.jp/ait/articles/1204/23/news132.html

### 問題ID 26865 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26865?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造とデータを確認して下さい。 次の問合せの実行結果について、正しい記述はどれですか。 SELECT department_id, salary, employee_name FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE department_name = '開発') AND salary < (SELECT MAX(salary) FROM employees WHERE department_id IN (SELECT de...
- 解説要約: 設問のSQL文では、副問合せを使用して、DEPARTMENTS表から「開発」部門のDEPARTMENT_IDを取り出しEMPLOYEES表の同列と比較しています。また、副問合せのネストを使用し、「開発」部門の最高給与より少ない給与であることという別条件を指定しています。正しく実行できるSQL文です。 以上より、 ・「開発」部門の中で最高給与でない従業員を表示する が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, salary, employee_name FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE department_name = '開発') AND salary < (SELECT MAX(salary) FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE departmen...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858
  - http://www.atmarkit.co.jp/ait/articles/1208/06/news118.html

### 問題ID 26866 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26866?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 給与の額が所属する部署の最低給与を超える従業員の一覧と、部署ごとの最低給与を表示します。 以下の問合せを実行しましたが、実行結果について正しい記述はどれですか。 SELECT e.employee_name, e.salary, e.department_id, s.minsal FROM employees e, (SELECT department_id, MIN(salary) minsal FROM employees GROUP BY department_id) s WHERE e.salary > s.minsal ORDER BY ...
- 解説要約: 設問のSQL文は、Oracle独自の結合構文です。 Oracle独自の結合構文では、 ・結合する表名は,(カンマ)で区切ってFROM句に指定 ・結合条件はWHERE句に指定 ・結合条件以外の条件はWHERE句に指定した結合条件の後にAND演算子で指定 します。 設問のSQL文ではEMPLOYEES表と、部署ごとの最低給与を問合せる（ ）で囲まれた副問合せをFROM句に指定し、両者を結合しています。 しかし、WHERE句には「e.salary > s.minsal」という検索条件しか指定されておらず、結合条件が欠けています。この場合エラーとはなりませんが、結合した全てのデータの組み合わせが返ってくるので正しい結果は得られません。 以上より、 ・実行されるが正しい結果が返されない が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT e.employee_name, e.salary, e.department_id, s.minsal FROM employees e, (SELECT department_id, MIN(salary) min...
- 参考URL: なし

### 問題ID 26867 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26867?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: PRODUCTS表とSALES表の構造を確認して下さい。 次の問い合わせの実行結果として、正しいものはどれですか。 SELECT p.prod_name, s.qty_sold FROM (SELECT prod_id, SUM(quantity_sold) qty_sold FROM sales GROUP BY prod_id) s RIGHT OUTER JOIN products p ON s.prod_id = p.prod_id;
- 解説要約: 設問のSQL文では、FROM句の副問合せでSALES表からPROD_IDごとの販売総数を取り出し、その結果とPRODUCTS表を結合して製品名と販売総数を表示しています。 JOIN句では、RIGHT OUTER JOINの右側にPRODUCTS表が指定されているため、結合条件を満たしていない製品名も全て取り出されます。 以上より、 ・売上の有無にかかわらず、全ての製品名が表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT p.prod_name, s.qty_sold FROM (SELECT prod_id, SUM(quantity_sold) qty_sold FROM sales GROUP BY prod_id) s RIGHT OUTER JOIN products p ON s.prod_id = p.prod_id;
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries006.htm#SQLRF52354

### 問題ID 26868 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26868?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 最も年収の高い従業員名と年収を表示する問合せはどれですか。 ただし、年収は月給(SALARY列)の12ヶ月分に歩合給(COMMISSION列)を足したものとします。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT employee_name, (SELECT MAX(salary * 12 + commission) FROM employees) "ANNUAL SALARY" FROM employees; WHERE句で検索条件を指定していないため、全従業員名と最高年収が表示されます。誤ったSQL文です。 ・SELECT employee_name, (salary * 12 + commission) "ANNUAL SALARY" FROM employees WHERE (salary * 12 + commission) = (SELECT MAX(salary * 12 + commission) FROM employees); WHERE句の副問合せで最高年収を取り出し、それと同じ年収の従業員だけを表示します。正しいSQL文です。 ・SELECT employee_name, "ANNUAL SALARY" FROM employees WHERE (salary * 12 + commission) = (SELECT ...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858
  - http://www.atmarkit.co.jp/ait/articles/1208/06/news118.html

### 問題ID 26869 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26869?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 所属する従業員の数が一番多い部署を検索する問合せを作成しました。 SELECT department_id, COUNT(*) FROM employees GROUP BY department_id HAVING COUNT(*) = (SELECT MAX(COUNT(*)) FROM employees GROUP BY department_id); この問合せの実行結果について、正しい記述はどれですか。
- 解説要約: 設問のSQL文では、まず、主問合せのGROUP BY句でDEPARTMENT_ID(部署)ごとにグループ化しています。HAVING句では、副問合せによって各部署の中で一番多い行数を取り出し、その行数と同じ行数の部署を取り出しています。正しいSQL文です。 以上より、 ・正常に実行され正しい結果を返す が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, COUNT(*) FROM employees GROUP BY department_id HAVING COUNT(*) = (SELECT MAX(COUNT(*)) FROM employees GROUP BY department_id); その他の選択肢については次のとおりです。 ・正常に実行されるが正しい結果を返さない 設問の条件どおりのSQL文です。 ・副問合せのグループ関数のネストでエラーになる 副問合せでは、GROUP BY句を指定して2レベルまでグループ関数をネストしているので問題ありません。 ・比較演算子=でエラーになる 単一行演算子である...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858
  - http://www.atmarkit.co.jp/ait/articles/1208/06/news118.html

### 問題ID 26870 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26870?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PROMOTIONS表の構造とデータを確認して下さい。 プロモーション開始日(PROMO_BEGIN_DATE)が2011年と2012年のプロモーションの数を表示します。 次のようなレポートを出力できるSQL文はどれですか(該当するものを全て選択して下さい)。 ただし、日付書式は"RR-MM-DD"とします。
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・SELECT COUNT(DECODE(TO_CHAR(promo_begin_date, 'rr'),'11',1,0)) "2011年のプロモーション", COUNT(DECODE(TO_CHAR(promo_begin_date, 'rr'),'12',1,0)) "2012年のプロモーション" FROM promotions; SELECT句の各列のDECODE関数は(TO_CHAR(promo_begin_date, 'rr')で取り出した年が「11」か「12」だったら、1を、それ以外は0を返します。が、その結果を渡しているCOUNT関数は単にデータの件数を返すので、全データの件数が表示されます。誤ったSQL文です。 ・SELECT SUM(DECODE(TO_CHAR(promo_begin_date, 'rr'),'11',1,0)) "2011年のプロモーション", SUM(DECODE(TO_CHAR(promo_begin_date, 'rr'),'12',1,0)) "2012年のプロモーション" FROM promotio...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions004.htm#SQLRF20037
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/functions049.htm#SQLRF00631

### 問題ID 26871 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26871?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: PAYMENTS表の構造を確認して下さい。 15時より前に完了した決済の日時(PAYMENT_DATE)と金額(PAYMENT_AMT)のレポートを作成します。 金額が入っていない場合は「-1」と表示します。 どの問合せを実行しますか(該当するものを全て選択して下さい)。 ただし、実行環境は日本語環境とし、PAYMENT_AMT列を次の形式で表示します。 例) ¥10,000
- 解説要約: TIMESTAMP型はDATE型を拡張したデータ型で、世紀、年、月、日、時、分、秒に加え、秒の小数点以下の値を格納できます。 設問の条件のように15時より前のPAYMENT_DATEを取り出すには、TO_CHAR(payment_date, 'HH24') < 15で、15時より前の時間を検索します。ここでは文字列→数値への暗黙的なデータ変換が行われます。 PAYMENT_AMT列を設問の書式にするには、TO_CHAR(payment_amt, 'L99,999,999')を指定します。 では、選択肢を1つずつ確認してみましょう。 ・SELECT TO_CHAR(payment_date, 'RR-MM-DD HH24:MI:SS') "決済日時", NVL(TO_CHAR(payment_amt, 'L99,999,999'), '未入力') "金額" FROM payments WHERE TO_DATE(payment_date, 'HH24') < 15; WHERE句の条件にTO_DATE(payment_date, 'HH24') < 15が指定されていますが、数値<->日...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00203
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements002.htm#SQLRF00214

### 問題ID 26872 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26872?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: EMPLOYEES表の構造を確認してください。 以下の問合せの結果と同じデータ型を返すSQL文はどれですか。 SELECT SYSDATE - hiredate FROM employees
- 解説要約: 設問のSQL文のSYSDATE - hiredate(日付値 - 日付値)は、2つの日付値間の日数を計算するので、演算結果のデータ型は数値です。 選択肢のSQL文の中では、TO_CHAR(hiredate, 'RR')で年だけ文字列として取り出し、それに数値を加算した場合、暗黙的なデータ変換が行われ数値データが返ります。 以上より、 ・SELECT TO_CHAR(hiredate, 'RR') + 10 FROM employees; が正解となります。 その他の選択肢については次のとおりです。 ・SELECT SYSDATE + hiredate FROM employees; 日付値 + 日付値の演算はできません。エラーとなるので、誤ったSQL文です。 ・SELECT TRUNC(hiredate) FROM employees; 日付値を引数に指定するTRUNC関数は、書式が省略された場合は"DD"が指定されたものとして日付データ当日の午前0時を返します。結果のデータ型は日付値です。よって、誤ったSQL文です。 TRUNC(日付[, 書式]) : 引数で指定された日付値を切り捨...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#SQLRF00202
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements003.htm#BABGIGCJ
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements001.htm#i48042

### 問題ID 26873 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26873?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: PRODUCTS表のデータを確認してください。 次のSQL文の実行結果として正しいものはどれですか。 SELECT TRIM('LED' FROM UPPER(prod_name)) FROM products WHERE LOWER(prod_name) LIKE 'led%';
- 解説要約: TRIM関数は、引数で指定された文字列の前後にある削除文字を取り除いた文字列を返します。 TRIM([LEADING | TRAILING | BOTH] [削除文字] FROM 文字列) または TRIM(文字列) LEADING,TRAILING,BOTHを省略した場合は、文字列の前後の削除文字が取り除かれます。 削除文字には任意の1文字を指定できますが、文字列は指定できません。 設問のSQL文ではTRIM('LED' FROM UPPER(prod_name))で、大文字に変換したPROD_NAME列のデータの前後から'LED'という文字列を削除しようとしていますが、削除文字が1文字ではないのでエラーとなります。 以上より、 ・エラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/functions219.htm#i79689

### 問題ID 26874 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26874?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: PROMOTIONS表とSALES3表の構造を確認して下さい。 プロモーション期間中に売れた製品の情報を表示します。 以下のSQL文の実行結果について正しいものはどれですか。 SELECT p.promo_name, p.promo_begin_date, p.promo_end_date, s.time_id, s.quantity_sold FROM promotions p JOIN sales3 s ON s.time_id BETWEEN p.promo_begin_date AND NVL(p.promo_end_date, SYSDATE);
- 解説要約: 設問のSQL文では、ON句にBETWEEN演算子を使用して非等価結合の条件を指定していますが、これですとTIME_ID列(売れた日)が全プロモーションの期間内に合致する行が全て取り出されてしまい、設問の条件に該当しません。 各プロモーションの期間中に売れた製品の情報のみを取り出すには、PROMOTIONS表とSALES3表のPROMO_ID列を結合列として結合条件に指定し、ANDでBETWEEN演算子を続けて取り出す行の条件を指定する必要があります。 SELECT p.promo_name, p.promo_begin_date, p.promo_end_date, s.time_id, s.quantity_sold FROM promotions p JOIN sales3 s ON p.promo_id = s.promo_id AND s.time_id BETWEEN p.promo_begin_date AND NVL(p.promo_end_date, SYSDATE); NVL関数は、PROMO_END_DATE列が入力されていない現在進行中のプロモーションも正しく条件...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55314
  - https://atmarkit.itmedia.co.jp/ait/articles/1203/22/news164.html

### 問題ID 26875 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26875?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: NEW_PRODUCTS表の構造を確認して下さい。 以下のSQL文の実行結果について正しいものはどれですか。 SELECT prod_name, list_price, CASE WHEN list_price >= (SELECT AVG(list_price) FROM new_products) THEN '高価格' ELSE '低価格' END "価格帯" FROM new_products;
- 解説要約: 設問のSQL文は、副問合せでNEW_PRODUCTS表の平均価格を取り出し全製品の価格と比較して、平均以上の価格は「高価格」、それ以外は「低価格」と表示する分岐処理です。 検索CASE式でも副問合せが使用できます。 以上より、 ・全製品を平均価格と比べて高いか安いかが表示される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT prod_name, list_price, CASE WHEN list_price >= (SELECT AVG(list_price) FROM new_products) THEN '高価格' ELSE '低価格' END "価格帯" FROM new_products; その他の選択肢については以下のとおりです。 ・GROUP BY句がないためエラーとなる グループ関数はネストしていなければGROUP BY句は必要ありません。AVG(list_price)はGROUP BY句なしで実行できます。 ・単一行演算子>=でエラーとなる 単一行演算子>=が比較している副問合せは1件のデータを返す単一行副問合せのため...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/expressions004.htm#SQLRF20037
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/queries007.htm#i2067858

### 問題ID 26876 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26876?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: 次の問合せの実行結果について正しいものはどれですか。 SELECT department_id, AVG(salary) FROM employees GROUP BY department_id HAVING AVG(salary) <ALL (SELECT MAX(salary) / 2 FROM employees GROUP BY department_id);
- 解説要約: 設問のSQL文の副問合せは、部署ごとの最高給与の半分の値を取り出す複数行副問合せです。 <ALLは、左辺の値が右辺のリスト内の最小値よりも小さい場合にTRUEを返す複数行演算子です。 単一行副問合せ、複数行副問合せで使用する演算子はそれぞれ次のとおりです。 以上より、 ・各部署の最高給与の半分の最小値より、部署の平均給与が少ない部署を検索する が正解となります。 その他の選択肢については次のとおりです。 ・副問合せが複数行データを返すため、エラーとなる <ALLは複数行副問合せの条件の判定が行える複数行演算子のため、エラーになりません。 ・各部署の最高給与の半分の最大値より、部署の平均給与が少ない部署を検索する 「副問合せの結果のうち、最大値よりも小さい」という判定は、<ANYで行います。 ・比較演算子を<ANYに置き換えられる <ANYは「副問合せの結果のうち、最大値よりも小さい」という意味なので、<ALLと同義ではありません。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/conditions002.htm#SQLRF52105

### 問題ID 26877 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26877?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: MERGE文の説明として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: MERGE文は異なる表の行をマージできるDML文です。1つのMERGE文で、該当する行があればUPDATE、無ければINSERTというように、行の挿入と更新を同時に行えます。 MERGE文は次のように使用します。 MERGE INTO 表名1 [表別名] USING 表名2 ｜ 副問合せ [表別名] ON ( 結合条件 ) WHEN MATCHED THEN UPDATE SET 列名 = 値 , ... WHEN NOT MATCHED THEN INSERT [ (列名, ... ) ] VALUES ( 値 , ... ); 以上より、 ・行の挿入と更新を同時に行える ・DML文に分類される が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9016.htm#i2081218

### 問題ID 26878 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26878?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: PROD表の構造を確認して下さい。 PRODID列にはPRIMARY KEY制約が定義されています。 PROD表と同じ構造をもつPROD2表を作成し、以下のSQL文を実行しました。 実行結果について正しいものはどれですか。 INSERT INTO prod2 VALUES (1, (SELECT name FROM prod WHERE prodid = 1), (SELECT category FROM prod WHERE prodid = 1), SYSDATE, NULL);
- 解説要約: 1つの列の1行のみ返す副問合せは、INSERT文のVALUES句の中でも使用できます。 設問のSQL文ではNAME列とCATEGORY列にそれぞれ1つの値を返す副問合せを使用しているため、正常に実行できます。 以上より、 ・正常に実行される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 INSERT INTO prod2 VALUES (1, (SELECT name FROM prod WHERE prodid = 1), (SELECT category FROM prod WHERE prodid = 1), SYSDATE, NULL);
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm

### 問題ID 26879 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26879?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: DML文の説明として正しいものはどれですか(該当するものを全て選択して下さい)。
- 解説要約: データ操作言語(DML)文は、スキーマ・オブジェクトのデータにアクセスし変更や削除などの操作を行えますが、オブジェクトの構造は変更しません。 SQL文の種類は次のとおりです。DML文の実行ではトランザクションは終了しません。 ※ Oracleデータベース公式ドキュメントにおいて、SELECT文はDMLに分類されていますが、INSERTやDELETEといった他のDML文とは異なり、データの変更を行うものではありません。 以上より、 ・データを操作する ・INSERT, DELETE文などがある が正解となります。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Types-of-SQL-Statements.html#GUID-2E008D4A-F6FD-4F34-9071-7E10419CA24D

### 問題ID 26880 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26880?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 次のSQL文の実行結果として、正しいものはどれですか(該当するものを全て選択して下さい)。 SELECT department_id, d.department_name, e.employee_name, e.salary FROM departments d JOIN employees e USING (department_id) WHERE e.salary IS NULL FOR UPDATE;
- 解説要約: SELECT文にFOR UPDATE句を指定すると、SELECT文で取り出される行に排他ロックをかけることができます。ロックがかかっていても、他のユーザーは該当の行を検索できますが、更新や削除はできません。他のユーザーが該当の行に更新などのSQL文を発行すると、FOR UPDATE句を使用したユーザーがCOMMIT文やROLLBACK文、またはDDL文やDCL文を発行してトランザクションを終了するまで待機させられます。 また、設問のSQL文のようにFROM句に複数の表が指定されている場合は、それぞれの表の対象となる行にロックをかけます。 以上より、 ・WHERE句の条件を満たす行のみロックされる ・他のユーザーは同じデータを検索できる が正解となります。 設問のSQL文を実行した結果です。 SQLを表示 SELECT department_id, d.department_name, e.employee_name, e.salary FROM departments d JOIN employees e USING (department_id) WHERE e.salary IS ...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10002.htm#SQLRF55370

### 問題ID 26881 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26881?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: EMP7表の構造を確認して下さい。 EMP7表に対して、正しく実行できるALTER TABLE文はどれですか(該当するものを全て選択して下さい)。 ただし、データはまだ入力されていないものとします。
- 解説要約: ALTER TABLE文では、既存の列へ制約を定義できます。 選択肢を1つずつ確認してみましょう。 ・ALTER TABLE emp7 ADD CONSTRAINT pk_empid PRIMARY KEY (employee_id); employee_id列にPRIMARY KEY制約を追加しています。正しいSQL文です。 ・ALTER TABLE emp7 ADD CONSTRAINT fk_dept FOREIGN KEY (department_id); department_id列にFOREIGN KEY制約を追加しようとしていますが、REFERENCES句で参照先の表と列が指定されていないためエラーとなります。誤ったSQL文です。 ・ALTER TABLE emp7 ADD CONSTRAINT nn_sal NOT NULL(salary); NOT NULL制約はALTER TABLE 文のADD CONSTRAINT句では追加できないためエラーとなります。誤ったSQL文です。NOT NULL制約はMODIFY句で追加する必要があります。 ・ALTER TABLE e...
- 参考URL:
  - https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_3001.htm#SQLRF01001
  - https://atmarkit.itmedia.co.jp/fdb/ref/ref_oracle/constraint.html#04
  - https://atmarkit.itmedia.co.jp/fdb/ref/ref_oracle/constraint.html#05

### 問題ID 26882 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26882?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: EMP7表の構造を確認して下さい。 EMP7表に対して以下の順番でSQL文を実行した後の説明として、正しいものはどれですか。 ① INSERT INTO emp7 VALUES (2000, '中山浩二', SYSDATE, NULL, 5); ② ALTER TABLE emp7 MODIFY (salary DEFAULT 200000); ③ INSERT INTO emp7 (employee_id, employee_name, hiredate, department_id) VALUES (2001, '長谷川智子', SYSDATE, 2);
- 解説要約: ALTER TABLE文では、既存の列へデフォルト値を設定できます。 設問の②では、SALARY列のデフォルト値を200000に設定していますが、この変更が反映されるのはALTER TABLE文の後に挿入される行だけです。①で挿入した行のSALARY列はNULL値のまま影響を受けません。ALTER TABLE文の後の③のINSERT文ではSALARY列が省略されているので、デフォルト値の200000が入ります。 以上より、 ・③で挿入された行のSALARY列の値が200000になる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 INSERT INTO emp7 VALUES (2000, '中山浩二', SYSDATE, NULL, 5); ALTER TABLE emp7 MODIFY (salary DEFAULT 200000); INSERT INTO emp7 (employee_id, employee_name, hiredate, department_id) VALUES (2001, '長谷川智子', SYSDATE, 2); S...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_3001.htm#SQLRF01001

### 問題ID 26883 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26883?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: 自分が作成したビュー「TEST_VIEW」を削除するにはどのSQL文を使用しますか。
- 解説要約: ビューの削除は、ビューの所有者またはDROP ANY VIEW権限を持つユーザーによって行われます。DROP VIEW文で削除します。 DROP VIEW ビュー名 以上より、 ・DROP VIEW test_view; が正解となります。
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9009.htm#SQLRF01812

### 問題ID 26884 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26884?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 以下の順番でSQL文を実行した後の説明として、正しいものはどれですか。 ① CREATE OR REPLACE VIEW v_emp AS SELECT department_id, AVG(salary) avg_sal FROM employees GROUP BY department_id; ② CREATE TABLE dep_salary (department_id NUMBER(2), department_name VARCHAR2(14), avarage_salary NUMBER(7)); ③ IN...
- 解説要約: INSERT文に副問合せを使用してデータの挿入を行えます。 INSERT INTO 表名1 [(列名 [, 列名...])] (SELECT 列名 [, 列名...] FROM 表名2 [WHERE 条件]); ※副問合せの部分を囲む()は必須ではありません。 設問の①では、EMPLOYEES表から部署ごとの平均給与を取り出した複合ビューV_EMPを作成しています。 ②では、CREATE TABLE文に記述した構造を持つDEP_SALARY表を作成しています。 ③では、副問合せでV_EMPビューとDEPARTMENTS表を結合して部署ID、部署名、平均給与を取り出し、DEP_SALARY表に挿入しています。 INSERT句の列のリストを省略した場合は、副問合せのSELECT句に指定する列のリストは同数かつ同じ順番で指定する必要がありますが、③の文は問題ありません。 V_EMPではavg_sal列、DEP_SALARY表ではavarage_salary列と、平均給与の列名が違いますが、データ型や桁数は同じのため問題ありません。 以上より、 ・正しく実行できる が正解となります。 設問のS...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_9014.htm

### 問題ID 26885 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26885?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を実行しました。 CREATE TABLE parent ( id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); CREATE TABLE child ( id NUMBER(2) CONSTRAINT cid_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT cname_uq UNIQUE, deptid NUMBER(2) CONSTRAINT dept_fk REFERENCES parent (id) ON DELETE CASCADE ); IN...
- 解説要約: PARENT表はCHILD表のFOREIGN KEY制約(参照整合性制約とも呼ばれます)の親表として参照されています。この場合、参照されている行がない場合でも、子表よりも先に親表を削除できません。DROP TABLE文はエラーとなります。 しかしデータの削除に関しては、FOREIGN KEY制約にON DELETEオプションを指定することによって、親表の行を削除した場合に子表の行をどのようにするかを指定できます。 設問のCHILD表のFOREIGN KEY制約には「ON DELETE CASCADE」が指定されているので、PARENT表の行を削除すると子表の行も削除されます。よって、DELETE文は正常に実行できます。 TRUNCATE TABLE文に関しては、データが存在した場合は、FOREIGN KEY制約の親表を切り捨てることはできません。 以上より、 ・DELETE FROM parent; が正解となります。 その他の選択肢については次のとおりです。 ・DROP TABLE parent; FOREIGN KEY制約で参照されている親表は子表よりも先に削除できません。 ・TR...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/clauses002.htm#SQLRF52199
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_10007.htm#SQLRF01707

### 問題ID 26886 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26886?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: NEW_PRODUCTS表の構造を確認して下さい。 各製品の定価から15%割引した価格に消費税8%をかけて、配送料600円を足した価格を出力するために、次のSQL文を作成しました。 SELECT prod_name, list_price - (list_price * 15/100) + ((list_price - (list_price * 15/100)) * (8/100)) + 600 AS "小計" FROM new_products; このSQL文から()括弧を削除すると、結果はどうなりますか。 ただし、小数点以下の取り扱いについては考慮しないこととします。
- 解説要約: SQL文で使用できる算術演算子は次のとおりです。 また、演算子の優先順位は次のとおりです。 算術式の優先順位を変更したい場合は、()括弧で囲むことで優先順位が高くなります。 設問のSQL文の算術式を確認してみましょう。分かりやすいようにlist_priceに100を割り当てて計算します。 [括弧あり] 100 - (100 * 15/100) + ((100 - (100 * 15/100)) * (8/100)) + 600 = 691.8 [括弧無し] 100 - 100 * 15/100 + 100 - 100 * 15/100 * 8/100 + 600 = 783.8 演算子の優先順位に従って計算すると、括弧無しの方が価格が高い結果となりました。 以上より、 ・最初のSQL文と比べて価格が高くなる が正解となります。 実行結果は次のようになります。 SQLを表示 SELECT prod_name, list_price - (list_price * 15/100) + ((list_price - (list_price * 15/100)) * (8/100)) + 60...
- 参考URL:
  - http://docs.oracle.com/cd/E16338_01/server.112/b56299/operators002.htm#SQLRF51156

### 問題ID 26887 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26887?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: EMPLOYEES表のデータを確認して下さい。 以下のSQL文を実行すると、どのような結果になりますか。 SELECT employee_id, employee_name, salary FROM employees ORDER BY salary FETCH FIRST 5 ROW WITH TIES;
- 解説要約: Oracle 12cより、SELECT文の問合せ結果として返される行数を制限できる機能、row_limiting_clause(行制限の条件)が加わりました。これにより、例えば上位10番目から20番目のデータを簡単に取り出せます。 row_limiting_clauseのFETCH句は返される行数、または行の割合を指定して、SELECT文の結果として返される行数を制限します。 FETCH { FIRST | NEXT } { 返される行数 | 返される行の割合 PERCENT } { ROW | ROWS } { ONLY | WITH TIES } 設問のSQL文では、ORDER BY句で給与の低い順にソートした後に「FETCH FIRST 5 ROW」で5行返されるように指定しています。ですが、WITH TIESキーワードも指定しているため、最後にフェッチ(取得)された行と同じソートキー(ORDER BY句に指定した列)の値を持つ全ての行も返されます。EMPLOYEES表のデータを見ると、給与の低い順にソートした結果の5行目と6行目の従業員が同じ給与であるため、6行目までが返されま...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_10002.htm#BABHFGAA

### 問題ID 26888 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26888?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: NEW_PRODUCTS表の構造を確認して下さい。 価格の安い順に4番目から8番目の製品を表示します。 どの問合せを使用しますか。 但し、8番目の製品と同じ価格の製品があった場合は、その製品も表示するものとします。
- 解説要約: SELECT文の結果として返される行数を制限するには、row_limiting_clause(行制限の条件)を指定します。row_limiting_clauseには、OFFSET句とFETCH句があります。 4番目から8番目の製品を取り出すには、OFFSET句で3行をスキップし、FETCH句で5行を返すように指定します。FETCH句のFIRST, NEXTキーワードに区別はなく、どちらを使用しても構いません。 また、最後にフェッチ(取得)された行と同じ価格の製品を表示するには、ORDER BY句で価格の安い順にソートし、WITH TIESキーワードを指定します。 以上より、 ・SELECT prod_name, list_price FROM new_products ORDER BY list_price OFFSET 3 ROWS FETCH NEXT 5 ROWS WITH TIES; が正解となります。 正解のSQL文の実行結果は次のとおりです。 8番目の製品の「油性マジック」と同じ価格の製品は他に2つあるので、これらも結果に含まれ、全部で7行が返されます。 SQLを表示 SE...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_10002.htm#BABHFGAA

### 問題ID 26889 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26889?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: row_limiting_clauseの説明として正しい記述はどれですか。
- 解説要約: Oracle 12cより、SELECT文の問合せ結果として返される行数を制限できる機能、row_limiting_clause(行制限の条件)が加わりました。これにより、例えば上位10番目から20番目のデータを簡単に取り出せます。 row_limiting_clauseにはOFFSET句とFETCH句があり、SELECT文で次のように指定します。 SELECT 列名[, 列名 ...] FROM 表名 [WHERE 条件] [ORDER BY 列名[, 列名 ...]] [OFFSET ...] [FETCH ...] ORDER BY句は省略できますが、省略した場合はどのような順番で問合せ結果が返されるか保証されません。そのため、「SALARY列の値の大きい順に上位N件を表示する」など、ソートした順番でデータを取り出したい場合は、ORDER BY句を指定する必要があります。 ORDER BY句を指定する場合は、ORDER BY句の後にrow_limiting_clauseを記述します。 OFFSET句にはスキップする行数を、FETCH句には返される行数、または行の割合を指定します。両...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_10002.htm#BABHFGAA

### 問題ID 26890 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26890?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 次のSQL文の実行結果として正しい記述はどれですか。 ただし、データベースの実行環境は英語環境とし、日付の表示書式はデフォルトとします。 SELECT TO_CHAR(NEXT_DAY(LAST_DAY(SYSDATE), 'FRI'), 'FMDD "is the first" Day "for" Month YYYY') "Result" FROM dual;
- 解説要約: 主な日付関数は次のとおりです。 設問のSQL文のLAST_DAY(SYSDATE)は、今月の最終日を返します。 NEXT_DAY(LAST_DAY(SYSDATE), 'FRI')は、今月の最終日の翌日以降の最初の金曜日、すなわち来月の最初の金曜日の日付を返します。 最後に、上記の結果をTO_CHAR関数で指定した書式で、"Result"という別名で表示しています。 以上より、 ・来月の最初の金曜日の日付を表示する が正解となります。 正解のSQL文の実行結果は次のようになります(実行日は2015年の1月です)。 ※日本語環境の場合は、事前に以下のSQL文を実行してセッションを英語環境に変更して下さい。 ALTER SESSION SET NLS_DATE_LANGUAGE = 'AMERICAN'; ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MON-RR'; SQLを表示 SELECT TO_CHAR(NEXT_DAY(LAST_DAY(SYSDATE), 'FRI'), 'FMDD "is the first" Day "for" Month ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions095.htm#i83733
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions117.htm#i78154
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions215.htm#i1009324

### 問題ID 26891 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26891?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次の2つのSQL文の結果として正しいものはどれですか。 1) SELECT employee_name, NVL(salary, salary + 10000) FROM employees; 2) SELECT employee_name, NVL2(salary, salary + 10000, '') FROM employees;
- 解説要約: NVL(salary, salary + 10000)は、SALARY列の値がNULL値の場合は「salary + 10000」を返し(但し、NULL値の算術演算の結果もNULLです)、NULL値以外の場合はそのままSALARY列の値を返します。 NVL2(salary, salary + 10000, '')は、SALARY列の値がNULL値以外の場合は「salary + 10000」を返し、NULL値の場合は''を返します。 以上より、 ・1),2)は正常に実行できるが、異なる結果が出力される が正解となります。 1)のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_name, NVL(salary, salary + 10000) FROM employees; 2)のSQL文の実行結果は次のようになります。 SQLを表示 SELECT employee_name, NVL2(salary, salary + 10000, '') FROM employees;
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL.html#GUID-3AB61E54-9201-4D6A-B48A-79F4C4A034B2
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NVL2.html#GUID-414D6E81-9627-4163-8AC2-BD24E57742AE

### 問題ID 26892 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26892?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: DEPARTMENT_IDが1の従業員名を、EMPLOYEE_IDの順番で一行で出力します。 どのSQL文を使用しますか。
- 解説要約: Oracle Database 11gリリース2から使用可能なLISTAGG関数は、複数行の列の値を連結して1行で表示できる関数です。 LISTAGG(連結して表示する列名 [, 'デリミタ']) WITHIN GROUP(ORDER BY ソートする項目 [ASC | DESC]) 区切り記号のデリミタは省略可能です。省略すると列の値は区切り記号なしに連結して表示されます。 WITHIN GROUP(ORDER BY～)キーワードは省略できず、必ずこの書式で記述しなければなりません。 以上より、 ・SELECT LISTAGG(employee_name, '|') WITHIN GROUP (ORDER BY employee_id) "従業員" FROM employees WHERE department_id = 1; が正解となります。 正解のSQL文の実行結果は次のようになります。 SQLを表示 SELECT LISTAGG(employee_name, '|') WITHIN GROUP (ORDER BY employee_id) "従業員" FROM employe...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions101.htm

### 問題ID 26893 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26893?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: Oracle Databaseで使用できるグループ関数とその説明として、正しい組合せはどれですか(3つ選択して下さい)。
- 解説要約: Oracle Databaseで使用できる主なグループ関数は次のとおりです。 以上より、 ・STDDEV：標準偏差を返す ・VARIANCE：分散を返す ・AVG：平均値を返す が正解となります。 その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions003.htm#i89203

### 問題ID 26894 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26894?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: SALES3表とPROMOTIONS表の構造を確認して下さい。 売上のあった全ての製品について、プロモーション名を表示します。 売れたのがプロモーション期間中でなかった(PROMO_ID列がNULL値である)製品は、代りにプロモーション名(PROMO_NAME列)で「No Promotion」を出力します。 どのSQL文を使用しますか。
- 解説要約: SALES3表のPROMO_ID列と、PROMOTIONS表のPROMO_ID列を結合列として2つの表を結合します。 売れたのがプロモーション期間中でなかった(PROMO_ID列がNULL値である)製品も出力するということですので、SALES3表の結合条件を満たしていないデータも取り出すために外部結合を行います。全ての選択肢において、SALES3表はJOIN句の左側にありますので、LEFT OUTER JOINを使用します。 また、PROMO_ID列がNULL値であるデータはプロモーション名(PROMO_NAME列)もNULL値ということになりますが、設問の条件を満たすためにPROMO_NAME列のNULL値をNVL関数で「No Promotion」に変換します。 以上より、 ・SELECT s.prod_id, NVL(p.promo_name, 'No Promotion') promotion FROM sales3 s LEFT OUTER JOIN promotions p ON (s.promo_id = p.promo_id); が正解となります。 正解のSQL文の実行結...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries006.htm#i2054062

### 問題ID 26895 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26895?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文の実行結果として正しい記述はどれですか。 SELECT department_id, employee_name, DECODE(salary, 200000, DECODE(department_id, 1, salary * .15, '0'), '0') "昇給" FROM employees;
- 解説要約: DECODE関数は、第1引数に指定された式の値と、第2引数以降に指定された条件を順に判定し、値が合致した条件に対応する戻り値を返します。 DECODE(式, 条件1, 戻り値1 [, 条件2, 戻り値2 …] [, デフォルトの戻り値]) 設問のSQL文では、SALARY列の値が200000の場合、入れ子になったDECODE関数を判定しDEPARTMENT_ID列が1であればSALARYの0.15倍を"昇給"として出力、それ以外では0を返します。 0は一重引用符(')で囲んで文字列として指定していますが、DECODE関数の最初の戻り値(入れ子になったDECODE関数のsalary * .15)の数値型に暗黙的なデータ変換が行われます。 以上より、 ・給与が200000、部署が1の従業員の給与の0.15倍が出力される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, employee_name, DECODE(salary, 200000, DECODE(department_id, 1, salary * .1...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions056.htm#i1017437

### 問題ID 26896 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26896?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 以下のSQL文を実行した結果について、正しい記述はどれですか。 SELECT department_id, maxincome, minincome FROM (SELECT department_id, MAX(commission + (salary * 12)) maxincome, MIN(commission + (salary * 12)) minincome FROM employees GROUP BY department_id) WHERE minincome > maxincome / 2 ORDER BY departmen...
- 解説要約: SQL文は以下の順序で評価されるため、通常は列別名だけを指定できるのはORDER BY句のみです(SELECT句で指定した列別名を認識できるのはORDER BY句のみのため)。 （評価順） FROM句→WHERE句→GROUP BY句→HAVING句→SELECT句→ORDER BY句 ですが、設問のSQL文ではFROM句の副問合せ(インライン・ビュー)で算術式に列別名を指定しているため、FROM句の後に評価される全ての句で列別名が認識されます。 FROM句の副問合せでは、部署ごとの年収(commission + (salary * 12))の最高額と最低額にそれぞれmaxincome、minincomeと列別名を指定し、その後のWHERE句→SELECT句でも簡潔な列別名で問合せが実行されます。GROUP BY句やHAVING句が含まれていたとしても、同様に列別名は認識されます。 FROM句で部署ごとの最高年収、最低年収を取り出し、WHERE句で最高年収の半分より多い最低年収という条件に絞っています。 以上より、 ・部署の最低年収が最高年収の半分より多い部署の情報が表示される が正解...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries007.htm#i2067858

### 問題ID 26897 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26897?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: EMPLOYEES表から、部下のいない従業員の名前を表示します。 各従業員のMANAGER_ID列に上司のEMPLOYEE_IDが登録されていますが、上司がいない従業員も存在します。 次の2つのSQL文の実行結果として正しいものはどれですか。 1) SELECT m.employee_name FROM employees m WHERE NOT EXISTS (SELECT e.employee_id FROM employees e WHERE e.manager_id = m.employee_id); 2) SELECT employee_name FROM employees WHE...
- 解説要約: 1)のSQL文のNOT EXISTS演算子は、主問合せで取り出した1行が副問合せの条件を満たしていない場合、つまり副問合せの結果が1行も返されない場合にTRUEとして評価され、主問合せの結果が返されます。主問合せのm表で取り出したデータが副問合せの「e.manager_id = m.employee_id」という条件を満たしていない場合、部下のいない従業員として主問合せは結果を返します。正しいSQL文です。 2)のSQL文のNOT IN演算子はリスト内の全ての値と等しくない場合にTRUEを返しますが、副問合せの結果にNULL値が含まれていると全ての値と等しくないという判定がされません。副問合せのMANAGER_ID列にNULL値が含まれているため、エラーとはなりませんが主問合せは1行もデータを返しません。 以上より、 ・どちらも正常に実行されるが、異なる結果となる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT m.employee_name FROM employees m WHERE NOT EXISTS (SELECT e.empl...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/conditions013.htm#i1051145

### 問題ID 26898 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26898?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: DEPARTMENTS表とEMPLOYEES表の構造を確認して下さい。 エラーが無く実行されるSQL文はどれですか(3つ選択して下さい)。
- 解説要約: 集合演算子を用いて複合問合せを行うには、いくつかのガイドラインがあります。 [SELECT句の指定] ・複合問合せの列見出しは1つ目の問合せに指定された列名が使用される(それぞれの問合せで指定される列名が異なっていても良い) ・2つの問合せでSELECT句に指定する列や式の数を同数にしなければならない ・2つの問合せでSELECT句に指定する列や式のデータ型を同じ、もしくは同じデータ型グループにしなければならない(ただし、データサイズは異なっていても良い) ※同じデータ型グループとは、CHAR型とVARCHAR2型のように文字同士など同じ種類のデータ型のことです。 選択肢を1つずつ確認してみましょう。 ・SELECT employee_id FROM employees UNION SELECT department_id FROM departments; EMPLOYEE_IDとDEPARTMENT_IDは同じデータ型なので正常に実行され、両方の問合せの全ての行が表示されます。正しいSQL文です。 ・SELECT department_id FROM departments UNI...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/operators005.htm#i1035612
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries004.htm#i2054381

### 問題ID 26899 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26899?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: 部署が「営業」で、10年以内に入社した給与が30万円以上の従業員を出力します。 どの問合せを使用しますか。
- 解説要約: 集合演算子を用いて複合問合せを行うには、いくつかのガイドラインがあります。 [集合演算子の優先順位] ・集合演算子には優先順位はない ・1つのSQL文に複数の集合演算子が使用されている場合は、SQL文の先頭から順番に複合問合せが実行される ・優先順位を明示的に指定したい場合は、()括弧を用いて優先順位を指定する 各条件を以下のように定義して、選択肢を1つずつ確認してみましょう(SQL文の実行日は2015年の1月です)。 条件1 : 部署が「営業」 条件2 : 10年以内に入社 条件3 : 給与が30万円以上 ・SELECT department_id, employee_name, hiredate, salary FROM employees WHERE department_id = (SELECT department_id FROM departments WHERE department_name = '営業') UNION SELECT department_id, employee_name, hiredate, salary FROM employees WHERE h...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/operators005.htm#i1035612
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/queries004.htm#i2054381

### 問題ID 26900 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26900?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 部署3に属する従業員の月給(SALARY)と歩合給(COMMISSION)を、上司(MANAGER_ID)と同じ金額に更新します。 但し、MANAGER_ID列がNULLである部署3の上司についてはデータを更新しない事とします。 次のSQL文の実行結果について、正しい記述はどれですか。 UPDATE employees e SET (e.salary, e.commission) = (SELECT m.salary, m.commission FROM employees m WHERE m.employee_id = e.manager_id) WHERE e.department_id ...
- 解説要約: 設問のSQL文では、主問合せの各行に対してその都度、副問合せが実行される「相関副問合せ」が使用されています。副問合せの中でそのFROM句に無い表を参照する場合(副問合せの外側にある表を参照する場合)に、相関副問合せとして処理されます。 EMPLOYEES表 e から取り出した各従業員のSALARY列とCOMMISSION列を、副問合せで取り出した、その従業員の上司と同じ金額に更新します。 副問合せは複数の列を返す「複数列副問合せ」を使用しています。 WHERE句には設問の条件である「e.department_id = 3」と、MANAGER_ID列がNULL値の上司のデータを除くために「e.manager_id IS NOT NULL」を指定しています。 正しいSQL文です。 以上より、 ・正常に実行でき、目的の結果が得られる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT department_id, employee_name, salary, commission FROM employees WHERE department_id...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_10008.htm#i2067715
  - https://atmarkit.itmedia.co.jp/ait/articles/1212/03/news009.html

### 問題ID 26901 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26901?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次の要件を満たす表を作成するには、どのSQL文を実行しますか(2つ選択して下さい)。 ・USER_IDはサイズ8の数値型で、NULL値を入力できない ・LOGIN_PWDは文字型で、NULL値を入力できない ・USER_ID, LOGIN_PWDの組み合せは一意でないといけない ・REGISTRATION_DATEは日付型で、デフォルト値は当日の日付 ・AGEはサイズ3の数値型で、デフォルト値は20 ・EMAILは文字型で、デフォルト値は「no@email.com」
- 解説要約: 選択肢を1つずつ確認してみましょう。 ・CREATE TABLE tmp ( user_id NUMBER(8) CONSTRAINT user_nn NOT NULL, login_pwd VARCHAR2(20) CONSTRAINT login_nn NOT NULL, registration_date DATE DEFAULT = SYSDATE, age NUMBER(3) DEFAULT = 20, email VARCHAR2(40) DEFAULT = 'no@email.com', CONSTRAINT user_log_uk UNIQUE (user_id, login_pwd)); 列のデフォルト値は「列名 データ型 DEFAULT 値」の書式で記述します。等号=は不要なのでエラーとなり、誤ったSQL文です。 ・CREATE TABLE tmp ( user_id NUMBER(8) CONSTRAINT user_nn NOT NULL, login_pwd VARCHAR2(20) CONSTRAINT login_nn NOT NULL, registra...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_7002.htm#i2095331
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/clauses002.htm#g1053592
  - https://docs.oracle.com/cd/E57425_01/121/CNCPT/datainte.htm#i6686

### 問題ID 26902 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26902?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: PROD3表の構造を確認して下さい。 PROD3表には6件のデータが登録されています。 新たにSTATUS列を追加する以下のSQL文を実行しました。結果について正しい記述はどれですか。 ALTER TABLE prod3 ADD status VARCHAR2(20) DEFAULT 'FOR SALE' NOT NULL;
- 解説要約: ALTER TABLE文で、既存の表へ新しい列を追加できます。 ALTER TABLE 表名 ADD ( 列名 データ型(サイズ) [DEFAULT 値] [[CONSTRAINT 制約名] 制約タイプ] [, 列名 データ型(サイズ)] ... ); 表に既存のデータが存在する場合、新しく追加された列にはデフォルトでNULL値が設定されます。表が空でない場合、NOT NULL制約を定義した列を追加しようとするとエラーとなりますが、列の追加時にNULL以外のデフォルト値を指定することで、既存のデータの列にもデフォルト値が設定されます。 設問のSQL文では、追加するSTATUS列にNOT NULL制約とデフォルト値「FOR SALE」を指定しているため、正常に表の最後に列が追加され、既存の行のSTATUS列にデフォルト値が設定されます。 以上より、 ・表の最後に列が追加され、既存の行のSTATUS列にデフォルト値が設定される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 ALTER TABLE prod3 ADD status VARCHAR2(20)...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#CJAHHIBI
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#i2198241

### 問題ID 26903 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26903?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を実行しました。 CREATE TABLE parent ( id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); CREATE TABLE child ( id NUMBER(2) CONSTRAINT cid_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT cname_uq UNIQUE, deptid NUMBER(2) CONSTRAINT dept_fk REFERENCES parent (id) ON DELETE CASCADE ); IN...
- 解説要約: ALTER TABLE文で、既存の表の列の削除を行えます。 ALTER TABLE 表名 DROP ( 列名 [, 列名...]) [CASCADE CONSTRAINTS]; ※1つの列のみ削除する場合は、次の構文も使用できます。 ALTER TABLE 表名 DROP COLUMN 列名 [CASCADE CONSTRAINTS]; 列の削除に関しては、以下の注意事項があります。 ・削除した列は戻せない ・表には最低1つの列を残す必要がある ・他から参照されるFOREIGN KEY制約の親表の列はCASCADE CONSTRAINTSオプションを指定する必要がある ・パーティション化キー列（表をパーティション化するためのキー列）は削除できない ・列に多くのデータが含まれている場合は、削除に時間がかかる 設問のSQL文では、CHILD表のDEPTID列に、PARENT表のID列を参照するFOREIGN KEY制約を定義しています。その際、ON DELETEオプションを指定していますが、親表の行を削除した場合の動作なので、親表の列の削除には関係ありません。PARENT表のID列を削除す...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#CJAHHIBI
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#i2103683

### 問題ID 26904 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26904?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: ALTER TABLE文での列の削除について、正しい記述はどれですか(3つ選択して下さい)。
- 解説要約: ALTER TABLE文で、既存の表の列の削除を行えます。 ALTER TABLE 表名 DROP ( 列名 [, 列名...]) [CASCADE CONSTRAINTS]; ※1つの列のみ削除する場合は、次の構文も使用できます。 ALTER TABLE 表名 DROP COLUMN 列名 [CASCADE CONSTRAINTS]; 列の削除に関しては、以下の注意事項があります。 ・削除した列は戻せない ・表には最低1つの列を残す必要がある ・他から参照されるFOREIGN KEY制約の親表の列はCASCADE CONSTRAINTSオプションを指定する必要がある ・パーティション化キー列（表をパーティション化するためのキー列）は削除できない ・列に多くのデータが含まれている場合は、削除に時間がかかる 以上より、 ・複数の列を同時に削除できる ・削除した列は戻せない ・参照整合性制約の親キー列はCASCADEオプションを指定する が正解となります。 その他の選択肢については次のとおりです。 ・表の全ての列を削除できる 表には最低1つの列を残す必要があります。 ・データが含まれている...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#CJAHHIBI
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#i2103683

### 問題ID 26905 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26905?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: ALTER TABLE文のSET UNUSED句について、正しい記述はどれですか(3つ選択して下さい)。
- 解説要約: ALTER TABLE文で既存の表の列を削除できますが、列の削除中は表にロックがかかり、列に多くのデータが含まれている場合は削除に時間がかかります。多くのユーザーがデータベースを利用する時間帯に負荷の高い削除処理を行いたくない場合、削除したい列にUNUSEDマークを設定して未使用にできます。 ALTER TABLE 表名 SET UNUSED ( 列名 [, 列名...]) [CASCADE CONSTRAINTS]; ※1つの列のみUNUSEDにする場合は、次の構文も使用できます。 ALTER TABLE 表名 SET UNUSED COLUMN 列名 [CASCADE CONSTRAINTS]; UNUSEDに設定した列は、次のALTER TABLE文で削除します。データベースの負荷の低い時間帯に行えます。 ALTER TABLE 表名 DROP UNUSED COLUMNS; SET UNUSED句に関しては、以下の注意事項があります。 ・UNUSEDに設定した列は戻せず、DESCRIBEコマンドなどで列名やデータ型を確認できなくなる ・UNUSEDにした列に作成された索引や制約...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#CJAHHIBI
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#i2103683

### 問題ID 26906 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26906?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: PROD3表の構造とデータを確認して下さい。 STATUS列に対して正常に実行できる変更はどれですか。
- 解説要約: ALTER TABLE文で、既存の列のデータ型、サイズ、デフォルト値を変更できます。 ALTER TABLE 表名 MODIFY ( 列名 [データ型(サイズ)] [DEFAULT 値] [, 列名 ...]); 列の変更に関しては、以下のガイドラインがあります。 ・列にNULL値のみが格納されている場合、データ型を変更できる ・列にデータが含まれている場合、列の変更後も格納できるデータ型やサイズであれば変更できる [OK例] CHAR(10) → VARCHAR2(20), VARCHAR2(20)に10バイト以下の文字が格納されている → CHAR(10) [NG例] CHAR(20)に10バイト以下の文字が格納されている → VARCHAR2(10) ※CHAR型は固定長のため「10バイト以下の文字 + 空白 = 20バイト」で格納される ・デフォルト値の変更は、新しい行の挿入時に反映される PROD3表のSTATUS列はVARCHAR2(20)ですが、可変長なので実際のサイズは格納されている「FOR SALE」分の8バイトです。8バイト以上のサイズであればVARCHAR2型とC...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#CJAHHIBI
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#i2181663

### 問題ID 26907 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26907?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 現在は西暦は2015年です。 次のSQL文を実行すると、結果はどうなりますか。 ただし、日付書式は"RR-MM-DD"とします。 SELECT TO_CHAR(TO_DATE('2099/12/31', 'RR-MM-DD'), 'YYYY-MM-DD') FROM dual;
- 解説要約: TO_DATE関数は、文字列を指定された書式に従って日付値に変換する関数です。 TO_DATE(文字列 [, '日付書式'] [, NLSパラメータ]) 設問のSQL文のように文字列と日付書式のフォーマットが一致しない場合、Oracle Databaseは別の書式要素の適用を試行します。 設問では、'RR-MM-DD'書式に対して、'2099/12/31'と異なるフォーマットの文字列が指定されていますが、Oracle Databaseは'RR'要素を'RRRR'要素に置き換えて試行するため、「2099/12/31」として扱われます。'RRRR'要素は明示的に4桁の数値が指定された場合、'YYYY'要素と同様にそのまま4桁の年号として扱われます。 また、「-」,「/」,「.」,「:」などの英数字以外の半角記号は、設問のように異なる記号を指定しても、内部的に区切り記号として一致させることができるのでエラーとなりません。 TO_DATE関数だけでは指定した日付書式"RR-MM-DD"で出力されますので、最後にTO_CHAR関数で"YYYY-MM-DD"という書式の文字列に変換して、4桁の西暦...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions218.htm#i1003589
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/functions215.htm#i1009324
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/sql_elements004.htm#i34924

### 問題ID 26908 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26908?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を実行しました。 CREATE TABLE parent ( id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); CREATE TABLE child ( id NUMBER(2) CONSTRAINT cid_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT cname_uq UNIQUE, deptid NUMBER(2) CONSTRAINT dept_fk REFERENCES parent (id) ); INSERT INTO parent V...
- 解説要約: 設問のPARENT表のID列は、CHILD表のDEPTID列からFOREIGN KEY制約(参照整合性制約とも呼ばれます)の親キーとして参照されています。参照する側のデータ、子レコードが存在する場合、親レコードを削除しようとすると設問のエラーが発生します。 先に子レコードを削除するか、FOREIGN KEY制約を無効にすることで、親レコードを削除できるようになります。 もしくは、CHILD表のFOREIGN KEY制約にON DELETEオプションを指定して再作成し、親レコード削除時の処理を設定します。 ALTER TABLE文で既存の表の制約を無効化、もしくは有効化できます。 ALTER TABLE 表名 DISABLE CONSTRAINT 制約名 [CASCADE]; ALTER TABLE 表名 ENABLE CONSTRAINT 制約名 [CASCADE]; 以上より、 ・ALTER TABLE child DISABLE CONSTRAINT dept_fk; ・DELETE FROM child WHERE deptid = 1; が正解となります。 正解のSQL文の実行...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#CJAHHIBI
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#i2056917

### 問題ID 26909 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26909?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 次のSQL文の実行結果として正しいものはどれですか。 SELECT hiredate || employee_name "date" FROM employees ORDER BY date;
- 解説要約: 「date」はOracleの予約語ですので表名や列名に使用できませんが、二重引用符(")で囲む事で列別名として使用できます。但し、列別名を二重引用符(")で囲んだ場合は、ORDER BY句でも同様に列別名を二重引用符(")で囲む必要があります。 設問のSQL文では「ORDER BY date」のように、dateを二重引用符(")で囲んでいないのでエラーとなります。 以上より、 ・ORDER BY句でエラーとなる が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 SELECT hiredate || employee_name "date" FROM employees ORDER BY date; SELECT hiredate || employee_name "date" FROM employees ORDER BY "date"; その他の選択肢については次のとおりです。 ・「date」はOracleの予約語のため、列別名として使用できない 「date」はOracleの予約語ですが、二重引用符(")で囲む事で列別名として使用できます。 ・日付型と...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_10002.htm#SQLRF55280
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/sql_elements008.htm#i27570
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/ap_keywd001.htm#BABCJAEB

### 問題ID 26910 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26910?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 次のSQL文のうち、正常に実行されるものはどれですか(3つ選択して下さい)。 ただし、データベースの実行環境は日本語環境とします。
- 解説要約: SQL文の実行結果に表示される列見出しには、列別名を指定できます。 列別名はオブジェクトのネーミング規則に従い命名しなければなりませんが、列別名を二重引用符(") で囲むことで、大文字と小文字を区別したり、スペースを含めるなどネーミング規則に反する列別名を使用できます。列別名の指定時に、ネーミング規則に反する列別名を使用するために二重引用符(")で囲んだ場合は、ORDER BY句でも同様に列別名を二重引用符(")で囲む必要があります。 選択肢を1つずつ確認してみましょう。 ・SELECT employee_name "社員名" FROM employees ORDER BY 社員名; 日本語環境では列別名に漢字、ひらがな、カタカナも使用できます。「社員名」という列別名を二重引用符(")で囲む必要はないため、ORDER BY句では列別名を二重引用符(")で囲んでいなくても正常に実行できます。正しいSQL文です。 SQLを表示 SELECT employee_name "社員名" FROM employees ORDER BY 社員名; ・SELECT employee_name AS "...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/SELECT.html#SQLRF55280
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Database-Object-Names-and-Qualifiers.html#SQLRF-GUID-75337742-67FD-4EC0-985F-741C93D918DA

### 問題ID 26911 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26911?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: リレーショナル・データベース(RDB)モデルに関して、正しい記述はどれですか(3つ選択して下さい)。
- 解説要約: Oracle Databaseはリレーショナル型データベースを管理するためのソフトウェアです。 リレーショナル・データベース管理システム(RDBMS)と呼ばれます。 リレーショナル・データベース(RDB)には次のような特徴があります。 ・データを行と列からなる2次元の表形式で格納する ・関連のあるデータをグループ化し、複数の表に分割して管理する ・関連のある表同士を表に格納されたデータに基づいて関連付けることができる ・SQLを使用してデータにアクセスする 以上より、 ・データを行と列からなる2次元の表形式で格納する ・複数の表をデータで関連付けることができる ・SQLを使用してデータにアクセスする が正解となります。 その他の選択肢については次のとおりです。 ・データをツリー構造で階層型に格納する 階層型データベースの説明です。
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/CNCPT/intro.htm#i57253

### 問題ID 26913 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26913?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: 以下の関係と例の組合せとして、正しいものはどれですか。 1) 1対1 2) 1対多 3) 多対1 4) 多対多 a) 上司と部下 b) 顧客と商品 c) 学生と担任教師 d) 個人と基礎年金番号
- 解説要約: 関係と例の正しい組合せは次のようになります。 1) 1対1 - d) 個人と基礎年金番号 : 1人に対して、基礎年金番号は1つです。 2) 1対多 - a) 上司と部下 : 通常、1人の上司が複数名の部下を持ちます。 3) 多対1 - c) 学生と担任教師 : クラスの複数名の学生に対して、担任教師は1人です。 4) 多対多 - b) 顧客と商品 : さまざまな顧客とさまざまな商品が存在します。 以上より、 ・2) と a) が正解となります。 その他の選択肢については上記の解説をご確認ください。
- 参考URL: なし

### 問題ID 26914 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26914?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のSQL文の実行結果として正しいものはどれですか。 ただし、日付書式は"RR-MM-DD"とします。 DEFINE date = '10-04-01' SELECT department_id, employee_name, hiredate FROM employees WHERE hiredate > '&date' AND department_id = &id;
- 解説要約: SQL*PlusやSQL Developerなどのツールでは、置換変数を利用できます。 置換変数を利用すると、WHERE句の条件などに指定する値を、SQL文の中に直接記述するのではなく、実行時に値を指定できるようになります。 DEFINEコマンドもSQL*Plusのコマンドで、ユーザー定義の変数に値を割り当てたり、変数の値を確認できます。 DEFINE 変数名 [ = 値 ] : 変数に設定されている値を表示[変数に値を設定] UNDEFINE 変数名 : 変数に設定されている値を破棄 設問のSQL文では、最初にDEFINEコマンドでdate変数に日付の文字列を割り当てています。そのため、SELECT文の実行時はdate変数の方は値の入力を促されません。また、通常「&置換変数」はSQL文実行後に変数の値が破棄されますが、DEFINEで定義したdate変数は、セッションを切断もしくはUNDEFINEコマンドで破棄するまで値が保持されます。 以上より、 ・「id」のみ入力を促される が正解となります。 設問のSQL文の実行結果は次のようになります。 SQLを表示 DEFINE date =...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQPUG/GUID-68AC9FF2-B92A-48D1-9699-133D47F8DDC1.htm#GUID-68AC9FF2-B92A-48D1-9699-133D47F8DDC1
  - https://docs.oracle.com/cd/E57425_01/121/SQPUG/GUID-72D4998C-EC2C-4FA6-9F7F-A305C407D666.htm

### 問題ID 26918 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26918?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: ER図(ERD: Entity Relationship Diagram)の説明として正しい記述はどれですか。
- 解説要約: ERモデル(Entity-Relationship Model)は、管理対象を「エンティティ(実体)」、「アトリビュート(属性)」、「リレーションシップ(関連)」という3つの構成要素で表現した概念データモデルです。 ER図(ERD: Entity Relationship Diagram)はERモデルを図にしたものです。 ER図にはいくつかの表記法がありますが、ここではデータベースの設計に特化したIDEF1X記法の例を示します。 ER図ではエンティティ間の関係を「リレーションシップ」という線で結びます。 リレーションシップの詳細は「カーディナリティ（多重度）」という要素で、片方のエンティティの1レコードに対してもう片方のエンティティのレコード数がいくつになるかを表現します。カーディナリティには「0以上」「1以上」などがあり、「1対1」「1対多」「多対多」のような関係を表すことができます。 以上より、 ・カーディナリティで「1対1」「1対多」「多対多」のような関係を表すことができる が正解です。 その他の選択肢については以下のとおりです。 ・リレーションシップ間の関係をエンティティという...
- 参考URL:
  - https://atmarkit.itmedia.co.jp/ait/articles/1703/01/news178.html
  - https://e-words.jp/w/ER%E5%9B%B3.html

### 問題ID 26920 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26920?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: トランザクションのACID特性のうち、Atomicityの説明として正しい記述はどれですか。
- 解説要約: 複数のSQLによるデータベースへの一連の操作のまとまりを「トランザクション」と呼び、トランザクションごとに処理を確定(コミット)または取消し(ロールバック)できます。 データベース管理システムがトランザクションを適切にデータベースに反映できるように、トランザクションにはACID特性と呼ばれる性質があります。 上表より正解は ・トランザクションは完全に実行されるか、全く実行されないかのどちらかとなる です。 例えば、ユーザAの銀行口座からユーザBの口座に送金する場合、以下の処理が行われます。 1. ユーザAの口座から3万円を引く 2. ユーザBの口座に3万円を足す 1、2のうちどちらかの処理しか実行されなければ預金残高の整合性が取れなくなります。そのため、これら2つの処理は1つのトランザクションとして完全に実行されるか、全く実行されないかのどちらかでなければなりません。この性質がAtomicity（原子性）です。 その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://atmarkit.itmedia.co.jp/ait/articles/1703/01/news194.html
  - https://ja.wikipedia.org/wiki/ACID_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E7%A7%91%E5%AD%A6)#%E4%B8%8D%E5%8F%AF%E5%88%86%E6%80%A7(Atomicity)
  - https://docs.oracle.com/cd/F19136_01/cncpt/transactions.html#GUID-31319EA7-994C-4D25-8814-0214ABD3CBDA

### 問題ID 26921 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26921?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: トランザクションのACID特性のうち、Consistencyの説明として正しい記述はどれですか。
- 解説要約: 複数のSQLによるデータベースへの一連の操作のまとまりを「トランザクション」と呼び、トランザクションごとに処理を確定(コミット)または取消し(ロールバック)できます。 データベース管理システムがトランザクションを適切にデータベースに反映できるように、トランザクションにはACID特性と呼ばれる性質があります。 上表より正解は ・トランザクションの実行前後でデータベースの整合性が保たれる です。 例えば、ユーザAの銀行口座からユーザBの口座に送金する場合、以下の処理が行われます。 1. ユーザAの口座から3万円を引く 2. ユーザBの口座に3万円を足す もし、ユーザAの口座に1万円しかなかった場合は1の処理で預金残高がマイナスになってしまうので、残高以上の金額は送金できないようにします。このように、トランザクションの終了後にもデータベースとしての整合性を保つための性質がConsistency（一貫性）です。 その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://atmarkit.itmedia.co.jp/ait/articles/1703/01/news194.html
  - https://ja.wikipedia.org/wiki/ACID_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E7%A7%91%E5%AD%A6)#%E4%B8%80%E8%B2%AB%E6%80%A7(Consistency)
  - https://docs.oracle.com/cd/F19136_01/cncpt/transactions.html#GUID-31319EA7-994C-4D25-8814-0214ABD3CBDA

### 問題ID 26922 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26922?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: トランザクションのACID特性のうち、Isolationの説明として正しい記述はどれですか。
- 解説要約: 複数のSQLによるデータベースへの一連の操作のまとまりを「トランザクション」と呼び、トランザクションごとに処理を確定(コミット)または取消し(ロールバック)できます。 データベース管理システムがトランザクションを適切にデータベースに反映できるように、トランザクションにはACID特性と呼ばれる性質があります。 上表より正解は ・トランザクションの処理が他のトランザクションの処理に影響を与えたり、受けたりしない です。 例えば、ユーザAの銀行口座からユーザBの口座に送金する場合、以下の処理が行われます。 1. ユーザAの口座から3万円を引く 2. ユーザBの口座に3万円を足す これら2つの処理が1つのトランザクションとして実行される間に他のトランザクションによって預金残高を参照・更新されると矛盾が生じてしまいます。そのため、トランザクション実行中は他のトランザクションから処理を分離して排他制御を行う性質がIsolation（独立性）です。 その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://atmarkit.itmedia.co.jp/ait/articles/1703/01/news194.html
  - https://ja.wikipedia.org/wiki/ACID_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E7%A7%91%E5%AD%A6)#%E7%8B%AC%E7%AB%8B%E6%80%A7(Isolation)
  - https://docs.oracle.com/cd/F19136_01/cncpt/transactions.html#GUID-31319EA7-994C-4D25-8814-0214ABD3CBDA

### 問題ID 26923 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26923?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: トランザクションのACID特性のうち、Durabilityの説明として正しい記述はどれですか。
- 解説要約: 複数のSQLによるデータベースへの一連の操作のまとまりを「トランザクション」と呼び、トランザクションごとに処理を確定(コミット)または取消し(ロールバック)できます。 データベース管理システムがトランザクションを適切にデータベースに反映できるように、トランザクションにはACID特性と呼ばれる性質があります。 上表より正解は ・トランザクションのコミットにより変更された内容が確実に保存される です。 例えば、ユーザAの銀行口座からユーザBの口座に送金する場合、以下の処理が行われます。 1. ユーザAの口座から3万円を引く 2. ユーザBの口座に3万円を足す これら2つの処理を1つのトランザクションとして実行完了（コミット）した後は、システム障害が発生してもトランザクションの処理結果が消失してはいけません。この性質がDurability（永続性）です。 その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://atmarkit.itmedia.co.jp/ait/articles/1703/01/news194.html
  - https://ja.wikipedia.org/wiki/ACID_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E7%A7%91%E5%AD%A6)#%E6%B0%B8%E7%B6%9A%E6%80%A7(Durability)
  - https://docs.oracle.com/cd/F19136_01/cncpt/transactions.html#GUID-31319EA7-994C-4D25-8814-0214ABD3CBDA

### 問題ID 26924 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26924?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: SQLの説明として適切な記述はどれですか(2つ選択して下さい)。
- 解説要約: SQL(Structured Query Language：構造化問合せ言語)はリレーショナル型データベースへデータを格納したり、格納したデータにアクセスするための言語です。SQLを使用すると、データの物理的な格納場所やアクセス順序を意識する必要はなく、「どの表のどの列の値を取り出す」といった指定方法でデータにアクセスできます。 以上より、 ・リレーショナル型データベースを操作するための言語である ・データの物理的な格納場所やアクセス順序を意識することなくデータにアクセスできる が正解です。 その他の選択肢については以下のとおりです。 ・ネットワーク型データベースを操作するための言語である リレーショナル型データベースを操作するための言語なので、誤りです。 ・HTMLの後継である SQLはHTMLの後継ではないので、誤りです。HTML(HyperText Markup Language)はWebページの作成に使用されるマークアップ言語(文書の構成をコンピュータに認識させる言語)です。 ・「どのストレージの何番目の値を取り出す」といった指定方法でデータにアクセスできる データの物理的な格...
- 参考URL:
  - https://www.oracle.com/jp/database/technologies/appdev/sql.html

### 問題ID 26925 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26925?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: 1つの列と1行のデータを持ち、計算や関数の値を確認する場合などに使用する表はどれですか。
- 解説要約: DUAL表はDUMMYというVARCHAR2型の列に「X」というデータを持つ表です。データベースに接続できるユーザ(CREATE SESSION権限を持つ)なら誰でも使用できます。 計算や関数の値を確認する場合などに使用します。 以上より、 ・DUAL が正解です。 以下はDUAL表の構造と問い合わせ結果です。 DUMMYという1つの列と、Xという1行のデータを持ちます。 その他の選択肢については以下のとおりです。 ・DUMMY DUMMYはDUAL表の列名なので誤りです。 ・X XはDUAL表のデータの文字列なので誤りです。 ・VARCHAR2 VARCHAR2は可変長のデータ型なので誤りです。 ・CALC CALCという表はデフォルトで存在しません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Selecting-from-the-DUAL-Table.html#GUID-0AB153FC-5238-4E79-8522-C9E2A04AB5E4

### 問題ID 26926 (Select文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26926?q%5Binclude_reference%5D=1
- 問題傾向: Select文
- 問題文要約: DESCRIBEコマンドで表示される表の情報はどれですか(3つ選択してください)。
- 解説要約: SQL*PlusのDESCRIBEコマンドは表構造を表示するためのコマンドです。 DESCRIBEコマンドは以下のように使用します。DESCと省略することもできます。 DESCRIBE 表名; または DESC 表名; 指定した表の「列の名前」「列でNULL値が許可されるかどうか」「列のデータ型・精度」の情報が表示されます。 以上より、 ・列の名前 ・列でNULL値が許可されるかどうか ・列のデータ型・精度 が正解です。 その他の選択肢については以下のとおりです。 ・列で重複した値が許可されるかどうか DESCRIBEコマンドで表示されるのは列のNOT NULL制約（NULL値を禁止する）のみで、重複した値を禁止するPRIMARY KEY制約（主キー制約）やUNIQUE制約（一意制約）は表示されません。 ・表のデータ件数 表の行数は表示されません。
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQPUG/GUID-2E7032A1-67E9-4E13-96B6-D8F7B138ECAA.htm

### 問題ID 26927 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26927?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 置換変数を使用したSQL文実行時に、置換変数と指定した値を置き換える前後のSQL文を表示するコマンドはどれですか。
- 解説要約: 置換変数を値と置き換える前後のSQL文を表示するかしないかは以下のコマンドで設定します。 SET VERIFY {ON|OFF} デフォルトは「SET VERIFY ON」で、置換前後のSQL文が表示されます。 以上より、 ・SET VERIFY ON が正解です。 以下は実行例です。 その他の選択肢については以下のとおりです。 ・SET VERIFY SHOW このようなコマンドはありません。 ・DEFINE 変数に設定されている値を表示するコマンドなので、誤りです。 ・UNDEFINE 変数に設定されている値を破棄するコマンドなので、誤りです。 ・DESCRIBE 表の構造を表示するためのコマンドなので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqpug/SET-system-variable-summary.html#GUID-74CA1665-165D-4C0D-BBB2-681BD3485211

### 問題ID 26928 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26928?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 今日から3ヶ月後の翌日以降で最初の月曜日を表示するSQL文はどれですか。 ただし、データベースの実行環境は日本語環境とし、日付の表示書式はRR-MM-DDとします。
- 解説要約: 主な日付関数は次のとおりです。 ADD_MONTHS関数は、引数で指定した日付のnヶ月後の日付を返す関数です。 ADD_MONTHS(日付, n) 設問の「今日から3ヶ月後」は、「ADD_MONTHS(SYSDATE, 3)」のように記述できます。 NEXT_DAY関数は引数で指定した日付の翌日以降に、指定した曜日になる最初の日付を返す関数です。日本語環境の場合は、'月曜日'や省略形の'月'のように曜日を指定します。 NEXT_DAY(日付, 曜日) 設問の「今日から3ヶ月後の翌日以降で最初の月曜日」は、「NEXT_DAY(ADD_MONTHS(SYSDATE, 3), '月')」のように記述できます。 以上より、 ・SELECT NEXT_DAY(ADD_MONTHS(SYSDATE, 3), '月') FROM dual; が正解です。 正解のSQL文の実行結果は次のようになります。 その他の選択肢については以下のとおりです。 ・SELECT NEXT_DAY(SYSDATE + 3, '月') FROM dual; 今日から3日後の翌日以降で最初の月曜日が表示されるので、誤りです...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/NEXT_DAY.html#GUID-01B2CC7A-1A64-4A74-918E-26158C9096F6
  - https://docs.oracle.com/cd/F19136_01/sqlrf/ADD_MONTHS.html#GUID-B8C74443-DF32-4B7C-857F-28D557381543

### 問題ID 26929 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26929?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: EMLOYEES表の構造を確認して下さい。 COMMISSION列(歩合給)の最大値は「5000000」です。 次のSQL文を実行すると、どのようになりますか。 SELECT TO_CHAR(commission, 'L999,999') FROM employees;
- 解説要約: TO_CHAR関数は、数値や日付値を指定された書式に従って文字列に変換する関数です。 第1引数に数値が指定された場合は、数値を文字列へ変換します。 TO_CHAR(数値 [, '数値書式'] [, NLSパラメータ]) EMLOYEES表のCOMMISSION列(歩合給)は7桁ですが、設問のSQL文の数値書式「L999,999」は6桁しかありません。 SELECT TO_CHAR(commission, 'L999,999') FROM employees; このように第1引数で指定した数値(小数点より左の整数部)よりも数値書式の桁数が少ない場合など、数値を適切に変換できない場合は、次のように#記号が表示されます。適切に変換できる行は正常に表示されます。 以上より、 ・COMMISSION列の桁数よりも書式の桁数が少ない行は「#」記号が表示される が正解です。 その他の選択肢については以下のとおりです。 ・SQL文がエラーになる エラーにはなりませんので、誤りです。 ・COMMISSION列の桁数よりも書式の桁数が少ない行は「?」記号が表示される ・COMMISSION列の桁数よりも書...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/TO_CHAR-number.html#GUID-00DA076D-2468-41AB-A3AC-CC78DBA0D9CB
  - https://docs.oracle.com/cd/E96517_01/sqlrf/Format-Models.html#GUID-096CA64F-1DA3-4C49-A18B-ECC7518EE56C

### 問題ID 26930 (グループ関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26930?q%5Binclude_reference%5D=1
- 問題傾向: グループ関数
- 問題文要約: NEW_PRODUCTS表の構造を確認して下さい。 以下のSQL文の実行結果について正しいものはどれですか。 SELECT ROUND(AVG(list_price), -1) FROM new_products;
- 解説要約: 設問のSQL文は、グループ関数AVGでNEW_PRODUCTS表の平均価格を取り出し、単一行関数ROUNDで平均価格の一の位を四捨五入しています。 このように、グループ関数の集計結果を別の関数(単一行関数やグループ関数)に引数として渡すことができます。 以上より、 ・list_priceの平均値が一の位で四捨五入される が正解です。 設問のSQL文の実行結果は次のようになります。 平均価格175が一の位で四捨五入されて180と表示されます。 その他の選択肢については以下のとおりです。 ・list_priceの平均値が小数点2桁目で四捨五入される ROUND関数の引数に1を指定した場合の説明なので、誤りです。 ・単一行関数とグループ関数は同時に使用できないのでエラーとなる 同時に使用できるので、誤りです。 ・ROUND関数の引数には負の値を指定できないのでエラーとなる 負の値を指定できるので、誤りです。 例) n=-2 十の位で四捨五入される ・GROUP BY句がないのでエラーとなる グループ関数はネストしていなければGROUP BY句は必要ありませんので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/AVG.html#GUID-B64BCBF1-DAA0-4D88-9821-2C4D3FDE5E4A
  - https://docs.oracle.com/cd/F19136_01/sqlrf/ROUND-number.html#GUID-849F6C45-0D72-4464-9C0F-8B6822BA85E1

### 問題ID 26931 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26931?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 自己結合の説明として正しいものはどれですか(2つ選択してください)。
- 解説要約: 1つの表に2つの表別名を指定し、1つの表を2つの表に見立てて結合することを自己結合といいます。 自己結合を行うには、次のように記述します。 SELECT 表別名.列名 [,表別名.列名 ...] FROM 表名1 表別名1 JOIN 表名1 表別名2 ON 表別名1.列名 = 表別名2.列名 ; 自己結合を行う場合は、表に対して必ず表別名を指定します。 以上より、 ・ON句に結合条件を指定する ・表に対して必ず表別名を指定する が正解です。 以下は実行例です。 従業員の氏名を持つEMPLOYEES表と、MANAGER_IDを持つEMPLOYEES表があると見立てて2つの表を結合して、従業員名とその上司の氏名を表示しています。 SQLを表示 SELECT emp.employee_name, mgr.employee_name FROM employees emp JOIN employees mgr ON emp.manager_id = mgr.employee_id; その他の選択肢については以下のとおりです。 ・非等価結合を使用することはできない 非等価結合を使用できるため、誤り...
- 参考URL:
  - https://atmarkit.itmedia.co.jp/ait/articles/1204/23/news132.html

### 問題ID 26932 (複数の表のデータ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26932?q%5Binclude_reference%5D=1
- 問題傾向: 複数の表のデータ
- 問題文要約: 以下はOracle Databaseで使用できる表の結合方法（ANSI SQL:1999準拠）です。このうち、Oracle独自の結合構文で記述できない結合はどれですか(2つ選択して下さい)。
- 解説要約: Oracle Databaseには、Oracle独自の結合構文があります。 構文は以下の通りです。 SELECT [表接頭辞.]列名 [, [表接頭辞.]列名 ...] FROM 表名1, 表名2 WHERE 結合条件 [AND 結合条件以外の条件]; 以下はOracle Databaseで使用できる表の結合方法（ANSI SQL:1999準拠の結合構文）で、〇がついているものはOracle独自の結合構文でも記述できます。 以上より、 ・自然結合 ・完全外部結合 が正解です。 Oracle独自の結合構文での外部結合では、完全外部結合は行えません。完全外部結合には FULL [OUTER] JOINを使用します。 その他の選択肢は全てOracle独自の結合構文で記述できる結合です。以下に例を示します。 なお、SQL:1999準拠の結合構文とOracle独自の結合構文とではパフォーマンスに違いはありません。 ・等価結合 Oracle独自の結合構文ではFROM句に結合する表を指定し、WHERE句に等価結合の結合条件を指定することで、ON句や USING句を使用した等価結合の結果と等しくなりま...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/Joins.html#GUID-39081984-8D38-4D64-A847-AA43F515D460

### 問題ID 26933 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26933?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 以下のSQL文の説明として正しいものはどれですか(2つ選択して下さい)。 INSERT ALL WHEN salary <= 200000 OR salary IS NULL THEN INTO grade_E WHEN salary > 200000 AND salary <= 400000 THEN INTO grade_D WHEN salary > 400000 AND salary <= 600000 THEN INTO grade_C WHEN salary > 600000 AND salary <= 800000 THEN INTO grade_B ELSE INTO grad...
- 解説要約: 設問のSQL文は、1つのSQL文で複数の表にデータを追加できるマルチテーブル・インサートです。WHEN句を使用して条件に合致する行を挿入します。 INSERT ALL（デフォルト）では、副問合せで返される行が全WHEN句の条件式で評価され、条件に合致したものがWHEN句に対応するINTO句で挿入されます。つまり、条件に合致した全ての表に挿入されます。 ELSE句ではWHEN句の条件に合致しない行が挿入されます。ELSE句を省略した場合は、WHEN句の条件に合致しない行は挿入されません。 以上より、 ・副問合せのSELECT句で返される行が全てのWHEN句で評価され、条件に合致した全てのINTO句で挿入される ・全てのWHEN句の条件に合致しない行は、ELSE句でGRADE_A表に挿入される が正解です。 以下は設問のSQL文の実行例です。 例）副問合せでEMPLOYEES表のEMPLOYEE_ID列（従業員番号）とSALARY列（給与）を参照し、WHEN句のそれぞれの条件に合致した給与等級の表（GRADE_A～GRADE_E表）に挿入する SQLを表示 INSERT ALL WHEN ...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/INSERT.html#GUID-903F8043-0254-4EE9-ACC1-CB8AC0AF3423

### 問題ID 26934 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26934?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: EMPLOYEES表とGRADE_E表の構造を確認して下さい。 EMPLOYEES表のSALARY列（給与）が200000以下もしくはNULLである従業員の従業員番号と給与をGRADE_E表に挿入するには、どのSQL文を実行しますか（2つ選択してください）。 なお、GRADE_E表にはデータは入っていません。
- 解説要約: 選択肢のMERGE文は異なる表の行をマージできるDML文です。1つのMERGE文で、該当する行があればUPDATE、無ければINSERTというように、行の挿入と更新を同時に行えます。 MERGE INTO 表名1 [表別名] USING 表名2 ｜ 副問合せ [表別名] ON ( 結合条件 ) WHEN MATCHED THEN UPDATE SET 列名 = 値 , ... [DELETE WHERE 条件] WHEN NOT MATCHED THEN INSERT [ (列名, ... ) ] VALUES ( 値 , ... ); 選択肢を1つずつ確認します。 ・MERGE INTO grade_E g USING employees e ON (g.employee_id = e.employee_id) WHEN NOT MATCHED THEN INSERT (g.employee_id, g.salary) VALUES (e.employee_id, e.salary) WHERE (e.salary <= 200000 OR e.salary IS NULL); EM...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/MERGE.html#GUID-5692CCB7-24D9-4C0E-81A7-A22436DC968F

### 問題ID 26935 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26935?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文で索引を作成しました。この索引の説明として正しいものはどれですか(2つ選択して下さい)。 CREATE INDEX ind_price ON new_products(list_price DESC);
- 解説要約: 設問のCREATE INDEX文のDESCキーワードは索引を降順で作成するように指定しています。 降順索引はOracle Databaseにファンクション索引として扱われます。ファンクション索引とは、関数や式を使用した列に作成される索引です。 以上より、 ・降順索引である ・ファンクション索引として扱われる が正解です。 以下はSQL文の実行例です。 降順索引はファンクション索引として扱われますので、ファンクション索引の式が格納されるUSER_IND_EXPRESSIONSビューで確認できます。 SQLを表示 CREATE INDEX ind_price ON new_products(list_price DESC); SELECT index_name, table_name, column_expression FROM user_ind_expressions; その他の選択肢については以下のとおりです。 ・昇順索引である 昇順索引はASCキーワードを指定するので、誤りです。なお、ASC|DESCを省略した場合のデフォルトは昇順です。 ・不可視索引である 不可視索引（SQL問合...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CREATE-INDEX.html#GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE__GUID-92F4F0FB-499A-4ED7-8630-B219F8A50B90

### 問題ID 26936 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26936?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文で索引を作成しました。この索引の説明として正しいものはどれですか(2つ選択して下さい)。 CREATE INDEX ind_price ON new_products(list_price) INVISIBLE;
- 解説要約: 設問のCREATE INDEX文のINVISIBLEキーワードは不可視索引を作成します。 不可視索引は、デフォルトではSQL問合せの処理を最適化するオプティマイザから見えないため、問合せ時に使用されない索引です。索引を削除せずに不可視索引に設定することで索引が無い場合のパフォーマンスをテストでき、必要であればデフォルトのVISIBLEに設定し直すことができます。 以上より、 ・不可視索引である ・デフォルトでは使用されない索引である が正解です。 以下はSQL文の実行例です。 LIST_PRICE列に不可視索引を作成し、「set autotrace on explain」で問合せの実行結果と実行計画（オプティマイザによって作成されるSQL文の実行手順）を表示しています。 問合せでWHERE句の条件にLIST_PRICE列を指定しましたが、実行計画ではTABLE ACCESS FULLで表全体を読み出しており、不可視索引は使用されていません。 SQLを表示 CREATE INDEX ind_price ON new_products(list_price) INVISIBLE; set ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CREATE-INDEX.html#GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE__BABBCCAA

### 問題ID 26937 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26937?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を実行した結果の説明として正しい記述はどれですか。 CREATE TABLE test ( test_id NUMBER(4), lot_no NUMBER(4), test_name VARCHAR2(40), CONSTRAINT pk_test PRIMARY KEY(test_id, lot_no) USING INDEX(CREATE INDEX idx_test_lot ON test(test_id, lot_no)) );
- 解説要約: PRIMARY KEY制約またはUNIQUE制約を定義するCONSTRAINT句では、USING INDEX句で指定した索引を使用できます。 USING INDEX句は列レベル制約、表レベル制約のどちらにも記述できます。 USING INDEX 索引名 | CREATE INDEX 索引名 ON 表名(列名 [,列名...]) 設問のSQL文は表レベル制約で、CREATE INDEX文で作成した索引idx_test_lotをPRIMARY KEY制約pk_testに指定しています。これらの索引と制約はCREATE TABLE文のTEST表と同時に作成されます。 以上より、 ・TEST表にPRIMARY KEY制約pk_testと索引idx_test_lotが作成される が正解です。 以下はSQL文の実行例です。 SQLを表示 CREATE TABLE test ( test_id NUMBER(4), lot_no NUMBER(4), test_name VARCHAR2(40), CONSTRAINT pk_test PRIMARY KEY(test_id, lot_no) USI...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6
  - https://docs.oracle.com/cd/F19136_01/sqlrf/constraint.html#GUID-1055EA97-BA6F-4764-A15F-1024FD5B6DFE__USING_INDEX_CLAUSE-8404D2EF

### 問題ID 26938 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26938?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を順番に実行しました。 CREATE GLOBAL TEMPORARY TABLE temp ( temp_id NUMBER(2), temp_name VARCHAR2(20) ) ON COMMIT PRESERVE ROWS; INSERT INTO temp VALUES (1, 'tempA'); COMMIT; この後の説明として正しい記述はどれですか(2つ選択して下さい)。
- 解説要約: 設問のGLOBAL TEMPORARY句ではグローバル一時表を作成しています。一時表は、トランザクションを終了またはセッションを切断するまでの間のみデータを保持する表です。一時表に挿入したデータはそのセッション内でのみ参照できます。セッション終了後も表の構造は残ります。セッション内だけ表の構造を参照できるプライベート一時表に対して、グローバル一時表は全てのセッションから表の構造を参照できます。 ON COMMIT PRESERVE ROWS句はセッション終了時にデータを削除（TRUNCATE）します。 TEMP表を作成した後はINSERT文で1件のデータを登録していますが、その後のCOMMIT文でトランザクションが終了した後もデータを参照できます。 以上より、 ・TEMP表のデータは1件である ・他のセッションからTEMP表を参照すると、データは0件である が正解です。 以下はSQL文の実行例です。 CREATE文を実行したセッション内ではTEMP表に挿入したデータを参照できます。他のセッションからはTEMP表の構造は確認できますがデータは参照できません。 SQLを表示 CREATE ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/tables-and-table-clusters.html#GUID-23B23DCF-7482-4585-9C63-AC073C5DE224
  - https://atmarkit.itmedia.co.jp/fdb/ref/ref_oracle/table.html

### 問題ID 26939 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26939?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: グローバル一時表の説明として間違っているものはどれですか。
- 解説要約: 一時表は、トランザクションを終了またはセッションを切断するまでの間のみデータを保持する表です。一時表に挿入したデータはそのセッション内でのみ参照できます。 一時表にはセッション内だけ表の構造を参照できるプライベート一時表と、全てのセッションから表の構造を参照できるグローバル一時表があります。 グローバル一時表の説明として間違っているものを回答しますので、 ・表を作成したセッション内でのみ表の構造を参照できる が正解です。 その他の選択肢については以下のとおりです。 ・トランザクションを終了またはセッションを切断するまでの間のみデータを保持する 一時表の正しい説明です。 ・実行したDML文はロールバックできる 一時表へのDML文の実行時は通常の表のようにUNDO（変更前のデータ）を生成するので、処理をロールバックすることができます。正しい説明です。 ・パブリックシノニムを作成できる シノニムはオブジェクトの別名を表すスキーマ・オブジェクトです。グローバル一時表は他のセッションからも表の構造を参照できるので、全てのユーザーが使用できるパブリックシノニムを作成できます。正しい説明です。 ・索...
- 参考URL:
  - https://docs.oracle.com/cd/F39414_01/admin/managing-tables.html#GUID-23B23DCF-7482-4585-9C63-AC073C5DE224

### 問題ID 26940 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26940?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 外部表に対して行えることはどれですか(3つ選択して下さい)。
- 解説要約: 外部表は、データベース外部のファイルに格納されたデータにアクセスするための仕組みです。データベースには外部表の情報を記述するメタデータのみ格納されます。 外部表は作成した時点でデータを問い合わせることができ、SQL*Loaderのように外部ファイルのデータを実表にロードする必要はありません。 外部表のデータはソートや結合を行えます。外部表に索引を作成したり、DML文での更新はできません。 以上より、 ・データの問い合わせ ・データのソート ・データの結合 が正解です。 以下はそれぞれの操作の実行例です。 ・データの問い合わせ SQLを表示 CREATE TABLE ext1 ( id NUMBER(4), text VARCHAR2(10)) ORGANIZATION EXTERNAL ( TYPE ORACLE_LOADER DEFAULT DIRECTORY ext_data ACCESS PARAMETERS ( RECORDS DELIMITED BY NEWLINE FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ( i...
- 参考URL:
  - https://docs.oracle.com/cd/E82638_01/admin/managing-tables.html#GUID-F6948F0E-0557-4C42-9145-1897DE974CC3

### 問題ID 26941 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26941?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 下図はOS（Linux）上にあるテキストファイル「ext1.csv」です。 このテキストファイルをデータソースとしてOracle Databaseに外部表EXT1を作成します。 次のSQL文のうち、デフォルト値と同じであるため省略できる句はどれですか(3つ選択して下さい)。 CREATE TABLE ext1 ( id NUMBER(4), text VARCHAR2(10)) ORGANIZATION EXTERNAL ( TYPE ORACLE_LOADER DEFAULT DIRECTORY ext_data ACCESS PARAMETERS ( RECORDS DELIMITED B...
- 解説要約: 選択肢を1つずつ確認します。 ・ORGANIZATION EXTERNAL 外部表を作成するための句なので省略できません。 ・TYPE 外部表には主に2つの型があり、次のアクセスドライバ（外部データを解析するAPI）によってサポートされます。 ・ORACLE_LOADER：テキスト形式の外部ファイルのデータをロードする（読み込む）。デフォルト値 ・ORACLE_DATAPUMP：既存の表のデータをバイナリ形式のダンプファイルにアンロード（書き込む）、ダンプファイルのデータをデータベースにロードする（読み込む） 設問のデータソースはテキストファイルなのでORACLE_LOADERを使用しますが、ORACLE_LOADERはデフォルト値なので省略できます。 ・DEFAULT DIRECTORY デフォルトで使用するディレクトリを、ディレクトリのパスではなくディレクトリオブジェクトとして指定します。LOCATION句のデータファイルやACCESS PARAMETERS句のログファイルなどのディレクトリオブジェクトを省略した場合に使用されます。DEFAULT DIRECTORYのデフォルト値は...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sutil/oracle-external-tables-concepts.html#GUID-ACF1D3AA-1D61-4682-AEC5-42C944756E12

### 問題ID 26942 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26942?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: テキスト形式の外部ファイルのデータをロードするための、外部表のアクセスドライバはどれですか。
- 解説要約: 外部表は、データベース外部のファイルに格納されたデータにアクセスするための仕組みです。データベースには外部表の情報を記述するメタデータのみ格納されます。 外部表には主に2つの型があり、次のアクセスドライバ（外部データを解析するAPI）によってサポートされます。 ・ORACLE_LOADER：テキスト形式の外部ファイルのデータをロードする（読み込む）。デフォルト値 ・ORACLE_DATAPUMP：既存の表のデータをバイナリ形式のダンプファイルにアンロード（書き込む）、ダンプファイルのデータをデータベースにロードする（読み込む） 以上より、 ・ORACLE_LOADER が正解です。 以下はORACLE_LOADERを使用してOS（Linux）上のテキストデータファイル「ext1.csv」をロードする外部表の例です。 例）テキストデータファイル「ext1.csv」 外部表EXT1を作成直後に外部ファイルのデータを問合せできます。 SQLを表示 CREATE TABLE ext1 ( id NUMBER(4), text VARCHAR2(10)) ORGANIZATION EXTERNA...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sutil/oracle_loader-access-driver.html#GUID-EA56D498-E8BB-4E02-8ABF-12E7083ED9D5

### 問題ID 26943 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26943?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: データベースのデータをバイナリ形式のダンプファイルにアンロードしたり、ダンプファイルのデータをデータベースにロードするためのアクセスドライバはどれですか。
- 解説要約: 外部表は、データベース外部のファイルに格納されたデータにアクセスするための仕組みです。データベースには外部表の情報を記述するメタデータのみ格納されます。 外部表には主に2つの型があり、次のアクセスドライバ（外部データを解析するAPI）によってサポートされます。 ・ORACLE_LOADER：テキスト形式の外部ファイルのデータをロードする（読み込む）。デフォルト値 ・ORACLE_DATAPUMP：既存の表のデータをバイナリ形式のダンプファイルにアンロード（書き込む）、ダンプファイルのデータをデータベースにロードする（読み込む） 以上より、 ・ORACLE_DATAPUMP が正解です。 ORACLE_DATAPUMPについては参考の「■ORACLE_DATAPUMPの使用」をご参照ください。 その他の選択肢については以下のとおりです。 ・ORACLE_LOADER テキスト形式の外部ファイルのデータをロードするアクセスドライバなので、誤りです。 ・ORACLE_BINARY ・ORACLE_DUMP これらのようなアクセスドライバは存在しません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sutil/oracle_datapump-access-driver.html#GUID-084DC623-9656-499C-885B-D8180C07704B

### 問題ID 26944 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26944?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 外部表EXT_STUDENTSを作成し、STUDENTS表のデータをダンプファイル「ext_students.dmp」にアンロードします。 次のSQL文の空欄に入る語句はどれですか。 CREATE TABLE ext_students ORGANIZATION EXTERNAL ( TYPE ORACLE_DATAPUMP DEFAULT DIRECTORY ext_data LOCATION ('ext_students.dmp') ) ________ SELECT * FROM students;
- 解説要約: 外部表は、データベース外部のファイルに格納されたデータにアクセスするための仕組みです。データベースには外部表の情報を記述するメタデータのみ格納されます。 設問のように、アクセスドライバ（外部データを解析するAPI）にORACLE_DATAPUMPを使用して既存の表のデータをダンプファイルにアンロードする（書き込む）には、AS SELECT句を使用します。 CREATE TABLE 外部表名 ORGANIZATION EXTERNAL ( TYPE ORACLE_DATAPUMP DEFAULT DIRECTORY デフォルトのディレクトリ LOCATION ([ディレクトリ:]'データファイル') ) AS SELECT 列名[, 列名 ...] FROM 表名 [WHERE 条件]); 以上より、 ・AS が正解です。 外部表に対して作成されたダンプファイルはバイナリ形式でORACLE_DATAPUMPのみが読み取りできます。ダンプファイルは他のデータベースの外部表でも使用できます。 以下は設問のSQL文の実行例です。 SQLを表示 CREATE TABLE ext_students...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sutil/oracle_datapump-access-driver.html#GUID-0B2EC1B2-701D-42ED-874C-47F22F21D847

### 問題ID 26945 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26945?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を実行しました。 CREATE TABLE parent ( id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); CREATE TABLE child ( id NUMBER(2) CONSTRAINT cid_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT cname_uq UNIQUE, deptid NUMBER(2) CONSTRAINT dept_fk REFERENCES parent (id) ); ALTER TABLE parent D...
- 解説要約: 設問のPARENT表のID列は、CHILD表のDEPTID列からFOREIGN KEY制約(参照整合性制約とも呼ばれます)の親キーとして参照されています。 FOREIGN KEY制約から参照されているPRIMARY KEY制約またはUNIQUE制約をDISABLE CONSTRAINTで無効化する場合は、設問のようにCASCADEオプションを指定して、無効化する制約を参照するFOREIGN KEY制約も同時に無効化しなければなりません。CASCADEオプションを付けないとエラーになります。 ALTER TABLE parent DISABLE CONSTRAINT pid_pk CASCADE; 上記のSQL文でPARENT表の制約PID_PKとCHILD表の制約DEPT_FKが無効化されました。 設問では表作成時の状態に制約を戻すことを問われていますが、ENABLE CONSTRAINTで制約を有効化する場合はCASCADEオプションは指定できないので、各制約をそれぞれ有効化する必要があります。 以上より、 ・ALTER TABLE parent ENABLE CONSTRAINT ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#CJAHHIBI
  - https://docs.oracle.com/cd/E57425_01/121/SQLRF/statements_3001.htm#i2056917

### 問題ID 26946 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26946?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューに関する説明として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: ビューとは、1つまたは複数の表や他のビューを基にして作成する仮想的な表のことです。ビューに対する問合せを実行すると、Oracleサーバーは、ビューの基となっている実表へ問合せ処理を行います。 ビューには以下の特徴があります。 ・ビューはデータベース・オブジェクトとしてデータベースに情報が格納される（オブジェクトIDを持つ）が、ビューには実データは含まれまないため、実表のようにセグメント（データの記憶域）を持たない ・索引は作成できない ・他のユーザーが所有する表（異なるスキーマの表）に対してもSELECT権限があればビューを作成できる ・ビューと実表を結合できる 以上より、 ・ビューはデータベース・オブジェクトとしてデータベースに格納される ・ビューには実データは含まれない が正解です。 その他の選択肢については以下のとおりです。 ・表や索引と同様にビューセグメントを持つ ビューは実表や索引のようにセグメントを持たないので、誤りです。 ・ビューに索引を作成できる ビューには索引を作成できませんので、誤りです。 ・異なるスキーマの表に対してはビューを作成できない 他のユーザーが所有する表...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/admin/managing-views-sequences-and-synonyms.html#GUID-6A691576-77B3-4DAF-ABC7-3EF4707302D4

### 問題ID 26947 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26947?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: EMPLOYEES表の構造を確認して下さい。 以下の順番でSQL文を実行した後の説明として、正しいものはどれですか。 ① CREATE OR REPLACE VIEW v_emp AS SELECT employee_id, employee_name FROM employees; ② INSERT INTO v_emp VALUES (9999, 'Tanaka'); ③ DROP VIEW v_emp;
- 解説要約: 設問の①では、EMPLOYEES表からEMPLOYEE_IDとEMPLOYEE_NAMEを取り出したビューV_EMPを作成しています。 ②では、ビューV_EMPを通じて実表であるEMPLOYEES表に新しい行を追加しています。 ③では、ビューV_EMPを削除しています。しかし、②でビューを通じて追加した行はEMPLOYEES表に残ります。 以上より、 ・EMPLOYEES表に②のINSERT文の行が追加されている が正解です。 以下は設問のSQL文の実行例です。 SQLを表示 CREATE OR REPLACE VIEW v_emp AS SELECT employee_id, employee_name FROM employees; INSERT INTO v_emp VALUES (9999, 'Tanaka'); DROP VIEW v_emp; SELECT employee_id, employee_name FROM employees; その他の選択肢については以下のとおりです。 ・EMPLOYEES表に行は追加されていない ビューを通じて実表に追加した行はビューを削除...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CREATE-VIEW.html#GUID-61D2D2B4-DACC-4C7C-89EB-7E50D9594D30

### 問題ID 26948 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26948?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: 次の権限のうち、システム権限はどれですか(3つ選択して下さい)。
- 解説要約: システム権限は特定のデータベース操作を許可するための権限です。管理者ユーザーが付与します。 主なシステム権限は次のとおりです。 以上より、 ・CREATE SESSION ・CREATE USER ・ALTER ANY TABLE が正解です。 スキーマとは、1人のユーザーが所有するオブジェクトの集合です。 システム権限のうち、ANY がついたシステム権限は、任意のスキーマに対して操作できる権限です。 例えば表を作成する権限にはCREATE TABLE権限とCREATE ANY TABLE権限がありますが、CREATE TABLE権限は自分のスキーマにのみ表を作成できるのに対し、CREATE ANY TABLE権限は他人のスキーマを含め任意のスキーマに表を作成できます。 その他の選択肢は全てオブジェクト権限（特定のデータベース・オブジェクトへの操作を許可するための権限）です。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3__BABEFFEE
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-6F401301-B5EA-482E-9615-21FD840CAF60

### 問題ID 26949 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26949?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: 次の権限のうち、システム権限はどれですか(4つ選択して下さい)。
- 解説要約: システム権限は特定のデータベース操作を許可するための権限です。管理者ユーザーが付与します。 主なシステム権限は次のとおりです。 以上より、 ・CREATE TABLE ・CREATE ANY TABLE ・CREATE VIEW ・DROP ANY TABLE が正解です。 スキーマとは、1人のユーザーが所有するオブジェクトの集合です。 システム権限のうち、ANY がついたシステム権限は、任意のスキーマに対して操作できる権限です。 例えば表を作成する権限にはCREATE TABLE権限とCREATE ANY TABLE権限がありますが、CREATE TABLE権限は自分のスキーマにのみ表を作成できるのに対し、CREATE ANY TABLE権限は他人のスキーマを含め任意のスキーマに表を作成できます。 その他の選択肢は全てオブジェクト権限（特定のデータベース・オブジェクトへの操作を許可するための権限）です。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3__BABEFFEE
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-6F401301-B5EA-482E-9615-21FD840CAF60

### 問題ID 26950 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26950?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: 次の権限のうち、オブジェクト権限はどれですか(3つ選択して下さい)。
- 解説要約: オブジェクト権限は特定のデータベース・オブジェクトへの操作を許可するための権限です。オブジェクト権限は管理者ユーザー、またはオブジェクトの所有者が付与します。 主なオブジェクト権限は次のとおりです。 以上より、 ・INSERT ・UPDATE ・ALTER が正解です。 オブジェクトの所有者はオブジェクト権限を明示的に付与しなくても自分のオブジェクトに対する操作を行えます。 その他の選択肢は全てシステム権限（特定のデータベース操作を許可するための権限）です。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3__BGBCIIEG
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-8AB43A10-FD9E-4B08-9C23-71C5A15DE1FC

### 問題ID 26951 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26951?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: 次の権限のうち、オブジェクト権限はどれですか(4つ選択して下さい)。
- 解説要約: オブジェクト権限は特定のデータベース・オブジェクトへの操作を許可するための権限です。オブジェクト権限は管理者ユーザー、またはオブジェクトの所有者が付与します。 主なオブジェクト権限は次のとおりです。 以上より、 ・SELECT ・DELETE ・INDEX ・REFERENCES が正解です。 オブジェクトの所有者はオブジェクト権限を明示的に付与しなくても自分のオブジェクトに対する操作を行えます。 その他の選択肢は全てシステム権限（特定のデータベース操作を許可するための権限）です。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3__BGBCIIEG
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-8AB43A10-FD9E-4B08-9C23-71C5A15DE1FC

### 問題ID 26952 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26952?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: システム権限に関する説明として、正しいものはどれですか。
- 解説要約: システム権限は特定のデータベース操作を許可するための権限です。システム権限は、管理者ユーザーが付与します。 ・管理者ユーザーによるシステム権限の付与 GRANT システム権限 TO {ユーザー名 | PUBLIC} [WITH ADMIN OPTION]; ※PUBLICは全てのユーザーです。 ※WITH ADMIN OPTION句を指定すると、システム権限を付与されたユーザーが他のユーザーに対してシステム権限を付与できるようになります。 以上より、 ・WITH ADMIN OPTION句で、付与されたシステム権限を他のユーザーに付与できる が正解です。 その他の選択肢については以下のとおりです。 ・WITH GRANT OPTION句で、付与されたシステム権限を他のユーザーに付与できる オブジェクト権限の付与に関する句なので、誤りです。 WITH GRANT OPTION句を指定すると、オブジェクト権限を付与されたユーザーが他のユーザーに対してオブジェクト権限を付与できるようになります。 ・システム権限を付与できるのはオブジェクトの所有者である システム権限を付与できるのは管理者ユー...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-6F401301-B5EA-482E-9615-21FD840CAF60

### 問題ID 26953 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26953?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: SYSTEMユーザーとしてUSER1ユーザーとUSER2ユーザーを作成しました。 CREATE USER user1 IDENTIFIED BY password; CREATE USER user2 IDENTIFIED BY password; これらのユーザーがデータベースに接続できるようにCREATE SESSIONシステム権限を付与するSQL文はどれですか。
- 解説要約: 設問ではCREATE USER文で、認証のパスワードを指定してUSER1ユーザーとUSER2ユーザーを作成しています。 CREATE USER ユーザー名 IDENTIFIED BY パスワード; ユーザーにシステム権限を付与する場合は、GRANT文を使用します。 GRANT システム権限 TO {ユーザー名 | PUBLIC} [WITH ADMIN OPTION]; ※PUBLICは全てのユーザーです。 ※WITH ADMIN OPTION句を指定すると、システム権限を付与されたユーザーが他のユーザーに対してシステム権限を付与できるようになります。 一度に複数の権限やユーザーを指定する場合はそれぞれを「,」で区切ります。 以上より、 ・GRANT CREATE SESSION TO user1, user2; が正解です。 以下は実行例です。 SQLを表示 CREATE USER user1 IDENTIFIED BY password; CREATE USER user2 IDENTIFIED BY password; GRANT CREATE SESSION TO user1,...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3

### 問題ID 26954 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26954?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: PINGTユーザーとしてEMPLOYEES表に対するSELECT, INSERTオブジェクト権限をUSER1ユーザーに付与します。正しいSQL文はどれですか。
- 解説要約: オブジェクト権限を付与する場合は、GRANT文を使用します。 GRANT {オブジェクト権限 | ALL} ON オブジェクト名 TO {ユーザー名 | PUBLIC} [WITH GRANT OPTION]; ※ALLは全てのオブジェクト権限です。 ※WITH GRANT OPTION句を指定すると、オブジェクト権限を付与されたユーザーが他のユーザーに対してオブジェクト権限を付与できるようになります。 一度に複数の権限やユーザーを指定する場合はそれぞれを「,」で区切ります。 以上より、 ・GRANT SELECT, INSERT ON employees TO user1; が正解です。 以下は実行例です。 SQLを表示 GRANT SELECT, INSERT ON employees TO user1; その他の選択肢は全て書式が間違っているので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3

### 問題ID 26955 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26955?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: SYSTEMユーザーとしてCREATE TABLE権限を全てのユーザーに付与します。 次のSQL文の空欄に入る語句はどれですか。 GRANT CREATE TABLE TO ____________;
- 解説要約: システム権限を付与する場合は、GRANT文を使用します。 GRANT システム権限 TO {ユーザー名 | PUBLIC} [WITH ADMIN OPTION]; ※PUBLICは全てのユーザーです。 ※WITH ADMIN OPTION句を指定すると、システム権限を付与されたユーザーが他のユーザーに対してシステム権限を付与できるようになります。 以上より、 ・PUBLIC が正解です。 以下は実行例です。 SQLを表示 GRANT CREATE TABLE TO PUBLIC; その他の選択肢は全てデフォルトでは存在しないキーワードです。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3

### 問題ID 26956 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26956?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: SYSTEMユーザーとして、全てのユーザーに付与していたCREATE TABLE権限を取消します。 正しいSQL文はどれですか。
- 解説要約: システム権限を取消す場合は、REVOKE文を使用します。 REVOKE システム権限 FROM {ユーザー名 | PUBLIC}; ※PUBLICは全てのユーザーです。 以上より、 ・REVOKE CREATE TABLE FROM PUBLIC; が正解です。 REVOKE文で権限を取消す際には、明示的に指定したものしか取消せません。全てのユーザーPUBLICからCREATE TABLE権限を取消しても、個別のユーザーに同じ権限が付与されていればその権限は残ります。 以下は実行例です。 SQLを表示 REVOKE CREATE TABLE FROM PUBLIC; その他の選択肢は全て権限を取消すSQL文ではないので、誤りです。 REMOVE文、ERASE文、ALLというユーザー名のキーワードは存在しません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/REVOKE.html#GUID-BAAD2331-40A5-4366-86CA-BAA6B957E866

### 問題ID 26957 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26957?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: CREATE USERシステム権限と、DBA_USERSデータ・ディクショナリ・ビューに対するSELECTオブジェクト権限を、SYSユーザーとしてPINGTユーザーに付与します。正しいSQL文はどれですか。
- 解説要約: 権限を付与する場合はGRANT文を使用しますが、システム権限（特定のデータベース操作を許可するための権限）とオブジェクト権限（特定のデータベース・オブジェクトへの操作を許可するための権限）は1つのGRANT文では同時に付与できません。それぞれ以下の書式で付与します。 ・管理者ユーザーによるシステム権限の付与 GRANT システム権限 TO {ユーザー名 | PUBLIC} [WITH ADMIN OPTION]; ※PUBLICは全てのユーザーです。 ※WITH ADMIN OPTION句を指定すると、システム権限を付与されたユーザーが他のユーザーに対してシステム権限を付与できるようになります。 ・管理者ユーザーまたはオブジェクトの所有者によるオブジェクト権限の付与 GRANT {オブジェクト権限 | ALL} ON オブジェクト名 TO {ユーザー名 | PUBLIC} {WITH GRANT OPTION}; ※ALLは全てのオブジェクト権限です。 ※WITH GRANT OPTION句を指定すると、オブジェクト権限を付与されたユーザーが他のユーザーに対してオブジェクト権限を付与で...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3

### 問題ID 26958 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26958?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: CREATE ROLE権限を持つPINGTユーザーとしてロールを作成しました。 CREATE ROLE role1; この後の説明として正しいものはどれですか。
- 解説要約: ロールとは、複数の権限を1つにまとめて名前を付けたものです。 ロールの作成や、ユーザーへのロールの付与、ユーザーからのロールの取消しはデータベース管理者かCREATE ROLEシステム権限を持つユーザーが行います。作成されたロールは作成者に所有されるスキーマ・オブジェクトとしてではなく、ユーザーと同様にシステム全体で共有されるオブジェクトとして格納されます。 そのため、ロール作成権限を持つ他のユーザーでも、設問のロール「ROLE1」と同じ名前のロールは作成できません。 以上より、 ・SYSTEMユーザーとしてロール「ROLE1」を作成できない が正解です。 以下は実行例です。 その他の選択肢については以下のとおりです。 ・SYSTEMユーザーとしてロール「ROLE1」を作成できる ロール名はデータベース内で一意でなければならないので、誤りです。 ・ロール「ROLE1」の所有者はPINGTユーザーである ・ロール「ROLE1」の所有者はSYSユーザーである ロールは特定のユーザーに所有されるスキーマ・オブジェクトではないので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CREATE-ROLE.html#GUID-B2252DC5-5AE7-49B7-9048-98062993E450

### 問題ID 26959 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26959?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: ロールの付与を行うGRANT文に関する説明として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: ユーザーにロールを付与したり、ロールに権限や他のロールを付与するにはGRANT文を使用します。 ・ユーザーにロールを付与 GRANT ロール名 TO {ユーザー名 | PUBLIC} [WITH ADMIN OPTION]; ※PUBLICは全てのユーザーです。 ※WITH ADMIN OPTION句を指定すると、ロールを付与されたユーザーが他のユーザーに対してロールを付与、取消しできるようになります。 1つのGRANT文でシステム権限とロールを同時に付与できます。オブジェクト権限とロールは同時に付与できません。 GRANT ロール名, システム権限 TO {ユーザー名 | PUBLIC | 他のロール名} [WITH ADMIN OPTION]; 以上より、 ・WITH ADMIN OPTION句を指定できる ・1つのGRANT文でロールとシステム権限を同時に付与できる が正解です。 以下は実行例です。 WITH ADMIN OPTION句付きでロールやシステム権限を付与されたユーザーは、他のユーザーに対してもロールを付与できるようになります。その際もWITH ADMIN OPTIO...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3

### 問題ID 26960 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26960?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: 以下のSQL文を実行しました。 CREATE ROLE role1; GRANT CREATE SESSION TO role1; GRANT role1 TO user1; GRANT CREATE SESSION TO user1; この後、次のSQL文を実行する際の説明として正しいものはどれですか(2つ選択して下さい)。 REVOKE CREATE SESSION FROM role1;
- 解説要約: 設問のSQL文ではROLE1ロールを作成し、CREATE SESSIONシステム権限（データベースに接続する権限）をROLE1ロールに付与しています。そして、ROLE1ロールと、個別にCREATE SESSION権限をUSER1ユーザーに付与しています。 REVOKE文ではROLE1ロールからCREATE SESSION権限を取消しています。 ユーザーに付与したロールに対して権限を追加したり、ロールから権限を削除した場合、ロールを付与されている全てのユーザーにロールの変更が影響します。 また、複数のロールや個別の権限によって同じ権限が付与されていても、権限を取消す際には、明示的に指定したものしか取消せません。よって、ROLE1ロールに含まれているCREATE SESSION権限は取消せましたが、個別に付与されているCREATE SESSION権限は残ります。 以上より、 ・ROLE1ロールを付与されている全てのユーザーにロールの変更が反映される ・CREATE SESSION権限は残るので、USER1ユーザーはデータベースに接続できる が正解です。 以下は実行例です。 SQLを表示 S...
- 参考URL:
  - https://atmarkit.itmedia.co.jp/fdb/ref/ref_oracle/role.html#09
  - https://docs.oracle.com/cd/F19136_01/sqlrf/REVOKE.html#GUID-BAAD2331-40A5-4366-86CA-BAA6B957E866

### 問題ID 26961 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26961?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: PINGTユーザーでPARENT表を作成しました。 CREATE TABLE parent ( id NUMBER(2) CONSTRAINT pid_pk PRIMARY KEY, dept_name VARCHAR2(10) ); USER1ユーザーとして、PARENT表を参照するFOREIGN KEY制約を持つCHILD表を作成します。この場合、PINGTユーザーがUSER1ユーザーに付与すべきPARENT表に対するオブジェクト権限はどれですか。最低限必要なものを1つ選択して下さい。 なお、CREATE TABLE権限など必要なシステム権限は既にUSER1ユーザーに付与されているものとし...
- 解説要約: オブジェクト権限は、特定のデータベース・オブジェクトへの操作を許可するための権限です。 主なオブジェクト権限は次のとおりです。 設問で問われているのは他ユーザー所有の表を参照するFOREIGN KEY制約を作成するのに最低限必要なオブジェクト権限なので、 ・REFERENCES が正解です。 REFERENCES権限があれば表の作成は可能です。ただし、PINGTユーザーのPARENT表のデータを問合せるにはSELECT権限が必要になります。 例）CHILD表を作成するSQL文 CREATE TABLE child ( id NUMBER(2) CONSTRAINT id_pk PRIMARY KEY, name VARCHAR2(10) CONSTRAINT name_nn NOT NULL, deptid NUMBER(2), CONSTRAINT dept_fk FOREIGN KEY (deptid) REFERENCES pingt.parent (id) ); 以下は実行例です。 SQLを表示 SHOW USER CREATE TABLE parent (id NUMBER(...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html

### 問題ID 26962 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26962?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: ユーザーやPUBLICに対してオブジェクト権限の付与を行うGRANT文に関する説明として正しいものはどれですか。
- 解説要約: オブジェクト権限を付与する場合は、GRANT文を使用します。 ・管理者ユーザーまたはオブジェクトの所有者によるオブジェクト権限の付与 GRANT {オブジェクト権限 | ALL} ON オブジェクト名 TO {ユーザー名 | PUBLIC} [WITH GRANT OPTION]; ※ALLは全てのオブジェクト権限です。 ※WITH GRANT OPTION句を指定すると、オブジェクト権限を付与されたユーザーが他のユーザーに対してオブジェクト権限を付与できるようになります。 以上より、 ・WITH GRANT OPTION句を指定できる が正解です。 以下は実行例です。 WITH GRANT OPTION句付きでオブジェクト権限を付与されたユーザーは、他のユーザーに対してもオブジェクトを付与できるようになります。その際もWITH GRANT OPTION句を付けられます。 SQLを表示 SHOW USER GRANT SELECT, UPDATE ON employees TO user1 WITH GRANT OPTION; CONNECT user1/password; GRANT...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3

### 問題ID 26963 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26963?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: データ・ディクショナリ・ビューの説明として正しいものはどれですか。
- 解説要約: データ・ディクショナリはデータベースに関する様々な管理情報が格納された読取り専用の表の集合です。 データ・ディクショナリ・ビューはデータ・ディクショナリ表のデータを参照するためのビューです。Oracle Databaseが管理するデータ・ディクショナリ表はほとんどのデータが暗号形式になっているため、人が読みやすい形式に変換されたデータ・ディクショナリ・ビューで管理情報を参照します。 以上より、 ・データ・ディクショナリ表のデータを参照するためのビューである が正解です。 その他の選択肢については以下のとおりです。 ・データベースに関する様々な管理情報が格納された読取り専用の表の集合である データ・ディクショナリ・ビューの基となるデータ・ディクショナリの説明なので、誤りです。 ・管理情報が格納されている論理的な記憶領域である データ・ディクショナリが格納されているSYSTEM表領域の説明なので、誤りです。 ・一般ユーザーは参照できない 接頭辞「ALL_」と「USER_」から始まるビューは一般ユーザーが参照できるので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/data-dictionary-and-dynamic-performance-views.html#CNCPT-GUID-6F1EA52F-C3AF-407C-B4FA-AE8C8651055E

### 問題ID 26964 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26964?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: 「*_TABLES」データ・ディクショナリ・ビューの説明として正しいものはどれですか。
- 解説要約: データ・ディクショナリ・ビューはデータ・ディクショナリ表のデータを参照するためのビューです。参照できるデータの範囲によって次の3つの接頭辞から始まる名前に分かれています。 同じ名前で接頭辞だけ異なるビューは共通のデータ・ディクショナリ表を参照します。 「USER_」から始まるビューは、問合せたユーザーが所有するオブジェクトの情報を表示します。上記2つのビューにある、所有者を示すOWNER列はありません。 「*_TABLES」は表の情報を表示します。 以上より、 ・USER_TABLESビューは問合せたユーザーが所有する表の情報を表示する が正解です。 その他の選択肢については以下のとおりです。 ・DBA_TABLES、ALL_TABLES、USER_TABLEビューはそれぞれ異なるデータ・ディクショナリ表を参照する 同じ名前で接頭辞だけ異なるビューは共通のデータ・ディクショナリ表を参照するので、誤りです。 ・DBA_TABLESビューは問合せたユーザーがアクセスできる表の情報を表示する 管理者権限で問合せでき、データベースの全ての表の情報を表示するので、誤りです。 ・ALL_TABLE...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/refrn/USER_TABLES.html
  - https://docs.oracle.com/cd/F19136_01/cncpt/data-dictionary-and-dynamic-performance-views.html#GUID-6F1EA52F-C3AF-407C-B4FA-AE8C8651055E

### 問題ID 26965 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26965?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: PINGTユーザーとしてプライベートシノニム「DEPT」を作成しました。デフォルトのアクセス権限でこのオブジェクトの情報を検索できる問合せはどれですか(2つ選択して下さい)。
- 解説要約: データ・ディクショナリ・ビューはデータ・ディクショナリ表のデータを参照するためのビューです。参照できるデータの範囲によって次の3つの接頭辞から始まる名前に分かれています。 選択肢の「*_SYNONYMS」はシノニムの情報を表示します。 設問のプライベートシノニムは作成したユーザーだけが使用できるので、所有者のPINGTユーザーとしてUSER_SYNONYMSビューを検索した場合に確認できます。 また、はSYSTEMユーザーなどの管理者権限で問合せできるDBA_SYNONYMSビューでは全てのシノニムを確認できます。 以上より、 ・PINGTユーザーとしてUSER_SYNONYMSを検索する ・SYSTEMユーザーとしてDBA_SYNONYMSを検索する が正解です。 以下は実行例です。 SQLを表示 SHOW USER SELECT * FROM user_synonyms; CONNECT system/[パスワード] SHOW USER SELECT owner, synonym_name FROM dba_synonyms WHERE synonym_name like '%DE...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/refrn/USER_SYNONYMS.html#GUID-D7528744-7201-45A6-9D52-F8A1A15DE2F2
  - https://docs.oracle.com/cd/F19136_01/refrn/DBA_SYNONYMS.html#GUID-A4B4EFAE-F979-4F78-A0B2-12EFDD22F25D
  - https://docs.oracle.com/cd/F19136_01/refrn/ALL_SYNONYMS.html#GUID-DCDB52FF-8339-4EDE-B36A-2E12AFE25D33

### 問題ID 26966 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26966?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: 動的パフォーマンス・ビューのシノニムの接頭辞はどれですか。
- 解説要約: 動的パフォーマンス・ビューは、データベースがOPEN（ユーザーがデータベースにアクセスできる状態）で使用されている間に動的に更新される仮想表です。 SYSユーザーが所有する「V_$」から始まる名前の動的パフォーマンス・ビューに対して、「V$」から始まるパブリックシノニムが作成されます。SYSユーザーか管理者権限を持つユーザーのみが動的パフォーマンス・ビューにアクセスできます。 主な動的パフォーマンス・ビューのパブリックシノニムには次のようなものがあります。 V$DATABASE：データベースに関する情報 V$PARAMETER：初期化パラメータに関する情報 V$SESSION：セッションに関する情報 V$DATAFILE：データファイルに関する情報 V$SQL：SQLの実行に関する情報 V$TABLESPACE：表領域に関する情報 以上より、 ・V$ が正解です。 例）「shared」を含む初期化パラメータ名を表示 SQLを表示 SELECT name FROM v$parameter WHERE name LIKE '%shared%'; その他の選択肢については以下のとおりです。 ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/data-dictionary-and-dynamic-performance-views.html#GUID-4093F62A-CA16-4054-B441-279D15CE03B3

### 問題ID 26967 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26967?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: 動的パフォーマンス・ビューの説明として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: 動的パフォーマンス・ビューは、データベースがOPEN（ユーザーがデータベースにアクセスできる状態）で使用されている間に動的に更新される仮想表です。 SYSユーザーが所有する「V_$」から始まる名前の動的パフォーマンス表に対して、ビューと「V$」から始まるパブリックシノニムが作成されます。 主な動的パフォーマンス・ビューのパブリックシノニムには次のようなものがあります。 V$DATABASE：データベースに関する情報 V$PARAMETER：初期化パラメータに関する情報 V$SESSION：セッションに関する情報 V$DATAFILE：データファイルに関する情報 V$SQL：実行されたSQLに関する統計情報 V$TABLESPACE：表領域に関する情報 動的パフォーマンス・ビューはデータベース管理者によるパフォーマンスの監視や、Oracle Enterprise Manager（システム管理ツール）によるデータベース情報の取得に使用されます。 以上より、 ・V$DATABASE、V$SESSIONなどのシノニムがある ・Oracle Enterprise Managerなどによって使用さ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/data-dictionary-and-dynamic-performance-views.html#GUID-4093F62A-CA16-4054-B441-279D15CE03B3

### 問題ID 26968 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26968?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: 動的パフォーマンス・ビューに格納される情報はどれですか(3つ選択して下さい)。
- 解説要約: 動的パフォーマンス・ビューは、データベースがOPEN（ユーザーがデータベースにアクセスできる状態）で使用されている間に動的に更新される仮想表です。 主な動的パフォーマンス・ビューのパブリックシノニムには次のようなものがあります。 V$DATABASE：データベースに関する情報 V$PARAMETER：初期化パラメータに関する情報 V$SESSION：セッションに関する情報 V$DATAFILE：データファイルに関する情報 V$SQL：実行されたSQLに関する統計情報 V$TABLESPACE：表領域に関する情報 以上より、 ・初期化パラメータに関する情報 ・セッションに関する情報 ・SQLの統計情報 が正解です。 例）「shared」を含む初期化パラメータ名を表示 SQLを表示 SELECT name FROM v$parameter WHERE name LIKE '%shared%'; その他の選択肢については以下のとおりです。 ・問合せたユーザーが所有する索引の情報 USER_INDEXESデータ・ディクショナリ・ビューの説明なので、誤りです。 ・問合せたユーザーがアクセスできる...
- 参考URL:
  - https://docs.oracle.com/cd/E82638_01/refrn/V-PARAMETER.html#GUID-C86F3AB0-1191-447F-8EDF-4727D8693754
  - https://docs.oracle.com/cd/E82638_01/refrn/V-SESSION.html#GUID-28E2DC75-E157-4C0A-94AB-117C205789B9
  - https://docs.oracle.com/cd/E82638_01/refrn/V-SQL.html#GUID-2B9340D7-4AA8-4894-94C0-D5990F67BE75

### 問題ID 26969 (データ・ディクショナリ・ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26969?q%5Binclude_reference%5D=1
- 問題傾向: データ・ディクショナリ・ビュー
- 問題文要約: 全てのデータ・ディクショナリ・ビューと動的パフォーマンス・ビューの名前と説明が格納されているビューの名前はどれですか。
- 解説要約: 全てのデータ・ディクショナリ・ビュー、動的パフォーマンス・ビューの名前と説明はDICTIONARYというビューに格納されています。 以上より、 ・DICTIONARY が正解です。 例）DICTIONARYビュー SQLを表示 DESC dictionary; SELECT * FROM dictionary ORDER BY table_name; その他の選択肢は全てデフォルトでは存在しません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/data-dictionary-and-dynamic-performance-views.html

### 問題ID 26970 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26970?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 現在のセッションのタイム・ゾーンを返す関数はどれですか。
- 解説要約: タイム・ゾーンとは同じ標準時（基準時刻との差）を扱う地域のことで、データベースにおいてはシステム運用の標準時を設定する項目です。 以下はデータベースのタイム・ゾーンや日時を返す関数です。 以上より、 ・SESSIONTIMEZONE が正解です。 ALTER SESSION文で現行セッションのタイム・ゾーンを変更できます。 タイム・ゾーンには「+09:00」のようなUTC（Coordinated Universal Time：協定世界時）との時間差（オフセット）か、「Asia/Tokyo」のようなタイム・ゾーン地域名を設定します。 SQLを表示 SELECT SESSIONTIMEZONE FROM dual; ALTER SESSION SET TIME_ZONE='America/New_York'; SELECT SESSIONTIMEZONE FROM dual; その他の選択肢については上表をご確認ください。 なお、SESSION_TIMEZONEという関数はありません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/SESSIONTIMEZONE.html#GUID-2A243878-C1C5-4B7C-81DE-D8B024796EAB

### 問題ID 26971 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26971?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: データベースが稼働しているOSの現在の日付・時刻を、DATE型の値に加え秒の小数点以下の値とタイム・ゾーンの情報も含めて返す関数はどれですか。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 SYSDATEがDATE型で現在の日時の秒までを返すのに対し、SYSTIMESTAMPはTIMESTAMP WITH TIME ZONEデータ型で返します。TIMESTAMP WITH TIME ZONEデータ型は、DATE型（世紀、年、月、日、時、分、秒）の値に加え秒の小数点以下の値とタイム・ゾーンの情報も含みます。 以上より、 ・SYSTIMESTAMP が正解です。 以下は実行例です。 SQLを表示 SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; SELECT SYSTIMESTAMP FROM dual; その他の選択肢については上表をご確認ください。 なお、SESSION_TIMEZONEという関数はありません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/SYSTIMESTAMP.html#GUID-FCED18CE-A875-4D5D-9178-3DE4FA956516

### 問題ID 26972 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26972?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: セッションのタイム・ゾーンの現在の日付・時刻をDATE型で返す関数はどれですか。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 以上より、 ・CURRENT_DATE が正解です。 SYSDATEがOSの日時を返すのに対し、CURRENT_DATEは現行セッションのタイム・ゾーン（SESSIONTIMEZONE）の日時を返します。 SQLを表示 SELECT SESSIONTIMEZONE FROM dual; SELECT TO_CHAR(CURRENT_DATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; ALTER SESSION SET TIME_ZONE='America/New_York'; SELECT SESSIONTIMEZONE FROM dual; SELECT TO_CHAR(CURRENT_DATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; その他の選択肢については上表をご確認ください。 なお、SESSION_DATEという関数はありません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CURRENT_DATE.html#GUID-96795097-D6F0-4288-90E7-9D7C49B4F6E5

### 問題ID 26973 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26973?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: セッションのタイム・ゾーンの現在の日付・時刻をTIMESTAMP WITH TIME ZONE型で返す関数はどれですか。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 以上より、 ・CURRENT_TIMESTAMP が正解です。 CURRENT_TIMESTAMPは現行セッションのタイム・ゾーン（SESSIONTIMEZONE）の日時をTIMESTAMP WITH TIME ZONEデータ型で返します。TIMESTAMP WITH TIME ZONEデータ型は、DATE型（世紀、年、月、日、時、分、秒）の値に加え秒の小数点以下の値とタイム・ゾーンの情報も含みます。 SQLを表示 SELECT SESSIONTIMEZONE FROM dual; SELECT CURRENT_TIMESTAMP FROM dual; その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CURRENT_TIMESTAMP.html#GUID-CBD42B84-869D-45C7-9FFC-001DD7712097

### 問題ID 26974 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26974?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: セッションのタイム・ゾーンの現在の日付・時刻をTIMESTAMP型で返す関数はどれですか。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 以上より、 ・LOCALTIMESTAMP が正解です。 LOCALTIMESTAMPは現行セッションのタイム・ゾーン（SESSIONTIMEZONE）の日時をTIMESTAMPデータ型で返します。TIMESTAMP型はDATE型を拡張したデータ型で、世紀、年、月、日、時、分、秒に加え秒の小数点以下の値を格納することができます。 SQLを表示 SELECT SESSIONTIMEZONE FROM dual; SELECT LOCALTIMESTAMP FROM dual; その他の選択肢については上表をご確認ください。 CURRENT_TIMESTAMPはTIMESTAMP WITH TIME ZONE型でタイム・ゾーンを含むので、誤りです。 なお、SESSION_TIMESTAMPという関数はありません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/LOCALTIMESTAMP.html#GUID-3C3D1F29-5F53-41F2-B2D6-A3767DFB22CA

### 問題ID 26975 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26975?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: ALTER SESSION文でセッションのタイム・ゾーンを変更します。次のSQL文の空欄に指定できる値の形式はどれですか(2つ選択して下さい)。 ALTER SESSION SET TIME_ZONE = '______________'
- 解説要約: タイム・ゾーンとは同じ標準時（基準時刻との差）を扱う地域のことで、データベースにおいてはシステム運用の標準時を設定する項目です。 タイム・ゾーンには「+09:00」のようなUTC（Coordinated Universal Time：協定世界時）との時間差（オフセット）か、「Asia/Tokyo」のようなタイム・ゾーン地域名を設定します。どちらの例も日本標準時を示します。 以上より、 ・+09:00 ・Asia/Tokyo が正解です。 「+09:00」は「9:00」のようにも記述できます。 以下は実行例です。 SQLを表示 SELECT SESSIONTIMEZONE FROM dual; ALTER SESSION SET TIME_ZONE='+09:00'; SELECT SESSIONTIMEZONE FROM dual; ALTER SESSION SET TIME_ZONE='Asia/Tokyo'; SELECT SESSIONTIMEZONE FROM dual; なお、TIME_ZONE句には以下のようにlocal（セッション開始時のローカルのタイム・ゾーン）やdb...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/ALTER-SESSION.html#GUID-DC7B8CDD-4F89-40CC-875F-F70F673711D4

### 問題ID 26976 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26976?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: ALTER SESSION文でセッションのタイム・ゾーンを変更します。次のSQL文の空欄に入る語句はどれですか。 ALTER SESSION SET ______________ = '+09:00'
- 解説要約: タイム・ゾーンとは同じ標準時（基準時刻との差）を扱う地域のことで、データベースにおいてはシステム運用の標準時を設定する項目です。 ALTER SESSION文で現行セッションのタイム・ゾーンを変更できます。 以上より、 ・TIME_ZONE が正解です。 以下は実行例です。 タイム・ゾーンには「+09:00」のようなUTC（Coordinated Universal Time：協定世界時）との時間差（オフセット）か、「Asia/Tokyo」のようなタイム・ゾーン地域名を設定します。どちらの例も日本標準時を示します。 SQLを表示 SELECT SESSIONTIMEZONE FROM dual; ALTER SESSION SET TIME_ZONE='+09:00'; SELECT SESSIONTIMEZONE FROM dual; ALTER SESSION SET TIME_ZONE='Asia/Tokyo'; SELECT SESSIONTIMEZONE FROM dual; その他の選択肢は全てALTER SESSION文に指定できない語句なので、誤りです。 なお、DBTI...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/ALTER-SESSION.html#GUID-DC7B8CDD-4F89-40CC-875F-F70F673711D4__GUID-9349F923-3015-46D3-9F58-3C2A1FE1B6B3

### 問題ID 26977 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26977?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: データベースが稼働しているOSの現在の日付・時刻をDATE型で返す関数はどれですか。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 以上より、 ・SYSDATE が正解です。 DATEデータ型には世紀、年、月、日、時、分、秒の値が格納されます。 「SELECT SYSDATE FROM dual;」でSYSDATE関数をそのまま問合せた場合は、初期化パラメータNLS_DATE_FORMATの書式で表示されます。日本語環境の場合は「RR-MM-DD」で日付しか表示されないので、TO_CHAR関数を使用して任意のフォーマットで表示します。 SQLを表示 SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/SYSDATE.html#GUID-807F8FC5-D72D-4F4D-B66D-B0FE1A8FA7D2

### 問題ID 26978 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26978?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: データ型のDATE型に格納される全ての情報の組合せはどれですか。
- 解説要約: 以下は日時を表すデータ型です。 以上より、 ・世紀、年、月、日、時、分、秒（小数点以下は含まない） が正解です。 以下は、データベースが稼働しているOSの現在の日付・時刻をDATE型で返すSYSDATE関数の問合せ結果です。 「SELECT SYSDATE FROM dual;」でSYSDATE関数をそのまま問合せた場合は、初期化パラメータNLS_DATE_FORMATの書式で表示されます。日本語環境の場合は「RR-MM-DD」で日付しか表示されないので、TO_CHAR関数を使用して任意のフォーマットで表示します。 SQLを表示 SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; その他の選択肢については以下のとおりです。 ・世紀、年、月、日、時、分、秒（小数点以下も含む） TIMESTAMP型です。 ・世紀、年、月、日、時、分、秒（小数点以下も含む）、タイム・ゾーン TIMESTAMP WITH TIME ZONE型です。 ・世紀、年、月、日 この情報だけが格納されるデータ型はありません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-789689BF-5682-4577-8ADE-8105C652CBB7

### 問題ID 26979 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26979?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: データ型のTIMESTAMP型に格納される全ての情報の組合せはどれですか。
- 解説要約: 以下は日時を表すデータ型です。 以上より、 ・世紀、年、月、日、時、分、秒（小数点以下も含む） が正解です。 以下はTIMESTAMP型の列を持つ表の例です。 SQLを表示 CREATE TABLE t1 (col TIMESTAMP); INSERT INTO t1 VALUES (SYSTIMESTAMP); SELECT * FROM t1; その他の選択肢については以下のとおりです。 ・世紀、年、月、日、時、分、秒（小数点以下は含まない） DATE型です。 ・世紀、年、月、日、時、分、秒（小数点以下も含む）、セッションのタイム・ゾーン TIMESTAMP WITH TIME ZONE型です。 ・世紀、年、月、日、時 この情報だけが格納されるデータ型はありません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-CD2954CE-45E2-4938-A599-CCB96879510F

### 問題ID 26980 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26980?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: データ型のTIMESTAMP WITH TIME ZONE型の説明として正しいものはどれですか。
- 解説要約: 以下は日時を表すデータ型です。 TIMESTAMP WITH TIME ZONEデータ型は、TIMESTAMP型の値に加えセッションのタイム・ゾーンの情報も含みます。 以上より、 ・TIMESTAMP型の値に加えてセッションのタイム・ゾーンを格納する が正解です。 以下はTIMESTAMP WITH TIME ZONE型の列を持つ表の例です。 SQLを表示 SELECT DBTIMEZONE FROM dual; SELECT SESSIONTIMEZONE FROM dual; CREATE TABLE t1 (col TIMESTAMP WITH TIME ZONE); INSERT INTO t1 VALUES (SYSTIMESTAMP); SELECT * FROM t1; その他の選択肢については以下のとおりです。 ・データベースのタイム・ゾーンに変換されたTIMESTAMP型の日時を格納する ・データ検索時にはクライアントのセッションのタイム・ゾーンに変換された日時を返す これらはTIMESTAMP WITH LOCAL TIME ZONEの説明なので、誤りです。 TIM...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-5BC5D2C1-6506-49BE-8177-F743A46FDC09

### 問題ID 26981 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26981?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: データ型のTIMESTAMP WITH LOCAL TIME ZONE型の説明として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: 以下は日時を表すデータ型です。 TIMESTAMP WITH LOCAL TIME ZONEデータ型は、タイム・ゾーンの情報を含みません。 また、データの検索時にはクライアントのローカルセッションのタイム・ゾーンに変換された値を返します。 以上より、 ・データベースのタイム・ゾーンに変換された日時を格納する ・データ検索時にはクライアントのセッションのタイム・ゾーンに変換された日時を返す が正解です。 以下はTIMESTAMP WITH LOCAL TIME ZONE型の列を持つ表の例です。 SQLを表示 SELECT DBTIMEZONE FROM dual; SELECT SESSIONTIMEZONE FROM dual; CREATE TABLE t2 (col TIMESTAMP WITH LOCAL TIME ZONE); INSERT INTO t2 VALUES (SYSTIMESTAMP); SELECT SYSTIMESTAMP FROM dual; SELECT * FROM t2; ALTER SESSION SET TIME_ZONE='-05:00'; SE...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-3F1C388E-C651-43D5-ADBC-1A49E5C2CA05

### 問題ID 26982 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26982?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 2つの日時の期間を、年、月の単位で格納するデータ型はどれですか。
- 解説要約: 以下は期間を表すデータ型です。 INTERVAL YEAR TO MONTH型は期間を年、月の単位で格納します(「5年6カ月」など)。 以上より、 ・INTERVAL YEAR TO MONTH が正解です。 INTERVAL YEAR TO MONTH型に値を格納するには、以下のような期間リテラルを使用します。 ・INTERVAL '5-6' YEAR TO MONTH：5年6ヶ月 ・INTERVAL '100' YEAR(3)：100年 ・INTERVAL '300' MONTH(3)：300ヶ月 ※年や月の精度が2桁より大きい場合は、YEAR(3)などのように精度を指定します。 その他の選択肢については以下のとおりです。 ・INTERVAL DAY TO SECOND 2つの日時の期間を、日、時、分、秒の単位で格納するデータ型なので、誤りです。 ・TIMESTAMP ・TIMESTAMP WITH TIME ZONE ・TIMESTAMP WITH LOCAL TIME ZONE これらは日時を表すデータ型なので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-517CEB46-C6FA-4B94-9299-5BBB5A58CF7B

### 問題ID 26983 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26983?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 2つの日時の期間を、日、時、分、秒の単位で格納するデータ型はどれですか。
- 解説要約: 以下は期間を表すデータ型です。 INTERVAL DAY TO SECOND型は期間を日、時、分、秒の単位で格納します(「10日と12時間30分30秒」など)。 以上より、 ・INTERVAL DAY TO SECOND が正解です。 INTERVAL DAY TO SECOND型に値を格納するには、以下のような期間リテラルを使用します。 ・INTERVAL '10 12:30:30' DAY TO SECOND：10日と12時間30分30秒 ・INTERVAL '10 12:30:30.555555' DAY TO SECOND：10日と12時間30分30.555555秒 ※SECOND(秒フィールド)には秒の小数点以下も格納できます その他の選択肢については以下のとおりです。 ・INTERVAL YEAR TO MONTH 2つの日時の期間を、年、月の単位で格納するデータ型なので、誤りです。 ・DATE 世紀、年、月、日、時、分、秒（小数点以下は含まない）を格納するデータ型なので、誤りです。 ・TIMESTAMP 世紀、年、月、日、時、分、秒（小数点以下を含む）を格納するデータ型な...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-FD8C41B7-8CDC-4D02-8E6B-5250416BC17D

### 問題ID 26984 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26984?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 現行セッションのタイム・ゾーンの現在の日時を返す関数はどれですか(3つ選択して下さい)。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 以上より、 ・CURRENT_DATE ・CURRENT_TIMESTAMP ・LOCALTIMESTAMP が正解です。 CURRENT_DATEがDATE型で現在の日時の秒までを返すのに対し、CURRENT_TIMESTAMPはTIMESTAMP WITH TIME ZONEデータ型で返します。 SQLを表示 SELECT SESSIONTIMEZONE FROM dual; SELECT TO_CHAR(CURRENT_DATE, 'RR-MM-DD HH24:MI:SS') FROM dual; SELECT CURRENT_TIMESTAMP FROM dual; LOCALTIMESTAMPはTIMESTAMP型で返し、CURRENT_TIMESTAMPのようにタイム・ゾーンの情報は含みません。 SQLを表示 SELECT LOCALTIMESTAMP FROM dual; その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CURRENT_DATE.html
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CURRENT_TIMESTAMP.html
  - https://docs.oracle.com/cd/F19136_01/sqlrf/LOCALTIMESTAMP.html#GUID-3C3D1F29-5F53-41F2-B2D6-A3767DFB22CA

### 問題ID 26985 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26985?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: OSの現在の日時を返す関数はどれですか(2つ選択して下さい)。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 SYSDATEとSYSTIMESTAMPはデータベースが稼働するOSの現在の日時を返します。 以上より、 ・SYSDATE ・SYSTIMESTAMP が正解です。 SYSDATEがDATE型で現在の日時の秒までを返すのに対し、SYSTIMESTAMPはTIMESTAMP WITH TIME ZONEデータ型で返します。TIMESTAMP WITH TIME ZONEデータ型は、DATE型の値に加え秒の小数点以下の値とタイム・ゾーンの情報も含みます。 SQLを表示 SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM dual; SELECT SYSTIMESTAMP FROM dual; その他の選択肢については上表をご確認ください。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/SYSDATE.html#GUID-807F8FC5-D72D-4F4D-B66D-B0FE1A8FA7D2
  - https://docs.oracle.com/cd/F19136_01/sqlrf/SYSTIMESTAMP.html#GUID-FCED18CE-A875-4D5D-9178-3DE4FA956516

### 問題ID 26986 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26986?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 関数の説明として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 タイム・ゾーンには「+09:00」のようなUTC（Coordinated Universal Time：協定世界時）との時間差（オフセット）か、「Asia/Tokyo」のようなタイム・ゾーン地域名を設定します。 CURRENT_DATEはDATE型、LOCALTIMESTAMPはTIMESTAMP型で値を返し、タイム・ゾーンの情報は含みません。 以上より、 ・DBTIMEZONEとSESSIONTIMEZONEにはUTCとのオフセットかタイム・ゾーン地域名を設定できる ・CURRENT_DATEとLOCALTIMESTAMPはタイム・ゾーンを含まない が正解です。 その他の選択肢については以下のとおりです。 ・SYSTIMESTAMPとCURRENT_DATEは同じデータ型で値を返す SYSTIMESTAMP（OSの現在の日時）はTIMESTAMP WITH TIME ZONE型で、CURRENT_DATE（セッションのタイム・ゾーンの現在の日時）はDATE型で返すので、誤りです。 ・SYSDATEとCURRENT_TIMEST...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-2AF15A96-CD19-4074-8DE6-17BAD0D7DF37
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CURRENT_DATE.html#GUID-96795097-D6F0-4288-90E7-9D7C49B4F6E5
  - https://docs.oracle.com/cd/F19136_01/sqlrf/LOCALTIMESTAMP.html

### 問題ID 26987 (集合演算子)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26987?q%5Binclude_reference%5D=1
- 問題傾向: 集合演算子
- 問題文要約: 次のSQL文を実行した結果の説明として正しい記述はどれですか。 SELECT 1, 'First' FROM dual INTERSECT SELECT 1 AS num, 'First' AS str FROM dual INTERSECT SELECT 1, 'First' FROM dual;
- 解説要約: INTERSECT演算子を用いた複合問合せでは、2つの問合せの結果の共通する行を表示します。 INTERSECT演算子を複数使用して3つ以上の問合せの共通する行を表示することも可能です。設問のSQLでは3つのSELECT文でDUAL表から「1」と「First」という共通の値を問合せています。よって、1行のデータが返されます。 以上より、 ・1行が返される が正解です。 以下は実行例です。 SQLを表示 SELECT 1, 'First' FROM dual INTERSECT SELECT 1 AS num, 'First' AS str FROM dual INTERSECT SELECT 1, 'First' FROM dual; その他の選択肢については以下のとおりです。 ・0行が返される ・3行が返される 3つのSELECT文に共通の1行が返されるので、誤りです。 ・2つ目の問合せの列名が異なるので、エラーになる 列数を同数にする必要がありますが、列名は異なっていても構いませんので誤りです。 ・複数のINTERSECT演算子を使用できないので、エラーになる 複数のINTERSE...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Set-Operators.html

### 問題ID 26988 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26988?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: マルチテーブル・インサートの説明として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: マルチテーブル・インサートは、1つのSQL文で複数の表にデータを追加できる機能です。 通常のINSERT文では1文につき1行ずつ挿入しますが、マルチテーブル・インサートでは副問合せで返される複数の行を1つ以上の表に挿入できます。無条件のマルチテーブル・インサートと、条件付きのマルチテーブル・インサートがあります。 条件付きのマルチテーブル・インサートのうちINSERT FIRSTでは、副問合せで返される行が順番にWHEN句の条件式で評価され、最初に条件に合致したWHEN句に対応するINTO句で挿入されます。その後のWHEN句はスキップされます。つまり、最初に条件に合致した表に挿入されます。 以上より、 ・副問合せで返される行を挿入する ・条件付きのINSERT FIRSTは最初に条件に合致した表に挿入する が正解です。 以下に、副問合せでEMPLOYEES表のEMPLOYEE_ID列（従業員番号）とSALARY列（給与）を参照し、WHEN句のそれぞれの条件に合致した給与等級の表（GRADE_A～GRADE_E表）に挿入する例を示します。 INSERT FIRSTでは最初に条件に合致した...
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/INSERT.html#GUID-903F8043-0254-4EE9-ACC1-CB8AC0AF3423__GUID-A375FB35-7EE9-4FF3-98BD-E58087EA1C6E

### 問題ID 26989 (DML文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26989?q%5Binclude_reference%5D=1
- 問題傾向: DML文
- 問題文要約: 以下の順番でSQL文を実行しました。トランザクションが開始されるSQL文はどれですか(3つ選択して下さい)。
- 解説要約: トランザクションは、Oracle Database接続後、または直前のトランザクションの終了後、最初のデータを操作するSQL文（通常のSELECT文は除く）実行時に開始され、下記のいずれかによって終了します。 ・COMMIT文またはROLLBACK文の実行 ・DDL文の実行 ・DCL文の実行 ・SQL DeveloperやSQL*Plusの終了 ・システム障害の発生 ⑤はSELECT文にFOR UPDATE句を指定することで検索対象となる行に排他ロックをかけることができ、トランザクションが開始されます。通常のSELECT文の実行時はロックをかけず、トランザクションは開始されません。 よって、設問の実行結果でトランザクションが開始されるのは CREATE TABLE文（DDL文）の後のINSERT文 --- ① COMMIT文の後のDELETE文 --- ③ ROLLBACK文の後のSELECT ～ FOR UPDATE文 --- ⑤ です。 以上より、 ・① ・③ ・⑤ が正解です。 その他の選択肢については以下のとおりです。 ・② ・④ これらはトランザクションが終了するSQL文なの...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/cncpt/transactions.html

### 問題ID 26990 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26990?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: PINGTユーザーとして次のSQL文を実行しました。 CREATE SEQUENCE seq_id MAXVALUE 100; CREATE TABLE list ( id NUMBER(3) DEFAULT seq_id.NEXTVAL PRIMARY KEY, name VARCHAR2(10) ); GRANT SELECT, INSERT ON list TO userA; この後、userAユーザーとしてLIST表にデータを挿入する際の説明として正しいものはどれですか。
- 解説要約: 設問のSQL文では順序SEQ_IDを作成し、LIST表のID列のデフォルト値にNEXTVAL疑似列を指定しています。データの追加時にID列への値の入力が省略された場合に、順序SEQ_IDの一意な順序値が列に格納されます。 GRANT文では、userAユーザーにLIST表へのデータの参照と挿入に必要なオブジェクト権限を付与しています。これでuserAユーザーはPINGTユーザーのLIST表にデータを挿入することは可能です。ただし、ID列の値を省略する場合は順序SEQ_IDが使用されるので、順序SEQ_IDを参照するためのSELECTオブジェクト権限かSELECT ANY SEQUENCE権限が必要になります。 以上より、 ・ID列の値を省略する場合は、順序SEQ_IDを参照する権限が必要である が正解です。 以下は実行例です。 その他の選択肢については以下のとおりです。 ・このまま、ID列の値を省略してLIST表へデータを挿入できる userAユーザーには順序SEQ_IDを参照するための権限（SELECTオブジェクト権限かSELECT ANY SEQUENCE権限）が付与されていないので...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Sequence-Pseudocolumns.html#GUID-693B576A-191D-45F5-B7CB-88D0EA821B44

### 問題ID 26991 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26991?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 次のSQL文を実行しました。 CREATE SEQUENCE seq_id MAXVALUE 100; CREATE TABLE list ( id NUMBER(3) DEFAULT seq_id.NEXTVAL PRIMARY KEY, name VARCHAR2(10) ); DROP SEQUENCE seq_id; この後、LIST表にデータを挿入する際の説明として正しい記述はどれですか。
- 解説要約: 設問のSQL文では順序SEQ_IDを作成し、LIST表のID列のデフォルト値にNEXTVAL疑似列を指定し、その後、順序SEQ_IDを削除しています。列のデフォルト値はデータの追加時にその列への値の入力が省略された場合に格納されるものなので、順序SEQ_IDが無いとエラーになります。 SQLを表示 CREATE SEQUENCE seq_id MAXVALUE 100; CREATE TABLE list ( id NUMBER(3) DEFAULT seq_id.NEXTVAL PRIMARY KEY, name VARCHAR2(10)); DROP SEQUENCE seq_id; INSERT INTO list (name) VALUES ('Sato'); INSERT INTO list VALUES (10, 'Sato'); 以上より、 ・ID列の値を省略すると、順序が無いのでエラーになる が正解です。 その他の選択肢については以下のとおりです。 ・ID列の値を省略すると、NULLが格納される ・ID列の値を省略すると、1が格納される 値は格納されず上記の実行例のエラ...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Sequence-Pseudocolumns.html#GUID-693B576A-191D-45F5-B7CB-88D0EA821B44

### 問題ID 26992 (索引、シノニムおよびシーケンス)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26992?q%5Binclude_reference%5D=1
- 問題傾向: 索引、シノニムおよびシーケンス
- 問題文要約: 索引に関する説明として、正しいものはどれですか。
- 解説要約: 表に索引を作成する権限であるINDEXオブジェクト権限かCREATE ANY INDEXシステム権限があれば、別のユーザーが所有する表に対しても索引を作成できます。「スキーマ名.表名」のように表名の前にスキーマ名をつけて、別ユーザーの表を参照します。 ※スキーマとは、オブジェクトの所有者を表す論理的な概念です。 以上より、 ・別のユーザーが所有する表に対しても索引を作成できる が正解です。 以下は実行例です。 SQLを表示 CREATE INDEX ind_userA ON userA.departments(manager_id); SELECT index_name, table_owner FROM user_indexes WHERE index_name = 'IND_USERA'; その他の選択肢については以下のとおりです。 ・表と索引の所有者は同じでなければならない 上記の解説のように表と索引の所有者が異なる場合もあるので、誤りです。 ・CREATE TABLE文では索引を作成できない CREATE TABLE文のPRIMARY KEY制約またはUNIQUE制約を定義する...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/admin/managing-indexes.html

### 問題ID 26993 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26993?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: DEPARTMENTS表の構造とデータを確認して下さい。 次のSQL文のWHERE句の条件で、データが1件も検索されないものはどれですか。 SELECT * FROM departments WHERE _________________;
- 解説要約: DEPARTMENT_ID列は数値なので「department_id = 1」と指定するべきですが、Oracle Databaseではデータ型の変換が意味を持つ場合に、自動的にデータ型の変換が行われます(暗黙的なデータ変換といいます)。 選択肢の条件を1つずつ確認します。 ・TO_CHAR(department_id) = '01' DEPARTMENT_ID列の数値をTO_CHAR関数で文字列に変換して'01'という文字列に一致する値が検索されます。格納されている数値「1」は文字列'1'になるので一致せず検索されません。 SQLを表示 SELECT * FROM departments WHERE TO_CHAR(department_id) = '01'; ・TO_CHAR(department_id) = '1' DEPARTMENT_ID列の数値をTO_CHAR関数で文字列に変換して'1'という文字列に一致する値が検索されます。格納されている数値「1」は文字列'1'になるので一致して検索されます。 SQLを表示 SELECT * FROM departments WHERE T...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Data-Type-Comparison-Rules.html#GUID-98BE3A78-6E33-4181-B5CB-D96FD9DC1694

### 問題ID 26994 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26994?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 次のSQL文を実行しました。 CREATE TABLE t1 (id NUMBER(2), text VARCHAR2(10)); INSERT INTO t1 VALUES (1, 'aaa'); ALTER TABLE t1 SET UNUSED (text); ALTER TABLE t1 READ ONLY; この後、T1表に対して実行できるSQL文はどれですか(3つ選択して下さい)。
- 解説要約: 設問のSQL文ではT1表を作成してデータを挿入後、ALTER TABLE文のSET UNUSED句でTEXT列を未使用にしています。また、最後のALTER文でT1表をREAD ONLY（読取り専用モード）に変更しています。 読取り専用モードの表にはデータの追加、更新、削除などのDML文は実行できませんが、表の削除や未使用の列の削除などデータを更新しないDDL文は実行できます。また、表に対する索引の操作も行えます。 以上より、 ・SELECT * FROM t1; ・CREATE INDEX idx_id ON t1 (id); ・ALTER TABLE t1 DROP UNUSED COLUMNS; が正解です。 なお、列にUNUSEDマークを設定して未使用にするALTER TABLE文のSET UNUSED句は読取り専用モードでは実行できません。設問のように読取り専用モードに変更する前にUNUSEDマークを設定する必要があります。 以下は実行例です。 SQLを表示 CREATE TABLE t1 (id NUMBER(2), text VARCHAR2(10)); INSERT IN...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/ALTER-TABLE.html
  - https://docs.oracle.com/cd/F19136_01/admin/managing-tables.html#GUID-E41130FA-C2C6-4CA0-922B-A3281632B65B

### 問題ID 26995 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26995?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: ALTER TABLE文のSET UNUSED句について、正しい記述はどれですか。
- 解説要約: ALTER TABLE文で既存の表の列を削除できますが、列の削除中は表にロックがかかり、列に多くのデータが含まれている場合は削除に時間がかかります。多くのユーザーがデータベースを利用する時間帯に負荷の高い削除処理を行いたくない場合、削除したい列にUNUSEDマークを設定して未使用にできます。 ALTER TABLE 表名 SET UNUSED ( 列名 [, 列名...]) [CASCADE CONSTRAINTS]; ※1つの列のみUNUSEDにする場合は、次の構文も使用できます。 ALTER TABLE 表名 SET UNUSED COLUMN 列名 [CASCADE CONSTRAINTS]; SET UNUSED句に関しては、以下の注意事項があります。 ・UNUSEDに設定した列は戻せず、DESCRIBEコマンドなどで列名やデータ型を確認できなくなる ・UNUSEDにした列に作成された索引や制約は削除される ・UNUSEDにした列と同じ名前の列を表に追加できる ・UNUSEDにした列の表名と列数は「USER_UNUSED_COL_TABS」ディクショナリで確認できる ・表に対し...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/vldbg/partition-concepts.html#GUID-DD6FC751-735F-48EF-BFC6-F636C2451701

### 問題ID 26996 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26996?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: 制約を定義する際のDEFERRABLE句の説明として正しいものはどれですか(2つ選択して下さい)。
- 解説要約: CREATE TABLE文のDEFERRABLE句では、制約のチェックをDML文単位ではなくトランザクション単位に遅延する遅延制約を設定します。制約のチェックを遅延させることで、参照整合性制約のデータの順番を気にせずに挿入することができます。 [列レベル制約] CREATE TABLE [スキーマ名].表名 ( 列名 データ型 [[CONSTRAINT 制約名] 制約の種類 [DEFERRABLE [INITIALLY IMMEDIATE|DEFERRED]]] [,列名 データ型 [[CONSTRAINT 制約名] 制約の種類 [DEFERRABLE [INITIALLY IMMEDIATE|DEFERRED]]]] … ) [表レベル制約] CREATE TABLE [スキーマ名].表名 ( 列名 データ型 [,列名 データ型] … [, [CONSTRAINT 制約名] 制約の種類 (列名 [,列名 …]) [DEFERRABLE [INITIALLY IMMEDIATE|DEFERRED]]] [, [CONSTRAINT 制約名] 制約の種類 (列名 [,列名 …]) [DE...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/constraint.html#GUID-1055EA97-BA6F-4764-A15F-1024FD5B6DFE__GUID-4056A42A-397D-4B33-BAE5-C93411256246

### 問題ID 26997 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26997?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: SYSTEMユーザーとして新たにTESTユーザーを作成し、CREATE SESSIONシステム権限を付与しました。 他のシステム権限も付与してTESTユーザーがいくつかの操作を行えるようにします。次のうち、システム権限のみでは行えない操作または適切な答えはどれですか。
- 解説要約: 主なシステム権限は次のとおりです。 選択肢の操作を1つずつ確認します。 ・PINGTユーザーの表を検索する TESTユーザーにSELECT ANY TABLEシステム権限を付与すれば、任意のスキーマの表を検索できます。 オブジェクト権限の場合は、PINGTユーザーから表に対するSELECTオブジェクト権限をTESTユーザーに付与します。 ・PINGTユーザーの表のデータをTRUNCATE文で削除する TESTユーザーにDROP ANY TABLEシステム権限を付与すれば、任意のスキーマの表の行をTRUNCATE文で削除（切捨て）できます。 ・PINGTユーザーのプロシージャを実行する TESTユーザーにEXECUTE ANY PROCEDUREシステム権限を付与すれば、任意のスキーマのプロシージャ（Oracle独自のプログラミング言語であるPL/SQLで記述されたプログラム）を実行できます。 オブジェクト権限の場合は、PINGTユーザーからプロシージャに対するEXECUTEオブジェクト権限をTESTユーザーに付与します。 以上より、選択肢の操作はシステム権限のみで行えますので ・全ての...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3__BABEFFEE

### 問題ID 26998 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26998?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(2つ選択して下さい)。 1. SYSTEMユーザーとして実行 GRANT SELECT ANY TABLE TO test WITH ADMIN OPTION; 2. TESTユーザーとして実行 GRANT SELECT ANY TABLE TO test2 WITH ADMIN OPTION; 3. SYSTEMユーザーとして実行 REVOKE SELECT ANY TABLE FROM test;
- 解説要約: 1.のGRANT文にはWITH ADMIN OPTION句が指定されているので、システム権限を付与されたユーザーが他のユーザーに対してシステム権限を付与できるようになります。 そのため、2.ではTESTユーザーからTEST2ユーザーに対してシステム権限を付与しています。 3.のREVOKE文ではTESTユーザーからシステム権限を取消していますが、TEST2ユーザーに付与されたシステム権限はそのまま残ります。 以上より、 ・TESTユーザーからSELECT ANY TABLEシステム権限が取消された ・TEST2ユーザーのSELECT ANY TABLEシステム権限は付与されたままである が正解です。 以下は実行例です。 SQLを表示 GRANT SELECT ANY TABLE TO test WITH ADMIN OPTION; SQLを表示 SHOW USER SELECT privilege, admin_option FROM user_sys_privs; GRANT SELECT ANY TABLE TO test2 WITH ADMIN OPTION; SQLを表示 RE...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-6F401301-B5EA-482E-9615-21FD840CAF60
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-6D899DDC-C7E6-47C9-A0EE-577792A7FA68

### 問題ID 26999 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/26999?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: 次の順番でSQL文を実行した時の説明として、正しいものはどれですか(2つ選択して下さい)。 1. PINGTユーザーとして実行 GRANT SELECT ON departments TO test WITH GRANT OPTION; 2. TESTユーザーとして実行 GRANT SELECT ON pingt.departments TO test2 WITH GRANT OPTION; 3. PINGTユーザーとして実行 REVOKE SELECT ON departments FROM test;
- 解説要約: 1.のGRANT文にはWITH GRANT OPTION句が指定されているので、オブジェクト権限を付与されたユーザーが他のユーザーに対してオブジェクト権限を付与できるようになります。 そのため、2.ではTESTユーザーからTEST2ユーザーに対して、PINGTユーザー所有のDEPARTMENTS表へのSELECTオブジェクト権限を付与しています。 3.のREVOKE文ではPINGTユーザーがTESTユーザーからDEPARTMENTS表へのSELECTオブジェクト権限を取消しています。この場合、TESTユーザーからTEST2ユーザーに付与されたオブジェクト権限も取消されます。WITH GRANT OPTION付きでオブジェクト権限を付与されたユーザーが付与したオブジェクト権限は、取消し時に連鎖的に取消されます。 以上より、 ・TESTユーザーからSELECTオブジェクト権限が取消された ・TEST2ユーザーからもSELECTオブジェクト権限が取消された が正解です。 以下は実行例です。 SQLを表示 GRANT SELECT ON departments TO test WITH GRA...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-8AB43A10-FD9E-4B08-9C23-71C5A15DE1FC
  - https://docs.oracle.com/cd/F19136_01/dbseg/configuring-privilege-and-role-authorization.html#GUID-613278F9-90CE-4B61-8465-B2BD22C175C1

### 問題ID 27000 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/27000?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: ユーザーに現在付与されているシステム権限を確認できるデータ・ディクショナリ・ビューはどれですか。
- 解説要約: ユーザーに付与されたシステム権限はUSER_SYS_PRIVSデータ・ディクショナリ・ビューで確認できます。 以上より、 ・USER_SYS_PRIVS が正解です。 以下は実行例です。 SQLを表示 GRANT SELECT ANY TABLE TO test WITH ADMIN OPTION; SQLを表示 SHOW USER SELECT privilege, admin_option FROM user_sys_privs; その他の選択肢については以下のとおりです。 ・USER_TAB_PRIVS ユーザーが所有するまたは付与されたオブジェクト権限を表示するデータ・ディクショナリ・ビューなので、誤りです。 ・V$SESSION セッションに関する情報を表示する動的パフォーマンス・ビュー（データベースがOPENで使用されている間に動的に更新される仮想表）なので、誤りです。 ・USER_GRANT_PRIVS このようなデータ・ディクショナリ・ビューは存在しません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/refrn/USER_SYS_PRIVS.html#GUID-8DEB9EB1-71F4-4FB2-9643-EED53259F3C3

### 問題ID 27001 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/27001?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: ユーザーに現在付与されているオブジェクト権限を確認できるデータ・ディクショナリ・ビューはどれですか。
- 解説要約: ユーザーが付与またはユーザに付与されたオブジェクト権限はUSER_TAB_PRIVSデータ・ディクショナリ・ビューで確認できます。 以上より、 ・USER_TAB_PRIVS が正解です。 以下は実行例です。 SQLを表示 GRANT SELECT ON departments TO test WITH GRANT OPTION; SQLを表示 SHOW USER SELECT grantor, owner, table_name, privilege, grantable FROM user_tab_privs; その他の選択肢については以下のとおりです。 ・USER_SYS_PRIVS ユーザーに付与されているシステム権限を確認できるデータ・ディクショナリ・ビューなので、誤りです。 ・USER_GRANT_PRIVS ・USER_OBJECT_PRIVS これらのようなデータ・ディクショナリ・ビューは存在しません。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/refrn/USER_TAB_PRIVS.html#GUID-C0EAE1FC-AAA6-4846-8009-35189BD72F2D

### 問題ID 27002 (データの制限およびソート)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/27002?q%5Binclude_reference%5D=1
- 問題傾向: データの制限およびソート
- 問題文要約: 次のコマンドの説明として正しいものはどれですか(3つ選択して下さい)。 SET VERIFY OFF
- 解説要約: 置換変数を使用したSQL文実行時に、置換変数を値と置き換える前後のSQL文を表示するかしないかは以下のコマンドで設定します。 SET VERIFY {ON|OFF} 設問の「SET VERIFY OFF」は、置換前後のSQL文を表示しません。 このVERIFYコマンドや置換変数はSQL*PlusやSQL Developerなどのツールで利用できます。 以上より、 ・置換変数を使用したSQL文実行時に、置換変数と指定した値を置き換える前後のSQL文を表示しない ・SQL*Plusで実行できる ・SQL Developerで実行できる が正解です。 以下はSQL*Plusでの実行例です。 その他の選択肢については以下のとおりです。 ・置換変数を使用したSQL文実行時に、置換変数と指定した値を置き換える前後のSQL文を表示する 「SET VERIFY ON」の説明なので、誤りです。 ・SQL文の構文チェックを行わない SQL*PlusなどのツールでSQL文の構文チェックを行わないようにすることはできませんので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqpug/SET-system-variable-summary.html#GUID-74CA1665-165D-4C0D-BBB2-681BD3485211

### 問題ID 27003 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/27003?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: PINGTユーザーとして以下の順番でSQL文を実行しました。この後TESTユーザーとしてV_VIEW1ビューを参照する場合の説明として、正しいものはどれですか。 ① CREATE OR REPLACE VIEW v_view1 AS SELECT employee_id, employee_name FROM employees; ② GRANT SELECT ON v_view1 TO test; ③ CREATE OR REPLACE VIEW v_view1 AS SELECT department_id, department_name FROM departments;
- 解説要約: 設問の①では、EMPLOYEES表からEMPLOYEE_IDとEMPLOYEE_NAMEを取り出したビューV_VIEW1を作成しています。 ②では、ビューV_VIEW1に対するSELECTオブジェクト権限をTESTユーザーに付与しています。この時点でTESTユーザーはビューV_VIEW1のデータを参照できます。 ③では、CREATE OR REPLACE VIEW文で既存のビューV_VIEW1の定義を置き換えて、DEPARTMENTS表からDEPARTMENT_IDとDEPARTMENT_NAMEを取り出しています。 CREATE OR REPLACE VIEW文でビューの定義を置き換えた場合、このビューに対するオブジェクト権限(特定のデータベース・オブジェクトへの操作を許可するための権限)はそのまま保持されるため、再度オブジェクト権限を付与する必要はありません。 以上より、 ・このままTESTユーザーは③のV_VIEW1ビューを参照できる が正解となります。 以下は実行例です。 その他の選択肢については以下のとおりです。 ・再度TESTユーザーにV_VIEW1に対するSELECT権限...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/CREATE-VIEW.html#GUID-61D2D2B4-DACC-4C7C-89EB-7E50D9594D30__GUID-4FEC4525-B779-43EF-8EC5-CAF739F36CC5

### 問題ID 27004 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/27004?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: Ping-tはIT系の資格の学習サイトです。サイトに会員登録したユーザが様々なWEB問題集(コンテンツ)を学習に利用できます。 Ping-t登録ユーザとWEB問題集の関係をERモデル(概念モデル)として設計した場合の説明として正しいものはどれですか(2つ選択して下さい。) ただし、以下の条件とします。 ・Ping-t登録ユーザを「ユーザ」エンティティ、WEB問題集を「問題集」エンティティとする ・1人の登録ユーザは1つ以上～複数の問題集を学習する ・1つの問題集は複数のユーザが受講する
- 解説要約: ERモデル(Entity-Relationship Model)は「データベースにどのような表を作成するか」といった、リレーショナル・データベースの設計において主に使用されている手法です。 データベースで管理したい現実世界の対象を「エンティティ(実体)」、「アトリビュート(属性)」、「リレーションシップ(関連)」という3つの構成要素で表現した概念データモデルを作成し、最終的には以下のような対応でリレーショナル・データベースに実装します。 ・エンティティ(実体) → 表 ・アトリビュート(属性) → 列 ・リレーションシップ(関連) → 外部キー 設問の条件より、ER図は以下のようになります。表に格納するデータの例も示します。 「ユーザ」エンティティと「問題集」エンティティ間には「多対多」の関係が成り立ちます。 2次元の表形式で格納するリレーショナル・モデル(リレーショナル・データベースで管理するための論理モデル)では「多対多」の関連を扱うことができません。よって、「多対多」の関連の間に中間テーブルと呼ばれるエンティティを追加して「1対多」の関係になるようにします。 以上より、 ・「ユー...
- 参考URL:
  - https://qiita.com/ramuneru/items/db43589551dd0c00fef9

### 問題ID 27005 (リレーショナル・データベース)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/27005?q%5Binclude_reference%5D=1
- 問題傾向: リレーショナル・データベース
- 問題文要約: 以下はPing-t登録ユーザとWEB問題集の関係をERモデル(概念モデル)化したER図です。 以下の条件とします。 ・Ping-t登録ユーザを「ユーザ」エンティティ、WEB問題集を「問題集」エンティティとする ・「ユーザ」エンティティの主キーは「ユーザID」で、「問題集」エンティティの主キーは「問題集ID」とする ・1人の登録ユーザは1つ以上～複数の問題集を学習する ・1つの問題集は複数のユーザが受講する 「ユーザ」エンティティと「問題集」エンティティ間の「多対多」の関連を解消してリレーショナル・モデルへ変換するため、以下のように中間テーブルである「学習」エンティティを追加しました。 この場合...
- 解説要約: 2次元の表形式で格納するリレーショナル・モデルでは「多対多」の関連を扱うことができません。よって、「多対多」の関連の間に中間テーブルと呼ばれるエンティティを追加して「1対多」の関係になるようにします。 次の例では中間テーブル「学習」エンティティを追加して、それぞれの表と「1対多」の関係にしています。 「学習」表には、「ユーザ」表を参照する外部キー(ユーザID)と、「問題集」表を参照する外部キー(問題集ID)を作成します。ユーザIDと問題集IDの組合せは、行データを一意に識別できる複合主キーとなります。 以上より、 ・「学習」エンティティは、「ユーザ」エンティティを参照する外部キー「ユーザID」を持つ ・「学習」エンティティは、「問題集」エンティティを参照する外部キー「問題集ID」を持つ ・「ユーザ」エンティティと「学習」エンティティ間は「1対多」の関係になる が正解です。 その他の選択肢については以下のとおりです。 ・「問題集」エンティティは、「ユーザ」エンティティを参照する外部キー「ユーザID」を持つ ・「ユーザ」エンティティは、「問題集」エンティティを参照する外部キー「問題集ID」...
- 参考URL:
  - https://qiita.com/ramuneru/items/db43589551dd0c00fef9

### 問題ID 28772 (変換関数および条件式)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/28772?q%5Binclude_reference%5D=1
- 問題傾向: 変換関数および条件式
- 問題文要約: 次のSQL文を実行すると、どのように表示されますか。 ただし、実行環境は日本語環境とします。 SELECT TO_CHAR(7777.777, 'L9,999') FROM dual;
- 解説要約: TO_CHAR関数は、数値や日付値を指定された書式に従って文字列に変換する関数です。 第1引数に数値が指定された場合は、数値を文字列へ変換します。 TO_CHAR(数値 [, '数値書式'] [, NLSパラメータ]) 設問のSQL文は数値書式にローカル通貨記号の"L"が指定されているので、日本語環境では¥記号が表示されます。また、指定された位置にカンマが表示されます。 第1引数の数値「7777.777」は小数点以下3桁まで指定されており数値書式と異なりますが、小数点以下は四捨五入されて正常に表示されます。 以上より、 ・¥7,778 が正解です。 以下は実行例です。 その他の選択肢については次のとおりです。 ・\7,777 小数点以下が四捨五入されていないので、誤りです。 ・\7,777.777 小数点以下が表示されているので、誤りです。 ・######### #記号が表示されるのは第1引数で指定した数値(小数点より左の整数部)よりも数値書式の桁数が少ない場合です。よって誤りです。 ・SQL文がエラーになる エラーになりませんので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/E96517_01/sqlrf/TO_CHAR-number.html#GUID-00DA076D-2468-41AB-A3AC-CC78DBA0D9CB
  - https://docs.oracle.com/cd/E96517_01/sqlrf/Format-Models.html#GUID-096CA64F-1DA3-4C49-A18B-ECC7518EE56C

### 問題ID 28773 (単一行関数)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/28773?q%5Binclude_reference%5D=1
- 問題傾向: 単一行関数
- 問題文要約: 明日以降で最初の日曜日を表示するSQL文として正しいものはどれですか(3つ選択してください)。 ただし、データベースの実行環境は英語環境とし、NLS_TERRITORYパラメータはAMERICAとします。
- 解説要約: NEXT_DAY関数は引数で指定した日付の翌日以降に、指定した曜日になる最初の日付を返す関数です。 曜日の指定は言語環境で異なります。 また、曜日に1から7の数字を指定することも可能です。データベースのNLS_TERRITORYパラメータが「AMERICA」や「JAPAN」などの多くの地域では以下の対応になります。 1：日曜日、2：月曜日、3：火曜日、4：水曜日、5：木曜日、6：金曜日、7：土曜日 設問は英語環境ですので、'SUNDAY'や省略形の'SUN'、数字の1が指定できます。 以上より、 ・SELECT NEXT_DAY(SYSDATE, 'SUNDAY') FROM dual; ・SELECT NEXT_DAY(SYSDATE, 'SUN') FROM dual; ・SELECT NEXT_DAY(SYSDATE, 1) FROM dual; が正解です。 正解のSQL文の実行結果は次のようになります。 ※日本語環境の場合は、事前に以下のSQL文を実行してセッションを英語環境に変更して下さい。 ALTER SESSION SET NLS_DATE_LANGUAGE = 'AM...
- 参考URL:
  - https://docs.oracle.com/cd/E82638_01/sqlrf/NEXT_DAY.html#GUID-01B2CC7A-1A64-4A74-918E-26158C9096F6
  - https://www.shift-the-oracle.com/sql/functions/next_day.html

### 問題ID 29053 (副問合せ)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/29053?q%5Binclude_reference%5D=1
- 問題傾向: 副問合せ
- 問題文要約: STUDENTS表の構造とデータを確認して下さい。 GRADUATION(卒業)表には卒業する生徒のSTUDENT_IDが登録されています。 次のSQL文の実行結果として正しい記述はどれですか(3つ選択して下さい)。 DELETE FROM students s WHERE EXISTS (SELECT 'test' FROM graduation g WHERE s.student_id = g.student_id);
- 解説要約: EXISTS演算子は、副問合せの結果が1行以上返される場合にTRUEとして評価される演算子です。 主問合せのWHERE句に列名と比較演算子を指定する代りに、EXISTS演算子を指定します。 WHERE EXISTS (副問合せ) 設問のSQL文では、主問合せで取り出したSTUDENTS表の各行に対して副問合せを実行し、STUDENTS表とGRADUATION表のSTUDENT_IDが一致する場合に条件が成り立ち、STUDENTS表から、GRADUATION表に存在する生徒の行が削除されます。 通常は副問合せ→主問合せの順に実行されますが、EXISTS演算子を使用した場合は、主問合せの各行に対してその都度、副問合せが実行され、条件に合う行が存在するかどうか確認していきます。このような手法は「相関副問合せ」と呼ばれます。副問合せの中でそのFROM句に無い表を参照する場合(副問合せの外側にある表を参照する場合)に、相関副問合せとして処理されます。 以上より、 ・相関副問合せである ・主問合せの各行に対してその都度、副問合せが実行される ・STUDENTS表から、GRADUATION表に存在す...
- 参考URL:
  - https://docs.oracle.com/cd/E82638_01/sqlrf/Using-Subqueries.html#GUID-53A705B6-0358-4E2B-92ED-A83DE83DFD20
  - https://docs.oracle.com/cd/E82638_01/sqlrf/EXISTS-Condition.html

### 問題ID 29066 (DDL文)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/29066?q%5Binclude_reference%5D=1
- 問題傾向: DDL文
- 問題文要約: ORDER_TABLE表の構造を確認して下さい。 この結果のみからわかることとして適切な記述はどれですか。
- 解説要約: 設問のDESCRIBEコマンド（DESCと省略可）は、指定した表の「列の名前」「列でNULL値が許可されるかどうか」「列のデータ型・精度」の情報が表示されます。 選択肢のうち、この結果のみからわかることは「NOT NULL」と表示されている列はNULL値を許可しないことです。 以上より、 ・ID列とORDER_DATE列にはNULL値を入力できない が正解です。 その他の選択肢については次のとおりです。 ・ID列にはPRIMARY KEY制約が定義されている ・ORDER_DATE列にはPRIMARY KEY制約が定義されている DESCRIBEコマンドではPRIMARY KEY制約もしくはNOT NULL制約が定義されている列が「NOT NULL」と表示されますが、PRIMARY KEY制約かどうかは確認できませんので誤りです。表に定義された制約の種類はUSER_CONSTRAINTSビューなどで確認します。 ・ORDER_DATE列のデフォルト値はSYSDATEである CREATE TABLE文では、行の挿入時に値が指定されなかった場合に挿入するデフォルト値を列に定義できますが、D...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqpug/DESCRIBE.html#GUID-2E7032A1-67E9-4E13-96B6-D8F7B138ECAA

### 問題ID 29070 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/29070?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: ビューに関する説明として正しいものはどれですか。
- 解説要約: ビューとは、1つまたは複数の表や他のビューを基にして作成する仮想的な表のことです。 複数の表を結合して複雑な問合せを行う場合、予めその問合せでビューを作成しておくと、複雑な問合せを毎回行う必要はなく、ビューに対して問合せを行うことで、目的のデータを取り出すことが可能になります。ビュー問合せ時にWHERE句で更に条件を絞り込むこともできます。 以上より、 ・ビュー問合せ時にWHERE句で条件を指定できる が正解です。 以下は実行例です。 SQLを表示 CREATE VIEW v_emp AS SELECT employee_id, employee_name, hiredate, department_id FROM employees; WHERE salary <= 450000; SELECT * FROM v_emp WHERE department_id = 1; その他の選択肢については次のとおりです。 ・ビュー定義には実表の制約が定義された列を含めなければならない ビューを利用する目的の一つに、表の一部の列の値をユーザーに参照させたくない場合などに参照させたくない列を除いた...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/admin/managing-views-sequences-and-synonyms.html#GUID-6A691576-77B3-4DAF-ABC7-3EF4707302D4

### 問題ID 29076 (ビュー)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/29076?q%5Binclude_reference%5D=1
- 問題傾向: ビュー
- 問題文要約: DML文（INSERT、UPDATE、DELETE）を実行できないビューに対して、DMLを実行できるようにするものはどれですか。
- 解説要約: DML文（INSERT、UPDATE、DELETE）を実行できないビューに対してDMLを実行できるようにするものは、INSTEAD OFトリガーです。 以上より、 ・INSTEAD OFトリガー が正解です。 DISTINCTキーワードを定義に含むV_PRODビューに対してDELETE文が発行された時に起動するINSTEAD OFトリガーの例を記載します。 本来はビューの定義にDISTINCTキーワードが含まれている場合はビューを通じて実表のデータを削除することはできません。しかし、V_PRODビューにDELETE文が発行されると代わりに（INSTEAD OF）起動するINSTEAD OFトリガーを作成すると、実表に対してDELETE文が実行できるようになります。 SQLを表示 CREATE VIEW v_prod AS SELECT DISTINCT category, name FROM prod; CREATE OR REPLACE TRIGGER delete_v_prod INSTEAD OF DELETE ON v_prod BEGIN DELETE prod WHERE ...
- 参考URL:
  - https://docs.oracle.com/cd/E57425_01/121/TDDDG/tdddg_triggers.htm#BABECIAE

### 問題ID 29084 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/29084?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 現在、データベースが稼働しているOSのタイム・ゾーンはAsia/Tokyo（2022年4月15日）です。 また、SQL*Plusで接続している現行セッションのタイム・ゾーンはAmerica/New_York（2022年4月14日）です。 日時関数を同時に問合せた場合の説明として、適切な記述はどれですか(2つ選択して下さい)。 なお、関数の書式を指定する初期化パラメータを以下のように設定して、現行セッションでの表示を英語環境に統一しています。 ALTER SESSION SET NLS_DATE_LANGUAGE = 'AMERICAN'; ALTER SESSION SET NLS_DATE_...
- 解説要約: 以下はデータベースのタイム・ゾーンや日時を返す関数です。 設問ではOSと現行セッションのタイム・ゾーンが異なりますので、関数によって日付・時刻が変わります。 SYSDATEとSYSTIMESTAMPはデータベースが稼働するOSの現在の日時を返します。SYSDATEがDATE型で現在の日時の秒までを返すのに対し、SYSTIMESTAMPはTIMESTAMP WITH TIME ZONEデータ型で返します。日付までの表示は同じです。 CURRENT_DATE、CURRENT_TIMESTAMPは現行セッションのタイム・ゾーンの現在の日時を返します。CURRENT_DATEがDATE型で現在の日時の秒までを返すのに対し、CURRENT_TIMESTAMPはTIMESTAMP WITH TIME ZONEデータ型で返します。日付までの表示は同じです。 以上より、 ・SYSDATEとSYSTIMESTAMPの日付は同じになる ・CURRENT_DATEとCURRENT_TIMESTAMPの日付は同じになる が正解です。 以下は日時関数を同時に問合せた実行例です。 OSと現行セッションの日時が異な...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/Single-Row-Functions.html#GUID-5652DBC2-41C7-4F07-BEDD-DAF620E35F3C

### 問題ID 29085 (異なるタイム・ゾーンでのデータ管理)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/29085?q%5Binclude_reference%5D=1
- 問題傾向: 異なるタイム・ゾーンでのデータ管理
- 問題文要約: 期間を表すデータ型の説明として正しいものはどれですか。
- 解説要約: 以下は期間を表すデータ型です。 INTERVAL YEAR TO MONTH型やINTERVAL DAY TO SECOND型に値を格納するためには、以下のような期間リテラルを使用します。負の数値も格納できます。 ・INTERVAL '5-6' YEAR TO MONTH：5年6ヶ月 ・INTERVAL '100' YEAR(3)：100年 ・INTERVAL '300' MONTH(3)：300ヶ月 ・INTERVAL '10 12:30:30' DAY TO SECOND：10日と12時間30分30秒 ・INTERVAL '10 12:30:30.555555' DAY TO SECOND：10日と12時間30分30.555555秒 ※SECOND(秒フィールド)には秒の小数点以下も格納できます ※年や月の精度が2桁より大きい場合は、YEAR(3)などのように精度を指定します 以上より、 ・INTERVAL YEAR TO MONTHの年に負の数値を格納できる が正解です。 以下はINTERVAL YEAR TO MONTHの年と、INTERVAL DAY TO SECONDの日に...
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html
  - https://docs.oracle.com/cd/F19136_01/nlspg/datetime-data-types-and-time-zone-support.html#GUID-FD8C41B7-8CDC-4D02-8E6B-5250416BC17D

### 問題ID 32536 (ユーザ・アクセスの制御)
- 問題URL: https://mondai.ping-t.com/question_subjects/61/questions/32536?q%5Binclude_reference%5D=1
- 問題傾向: ユーザ・アクセスの制御
- 問題文要約: SYSTEMユーザーとしてCREATE TABLE権限を全てのユーザーに付与しました。 GRANT CREATE TABLE TO PUBLIC; TESTユーザーのみからCREATE TABLE権限を取消したい場合はどうすればよいですか。 なお、TESTユーザーにはCREATE SESSION権限しか付与されていません。
- 解説要約: 設問のSQL文では全てのユーザーを表すPUBLICにCREATE TABLE権限を付与しています。 GRANT CREATE TABLE TO PUBLIC; この場合、特定のユーザーのみから権限を取消すことはできません。 よって、その他の権限を付与したいユーザーにのみ権限を付与するか、PUBLICではないロールに権限を付与してその他のユーザーに付与する必要があります。 したがって正解は ・PUBLICに付与した権限を特定のユーザーから取消すことはできない です。 その他の選択肢については次のとおりです。 ・「REVOKE CREATE TABLE FROM PUBLIC;」を実行する PUBLICから権限を取消すと全てのユーザーから権限が取消されるので、誤りです。 ・「REVOKE CREATE TABLE FROM test;」を実行する CREATE TABLE権限を直接TESTユーザーに付与していないのでREVOKE文で取消すことはできません。誤りです。 ・TESTユーザーを削除して再作成する PUBLICに付与された権限は新規ユーザーに対しても有効になるので、誤りです。
- 参考URL:
  - https://docs.oracle.com/cd/F19136_01/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3#:~:text=PUBLICにロールを付与する場合
