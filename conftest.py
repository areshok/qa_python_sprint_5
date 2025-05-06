import pytest

from .settings import urls, TEST_DATA_USER
from .utilits.utils import get_browser, browser_options, wait_click
from .utilits.locators import LoginPage


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
    email.send_keys(TEST_DATA_USER['created']['email'])
    password.send_keys(TEST_DATA_USER['created']['password'])
    wait_click(browser, LoginPage.enter)
    yield browser
    browser.quit()
