from pages.base_page import BasePage, by_testid

class LoginPage(BasePage):
    EMAIL = by_testid("login-email")
    PASSWORD = by_testid("login-password")
    LOGIN_BTN = by_testid("login-submit")
    ERROR_TEXT = by_testid("error-message")
    SUCCESS_TEXT = by_testid("success-message")

    def open_page(self):
        self.open("/login")

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def error_text(self):
        return self.text_of(self.ERROR_TEXT)

    def success_text(self):
        return self.text_of(self.SUCCESS_TEXT)