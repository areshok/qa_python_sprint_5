import time
import pytest

from .settings import urls, TEST_DATA_USER
from .utils import get_browser, browser_options
from .locators import LoginPage


@pytest.fixture(scope='class')
def browser_cls():
    "Новый браузер для класса"
    browser = get_browser(browser_options())
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def browser_def():
    "Новый браузер для каждой функции"
    browser = get_browser(browser_options())
    yield browser
    browser.quit()


@pytest.fixture(scope='class')
def browser_user_auth():
    "Новый бразуер для класса с аутентифицированным пользователем"
    browser = get_browser(browser_options())
    browser.get(urls["login"])
    email = browser.find_element(*LoginPage.email)
    password = browser.find_element(*LoginPage.password)
    buttom = browser.find_element(*LoginPage.enter)
    email.send_keys(TEST_DATA_USER['created']['email'])
    password.send_keys(TEST_DATA_USER['created']['password'])
    time.sleep(1)
    buttom.click()
    yield browser
    browser.quit()
