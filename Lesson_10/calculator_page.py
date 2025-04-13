import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Этот класс представляет страницу калькулятора"""


class CalculatorPage:
    @allure.step("Открыть в браузере страницу калькулятора")
    def __init__(self, driver: str):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    @allure.step("Установить задержку")
    def set_delay(self, delay: int):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажать заданные кнопки на калькуляторе")
    def click_button(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Получить результат операции с ожиданием")
    def get_result(self, expected_result) -> int:
        self.result_screen = (By.CLASS_NAME, "screen")
        wait = WebDriverWait(self.driver, 46)
        wait.until(EC.text_to_be_present_in_element(self.result_screen, expected_result))
        return self.driver.find_element(*self.result_screen).text
