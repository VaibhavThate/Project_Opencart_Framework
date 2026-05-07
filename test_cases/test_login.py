'''
test case
===========
validate the login with valid email and password
validate the successful login message
validate the login with invalid email and invalid password
validate the error message after invalid login
'''

from pages.Login_page import Login
from pages.Homepage import Homepage
from config import Config
import pytest


# validate the login with valid email and password
def test_valid_login(page):
    home_page = Homepage(page)
    login_page = Login(page)
    #click on myaccount button
    home_page.click_my_account()
    #from home page click on the login button
    home_page.click_login()

    #valid email and password field filling
    login_page.enter_email(Config.email)
    login_page.enter_password(Config.password)

    #click on login button
    login_page.click_login()

    #validate the success message
    login_page.check_successful_login()


def test_invalid_login(page):
    login_page = Login(page)
    home_page = Homepage(page)
    # click on myaccount button
    home_page.click_my_account()
    # from home page click on the login button
    home_page.click_login()
    #invalid login
    login_page.invalid_login(Config.invalid_email,Config.invalid_password)
    login_page.error_invalid_login()

