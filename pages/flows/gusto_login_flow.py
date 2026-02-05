from pages.components.gusto_navbar_component import GustoNavbarComponent
from pages.gusto_login_page import GustoLoginPage
from common.utils.env_loader import get_env

class GustoLoginFlow:
    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger
        self.navbar = GustoNavbarComponent(page)
        self.login_page = GustoLoginPage(page)

    def _log(self, message):
        if self.logger:
            self.logger.info(message)

    def run(self, username, password):
        self._log("Navigating to https://gusto.com")
        self.page.goto(get_env("GUSTO_URL", "https://gusto.com"))
        self._log("Clicking Sign in in navbar")
        self.navbar.click_sign_in()
        self._log("Submitting login form")
        self.login_page.login(username, password)
        return self
