from enum import Enum


class AppNavItem(Enum):
    HOME = "home"
    PEOPLE = "people"
    PAY = "pay"
    REPORTS = "reports"
    TAXES_TOGGLE = "taxes_toggle"
    TIME_TOGGLE = "time_toggle"
    BENEFITS = "benefits"
    DOCUMENTS = "documents"
    MONEY = "money"


class AppNavComponent:
    def __init__(self, page):
        self.page = page
        self.root = page.locator("nav#app-nav")

        self.home = self.root.locator("a[data-analytics-name='Home']")
        self.people = self.root.locator("a[data-analytics-name='People']")
        self.pay = self.root.locator("a[data-analytics-name='Pay']")
        self.reports = self.root.locator("a[data-analytics-name='Reports']")
        self.taxes_toggle = self.root.locator("button[data-analytics-name='Taxes & compliance']")
        self.time_toggle = self.root.locator("button[data-analytics-name='Time & attendance']")
        self.benefits = self.root.locator("a[data-analytics-name='Benefits']")
        self.documents = self.root.locator("a[data-analytics-name='Documents']")
        self.money = self.root.locator("a[data-analytics-name='Money']")

        self.people_items = {
            "hiring": self.root.locator("a[data-analytics-name='Hiring']"),
            "learning": self.root.locator("a[data-analytics-name='Learning']"),
        }

        self.taxes_items = {
            "tax_setup": self.root.locator("a[data-analytics-name='Tax setup']"),
            "tax_documents": self.root.locator("a[data-analytics-name='Tax documents']"),
            "tax_credits": self.root.locator("a[data-analytics-name='Tax credits']"),
            "business_insurance": self.root.locator("a[data-analytics-name='Business insurance']"),
        }

        self.time_items = {
            "time_off": self.root.locator("a[data-analytics-name='Time off']"),
        }

        self.money_items = {
            "bill_pay": self.root.locator("a[data-analytics-name='Bill pay']"),
            "invoicing": self.root.locator("a[data-analytics-name='Invoicing']"),
        }

        self.support_items = {
            "refer_earn": self.root.locator("a[data-analytics-name='Refer & earn']"),
            "app_directory": self.root.locator("a[data-analytics-name='App directory']"),
            "company_profile": self.root.locator("a[data-analytics-name='Company profile']"),
        }

    def click_main(self, name: AppNavItem):
        targets = {
            AppNavItem.HOME: self.home,
            AppNavItem.PEOPLE: self.people,
            AppNavItem.PAY: self.pay,
            AppNavItem.REPORTS: self.reports,
            AppNavItem.TAXES_TOGGLE: self.taxes_toggle,
            AppNavItem.TIME_TOGGLE: self.time_toggle,
            AppNavItem.BENEFITS: self.benefits,
            AppNavItem.DOCUMENTS: self.documents,
            AppNavItem.MONEY: self.money,
        }
        targets[name].click()

    def click_people_item(self, name):
        self.people_items[name].click()

    def click_taxes_item(self, name):
        self.taxes_items[name].click()

    def click_time_item(self, name):
        self.time_items[name].click()

    def click_money_item(self, name):
        self.money_items[name].click()

    def click_support_item(self, name):
        self.support_items[name].click()
