from playwright.sync_api import Page, expect
import pytest

class Homepage:
    def __init__(self, page: Page):
    #with the constructor selecting the specific locator
        self.page = page
        self.my_account = self.page.locator("span:has-text('My Account')")
        self.btn_register = self.page.locator(".dropdown-item:has-text('Register')")
        self.btn_login = self.page.locator(".dropdown-item:has-text('Login')")
        self.search_box = self.page.get_by_placeholder("Search")
        self.btn_search = self.page.locator("button[class='btn btn-light btn-lg']")
        self.item_cart_btn = self.page.locator("button[class='btn btn-lg btn-dark d-block dropdown-toggle']")
        self.empty_cart_msg = self.page.locator("li.text-center.p-4")
        self.remove_item_cart_btn = self.page.locator("tbody tr td button[title='Remove']")
        self.item_remove_msg_from_cart = self.page.locator("#alert div.alert")
    def click_my_account(self):
        #click on the my account link
        try:
            self.my_account.click()
        except Exception as e:
            print(f"Exception happen while click on my account : {e}")
            raise

    def click_register(self):
        #function to click on the register button
        try:
            self.btn_register.click()
        except Exception as e:
            print(f"Exception happen while click register button : {e}")
            raise

    def click_login(self):
        #click on logi button
        try:
            self.btn_login.click()
        except Exception as e:
            print(f"login failed : {e}")
            raise

    def enter_search_box(self, product_name: str):
        #enter the product name into the search box
        try:
            self.search_box.fill(product_name)
        except Exception as e:
            print(f"search box failed {e}")
            raise

    def click_search(self):
        #click on the search button
        try:
            self.btn_search.click()
        except Exception as e:
            print(f"search button failed {e}")
            raise

    def click_item_cart(self):
        self.item_cart_btn.click()

    def check_empty_cart_msg(self):
        return self.empty_cart_msg

    def clear_item_cart(self,page:Page):

        while True:
            count = self.remove_item_cart_btn.count()

            if count == 0:
                break
            self.item_cart_btn.click()
            self.remove_item_cart_btn.nth(0).click()

            expect(self.item_remove_msg_from_cart).to_contain_text(
                "Success: You have removed"
            )

            page.wait_for_timeout(1000)

    def check_item_remove_mag(self):
        return self.item_remove_msg_from_cart

