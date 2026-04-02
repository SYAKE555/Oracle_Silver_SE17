# AI Prompt Template: Learning System Builder

Use this prompt to instruct an AI (e.g., Gemini 2.0 Pro/Flash) to generate a complete learning environment for a new certification.

---

## Prompt Instructions

**Role**: You are an Expert Educational Architect specializing in IT Certification training.

**Task**: Create a comprehensive study environment for the **[Certification Name (e.g., LPI Linux Essentials)]** certification.

**Input Resource**: Use the official syllabus for [Certification Name] located at [Link/Text].

**Output Requirements**:

1.  **Textbook (HTML)**:
    - Create a single-file HTML textbook based on the `unified_engine_template.html` structure.
    - Organize into chapters following the official syllabus.
    - Each chapter MUST have a unique ID (e.g., `id="section-1"`, `id="section-2"`).
    - Implement the **Responsive Mobile Layout**: Ensure any custom CSS inherently forces the main content to `margin-left: 0; width: 100%` and sidebars to stack vertically or hide on `@media (max-width: 860px)`.
    - Use technical, precise language for professional training.

2.  **Question Database (JS)**:
    - Generate a `questions.js` data Buffer strictly adhering to the 12-key schema found in `sample_data.js` / `specification.md`.
    - Every object MUST contain: `id, category, text, type, answer, options, logic, plan, weight, textbook_ref, tags, difficulty`.
    - Create **[Quantity (e.g., 50)]** high-quality questions. Target output path for project integration: `app/data/initial_state.js`.
    - Ensure a mix of `choice` and `text` types.
    - Map each question to a `textbook_ref` **array of strings** matching the chapter IDs in the textbook (e.g., `["chapter-3", "routing-fundamentals"]`). Do NOT use integers; use the section `id` attributes from the HTML textbook.
    - Include a detailed `logic` field (200+ characters) explaining the precise technical facts.

3.  **Self-Audit Phase (MANDATORY)**:
    - Before finalizing output, you MUST perform a mental check against the **QualityGuard** logic:
        - [ ] All 12 keys exist in EVERY segment?
        - [ ] No placeholder text remains?
        - [ ] Logic field contains specific numerical or protocol-specific facts?
        - [ ] Answer string exists verbatim in the options list?
    - If ANY check fails, you MUST regenerate the segment before delivery.

4.  **Exam Logic**:
    - Configure the `DOMAIN_EXAM_WEIGHTS` equivalent for this certification based on the official score distribution.

**Strict Constraints**:
- **Basetract Standard**: Technical precision is non-negotiable. For protocols (OSPF, STP, etc.), you MUST include specific timer values, port states, and standard-specific nuances (e.g., NETCONF is XML-only).
- **Text-Only**: Do not refer to images or "Figure 1". Use CLI output or ASCII to illustrate concepts.
- **Consistency**: The `category` in `questions.js` must strictly match the naming in the Exam weights configuration.


---

## Variable Placeholder Guide
- `[Certification Name]`: The name of the exam.
- `[Major Categories]`: List the 4-6 main domains of the exam.
- `[Weightings]`: The % of questions assigned to each domain.
