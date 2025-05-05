import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from ..settings import urls


class TestRedirectLogIn:
    "Тест кейс проверки перехода на url входа в аккаунт"

    def test_redirect_log_in_on_home_page(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку войти на главной странице
        """
        browser_cls.get(urls['/'])
        time.sleep(1)
        loigin_buttom = browser_cls.find_element(
            By.XPATH, ".//button[text()='Войти в аккаунт']")
        loigin_buttom.click()
        current_url = browser_cls.current_url
        assert current_url == urls['login']
        try:
            browser_cls.find_element(By.CLASS_NAME, 'Auth_form__3qKeq.mb-20')
        except NoSuchElementException:
            assert False, "Форма входа не найдена"

    def test_redirect_log_in_button_personal_account(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку личный кабинет
        """
        browser_cls.get(urls['/'])
        time.sleep(1)
        loigin_buttom = browser_cls.find_element(
            By.XPATH, 'html/body/div/div/header/nav/a')
        loigin_buttom.click()
        current_url = browser_cls.current_url
        assert current_url == urls['login']
        try:
            browser_cls.find_element(By.CLASS_NAME, 'Auth_form__3qKeq.mb-20')
        except NoSuchElementException:
            assert False, "Форма входа не найдена"

    def test_redirect_log_in_button_registration_form(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажанития на кнопку в форме регистрации
        """
        browser_cls.get(urls["register"])
        time.sleep(1)
        loigin_buttom = browser_cls.find_element(
            By.XPATH, ".//a[text()='Войти']")
        href = loigin_buttom.get_attribute('href')
        assert href == urls['login']

        loigin_buttom.click()
        current_url = browser_cls.current_url
        assert current_url == urls['login']
        try:
            browser_cls.find_element(By.CLASS_NAME, 'Auth_form__3qKeq.mb-20')
        except NoSuchElementException:
            assert False, "Форма входа не найдена"

    def test_redirect_log_in_on_buttom_password_fogot(self, browser_cls):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку на странице восстановление пароля
        """
        browser_cls.get(urls['fogot-password'])
        time.sleep(1)
        login_button = browser_cls.find_element(
            By.XPATH, ".//a[text()='Войти']")
        login_button.click()
        current_url = browser_cls.current_url
        assert current_url == urls['login']
        try:
            browser_cls.find_element(By.CLASS_NAME, 'Auth_form__3qKeq.mb-20')
        except NoSuchElementException:
            assert False, "Форма входа не найдена"
