from playwright.sync_api import Page, expect
from utils.environment import user_phone_number, user_password


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = 'https://cart.daraz.com.bd/cart'
        self.other_item_remove_locator= page.locator(".lazada.lazada-ic-Delete.lazada-icon.icon.delete").nth(1)
        self.remove_warning_box= page.get_by_text("Remove from cart")
        self.confirm_remove_button = page.get_by_role("button", name="REMOVE")
        self.product_checkbox = page.locator("xpath=/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/label/input")
        self.proceed_to_checkout_button = page.get_by_role("button", name="PROCEED TO CHECKOUT (1)")


    def goto_to_cart(self):
        self.page.goto(self.page_url)

    def remove_item(self):
        expect(self.other_item_remove_locator).to_be_visible()
        self.other_item_remove_locator.click()

    def check_warning(self):
        expect(self.remove_warning_box).to_be_visible()

    def confirm_remove(self):
        expect(self.confirm_remove_button).to_be_visible()
        # expect(self.confirm_remove_button).to_be_clickable()
        self.confirm_remove_button.click()

    def confirm_first_product(self):
        expect(self.product_checkbox).to_be_visible()
        self.product_checkbox.check()
        # self.page.wait_for_timeout(1000)

    def proceed_to_checkout(self):
        expect(self.proceed_to_checkout_button).to_be_visible()
        self.proceed_to_checkout_button.click()
