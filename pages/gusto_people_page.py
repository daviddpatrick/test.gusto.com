from typing import List, Optional

from pages.data.data_types import Person

class GustoPeoplePage:
    def __init__(self, page):
        self.page = page
        self.header = page.locator("h1", has_text="People")
        self.team_members_table = page.locator("table", has=page.locator("caption", has_text="Team members"))
        self.team_members_body = self.team_members_table.locator("tbody")

    def is_loaded(self):
        return self.header.is_visible()

    def person_row(self, name):
        return self.team_members_body.locator("tr").filter(has=self.page.locator("a", has_text=name))

    def get_person(self, name) -> Optional[Person]:
        row = self.person_row(name).first
        if row.count() == 0:
            return None
        return self._row_to_person(row)

    def get_people(self) -> List[Person]:
        rows = self.team_members_body.locator("tr")
        count = rows.count()
        people = []
        for index in range(count):
            people.append(self._row_to_person(rows.nth(index)))
        return people

    def _row_to_person(self, row) -> Person:
        cells = row.locator("td")
        # Columns: select | name | department | job title | worker type
        name = cells.nth(1).locator("a").inner_text().strip()
        department = cells.nth(2).inner_text().strip()
        job_title = cells.nth(3).inner_text().strip()
        worker_type = cells.nth(4).inner_text().strip()
        return Person(
            name=name,
            department=department,
            job_title=job_title,
            worker_type=worker_type,
        )
