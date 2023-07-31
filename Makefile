SHELL := /usr/bin/zsh

install:
	source ./venv/bin/activate; \
	pip install -r requirements.txt; \
  