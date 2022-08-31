import os

from selene.support.shared import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope='function', autouse=True)
# def browser_management():
#     browser.config.browser_name = 'chrome'
#     browser.config.base_url = 'https://demoqa.com/'
#     browser.config.hold_browser_open = True


@pytest.fixture(scope='function', autouse=True)
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/'
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "99.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.base_url = 'https://demoqa.com/'
    browser.config.hold_browser_open = True
