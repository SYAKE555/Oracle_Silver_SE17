/**
 * Basetract Data Loader (v7.0-synced)
 * 修正点:
 *   - バージョン不整合を是正 (v10 -> v7.0-synced)
 *   - window.dataBuffer の競合を避けるため、ロード完了直後にバッファを退避する設計に変更
 */
class BasetractLoader {
    constructor() {
        this.registry = [];
        this.isProcessing = false;
    }

    /**
     * 指定した名前のJSセグメントを動的にロードし、
     * basetract_core の registry にも橋渡しする。
     * @param {string} name - ファイル名（拡張子なし）
     * @param {string} basePath - データディレクトリのパス
     * @returns {Promise<void>}
     */
    async ingestSegment(name, basePath = './app/data/') {
        console.log(`[Loader] Ingesting segment: ${name}`);
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            const cleanBasePath = basePath.endsWith('/') ? basePath : basePath + '/';
            script.src = `${cleanBasePath}${name.toLowerCase()}.js`;

            script.onload = () => {
                // ロード完了直後にデータをキャプチャ（他スクリプトによる上書き防止）
                const buffer = window.dataBuffer;
                window.dataBuffer = null;

                if (buffer && Array.isArray(buffer)) {
                    // 1. ローカルレジストリに追加
                    this.registry = [...this.registry, ...buffer];

                    // 2. basetract_core.js の registry にも橋渡し
                    if (window.basetract && typeof window.basetract.injectData === 'function') {
                        window.basetract.injectData(buffer);
                    } else {
                        console.warn('[Loader] window.basetract not ready yet. Data queued in loader registry.');
                    }

                    console.log(`[Loader] Loaded ${buffer.length} entries from segment: ${name}`);
                    resolve();
                } else {
                    const err = `Segment "${name}" contains no valid window.dataBuffer array.`;
                    console.error(`[Loader] ${err}`);
                    reject(new Error(err));
                }
            };

            script.onerror = () => {
                const err = `Failed to load segment file: ${script.src}`;
                console.error(`[Loader] ${err}`);
                reject(new Error(err));
            };

            document.head.appendChild(script);
        });
    }

    /**
     * 複数セグメントを順番にロードする。
     * @param {string[]} names - セグメント名の配列
     * @param {string} basePath - データディレクトリ
     */
    async ingestAll(names, basePath = './app/data/') {
        for (const name of names) {
            try {
                await this.ingestSegment(name, basePath);
            } catch (e) {
                console.error(`[Loader] Skipping segment "${name}": ${e.message}`);
            }
        }
        console.log(`[Loader] All segments processed. Total registry: ${this.registry.length} entries.`);
    }

    getData() {
        return this.registry;
    }
}

window.basetractLoader = new BasetractLoader();
