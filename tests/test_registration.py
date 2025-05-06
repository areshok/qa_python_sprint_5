
from selenium.common.exceptions import NoSuchElementException

from ..utils import (
    generate_user_data, write_file_create_user, clear_field, wait_click)
from ..settings import urls, TEST_DATA_USER
from ..locators import RegistrationPage


class TestRegistrationUser:
    "Тест кейс регистрации пользователя"

    def test_correct_registation_user(self, browser_def):
        """
        тест: проверка регистрации пользователя с валидными данными.
        """
        user_data = {
            "username": TEST_DATA_USER["created"]['name'],
            "email": TEST_DATA_USER["created"]['email'],
            "password": TEST_DATA_USER["created"]['password']
        }
        browser_def.get(urls["register"])

        name = browser_def.find_element(*RegistrationPage.name)
        email = browser_def.find_element(*RegistrationPage.email)
        password = browser_def.find_element(*RegistrationPage.password)

        while True:
            clear_field(name)
            clear_field(email)
            clear_field(password)
            name.send_keys(user_data['username'])
            email.send_keys(user_data['email'])
            password.send_keys(user_data['password'])
            wait_click(browser_def, RegistrationPage.register)
            try:
                browser_def.find_element(*RegistrationPage.err_already_there)
                user_data = generate_user_data()
            except NoSuchElementException:
                break
        write_file_create_user(
            user_data['username'], user_data['email'], user_data['password'])
        current_url = browser_def.current_url
        assert current_url == urls['login']

    def test_uncorrect_password_5_symbol_registration_user(self, browser_def):
        """
        тест: проверка получение ошибки регистрации пользователя
        с паролем из 5 символов.
        """
        browser_def.get(urls["register"])
        name = browser_def.find_element(*RegistrationPage.name)
        email = browser_def.find_element(*RegistrationPage.email)
        password = browser_def.find_element(*RegistrationPage.password)
        name.send_keys(TEST_DATA_USER["uncorrect"]["name"])
        email.send_keys(TEST_DATA_USER["uncorrect"]["email"])
        password.send_keys(TEST_DATA_USER["uncorrect"]["password"])
        wait_click(browser_def, RegistrationPage.register)
        error = browser_def.find_element(*RegistrationPage.err_password)
        assert error.text == 'Некорректный пароль'
