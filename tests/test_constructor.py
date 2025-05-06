from selenium.webdriver.common.by import By

from ..settings import urls
from ..locators import Сonstructor
from ..utils import wait_click


class TestConstuctor:
    "Тест кейс констуктора бургера"

    def test_constructor_selection(self, browser_cls):
        "тест: проверка перехода к разделам"
        browser_cls.get(urls['/'])

        buttons = [
            Сonstructor.breads,
            Сonstructor.sauces,
            Сonstructor.toppings,
        ]

        for button in buttons[::-1]:
            button = wait_click(browser_cls, button)
            update_parent = button.find_element(By.XPATH, "./..")
            assert 'current' in update_parent.get_attribute("class")
