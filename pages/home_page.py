"""Page object for the application's login entry page."""


class HomePage:
    """Models the unauthenticated landing page."""

    def __init__(self, page):
        self.page = page

        self.body = page.locator("body")
        self.login_form = page.locator('[data-test="login-container"]')

    def navigate(self, url):
        """Navigates to the configured home page URL."""
        self.page.goto(url)

    def is_loaded(self):
        """Returns whether the landing page is visibly ready."""
        return self.body.is_visible() and self.login_form.is_visible()
