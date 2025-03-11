import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping_flow(browser):
    browser.get("https://www.saucedemo.com/")

    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        item = browser.find_element(By.XPATH, f"//div[text()='{item_name}']")
        add_to_cart_button = item.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']//button")
        add_to_cart_button.click()

    cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    checkout_button = browser.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_field = browser.find_element(By.ID, "first-name")
    last_name_field = browser.find_element(By.ID, "last-name")
    postal_code_field = browser.find_element(By.ID, "postal-code")
    continue_button = browser.find_element(By.ID, "continue")

    first_name_field.send_keys("John")
    last_name_field.send_keys("Doe")
    postal_code_field.send_keys("12345")
    continue_button.click()

    total_amount = browser.find_element(By.CLASS_NAME, "summary_total_label").text

    assert total_amount == "Total: $58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: {total_amount}"
