import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_page import ShopPage


@allure.title("Тест на проверку работы интернет-магазина")
@allure.feature("Shop")
@allure.description("Проверка работы интернет-магазина на авторизацию, добавление товаров в корзину, оформление заказа и итоговую стоимость")
@allure.severity("critical")
def test_02_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Открыть сайт интернет-магазина"):
        shop_page = ShopPage(driver)
    with allure.step("Авторизоваться на сайте"):
        shop_page.fill_form("standard_user", "secret_sauce")
    with allure.step("Добавить товары в корзину"):
        shop_page.add_products()
    with allure.step("Перейти в корзину"):
        shop_page.shopping_cart()
    with allure.step("Нажать кнопку checkout"):
        shop_page.checkout()
    with allure.step("Заполнить своими данными страницу оформления заказа"):
        shop_page.your_information("Tatiana", "Fedoseeva", "443100")
    with allure.step("Получить итоговую стоимость"):
        total_value = shop_page.total()
    with allure.step("Проверить итоговую стоисомть"):
        assert total_value == "Total: $58.29"
    """Закрытие браузера"""
    driver.quit()
    