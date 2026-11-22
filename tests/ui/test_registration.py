import pytest

from pages.login_page import LoginPage
from pages.register_page import RegisterPage

@pytest.mark.regression
def test_successful_registration_with_valid_credentials(driver, base_url,unique_email):
    register_page = RegisterPage(driver, base_url)
    register_page.open_page()
    register_page.register(unique_email, "python")
    login_page = LoginPage(driver, base_url)
    assert login_page.success_text() == "Account created. Please log in."

@pytest.mark.regression
def test_incorrect_registration_with_short_password(driver, base_url,unique_email):
    register_page = RegisterPage(driver, base_url)
    register_page.open_page()
    register_page.register(unique_email, "pyt")
    assert register_page.error_text() == "Valid email and a password of 6+ characters are required"

@pytest.mark.regression
def test_registration_with_existing_email(driver, base_url,unique_email):
    register_page = RegisterPage(driver, base_url)
    login_page = LoginPage(driver, base_url)
    register_page.open_page()
    register_page.register(unique_email, "python")
    assert login_page.success_text() == "Account created. Please log in."
    register_page.open_page()
    register_page.register(unique_email, "python")
    assert register_page.error_text() == "Email already registered"    