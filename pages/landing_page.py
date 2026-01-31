from playwright.sync_api import Page, expect
from utils.environment import user_phone_number, user_password


class LandingPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = 'https://www.daraz.com.bd/'
        self.login_popup = page.get_by_role("link", name="Login")
        self.username_input = page.get_by_role("textbox", name="Please enter your Phone or")
        self.password_input = page.get_by_role("textbox", name="Please enter your password")
        self.login_button = page.get_by_role("button", name="LOGIN")

        # Locators After Successful Login
        self.username = page.get_by_text("Ahmed Manan's account")

        # Locators For Search Functionality
        self.searchbox = page.get_by_role("searchbox", name="Search in Daraz")
        self.search_button = page.get_by_role("link", name="SEARCH")

        # Locators for logout
        self.logout_button = page.get_by_role("listitem").filter(has_text="Logout")

    def open_page(self):
        self.page.goto(self.page_url)

    def get_login_popup(self):
        self.login_popup.click()

    def fill_username_password(self):
        self.username_input.fill(user_phone_number)
        self.password_input.fill(user_password)

    def click_login(self):
        self.login_button.click()

    def verify_user_login(self):
        expect(self.username).to_be_visible(timeout=10000)

    def fill_searchbox(self):
        expect(self.searchbox).to_be_visible()
        self.searchbox.fill("Samsung Galaxy S23")

    def click_search(self):
        expect(self.search_button).to_be_visible()
        self.search_button.click()

    def logout(self):
        self.username.click()
        self.logout_button.click()



