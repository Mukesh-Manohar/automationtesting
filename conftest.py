import json
import os
import uuid
import pytest
from utils.driver_factory import launch_browser


def load_config():
    env = os.getenv("TEST_ENV", "local")
    file_path = "config/" + env + ".json"
    with open(file_path) as file:
        return json.load(file)

CONFIG = load_config()

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true")

@pytest.fixture
def base_url():
    return CONFIG["base_url"]

@pytest.fixture
def unique_email():
    return (f"ABC{uuid.uuid4().hex[:8]}@gmail.com")

@pytest.fixture
def driver(request):
    headless = CONFIG["headless"]
    if request.config.getoption("--headless"):
        headless = True
    driver = launch_browser(CONFIG["browser"], headless)

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_failed = report.when == "call" and report.failed
    uses_browser = "driver" in item.funcargs

    if test_failed and uses_browser:
        browser = item.funcargs["driver"]
        image = browser.get_screenshot_as_base64()
        html_plugin = item.config.pluginmanager.getplugin("html")
        report.extras = [html_plugin.extras.image(image)]