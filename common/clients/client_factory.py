from common.clients.gusto_client import GustoApiClient


class ClientFactory(object):

    def create(self, name, base_url, logger, auth_token=None, extra_headers=None,
               request_context=None, storage_state=None, playwright_timeout_ms=30000):
        while name:
            api_clients = {
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
            except KeyError:
                raise ValueError(f"Invalid client name: {name}")
