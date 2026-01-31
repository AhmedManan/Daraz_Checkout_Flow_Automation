from playwright.sync_api import Page, expect
from utils.environment import user_phone_number, user_password


class ItemPage:

    def __init__(self, page: Page):
        self.page = page
        self.other_item_page_url = 'https://www.daraz.com.bd/products/samsung-galaxy-samsung-ultra-i488055775-s2361324723.html'
        self.add_to_cart_button= page.get_by_role("button", name="Add to Cart")
        self.add_to_cart_popup_text = page.locator("#dialog-body-1 div").filter(has_text="Added to cart successfully!").nth(4)


    def add_to_cart(self):
        expect(self.add_to_cart_button).to_be_visible()
        self.add_to_cart_button.click()

    def verify_add_to_cart(self):
        expect(self.add_to_cart_popup_text).to_be_visible()

    def goto_other_item_page(self):
        self.page.goto(self.other_item_page_url)