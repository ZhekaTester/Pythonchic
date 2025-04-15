import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@allure.title("Тест на проверку работы калькулятора")
@allure.feature("Calculator")
@allure.description("Проверка работы калькулятора, сравнение полученного результата вычисления с действительным значением")
@allure.severity("critical")
def test_02_calc():
    with allure.step("Открыть страницу калькулятора по ссылке"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    """Создание объекта страницы калькулятора"""
    calculator_page = CalculatorPage(driver)
    with allure.step("Установить задержку в поле 45 секунд"):
        calculator_page.set_delay("45")
    with allure.step("Ввести 7 + 8 ="):
        calculator_page.click_button()
    """Проверка результата"""
    result = calculator_page.get_result("15")
    assert result == "15"
    """Закрытие браузера"""
    driver.quit()
