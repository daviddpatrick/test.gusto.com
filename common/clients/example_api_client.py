"""Example API client used by the model test repository."""

from common.http_base.http_base import HttpClientBase


class ExampleApiClient(HttpClientBase):
    """Provides simple example endpoints for API and shared-auth tests."""

    def __init__(
        self,
        base_url,
        logger,
        auth_token=None,
        http_timeout=(5, 30),
        content_type="application/json",
        extra_headers=None,
        request_context=None,
        storage_state=None,
        playwright_timeout_ms=30000,
    ):
        super().__init__(
            base_url=base_url,
            logger=logger,
            auth_token=auth_token,
            http_timeout=http_timeout,
            content_type=content_type,
            extra_headers=extra_headers,
            request_context=request_context,
            storage_state=storage_state,
            playwright_timeout_ms=playwright_timeout_ms,
        )
        self.logger.info("Example API Client")

    def get_post(self, post_id=1):
        """Fetches a sample post resource by ID."""
        return self._get(f"posts/{post_id}")

    def get_authenticated_resource(self, endpoint):
        """Fetches an authenticated resource using the current session state."""
        return self._get(endpoint.lstrip("/"))
