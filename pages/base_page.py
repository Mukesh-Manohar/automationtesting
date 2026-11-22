from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def by_testid(test_id):
    return (By.CSS_SELECTOR, f'[data-testid="{test_id}"]')

class BasePage:
    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self, path=""):
        self.driver.get(self.base_url + path)

    def find(self, locator):
        ele = self.wait.until(EC.visibility_of_element_located(locator))
        return ele

    def click(self, locator):
        ele = self.wait.until(EC.element_to_be_clickable(locator))
        ele.click()

    def type(self, locator, text):
        ele = self.find(locator)
        ele.clear()
        ele.send_keys(text)

    def text_of(self, locator):
        ele = self.find(locator)
        return ele.text

    def is_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0
        