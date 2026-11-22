from pages.base_page import BasePage, by_testid


class RegisterPage(BasePage):
    EMAIL = by_testid("register-email")
    PASSWORD = by_testid("register-password")
    REGISTER_BTN = by_testid("register-submit")
    ERROR_TEXT = by_testid("error-message")

    def open_page(self):
        self.open("/register")

    def register(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.REGISTER_BTN)

    def error_text(self):
        return self.text_of(self.ERROR_TEXT)
    