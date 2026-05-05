'''
test cases
============
validate all the mandatory fields and fill
validate the privacy
validate the continue button
'''

from pages.Homepage import Homepage
from pages.Register_page import Register
from utilities.randon_data_utility import RandomDataUtil
from playwright.sync_api import Page,expect

def test_register_page(page):
    home_page = Homepage(page)
    register_page = Register(page)
    util_data = RandomDataUtil()

    #from the homepage click on register button
    home_page.click_my_account()
    home_page.click_register()
    expect(register_page.get_header_msg()).to_be_visible()

    #from registration page
    register_page.set_first_name(util_data.get_first_name())
    register_page.set_last_name(util_data.get_last_name())
    register_page.set_email(util_data.get_email())
    register_page.set_password(util_data.get_password())
    register_page.set_privacy_policy()
    register_page.click_continue()
    register_page.get_confirmation_msg()
    expect(register_page.get_confirmation_msg()).to_be_visible()

