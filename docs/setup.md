# Infrastructure Setup Guide

## 1. Dependency Management
Install the required environment via the automated bootstrap:
`python3 pipeline/bootstrap.py`

## 2. Environment Initialization
To create a new project environment:
`python3 tools/factory.py "Project_Name"`

**Updating an existing project**:
`python3 tools/factory.py "Project_Name" --sync`
(This updates infrastructure files without overwriting your `initial_state.js`).

## 3. AI Configuration (Optional)
If you wish to use automated AI Review or enhanced generation:
1. Navigate to `/config`.
2. Rename `secrets.template.env` to `.env`.
3. Enter your API keys (OpenAI, Anthropic, or Google) into the file.
4. The system will automatically detect the key and enable AI-assisted modes.

## 4. Toolchain Usage
- **Validation**: Use `quality_guard.py` to verify data integrity before deployment.
- **Acquisition**: Use `research_crawler.py` to extract structured technical data from documentation URLs.
- **Generation**: Use `content_generator.py` to transform extracted JSON data into structured questions (replaces the legacy `segment_generator.py` / `question_generator.py` pair; supports both segment and question generation in a single tool).

## 5. Documentation
Refer to `docs/technical_reference.html` for a full overview of the system architecture and data models.
