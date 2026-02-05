ENV ?= venv
VENV ?= venv
PIP = $(VENV)/bin/pip3
PYTHON = $(VENV)/bin/python3
TESTENV ?= us

default: test

setup:
	python3 -m venv $(VENV)
	echo $(CURDIR)/$(VENV)

build: $(VENV)
	clear
	$(PIP) install -r requirements.txt

test: $(VENV)
	clear
	-$(PYTHON) -m pytest tests --test_env=$(TESTENV) --alluredir=allure-results -W ignore::Warning;
	sleep 5;
	allure serve allure-results;

test-login: $(VENV)
	clear
	-$(PYTHON) -m pytest tests/test_login.py --test_env=$(TESTENV) --alluredir=allure-results -W ignore::Warning;

test-people: $(VENV)
	clear
	-$(PYTHON) -m pytest tests/test_people.py --test_env=$(TESTENV) --alluredir=allure-results -W ignore::Warning;

report:
	clear
	allure generate allure-results -o allure-report --clean
	allure open allure-report
