from playwright.sync_api import Page, expect
from utils.environment import user_phone_number, user_password


class SearchPage:

    def __init__(self, page: Page):
        self.page = page
        # self.page_url = 'https://www.daraz.com.bd/'
        self.search_heading= page.get_by_role("heading", name="Samsung Galaxy S23")
        self.first_product_name = page.get_by_text("Galaxy S23 Ultra 5G", exact=False)


    def verify_page_heading(self):
        expect(self.search_heading).to_be_visible(timeout=10000)

    def verify_first_product_name(self):
        expect(self.first_product_name.first).to_be_visible(timeout=10000)

    def navigate_to_first_product_page(self):
        self.first_product_name.first.click()