from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID,"username")
username.send_keys("tomsmith")
password = driver.find_element(By.ID,"password")
password.send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()
