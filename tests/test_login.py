import allure
from playwright.sync_api import expect

from common.fixtures.base_test_fixture import BaseTestFixture
from pages.gusto_login_page import GustoLoginPage


class TestLogin(BaseTestFixture):
    @allure.feature("Authentication")
    @allure.story("Gusto login")
    def test_gusto_login(self, gusto_logged_in_page):
        page = gusto_logged_in_page

        # If login succeeds, the login form should no longer be visible.
        login_page = GustoLoginPage(page)
        assert not login_page.email_input.is_visible()

        welcome_header = page.locator("h1", has_text="Welcome to Gusto, David")
        expect(welcome_header).to_be_visible()
        expect(welcome_header).to_have_text("Welcome to Gusto, David")
        allure.attach(page.screenshot(), name="Welcome to Gusto", attachment_type=allure.attachment_type.PNG)

