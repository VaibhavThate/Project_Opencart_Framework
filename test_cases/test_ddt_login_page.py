'''
using the data from json,excel,cssv file drive the testing
test cases
validate the login with valid credential
validate the login with invalid credential
'''
from pages.Homepage import Homepage
from pages.Login_page import Login
from utilities.data_reader import read_json_data
from utilities.data_reader import read_csv_file
from utilities.data_reader import read_excel_file
from playwright.sync_api import expect, Page
import pytest

test_data = read_json_data("test_data/logindata.json")
test_data_1 = read_csv_file("test_data/logindata.csv")
test_data_2 = read_excel_file("test_data/logindata.xlsx")

@pytest.mark.regression
@pytest.mark.parametrize("data", test_data)
def test_login_json(page,data):
    home_page = Homepage(page)
    login_page = Login(page)

    home_page.click_my_account()
    home_page.click_login()
    expect(login_page.check_login_header()).to_be_visible()

    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_login()

    #check login successful or error message with jason data
    if data["expected"] == "success":
        login_page.check_successful_login()
    else:
        login_page.error_invalid_login()

@pytest.mark.parametrize("data", test_data_1)
def test_login_csv(page, data):
    home_page = Homepage(page)
    login_page = Login(page)

    home_page.click_my_account()
    home_page.click_login()
    expect(login_page.check_login_header()).to_be_visible()

    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_login()

    # check login successful or error message with jason data
    if data["expected"] == "success":
        login_page.check_successful_login()
    else:
        login_page.error_invalid_login()

@pytest.mark.parametrize("data", test_data_2)
def test_login_excel(page,data):
    home_page = Homepage(page)
    login_page = Login(page)

    home_page.click_my_account()
    home_page.click_login()
    expect(login_page.check_login_header()).to_be_visible()

    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_login()

    # check login successful or error message with jason data
    if data["expected"] == "success":
        login_page.check_successful_login()
    else:
        login_page.error_invalid_login()


