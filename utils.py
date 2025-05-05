import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .settings import DIAPASON_END, DIAPASON_START, TEST_DATA_USER, BROWSER


def generate_user_data():
    "Генерация данных пользователя"
    numb = random.randint(DIAPASON_START, DIAPASON_END)
    name_template = TEST_DATA_USER["correct"]["name"]
    username = f'{name_template}{numb}'
    email = f'{name_template}{numb}@{name_template}.ru'
    password = f'{TEST_DATA_USER["correct"]["password"]}{numb}'
    return {"username": username, "email": email, "password": password}


def write_file_create_user(username, email, password):
    "Запись в файл пользователя"
    with open('created_user.txt', mode='a', encoding='utf-8') as file:
        file.write(f'{username} - {email} - {password} \n')


def browser_options():
    "Опции браузера"
    if BROWSER == "Chrome":
        options = Options()
        options.add_argument("--disable-cache")
        options.add_argument("--incognito")
    if BROWSER == "FireFox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--private")
    return options


def get_browser(option=None):
    "Браузер"
    if BROWSER == "Chrome":
        return webdriver.Chrome(options=option)
    if BROWSER == "FireFox":
        return webdriver.Firefox(options=option)
