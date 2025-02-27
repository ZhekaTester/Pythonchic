from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

click_count = 0
for _ in range(5):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]").click()
    click_count += 1

print("Количество кликов:", click_count)

sleep(5)






