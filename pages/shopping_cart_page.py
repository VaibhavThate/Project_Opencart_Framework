from playwright.sync_api import Page,expect
import pytest
import logging
logger = logging.getLogger(__name__)

class ShoppingCartPage:
    def __init__(self, page:Page):
        self.page = page
        self.product_info = self.page.locator(".table-responsive .table tbody tr")
        self.total_product_price = self.page.locator("//tfoot[@id='checkout-total']//tr[td[normalize-space()='Total']]/td[last()]")
        self.btn_checkout = self.page.locator("a[class='btn btn-primary']")

    def get_product_name(self, product_name: str):
        count = self.product_info.count()
        print(f"here is the count: {count}")
        product_list = []
        for i in range(count):
            name = self.product_info.nth(i).locator("td:nth-child(2) a").inner_text()
            product_list.append(name)
        print(f"here is the product names: {product_list}")

        if product_name in product_list:
            print(f"product name is available in cart")

        return product_list


    def check_added_qty(self,qty: str):
        count = self.product_info.count()
        qty_list = []
        for i in range(count):
            all_qty = self.product_info.nth(i).locator("td:nth-child(3) input[name='quantity']").input_value()
            qty_list.append(all_qty)

        if qty in qty_list:
            print("the product quantity is available")

        return qty_list

    def check_total_price(self,total_price: str):
        total = self.total_product_price.inner_text()
        return total

    def click_checkout_button(self):
        self.btn_checkout.click()









