/**
 * Basetract Unified Core Protocol (v7.0-synced)
 * 修正点:
 *   - バージョン不整合を是正 (v10 -> v7.0-synced)
 *   - injectData() における重複登録防止ロジックの追加
 */
class BasetractCore {
    constructor() {
        this.registry = [];
        this.mode = 'READ'; // READ | TEST
        this.currentSegment = null;
        this.observedIds = new Set();
    }

    async init() {
        console.log('[Basetract] Core initializing...');
        this.ensureModal();
        this.hydrateQuizzes();
    }

    ensureModal() {
        if (document.getElementById('basetract-modal')) return;
        const modal = document.createElement('div');
        modal.id = 'basetract-modal';
        modal.innerHTML = `
            <div class="bt-modal-content">
                <span class="bt-close">&times;</span>
                <div id="bt-quiz-body"></div>
            </div>
            <style>
                #basetract-modal { display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); backdrop-filter: blur(5px); }
                .bt-modal-content { background: #1e293b; margin: 8% auto; padding: 30px; border: 1px solid var(--primary-neon, #38bdf8); width: 85%; max-width: 620px; border-radius: 12px; position: relative; color: #fff; box-shadow: 0 0 30px rgba(56, 189, 248, 0.2); max-height: 80vh; overflow-y: auto; }
                .bt-close { position: absolute; right: 20px; top: 10px; color: #64748b; font-size: 28px; font-weight: bold; cursor: pointer; line-height: 1; }
                .bt-close:hover { color: var(--accent-neon, #f472b6); }
                #bt-quiz-body h3 { color: var(--primary-neon, #38bdf8); margin-top: 0; font-size: 1rem; }
                #bt-quiz-body p { line-height: 1.7; }
                /* 選択肢 */
                .bt-option { display: block; padding: 12px 15px; margin: 8px 0; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; cursor: pointer; transition: background 0.2s, border-color 0.2s; font-size: 0.95rem; }
                .bt-option:hover:not(.bt-answered) { background: rgba(56, 189, 248, 0.1); border-color: var(--primary-neon, #38bdf8); }
                /* 正解・不正解フィードバック */
                .bt-option.bt-correct { background: rgba(16, 185, 129, 0.2) !important; border-color: #10b981 !important; color: #6ee7b7; cursor: default; }
                .bt-option.bt-incorrect { background: rgba(239, 68, 68, 0.15) !important; border-color: #ef4444 !important; color: #fca5a5; cursor: default; }
                .bt-option.bt-answered { cursor: default; pointer-events: none; }
                /* 解説ブロック */
                .bt-logic { margin-top: 20px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-left: 4px solid var(--primary-neon, #38bdf8); display: none; font-size: 0.9rem; line-height: 1.7; }
                .bt-logic strong { color: var(--primary-neon, #38bdf8); }
                .bt-result-label { font-weight: 700; margin-bottom: 8px; font-size: 1rem; }
                .bt-result-label.correct { color: #10b981; }
                .bt-result-label.incorrect { color: #ef4444; }
            </style>
        `;
        document.body.appendChild(modal);
        modal.querySelector('.bt-close').onclick = () => modal.style.display = 'none';
        window.addEventListener('click', (e) => { if (e.target === modal) modal.style.display = 'none'; });
    }

    switchMode(newMode) {
        this.mode = newMode;
        document.body.dataset.mode = newMode;
        console.log(`[Basetract] Mode: ${newMode}`);
        if (newMode === 'TEST') {
            this.renderExam();
        }
    }

