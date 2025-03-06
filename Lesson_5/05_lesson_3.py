from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)
try:
    driver.find_element(By.CLASS_NAME, "modal-footer").click()
except Exception as e:
    print("Не удалось закрыть модальное окно:", e)
sleep(2)
driver.quit()
