from pages.components.gusto_navbar_component import GustoNavbarComponent
from common.utils.env_loader import get_env


class GustoHomePage:
    def __init__(self, page):
        self.page = page
        self.navbar = GustoNavbarComponent(page)

    def navigate(self):
        self.page.goto(get_env("GUSTO_TEST_URL", "https://test.gusto.com"))

    def is_loaded(self):
        return self.navbar.root.is_visible()
