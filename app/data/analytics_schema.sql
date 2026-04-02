-- Learning Analytics Schema Template
-- 修正点: 外部キー制約（FOREIGN KEY）を追加し、参照整合性を保証する
-- SQLite での外部キー制約は PRAGMA foreign_keys = ON; を有効にしてから使用すること

PRAGMA foreign_keys = ON;

-- ユーザー基本情報
CREATE TABLE IF NOT EXISTS users (
    user_id  TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    target_exam TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 学習セッション記録
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    user_id    TEXT NOT NULL,
    start_time TIMESTAMP,
    end_time   TIMESTAMP,
    mode       TEXT CHECK(mode IN ('Exam', 'Practice', 'Lab')),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- 回答履歴（Weakness Analysis用）
CREATE TABLE IF NOT EXISTS response_history (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id    TEXT NOT NULL,
    question_id   TEXT NOT NULL,
    is_correct    INTEGER NOT NULL CHECK(is_correct IN (0, 1)), -- SQLite に BOOLEAN はない
    response_time INTEGER, -- 秒
    category      TEXT,
    difficulty    TEXT CHECK(difficulty IN ('Easy', 'Medium', 'Hard')),
    timestamp     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
);

-- カテゴリ別習熟度
CREATE TABLE IF NOT EXISTS category_proficiency (
    user_id       TEXT NOT NULL,
    category      TEXT NOT NULL,
    mastery_score REAL DEFAULT 0.0 CHECK(mastery_score BETWEEN 0.0 AND 100.0),
    last_practice TIMESTAMP,
    PRIMARY KEY (user_id, category),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- AI推薦ログ
CREATE TABLE IF NOT EXISTS ai_recommendations (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id               TEXT NOT NULL,
    message               TEXT NOT NULL,
    derived_from_category TEXT,
    status                TEXT DEFAULT 'Pending' CHECK(status IN ('Pending', 'Completed', 'Dismissed')),
    created_at            TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ── Flask API 用テーブル ────────────────────────────────────────────
-- app.py の /api/questions エンドポイントが使用するテーブル
-- ← 修正: init_db() が analytics_schema.sql を使うように変更したため、
--   app.py が参照するテーブルをここで定義しなければ「no such table」エラーになる

-- 問題データストア（API経由でインポートされた Basetract 12キースキーマデータ）
CREATE TABLE IF NOT EXISTS questions (
    id           TEXT PRIMARY KEY,
    topic        TEXT,
    question_data TEXT NOT NULL,  -- JSON シリアライズされた問題オブジェクト全体
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 簡易学習履歴（API の /api/history エンドポイントが書き込む）
-- 詳細分析は response_history テーブルを使用すること
CREATE TABLE IF NOT EXISTS learning_history (
    id          TEXT PRIMARY KEY,
    user_id     TEXT NOT NULL DEFAULT 'anonymous',
    question_id TEXT NOT NULL,
    result      INTEGER NOT NULL CHECK(result IN (0, 1)),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- パフォーマンス向上のためのインデックス
CREATE INDEX IF NOT EXISTS idx_response_session    ON response_history(session_id);
CREATE INDEX IF NOT EXISTS idx_response_question   ON response_history(question_id);
CREATE INDEX IF NOT EXISTS idx_response_category   ON response_history(category);
CREATE INDEX IF NOT EXISTS idx_sessions_user       ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_proficiency_user    ON category_proficiency(user_id);
CREATE INDEX IF NOT EXISTS idx_ai_rec_user         ON ai_recommendations(user_id);
CREATE INDEX IF NOT EXISTS idx_questions_topic     ON questions(topic);
CREATE INDEX IF NOT EXISTS idx_lh_user             ON learning_history(user_id);
CREATE INDEX IF NOT EXISTS idx_lh_question         ON learning_history(question_id);
