from selenium.webdriver.common.by import By

from ..settings import urls
from ..locators import Сonstructor


class TestConstuctor:
    "Тест кейс констуктора бургера"

    def test_constructor_selection(self, browser_cls):
        "тест: проверка перехода к разделам"
        browser_cls.get(urls['/'])

        buttons = [
            browser_cls.find_element(*Сonstructor.breads),
            browser_cls.find_element(*Сonstructor.sauces),
            browser_cls.find_element(*Сonstructor.toppings),
        ]

        for button in buttons[::-1]:
            button.click()
            update_parent = button.find_element(By.XPATH, "./..")
            assert 'current' in update_parent.get_attribute("class")
