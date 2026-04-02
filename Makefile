SHELL := /bin/bash

.PHONY: qa prepare-site

qa:
	python3 scripts/qa_textbooks_v5.py
	@echo "QA report: research/qa_textbooks_v5_report.md"

prepare-site:
	./scripts/prepare_site.sh
	@echo "Static site prepared in dist/"
