import time

from ..settings import urls
from ..locators import Header, AccountPage


class TestTrasitionAuthUser:
    "Тест кейс перехода по ссылкам авторизированного пользователя"

    # для ревьюера
    # нумерацию на тестах поставил чтоб проверка выхода была последней
    # без нумерации тестов, они запускаются в лексикографическом порядке

    def test_1_transition_to_personal_account(self, browser_user_auth):
        """
        тест: переход в личный кабинет с главной страницы
        """
        button = browser_user_auth.find_element(*Header.personal_account)
        time.sleep(1)
        button.click()
        current_url = browser_user_auth.current_url
        assert current_url in urls['profile']

    def test_2_transition_personal_account_to_constructor_button(
            self, browser_user_auth):
        """
        Переход из личного кабинета на конструктор бургера
        нажатием на кнопку конструктор
        """
        button = browser_user_auth.find_element(*Header.personal_account)
        time.sleep(1)
        button.click()
        button_construct = browser_user_auth.find_element(*Header.constuctor)
        time.sleep(1)
        button_construct.click()
        current_url = browser_user_auth.current_url
        assert current_url == urls['/']

    def test_3_transition_personal_account_to_logo_button(
            self, browser_user_auth):
        """
        тест: переход из личного кабинета на главную страницу
        нажанием на логотип
        """
        button = browser_user_auth.find_element(*Header.personal_account)
        time.sleep(1)
        button.click()
        logo_button = browser_user_auth.find_element(*Header.logo)
        time.sleep(1)
        logo_button.click()
        current_url = browser_user_auth.current_url
        assert current_url == urls['/']

    def test_4_transition_personal_account_main_url(self, browser_user_auth):
        """
        тест: переход из личного кабинета на домашнюю страницу
        """
        button = browser_user_auth.find_element(*Header.personal_account)
        time.sleep(1)
        button.click()
        browser_user_auth.get(urls['/'])
        current_url = browser_user_auth.current_url
        assert current_url == urls['/']

    def test_5_exit_in_account(self, browser_user_auth):
        """
        тест: выход из учетной записи
        """
        button = browser_user_auth.find_element(*Header.personal_account)
        time.sleep(1)
        button.click()
        time.sleep(1)
        exit_button = browser_user_auth.find_element(*AccountPage.exit)
        time.sleep(1)
        exit_button.click()
        time.sleep(1)
        current_url = browser_user_auth.current_url
        assert current_url in urls['login']
