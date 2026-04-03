from playwright.sync_api import Page
from pages.landing_page import LandingPage
from pages.search_page import SearchPage

class TestSearchProduct:

    def test_search_for_a_product(self, page: Page):
        # ------------------------------------
        """Search For A Product"""
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
        landing_page.fill_searchbox()
        landing_page.click_search()

        # Navigate to search page
        search_page = SearchPage(page)
        search_page.verify_page_heading()
        search_page.verify_first_product_name()