    /**
     * TEST モード: #exam-mount に問題一覧・スコアリング・進捗を描画する
     * - registry からすべての問題を取得してレンダリング
     * - 各問題は独立した正解判定と解説表示を持つ
     * - 最下部にスコアサマリーを表示（全問回答後に解放）
     */
    renderExam() {
        const mount = document.getElementById('exam-mount');
        if (!mount) return;

        if (this.registry.length === 0) {
            mount.innerHTML = '<p style="color:#64748b;text-align:center;padding:60px 0;">No questions loaded. Check that data files exist in app/data/.</p>';
            return;
        }

        // 既にレンダリング済みかつデータが同じ場合はスキップ（重複レンダリング防止）
        if (mount.dataset.examRendered === String(this.registry.length)) return;
        mount.dataset.examRendered = String(this.registry.length);

        // 状態管理
        const state = {
            total: this.registry.length,
            answered: 0,
            correct: 0
        };

        // スタイル注入（初回のみ）
        if (!document.getElementById('bt-exam-styles')) {
            const style = document.createElement('style');
            style.id = 'bt-exam-styles';
            style.textContent = `
                .bt-exam-header { margin-bottom: 40px; }
                .bt-exam-progress-bar-wrap { background: rgba(255,255,255,0.07); border-radius: 6px; height: 6px; overflow: hidden; margin: 16px 0 8px; }
                .bt-exam-progress-bar { height: 100%; width: 0%; background: var(--primary-neon, #38bdf8); transition: width 0.4s ease; border-radius: 6px; }
                .bt-exam-counter { font-size: 0.85rem; color: #64748b; }
                .bt-exam-question { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 28px 32px; margin-bottom: 24px; transition: border-color 0.3s; }
                .bt-exam-question.bt-q-correct { border-color: #10b981; }
                .bt-exam-question.bt-q-incorrect { border-color: #ef4444; }
                .bt-exam-q-meta { font-size: 0.78rem; color: #475569; margin-bottom: 12px; display: flex; gap: 10px; flex-wrap: wrap; }
                .bt-exam-q-meta span { background: rgba(255,255,255,0.05); padding: 2px 8px; border-radius: 4px; }
                .bt-exam-q-text { font-size: 1rem; line-height: 1.7; margin-bottom: 18px; }
                .bt-exam-options { display: flex; flex-direction: column; gap: 8px; }
                .bt-exam-opt { padding: 11px 16px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 7px; cursor: pointer; font-size: 0.93rem; transition: background 0.2s, border-color 0.2s; }
                .bt-exam-opt:hover:not(.bt-answered) { background: rgba(56,189,248,0.1); border-color: var(--primary-neon, #38bdf8); }
                .bt-exam-opt.bt-answered { cursor: default; pointer-events: none; }
                .bt-exam-opt.bt-correct { background: rgba(16,185,129,0.18) !important; border-color: #10b981 !important; color: #6ee7b7; }
                .bt-exam-opt.bt-incorrect { background: rgba(239,68,68,0.14) !important; border-color: #ef4444 !important; color: #fca5a5; }
                .bt-exam-logic { display: none; margin-top: 16px; padding: 14px 18px; background: rgba(56,189,248,0.05); border-left: 3px solid var(--primary-neon, #38bdf8); font-size: 0.88rem; line-height: 1.7; }
                .bt-exam-logic .bt-exam-result { font-weight: 700; margin-bottom: 8px; }
                .bt-exam-logic .bt-exam-result.correct { color: #10b981; }
                .bt-exam-logic .bt-exam-result.incorrect { color: #ef4444; }
                .bt-exam-summary { display: none; background: rgba(255,255,255,0.04); border: 1px solid var(--primary-neon, #38bdf8); border-radius: 14px; padding: 40px 32px; margin-top: 40px; text-align: center; animation: slideIn 0.5s ease; }
                .bt-exam-summary h2 { color: var(--primary-neon, #38bdf8); margin: 0 0 16px; font-size: 1.5rem; }
                .bt-exam-score-big { font-size: 3.5rem; font-weight: 800; line-height: 1; }
                .bt-exam-score-big.grade-s { color: #f472b6; }
                .bt-exam-score-big.grade-a { color: #38bdf8; }
                .bt-exam-score-big.grade-b { color: #34d399; }
                .bt-exam-score-big.grade-c { color: #fbbf24; }
                .bt-exam-score-big.grade-d { color: #f87171; }
                .bt-exam-score-label { color: #94a3b8; margin: 8px 0 24px; font-size: 0.95rem; }
                .bt-exam-retry-btn { padding: 12px 32px; background: var(--primary-neon, #38bdf8); color: #000; border: none; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.95rem; transition: opacity 0.2s; }
                .bt-exam-retry-btn:hover { opacity: 0.85; }
            `;
            document.head.appendChild(style);
        }

        // ヘッダー（進捗バー）
        const header = document.createElement('div');
        header.className = 'bt-exam-header';
        header.innerHTML = `
            <div class="bt-exam-progress-bar-wrap"><div class="bt-exam-progress-bar" id="bt-exam-pbar"></div></div>
            <div class="bt-exam-counter" id="bt-exam-counter">0 / ${state.total} answered</div>
        `;
        mount.innerHTML = '';
        mount.appendChild(header);

        const updateProgress = () => {
            const pct = (state.answered / state.total) * 100;
            const pbar = document.getElementById('bt-exam-pbar');
            const counter = document.getElementById('bt-exam-counter');
            if (pbar) pbar.style.width = pct + '%';
            if (counter) counter.textContent = `${state.answered} / ${state.total} answered`;
            if (state.answered === state.total) {
                showSummary();
            }
        };

        // 問題カード生成
        this.registry.forEach((q, idx) => {
            const card = document.createElement('div');
            card.className = 'bt-exam-question';
            card.id = `bt-exam-q-${idx}`;

            const tags = Array.isArray(q.tags) ? q.tags.join(', ') : (q.tags || '');
            const optionsHTML = (q.options || []).map(opt =>
                `<div class="bt-exam-opt" data-opt="${opt.replace(/"/g, '&quot;')}">${opt}</div>`
            ).join('');

            card.innerHTML = `
                <div class="bt-exam-q-meta">
                    <span>#${idx + 1}</span>
                    <span>${q.category || 'General'}</span>
                    <span>Difficulty: ${q.difficulty || '-'}</span>
                    ${tags ? `<span>${tags}</span>` : ''}
                </div>
                <div class="bt-exam-q-text">${q.text}</div>
                <div class="bt-exam-options">${optionsHTML}</div>
                <div class="bt-exam-logic" id="bt-exam-logic-${idx}">
                    <div class="bt-exam-result" id="bt-exam-result-${idx}"></div>
                    <strong style="color:var(--primary-neon,#38bdf8);">Correct Answer:</strong> ${q.answer}
                    ${q.logic ? `<br><br>${q.logic}` : ''}
                    ${q.plan ? `<br><br><em style="color:#94a3b8;">Study plan: ${q.plan}</em>` : ''}
                </div>
            `;

            // 選択肢クリックイベント
            card.querySelectorAll('.bt-exam-opt').forEach(optEl => {
                optEl.addEventListener('click', () => {
                    if (optEl.classList.contains('bt-answered')) return;
                    const selected = optEl.dataset.opt;
                    const isCorrect = selected === q.answer;

                    // 全選択肢ロック
                    card.querySelectorAll('.bt-exam-opt').forEach(o => {
                        o.classList.add('bt-answered');
                        if (o.dataset.opt === q.answer) o.classList.add('bt-correct');
                    });
                    if (!isCorrect) optEl.classList.add('bt-incorrect');

                    // カードボーダー
                    card.classList.add(isCorrect ? 'bt-q-correct' : 'bt-q-incorrect');

                    // 解説表示
                    const logicEl = document.getElementById(`bt-exam-logic-${idx}`);
                    const resultEl = document.getElementById(`bt-exam-result-${idx}`);
                    if (resultEl) {
                        resultEl.textContent = isCorrect ? '✓ Correct' : '✗ Incorrect';
                        resultEl.className = `bt-exam-result ${isCorrect ? 'correct' : 'incorrect'}`;
                    }
                    if (logicEl) logicEl.style.display = 'block';

                    // スコア更新
                    if (isCorrect) state.correct++;
                    state.answered++;
                    updateProgress();
                });
            });

            mount.appendChild(card);
        });

        // サマリーカード（全問回答後に表示）
        const summary = document.createElement('div');
        summary.className = 'bt-exam-summary';
        summary.id = 'bt-exam-summary';
        mount.appendChild(summary);

        const showSummary = () => {
            const pct = Math.round((state.correct / state.total) * 100);
            const grade = pct >= 90 ? 'S' : pct >= 75 ? 'A' : pct >= 60 ? 'B' : pct >= 45 ? 'C' : 'D';
            const gradeClass = `grade-${grade.toLowerCase()}`;
            summary.innerHTML = `
                <h2>Exam Complete</h2>
                <div class="bt-exam-score-big ${gradeClass}">${pct}%</div>
                <div class="bt-exam-score-label">${state.correct} / ${state.total} correct — Grade <strong>${grade}</strong></div>
                <button class="bt-exam-retry-btn" id="bt-exam-retry">Retry Exam</button>
            `;
            summary.style.display = 'block';
            summary.scrollIntoView({ behavior: 'smooth', block: 'center' });

            document.getElementById('bt-exam-retry').addEventListener('click', () => {
                // リトライ: exam-mount のレンダリングキャッシュを消去して再描画
                delete mount.dataset.examRendered;
                this.renderExam();
            });
        };

        console.log(`[Basetract] Exam rendered: ${state.total} questions.`);
    }

