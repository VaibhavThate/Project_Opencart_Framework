'''
test case
============
validate the quantity field by entering the quantity
validate the add to cart button
validate success toast message
validate item button
validate view cart inside item button window
'''

from pages.product_page import ProductPage
from pages.Homepage import Homepage
from pages.Login_page import Login
from pages.search_result_page import SRP_page
from config import Config
from playwright.sync_api import expect
import pytest


def test_product_page(page):
    home_page = Homepage(page)
    login_page = Login(page)
    srp_page = SRP_page(page)
    product_page = ProductPage(page)

    #from homepage click on myaccount and go to login
    home_page.click_my_account()
    home_page.click_login()

    #from login page entering the valid credential and login
    login_page.enter_email(Config.email)
    login_page.enter_password(Config.password)
    login_page.click_login()
    expect(login_page.check_successful_login()).to_be_visible()

    #from account info page enter the product name and search click
    home_page.enter_search_box(Config.product_name[0])
    home_page.click_search()
    expect(srp_page.product_list.first).to_be_visible()

    #from the srp page click on the product
    srp_page.click_product(Config.product_name[0])

    #from the product page enter quantity and click on add to cart button
    product_page.enter_qty_product(Config.qty)
    product_page.click_add_to_cart()

    #checking the toast message
    product_page.success_toast_msg()
    expect(product_page.added_msg).to_be_visible()


    #from same product page click on the item button and from window click on view cart
    product_page.click_item_homepage_button()
    product_page.click_view_cart()
    expect(page).to_have_url("http://localhost/opencart/index.php?route=checkout/cart&language=en-gb")


