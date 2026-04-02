"""Reusable UI flow for logging into the application."""

from pages.login_page import LoginPage


class LoginFlow:
    """Encapsulates the login journey for UI tests."""

    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger
        self.login_page = LoginPage(page)

    def _log(self, message):
        if self.logger:
            self.logger.info(message)

    def run(self, username, password, url):
        """Executes the login flow and returns the flow object."""
        self.login_page.login(username, password, url)
        self._log("Login submitted")
        return self
