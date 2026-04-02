# Learning System: System Architecture (Basetract Standard)

This document defines the core architecture of the Basetract autonomous learning system. When initializing new projects via `factory.py`, these conventions must be maintained to ensure tool-chain compatibility.

## 1. Standard Directory Structure

```text
/Project_Root
├── index.html                  # Standard PC Edition (Features & Rich UI)
├── mobile.html                 # Reliability Mobile Edition (Zero-Fail Layout)
├── app/                        # Presentation Layer
│   ├── data/                   # Question Databases & Analytics Schemas
│   ├── loader.js               # Dynamic Content Loader
│   ├── basetract_core.js       # Core Application Engine
│   └── theme.css               # Design Tokens & UI Styles
├── pipeline/                   # Automation & AI Logic
│   ├── tools/                  # Basetract Core Tool Suite (Python)
│   └── logs/                   # Execution & Audit Logs
├── materials/
│   └── sources/                # Text & Image Inputs
├── docs/                       # Specifications & Architecture Manuals
└── config/skills/              # AI Behavior & Evolution Rules
```

## 2. Component Responsibilities

### A. Dual-Track Presentation Layer (`index.html` / `mobile.html`)
- **Role**: Provides the reliable reading environment.
- **Philosophy**: `index.html` runs rich scripts and interactive logic. `mobile.html` is hard-compiled with Zero-Fail responsive CSS to ensure zero layout crushing on smaller screens regardless of external styling.

### B. Dynamic Logic Layer (`app/`)
- **Role**: Provides the interactive test and study environment overlay.
- **Data Source**: Loads `app/data/initial_state.js` or `questions.js` as modular `window.dataBuffer` arrays.
- **Logic**: Handles filtering, scoring, and synchronized review linking to the textbook.

### C. Automation Pipeline (`pipeline/`)
- **Role**: Automates the transition from raw data to structured learning.
- **Tools**: Includes `factory.py` (orchestration), `quality_guard.py` (validation), and `hallucination_detector.py` (QA).
- **Generation**: `content_generator.py` transforms raw JSON (term/definition pairs) into Basetract-compliant question segments.
- **OCR Logic**: `ocr_engine.py` handles image-to-text extraction from `materials/sources/` via Tesseract OCR and OpenAI Vision API.

### D. AI Skills (`config/skills/`)
- **Role**: Defines the self-correction and evolution logic for the AI.
- **Cycle**: Scan (Validation) → Fix (Reference Textbook) → Audit (Verification).

## 3. Standard Data Flow

1. **OCR Processor** (`ocr_engine.py`) extracts from **Sources** → **Raw JSON**.
2. **Unified Generator** (`content_generator.py`) transforms **JSON** → **initial_state.js** (Basetract 12-key schema).
3. **Quality Guard** (`quality_guard.py`) validates **initial_state.js** against **Specification**.
4. **Hallucination Detector** (`hallucination_detector.py`) verifies **Logic** density and keyword accuracy.
5. **App Layer** renders content for the user (served via Flask `app.py`).

## 4. UI/UX Architectural Constraints (Validated Responsive Layout)

Basetract's fundamental philosophy is **reliability across all devices**. To prevent layout failures (e.g., sidebars crushing main content on mobile screens), all UI generation must strictly adhere to the following CSS constraints:

1. **Strict Responsive Sidebar (The "Fold or Stack" Rule)**:
   - On screens `<= 860px`, sidebars MUST either transition to a hidden drawer (`transform: translateX(-100%)`) OR stack vertically above the main content (`width: 100%`, `position: relative`).
   - Sidebars MUST NEVER maintain a rigid horizontal width that competes with the reading area on mobile widths.

2. **Absolute Fluidity Principle**:
   - The primary reading area (`main`, `.content-viewport`) MUST forcibly reclaim the full width of the screen on mobile devices (`width: 100% !important`, `margin-left: 0 !important`).
   - Flex containers must employ `min-width: 0` to prevent implicitly derived widths from causing unwanted horizontal overflow.

3. **Safe Content Wrapping**:
   - All text, tables, and `<pre>` blocks injected into the DOM must be constrained (`max-width: 100%`, `overflow-x: auto`) to guarantee they never puncture the viewport boundaries.
