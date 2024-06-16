from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/registration2.html")

    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Y")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("L")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("yl@gmail.com")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
