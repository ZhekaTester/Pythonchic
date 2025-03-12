from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome(service =ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()

delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_input.clear()
delay_input.send_keys("45")

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()


equals_button = WebDriverWait(driver, 46).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
)

driver.execute_script("arguments[0].scrollIntoView(true);", equals_button)

driver.execute_script("arguments[0].click();", equals_button)

result = WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)
assert result, "Результат не равен 15"

driver.quit()
