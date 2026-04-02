"""Page object for the example login form."""


class LoginPage:
    """Wraps the login interactions for the demo UI."""

    def __init__(self, page):
        self.page = page

        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.submit_button = page.locator('[data-test="login-button"]')
        self.error_banner = page.locator('[data-test="error"]')

    def navigate(self, url):
        """Opens the login page."""
        self.page.goto(url)

    def enter_username(self, username):
        """Fills the username field."""
        self.username_input.fill(username)

    def enter_password(self, password):
        """Fills the password field."""
        self.password_input.fill(password)

    def submit(self):
        """Submits the login form."""
        self.submit_button.click()

    def login(self, username, password, url):
        """Logs in with the provided credentials."""
        self.navigate(url)
        self.username_input.wait_for(state="visible")
        self.enter_username(username)
        self.enter_password(password)
        self.submit()
