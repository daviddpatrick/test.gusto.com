import pytest

from common.fixtures.base_test_fixture import BaseTestFixture


@pytest.mark.api
class TestApi(BaseTestFixture):
    """API smoke tests for the model repository."""

    def test_get_post(self, config, clients, session_logger):
        """Verifies that the example API client can fetch a resource."""
        api_client = clients.create(
            name="ExampleApiClient",
            base_url=config["api_base_url"],
            logger=session_logger,
        )

        try:
            response = api_client.get_post(1)
            assert response.status_code == 200

            body = response.json()
            assert body["id"] == 1
            assert "title" in body
        finally:
            api_client.close()
