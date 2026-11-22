import pytest

from pages.login_page import LoginPage

@pytest.mark.regression
def test_wrong_password(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open_page()
    login_page.login("abcd@gmail.com", "abcd")
    assert login_page.error_text() == "Invalid email or password"

@pytest.mark.regression
def test_wrong_email(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open_page()
    login_page.login("wrong@gmail.com", "password")
    assert login_page.error_text() == "Invalid email or password"    