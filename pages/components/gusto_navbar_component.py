class GustoNavbarComponent:
    def __init__(self, page):
        self.page = page
        self.root = page.locator("section#gusto-navbar")
        self.logo = page.locator("img.gusto-logo")

        self.why_gusto = page.locator("#header-nav_item_desktop-why_gusto")
        self.products_toggle = page.locator("#Products-container")
        self.solutions_toggle = page.locator("#Solutions-container")
        self.accountants_toggle = page.locator("#Accountants-container")
        self.resources_toggle = page.locator("#Resources-container")
        self.pricing = page.locator("#header-nav_item_desktop-pricing")
        self.sign_in = self.root.locator("a[data-identifier='button-sign_in-https_app_gusto_com_login']")
        self.mobile_menu = page.locator("#gusto-mobile-menu")
        self.mobile_sign_in = self.mobile_menu.get_by_role("link", name="Sign in")
        self.burger_toggle = page.locator("#gusto-burger-col")

        self.products_items = {
            "payroll": page.locator("#header-nav_item_desktop-payroll"),
            "time": page.locator("#header-nav_item_desktop-time"),
            "workers_comp": page.locator("#header-nav_item_desktop-workers-comp"),
            "employee_benefits": page.locator("#header-nav_item_desktop-employee-benefits"),
            "hiring_onboarding": page.locator("#header-nav_item_desktop-hiring-onboarding"),
            "integrations": page.locator("#header-nav_item_desktop-integrations"),
            "hr": page.locator("#header-nav_item_desktop-hr"),
            "talent_management": page.locator("#header-nav_item_desktop-talent-management"),
            "compare": page.locator("#header-nav_item_desktop-compare"),
            "gusto_money": page.locator("#header-nav_item_desktop-gusto-money"),
            "insights": page.locator("#header-nav_item_desktop-insights"),
            "gusto_global": page.locator("#header-nav_item_desktop-remote-and-global-teams"),
        }

        self.solutions_items = {
            "one_employee": page.locator("#header-nav_item_desktop-one-employee"),
            "new_businesses": page.locator("#header-nav_item_desktop-new-businesses-and-startups"),
            "small_business": page.locator("#header-nav_item_desktop-small-business"),
            "switching_providers": page.locator("#header-nav_item_desktop-switching-providers"),
            "mid_size_businesses": page.locator("#header-nav_item_desktop-mid-size-businesses"),
            "contractors_only": page.locator("#header-nav_item_desktop-contractors-only"),
            "technology": page.locator("#header-nav_item_desktop-tech"),
            "real_estate": page.locator("#header-nav_item_desktop-real-estate"),
            "professional_services": page.locator("#header-nav_item_desktop-professional-services"),
            "healthcare": page.locator("#header-nav_item_desktop-healthcare"),
            "dentists": page.locator("#header-nav_item_desktop-dentists"),
            "retail": page.locator("#header-nav_item_desktop-retail"),
            "manufacturing": page.locator("#header-nav_item_desktop-manufacturing"),
            "construction": page.locator("#header-nav_item_desktop-construction"),
            "view_more_industries": page.locator("#header-nav_item_desktop-view-more-industries"),
            "explore_all_solutions": page.locator("#header-nav_item_desktop-explore_all_solutions"),
        }

        self.accountants_items = {
            "become_a_partner": page.locator("#header-nav_item_desktop-become_a_partner"),
            "partner_community": page.locator("#header-nav_item_desktop-partner_community"),
            "gusto_pro_dashboard": page.locator("#header-nav_item_desktop-gusto_pro_dashboard"),
            "professional_development": page.locator("#header-nav_item_desktop-professional_development"),
            "accountant_blog": page.locator("#header-nav_item_desktop-accountant_blog"),
            "resources": page.locator("#header-nav_item_desktop-resources"),
        }

        self.resources_items = {
            "about_gusto": page.locator("#header-nav_item_desktop-about_gusto"),
            "talk_shop_blog": page.locator("#header-nav_item_desktop-talk_shop_blog"),
            "help_center": page.locator("#header-nav_item_desktop-help_center"),
            "company_news": page.locator("#header-nav_item_desktop-company_news"),
            "gusto_insights": page.locator("#header-nav_item_desktop-gusto_insights"),
            "support_log_in": page.locator("#header-nav_item_desktop-support_log_in"),
            "careers": page.locator("#header-nav_item_desktop-careers_we_re_hiring"),
            "tools_and_calculators": page.locator("#header-nav_item_desktop-tools_and_calculators"),
            "gusto_embedded_payroll": page.locator("#header-nav_item_desktop-gusto_embedded_payroll"),
            "pay_insights": page.locator("#header-nav_item_desktop-pay"),
        }

    def click_main(self, name):
        targets = {
            "why_gusto": self.why_gusto,
            "products": self.products_toggle,
            "solutions": self.solutions_toggle,
            "accountants": self.accountants_toggle,
            "resources": self.resources_toggle,
            "pricing": self.pricing,
        }
        targets[name].click()

    def click_products_item(self, name):
        self.products_items[name].click()

    def click_solutions_item(self, name):
        self.solutions_items[name].click()

    def click_accountants_item(self, name):
        self.accountants_items[name].click()

    def click_resources_item(self, name):
        self.resources_items[name].click()

    def click_sign_in(self):
        if self.sign_in.first.is_visible():
            self.sign_in.first.click()
            return
        fallback_sign_in = self.page.get_by_role("link", name="Sign in").first
        if fallback_sign_in.is_visible():
            fallback_sign_in.click()
            return
        if self.burger_toggle.is_visible():
            self.burger_toggle.click()
        self.mobile_sign_in.wait_for(state="visible")
        self.mobile_sign_in.click()
