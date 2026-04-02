import pytest
from playwright.sync_api import expect

from common.fixtures.base_test_fixture import BaseTestFixture
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
class TestUi(BaseTestFixture):
    """UI smoke tests for the model repository."""

    def test_login_flow_reaches_inventory(self, logged_in_page):
        """Verifies that valid credentials reach the post-login page."""
        inventory_page = InventoryPage(logged_in_page)
        expect(inventory_page.inventory_container).to_be_visible()
        expect(inventory_page.page_title).to_have_text("Products")

    def test_home_page_loads(self, chrome_launch, config):
        """Verifies that the login page loads successfully."""
        home_page = HomePage(chrome_launch)
        home_page.navigate(config["ui_base_url"])
        assert home_page.is_loaded()
