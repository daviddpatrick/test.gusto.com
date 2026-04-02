"""Factory for building API client instances used in tests."""

from common.clients.example_api_client import ExampleApiClient
from common.clients.gusto_client import GustoApiClient


class ClientFactory:
    """Creates named API client instances with shared constructor inputs."""

    def create(
        self,
        name,
        base_url,
        logger,
        auth_token=None,
        extra_headers=None,
        request_context=None,
        storage_state=None,
        playwright_timeout_ms=30000,
    ):
        """Builds the requested client instance.

        Args:
            name: Registered client class name.
            base_url: Base URL used by the client.
            logger: Logger instance for request logging.
            auth_token: Optional authorization token.
            extra_headers: Optional extra HTTP headers.
            request_context: Optional Playwright request context.
            storage_state: Optional Playwright storage state.
            playwright_timeout_ms: Request timeout for Playwright-backed clients.

        Returns:
            A configured API client instance.

        Raises:
            ValueError: If the client name is not registered.
        """
        api_clients = {
            "ExampleApiClient": lambda: ExampleApiClient(
                base_url,
                logger,
                auth_token=auth_token,
                extra_headers=extra_headers,
                request_context=request_context,
                storage_state=storage_state,
                playwright_timeout_ms=playwright_timeout_ms,
            ),
            "GustoApiClient": lambda: GustoApiClient(
                base_url,
                logger,
                auth_token=auth_token,
                extra_headers=extra_headers,
                request_context=request_context,
                storage_state=storage_state,
                playwright_timeout_ms=playwright_timeout_ms,
            ),
        }
        try:
            return api_clients[name]()
        except KeyError as exc:
            raise ValueError(f"Invalid client name: {name}") from exc
