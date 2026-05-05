'''
test case
===========
validate the product name available on the cart
validate the qty available of the product on the cart
validate the total price of the product
validate the checkout button
'''

from pages.Homepage import Homepage
from pages.search_result_page import SRP_page
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from config import Config
import pytest
from playwright.sync_api import expect

@pytest.mark.sanity
@pytest.mark.regression
def test_shopping_cart(page):
    home_page = Homepage(page)
    srp_page = SRP_page(page)
    product_page = ProductPage(page)
    shopping_cart_page = ShoppingCartPage(page)

    #from home page enter the product name and click on the search button
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
    page.wait_for_timeout(5000)

    #from same product page click on the item button and from window click on view cart
    product_page.click_item_homepage_button()
    product_page.click_view_cart()
    expect(page).to_have_url("http://localhost/opencart/index.php?route=checkout/cart&language=en-gb")

    #from the cart page check the product name available on cart page
    product_list = shopping_cart_page.get_product_name(Config.product_name[0])
    assert Config.product_name[0] in product_list,(
        f"product {Config.product_name[0]} not found in cart"
        f"Actual : {product_list}"
    )

    #from the cart page check the quantity same as entered
    qty_list = shopping_cart_page.check_added_qty(Config.qty)
    assert Config.qty in qty_list, (
        f"quantity {Config.qty} not found in cart"
        f"Actual: {qty_list}"
    )

    # total price show exact price on cart page
    total = shopping_cart_page.check_total_price(Config.total_price[0])
    assert total == Config.total_price[0], (
        f" total mismatch expected: {Config.total_price[0]}"
        f" Actual is : {total}"
    )



