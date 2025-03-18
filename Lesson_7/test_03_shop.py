from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_page import ShopPage


def test_02_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop_page = ShopPage(driver)
    shop_page.fill_form("standard_user", "secret_sauce")
    shop_page.add_products()
    shop_page.shopping_cart()
    shop_page.checkout()
    shop_page.your_information("Tatiana", "Fedoseeva", "443100")
    total_value = shop_page.total()

    assert total_value == "Total: $58.29"
    driver.quit()
