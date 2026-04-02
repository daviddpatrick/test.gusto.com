import pytest

from common.fixtures.base_test_fixture import BaseTestFixture


@pytest.mark.shared_auth
class TestUiApiSharedAuth(BaseTestFixture):
    """Examples for reusing UI authentication in API requests."""

    def test_ui_and_api_shared_auth(self, logged_in_page, config, clients, session_logger):
        """Uses browser storage state to call an authenticated endpoint."""
        if not config.get("shared_auth_enabled"):
            pytest.skip("Enable shared_auth_enabled in common/config/us.json to exercise this pattern.")

        storage_state = logged_in_page.context.storage_state()
        api_client = clients.create(
            name="ExampleApiClient",
            base_url=config["shared_auth_base_url"],
            logger=session_logger,
            storage_state=storage_state,
        )

        try:
            response = api_client.get_authenticated_resource(config["shared_auth_endpoint"])
            assert response.ok

            expected_text = config.get("shared_auth_expected_text")
            if expected_text:
                assert expected_text in response.text
        finally:
            api_client.close()
