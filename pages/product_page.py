from playwright.sync_api import expect,Page
import pytest
import logging
logger = logging.getLogger(__name__)

class ProductPage:
    def __init__(self, page:Page):
        self.page = page
        self.qty_product = self.page.locator("#input-quantity")
        self.btn_add_to_cart = self.page.locator("#button-cart")
        self.added_msg = self.page.locator("#alert .alert")
        self.btn_item_homepage = self.page.locator("button[data-bs-toggle='dropdown']")
        self.btn_view_button = self.page.locator("//strong[normalize-space()='View Cart']")


    def enter_qty_product(self, qty: str):
        self.qty_product.fill("")
        self.qty_product.fill(qty)
        expect(self.qty_product).to_have_value(str(qty))

    def click_add_to_cart(self):
        self.btn_add_to_cart.click()

    def success_toast_msg(self):
        expect(self.added_msg).to_be_visible()
        expect(self.added_msg).to_contain_text(" Success: You have added ")
        print(f"toast message successfully generated")
        # raise Exception(f"toast message not generated")

    def click_item_homepage_button(self):
        self.btn_item_homepage.click()

    def click_view_cart(self):
        self.btn_view_button.click()




