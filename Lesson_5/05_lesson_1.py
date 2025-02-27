from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()

sleep(5)