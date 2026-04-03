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
	clear
	$(PIP) install -r requirements.txt

test: $(VENV)
	clear
	-$(PYTHON) -m pytest tests --test_env=$(TESTENV) -W ignore::Warning;
	sleep 5;
	allure serve allure-results;

test-login: $(VENV)
	clear
	-$(PYTHON) -m pytest tests/test_login.py --test_env=$(TESTENV) -W ignore::Warning;

test-people: $(VENV)
	clear
	-$(PYTHON) -m pytest tests/test_people.py --test_env=$(TESTENV) -W ignore::Warning;

report:
	clear
	allure generate allure-results -o allure-report --clean
	allure open allure-report
