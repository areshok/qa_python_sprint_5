from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from ..settings import urls
from ..utilits.locators import Сonstructor
from ..utilits.utils import wait_click, wait_element


class TestConstuctor:
    "Тест кейс констуктора бургера"

    def test_1_touch_toppings_buttom(self, browser_def):
        "тест: проверка конструктор нажатие на кнопку топинги"
        browser_def.get(urls['/'])
        wait_click(browser_def, Сonstructor.toppings)
        WebDriverWait(browser_def, 1).until(
            expected_conditions.presence_of_element_located(
                Сonstructor.parent_toppings))
        parent_toppings = wait_element(
            browser_def, Сonstructor.parent_toppings)
        assert 'current' in parent_toppings.get_attribute("class")

    def test_2_touch_sauces_buttom(self, browser_def):
        "тест: проверка конструктор нажатие на кнопку соусы"
        browser_def.get(urls['/'])
        wait_click(browser_def, Сonstructor.sauces)
        WebDriverWait(browser_def, 1).until(
            expected_conditions.presence_of_element_located(
                Сonstructor.parent_sauces))
        parent_souces = wait_element(browser_def, Сonstructor.parent_sauces)
        assert 'current' in parent_souces.get_attribute("class")

    def test_3_touch_breads_buttom(self, browser_def):
        "тест: проверка конструктор нажатие на кнопку булки"
        browser_def.get(urls['/'])
        wait_click(browser_def, Сonstructor.toppings)
        wait_click(browser_def, Сonstructor.breads)
        WebDriverWait(browser_def, 1).until(
            expected_conditions.presence_of_element_located(
                Сonstructor.parents_bread))
        parent_bread = wait_element(browser_def, Сonstructor.parents_bread)
        assert 'current' in parent_bread.get_attribute("class")
