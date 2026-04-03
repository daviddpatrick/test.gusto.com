from common.fixtures.base_test_fixture import BaseTestFixture
from pages.home_page import HomePage
from pages.flows.login_flow import LoginFlow


class TestUiApiSharedAuth(BaseTestFixture):
    def test_ui_and_api_shared_auth(self, chrome_launch, config, clients, session_logger):
        page = chrome_launch
        home = HomePage(page)
        home.navigate()
        assert home.is_loaded()

        LoginFlow(page, session_logger).run("user@example.com", "password")

        api_client = clients.create(
            name="CoinbaseApiClient",
            base_url=config["coinbase_url"],
            logger=session_logger,
            request_context=page.context.request,
        )
        try:
            response = api_client._get("prices/BTC-USD/spot")
            assert response.ok
        finally:
            api_client.close()
