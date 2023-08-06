.ONESHELL:

.SHELLFLAGS := -euo pipefail -c
SHELL := bash

venv:
	python3.10 -m venv venv
	source venv/bin/activate
	pip install -r requirements-dev.txt

.PHONY: devenv
devenv: venv
	source venv/bin/activate
	mypy --install-types

.PHONY: manual
manual: venv clean_manual
	source venv/bin/activate
	sphinx-build docs pages

.PHONY: clean_manual
clean_manual:
	rm -rf pages

.PHONY: build
build:
	rm dist/*
	flit build

.PHONY: publish_test
publish_test: build
	twine upload --repository testpypi dist/*

.PHONY: publish
publish: build
	twine upload --repository pypi dist/*

.PHONY: test
test: build
	tox -p
