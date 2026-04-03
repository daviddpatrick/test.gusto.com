# test.gusto.com


## Run Code:
To run the pytest tests, run the following Makefile commands from the root directory of the project:

	make setup
	make build
	make test

## Makefile Commands Explained:
### Make setup
This command will create a virtual environment.

### Make build
This command will install the required packages.

### Make test
This command will run all pytest tests and also generate an Allure report. The report should bring up a browser window.

## Allure Setup
Install the Allure Python plugin and CLI:

	pip install allure-pytest
	brew install allure

## Environment Variables
Create a `.env` file in the project root with the required credentials and URLs:

	GUSTO_USERNAME=your_email
	GUSTO_PASSWORD=your_password
	GUSTO_URL=https://gusto.com
	GUSTO_TEST_URL=https://test.gusto.com

## Notes
Playwright is configured to run headed with `no_viewport=True` for stability on Gusto.
