---
name: Certification_Evolution
description: Rules for autonomously evolving the [Certification] question database.
---

# QuestionDB Evolution Skill Template

## Purpose
`app/data/sample.js` または `questions.js` の `window.dataBuffer` 配列を自律的にリファクタリングし、試験品質を担保する。

---

## 1. データスキーマ定義

`window.dataBuffer` の各エントリは以下のスキーマに厳格に従うこと。

```json
{
  "id": "DB[4桁の連番]",
  "category": "[Official Category 1] | [Official Category 2] | ...",
  "text": "問題文。具体的数値やCLI出力を可能な限り含めること。",
  "type": "choice | text",
  "answer": "正解の文字列",
  "options": ["A. xxx", "B. yyy", "C. zzz", "D. www"],
  "logic": "【正解の根拠】技術仕様に基づく詳細な理由。【誤答の根拠】他が誤りである理由。",
  "plan": "不正解時の具体的学習プラン。",
  "weight": 0.1,
  "textbook_ref": [対応する教科書の章番号],
  "tags": ["タグ1", "タグ2"],
  "difficulty": "Easy | Medium | Hard"
}
```

---

## 2. カテゴリ制限

以下の公式カテゴリ以外は一切使用禁止です。

1. **[Category A]**: (分野の説明)
2. **[Category B]**: (分野の説明)
...

---

## 3. 品質基準（Must）

- **画像依存の排除**: `[IMG]` などのタグは使わず、テキストベース（CLI出力やASCIIトポロジ）で完結させる。
- **解説の詳理性**: `logic` は「なぜ正解か」だけでなく「なぜ誤答か（消去法の根拠）」を必ず含む。
- **教科書リンク**: `textbook_ref` は実在する章番号と一致させる。

---

## 4. 自律実行サイクル (Safety Optimized)

1. **Pre-Check**: 現状の `questions.js` を `json.loads` 等でパースし、構文エラーがないことを確認する。
2. **Scan**: バリデータの結果からエラー（スキーマ不整合、解説不足、画像依存）がある問題を **最大3問** 抽出する。
3. **Fix**: コンパイル済みの Basetract 教科書（`index.html` 等）を唯一の正解（Ground Truth）として参照し、修正する。
4. **Lint**: 修正後、必ず JSON バリデータを通し、`UTF-8` で保存されているか確認する。
5. **Report**: 修正内容を `修正履歴` フォルダに詳細に記録する。

---

## 5. 禁止事項 (Pitfall Prevention)

1. **推測でのデータ作成**: 教科書や仕様にない情報を勝手に捏造しない。
2. **ファイル全体の一括書き換え**: 構造（Div等）を壊すリスクがあるため、対象行のみを置換する。
3. **カテゴリ名の揺らぎ**: 公式カテゴリ名と完全一致（大文字小文字・スペース）させること。
4. **関数・スタイルの上書き**: コンテンツ修正時に `<script>` や `<style>` タグを誤って削除・変更しないこと。

