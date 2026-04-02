"""Page object for the post-login inventory view."""


class InventoryPage:
    """Models the inventory page shown after successful login."""

    def __init__(self, page):
        self.page = page
        self.inventory_container = page.locator('[data-test="inventory-container"]')
        self.page_title = page.locator('[data-test="title"]')

    def is_loaded(self):
        """Returns whether the inventory view is visible."""
        return self.inventory_container.is_visible()
