class LoginPage:
    def __init__(self, page):
        self.page = page

        self.email_input = page.locator('[data-testid="email-input"]')
        self.email_submit = page.locator('[data-testid="email-submit-button"]')
        self.password_input = page.locator('[data-testid="password-input"]')
        self.password_submit = page.locator('[data-testid="password-submit-button"]')
        self.email_button = page.locator('[data-testid="email-button"]')

    def navigate(self, url):
        self.page.goto(url)

    def enter_email(self, email):
        self.email_input.fill(email)

    def continue_from_email(self):
        self.email_submit.click()

    def enter_password(self, password):
        self.password_input.fill(password)

    def submit_password(self):
        self.password_submit.click()

    def login(self, email, password, url):
        self.navigate(url)
        self.enter_email(email)
        self.continue_from_email()
        self.password_input.wait_for(state="visible")
        self.enter_password(password)
        self.submit_password()
