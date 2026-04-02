#!/usr/bin/env python3
# ← 互換性修正: dict | None, tuple[str, bool] の Python 3.10+ 構文を 3.9 以前でも動作させる
from __future__ import annotations
"""
Basetract OCR Engine
抽出エンジン: Tesseract (pytesseract) および OpenAI Vision API
"""

import os
import re
import json
import base64
import logging

# 中央化インポートマネージャーを使用
from import_manager import import_profile_loader, import_network_config
profile_loader = import_profile_loader()
network_config = import_network_config()

from profile_loader import load_quality_profile
from network_config import NetworkConfig

_PROFILE = load_quality_profile()
_NET_CFG = NetworkConfig.get_ocr_config()

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# 技術用語ホワイトリスト（信頼スコアのブースト判定用）
TECH_DICTIONARY = [
    "protocol", "interface", "priority", "address", "routing",
    "standard", "configuration", "metric", "distance", "segment",
    "ospf", "bgp", "vlan", "subnet", "gateway", "firewall", "dns",
    "tcp", "udp", "icmp", "http", "ssh", "tls", "acl",
]


class OCRProcessor:
    """
    画像からテキストを抽出する。
    - Tesseract OCR (ローカル)
    - OpenAI Vision API (クラウド)
    """

    def __init__(self, vision_api_enabled: bool = False, lang: str | None = None):
        self.vision_api_enabled = vision_api_enabled
        self.lang = lang or _NET_CFG.get("lang", "jpn+eng")

    def process_image(self, image_path: str) -> dict | None:
        logger.info(f"Processing image: {image_path}")

        if not os.path.exists(image_path):
            logger.error(f"File not found: {image_path}")
            return None

        if self.vision_api_enabled and os.getenv('OPENAI_API_KEY'):
            return self._process_via_vision_api(image_path)
        else:
            return self._process_via_tesseract(image_path)

    def _process_via_tesseract(self, image_path: str) -> dict:
        try:
            import pytesseract
            from PIL import Image
        except ImportError:
            logger.error("Dependency missing: pytesseract/Pillow")
            return {"source": image_path, "text": "", "confidence": 0.0, "error": "ImportError"}

        try:
            img = Image.open(image_path)
            config = f'--oem 3 --psm 6 -l {self.lang}'
            extracted_text = pytesseract.image_to_string(img, config=config)

            data = pytesseract.image_to_data(img, config=config, output_type=pytesseract.Output.DICT)
            confidences = [int(c) for c in data['conf'] if str(c).isdigit() and int(c) >= 0]
            raw_confidence = (sum(confidences) / len(confidences) / 100.0) if confidences else 0.5

        except Exception as e:
            logger.error(f"Tesseract failure: {e}")
            return {"source": image_path, "text": "", "confidence": 0.0, "error": str(e)}

        return self._build_result(image_path, extracted_text, raw_confidence, engine="tesseract")

    def _process_via_vision_api(self, image_path: str) -> dict:
        try:
            import openai
        except ImportError:
            return self._process_via_tesseract(image_path)

        try:
            with open(image_path, "rb") as f:
                image_data = base64.b64encode(f.read()).decode("utf-8")

            ext = os.path.splitext(image_path)[1].lower()
            mime_map = _NET_CFG.get("mime_types", {})
            mime = mime_map.get(ext, "image/png")

            client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            response = client.chat.completions.create(
                model=_NET_CFG.get("default_model", "gpt-4o-mini"),
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{image_data}"}},
                        {"type": "text", "text": "Extract text verbatim. Return raw text only."}
                    ]
                }],
                max_tokens=2000
            )
            extracted_text = response.choices[0].message.content or ""
            raw_confidence = 0.95

        except Exception as e:
            logger.warning(f"Vision API failure: {e}. Falling back.")
            return self._process_via_tesseract(image_path)

        return self._build_result(image_path, extracted_text, raw_confidence, engine="vision_api")

    def _build_result(self, image_path: str, text: str, raw_confidence: float, engine: str) -> dict:
        ocr_cfg = _PROFILE.get("ocr", {})
        confidence_min = ocr_cfg.get("confidence_min", 0.70)
        noise_ratio_max = ocr_cfg.get("noise_ratio_max", 0.10)
        
        # 技術用語マッチによる信頼スコア補正
        matches = [term for term in TECH_DICTIONARY if term in text.lower()]
        confidence_boost = min(len(matches) * 0.02, 0.1)
        final_confidence = min(1.0, raw_confidence + confidence_boost)

        if final_confidence < confidence_min:
            logger.warning(f"Low confidence ({final_confidence * 100:.1f}%) below threshold ({confidence_min * 100:.1f}%) for {image_path}")
        else:
            logger.info(f"Extraction complete (confidence: {final_confidence * 100:.1f}%, engine: {engine})")

        return {
            "source": image_path,
            "text": text,
            "confidence": round(final_confidence, 3),
            "detected_terms": matches,
            "engine": engine,
            "thresholds": {
                "confidence_min": confidence_min,
                "noise_ratio_max": noise_ratio_max
            }
        }


def batch_process(sources_dir: str, output_path: str, vision_api: bool = False) -> None:
    """ディレクトリ内の画像をバッチ処理し、結果を保存する。"""
    processor = OCRProcessor(vision_api_enabled=vision_api)
    results = []
    supported = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"}

    for fname in sorted(os.listdir(sources_dir)):
        if os.path.splitext(fname)[1].lower() not in supported:
            continue
        result = processor.process_image(os.path.join(sources_dir, fname))
        if result:
            results.append(result)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info(f"Batch processing complete: {len(results)} files → {output_path}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 ocr_engine.py <image_path> [--vision]")
        sys.exit(1)

    use_vision = "--vision" in sys.argv
    proc = OCRProcessor(vision_api_enabled=use_vision)
    result = proc.process_image(sys.argv[1])
    if result:
        print(json.dumps(result, ensure_ascii=False, indent=2))
