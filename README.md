# UI + API Test Model Repo

This repository is now a Python `pytest` + Playwright starter for teams that want one place to keep:

- UI browser tests
- API tests
- shared-auth tests that reuse browser login state for backend calls

The default sample setup uses public demo targets so the structure is easy to understand:

- UI demo app: `https://www.saucedemo.com`
- API demo app: `https://jsonplaceholder.typicode.com`

## What the repo shows

- `tests/test_ui.py`: basic UI smoke coverage
- `tests/test_api.py`: direct API coverage through a reusable client
- `tests/test_ui_api_shared_auth.py`: the pattern for taking browser auth and reusing it in API requests
- `pages/`: page objects and UI flows
- `common/clients/`: reusable API clients
- `common/fixtures/`: shared pytest fixtures for browser, config, clients, and logging

## Quick start

```bash
make setup
make test
```

Run specific suites:

```bash
make test-ui
make test-api
make test-shared-auth
```

Generate an Allure report after a run:

```bash
make report
```

## Configuration

Base config lives in [common/config/us.json](/Users/davidpatrick/test.framework.com/common/config/us.json). You can either edit that file or override values with a local `.env`.

Supported environment variables:

```bash
UI_BASE_URL=https://your-ui-app.example.com
API_BASE_URL=https://your-api.example.com
UI_USERNAME=your_username
UI_PASSWORD=your_password
HEADLESS=true
SHARED_AUTH_BASE_URL=https://your-ui-app.example.com
SHARED_AUTH_ENDPOINT=/api/me
SHARED_AUTH_EXPECTED_TEXT=expected-string
```

## Adapting this to your app

1. Replace the demo selectors in [pages/login_page.py](/Users/davidpatrick/test.framework.com/pages/login_page.py) and [pages/inventory_page.py](/Users/davidpatrick/test.framework.com/pages/inventory_page.py).
2. Update the endpoints in [common/clients/example_api_client.py](/Users/davidpatrick/test.framework.com/common/clients/example_api_client.py).
3. Change config values in [common/config/us.json](/Users/davidpatrick/test.framework.com/common/config/us.json).
4. Turn on the shared-auth example by setting `"shared_auth_enabled": true` once your app exposes an authenticated endpoint that works with browser session cookies.

## Notes

- Generated artifacts such as `allure-results/` and `results/` should stay out of version control.
- The shared-auth test is intentionally skipped by default because every app exposes authenticated APIs differently.
