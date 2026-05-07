'''
test case
===============
Validate the searched product same available on srp page
Validate the product count available on srp page
Validate the product name available on srp page

'''

from pages.search_result_page import SRP_page
from pages.Homepage import Homepage
from config import Config
from playwright.sync_api import expect
import pytest

def test_srp_page(page):
    home_page = Homepage(page)
    srp_page = SRP_page(page)

    #click on the search box and filling the product name
    home_page.enter_search_box(Config.product_name[0])

    #click on the search
    home_page.click_search()
    expect(srp_page.product_list.first).to_be_visible()

    #check the searched product name avilable on srp page
    srp_page.header_text(Config.product_name[0])

    #check the product count on srp page availble
    srp_page.product_count()

    #check the product list available on the srp page
    srp_page.product_name()