    hydrateQuizzes() {
        const triggers = document.querySelectorAll('[data-quiz-id]');
        triggers.forEach(el => {
            // 重複バインドを防ぐ
            if (el.dataset.btBound) return;
            el.dataset.btBound = '1';
            el.addEventListener('click', () => this.launchMiniQuiz(el.dataset.quizId));
            el.style.cursor = 'help';
            el.style.borderBottom = '1px dashed var(--primary-neon, #38bdf8)';
        });
        if (triggers.length > 0) {
            console.log(`[Basetract] Hydrated ${triggers.length} quiz triggers.`);
        }
    }

    launchMiniQuiz(id) {
        const q = this.registry.find(item => item.id === id);
        if (!q) {
            console.error(`[Basetract] Quiz ID "${id}" not found in registry (${this.registry.length} entries).`);
            return;
        }

        const body = document.getElementById('bt-quiz-body');
        const optionsHTML = q.options.map(opt => {
            return `<div class="bt-option" data-opt="${opt.replace(/"/g, '&quot;')}">${opt}</div>`;
        }).join('');

        body.innerHTML = `
            <h3>Practice Check: ${q.category || 'Technical Verification'}</h3>
            <p>${q.text}</p>
            <div id="bt-options">${optionsHTML}</div>
            <div class="bt-logic" id="bt-logic-block">
                <div class="bt-result-label" id="bt-result-label"></div>
                <strong>Correct Answer:</strong> ${q.answer}<br><br>
                ${q.logic}
                ${q.plan ? `<br><br><em style="color:#94a3b8;">Study plan: ${q.plan}</em>` : ''}
            </div>
        `;

        // 正解判定ロジック（旧版では未実装だった）
        document.querySelectorAll('#bt-options .bt-option').forEach(optEl => {
            optEl.addEventListener('click', () => {
                const selected = optEl.dataset.opt;
                const isCorrect = selected === q.answer;

                // 全選択肢をロック
                document.querySelectorAll('#bt-options .bt-option').forEach(o => {
                    o.classList.add('bt-answered');
                    if (o.dataset.opt === q.answer) {
                        o.classList.add('bt-correct');
                    }
                });

                // 選択した選択肢が不正解なら赤くハイライト
                if (!isCorrect) {
                    optEl.classList.add('bt-incorrect');
                }

                // 結果ラベルと解説を表示
                const resultLabel = document.getElementById('bt-result-label');
                resultLabel.textContent = isCorrect ? '✓ Correct' : '✗ Incorrect';
                resultLabel.className = `bt-result-label ${isCorrect ? 'correct' : 'incorrect'}`;
                document.getElementById('bt-logic-block').style.display = 'block';
            });
        });

        document.getElementById('basetract-modal').style.display = 'block';
    }

    injectData(buffer) {
        if (!Array.isArray(buffer)) {
            console.error('[Basetract] injectData() requires an array.');
            return;
        }
        
        const newEntries = buffer.filter(item => {
            if (item.id && !this.observedIds.has(item.id)) {
                this.observedIds.add(item.id);
                return true;
            }
            return false;
        });

        if (newEntries.length === 0) return;

        this.registry = [...this.registry, ...newEntries];
        console.log(`[Basetract] Registry updated: +${newEntries.length} entries (Total: ${this.registry.length})`);
        // 新たに追加されたデータに対して data-quiz-id トリガーを再バインド
        this.hydrateQuizzes();
    }
}

window.basetract = new BasetractCore();
window.addEventListener('DOMContentLoaded', () => window.basetract.init());
