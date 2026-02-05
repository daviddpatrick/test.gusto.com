import allure
from playwright.sync_api import expect
from common.fixtures.base_test_fixture import BaseTestFixture
from pages.flows.people_flow import PeopleFlow
from pages.gusto_app_page import GustoAppPage


class TestPeople(BaseTestFixture):
    def _arrive_on_people_page(self, gusto_logged_in_page, session_logger):
        page = gusto_logged_in_page
        people_page = PeopleFlow(page, session_logger).run()
        mike_row = people_page.person_row("Mike Johnson")
        expect(mike_row).to_be_visible()
        allure.attach(page.screenshot(), name="People Page", attachment_type=allure.attachment_type.PNG)
        return page

    def _get_auth(self, page):
        app_page = GustoAppPage(page)
        csrf_token = app_page.get_csrf_token()
        role_id = app_page.get_role_id()
        if not csrf_token:
            raise AssertionError("Missing CSRF token for MembersTable fetch.")
        if not role_id:
            raise AssertionError("Missing role_id for MembersTable fetch.")
        return csrf_token, role_id

    @allure.feature("People")
    @allure.story("Members table va UI and request")
    def test_people_includes_mike_johnson_request(self, gusto_logged_in_page, clients, session_logger):
        page = self._arrive_on_people_page(gusto_logged_in_page, session_logger)
        csrf_token, role_id = self._get_auth(page)

        gusto_client = clients.create(
            name="GustoApiClient",
            base_url="https://graphql.app.gusto.com",
            logger=session_logger,
            request_context=page.context.request,
        )
        data = gusto_client.members_table_via_request(
            csrf_token=csrf_token,
            role_id=role_id,
        ).json()
        assert data.get("data", {}).get("company") is not None, f"MembersTable failed: {data}"
        members = data["data"]["company"]["members"]["nodes"]
        assert any(member.get("preferredFullName") == "Mike Johnson" for member in members)

    @allure.feature("People")
    @allure.story("Members table va UI and browser")
    def test_people_includes_mike_johnson_browser(self, gusto_logged_in_page, clients, session_logger):
        page = self._arrive_on_people_page(gusto_logged_in_page, session_logger)
        csrf_token, role_id = self._get_auth(page)

        gusto_client = clients.create(
            name="GustoApiClient",
            base_url="https://graphql.app.gusto.com",
            logger=session_logger,
            request_context=page.context.request,
        )
        data = gusto_client.members_table_via_browser(
            page=page,
            csrf_token=csrf_token,
            role_id=role_id,
        )
        assert data.get("data", {}).get("company") is not None, f"MembersTable failed: {data}"
        members = data["data"]["company"]["members"]["nodes"]
        assert any(member.get("preferredFullName") == "Mike Johnson" for member in members)
