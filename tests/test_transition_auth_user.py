import time

from ..settings import urls
from ..utilits.locators import Header, AccountPage
from ..utilits.utils import wait_click


class TestTrasitionAuthUser:
    "Тест кейс перехода по ссылкам авторизированного пользователя"

    # для ревьюера
    # нумерацию на тестах поставил чтоб проверка выхода была последней
    # без нумерации тестов, они запускаются в лексикографическом порядке

    def test_1_transition_to_personal_account(self, browser_user_auth):
        """
        тест: переход в личный кабинет с главной страницы
        """
        wait_click(browser_user_auth, Header.personal_account)
        current_url = browser_user_auth.current_url
        assert current_url in urls['profile']

    def test_2_transition_personal_account_to_constructor_button(
            self, browser_user_auth):
        """
        Переход из личного кабинета на конструктор бургера
        нажатием на кнопку конструктор
        """
        wait_click(browser_user_auth, Header.personal_account)
        wait_click(browser_user_auth, Header.constuctor)
        current_url = browser_user_auth.current_url
        assert current_url == urls['/']

    def test_3_transition_personal_account_to_logo_button(
            self, browser_user_auth):
        """
        тест: переход из личного кабинета на главную страницу
        нажанием на логотип
        """
        wait_click(browser_user_auth, Header.personal_account)
        wait_click(browser_user_auth, Header.logo)
        current_url = browser_user_auth.current_url
        assert current_url == urls['/']

    def test_4_transition_personal_account_main_url(self, browser_user_auth):
        """
        тест: переход из личного кабинета на домашнюю страницу
        """
        wait_click(browser_user_auth, Header.personal_account)
        browser_user_auth.get(urls['/'])
        current_url = browser_user_auth.current_url
        assert current_url == urls['/']

    def test_5_exit_in_account(self, browser_user_auth):
        """
        тест: выход из учетной записи
        """
        wait_click(browser_user_auth, Header.personal_account)
        wait_click(browser_user_auth, AccountPage.exit)
        time.sleep(1)  # тут не получается отказаться от явного ожидания
        current_url = browser_user_auth.current_url
        assert current_url in urls['login']
