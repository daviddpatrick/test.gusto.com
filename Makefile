ENV ?= venv
VENV ?= venv
PYTHON = $(VENV)/bin/python3
PIP = $(PYTHON) -m pip
TESTENV ?= us

default: test

setup:
	rm -rf $(VENV)
	python3.11 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt
	echo $(CURDIR)/$(VENV)

build: $(VENV)
	$(PIP) install -r requirements.txt

test: $(VENV)
	$(PYTHON) -m pytest tests --test_env=$(TESTENV) -W ignore::Warning

test-ui: $(VENV)
	$(PYTHON) -m pytest tests/test_ui.py -m ui --test_env=$(TESTENV) -W ignore::Warning

test-api: $(VENV)
	$(PYTHON) -m pytest tests/test_api.py -m api --test_env=$(TESTENV) -W ignore::Warning

test-shared-auth: $(VENV)
	$(PYTHON) -m pytest tests/test_ui_api_shared_auth.py -m shared_auth --test_env=$(TESTENV) -W ignore::Warning

report:
	allure generate allure-results -o allure-report --clean
