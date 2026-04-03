from pages.dialogs.cookies_dialog import CookiesDialog
from pages.login_page import LoginPage


class LoginFlow:
    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger
        self.login_page = LoginPage(page)
        self.cookies_dialog = CookiesDialog(page)

    def _log(self, message):
        if self.logger:
            self.logger.info(message)

    def _maybe_handle_cookies(self):
        if self.cookies_dialog.is_visible():
            self._log("Dismissing cookies dialog")
            self.cookies_dialog.dismiss()


    def run(self, username, password, url):
        self.login_page.login(username, password, url)
        self._maybe_handle_cookies()
        return self
