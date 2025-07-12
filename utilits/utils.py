import time
import csv
import string
from random import randint, choice

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    ElementClickInterceptedException, NoSuchElementException)
from selenium.webdriver.common.keys import Keys

from ..settings import (
    BROWSER, OS, TIME_MAX,
    EMAILS, USERS_FILE, CREATED_USERS)


def generate_user_data():
    "Генерация данных пользователя"
    firs_last_name = []
    with open(USERS_FILE, mode="r", encoding="utf-8") as file:
        read = csv.reader(file, delimiter=";")
        for row in read:
            firs_last_name.append(row)
    diapason = len(firs_last_name) - 1
    firs_name = firs_last_name[randint(0, diapason)][0].lower()
    last_name = firs_last_name[randint(0, diapason)][1].lower()
    username = f"{firs_name}_{last_name}"
    email = f"{last_name}{firs_name}{choice(EMAILS)}"
    password = ""
    len_password = randint(6, 20)
    for _ in range(len_password):
        letter = choice(string.ascii_letters)
        digit = choice(string.digits)
        if randint(0, 300) % 2 == 0:
            password += letter
        else:
            password += digit
    return {"username": username, "email": email, "password": password}


def write_file_create_user(username, email, password):
    "Запись в файл пользователя"
    with open(CREATED_USERS, mode='a', encoding='utf-8') as file:
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


def clear_field(field):
    "Очиска поля в зависимости от OS"
    if OS == "Windows" or OS == "Linux":
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
    if OS == "Darwin":
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.DELETE)


def wait_element(browser, path):
    "Ожидание элемента"
    time_start = time.time()
    while True:
        try:
            element = browser.find_element(*path)
            return element
        except NoSuchElementException as e:
            if time.time() - time_start > TIME_MAX:
                raise e
            time.sleep(0.5)


def wait_click(browser, path):
    "Ожидание нажатие на кнопку"
    time_start = time.time()
    button = wait_element(browser, path)
    while True:
        try:
            button.click()
            return button
        except ElementClickInterceptedException as e:
            if time.time() - time_start > TIME_MAX:
                raise e
            time.sleep(0.5)
