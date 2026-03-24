import pytest
from playwright.sync_api import expect
import time
from pages.login_page import LoginPage
import utils


"""
This test verifies that a user can successfully log in with valid 
credentials.
It uses parameterization to test multiple sets of valid credentials 
from a CSV file.
"""


@pytest.mark.parametrize("users_list", utils.get_csv_data("test_data\\valid_users.csv"))
def test_login_success(page, users_list):
    valid_username = str(users_list[0])
    valid_password = str(users_list[1])
    login = LoginPage(page)
    login.login(valid_username, valid_password)
    assert "dashboard" in page.url
    expect(page.get_by_test_id("user-display")).to_contain_text(f"Hello, {valid_username}")
    login.logout()
    time.sleep(0.5)


"""
This test verifies that the login page displays an error message
 when invalid credentials are entered.
It uses parameterization to test multiple sets of invalid 
credentials from a CSV file.
"""


@pytest.mark.parametrize("invalid_users_list", utils.get_csv_data("test_data\\invalid_users.csv"))
def test_invalid_login(page, invalid_users_list):
    invalid_username = str(invalid_users_list[0])
    invalid_password = str(invalid_users_list[1])
    login = LoginPage(page)
    login.login(invalid_username, invalid_password)
    if "dashboard" in page.url:
        login.logout()
    expect(page.get_by_test_id("login-error")).to_be_visible(timeout=2000)
    time.sleep(0.5)


"""
This test verifies that the login page displays an error message 
when the username or password fields are left empty.
It uses parameterization to test multiple combinations of 
empty fields from a CSV file.
"""


@pytest.mark.parametrize("empty_users_list", utils.get_csv_data("test_data\\empty_fields_login.csv"))
def test_login_empty_fields(page, empty_users_list):
    empty_username = str(empty_users_list[0])
    empty_password = str(empty_users_list[1])
    login = LoginPage(page)
    login.login(empty_username, empty_password)
    expect(page.get_by_test_id("login-error"), "Please enter username and password").to_be_visible(timeout=2000)
    time.sleep(0.5)
