from playwright.sync_api import Page,Playwright,expect
# from utilities.randon_data_utility import RandomDataUtil
import pytest

class Register:
    def __init__(self, page:Page):
        self.page = page

        #locators
        self.reg_header = self.page.locator("div h1:has-text('Register Account')")
        self.reg_firstname = self.page.locator("#input-firstname")
        self.reg_lastname = self.page.locator("#input-lastname")
        self.reg_email = self.page.locator("#input-email")
        self.reg_password = self.page.locator("#input-password")

        #checkbox and privacy
        self.reg_policy = self.page.locator("input[name='agree']")

        #continue button
        self.reg_continue = self.page.get_by_role("button", name="Continue")

        #confimation msg after successful registration
        self.confirm_msg = self.page.locator("h1:has-text('Your Account Has Been Created!')")

    def get_header_msg(self):
        return self.reg_header

    def set_first_name(self, fname: str):
        self.reg_firstname.fill(fname)

    def set_last_name(self, lname: str):
        self.reg_lastname.fill(lname)

    def set_email(self, email: str):
        self.reg_email.fill(email)

    def set_password(self, password: str):
        self.reg_password.fill(password)

    def set_privacy_policy(self):
        self.reg_policy.click()

    def click_continue(self):
        self.reg_continue.click()

    def get_confirmation_msg(self):
        return self.confirm_msg

