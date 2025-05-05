from selenium.webdriver.common.by import By

from ..settings import urls


class TestConstuctor:
    "Тест кейс констуктора бургера"

    def test_constructor_selection(self, browser_cls):
        "тест: проверка перехода к разделам"
        browser_cls.get(urls['/'])
        text_buttons = []
        parents = browser_cls.find_elements(
            By.XPATH, ".//div[contains(@class, 'tab_tab__1SPyG')]")
        for parent in parents:
            child = parent.find_element(
                By.CLASS_NAME, 'text.text_type_main-default')
            text_buttons.append(child.text)
        for text in text_buttons[::-1]:
            button = browser_cls.find_element(
                By.XPATH, f".//span[text()='{text}']")
            button.click()
            update_parent = button.find_element(By.XPATH, "./..")
            assert 'current' in update_parent.get_attribute("class")
