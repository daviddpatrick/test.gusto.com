class CookiesDialog:
    def __init__(self, page):
        self.page = page
        self.dismiss_button = page.locator('[data-testid="dismiss-button"]')

    def is_visible(self):
        return self.dismiss_button.is_visible()

    def dismiss(self):
        if self.dismiss_button.is_visible():
            self.dismiss_button.click()
