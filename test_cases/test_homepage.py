'''
test case
============
validate the my_account section
validate the login button
validate the register button
validate search box
validate the search button

'''
from pages.Homepage import Homepage
from config import Config
from pages.search_result_page import SRP_page
import pytest


def test_my_account(page):
    #check my_account section to click on the my_account button
    home_page = Homepage(page)
    home_page.click_my_account()

    #check login button to click login button
    home_page.click_login()


def test_register(page):
    #check register button login
    home_page = Homepage(page)
    home_page.click_my_account()
    home_page.click_register()



def test_search_box(page):
    #entering the product name into the search box
    home_page = Homepage(page)
    srp_page = SRP_page(page)
    home_page.enter_search_box(Config.product_name[0])
    home_page.click_search()

    #check the same searched product name displayed on srp page
    srp_page.header_text(Config.product_name[0])






