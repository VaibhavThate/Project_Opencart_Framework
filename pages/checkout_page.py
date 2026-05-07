from playwright.sync_api import Page, expect, Playwright
from utilities.data_reader import read_json_data
import pytest
test_data = read_json_data("test_data/checkout_data.json")
class CheckoutPage:
    def __init__(self, page:Page):
        self.page = page
        self.checkout_header_text = self.page.locator("h1:has-text('Checkout')")
        self.fname_checkout = self.page.get_by_placeholder("First Name")
        self.lname_checkout = self.page.get_by_placeholder("Last Name")
        self.address_1_checkout = self.page.get_by_placeholder("Address 1")
        self.city_checkout = self.page.get_by_placeholder("City")
        self.post_code_checkout = self.page.get_by_placeholder("Post Code")
        self.country_checkout = self.page.locator("#input-shipping-country")
        self.reginal_state_checkout = self.page.locator("#input-shipping-zone")
        self.shipping_choose = self.page.locator("#button-shipping-methods")
        self.payment_choose = self.page.locator("#button-payment-methods")
        self.shipping_error_msg = self.page.locator("#error-shipping-method")
        self.payment_error_msg = self.page.locator("#error-payment-method")
        self.comment_box = self.page.locator("#input-comment")
        self.product_info = self.page.locator(".table.table-bordered.table-hover tbody tr td:nth-child(2)")
        self.total_amount = self.page.locator("//table[contains(@class,'table')]//tr[last()]/td[@class='text-end']")

    def check_header_checkout(self):
        return self.checkout_header_text

    def enter_fname(self):
        self.fname_checkout.fill("mumbai")

    def enter_lname(self):
        self.lname_checkout.fill("Indians")

    def enter_address_checkout(self):
        self.address_1_checkout.fill("test")

    def enter_city(self):
        self.city_checkout.fill("Mumbai")

    def enter_post_code(self):
        self.post_code_checkout.fill("413606")

    def select_country_checkout(self):
        self.country_checkout.select_option("India")

    def select_state_checkout(self):
        self.reginal_state_checkout.select_option("Maharashtra")

    def click_shipping_btn(self):
        self.shipping_choose.click()

    def error_msg_shipping(self):
        return self.shipping_error_msg

    def error_msg_payment(self):
        return self.payment_error_msg

    def click_payment_btn(self):
        self.payment_choose.click()

    def add_comment_box(self):
        self.comment_box.fill("test")


    def check_product_price(self, product_1_price: float, product_2_price: float):
        count = self.product_info.count()
        print(count)
        product_prices = []
        for i in range(count):
            price = self.product_info.nth(i).inner_text().strip()
            clean_value = float(price.replace("$","").replace(",",""))
            print(clean_value)
            product_prices.append(clean_value)

        print(f"here is the product prices {product_prices}")

        assert product_1_price in product_prices, f"{product_1_price} not in {product_prices}"
        assert product_2_price in product_prices, f"{product_2_price} not in {product_prices}"




