import pytest
from pages.register_page import RegisterPage
from pages.login_page import LoginPage

@pytest.mark.regression
def test_wrong_password(driver, base_url, unique_email):
    login_page = LoginPage(driver, base_url)
    register_page = RegisterPage(driver, base_url)
    register_page.open_page()
    register_page.register(unique_email, "python")
    assert login_page.success_text() == "Account created. Please log in."
    login_page.login(unique_email, "abcd")
    assert login_page.error_text() == "Invalid email or password"

@pytest.mark.regression
def test_wrong_email(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open_page()
    login_page.login("wrong@gmail.com", "password")
    assert login_page.error_text() == "Invalid email or password"    