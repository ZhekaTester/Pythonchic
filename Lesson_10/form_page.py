import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Класс описывает страницу проверки формы для заполнения"""


class FormPage:
    @allure.step("Настроить драйвер")
    def __init__(self, driver: str):
        self.driver = driver

    @allure.step("Заполнить поля формы")
    def fill_form(self, data: {}):
        for field_name, value in data.items():
            self.driver.find_element(By.NAME, field_name).send_keys(value)

    @allure.step("Нажать на кнопку отправки формы")
    def submit_form(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(submit_button)).click()

    @allure.step("Ожидать подсветки поля Zip code")
    def wait_for_zip_code(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "zip-code")))

    @allure.step("Получить цвет подсветки поля Zip code")
    def get_zip_code_color(self) -> WebElement:
        zip_code = self.driver.find_element(By.ID, "zip-code")
        return zip_code.value_of_css_property("background-color")

    @allure.step("Получить цвет подсветки остальных полей формы")
    def get_field_color(self, field_name: {}) -> WebElement:
        field = self.driver.find_element(By.CSS_SELECTOR, f"[id='{field_name}']")
        return field.value_of_css_property("background-color")
