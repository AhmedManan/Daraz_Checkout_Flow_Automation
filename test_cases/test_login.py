from playwright.sync_api import Page
from pages.landing_page import LandingPage

class TestLogin:

    def test_verify_login_functionality(self, page: Page):
        # ------------------------------------
        """Verify Login Functionality With Valid Credentials"""
        # ------------------------------------

        # Navigate to page
        landing_page = LandingPage(page)
        landing_page.open_page()

        # Perform Login
        landing_page.get_login_popup()
        landing_page.fill_username_password()
        landing_page.click_login()

        # Verification
        landing_page.verify_user_login()

