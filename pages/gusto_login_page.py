class GustoLoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.locator("input#email[name='username']")
        self.password_input = page.locator("input#password[name='password']")
        self.continue_button = page.locator("button[name='btn-login']")

    def is_loaded(self):
        return self.email_input.is_visible()

    def login(self, username, password):
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.continue_button.click()
