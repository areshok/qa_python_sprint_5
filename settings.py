import platform

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
    "correct": {"name": "ars", "email": "ars@ars.ru", "password": "123456"},
    "uncorrect": {"name": "2ars", "email": "2ars@ars.ru", "password": "12345"},
    "created": {"name": "ars", "email": "ars@ars.ru", "password": "123456"}
}


DIAPASON_START = 0
DIAPASON_END = 100

# Меняем параметр на  Chrome, FireFox
# В зависимости какой браузер нам нужен
BROWSER = 'FireFox'

# определяет платформу на которой был произведен запуск тестов
# Windows, Linux, Darwin
OS = platform.system()
