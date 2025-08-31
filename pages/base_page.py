import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Поиск элемента')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait_for_element(locator).text.strip()

    @allure.step('Ввод текста')
    def send_keys(self, locator, text, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Дождаться видимости элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Дождаться присутствия элемента в DOM')
    def wait_for_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Дождаться скрытия элемента')
    def wait_hide_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Дождаться изменения текста в элементе')
    def wait_change_element(self, locator, element_text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: (el := d.find_element(*locator)) and el.text != element_text and el.text
        )

    @allure.step('Дождаться загрузки всех элементов по локатору')
    def wait_load_all_elements(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step('Переход по ссылке')
    def switch_new_page(self, url):
        self.driver.get(url)

    @allure.step('Получить URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)
