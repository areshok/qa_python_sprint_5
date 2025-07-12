from ..settings import urls
from ..utilits.locators import (
    Header, HomePage, RegistrationPage,
    LoginPage, RecoveryPasswordPage)
from ..utilits.utils import wait_click, wait_element


class TestRedirectLogIn:
    "Тест кейс проверки перехода на url входа в аккаунт"

    def test_redirect_log_in_on_home_page(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку войти на главной странице
        """
        browser_cls.get(urls['/'])
        wait_click(browser_cls, HomePage.log_in)
        current_url = browser_cls.current_url
        wait_element(browser_cls, LoginPage.recover_password)
        assert current_url == urls['login']

    def test_redirect_log_in_button_personal_account(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку личный кабинет
        """
        browser_cls.get(urls['/'])
        wait_click(browser_cls, Header.personal_account)
        current_url = browser_cls.current_url
        wait_element(browser_cls, LoginPage.recover_password)
        assert current_url == urls['login']

    def test_redirect_log_in_button_registration_form(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажанития на кнопку в форме регистрации
        """
        browser_cls.get(urls["register"])
        wait_click(browser_cls, RegistrationPage.enter)
        current_url = browser_cls.current_url
        wait_element(browser_cls, LoginPage.recover_password)
        assert current_url == urls['login']

    def test_redirect_log_in_on_buttom_password_fogot(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку на странице восстановление пароля
        """
        browser_cls.get(urls['fogot-password'])
        wait_click(browser_cls, RecoveryPasswordPage.enter)
        current_url = browser_cls.current_url
        wait_element(browser_cls, LoginPage.recover_password)
        assert current_url == urls['login']
