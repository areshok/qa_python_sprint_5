from ..utilits.utils import (
    generate_user_data, write_file_create_user, wait_click, wait_element)
from ..settings import urls
from ..utilits.locators import RegistrationPage, LoginPage


class TestRegistrationUser:
    "Тест кейс регистрации пользователя"

    def test_correct_registation_user(self, browser_def):
        """
        тест: проверка регистрации пользователя с валидными данными.
        """
        browser_def.get(urls["register"])
        name = browser_def.find_element(*RegistrationPage.name)
        email = browser_def.find_element(*RegistrationPage.email)
        password = browser_def.find_element(*RegistrationPage.password)
        user = generate_user_data()
        name.send_keys(user['username'])
        email.send_keys(user['email'])
        password.send_keys(user['password'])
        wait_click(browser_def, RegistrationPage.register)
        wait_element(browser_def, LoginPage.recover_password)
        write_file_create_user(**user)
        current_url = browser_def.current_url
        assert current_url == urls['login']

    def test_uncorrect_password_5_symbol_registration_user(self, browser_def):
        """
        тест: проверка получение ошибки регистрации пользователя
        с паролем из 5 символов.
        """
        browser_def.get(urls["register"])
        user = generate_user_data()
        user['password'] = "12345"
        name = browser_def.find_element(*RegistrationPage.name)
        email = browser_def.find_element(*RegistrationPage.email)
        password = browser_def.find_element(*RegistrationPage.password)
        name.send_keys(user["username"])
        email.send_keys(user["email"])
        password.send_keys(user["password"])
        wait_click(browser_def, RegistrationPage.register)
        error = browser_def.find_element(*RegistrationPage.err_password)
        assert error.text == RegistrationPage.err_password_text
