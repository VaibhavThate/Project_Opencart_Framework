from playwright.sync_api import Page,expect
import pytest

class Login:
    def __init__(self, page:Page):
        self.page = page
        self.login_page_header = self.page.locator("h2:has-text('Returning Customer')")
        self.Email_field = self.page.get_by_placeholder("E-Mail Address")
        self.password_field = self.page.get_by_placeholder("Password")
        self.btn_login = self.page.locator("//button[normalize-space()='Login']")
        self.error_msg = self.page.locator("#alert")
        self.success_msg = self.page.locator("#content h1")

    def check_login_header(self):
        return self.login_page_header

    def enter_email(self, email: str):
    #fill the email fields with valid/invalid email
        try:
            self.Email_field.fill(email)
        except Exception as e:
            print(f"exception happen while entering the email {e}")
            raise

    def enter_password(self, password: str):
    #fill password field in password valid/invalid
        try:
            self.password_field.fill(password)
        except Exception as e:
            print(f"exception while entering the password {e}")
            raise

    def click_login(self):
        #click the login button
        try:
            self.btn_login.click()
        except Exception as e:
            print(f"exception while the login button click {e}")
            raise

    def check_successful_login(self):
        return self.success_msg


    def invalid_login(self,email: str, password: str):
        #enter the invalid email/password and check with show error toast message
        self.Email_field.fill(email)
        self.password_field.fill(password)
        self.btn_login.click()

    def error_invalid_login(self):
        error = self.error_msg
        expect(error).to_contain_text("Warning:")





