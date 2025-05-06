import platform
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = os.path.join(BASE_DIR, "data/users.csv")
CREATED_USERS = os.path.join(BASE_DIR, "data/created_user.txt")

BASE_URL = "https://stellarburgers.nomoreparties.site"

urls = {
    "/": f"{BASE_URL}/",
    "register": f"{BASE_URL}/register",
    "login": f"{BASE_URL}/login",
    "fogot-password": f"{BASE_URL}/forgot-password",
    "feed": f"{BASE_URL}/feed",
    "profile": f"{BASE_URL}/account/profile",
}

TEST_DATA_USER = {
    "created": {"name": "ars", "email": "ars@ars.ru", "password": "123456"}
}


# Меняем параметр на  Chrome, FireFox
# В зависимости какой браузер нам нужен
BROWSER = 'Chrome'

# определяет платформу на которой был произведен запуск тестов
# Windows, Linux, Darwin
OS = platform.system()

TIME_MAX = 10

EMAILS = ["@yandex.ru", "@mail.ru", "@gmail.com"]
