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







