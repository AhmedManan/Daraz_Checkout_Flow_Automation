from playwright.sync_api import Page
from pages.landing_page import LandingPage
from pages.search_page import SearchPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage

class TestCheckout:

    def test_checkout(self, page: Page):
        # ------------------------------------
        """Checkout"""
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
        search_page.navigate_to_first_product_page()

        # Navigate to item page
        item_page = ItemPage(page)
        item_page.add_to_cart()
        item_page.verify_add_to_cart()

        # Add other item to cart
        item_page.goto_other_item_page()
        item_page.add_to_cart()
        item_page.verify_add_to_cart()

        # Navigate to cart page
        cart_page = CartPage(page)
        cart_page.goto_to_cart()
        cart_page.remove_item()
        cart_page.check_warning()
        cart_page.confirm_remove()

        # Proceed to checkout
        # cart_page.confirm_first_product()
        # cart_page.proceed_to_checkout()

        # Verify checkout Screen shows correctly

        # Logout
        landing_page.logout()