class HomePage:
    def __init__(self, page):
        self.page = page

        self.body = page.locator("body")

    def navigate(self):
        self.page.goto("https://www.coinbase.com")

    def is_loaded(self):
        return self.body.is_visible()
