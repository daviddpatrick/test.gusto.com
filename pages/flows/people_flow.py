from pages.components.app_nav_component import AppNavComponent, AppNavItem
from pages.gusto_people_page import GustoPeoplePage


class PeopleFlow:
    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger
        self.nav = AppNavComponent(page)
        self.people_page = GustoPeoplePage(page)

    def _log(self, message):
        if self.logger:
            self.logger.info(message)

    def run(self):
        self._log("Navigating to People page")
        self.nav.click_main(AppNavItem.PEOPLE)
        self.people_page.header.wait_for(state="visible")
        return self.people_page
