from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)
driver.find_element(By.CLASS_NAME, "modal-footer").click()

sleep(5)

