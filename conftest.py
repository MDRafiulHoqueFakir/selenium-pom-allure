import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Attach screenshot to Allure on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            allure.attach(
                drv.get_screenshot_as_png(),
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG
            )
