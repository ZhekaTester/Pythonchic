from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.XPATH, "//input")
search_input.send_keys(1000)
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys(999)





