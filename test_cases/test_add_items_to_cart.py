from playwright.sync_api import Page
from pages.landing_page import LandingPage
from pages.search_page import SearchPage
from pages.item_page import ItemPage

class TestAddItemsToCart:

    def test_add_items_to_cart(self, page: Page):
        # ------------------------------------
        """Add Items To Cart"""
        # ------------------------------------

        # Navigate to page
        landing_page = LandingPage(page)
        landing_page.open_page()

        # Perform Login
        landing_page.get_login_popup()
        landing_page.fill_username_password()
        landing_page.click_login()

        # Login Verification
        landing_page.verify_user_login()

        # Search Verification
        # page.get_by_role("searchbox", name="Search in Daraz").click()
        # page.get_by_role("searchbox", name="Search in Daraz").fill("Samsung Galaxy S23")
        landing_page.fill_searchbox()
        landing_page.click_search()

        # Navigate to search page
        search_page = SearchPage(page)
        search_page.verify_page_heading()
        search_page.verify_first_product_name()
        search_page.navigate_to_first_product_page()

        # Navigate to item page
        item_page = ItemPage(page)
        item_page.add_to_cart()
        item_page.verify_add_to_cart()

