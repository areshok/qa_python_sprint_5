
import time

from ..settings import urls, TEST_DATA_USER
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from ..utils import generate_user_data, write_file_create_user


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
        name, email, password = browser_def.find_elements(
            By.CLASS_NAME, "text.input__textfield.text_type_main-default")
        form_button = browser_def.find_element(
            By.XPATH, ".//button[text()='Зарегистрироваться']")

        while True:
            name.clear()
            email.clear()
            password.clear()
            name.send_keys(user_data['username'])
            email.send_keys(user_data['email'])
            password.send_keys(user_data['password'])
            form_button.click()
            time.sleep(1)
            try:
                browser_def.find_element(
                    By.CLASS_NAME, "input__error.text_type_main-default")
                user_data = generate_user_data()
            except NoSuchElementException:
                break
        time.sleep(1)
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
        name, email, password = browser_def.find_elements(
            By.CLASS_NAME, "text.input__textfield.text_type_main-default")

        name.send_keys(TEST_DATA_USER["uncorrect"]["name"])
        email.send_keys(TEST_DATA_USER["uncorrect"]["email"])
        password.send_keys(TEST_DATA_USER["uncorrect"]["password"])
        form_button = browser_def.find_element(
            By.XPATH, ".//button[text()='Зарегистрироваться']")
        form_button.click()
        error = browser_def.find_element(
            By.CLASS_NAME, 'input__error.text_type_main-default')
        assert error.text == 'Некорректный пароль'
