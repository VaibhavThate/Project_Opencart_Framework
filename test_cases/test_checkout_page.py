'''
test case
===========
validate all the mandatory field
validate the errors shipping and payment button
validate product total price
'''

from pages.checkout_page import CheckoutPage
from pages.Homepage import Homepage
from pages.Login_page import Login
from pages.search_result_page import SRP_page
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from config import Config
from playwright.sync_api import expect,Page
from utilities.data_reader import read_json_data
import pytest
test_data = read_json_data("test_data/checkout_data.json")

@pytest.mark.sanity
@pytest.mark.parametrize("data", test_data)
def test_checkout_page(page,data):
    home_page = Homepage(page)
    login_page = Login(page)
    srp_page = SRP_page(page)
    product_page = ProductPage(page)
    cart_page = ShoppingCartPage(page)
    check_out = CheckoutPage(page)

    #from the homepage login
    home_page.click_my_account()
    home_page.click_login()

    #from login fill the login
    expect(login_page.check_login_header()).to_be_visible()

    login_page.enter_email(Config.email)
    login_page.enter_password(Config.password)
    login_page.click_login()

    expect(login_page.check_successful_login()).to_be_visible()

    #from home page click on the item section
    home_page.clear_item_cart(page)

    home_page.click_item_cart()
    expect(home_page.check_empty_cart_msg()).to_contain_text("Your shopping cart is empty!")

    for i in range(0,2):
        home_page.enter_search_box(Config.product_name[i])
        home_page.click_search()

        expect(srp_page.product_list.first).to_be_visible()

        srp_page.product_count()
        srp_page.product_name()
        srp_page.click_product(Config.product_name[i])

        product_page.enter_qty_product(Config.qty)
        product_page.click_add_to_cart()
        product_page.success_toast_msg()
        page.wait_for_timeout(5000)
        product_page.click_item_homepage_button()
        product_page.click_view_cart()

        cart_page.get_product_name(Config.product_name[i])
        cart_page.check_added_qty(Config.qty)

    page.wait_for_timeout(1000)
    cart_page.click_checkout_button()

    check_out.check_header_checkout()
    check_out.enter_fname()
    check_out.enter_lname()
    check_out.enter_address_checkout()
    check_out.enter_city()
    check_out.enter_post_code()
    check_out.select_country_checkout()
    check_out.select_state_checkout()
    check_out.click_shipping_btn()
    expect(check_out.error_msg_shipping()).to_contain_text("Shipping address required!")
    check_out.click_payment_btn()
    expect(check_out.error_msg_payment()).to_contain_text("Shipping method required!")

    check_out.add_comment_box()
    check_out.check_product_price(data["product_1_price"],data["product_2_price"])







