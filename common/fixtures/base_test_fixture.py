"""Shared pytest fixtures for UI and API test suites."""

from datetime import datetime
import logging
import os

import pytest
from common.clients.client_factory import ClientFactory
from common.utils.configs_util import create_directory_if_necessary
from common.utils.configs_util import load_config
from common.utils.env_loader import get_env
from pages.flows.login_flow import LoginFlow
from playwright.sync_api import sync_playwright


class BaseTestFixture:
    """Provides reusable fixtures for browser, config, clients, and logging."""

    @pytest.fixture(scope="session")
    def test_env(self, request):
        """Returns the named test environment from the pytest CLI option."""
        return request.config.getoption(name='--test_env') or "us"

    @pytest.fixture(scope="session")
    def config(self, test_env, session_logger):
        """Loads the active environment configuration for the test session."""
        env_config = load_config(test_env)
        session_logger.info(f"Using these Environment Configs: {env_config}")
        return env_config

    @pytest.fixture(scope="session")
    def clients(self):
        """Builds the API client factory used by tests."""
        return ClientFactory()

    @pytest.fixture(scope="session")
    def session_logger(self, worker_id):
        """Creates a per-session logger that writes to the results directory."""
        result_dir = os.path.join("results")
        create_directory_if_necessary(result_dir)
        logger = self.create_logger(
            result_dir,
            f"Log_{worker_id.capitalize()}_Session.log",
            logger_name="session",
        )
        logger.info("*********************** Session Logging ****************************")
        logger.info("=================================================================")
        start = datetime.now()
        logger.info("Starting test:")
        yield logger

        stop = datetime.now()
        duration = stop - start
        logger.info("Test Duration: %s seconds", duration.total_seconds())
        logger.info("FINISHED")
        logger.info("=================================================================")

    def create_logger(self, result_dir, log_file_name, logger_name="", log_level=None):
        """Creates a file-backed logger for the current test run."""
        logging.getLogger("selenium").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("PIL").setLevel(logging.WARNING)
        logger = logging.getLogger(logger_name)
        logger.handlers = []
        logger.propagate = False
        formatter = logging.Formatter("%(asctime)-22s - %(levelname)-8s %(message)s")
        formatter.datefmt = "%m/%d/%Y %I:%M:%S %p"
        log = os.path.join(result_dir, log_file_name)
        file_handler = logging.FileHandler(log, mode="w")
        file_handler.setFormatter(formatter)
        if log_level is not None:
            logger.setLevel(log_level)
        else:
            logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        return logger

    @pytest.fixture
    def logged_in_page(self, chrome_launch, session_logger, config):
        """Logs in through the UI and returns an authenticated Playwright page."""
        page = chrome_launch
        username = get_env("UI_USERNAME", config.get("ui_username"))
        password = get_env("UI_PASSWORD", config.get("ui_password"))
        if not username or not password:
            raise AssertionError("Missing UI_USERNAME or UI_PASSWORD in config or environment.")
        LoginFlow(page, session_logger).run(username, password, config["ui_base_url"])
        return page

    @pytest.fixture
    def chrome_launch(self):
        """Launches a Chromium browser page for UI tests."""
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=get_env("HEADLESS", "true").lower() == "true",
            )
            context = browser.new_context(viewport={"width": 1440, "height": 960})
            page = context.new_page()

            try:
                yield page
            finally:
                context.close()
                browser.close()
