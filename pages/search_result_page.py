from playwright.sync_api import Page,expect
import logging
logger = logging.getLogger(__name__)
import pytest

class SRP_page:
    def __init__(self, page:Page):
        self.page = page
        self.header_part = self.page.locator("h1")
        self.product_list = self.page.locator("#product-list .product-thumb")
        self.product_names = self.page.locator(".description h4 a")

    def header_text(self, product_name: str):
        #header text should be present
        logger.info(f"validating the product heading on srp page: {product_name}")
        header = self.header_part
        expect(header).to_have_text(f"Search - {product_name}")

    def product_count(self):
        #counting the product available on srp page
        try:
            count = self.product_list.count()
            print(f"the total count of product on srp page are: {count}")
            return count
        except Exception:
            logger.exception(f"exception occured while product count")
            raise

    def product_name(self):
        #print the all product name available on srp page
        try:
            count = self.product_list.count()
            for i in range(count):
                product = self.product_list.nth(i)
                name = product.locator(".description h4 a").inner_text()
                print(f"product name available on srp page are: {name}")
        except Exception:
            logger.exception(f"exception for product_name")
            raise


    def click_product(self, product_name: str):
        try:
            count = self.product_names.count()

            for i in range(count):
                name = self.product_names.nth(i).inner_text()
                if name == product_name:
                    self.product_names.nth(i).click()
                    break
            # print(f"Product '{product_name}' not found")
            # raise Exception(f"{product_name} not found on SRP page")
        except Exception:
            logger.exception(f"product select is failed or product not found")
            raise


